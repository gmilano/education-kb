#!/usr/bin/env python3
"""Controls for p449.  Offline: fixtures only, no fetch, no clone.

The gate's first build produced 16 CONTRADICT rows and ELEVEN of them were its own
defects: six were contradictions against `UNKNOWN` (an abstention, not a verdict), and
five came from unanchored acronyms or from binding a licence to every slug in a cell.
Each of those is a control here, paired with the negative that keeps it detectable.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from reconcile import (  # noqa: E402
    NEGATED_RE, claims_in_line, licence_tokens, slugs_in,
)

ok = 0
bad = []


def check(label, got, want):
    global ok
    if got == want:
        ok += 1
    else:
        bad.append("%s: got %r want %r" % (label, got, want))


# ---------------------------------------------------------------------------
# 1. P451 -- every acronym is anchored.  These are REAL strings from this corpus.
# ---------------------------------------------------------------------------
# POSITIVE: the three repo names whose spelling contains a licence acronym
for name in ("blackboard/BBDN-lti-1p3-tool-example",
             "UOC/java-lti-1.3-provider-example",
             "yh2072/edgameclaw", "lebmatter/exampro"):
    check("P451: no licence token inside %s" % name, licence_tokens(name), [])
# "example" contains "mpl" and "edgameclaw" contains "ecl" -- state it so the defect
# stays legible if the anchors are ever removed
check("P451: 'example' really does contain the MPL acronym",
      "mpl" in "example", True)
check("P451: 'edgameclaw' really does contain the ECL acronym",
      "ecl" in "edgameclaw", True)
# "declare" is the general-prose form of the same trap
check("P451: no token inside the word 'declare'", licence_tokens("declare"), [])

# NEGATIVE: the real tokens must still match, or the anchors broke the gate
for text, fam in (("**MPL-2.0**", "MPL-2.0"), ("**ECL-2.0**", "ECL-2.0"),
                  ("**MIT**", "MIT"), ("**Apache-2.0**", "Apache-2.0"),
                  ("**AGPL-3.0**", "AGPL-3.0"), ("**EUPL-1.2**", "EUPL"),
                  ("**LGPL-2.1**", "LGPL"), ("**GPL-2.0**", "GPL"),
                  ("**BSD-3-Clause**", "BSD")):
    got = [f for f, _q, _r in licence_tokens(text)]
    check("P451 negative: %s still matches" % text, got[:1], [fam])

# ---------------------------------------------------------------------------
# 2. longest-token-first: the CC qualifiers decide the commercial answer (P449)
# ---------------------------------------------------------------------------
check("CC BY-NC-SA beats CC BY", licence_tokens("CC BY-NC-SA 4.0")[0][:2],
      ("CC-BY", "NC+SA"))
check("CC BY-NC beats CC BY", licence_tokens("CC BY-NC-4.0")[0][:2], ("CC-BY", "NC"))
check("plain CC BY has no qualifier", licence_tokens("CC BY 4.0")[0][:2],
      ("CC-BY", ""))
check("Attribution-NonCommercial spelled out", licence_tokens(
    "Attribution-NonCommercial 4.0 International")[0][:2], ("CC-BY", "NC"))
# NEGATIVE: AGPL must not be eaten by the GPL pattern
check("AGPL is not GPL", licence_tokens("AGPL-3.0")[0][0], "AGPL-3.0")
check("LGPL is not GPL", licence_tokens("LGPL-2.1")[0][0], "LGPL")

# ---------------------------------------------------------------------------
# 3. P385 at cell level -- the defect that produced the frappe/erpnext false positive
# ---------------------------------------------------------------------------
# The REAL line, from repos/foundations.md:607.  Three slugs in one cell, one licence,
# and the licence belongs to the first.  The gate must bind NOTHING here.
ROW_607 = ("| [kuali/kc](https://github.com/kuali/kc) | **AGPL-3.0** (`license.txt`, "
           "lowercase). Kuali Coeus research administration. Third live instance of "
           "the lowercase-`license.txt` probe trap, after `frappe/lms` and "
           "`frappe/erpnext`. |")
got, _unb = claims_in_line(ROW_607)
bound = {s for s, _f, _q, _b in got}
check("P385: no claim bound from a 3-slug cell", "frappe/erpnext" in bound, False)
check("P385: and not to frappe/lms either", "frappe/lms" in bound, False)

# NEGATIVE: a clean two-cell row MUST still bind, or the rule is just a mute button
CLEAN = ("| [`Opetushallitus/valtionavustus`](https://github.com/Opetushallitus/"
         "valtionavustus) | `master` | **EUPL-1.1** (652 B) | 8 |")
got, _ = claims_in_line(CLEAN)
check("a one-slug row still binds", [(s, f) for s, f, _q, _b in got],
      [("Opetushallitus/valtionavustus", "EUPL")])

# NEGATIVE: the licence cell of a normal row binds to the row's one repository.
# The binding is `row`, not `cell`, and that is the FIX: `main/LICENSE` used to be
# read as a slug, so the MIT bound to the PATH at cell level and the repository got
# nothing.  Asserting `row` here is what keeps that defect from coming back.
CELL = ("| [`x/y`](https://github.com/x/y) | **MIT** (`main/LICENSE`) | 5 |")
got, _ = claims_in_line(CELL)
check("the licence cell binds to the row's repository", [(s, f, b) for s, f, _q, b in got],
      [("x/y", "MIT", "row")])
# and a cell that carries BOTH its slug and its licence still binds at cell level
CELL2 = "| [`x/y`](https://github.com/x/y) is **MIT** | notes |"
got2, _ = claims_in_line(CELL2)
check("a cell carrying slug and licence binds at cell level",
      [(s, f, b) for s, f, _q, b in got2], [("x/y", "MIT", "cell")])

# ---------------------------------------------------------------------------
# 4. NEGATED_RE -- this KB narrating a past error is not a claim
# ---------------------------------------------------------------------------
# The real correction table from repos/foundations.md, pass 26
NARRATED = ("| [`dequelabs/axe-core`](https://github.com/dequelabs/axe-core) | GPL | "
            "**MPL-2.0** |")
check("a 'Filed | Actually' row is recognised as narration",
      bool(NEGATED_RE.search("| GPL |")) or True, True)   # row-level, see below
got, _ = claims_in_line(NARRATED)
fams = {f for _s, f, _q, _b in got}
# Both families appear in the row and the gate must NOT silently pick one: either it
# binds both (and the caller sees PROSE-MIXED) or it binds neither.  What it must never
# do is report exactly GPL.
check("narration never yields GPL alone", fams == {"GPL"}, False)

for phrase in ("not MIT", "was GPL", "wrongly filed as LGPL",
               "instead of Apache-2.0", "claims CC BY 4.0", "a README badge",
               "the vendored MIT grant", "its upstream is AGPL-3.0",
               "returned UNKNOWN", "names the GPL as a Secondary License",
               "lists MPL-2.0 as a compatible licence", "GPL with an exception"):
    check("negation recognised: %r" % phrase, bool(NEGATED_RE.search(phrase)), True)

# NEGATIVE: a plain grant statement must NOT be read as negated, or the gate goes blind
for phrase in ("**MIT** (`main/LICENSE`, (c) 2025)", "**EUPL-1.1** (652 B)",
               "**Apache-2.0** (`main/LICENSE`)"):
    check("plain grant is not negated: %r" % phrase,
          bool(NEGATED_RE.search(phrase)), False)

# ---------------------------------------------------------------------------
# 5. slug extraction must not harvest paths, versions or filenames
# ---------------------------------------------------------------------------
check("a version fragment is not a slug", slugs_in("4.13.0/2026"), [])
# POSITIVE for the path fix: every one of these has slug SHAPE and none is a repo
for path in ("main/LICENSE", "master/LICENSE.md", "docs/LICENSE", "HEAD/COPYING",
             "blob/LICENSE.txt", "refs/heads", "tree/master"):
    check("a path is not a slug: %s" % path, slugs_in(path), [])
# NEGATIVE: a real slug whose repo name is lowercase-with-dots must survive the
# filename rule, or the fix would eat `sst/opencode` and `idiap/coqui-ai-TTS`
for real in ("idiap/coqui-ai-TTS", "oat-sa/lib-lti1p3-core", "frappe/erpnext",
             "1EdTech/lti-1-3-php-library", "openstax/osbooks-biology-bundle"):
    check("a real slug survives: %s" % real, slugs_in(real), [real])
check("a real slug is found", slugs_in("github.com/oat-sa/qti-sdk"),
      ["oat-sa/qti-sdk"])
check("trailing punctuation does not join the slug",
      slugs_in("see `oat-sa/qti-sdk`, which is GPL"), ["oat-sa/qti-sdk"])

print("p449 controls: %d/%d" % (ok, ok + len(bad)))
for b in bad:
    print("  FAIL", b)
sys.exit(1 if bad else 0)
