#!/usr/bin/env python3
"""`p444/readme_claim.py` — the half of `Gap 443-C` that did not exist.

`Gap 443-C`, declared by `p443`: this base has no instrument that compares the grant a
README *states* against the grant the payload *is*.  `ipti/br.tag` was caught by hand —
its README says "The BSD-3-Clause" while `LICENSE` is GNU GPL v2 — and the gap notes that
this is the direction that costs money, because a reader who trusts the README vendors a
copyleft platform as permissive.

This module answers ONLY the README side.  The payload side is `lib/license_family.sh`'s
`family_of`, which is `P171`-hardened, and is NOT reimplemented here: `P237`/`P197` say a
new sweep written from scratch re-imports every defect already paid for.  The comparator
(`compare.py`) joins the two.

Contract
--------
`claims_in(text)` -> list of `Claim(family, tier, context, evidence)`.

A licence NAME is not a CLAIM.  A README that says "unlike the GPL-3.0 projects in this
space" names GPL-3.0 and claims nothing, and a dependency table naming twelve licences
claims none of them.  So every match here must sit in a CLAIM CONTEXT:

  BADGE    a shields.io-style licence badge, or an image whose alt text is about licence
  PROSE    "licensed under X", "released under X", "under the X licence", "licence: X"
  SECTION  inside a `#`-heading section whose title is Licence/License/Licensing

That gate is the whole instrument.  Without it the channel is a licence-word grep, and
`p288`'s README channel already showed a word grep cannot carry a verdict.
"""
import re
import sys
from dataclasses import dataclass

# Tier is PERMISSIVENESS, coarse and defensible.  The comparator only ever compares tiers,
# never spellings, because the money question is "does the README look MORE permissive than
# the file" and that is a tier question.
TIER = {
    "PUBLIC-DOMAIN": 0, "MIT": 0, "BSD": 0, "BSD-2-Clause": 0, "BSD-3-Clause": 0,
    "ISC": 0, "Unlicense": 0, "CC0-1.0": 0, "0BSD": 0, "Apache-2.0": 0, "Zlib": 0,
    "MPL-2.0": 1, "EPL-2.0": 1, "LGPL-2.1": 1, "LGPL-3.0": 1, "LGPL": 1, "ECL-2.0": 1,
    "GPL-2.0": 2, "GPL-3.0": 2, "GPL": 2,
    "AGPL-3.0": 3,
    "CC-BY-NC": 4, "NONCOMMERCIAL-NOT-OSI": 4, "PROPRIETARY": 4,
    # 🔵 Added by the first shelf run: families the sell shelves actually carry and this map
    # did not.  Each is placed by the obligation it imposes, not by its popularity.
    "MPL-1.1": 1, "LGPL-2.0": 1, "EUPL-1.2": 2, "ECL-1.0": 1,
    "CC-BY-SA": 2, "CC-BY": 0, "ODbL": 2, "OSL-3.0": 2, "CPAL-1.0": 2,
}

# 🔴 THE SECOND DEFECT THIS INSTRUMENT FOUND IN ITSELF, on its first run over the shelf.
#
# `TIER.get(fam, 9)` treated an UNMAPPED payload family as tier 9 — more restrictive than
# anything — so any README claim at all became "README-MORE-PERMISSIVE".  Measured on the
# shelf: of 4 such verdicts, TWO were this artefact — `OS4ED/openSIS-Classic` (payload
# MPL-1.1, unmapped) and `withmarbleapp/os-taxonomy` (payload ODbL-UNVERSIONED, unmapped).
# Both were manufactured by the default, not found in the repository.
#
# 🔵 An unknown family is UNKNOWN, not severe.  A missing map entry must produce a verdict
# that says the map is missing an entry — never a finding against the repository.  This is
# `p443`'s own lesson about nil results, arriving one level down: a default that silently
# stands in for a measurement reads exactly like a measurement.
def tier_of(fam):
    """Permissiveness tier, or None when the family is not in the map."""
    base = fam.split(" ")[0] if fam else fam
    for key in (fam, base):
        if key in TIER:
            return TIER[key]
    for prefix in ("CC-BY-NC", "CC-BY-SA", "CC-BY", "ODbL", "MPL", "LGPL", "EUPL", "GPL"):
        if base and base.startswith(prefix):
            return TIER.get(prefix)
    return None

# Longest-first: "AGPL-3.0" must win over "GPL-3.0", and "LGPL" over "GPL".
_NAMES = [
    (r"agpl[-\s_]*v?3(?:\.0)?|affero\s+general\s+public\s+license\s+v?3|affero\s+gpl", "AGPL-3.0"),
    (r"agpl", "AGPL-3.0"),
    (r"lgpl[-\s_]*v?2\.1|lesser\s+general\s+public\s+license\s+v?2\.1", "LGPL-2.1"),
    (r"lgpl[-\s_]*v?3(?:\.0)?|lesser\s+general\s+public\s+license\s+v?3", "LGPL-3.0"),
    (r"lgpl|lesser\s+general\s+public\s+license", "LGPL"),
    (r"gpl[-\s_]*v?3(?:\.0)?|gnu\s+general\s+public\s+license\s+v?3|gplv3", "GPL-3.0"),
    (r"gpl[-\s_]*v?2(?:\.0)?|gnu\s+general\s+public\s+license\s+v?2|gplv2", "GPL-2.0"),
    (r"gnu\s+general\s+public\s+license|gpl", "GPL"),
    (r"apache[-\s_]*(?:license[-\s_]*)?v?2(?:\.0)?|apache\s+software\s+license", "Apache-2.0"),
    (r"bsd[-\s_]*3[-\s_]*clause|3[-\s_]*clause\s+bsd|new\s+bsd", "BSD-3-Clause"),
    (r"bsd[-\s_]*2[-\s_]*clause|2[-\s_]*clause\s+bsd|simplified\s+bsd", "BSD-2-Clause"),
    (r"bsd", "BSD"),
    (r"mpl[-\s_]*v?2(?:\.0)?|mozilla\s+public\s+license", "MPL-2.0"),
    (r"epl[-\s_]*v?2(?:\.0)?|eclipse\s+public\s+license", "EPL-2.0"),
    (r"ecl[-\s_]*v?2(?:\.0)?|educational\s+community\s+license", "ECL-2.0"),
    (r"\bmit\b", "MIT"),
    (r"\bisc\b", "ISC"),
    (r"unlicen[sc]e|public\s+domain", "Unlicense"),
    (r"cc0", "CC0-1.0"),
    (r"cc[-\s_]*by[-\s_]*nc[a-z0-9\-\.]*|non[-\s]?commercial", "CC-BY-NC"),
    (r"\bzlib\b", "Zlib"),
    (r"proprietary|all\s+rights\s+reserved", "PROPRIETARY"),
]
_NAME_RE = [(re.compile(p, re.I), fam) for p, fam in _NAMES]


@dataclass(frozen=True)
class Claim:
    family: str
    tier: int
    context: str   # BADGE | PROSE | SECTION
    evidence: str


def _families_in(s: str):
    """Every licence family named in `s`, longest-name-first so AGPL beats GPL.

    Consumes each match so one spelling cannot be counted twice under two names.
    """
    out, work = [], s
    for rx, fam in _NAME_RE:
        m = rx.search(work)
        if m:
            out.append(fam)
            work = work[:m.start()] + " " + work[m.end():]
    return out


# A badge: markdown image whose URL or alt text is about a licence.
_BADGE = re.compile(r"!\[([^\]]*)\]\(([^)]*)\)", re.I)
# Prose claim forms.  The verb is what makes it a claim.
_PROSE = re.compile(
    r"(?:"
    r"licen[sc]ed\s+under(?:\s+the)?|"
    r"released\s+under(?:\s+the)?|"
    r"distributed\s+under(?:\s+the)?|"
    r"available\s+under(?:\s+the)?|"
    r"published\s+under(?:\s+the)?|"
    r"licen[sc]e\s*[:=]|licen[sc]ing\s*[:=]|"
    r"under\s+the\s+terms\s+of(?:\s+the)?|"
    r"bajo\s+(?:la\s+)?licen[sc]ia|licen[sc]ia\s*[:=]|"
    r"sob\s+a\s+licen[çc]a|licen[çc]a\s*[:=]"
    r")([^\n.;]{0,120})", re.I)
_HEADING = re.compile(r"^\s{0,3}(#{1,6})\s*(.+?)\s*#*\s*$", re.M)
_LIC_TITLE = re.compile(r"^(licen[sc]e|licen[sc]ing|licen[sc]ia|licen[çc]a)\b", re.I)


def _license_sections(text: str):
    """Body text of every `#`-heading section whose title is a licence heading."""
    heads = [(m.start(), len(m.group(1)), m.group(2), m.end()) for m in _HEADING.finditer(text)]
    out = []
    for i, (_start, level, title, end) in enumerate(heads):
        if not _LIC_TITLE.match(title.strip()):
            continue
        stop = len(text)
        for nstart, nlevel, _nt, _ne in heads[i + 1:]:
            if nlevel <= level:
                stop = nstart
                break
        out.append(text[end:stop])
    return out


# 🔴 Found first-hand on `ipti/br.tag` while building this module, and it changes the
# instrument: the repository's BSD-3-Clause SHIELD IS HTML-COMMENTED OUT on line 1
# (`<!-- [![License](...badge/License-BSD%203--Clause...)]... -->`), so it is not a live
# claim at all.  A badge-only comparator reads that comment and "catches" the divergence
# for a reason the file does not state; a badge-only comparator that correctly ignored
# comments would grade the repository SILENT and miss the divergence entirely.  The live
# claim is the `## Licença` section reading "The BSD-3-Clause".  So: comments are stripped
# BEFORE any context is scanned, and the SECTION context is load-bearing, not a nicety.
_COMMENT = re.compile(r"<!--.*?-->", re.S)


def strip_comments(text: str) -> str:
    """HTML comments removed.  A commented-out badge is not a claim."""
    return _COMMENT.sub(" ", text or "")


# 🔴 FOUND BY THIS INSTRUMENT'S OWN FIRST LIVE RUN, on `jeanhrm/siagie-analytics`, and it
# is a defect in the module above, recorded here rather than quietly patched out.
#
# That repository ships an UNMODIFIED LARAVEL SKELETON README.  Its `## License` section
# reads "The Laravel framework is open-sourced software licensed under the MIT license",
# and the repository itself carries NO grant file across 146 paths.  The claim-context gate
# graded it a live MIT claim, so the comparator reported `NO-PAYLOAD` — a repository that
# states MIT and never made the grant.  That verdict is wrong for the stated reason: the
# repository never claimed anything.  LARAVEL did.
#
# 🔵 The lesson, and it is the same shape as `P237`: the claim-context gate answers *"is
# this a claim?"* and not *"WHOSE grant is being claimed?"*.  Boilerplate READMEs —
# Laravel, create-react-app, every `npx` starter — carry the UPSTREAM project's licence
# claim, and a repository that never replaced the skeleton inherits a claim it did not
# make.  A subject-blind reading turns every un-edited starter into a false licence row,
# and in the thin-supply tranche this pass probed, un-edited starters are COMMON.
# 🔴 THE SECOND SURFACE FORM of the subject question, found on `withmarbleapp/os-taxonomy`
# by the same shelf run.  Its `## License` section is an exemplary multi-licence TABLE —
# ODbL 1.0 for the database, CC BY-SA 4.0 for the content — and it closes with
# "Bundled Three.js and Baloo 2 retain their separate MIT and OFL licenses and notices."
# The MIT in that sentence belongs to THREE.JS.  The subject gate above did not catch it
# because the gate wanted "X library is licensed", and this is "bundled X retain their".
# 🔵 Same defect class as the Laravel skeleton, different grammar — which is the argument
# for a SEPARATE pattern per form rather than one clever regex: each form is a measurement.
_BUNDLED_CLAIM = re.compile(
    # 🔴 v1 wrote `[^.\n]` to stay inside one sentence, and a dot inside a PROJECT NAME
    # defeated it: "Bundled **Three.js** and Baloo 2 retain their separate MIT..." could not
    # be crossed, so the pattern this was written for did not match it.  Stay on one LINE
    # instead of one sentence; the 120-character cap does the rest.
    r"(?:bundled|vendored|third[-\s]?party|dependenc(?:y|ies)|upstream|included\s+librar)"
    r"[^\n]{0,120}?(?:retain|keep|carry|remain|are\s+licen[sc]ed|under)",
    re.I)


def bundled_claim(window):
    """True when the window is about a BUNDLED third party's grant, not this project's."""
    return bool(_BUNDLED_CLAIM.search(window or ""))


_FOREIGN_SUBJECT = re.compile(
    r"(?:^|[.\n]\s*)(?:the\s+)?([A-Z][\w.+-]{1,30})\s+"
    r"(?:framework|library|project|package|sdk|cli|template|boilerplate|starter|toolkit|engine)\s+"
    r"(?:is|was)\s+(?:open-sourced\s+)?(?:software\s+)?licen[sc]ed",
    re.I)


def _slug_tokens(repo_slug):
    if not repo_slug:
        return set()
    raw = re.split(r"[/_.\-\s]+", repo_slug.lower())
    return {t for t in raw if t}


def foreign_subject(window, repo_slug=None):
    """The named third-party subject of a licence claim, or None.

    Returns the subject name when the claim's grammatical subject is a NAMED project that
    is not this repository.  `repo_slug` is how "not this repository" is decided; without
    it, any named project subject counts as foreign, which is the SAFE default (P266: the
    conservative reading is the default and the lenient one is asked for).
    """
    m = _FOREIGN_SUBJECT.search(window or "")
    if not m:
        return None
    subject = m.group(1)
    if subject.lower() in _slug_tokens(repo_slug):
        return None
    return subject


def claims_in(text: str, repo_slug: str = None):
    """Every licence CLAIM in a README, in claim contexts only.  De-duplicated by family.

    `repo_slug` enables the subject gate: a claim whose subject is a named third-party
    project is returned with context `FOREIGN:<subject>` instead of being counted as this
    repository's claim.  The comparator drops `FOREIGN:*` claims.
    """
    if not text:
        return []
    text = strip_comments(text)
    found = {}

    def add(fam, ctx, ev):
        if fam not in found:
            found[fam] = Claim(fam, TIER.get(fam, 9), ctx, ev.strip()[:160])

    for m in _BADGE.finditer(text):
        alt, url = m.group(1), m.group(2)
        blob = f"{alt} {url}"
        if not re.search(r"licen[sc]e", blob, re.I):
            continue
        # shields.io encodes the value in the path: badge/license-MIT-green
        for fam in _families_in(blob):
            add(fam, "BADGE", m.group(0))

    for m in _PROSE.finditer(text):
        # The window for the subject question starts BEFORE the verb: the subject of
        # "The Laravel framework is licensed under X" sits to the LEFT of the match.
        lo = max(0, m.start() - 160)
        window = text[lo:m.end()]
        fs = foreign_subject(window, repo_slug)
        if not fs and bundled_claim(window):
            fs = "BUNDLED"
        ctx = f"FOREIGN:{fs}" if fs else "PROSE"
        for fam in _families_in(m.group(1)):
            add(fam, ctx, m.group(0))

    for body in _license_sections(text):
        # Only the first lines of a licence section: a full inlined licence text would
        # otherwise contribute its own body words (the P171 class, through a section).
        #
        # 🔵 And scanned LINE BY LINE, not as one blob.  `withmarbleapp/os-taxonomy`'s
        # licence section is a multi-licence TABLE: one row grants ODbL over the database,
        # one grants CC BY-SA over the content, and one notes that BUNDLED three.js retains
        # MIT.  Testing the whole section for a bundled note would have muted the two
        # CORRECT claims along with the foreign one.  A table row is its own claim context.
        for line in body.strip().splitlines()[:8]:
            fams = _families_in(line)
            if not fams:
                continue
            fs = foreign_subject(line, repo_slug)
            if not fs and bundled_claim(line):
                fs = "BUNDLED"
            ctx = f"FOREIGN:{fs}" if fs else "SECTION"
            for fam in fams:
                add(fam, ctx, line)

    return sorted(found.values(), key=lambda c: (c.tier, c.family))


def main():
    if len(sys.argv) < 2:
        print("usage: readme_claim.py <README-file> [owner/name]", file=sys.stderr)
        return 2
    try:
        with open(sys.argv[1], encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"cannot read: {exc}", file=sys.stderr)
        return 1
    cs = claims_in(text, sys.argv[2] if len(sys.argv) > 2 else None)
    if not cs:
        print("README-SILENT")
        return 0
    for c in cs:
        print(f"{c.family}\t{c.tier}\t{c.context}\t{c.evidence}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
