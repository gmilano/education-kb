#!/usr/bin/env python3
"""gap-register-audit.py -- the instrument Gap 551-A demanded (p551).

WHY THIS EXISTS
  p550 registered six gaps -- 550-A through 550-F -- in its per-page pass
  sections, with reasons, measurements and asks, cited across five and six files
  each including its own `compose/code/` READMEs. NONE of the six reached
  `intel/open-gaps.md`, whose newest section is still p549's. Verified by grep
  for the bare id, so it is not a matcher artefact: zero occurrences in any
  form, on the one page a successor reads to find out what is owed.

  This is the defect class p546 named one level down: a figure typed into prose
  by the pass that computed it, with the rule left in that pass's head. Here it
  is a GAP announced in prose by the pass that found it, with the registration
  left in that pass's intent. p550's own Gap 550-A says it exactly -- "a
  correction announced in prose is not a correction" -- and p550 then committed
  the same error one object up: a gap announced in prose is not a registered gap.

🔴 WHAT THIS INSTRUMENT CANNOT DO, STATED FIRST
  It cannot tell you how big the leak is, and p551 refuses to publish a figure
  for it. Two honest matcher dialects disagree by nearly 4x on this corpus:

      worded    `Gap NNN-X`        registered 610  cited 505  MISSING 125
      any_form  bare `NNN-X` too   registered 874  cited 1066 MISSING 481

  `worded` MISSES real registrations -- `547-I` sits on the register seven times
  as a bare backticked id with no preceding "Gap", so worded calls it missing
  when it is not. `any_form` over-collects, reaching back to `100-A` and picking
  up tokens from id spaces that are not gaps at all. This is exactly p546's
  five-rules-five-counts situation, and p546's verdict applies unchanged: "This
  is not a claim that p545 was wrong -- it is a claim that nobody can tell."

  So the AGGREGATE is not evidence. MEMBERSHIP for a named id is, because
  `--gap` answers it by substring across every form at once, which is the one
  question no dialect can disagree about. Use `--gap`; quote `--audit` only as
  a dialect-labelled pair of upper bounds, never as "the leak".

WHAT IT GUARANTEES
  1. Both sides are read from the files, never from a pass's recollection.
  2. No rule is privileged by being the only one printed -- both dialects report,
     p547's address-count.py convention applied to a second instrument.
  3. A gap counts as registered only if it reaches `intel/open-gaps.md`. The
     register is the authority; a mention elsewhere is a citation, which is
     p550's Gap 550-D distinction ("citation is not attribution") applied to
     gaps instead of rows.
  4. `--gap ID` exits non-zero when that id is cited in pass sections and absent
     from the register, so a pass CAN be gated on its own registrations landing
     without depending on an unmeasurable total.

USAGE
    python3 ingest/gap-register-audit.py --gap 550-A [550-B ...]   # membership
    python3 ingest/gap-register-audit.py --audit                   # both dialects
    python3 ingest/gap-register-audit.py --tsv                     # evidence store
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTER = "intel/open-gaps.md"
PAGES = [
    "agents/top.md", "agents/trending.md",
    "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md",
    "compose/patterns.md", "intel/measured-unusable.md", "README.md",
]

# Named, both reported. Neither is designated canonical for the AGGREGATE,
# because p551 measured that the aggregate is dialect-dependent and withdrew it.
RULES = {
    "worded": re.compile(r"\bGap\s+(\d{3})-([A-Z])\b"),
    "any_form": re.compile(r"(?<![\d.\-])(\d{3})-([A-Z])(?![A-Za-z0-9])"),
}


def text(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def gaps(rel, rx):
    out = {}
    for n, line in enumerate(text(rel).splitlines(), 1):
        for m in rx.finditer(line):
            out.setdefault(f"{m.group(1)}-{m.group(2)}", n)
    return out


def sort_key(g):
    num, letter = g.split("-")
    return (int(num), letter)


def membership(ids):
    """Dialect-independent: substring presence, every written form at once."""
    reg = text(REGISTER)
    rows, bad = [], 0
    for gid in ids:
        on_register = reg.count(gid)
        cites = [pg for pg in PAGES if gid in text(pg)]
        # compose/code READMEs are pass artefacts too; p550 cited gaps there.
        for extra in sorted(ROOT.glob("compose/code/*/README.md")):
            if gid in extra.read_text(encoding="utf-8"):
                cites.append(str(extra.relative_to(ROOT)))
        status = "REGISTERED" if on_register else (
            "MISSING-FROM-REGISTER" if cites else "UNKNOWN-ID")
        if status == "MISSING-FROM-REGISTER":
            bad += 1
        rows.append((gid, status, on_register, cites))
    return rows, bad


def main(argv):
    if "--gap" in argv:
        ids = [a for a in argv[argv.index("--gap") + 1:] if not a.startswith("--")]
        if not ids:
            sys.exit("gap-register-audit: --gap needs at least one id, e.g. 550-A")
        rows, bad = membership(ids)
        print("gap\tstatus\ton_register\tcited_in")
        for gid, status, n, cites in rows:
            print(f"{gid}\t{status}\t{n}\t{','.join(cites) or '-'}")
        return 1 if bad else 0

    tsv = "--tsv" in argv
    if tsv:
        print("rule\tregistered\tcited\tmissing\tmissing_ids")
    for name, rx in RULES.items():
        reg = gaps(REGISTER, rx)
        cited = {}
        for pg in PAGES:
            for g, ln in gaps(pg, rx).items():
                cited.setdefault(g, (pg, ln))
        missing = sorted((g for g in cited if g not in reg), key=sort_key)
        if tsv:
            print(f"{name}\t{len(reg)}\t{len(cited)}\t{len(missing)}\t{' '.join(missing)}")
        else:
            print(f"{name}\tregistered={len(reg)}\tcited={len(cited)}\tMISSING={len(missing)}")
    if not tsv:
        print()
        print("🔴 The two dialects disagree. Neither MISSING figure is this base's")
        print("   leak size; both are dialect-labelled upper bounds. Use --gap for")
        print("   a membership answer that no dialect can dispute.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
