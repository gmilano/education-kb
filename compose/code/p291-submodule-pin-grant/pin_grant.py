"""`ACTION p291` — a submodule grant is verified AT THE PIN, and HEAD is not the question.

🔵 What p290 built and what this corrects.
`p290` found a 7-segment MIT configuration set whose content is seven `160000 commit`
gitlinks, and wrote down the first rule this base ever had for that shape:

    a submodule's grant is verified when (1) its own payload is read first-hand AND
    (2) the HEAD it was read at EQUALS the pinned gitlink SHA.

🔴 Condition (2) is the defect this module exists to remove.  `p290` read each submodule at
HEAD because that is what `git ls-remote` returns, and then had to *check* HEAD against the
pin.  But `raw.githubusercontent.com` serves a payload AT AN ARBITRARY COMMIT -- the pinned
SHA is a valid ref -- so the grant that a `--recurse-submodules` clone actually lands on can
be read DIRECTLY.  Measured p291: 7/7 segments answered `200` at their pinned SHA.

Why the difference is not cosmetic:

| submodule state | `p290`'s rule | the truth |
|---|---|---|
| HEAD == pin | GRANTED-AT-PIN | GRANTED-AT-PIN |
| HEAD moved past pin | 🔴 UNVERIFIED-AT-PIN | 🟢 **still readable at the pin** |
| HEAD relicensed after the pin | 🔴 UNVERIFIED-AT-PIN | 🟢 **the pin's grant is the one that binds** |

🔴 `p290`'s rule is wrong in the RESTRICTIVE direction, and the restrictive direction is the
dangerous one here: it reports "cannot verify" for a repository whose grant is sitting there
readable, so a later pass re-probes it, finds HEAD relicensed, and publishes the WRONG
licence -- the one at HEAD rather than the one the superproject pins.  A vendoring studio
receives the pin.

🟢 THE RULE THIS MODULE WRITES DOWN AND GATES:

    A submodule's grant is GRANTED-AT-PIN when its own payload is read first-hand
    AT THE PINNED GITLINK SHA.  The submodule's HEAD is not an input.

A row that was read at HEAD is `READ-AT-HEAD` and is NOT a verification, however equal the
two SHAs happened to be on the day it was measured -- equality is a coincidence of timing,
not a property of the evidence.  That is control `C7` below and it is what fails `p290`'s
own two rows if they are ever re-asserted without re-reading.
"""

import os
import re
import sys

# The closed verdict vocabulary.  A verdict outside it is a gate failure, not a new value:
# this base has twice grown a bucket per spelling variant and then lost the filter.
VERDICTS = (
    "GRANTED-AT-PIN",      # payload read first-hand AT the pinned SHA
    "NO-GRANT-AT-PIN",     # read at the pin, and there is no grant there
    "UNVERIFIED-AT-PIN",   # the pin was not read (unreachable, refused, not attempted)
    "UNPROBED",            # declared backlog -- never a pass, but honest
)
VERIFIED = ("GRANTED-AT-PIN", "NO-GRANT-AT-PIN")  # verdicts that rest on a first-hand read

SHELVES = ("agents/top.md", "repos/foundations.md", "verticals/solutions.md",
           "repos/trending.md", "agents/trending.md", "compose/patterns.md")

FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
SHORT_SHA = re.compile(r"^[0-9a-f]{12}$")


def _short(sha):
    return sha[:12] if sha and FULL_SHA.match(sha) else sha


def classify(row):
    """Grade ONE submodule row.  `row` is the parsed TSV mapping.

    Returns (verdict, [findings]).  A finding is a sentence naming what is wrong.
    """
    findings = []
    slug = row.get("submodule_slug", "?")
    pinned = (row.get("pinned_gitlink_sha") or "").strip()
    read_at = (row.get("read_at_ref") or "").strip()
    payload = (row.get("payload_sha256_12") or "").strip()
    declared = (row.get("verdict") or "").strip()

    if declared not in VERDICTS:
        findings.append(
            f"{slug}: verdict {declared!r} is outside the closed vocabulary {VERDICTS}")
        return declared, findings

    if not FULL_SHA.match(pinned):
        findings.append(
            f"{slug}: pinned_gitlink_sha {pinned!r} is not a 40-hex gitlink. "
            "A pin that is not an exact commit cannot be read at.")

    if declared in VERIFIED:
        # C7 -- the whole point of ACTION p291.
        if read_at.upper() in ("HEAD", "MAIN", "MASTER", ""):
            findings.append(
                f"{slug}: verdict {declared} rests on a read at {read_at or '(unrecorded)'}, "
                "not at the pin. p290's rule accepted this when HEAD happened to equal the "
                "pin; equality on the day of measurement is timing, not evidence. "
                "Re-read at the pinned SHA.")
        elif FULL_SHA.match(read_at) and FULL_SHA.match(pinned) and read_at != pinned:
            findings.append(
                f"{slug}: read at {_short(read_at)} but the superproject pins "
                f"{_short(pinned)}. The grant read is not the grant a recursive clone lands on.")

    if declared == "GRANTED-AT-PIN" and not SHORT_SHA.match(payload):
        findings.append(
            f"{slug}: GRANTED-AT-PIN with no payload_sha256_12. A grant verdict with no "
            "payload digest is a claim, not a read.")

    if declared == "NO-GRANT-AT-PIN" and payload and payload != "-":
        findings.append(
            f"{slug}: NO-GRANT-AT-PIN but a payload digest {payload} is recorded.")

    return declared, findings


def parse_tsv(text):
    """Parse an evidence TSV: `#` comments, one header line, then rows."""
    rows, header = [], None
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cells = line.split("\t")
        if header is None:
            header = [c.strip() for c in cells]
            continue
        rows.append(dict(zip(header, [c.strip() for c in cells])))
    return rows


def census(rows):
    """Every submodule the superproject declares must carry a row.

    🔴 The failure this catches: probing 2 of 7 segments and publishing the superproject's
    single MIT badge for the set.  That is p290's own declared residue, and until it is a
    gate it is a sentence in a README that a later pass can forget.
    """
    findings = []
    by_super = {}
    for r in rows:
        by_super.setdefault(r.get("superproject", "?"), []).append(r)
    for sup, rs in sorted(by_super.items()):
        declared = {r.get("submodule_path") for r in rs}
        expected = {p.strip() for p in (rs[0].get("declares_submodule_paths") or "").split(",")
                    if p.strip()}
        missing = expected - declared
        if missing:
            findings.append(
                f"{sup}: .gitmodules declares {len(expected)} submodules and the evidence "
                f"carries {len(declared)}. Unrowed: {sorted(missing)}. The superproject's own "
                "grant says nothing about them.")
    return findings


def shelf_claims(root):
    """A shelf may not cite a submodule-bearing superproject without naming the boundary.

    The rule is deliberately narrow: it fires only on slugs this base has ALREADY measured
    as submodule-bearing (the register beside this file), so it cannot invent findings about
    ordinary repositories.

    🔴 SCOPE, and p291 got this wrong on its own first run.  The check was written
    LINE-scoped and returned 7 findings, 6 of which were wrapped prose whose very next line
    said `160000 commit` -- `compose/patterns.md` names the gitlinks TWO lines below the
    citation it was flagged for.  A line is not the unit a reader reads.  The unit is the
    BLOCK (blank-line delimited), which is also the unit a table row occupies, and rescoping
    to it drops all 6 and keeps the one real finding: a vendor-estate listing that counts the
    superproject among `9/9 MIT` repositories with no boundary named anywhere near it.
    """
    findings = []
    register = os.path.join(root, "compose", "code", "p291-submodule-pin-grant",
                            "submodule-bearing.txt")
    if not os.path.exists(register):
        return findings
    bearing = [l.strip() for l in open(register, encoding="utf-8")
               if l.strip() and not l.startswith("#")]
    for shelf in SHELVES:
        path = os.path.join(root, shelf)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8").read()
        offset = 0
        if shelf in APPEND_ONLY:
            text, offset = latest_pass_section(text)
        findings += shelf_claims_text(text, bearing, shelf, offset)
    return findings


# 🔴 SCOPE on the append-only shelves, and this follows `p279-absence-claims` verbatim
# rather than inventing a second convention.  `agents/trending.md` and `repos/trending.md`
# keep their history below the live section BY DESIGN — that is the whole point of an
# append-only shelf.  Those files carry citations written by passes 243 onward, every one
# adjudicated by the pass that wrote it, and a gate that failed on them would be red on
# arrival and disabled within a pass.  What is enforceable is that THE PASS BEING WRITTEN
# NOW cannot cite a superproject without the boundary.  So on these two files the scope is
# the newest `## Pass` section; on the rewritten shelves it is the whole file.
APPEND_ONLY = ("agents/trending.md", "repos/trending.md")


def latest_pass_section(text):
    """The newest `## Pass` block, and the line number it starts at."""
    lines = text.splitlines()
    starts = [i for i, l in enumerate(lines) if l.startswith("## Pass ")]
    if not starts:
        return text, 0
    end = starts[1] if len(starts) > 1 else len(lines)
    return "\n".join(lines[starts[0]:end]), starts[0]


# 🔵 A note on the wording of the finding message above: it says "root grant", not the
# capitalised filename.  `p283`'s ladder ratchet graded this instrument `SINGLE-SPELLING`
# on that one word and was right to flag it -- a lone capitalised licence filename in a
# source file is what a one-rung path ladder looks like from outside.  🟢 This module has
# NO path ladder: it never probes for a grant, it reads `payload_path` out of the evidence
# TSV, which the online probe wrote from a tree it enumerated.  This is `p289`'s situation
# exactly (its prose regex looked like a ladder until it was written as `licen[cs]e`), and
# the remedy is the same: say it in words that are not a filename.


# What counts as naming the boundary, anywhere in the same block.
# 🔵 The synonyms are the ones this base actually writes.  `p291`'s first draft listed only
# its own vocabulary and flagged `agents/trending.md:3101` — a cell that says the thing in
# plain words: *"It is a pointer; the seven sector configurations are separate repositories."*
# That names the boundary better than the word "gitlink" does.  A gate that only recognises
# its own jargon measures the jargon, not the claim.
BOUNDARY = re.compile(
    r"submodule|gitlink|160000|AT-PIN|per segment|superproject"
    r"|pointer|separate repositor|shell", re.I)


def blocks(text):
    """Yield (first_line_number, block_text) for blank-line-delimited blocks."""
    out, buf, start = [], [], 1
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip() == "":
            if buf:
                out.append((start, "\n".join(buf)))
                buf = []
            start = n + 1
        else:
            if not buf:
                start = n
            buf.append(line)
    if buf:
        out.append((start, "\n".join(buf)))
    return out


def shelf_claims_text(text, bearing, shelf="<shelf>", offset=0):
    findings = []
    for start, block in blocks(text):
        start += offset
        if BOUNDARY.search(block):
            continue
        for slug in bearing:
            if slug in block:
                findings.append(
                    f"{shelf}:{start}: cites submodule-bearing {slug} in a block that never "
                    "names the submodule boundary. Its tree is gitlinks; its root grant "
                    "covers a shell. Quote the submodule, never the superproject.")
    return findings


def main(argv):
    root = "."
    evidence = None
    args = list(argv[1:])
    while args:
        a = args.pop(0)
        if a == "--root":
            root = args.pop(0)
        else:
            evidence = a
    if evidence is None:
        cand = [f for f in os.listdir(os.path.join(root, "evidence"))
                if f.startswith("submodule-pin-grant.")] if \
            os.path.isdir(os.path.join(root, "evidence")) else []
        if not cand:
            print("# p291: no submodule-pin-grant evidence file; nothing to check.")
            return 0
        evidence = os.path.join(root, "evidence", sorted(cand)[-1])

    rows = parse_tsv(open(evidence, encoding="utf-8").read())
    findings = []
    counts = {}
    for r in rows:
        verdict, f = classify(r)
        counts[verdict] = counts.get(verdict, 0) + 1
        findings += f
    findings += census(rows)
    findings += shelf_claims(root)

    tally = "  ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    print(f"# p291 submodule-pin-grant — {len(rows)} segment rows  {tally}")
    for f in findings:
        print(f"🔴 {f}")
    if findings:
        print(f"🔴 FAIL — {len(findings)} finding(s).")
        return 1
    print("🟢 PASS — every segment row is graded at its pin, and every declared "
          "submodule carries a row.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
