"""Step 1 of `ACTION ST` — harvest (slug, licence_cell) pairs from the licence shelf.

The harvest is the part that can silently invent findings, so every rule below
exists because these shelves already recorded the defect it prevents.

  T224-2  a dotted owner is a HOSTNAME, not an account  -> reject dotted owners
  T224-3  the unit is the grant's SUBJECT, not the row sharing its line
          -> a line citing 2+ distinct slugs yields NO pair (ambiguous attribution)
  T227-V2 `GPL-3.0` is a SUBSTRING of `AGPL-3.0`
          -> licence tokens are matched longest-first with explicit boundaries
  p227    a cell behind a `<!--corrected-->` marker is WITHDRAWN, not live
          -> withdrawn cells are harvested but flagged, never gated
"""
import re
import sys

SLUG_RE = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9_-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*?)(?=[)\s`,.;:'\"\]]|$)")

# Longest-first: AGPL before GPL, LGPL before GPL, -or-later before -only before bare.
LICENCE_TOKENS = [
    "AGPL-3.0-or-later", "AGPL-3.0-only", "AGPL-3.0", "AGPLv3", "AGPL-3",
    "LGPL-3.0-or-later", "LGPL-3.0-only", "LGPL-3.0", "LGPL-2.1", "LGPL-3",
    "GPL-3.0-or-later", "GPL-3.0-only", "GPL-3.0", "GPL-2.0", "GPLv3", "GPLv2", "GPL-3", "GPL-2",
    "Apache-2.0", "Apache 2.0",
    "BSD-3-Clause", "BSD-2-Clause",
    "MPL-2.0", "EPL-2.0", "EUPL-1.2",
    "CC-BY-SA-4.0", "CC-BY-4.0", "CC0-1.0",
    "ECL-2.0",
    "Unlicense", "ISC", "MIT",
]
# A token is only a cell if it stands as a WORD (p227's standing rule: the unit
# of a licence family token is a word in a known section, never a substring).
_TOKEN_RES = [(t, re.compile(r"(?<![A-Za-z0-9.-])" + re.escape(t) + r"(?![A-Za-z0-9-])")) for t in LICENCE_TOKENS]

NO_GRANT_RE = re.compile(r"NO GRANT|NO-GRANT|DANGLING", re.I)


def slugs_on(line):
    out = []
    for m in SLUG_RE.finditer(line):
        owner, repo = m.group(1), m.group(2)
        if "." in owner:          # T224-2: dotted owner is a hostname
            continue
        repo = repo.rstrip(".")
        if not repo or repo in {"md", "txt"}:
            continue
        out.append(f"{owner}/{repo}")
    # order-preserving unique
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def licences_on(line):
    """Longest-first, non-overlapping. Returns tokens in order of appearance."""
    claimed = [False] * len(line)
    hits = []
    for tok, rx in _TOKEN_RES:
        for m in rx.finditer(line):
            if any(claimed[m.start():m.end()]):
                continue           # T227-V2: already consumed by a longer token
            for i in range(m.start(), m.end()):
                claimed[i] = True
            hits.append((m.start(), tok))
    return [t for _, t in sorted(hits)]


# ---------------------------------------------------------------------------
# The five NON-GRANT subjects a licence token can have on a shelf line.
#
# p228's first gate run returned 11 family disagreements and 9 of them were
# defects IN THIS HARVESTER, not in the shelves. A licence token sitting on a
# line that cites exactly one repository is still not necessarily that
# repository's grant, and every class below cost a false finding before it was
# named. This is p224's `T224-3` -- the unit is the grant's SUBJECT -- in five
# further shapes.
# ---------------------------------------------------------------------------

# 1. DIRECTORY-SCOPED: the row's own subject is a path inside the repo, not the
#    repo. `pupilfirst/pupilfirst | 978 | docs/** | CC-BY-SA-4.0` is a CORRECT
#    cell about `docs/`, and p227 recorded this unit as `T227-A4`.
# A scope is an explicit GLOB or a stated directory carve-out. A grant merely
# STORED at `docs/License.txt` is still the repository's grant (openSIS, 11 cells)
# and must NOT be excluded -- the first draft of this pattern excluded 553 cells
# by matching ordinary markdown emphasis across a table pipe.
SCOPED_RE = re.compile(r"`[^`\s|]*/\*\*?`|`/(mod|docs|src|lib)\b|\bthe contents of the\b")

# 2. BODY-CONTENT: the token names what the licence FILE CONTAINS, not what the
#    project grants -- "LGPL preamble, `GPL-3.0` by reference", "`GPL-3.0`
#    included by value". Both are true statements and neither is a grant.
BODY_CONTENT_RE = re.compile(r"by \*\*(reference|value)\*\*|\bincluded by\b|\bby reference\b|\bby value\b|\bpreamble\b", re.I)

# 3. CORRECTION NARRATIVE / REFUTED PATTERN: the token is the value being
#    WITHDRAWN or the pattern a refuted-claims row exists to catch. Harvesting
#    it as live inverts the very correction that recorded it.
NARRATIVE_RE = re.compile(
    r'was published|published as|flagged as|a row mentioning|refut|withdraw|'
    r"corrected|stale|wrongly|no longer|used to|previously|p\d{2,3} published|"
    r"claimed|over-?restrictive|over-?permissive|defect", re.I)

# 4. UNLINKED CO-SUBJECT: another named entity shares the line, so the token's
#    subject is ambiguous even though only one slug is LINKED. The `AGPL-3` in
#    "`OpenEduCat`, Open edX *(`AGPL-3`)*" belongs to Open edX.
CO_SUBJECT_NAMES = [
    "Open edX", "Moodle", "Canvas", "Chamilo", "Odoo", "Open Olat", "OpenOlat",
    "Sakai", "ILIAS", "Gibbon", "RosarioSIS", "OpenMRS", "Kolibri", "Tutor",
    "BigBlueButton", "Frappe", "ERPNext", "OpenEduCat", "AlekSIS", "UniTime",
    "Elgg", "SWAD", "Pupilfirst", "Jupyter", "Totara", "Blackboard", "D2L",
]

# 5. QUOTED EXTERNAL CLAIM: the token sits inside a quotation of a SOURCE, which
#    is evidence about the source and never a cell about the repository.
QUOTED_RE = re.compile('\\*"[^"]*"\\*|\u201c[^\u201d]*\u201d')


def non_grant_subject(line, slug):
    """Return the name of the non-grant subject class, or None if the token is
    plausibly this repository's own grant.

    Order matters and the classes must stay DISJOINT: a quotation is owned by
    `QUOTED_RE` and not by the narrative pattern, so a cell quoting a source's
    wrong claim is filed as evidence about the SOURCE rather than as a correction
    this KB made.
    """
    if SCOPED_RE.search(line):
        return "DIRECTORY-SCOPED"
    if BODY_CONTENT_RE.search(line):
        return "BODY-CONTENT"
    if QUOTED_RE.search(line):
        return "QUOTED-EXTERNAL-CLAIM"
    if NARRATIVE_RE.search(line):
        return "CORRECTION-NARRATIVE"
    repo_tail = slug.split("/")[-1].lower()
    others = [n for n in CO_SUBJECT_NAMES
              if re.search(r"(?<![\w-])" + re.escape(n) + r"(?![\w-])", line)
              and n.lower().replace(" ", "") not in repo_tail.replace("-", "").replace("_", "")]
    if len(others) >= 2 or (others and ("," in line or " and " in line) and "|" not in line):
        return "UNLINKED-CO-SUBJECT"
    return None


def harvest(path, text):
    """Yield dict rows. Only a line with EXACTLY ONE slug can attribute a cell."""
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        slugs = slugs_on(line)
        if not slugs:
            continue
        lics = licences_on(line)
        withdrawn = "<!--corrected-->" in line
        if len(slugs) > 1:
            if lics:
                rows.append(dict(file=path, line=n, slug="|".join(slugs),
                                 cell="|".join(lics), status="AMBIGUOUS-MULTI-SLUG",
                                 withdrawn=withdrawn))
            continue
        if not lics:
            if NO_GRANT_RE.search(line):
                rows.append(dict(file=path, line=n, slug=slugs[0], cell="",
                                 status="NO-GRANT-ASSERTED", withdrawn=withdrawn))
            continue
        if len(lics) > 1:
            rows.append(dict(file=path, line=n, slug=slugs[0], cell="|".join(lics),
                             status="MULTI-LICENCE-CELL", withdrawn=withdrawn))
            continue
        if withdrawn:
            status = "WITHDRAWN"
        else:
            status = non_grant_subject(line, slugs[0]) or "LIVE"
        rows.append(dict(file=path, line=n, slug=slugs[0], cell=lics[0],
                         status=status, withdrawn=withdrawn))
    return rows


def main(paths):
    print("\t".join(["file", "line", "slug", "cell", "status", "withdrawn"]))
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for r in harvest(p, fh.read()):
                print("\t".join([r["file"], str(r["line"]), r["slug"], r["cell"],
                                 r["status"], "yes" if r["withdrawn"] else "no"]))


if __name__ == "__main__":
    main(sys.argv[1:])
