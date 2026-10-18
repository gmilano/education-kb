#!/usr/bin/env python3
"""p279 controls for the absence-claims gate.

🔴 CONTROL ZERO is `p277`'s verbatim sentence.  A gate built from a historical defect that
cannot reproduce that defect is a gate built from a story, so the first control is the real
text, over a fixture that carries the real claim, asserting the real verdict.

Every house-style shape that broke a draft of this gate is a control here too, so a later
pass widening the predicate detonates on these instead of on the shelves.
"""
import sys
import tempfile
import pathlib

# `-I` drops the script's own directory from `sys.path`, and the Makefile runs the suites
# under `-I` deliberately.  A suite that cannot import its subject under the interpreter
# flags the gate actually uses is a suite that does not run.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import absence_claims as A  # noqa: E402

FAILED = []


def check(label, actual, expected):
    if actual != expected:
        FAILED.append(f"{label}: expected {expected!r}, got {actual!r}")


def fixture(**shelves):
    """A throwaway root carrying only the shelves a control needs."""
    d = tempfile.mkdtemp()
    for name, body in shelves.items():
        p = pathlib.Path(d) / name.replace("__", "/")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
    return d


# --- CONTROL ZERO: p277's real sentence, p121's real claim ------------------------------
P277 = ("`p277`'s top-ranked item read: this base has a grade for payload and a grade for "
        "metadata and **no class at all for CONFLICT**.")
root = fixture(**{
    "README.md": "## Pass 277\n" + P277 + "\n",
    # p121's class, where it really lives -- a DIFFERENT shelf from the one p277 was in
    "repos__trending.md": "| slug | CONFLICT | direction |\n" * 26,
})
ref, q, qt = A.findings(P277, root, exclude_shelf="README.md")
check("p277's sentence is REFUTED by p121's shelf", len(ref), 1)
check("the refuted subject is `conflict`", ref[0][2] if ref else None, "conflict")
check("the refutation names the shelf that already claims it",
      list(ref[0][3]) if ref else None, ["repos/trending.md"])

# the same sentence over a base that genuinely does NOT carry the class: establishable
root_clean = fixture(**{"README.md": "## Pass 277\n" + P277 + "\n",
                        "repos__trending.md": "| slug | payload | metadata |\n"})
ref2, _, _ = A.findings(P277, root_clean, exclude_shelf="README.md")
check("the SAME sentence over a base without the class is NOT refuted", len(ref2), 0)

# --- the gate must read the LIVE pass section, not the whole file ------------------------
readme = ("## Pass 279 — today\nnothing to declare here.\n\n"
          "## Pass 277 — history\n" + P277 + "\n")
check("only the newest `## Pass` section is in the fatal scope",
      "CONFLICT" in A.latest_pass_section(readme), False)
check("the newest section is the one that IS read",
      "nothing to declare" in A.latest_pass_section(readme), True)
check("a README with no pass section yields an empty scope, not a crash",
      A.latest_pass_section("# title\nprose\n"), "")

# --- subject extraction -----------------------------------------------------------------
check("a backticked subject is distinctive",
      A.subjects_in(" no class at all for `gegok12` on this shelf")[0], "gegok12")
check("an owner/repo slug is distinctive",
      "ls1intum/athena" in A.subjects_in(" there is no manifest in ls1intum/Athena"), True)
check("an ALL-CAPS subject is distinctive",
      A.subjects_in(" there is no MCP server for this")[0], "mcp")
check("the clause ENDS at the sentence boundary -- the next claim's subject is not ours",
      A.subjects_in(" there is no MCP here. But CONFLICT is elsewhere."), ["mcp"])

# --- shapes that broke a draft ----------------------------------------------------------
check("lowercase prose alone resolves no subject -> QUEUE, not a finding",
      A.subjects_in(" there is no dominant open source tutor yet"), [])
check("a structural ALL-CAPS word is not a subject (STOP/PASS/NEW)",
      A.subjects_in(" there is no PASS here, STOP"), [])
check("a licence token is not a subject -- it is on every shelf by construction",
      A.subjects_in(" there is no MIT grant committed"), [])
check("`education` is too common to carry an absence verdict",
      A.subjects_in(" there is no `education` angle"), [])
check("a two-letter caps word is below the distinctiveness floor",
      A.subjects_in(" there is no AI in it"), [])

# QUEUE rows are the backlog and must NOT be fatal -- gate-enumeration's polarity
_, queued, _ = A.findings("## Pass 279\nthere is no dominant open source tutor yet.\n",
                          root_clean, exclude_shelf="README.md")
check("unresolved absence prose is QUEUED", len(queued), 1)
_ref, _, _ = A.findings("## Pass 279\nthere is no dominant open source tutor yet.\n",
                        root_clean, exclude_shelf="README.md")
check("...and QUEUE alone is not a refutation", len(_ref), 0)

# --- the vocabulary ---------------------------------------------------------------------
for phrase in ("there is no", "no class at all for", "this base has no", "nothing on",
               "no binding", "never built"):
    check(f"vocabulary carries {phrase!r}", bool(A.ABSENCE_RE.search(f"x {phrase} `tok`")), True)
check("an unrelated sentence matches no absence phrase",
      bool(A.ABSENCE_RE.search("the grant is MIT and the tree was enumerated")), False)

# --- the exclude_shelf arm: a claim must not refute ITSELF -------------------------------
self_only = fixture(**{"README.md": "## Pass 279\nthere is no `widgetron` anywhere.\n"})
ref3, _, _ = A.findings("there is no `widgetron` anywhere.", self_only,
                        exclude_shelf="README.md")
check("a sentence does not refute itself via its own shelf", len(ref3), 0)
ref4, _, _ = A.findings("there is no `widgetron` anywhere.", self_only, exclude_shelf=None)
check("...and without the exclusion it would have (the arm is load-bearing)", len(ref4), 1)

# --- the QUOTED arm: the false positive this gate found on its own first real run --------
# 🔴 `p278`'s real headline, verbatim.  It QUOTES `p277`'s absence in order to document it.
P278_QUOTING = ('`p277`\'s top-ranked item read: *"**Build the payload-vs-metadata CONFLICT '
                'class** … this base has a grade for *payload* and **no class at all for '
                'CONFLICT**."*')
r_q, _, qt_q = A.findings(P278_QUOTING, root, exclude_shelf="README.md")
check("a QUOTED absence is not an assertion -> not refuted", len(r_q), 0)
check("...and it is still REPORTED as quoted, never silently dropped", len(qt_q), 1)
check("the quoted finding still names the subject", qt_q[0][2] if qt_q else None, "conflict")

# the same text UNQUOTED is the assertion, and it must still fail
check("the same sentence asserted rather than quoted IS refuted",
      len(A.findings("this base has no class at all for CONFLICT", root,
                     exclude_shelf="README.md")[0]), 1)

check("a markdown blockquote is a report, not an assertion",
      A.in_quote("> there is no CONFLICT class", 2), True)
check("an unquoted line is an assertion",
      A.in_quote("there is no CONFLICT class", 0), False)
check("the opening quote mark puts what follows inside the span",
      A.in_quote('p277 wrote "there is no CONFLICT class', 12), True)
check("text AFTER a closed quote span is the pass's own voice again",
      A.in_quote('"quoted bit" and there is no CONFLICT class', 20), False)
check("a curly opening quote counts (the shelves carry both)",
      A.in_quote('“there is no CONFLICT', 5), True)

# 🔴 THE WRAPPED SHAPE — `p278`'s headline as it is ACTUALLY hard-wrapped in README.md.
# The opening `*"` is on the line ABOVE the absence phrase.  A line-local quote-parity
# predicate passes every control above and still reports this as an assertion, which is how
# the first fix for the quoting false positive was itself wrong.  Verbatim from the shelf:
WRAPPED = ('`p277`\'s top-ranked item read: *"**Build the payload-vs-metadata CONFLICT '
           'class** … this base has a\ngrade for *payload* and a grade for *metadata* and '
           '**no class at all for CONFLICT**."*\n')
r_w, _, qt_w = A.findings(WRAPPED, root, exclude_shelf="README.md")
check("a quote WRAPPED across lines is still a report, not an assertion", len(r_w), 0)
check("...and is reported as quoted", len(qt_w), 1)
check("paragraph scope, not file scope: a NEW paragraph reopens the pass's own voice",
      len(A.findings('"a quoted bit ends here."\n\nthis base has no class at all for '
                     'CONFLICT\n', root, exclude_shelf="README.md")[0]), 1)
check("a subject clause that WRAPS is still resolved",
      A.subjects_in(" there is no\n`gegok12` row".replace("\n", " "))[0], "gegok12")
check("line numbers survive the paragraph walk",
      A.findings('para one\n\nthis base has no class at all for CONFLICT\n', root,
                 exclude_shelf="README.md")[0][0][0], 3)

if FAILED:
    print(f"🔴 {len(FAILED)} control(s) FAILED")
    for f in FAILED:
        print("   " + f)
    sys.exit(1)
print("🟢 p279-absence-claims: all controls pass")
