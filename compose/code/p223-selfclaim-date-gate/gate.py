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

# 🟢 p279: `digital omnibus` joins the subject vocabulary.  `ACTION SH`'s first real run
# caught one of the TWO stale assertions in its own inbound file and missed the other,
# because the missed sentence names only the instrument that AMENDS the Act -- and this
# base's own note records the Omnibus "AMENDS Regulation (EU) 2024/1689, the AI Act".
# A table that knows the Act and not its amending instrument has a hole the size of every
# source that writes about the delay rather than the Act.
SUBJECT = re.compile(
    r"(ai act|aiact|high-risk|alto riesgo|annex iii|anexo iii|digital omnibus)", re.I)

# 🔴 p282: the onset vocabulary was ONE INFLECTION WIDE.  `applies from` was the only
# "starts on this date" spelling the table carried, and the subject of this sentence in the
# wild is almost always PLURAL -- "requirements apply from", "obligations apply from",
# "duties apply from" -- so the spelling a source actually writes was the one not matched.
# Measured, not read: this pass's own mandated EMEA leg returned *"requirements for
# high-risk AI systems apply from August 2026"* and `make inbound-claims` reported `0`.
# 🔵 Same class as the `august 2, 2026` miss p279 recorded one arm below: the table knew a
# spelling of the claim rather than the claim.
FULL_EFFECT = re.compile(
    r"(?:full(?:y)?[ -]?(?:effect(?:ive)?|application|aplicaci[oó]n)|"
    r"plena (?:vigencia|aplicaci[oó]n)|applies from|taking full effect|effective"
    r"|appl(?:y|ies|ied)\s+(?:from|as of|in)"
    r"|in force\s+(?:from|as of|on)"
    r"|com(?:e|es|ing)\s+into\s+(?:force|effect|application)"
    r"|tak(?:e|es|ing)\s+effect"
    r"|entra(?:n)?\s+en\s+vigor"
    r"|begin(?:s|ning)?\s+(?:from|in|on)"
    r"|start(?:s|ing)?\s+(?:from|in|on)"
    r"|kick(?:s)?\s+in)"
    # 🟢 p282: the DAY-number spelling, on every arm rather than only on `remains`.
    # p279 found `August 2, 2026` defeating an arm that spelled the date `august\s*2026`
    # and fixed it in that one arm; the same hole was open in this one.
    r"[^.\n]{0,40}august\s*`?\**\s*(?:\d{1,2}\s*,?\s*)?2026"
    r"|august\s*`?\**\s*2026\**`?[^.\n]{0,30}(?:full effect|pleno|plena)"
    # 🟢 p279: the "it has NOT moved" shape, which asserts the stale date by denying the
    # correction rather than by stating an effective date.  Narrowly bound to an
    # obligation/deadline/date subject so that a bare "approaching the August 2026
    # deadline" -- a true sentence about Article 50 -- is still not a hit.
    # 🔴 And the first cut of THIS arm missed its own motivating sentence, because it
    # spelled the date `august\s*2026` while the source wrote "August 2, 2026" -- a DAY
    # number between the month and the year.  `2026-08-02` is the date the whole table is
    # about, so the one spelling a reader would actually meet was the one not matched.
    r"|(?:obligation|deadline|date)\s+remains[^.\n]{0,20}august[^.\n]{0,8}2026"
    r"|remains\s+(?:at\s+)?august[^.\n]{0,8}2026",
    re.I)

CORRECTED = re.compile(
    r"(2027-12-02|2\s*december\s*`?\**\s*2027|2\s*dic(?:iembre)?\s*`?\**\s*2027"
    r"|stale|wrong|incorrect|contradic|refut|obsolet|not verified|unverified|no verificad)",
    re.I)

# 🟢 p282: `2026-08-02` REALLY IS Article 50's date, so a line about transparency or
# marking that says nothing about the high-risk tier is a TRUE sentence and must not be
# flagged.  The narrow `applies from` arm never reached these; the widened onset arms above
# do, so the exemption is now load-bearing and is pinned by controls in both directions.
ARTICLE50_TRUE = re.compile(r"(article\s*50|art\.?\s*50|transparency|marking)", re.I)
HIGH_RISK = re.compile(r"(high-risk|alto riesgo|annex iii|anexo iii)", re.I)

ATTRIBUTION = re.compile(
    r"(one guide|some guides|reported as|reportedly|a source|according to|seg[uú]n|"
    r"claims?|says?|roundup|vendor)", re.I)

# 🟢 p282: the span may WRAP.  `[^...\n]` confined a quoted span to one physical line, so a
# forensic quotation that hard-wraps -- the shape this base's write-ups are made of -- read as
# an assertion.  That is exactly the defect `p279` repaired in `p279-absence-claims`
# (*"a line-local predicate over a hard-wrapped corpus is the same defect one layer out"*),
# live in a SIBLING instrument that was never re-read for it.
QUOTE_SPAN = re.compile(r"[\"“‘«'][^\"”’»']{0,400}[\"”’»']")
QUOTE_CHARS = re.compile(r"[\"\u201c\u201d\u2018\u2019\u00ab\u00bb]")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s")


def _sentence_around(block: str, start: int, end: int) -> str:
    """-> the sentence containing the match.  The Article-50 exemption is a property of the
    CLAIM, not of its neighbours, so it is read at sentence scope even though CORRECTED and
    the quote predicate are read at paragraph scope."""
    head = block[:start]
    cuts = [m.end() for m in SENT_SPLIT.finditer(head)]
    lo = cuts[-1] if cuts else 0
    nxt = SENT_SPLIT.search(block, end)
    return block[lo: nxt.start() if nxt else len(block)]


def classify_block(block: str, m):
    """Classify one FULL_EFFECT match inside `block`, which is a paragraph or a table row."""
    sent = _sentence_around(block, m.start(), m.end())
    # p282: a true Article-50 sentence is not a stale claim.  Sentence scope, so that naming
    # Article 50 elsewhere in a paragraph cannot launder a high-risk assertion.
    if ARTICLE50_TRUE.search(sent) and not HIGH_RISK.search(sent):
        return None
    if block.lstrip().startswith(">") or \
            block[:m.start()].split("\n")[-1].lstrip().startswith(">"):
        return "QUOTED"
    if CORRECTED.search(block):
        return "CORRECTED"
    for q in QUOTE_SPAN.finditer(block):
        if q.start() <= m.start() and m.end() <= q.end():
            return "QUOTED"
    # a quotation that OPENED earlier in the paragraph, or closes later in it:
    # an unpaired quote character on the same side of the match is enough.
    opens = len(QUOTE_CHARS.findall(block[:m.start()]))
    closes = len(QUOTE_CHARS.findall(block[m.end():]))
    if opens % 2 == 1 or closes % 2 == 1:
        return "QUOTED-MULTILINE"
    head = block[:m.start()].replace("\n", " ")
    if ATTRIBUTION.search(head[-90:]):
        return "ATTRIBUTED"
    return "ASSERTED"


def classify(line: str):
    """Single-unit entry point -- the controls' interface, and correct for any unit that does
    not wrap."""
    if not SUBJECT.search(line):
        return None
    m = FULL_EFFECT.search(line)
    if not m:
        return None
    return classify_block(line, m)


def units(text: str):
    """-> (unit_text, first_lineno) over the whole text.

    🟢 p282.  The unit is the PARAGRAPH, because that is what a reflow preserves and what
    `p279` established for the sibling gate -- **except that a markdown TABLE ROW is its own
    unit**.  A table is one block of text and many independent claims: read at block scope,
    one row's `refuted` or `2 December 2027` would launder the stale assertion sitting in the
    row beside it.  Measured on this corpus, not reasoned about: the live `ASSERTED` cell this
    pass found sits in a table whose other rows carry correction vocabulary.
    """
    lineno = 1
    for block in re.split(r"\n[ \t]*\n", text):
        buf, buf_start = [], lineno
        n = lineno
        for line in block.split("\n"):
            if line.lstrip().startswith("|"):
                if buf:
                    yield "\n".join(buf), buf_start
                    buf = []
                yield line, n
            else:
                if not buf:
                    buf_start = n
                buf.append(line)
            n += 1
        if buf:
            yield "\n".join(buf), buf_start
        lineno = n + 1


def scan(root: pathlib.Path):
    rows = []
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts or "archive" in md.parts:
            continue  # archive/ is frozen history, not a live claim
        text = md.read_text(encoding="utf-8", errors="replace")
        for unit, n in units(text):
            if not SUBJECT.search(unit):
                continue
            for m in FULL_EFFECT.finditer(unit):
                verdict = classify_block(unit, m)
                if verdict and verdict not in ("CORRECTED", "QUOTED", "QUOTED-MULTILINE"):
                    ln = n + unit[: m.start()].count("\n")
                    snippet = " ".join(unit.split())[:180]
                    rows.append((verdict, str(md.relative_to(root)), ln, snippet))
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
    # --- p279: the shapes ACTION SH's first inbound run exposed -------------------------
    ("until a formal legislative extension is enacted, the AI Act legal obligation remains August 2, 2026", "ASSERTED"),
    ("the Digital Omnibus is not adopted, so the deadline remains August 2026", "ASSERTED"),
    ("13% of Italian universities had operational AI governance approaching the August 2026 high-risk deadline", None),
    # Not a candidate at all: no August-2026 claim is made, so there is nothing to correct.
    # (This control was first written expecting CORRECTED -- wrongly.  CORRECTED is a verdict
    # on a line that DOES carry the stale date and also carries its refutation.)
    ("the Digital Omnibus moved Annex III education high-risk to 2 December 2027", None),
    # --- p282: the PLURAL-SUBJECT onset, which is the spelling sources actually write ----
    # Control Zero is this pass's own EMEA leg, verbatim.  It returned `0` hits.
    ("One guide says requirements for high-risk AI systems apply from August 2026.", "ATTRIBUTED"),
    ("requirements for high-risk AI systems apply from August 2026", "ASSERTED"),
    ("Annex III education duties come into force in August 2026", "ASSERTED"),
    ("high-risk obligations take effect in August 2026", "ASSERTED"),
    ("AI Act high-risk rules start in August 2026", "ASSERTED"),
    ("high-risk obligations kick in in August 2026", "ASSERTED"),
    ("las obligaciones de alto riesgo entran en vigor en August 2026", "ASSERTED"),
    ("AI Act high-risk duties apply from August 2, 2026", "ASSERTED"),
    # The ARTICLE50_TRUE exemption, both directions.  2026-08-02 IS Article 50's date.
    ("Article 50 transparency obligations apply from 2 August 2026", None),
    ("the AI Act's marking duties take effect in August 2026", None),
    # ...but naming Article 50 does not launder a high-risk claim in the same sentence.
    ("unlike Article 50, Annex III education high-risk applies from August 2026", "ASSERTED"),
]

# 🟢 p282 — the UNIT controls.  `classify()` sees one unit; these pin what a unit IS, which
# is the half that decided all three live cells this pass found.
UNIT_CONTROLS = [
    # 1. A forensic quotation that HARD-WRAPS.  agents/trending.md:19652 in the live corpus:
    #    the stale row is quoted across a line break and refuted in the next sentence.
    ("""`intel/trends.md` trend 39 carried, in its headline table: **`EU AI Act, high-risk
obligations | Apply from August 2026 — in force now`**. That is **wrong**, and this KB
already knew it.""", "CORRECTED"),
    # 2. The same shape with the correction only in the WRAPPED tail -- line scope misses it.
    ("""EU AI Act high-risk duties for education apply from August 2026, a claim these
shelves have refuted.""", "CORRECTED"),
    # 3. 🔴 THE TABLE-ROW UNIT.  Two rows of ONE markdown table: row A asserts the stale
    #    claim, row B carries correction vocabulary.  At paragraph scope row B launders row
    #    A and the gate reports nothing.  Each row must be judged on its own bytes.
    ("| EMEA | EU AI Act high-risk duties for education apply from August 2026 |", "ASSERTED"),
    ("| APAC | Vietnam's regime is not refuted; it is in force 2027-03-01 |", None),
    # 4. A blockquote is a report, not an assertion.
    ("> EU AI Act high-risk obligations apply from August 2026", "QUOTED"),
]


def unit_self_test() -> int:
    """The unit controls run through the SAME classifier, over `units()` where the control
    is multi-line, so a control cannot pass against a code path the corpus does not use."""
    bad = 0
    for text, want in UNIT_CONTROLS:
        got = None
        for unit, _ in units(text):
            if not SUBJECT.search(unit):
                continue
            m = FULL_EFFECT.search(unit)
            if m:
                got = classify_block(unit, m)
                break
        ok = got == want
        bad += 0 if ok else 1
        flat = " ".join(text.split())[:66]
        print(f"{'ok  ' if ok else 'FAIL'}  got={str(got):10} want={str(want):10} {flat}")
    print(f"{len(UNIT_CONTROLS) - bad}/{len(UNIT_CONTROLS)} unit controls pass")
    return 1 if bad else 0


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


def inbound(path) -> int:
    """🟢 p279 — `ACTION SH`, registered since p226 and never built.

    `ACTION SA`'s gate watches OUTBOUND prose: where does the KB assert the stale claim?
    `ACTION SH` asks it of the INBOUND side -- where does a source this pass just read
    assert it? -- and it is the same table, so it is the same classifier and NOT a second
    implementation of one.

    🔴 Why it is worth a recipe.  The *"education high-risk from August 2026"* claim has now
    arrived from an inbound source in FIVE separate passes, each time from a source these
    shelves do not cite, and each time it was caught by a person reading carefully.  `p279`'s
    own mandated EMEA leg returned it again, which is the fifth.  A claim this base refuted
    on 2026-10-15 should not need re-adjudicating by hand every hour.

    🔵 Polarity is `make claims`'s: exit 1 is the STOP signal.  An inbound stale claim is not
    a defect in the KB -- nothing is wrong on a shelf -- so this stays OUT of `make hooks`
    and is run against a research file BEFORE its findings are written up.
    """
    text = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    hits = []
    for unit, n in units(text):
        if not SUBJECT.search(unit):
            continue
        for m in FULL_EFFECT.finditer(unit):
            v = classify_block(unit, m)
            # QUOTED/CORRECTED are clean OUTBOUND, because they mean the KB is reporting or
            # fixing the claim.  INBOUND there is no such exemption: the source asserting it
            # inside quotation marks is still the source asserting it.
            if v and v != "CORRECTED":
                ln = n + unit[: m.start()].count("\n")
                hits.append((v, ln, " ".join(unit.split())[:160]))
    print("verdict\tline\ttext")
    for v, n, t in hits:
        print(f"{v}\t{n}\t{t}")
    print(f"# {len(hits)} inbound stale-claim hit(s) in {path}")
    if hits:
        print("🔴 STOP — a source read this pass asserts a claim these shelves have already "
              "refuted.  Annex III point 3 (education) applies 2027-12-02; 2026-08-02 is "
              "Article 50 transparency.  Do NOT shelve this.")
        return 1
    print("🟢 no refuted date-claim in this inbound text")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test() or unit_self_test())
    if "--inbound" in sys.argv:
        sys.exit(inbound(sys.argv[sys.argv.index("--inbound") + 1]))
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    rows = scan(root)
    print("verdict\tfile\tline\ttext")
    for v, f, n, t in rows:
        print(f"{v}\t{f}\t{n}\t{t}")
    asserted = sum(1 for r in rows if r[0] == "ASSERTED")
    print(f"# {asserted} ASSERTED, {len(rows) - asserted} ATTRIBUTED", file=sys.stderr)
    sys.exit(1 if asserted else 0)
