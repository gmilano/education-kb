#!/usr/bin/env python3
"""p279 (`p278`'s declared item 1) — MAKE `make claims` A STEP, NOT AN INSTRUCTION.

🔴 Why it exists.  `p278`'s headline was a gate that **exists and was not run**.  `p277`
ranked *"build the payload-vs-metadata CONFLICT class"* **first, at zero searches**, on the
stated ground that *"this base has a grade for payload and a grade for metadata and **no
class at all for CONFLICT**"*.  `p121` had built that class on 2026-10-11 — 249 addresses,
161 manifests, 10 contradictions — and the instance `p277` reported as NEW was **row 8 of
`p121`'s own published table**.

🔵 `make claims TOKEN=conflict` answers `ALREADY CLAIMED … STOP` over **26 cells** and exits
1.  The recipe was correct, documented in the Makefile as *"THE GATE: run before publishing
any 'there is no X'"*, and **nobody ran it** — so `p278` registered the remedy as: *"the next
pass should not be able to publish an absence without it having run."*

🔴 AND "read more carefully" is not the remedy.  `p121`'s class lives in `repos/trending.md`
while `p277` was working in `agents/top.md` and `intel/open-gaps.md`.  On ten shelves and
28,000+ lines, **care does not substitute for running the index**.  A sentence in a Makefile
help string is an instruction; this file is the step.

🟢 THE PREDICATE, kept narrow enough to have no false positives on this base's house style:

    an ABSENCE PHRASE from the vocabulary below, followed by a DISTINCTIVE SUBJECT TOKEN
    (backticked, ALL-CAPS, or slug-shaped) that `carried_index.claims()` already finds on
    the shelves

🔵 Why DISTINCTIVE and not every noun.  The subjects this base writes absences about are
written as `CONFLICT`, `MCP`, `AGPL`, `` `gegok12` `` — capitalised or backticked, because
that is how it names classes and slugs.  Testing every word instead would report
`education` and `licence` as "already claimed" on every line of a 28,000-line corpus and
the gate would be noise within one pass.  A narrow gate that fires is worth more than a
broad one that is ignored.

🔵 POLARITY, copied deliberately from `gate-enumeration`, whose shape this base already
reads correctly:

  * `REFUTED`  — an absence whose own subject is already claimed.  **This FAILS the gate.**
  * `QUEUE`    — absence prose whose subject did not resolve to a distinctive token.  This
    is the BACKLOG, not a failure signal, exactly as `QUEUE-UNENUMERATED` is.

🔴 And the SCOPE is the live pass section, not the whole corpus — the one judgement call in
this file, so it is stated plainly.  The shelves carry hundreds of historical absence
sentences, every one of them already adjudicated by the pass that wrote it; failing on those
would make `make hooks` red on arrival and the gate would be disabled within a pass.  What
`p278` asked for is that **the pass being written now** cannot publish an unchecked absence.
So the fatal arm reads the NEWEST `## Pass` section of `README.md`, and `--census` reads
everything and never fails.
"""
import re
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "p235-carried-index"))
import carried_index  # noqa: E402  -- the index IS the gate; this file only makes it a step

# 🔵 The absence vocabulary.  Every phrase here is one this base has actually written; the
# first is `p277`'s verbatim.  Not lazy: `ACTION TB`'s lint runs over this directory.
ABSENCE = [
    r"no class at all for",
    r"there is no",
    r"there are no",
    r"this base has no",
    r"has no class for",
    r"no dominant",
    r"nothing on",
    r"no such",
    r"none exists",
    r"does not exist on",
    r"is absent from",
    r"no binding",
    r"not carried",
    r"never built",
    r"no gate on this base",
]
ABSENCE_RE = re.compile("(" + "|".join(ABSENCE) + ")", re.IGNORECASE)

# A distinctive subject: a backticked span, an ALL-CAPS word, or an owner/repo slug.
BACKTICKED = re.compile(r"`([^`]+)`")
ALLCAPS = re.compile(r"\b([A-Z][A-Z0-9_-]{2,})\b")
SLUGLIKE = re.compile(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b")

# 🔵 ALL-CAPS words that are STRUCTURE on this base, never a subject.  Each one of these
# fired on a draft of this gate over the real README and had to be excluded by name.
NOT_SUBJECTS = {
    "STOP", "PASS", "FAIL", "FAILED", "NEW", "GREY", "RED", "TSV", "URL", "SHA", "HEAD",
    "AND", "NOT", "THE", "FOR", "ALL", "ANY", "ONE", "TWO", "SIX", "TEN", "NOW", "WAS",
    "ACTION", "QUEUE", "REFUTED", "CARRIED", "CLAIMED", "ALREADY", "NONE", "YES", "NO",
    "README", "MIT", "BSD", "ISC", "GPL", "LGPL", "AGPL", "SPDX", "OSI", "CAGR", "USD",
    "EUR", "GBP", "LMS", "SIS", "ERP", "CRM", "API", "CLI", "SDK", "LLM", "LLMS", "RAG",
    "VERIFIED", "UNRESOLVED", "UNPLACEABLE", "NO-CHANNEL", "STALE", "OK", "WIP",
}
# Words whose claim-count is structurally meaningless: they are on every shelf by
# construction, so an `ALREADY CLAIMED` on them says nothing about the absence.
TOO_COMMON = {"education", "licence", "license", "repo", "repos", "agent", "agents",
              "github", "base", "shelf", "shelves", "pass", "row", "rows", "gate"}

SENTENCE_END = re.compile(r"[.;:!?]")

# 🔴 THE FALSE POSITIVE THAT THIS GATE FOUND ON ITS FIRST REAL RUN, and the shape matters
# more than the fix.  Run over the live pass section, the first draft reported `p278`'s own
# headline as `REFUTED conflict`.  It was RIGHT about the text and WRONG about the act:
# `p278` was QUOTING `p277`'s sentence in order to document the error, which is the opposite
# of committing it.  A pass that reports "`p277` wrote: there is no X" asserts nothing about
# X, so a gate that cannot tell an assertion from a report would punish every pass that does
# the forensic write-up this base is built on — and would have been disabled within a pass.
# 🔵 The house quoting style is `*"…"*` and the markdown blockquote, so both are excluded,
# and a QUOTED hit is still REPORTED rather than dropped: a pass could quote itself to
# evade the gate, and the output has to make that visible if it ever happens.
# 🔴 AND THE FIRST FIX WAS ITSELF THE WRONG SHAPE, measured on the real README rather than
# read.  Quote parity computed PER LINE still reported `p278`'s headline as an assertion,
# because the sentence WRAPS: the opening `*"` sits on the line above the absence phrase, so
# a line-local scan sees zero quote marks before it.  🔵 That is exactly the class `p278`
# repaired in its own anchors — *"an anchor that breaks when a paragraph is reflowed is the
# same brittleness class as one copied from the number it checks"* — so a line-local
# predicate over a hard-wrapped corpus is the same defect one layer out.  Quote state is
# therefore tracked across the PARAGRAPH, which is the unit a reflow preserves.
QUOTE_CHARS = '"“”'


def in_quote(block, pos):
    """Is `pos` inside a quoted span of `block`, i.e. a REPORT of an absence rather than
    an assertion of one?  `block` is a PARAGRAPH, never a single line: see above."""
    head = block[:pos]
    if head.split("\n")[-1].lstrip().startswith(">") or block.lstrip().startswith(">"):
        return True
    return sum(1 for ch in head if ch in QUOTE_CHARS) % 2 == 1


def subjects_in(tail):
    """-> the distinctive tokens in the clause FOLLOWING an absence phrase.

    The clause ends at the first sentence boundary: an absence sentence's subject is in
    that sentence, and reading past it collects the subject of the NEXT claim.
    """
    cut = SENTENCE_END.search(tail)
    clause = tail[: cut.start()] if cut else tail
    out = []
    for raw in BACKTICKED.findall(clause):
        out.append(raw)
    for raw in SLUGLIKE.findall(clause):
        out.append(raw)
    for raw in ALLCAPS.findall(clause):
        if raw.upper() not in NOT_SUBJECTS:
            out.append(raw)
    seen, uniq = set(), []
    for tok in out:
        t = tok.strip().strip("`*_,.()[]").lower()
        # a bare `**` emphasis span or a one-word stopword is not a subject
        if len(t) < 3 or t in TOO_COMMON or t in seen:
            continue
        seen.add(t)
        uniq.append(t)
    return uniq


def findings(text, root=".", exclude_shelf=None):
    """-> (refuted, queued, quoted).  `refuted` is the fatal list: an absence this text
    ASSERTS whose subject the shelves already claim.  `queued` is absence prose with no
    resolvable subject.  `quoted` is an absence this text REPORTS -- visible, not fatal."""
    refuted, queued, quoted = [], [], []
    cache = {}
    # Paragraphs, not lines: the quote span that decides assertion-vs-report survives a
    # reflow only at paragraph scope.  Line numbers are recovered by counting newlines.
    offset, lineno_at = 0, 1
    for block in re.split(r"\n[ \t]*\n", text):
        for m in ABSENCE_RE.finditer(block):
            lineno = lineno_at + block[: m.start()].count("\n")
            # The subject clause may itself wrap, so read the rest of the PARAGRAPH and let
            # the sentence boundary end it -- not the rest of the physical line.
            toks = subjects_in(block[m.end():].replace("\n", " "))
            snippet = " ".join(block[m.start(): m.start() + 120].split())
            if not toks:
                queued.append((lineno, m.group(1), snippet))
                continue
            for tok in toks:
                if tok not in cache:
                    cache[tok] = carried_index.claims(tok, root)
                hits = dict(cache[tok])
                if exclude_shelf:
                    hits.pop(exclude_shelf, None)
                if not hits:
                    continue
                target = quoted if in_quote(block, m.start()) else refuted
                target.append((lineno, m.group(1), tok, hits, snippet))
        lineno_at += block.count("\n") + 2
        offset += len(block)
    return refuted, queued, quoted


def latest_pass_section(readme):
    """The newest `## Pass` block — what the pass being written now is publishing."""
    lines = readme.splitlines()
    starts = [i for i, l in enumerate(lines) if l.startswith("## Pass ")]
    if not starts:
        return ""
    return "\n".join(lines[starts[0]: starts[1] if len(starts) > 1 else len(lines)])


def main(argv):
    root = "."
    census = "--census" in argv
    for i, a in enumerate(argv):
        if a == "--root" and i + 1 < len(argv):
            root = argv[i + 1]
    try:
        readme = open(f"{root}/README.md", encoding="utf-8", errors="replace").read()
    except FileNotFoundError:
        print("🔴 p279-absence-claims: no README.md at --root", file=sys.stderr)
        return 1

    if census:
        # The whole-corpus arm: a measurement, never a failure.  This is the backlog.
        total_r, total_q, total_quoted = 0, 0, 0
        for shelf in carried_index.SHELVES:
            try:
                body = open(f"{root}/{shelf}", encoding="utf-8", errors="replace").read()
            except FileNotFoundError:
                continue
            r, q, qt = findings(body, root, exclude_shelf=shelf)
            total_r += len(r)
            total_q += len(q)
            total_quoted += len(qt)
            if r:
                print(f"CENSUS\t{shelf}\trefuted={len(r)}\tqueued={len(q)}\tquoted={len(qt)}")
        print(f"# CENSUS-REFUTED={total_r} CENSUS-QUEUED={total_q} CENSUS-QUOTED={total_quoted}")
        print("#   (a census is a measurement -- it does not fail the gate)")
        return 0

    section = latest_pass_section(readme)
    if not section.strip():
        print("🔴 p279-absence-claims: README.md has no `## Pass ` section to check")
        return 1
    refuted, queued, quoted = findings(section, root, exclude_shelf="README.md")
    for lineno, phrase, tok, hits, line in refuted:
        where = "  ".join(f"{s}:{n}" for s, n in sorted(hits.items(), key=lambda kv: -kv[1]))
        print(f"REFUTED\t{tok}\t{phrase!r}\t{where}")
        print(f"\t{line}")
    # A quoted absence is the forensic write-up, not a claim -- but it is printed, because
    # a pass quoting ITSELF to get past this gate must be visible in the gate's own output.
    for lineno, phrase, tok, hits, line in quoted:
        print(f"QUOTED\t{tok}\t{phrase!r}\t(a report of an absence, not an assertion)")
    print(f"# ABSENCE-REFUTED={len(refuted)} ABSENCE-QUEUED={len(queued)} "
          f"ABSENCE-QUOTED={len(quoted)}"
          f"  (live pass section, {len(section.splitlines())} lines)")
    if refuted:
        print("🔴 FAIL — this pass publishes an absence whose subject the shelves already "
              "claim.  Read those cells, as `p277` did not.")
        return 1
    print("🟢 PASS — every absence in the live pass section was checked against the index.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
