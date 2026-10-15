#!/usr/bin/env python3
"""p223 — the self-claim date gate.

This KB has flagged *"EU AI Act high-risk for education, full effect August
2026"* as stale four times. Every one of those flags was aimed at an INBOUND
source. This gate asks the question the other way round: where does the KB
ASSERT it, in its own prose, as its own instrument line?

A line is a candidate when it carries, in the same line:
  (a) an AI-Act / high-risk / Annex-III token, AND
  (b) an August-2026 *full-application* token (not entry into force, and not
      the Article 50 transparency date, which really is 2026-08-02).

A candidate is then classified, not merely dropped:

  CORRECTED  the line also carries the right date (2027-12-02) or an explicit
             verdict (stale / wrong / contradicts / not verified)  -> clean
  QUOTED     the August-2026 span sits inside quotation marks       -> clean
             (the KB reporting what a source said is evidence, not a defect)
  ATTRIBUTED a reporting verb governs the claim ("one guide puts",
             "reported as") but no verdict follows on the line       -> WARN
  ASSERTED   none of the above: the KB is stating it                 -> FAIL

p222's own `intel/market.md` EMEA opportunity paragraph is an ASSERTED hit, and
the first draft of this gate missed it: a straight quote mark ELSEWHERE on the
line ("EMEA readiness") exonerated the whole line. Scope again — the unit is
the matched SPAN, not the line.

Usage:  python3 gate.py [root]        TSV on stdout; exit 1 on any ASSERTED hit
        python3 gate.py --self-test   run the controls
"""
import re
import sys
import pathlib

SUBJECT = re.compile(r"(ai act|aiact|high-risk|alto riesgo|annex iii|anexo iii)", re.I)

FULL_EFFECT = re.compile(
    r"(?:full(?:y)?[ -]?(?:effect(?:ive)?|application|aplicaci[oó]n)|"
    r"plena (?:vigencia|aplicaci[oó]n)|applies from|taking full effect|effective)"
    r"[^.\n]{0,40}august\s*`?\**\s*2026"
    r"|august\s*`?\**\s*2026\**`?[^.\n]{0,30}(?:full effect|pleno|plena)",
    re.I)

CORRECTED = re.compile(
    r"(2027-12-02|2\s*december\s*`?\**\s*2027|2\s*dic(?:iembre)?\s*`?\**\s*2027"
    r"|stale|wrong|incorrect|contradic|refut|obsolet|not verified|unverified|no verificad)",
    re.I)

ATTRIBUTION = re.compile(
    r"(one guide|some guides|reported as|reportedly|a source|according to|seg[uú]n|"
    r"claims?|says?|roundup|vendor)", re.I)

QUOTE_SPAN = re.compile(r"[\"“‘«'][^\"”’»'\n]{0,200}[\"”’»']")
QUOTE_CHARS = re.compile(r"[\"\u201c\u201d\u2018\u2019\u00ab\u00bb]")


def classify(line: str):
    if not SUBJECT.search(line):
        return None
    m = FULL_EFFECT.search(line)
    if not m:
        return None
    if CORRECTED.search(line):
        return "CORRECTED"
    for q in QUOTE_SPAN.finditer(line):
        if q.start() <= m.start() and m.end() <= q.end():
            return "QUOTED"
    # a quotation that OPENED on an earlier line, or closes on a later one:
    # an unpaired quote character on the same side of the match is enough.
    opens = len(QUOTE_CHARS.findall(line[:m.start()]))
    closes = len(QUOTE_CHARS.findall(line[m.end():]))
    if opens % 2 == 1 or closes % 2 == 1:
        return "QUOTED-MULTILINE"
    head = line[:m.start()]
    if ATTRIBUTION.search(head[-90:]):
        return "ATTRIBUTED"
    return "ASSERTED"


def scan(root: pathlib.Path):
    rows = []
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts or "archive" in md.parts:
            continue  # archive/ is frozen history, not a live claim
        for n, line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            verdict = classify(line)
            if verdict and verdict not in ("CORRECTED", "QUOTED", "QUOTED-MULTILINE"):
                rows.append((verdict, str(md.relative_to(root)), n, line.strip()[:180]))
    return rows


CONTROLS = [
    ("the EU AI Act, fully effective **August 2026**, with education classified **high-risk** — so \"EMEA readiness\" is not one state", "ASSERTED"),
    ("AI Act high-risk for education: full effect August `2026`", "ASSERTED"),
    ("**EU — the `AI Act`.** Reported as taking full effect **August `2026`**, classifying education AI as high-risk", "ATTRIBUTED"),
    ("one guide puts high-risk obligations for education AI at full effect in August `2026`. Not verified against an official source", "CORRECTED"),
    ("Annex III education high-risk applies from 2 December 2027, not August 2026", "CORRECTED"),
    ("the shelf still carries \"high-risk applies from August 2026\" in a vendor FAQ", "QUOTED"),
    ("Article 50 transparency is in force since 2 August 2026", None),
    ("the AI Act entered into force in July 2026", None),
    ("Boston Public Schools makes AI fluency a graduation requirement from September 2026", None),
    ("13% of Italian universities had operational AI governance approaching the August 2026 deadline", None),
    ("EU AI Act classifies education AI as high-risk, with full effect in August 2026.\u201d The source", "QUOTED-MULTILINE"),
]


def self_test() -> int:
    bad = 0
    for text, want in CONTROLS:
        got = classify(text)
        ok = got == want
        bad += 0 if ok else 1
        print(f"{'ok  ' if ok else 'FAIL'}  got={str(got):10} want={str(want):10} {text[:70]}")
    print(f"\n{len(CONTROLS) - bad}/{len(CONTROLS)} controls pass "
          f"({sum(1 for _, w in CONTROLS if w in (None, 'CORRECTED', 'QUOTED'))} of them must NOT fail the build)")
    return 1 if bad else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    rows = scan(root)
    print("verdict\tfile\tline\ttext")
    for v, f, n, t in rows:
        print(f"{v}\t{f}\t{n}\t{t}")
    asserted = sum(1 for r in rows if r[0] == "ASSERTED")
    print(f"# {asserted} ASSERTED, {len(rows) - asserted} ATTRIBUTED", file=sys.stderr)
    sys.exit(1 if asserted else 0)
