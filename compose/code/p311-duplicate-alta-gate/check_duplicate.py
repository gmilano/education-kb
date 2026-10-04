#!/usr/bin/env python3
"""check_duplicate.py -- the gate this base did not have, and the pase 100 proved it needed.

WHY THIS EXISTS, and it is a defect of THIS pase, caught before publishing.

The pase 100 rotated its search axis to pronunciation / spoken assessment, picked that axis from
its own market sweep, measured 14 candidates first-hand, and drafted a header note announcing
that "this base had ZERO speech pieces".  That claim was FALSE.  `repos/foundations.md` has
carried a section titled "Capa de habla y lectura oral" since the PASE 14 (2026-10-01), holding
`Halleck45/OpenPronounce`, `kaldi-asr/kaldi` and `jimbozhang/speechocean762` -- including the very
finding the pase 100 was about to publish as new (speechocean762 ships no licence file).  The same
went for `eecs-autograder/autograder.io`, inventoried in `verticals/solutions.md` since the PASE 5
with its licence already marked undeclared.

So the defect is not a wrong licence or a wrong number.  It is that an "alta" was about to be
published for pieces the base ALREADY HELD, and nothing in the repository would have objected.
This base has controls for frontmatter coverage, table integrity, region vocabulary, dangling
trend citations, pattern citations, licence family, holder, commercial use and manifest ownership
-- and NOT ONE of them asks the question that matters when a base is 100 passes and ~250 slugs
deep: IS THIS ALREADY HERE?

That is a structural blind spot, not an accident.  Every other control checks a claim the pase is
MAKING.  This one checks a claim the pase is IMPLICITLY making by calling something an alta -- that
it is new -- and an implicit claim is exactly the kind nothing audits.

USAGE
    python3 check_duplicate.py <slug> [<slug> ...]      # explicit slugs
    python3 check_duplicate.py --stdin                  # one slug per line
    python3 check_duplicate.py --self-test              # fixtures, offline

Exit status is 1 when any slug is already published, so it can gate a commit.
"""
import os
import re
import sys

# The files a reader of this KB actually reads.  compose/code/ is excluded on purpose: an
# instrument's fixtures and TSVs name slugs for measurement, which is not publication, and
# counting them would make every measured candidate look like an existing row.
PUBLISHED = [
    "agents/top.md", "agents/trending.md",
    "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md", "intel/trends.md",
    "compose/patterns.md",
]


def repo_root(start=None):
    d = os.path.abspath(start or os.path.dirname(__file__))
    while True:
        if os.path.isdir(os.path.join(d, "agents")) and os.path.isdir(os.path.join(d, "intel")):
            return d
        nd = os.path.dirname(d)
        if nd == d:
            raise SystemExit("check_duplicate: repository root not found")
        d = nd


def load(root):
    """Return {path: text}.  A file that does not exist is skipped, not fatal: this gate must
    keep working if the layout changes, because a gate that crashes gets deleted."""
    out = {}
    for rel in PUBLISHED:
        p = os.path.join(root, rel)
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as fh:
                out[rel] = fh.read()
    return out


def section_of(text, idx):
    """The nearest '## ' heading at or above idx -- so the report says WHERE, not just whether.
    Naming the section is what turns the answer from 'already there' into 'already there, in the
    speech layer added in the pase 14', which is the difference between a warning and a fix."""
    best = None
    for m in re.finditer(r"(?m)^##+ +(.*)$", text):
        if m.start() <= idx:
            best = m.group(1).strip()
        else:
            break
    return best or "(before the first heading)"


def find(slug, files):
    """Hits for a slug.  Matched case-insensitively on the WHOLE slug, and also on the bare repo
    name when that name is distinctive.

    P299's lesson applies here in its own key: a bare name match is a SUBSTRING question, and a
    short or generic name ('qti', 'core', 'agent') would hit prose everywhere.  So the bare-name
    probe is gated on length AND required to sit on a word boundary.  The owner/name form is
    always reported; the bare-name form is reported SEPARATELY, because the two answers mean
    different things: the first is 'this repo is published', the second is 'something with this
    name is published, go look'.
    """
    owner, _, name = slug.partition("/")
    full_hits, name_hits = [], []
    full_re = re.compile(re.escape(slug), re.I)
    name_re = re.compile(r"(?<![A-Za-z0-9._-])" + re.escape(name) + r"(?![A-Za-z0-9._-])", re.I) \
        if len(name) >= 5 else None
    for rel, text in sorted(files.items()):
        for m in full_re.finditer(text):
            full_hits.append((rel, text[:m.start()].count("\n") + 1, section_of(text, m.start())))
        if name_re is not None:
            for m in name_re.finditer(text):
                if not full_re.search(text[max(0, m.start() - len(owner) - 1):m.end()]):
                    name_hits.append((rel, text[:m.start()].count("\n") + 1,
                                      section_of(text, m.start())))
    return full_hits, name_hits


def report(slugs, files):
    dup = 0
    for slug in slugs:
        full, byname = find(slug, files)
        if full:
            dup += 1
            print("ALREADY PUBLISHED  %s" % slug)
            seen = set()
            for rel, line, sec in full:
                key = (rel, sec)
                if key in seen:
                    continue
                seen.add(key)
                print("    %s:%d  [%s]" % (rel, line, sec[:96]))
        elif byname:
            print("NAME COLLISION     %s  (the slug is absent; the bare name is present)" % slug)
            seen = set()
            for rel, line, sec in byname[:4]:
                key = (rel, sec)
                if key in seen:
                    continue
                seen.add(key)
                print("    %s:%d  [%s]" % (rel, line, sec[:96]))
        else:
            print("NEW                %s" % slug)
    print("\n# slugs checked: %d   already published: %d" % (len(slugs), dup))
    return dup


def self_test():
    """Offline fixtures.  P126 pt.2: the assertions have to include the case that breaks the
    instrument, so there is a negative control for each of the two ways this gate can be wrong --
    a false NEW (the defect it exists to stop) and a false ALREADY (which would block real work).
    """
    files = {
        "repos/foundations.md": (
            "# Repos\n"
            "## Capa de habla y lectura oral - agregada en el pase 14\n"
            "| [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | MIT |\n"
            "| `kaldi-asr/kaldi` | Apache-2.0 |\n"
            "## Capa QTI\n"
            "| `instructure/qti` | MIT |\n"
        ),
        "verticals/solutions.md": (
            "# Verticales\n"
            "## Capa de autograding - agregada en el pase 5\n"
            "| Autograder.io | https://github.com/eecs-autograder/autograder.io | Docker |\n"
        ),
        "agents/top.md": (
            "# Agentes\n"
            "## Capa Canvas-MCP\n"
            "| `AmirF194/canvas-mcp` | MIT |\n"
        ),
    }
    n = ok = 0

    def check(label, expected, actual):
        nonlocal n, ok
        n += 1
        if expected == actual:
            ok += 1
            print("  ok   %s" % label)
        else:
            print("  FAIL %s\n    expected %r\n    actual   %r" % (label, expected, actual))

    f, _ = find("Halleck45/OpenPronounce", files)
    check("the pase-100 specimen is caught", True, bool(f))
    check("and it names the section that holds it", True,
          any("pase 14" in s for _, _, s in f))
    f, _ = find("eecs-autograder/autograder.io", files)
    check("a slug inside a URL is caught", True, bool(f))
    check("and names the autograding layer", True, any("autograding" in s for _, _, s in f))
    f, _ = find("mikhailvs/loqui", files)
    check("a genuinely new slug is NOT flagged", False, bool(f))
    f, _ = find("kaldi-asr/kaldi", files)
    check("a bare-backticked slug is caught", True, bool(f))

    # NEGATIVE CONTROL 1 -- a different owner for the same repo name must NOT be reported as
    # already published.  This is the fork/namesake case, and calling it a duplicate would
    # SUPPRESS a real alta -- the failure direction that costs this base work rather than
    # accuracy.  The specimen is real: this base inventories `AmirF194/canvas-mcp` and
    # `BartMassey-upstream/canvas-mcp` as separate rows, and the pase 99 measured
    # `examplary/qti` and `instructure/qti` as separate pieces with separate licences.
    f, byname = find("BartMassey-upstream/canvas-mcp", files)
    check("NEG: a namesake under another owner is not a duplicate", False, bool(f))
    check("NEG: but it IS reported as a name collision", True, bool(byname))

    # NEGATIVE CONTROL 2 -- a short, generic repo name must not fire the bare-name probe, or the
    # gate would call everything a collision and get ignored.  P299 in this instrument's own key.
    # `qti` is 3 characters and the inventory holds FOUR distinct owners of it, so without the
    # length gate every QTI alta would arrive pre-flagged.
    _, byname = find("someowner/qti", files)
    check("NEG: a 3-char name does not fire the bare-name probe", False, bool(byname))
    f, _ = find("instructure/qti", files)
    check("NEG: and the real qti slug is still caught by the full form", True, bool(f))

    # NEGATIVE CONTROL 3 -- the gate must not count its own measurement files as publication.
    check("NEG: compose/code is outside the published set", False,
          any(p.startswith("compose/code") for p in PUBLISHED))

    print("\n%d/%d" % (ok, n))
    return 0 if ok == n else 1


def main():
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    if args[0] == "--self-test":
        return self_test()
    files = load(repo_root())
    if not files:
        raise SystemExit("check_duplicate: no published files found")
    slugs = [l.strip() for l in sys.stdin if l.strip()] if args[0] == "--stdin" else args
    return 1 if report(slugs, files) else 0


if __name__ == "__main__":
    sys.exit(main())
