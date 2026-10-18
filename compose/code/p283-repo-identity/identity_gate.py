#!/usr/bin/env python3
"""p283 (`p282`'s declared item 1) — THE IDENTITY CENSUS STOPS BEING A ONE-OFF.

🔴 Why it exists.  `p282` found that `agents/top.md` carried `ls1intum/Iris` and
`ls1intum/Pyris` as **two rows of the build-on tier** when they are **one repository**:
identical HEAD `d7b2c095204e`, 245 refs, root tree `4e2f096df767`, 203 files, the same
1 088-byte MIT payload.  Six recipes in `compose/patterns.md` told a delivery team to
compose the two.

🔴 Why twenty passes of licence rigour could not see it, in `p282`'s own words: *"Every
instrument was right about the row it measured.  **Duplication is a relation BETWEEN rows,
and this base owns no per-pair check.**"*  `recount` matched 27 rows to 27 because 27 rows
is what the file has.

🔴 And `p282` then proved the remedy **by hand** and left it out of the Makefile — which is
this base's own named recurring failure mode, the one the Makefile header opens with: *"a
working gate that stayed a one-off"*.  `p283` registered it first for exactly that reason.
This file is the gate.

🟢 TWO HALVES, split on egress, following this Makefile's standing convention that the
online half stays out of `make hooks` so the suite runs where there is no network.

  OFFLINE (`make gate-identity`, in `hooks`):
    no shelf may recommend both members of a RECORDED alias pair as two live rows,
    and no shelf may carry the same address as two live rows of one table.

  ONLINE (`make gate-identity-online`, out of `hooks`):
    `git ls-remote <addr> HEAD` for every build-on address; two addresses that answer
    with the same HEAD are the same repository.  New pairs are reported, not assumed --
    a collision is a FINDING for a human to shelve into `aliases.tsv`, because two
    genuinely distinct forks can share a HEAD the day one is forked from the other.

🔵 THE PREDICATE THAT MAKES THIS SOUND, and it is the one subtlety in the file.
`p282` withdrew the `Iris` row **IN PLACE** rather than deleting it -- the row is still
published, struck through, carrying the evidence of its own withdrawal.  A naive
"both addresses appear in this file" check therefore fires on the CORRECTION ITSELF and
is unfixable without deleting the forensic record.  So the unit is not the address, it is
the **LIVE ROW**:

    a markdown table data row is LIVE unless its first cell is struck through (`~~`)
    or the row says `WITHDRAWN`.

🔵 Prose is not a row.  `verticals/solutions.md` names both halves of the pair inside an
indented ASCII diagram, annotated `ls1intum/Iris is an ALIAS of this repo -- p282`.  That
is the base explaining the alias, which is the opposite of the defect, and a row-scoped
predicate excludes it for free.

🔴 p300: AND THE SAME ERROR CLASS SURVIVED *INSIDE* THE ROW, where it went red for two
passes.  The note above records that FILE scope produced 15 false positives, every one of
them a CROSS-REFERENCE, and narrowed the unit to the table to fix it.  A row's DESCRIPTION
cell cites sibling repositories in exactly the same way -- this base's house style -- so
from `p298` this gate reported four ADDRESS-TWICE findings that were all that same shape
one level down:

    | 1EdTech/lti-1-3-php-library | Apache-2.0 | ... cf. tsugiproject/tsugi |
    | tsugiproject/tsugi          | Apache-2.0 | ... |

Two rows of one table, `tsugiproject/tsugi` harvested from both -- and RECOMMENDED by one.
🔴 Measured red at `p298` and `p299` and green at `p297`; and because `make hooks` was a
fail-fast chain, the SIX gates ordered after this one did not run at all for two passes.

🟢 THE SPLIT THAT FIXES IT, and it is deliberately NOT symmetric:

  ADDRESS-TWICE   -> the row's SUBJECT only.  "Recommended twice" means two rows whose
                     subject is the same repository.  A citation in a later cell is the
                     house style, not a second recommendation.
  ALIAS-PAIR-LIVE -> the WHOLE row, unchanged.  Control C6 pins a live finding `p283`
                     made: ONE row presenting `Iris` and `Pyris` as two distinct MIT
                     subsystems.  Naming both halves of a PROVEN alias pair anywhere in
                     one row is that defect whatever cell they sit in, so narrowing this
                     arm would delete the finding the gate was built on.

🔵 The subject is the FIRST ADDRESS-BEARING CELL, never cell 1.  Measured on this corpus
at `p300`: of 379 live address rows, 153 carry no address in cell 1 at all (the first cell
is a plain name), so a cell-1 rule would blind the gate on 40 % of the shelf.  29 rows
spread addresses across more than one cell -- that is the entire cross-reference
population, and it is what the subject scope excludes.

🔵 One thing it deliberately does NOT do: resolve aliases over the network in the offline
half.  `ls1intum/Iris` 302s to `Pyris` at the HTTP layer, but that needs egress, and
`p281` recorded that an instrument which cannot run where the pass runs is an instrument
that does not run.  The ledger is the offline memory of what the online half found.
"""
import argparse
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SHELVES = ("agents/top.md", "repos/foundations.md", "verticals/solutions.md")
# 🔵 No lazy quantifier: `ACTION TB`'s lint rejects one, and it is right to --
# the terminator set is easier to get wrong than a greedy class plus a strip.
ADDR = re.compile(r"github\.com/([A-Za-z0-9_-][A-Za-z0-9._-]*)/([A-Za-z0-9_-][A-Za-z0-9._-]*)")
ROW = re.compile(r"^\|")
SEP = re.compile(r"^\|[\s:|-]*-[\s:|-]*\|?\s*$")


def load_aliases(path):
    """owner/repo <TAB> owner/repo <TAB> pass <TAB> head -- the shelved alias ledger."""
    pairs = []
    for raw in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        f = raw.split("\t")
        if len(f) >= 2:
            pairs.append((f[0].strip().lower(), f[1].strip().lower(), f[2].strip() if len(f) > 2 else "?"))
    return pairs


def live_rows(text, subject_only=False):
    """Yield (table_id, lineno, addresses) for every LIVE markdown table data row.

    `subject_only` yields ONLY the addresses of the first address-bearing cell -- the
    repository the row RECOMMENDS -- rather than every address on the line.  The two
    arms of this gate want different answers; the module docstring says why.

    A row is dead -- and so invisible to this gate -- if it is struck through in its
    first cell or marked WITHDRAWN.  See the module docstring: p282's correction is
    itself published as a row, and a gate that fires on a correction cannot be green.

    🔴 THE UNIT IS THE TABLE, NOT THE FILE, and the first draft of this gate got it
    wrong.  File scope produced 15 findings on a green shelf, every one of them a row
    in the `## Agents by function` INDEX pointing at a repository the build-on tier
    also lists.  That is a cross-reference -- this base's house style, and the whole
    point of an index.  Recommending one repository twice means twice in ONE table.
    A blank line, a heading or any non-row line ends a table.
    """
    out, table = [], 0
    prev_was_row = False
    for i, line in enumerate(text.splitlines(), 1):
        is_row = bool(ROW.match(line))
        if not is_row:
            if prev_was_row:
                table += 1
            prev_was_row = False
            continue
        prev_was_row = True
        if SEP.match(line):
            continue
        cells = line.split("|")
        first = cells[1] if len(cells) > 1 else ""
        if "~~" in first or "WITHDRAWN" in line.upper():
            continue
        def harvest(chunk):
            return {
                f"{m.group(1)}/{m.group(2)}".lower().rstrip(".").removesuffix(".git")
                for m in ADDR.finditer(chunk)
            }

        if subject_only:
            # 🔵 The FIRST cell carrying any address is the subject.  A cell may carry
            # two legitimately (C6's shape), so the whole cell is taken, never the
            # first match -- and the search starts at cells[1] because a markdown row
            # splits to an empty cells[0].
            addrs = set()
            for cell in cells[1:]:
                addrs = harvest(cell)
                if addrs:
                    break
        else:
            addrs = harvest(line)
        if addrs:
            out.append((table, i, addrs))
    return out


def check_offline(root, aliases):
    findings = []
    for shelf in SHELVES:
        p = root / shelf
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        rows = live_rows(text)
        # 🔵 p300: the two arms read DIFFERENT scopes of the same rows, and that
        # asymmetry is the fix -- see the module docstring.  The alias arm keeps the
        # whole row (C6); the duplicate-address arm takes the row's subject (C13).
        subj = {(t, n): s for t, n, s in live_rows(text, subject_only=True)}
        tables = sorted({t for t, _, _ in rows})
        for t in tables:
            trows = [(n, s) for tt, n, s in rows if tt == t]
            # (1) a recorded alias pair, both halves recommended by one table.
            #     WHOLE-ROW scope, deliberately: naming both halves of a proven alias
            #     anywhere in one row is p283's C6 finding.
            for a, b, prov in aliases:
                la = [n for n, s in trows if a in s]
                lb = [n for n, s in trows if b in s]
                if la and lb:
                    where = f"{la[0]}" if la == lb else f"{la[0]},{lb[0]}"
                    same = " (both in ONE row)" if la == lb else ""
                    findings.append(
                        f"ALIAS-PAIR-LIVE\t{shelf}:{where}\t{a} == {b}\t"
                        f"one repository recommended twice{same} (ledger: {prov})"
                    )
            # (2) the same address RECOMMENDED by two live rows of one table.
            #     SUBJECT scope: a sibling cited in a description cell is a
            #     cross-reference, which is this base's house style and not a
            #     second recommendation.  Whole-row scope here was red for two passes.
            seen = {}
            for n, _ in trows:
                for a in subj.get((t, n), ()):
                    seen.setdefault(a, []).append(n)
            for a, lines in sorted(seen.items()):
                if len(lines) > 1:
                    findings.append(
                        f"ADDRESS-TWICE\t{shelf}:{','.join(map(str, lines))}\t{a}\t"
                        f"the same address is published as {len(lines)} live rows of one table"
                    )
    return findings


def ls_remote_head(addr, timeout=40):
    try:
        r = subprocess.run(
            ["git", "ls-remote", f"https://github.com/{addr}", "HEAD"],
            capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    if r.returncode != 0 or not r.stdout.strip():
        return None, "UNREACHABLE"
    return r.stdout.split()[0], "OK"


def check_online(root, aliases, out_tsv):
    """ls-remote every build-on address; equal HEAD == one repository."""
    known = {frozenset((a, b)) for a, b, _ in aliases}
    addrs = set()
    for shelf in SHELVES:
        p = root / shelf
        if p.exists():
            for _, _, s in live_rows(p.read_text(encoding="utf-8")):
                addrs |= s
    heads, rows = {}, []
    for a in sorted(addrs):
        sha, state = ls_remote_head(a)
        rows.append(f"{a}\t{sha or '-'}\t{state}")
        if sha:
            heads.setdefault(sha, []).append(a)
    findings = []
    for sha, group in sorted(heads.items()):
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    pair = frozenset((group[i], group[j]))
                    tag = "KNOWN-ALIAS" if pair in known else "HEAD-COLLISION-NEW"
                    findings.append(f"{tag}\t{group[i]}\t{group[j]}\t{sha[:12]}")
    if out_tsv:
        pathlib.Path(out_tsv).write_text(
            "address\thead\tstate\n" + "\n".join(rows) + "\n", encoding="utf-8"
        )
    return findings, len(addrs), len(heads)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--aliases", default=str(HERE / "aliases.tsv"))
    ap.add_argument("--online", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    root = pathlib.Path(a.root).resolve()
    aliases = load_aliases(a.aliases)

    if a.online:
        findings, n_addr, n_heads = check_online(root, aliases, a.out)
        new = [f for f in findings if f.startswith("HEAD-COLLISION-NEW")]
        for f in findings:
            print(f)
        print(f"# addresses={n_addr} distinct-HEADs={n_heads} "
              f"known-alias-pairs={len(findings) - len(new)} NEW={len(new)}")
        if new:
            print("# 🔴 FAIL — a HEAD collision this base has not shelved. "
                  "Adjudicate it, then record it in aliases.tsv.")
            return 1
        print("# 🟢 PASS — every live build-on address is a distinct repository, "
              "or a collision this base has already adjudicated.")
        return 0

    findings = check_offline(root, aliases)
    for f in findings:
        print(f)
    print(f"# shelves={len(SHELVES)} ledger-pairs={len(aliases)} findings={len(findings)}")
    if findings:
        print("# 🔴 FAIL — a shelf recommends one repository twice.")
        return 1
    print("# 🟢 PASS — no shelf recommends one repository under two live rows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
