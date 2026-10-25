#!/usr/bin/env python3
"""Offline controls for `p442`'s cell-reproduction gate.  No network: every case is a
synthetic shelf plus a synthetic record written to a temp tree.

🔵 The controls that carry this suite are the NEGATIVE ones — a gate that cannot go red is
not a gate.  Each mutation below was run against the gate and is asserted to produce a RED,
with the reason named, because `p441` found a control in its own suite that stayed green
after the entire code path under it was deleted.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(HERE, "cell_reproduction_gate.py")
RECORD_REL = os.path.join("evidence", "published-cell-reproduction.2026-10-25-p442.tsv")
HEAD = "slug\tref\tpub_path\tpath\tpub_bytes\tpub_sha12\tfile_bytes\tfile_sha12\tcapture_sha12\tverdict"

ROW = ("| [{slug}](https://github.com/{slug}) | MIT | `aaaaaaaaaaaa` | `{path}` {b} B "
       "· `{sha}` | what it does | Global |")
TABLE_HEAD = ("| Agent / repo | Licence | HEAD | Licence payload | What it does | Region |\n"
              "|---|---|---|---|---|---|\n")

passed = failed = 0


def check(label, want, got):
    global passed, failed
    if want == got:
        passed += 1
        print("  OK   %s" % label)
    else:
        failed += 1
        print("  FAIL %s\n       want %r\n       got  %r" % (label, want, got))


def build(tmp, shelf_rows, record_rows, shelves=("agents/top.md", "repos/foundations.md",
                                                 "verticals/solutions.md")):
    for rel in shelves:
        d = os.path.join(tmp, os.path.dirname(rel))
        os.makedirs(d, exist_ok=True)
        body = TABLE_HEAD + "\n".join(shelf_rows.get(rel, [])) + "\n"
        open(os.path.join(tmp, rel), "w", encoding="utf-8").write(body)
    os.makedirs(os.path.join(tmp, "evidence"), exist_ok=True)
    open(os.path.join(tmp, RECORD_REL), "w", encoding="utf-8").write(
        "\n".join([HEAD] + record_rows) + "\n")


def run(tmp):
    r = subprocess.run([sys.executable, "-I", GATE, "--root", tmp],
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def rec(slug, path, b, sha, verdict, fb=None, fsha=None):
    fb = fb if fb is not None else b
    fsha = fsha if fsha is not None else sha
    return "\t".join([slug, "main", path, path, str(b), sha, str(fb), fsha, "cccccccccccc",
                      verdict])


def main():
    sha_a = "a" * 12
    sha_b = "b" * 12

    # C1 — the happy path: one cell, recorded as REPRODUCES.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a)]},
              [rec("o/r", "LICENSE", "1063", sha_a, "REPRODUCES")])
        rc, out = run(tmp)
        check("C1 a recorded, reproducing cell is green", 0, rc)
        check("C1 the count is reported", True, "1 published cells, 1 green" in out)

    # C2 — NEGATIVE: the cell is recorded as capture-measured.  This is the live defect
    # `p442` found 19 times; the gate must name it, not merely fail.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a)]},
              [rec("o/r", "LICENSE", "1063", sha_a, "CAPTURE-MEASURED", 1064, sha_b)])
        rc, out = run(tmp)
        check("C2 a capture-measured cell is RED", 1, rc)
        check("C2 the verdict is named in the output", True, "CAPTURE-MEASURED" in out)

    # C3 — NEGATIVE: a published cell that is in no record at all.  This is the ratchet: a
    # pass may add a row, but not an UNMEASURED one.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a),
                                      ROW.format(slug="o/new", path="LICENSE", b="1 069",
                                                 sha=sha_b)]},
              [rec("o/r", "LICENSE", "1063", sha_a, "REPRODUCES")])
        rc, out = run(tmp)
        check("C3 an unrecorded cell is RED", 1, rc)
        check("C3 it is typed CELL-UNMEASURED", True, "CELL-UNMEASURED" in out)
        check("C3 the offending slug is named", True, "o/new" in out)

    # C4 — NEGATIVE: the record is for the same slug and path but a DIFFERENT digest, i.e.
    # the shelf cell was edited after the sweep.  A stale record must not confer green.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a)]},
              [rec("o/r", "LICENSE", "1063", sha_b, "REPRODUCES")])
        rc, out = run(tmp)
        check("C4 a record with another digest does NOT cover the cell", 1, rc)
        check("C4 ... and is typed CELL-UNMEASURED", True, "CELL-UNMEASURED" in out)

    # C5 — NEGATIVE: no cross-slug credit.  The identical payload digest recorded under a
    # DIFFERENT repository must not satisfy this row — two repositories can ship the same
    # stock MIT text, which this base measures constantly.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a)]},
              [rec("other/repo", "LICENSE", "1063", sha_a, "REPRODUCES")])
        rc, _ = run(tmp)
        check("C5 the same digest under another slug is not credit", 1, rc)

    # C6 — the branch-qualified spelling (`master/LICENSE`) is keyed as the shelf writes it.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="master/LICENSE",
                                                 b="1 560", sha=sha_a)]},
              [rec("o/r", "master/LICENSE", "1560", sha_a, "REPRODUCES")])
        rc, _ = run(tmp)
        check("C6 a branch-qualified path is covered by its published spelling", 0, rc)

    # C7 — one payload published on all three sell shelves needs coverage once, and is
    # counted three times.  (`robotros/California-IEP-AI-project-kit` is this shape live.)
    with tempfile.TemporaryDirectory() as tmp:
        row = ROW.format(slug="o/r", path="LICENSE", b="1 065", sha=sha_a)
        build(tmp, {"agents/top.md": [row], "repos/foundations.md": [row],
                    "verticals/solutions.md": [row]},
              [rec("o/r", "LICENSE", "1065", sha_a, "REPRODUCES")])
        rc, out = run(tmp)
        check("C7 the same cell on three shelves is green", 0, rc)
        check("C7 ... and is counted three times", True, "3 published cells" in out)

    # C8 — NEGATIVE: an unknown verdict string must not pass.  Only REPRODUCES is green, so
    # a future verdict added to the sweep cannot silently inherit a pass.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a)]},
              [rec("o/r", "LICENSE", "1063", sha_a, "PROBABLY-FINE")])
        rc, out = run(tmp)
        check("C8 an unknown verdict is RED", 1, rc)
        check("C8 ... and is echoed verbatim", True, "PROBABLY-FINE" in out)

    # C9 — P355: measuring nothing is not a clean tree.  A missing record, an empty record
    # and a shelf set with no cells are each exit 2, never a pass.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a)]}, [])
        rc, out = run(tmp)
        check("C9 an empty record exits 2", 2, rc)
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {}, [rec("o/r", "LICENSE", "1063", sha_a, "REPRODUCES")])
        rc, out = run(tmp)
        check("C9 zero parsed cells exits 2, not 0", 2, rc)
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a)]},
              [rec("o/r", "LICENSE", "1063", sha_a, "REPRODUCES")])
        os.remove(os.path.join(tmp, RECORD_REL))
        rc, _ = run(tmp)
        check("C9 a missing record exits 2", 2, rc)

    # C10 — the record must declare its columns.  A header-less or renamed record is a
    # configuration fault, not a clean run (the `gate-tables` lesson: a header read as data).
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": [ROW.format(slug="o/r", path="LICENSE", b="1 063",
                                                 sha=sha_a)]},
              [rec("o/r", "LICENSE", "1063", sha_a, "REPRODUCES")])
        p = os.path.join(tmp, RECORD_REL)
        body = open(p, encoding="utf-8").read().split("\n")
        body[0] = body[0].replace("pub_sha12", "sha_prefix")
        open(p, "w", encoding="utf-8").write("\n".join(body))
        rc, out = run(tmp)
        check("C10 a renamed record column exits 2", 2, rc)
        check("C10 ... and the missing column is named", True, "pub_sha12" in out)

    # C11 — a table HEADER row must never be read as a cell.  The shelves' own header has no
    # payload cell, so this is a parser control: three shelves of pure header parse as zero
    # cells, which C9's second case then types as a parse fault.
    with tempfile.TemporaryDirectory() as tmp:
        build(tmp, {"agents/top.md": ["| Nombre | Repo | Licencia |", "|---|---|---|"]},
              [rec("o/r", "LICENSE", "1063", sha_a, "REPRODUCES")])
        rc, out = run(tmp)
        check("C11 a header-only shelf parses as zero cells", 2, rc)

    # ── C12–C14: three defects this gate found in its OWN parser, during the pass that
    # wrote it, on the pass's own prose.  Each is a control now, because a parser that
    # cannot see a cell lets the cell go unverified — which is the same failure as having
    # no gate, wearing a green badge.
    sys.path.insert(0, HERE)
    import extract_published_cells as parser

    # C12 — a BOLDED byte count is still a cell.  v1 required whitespace between the path
    # and the digits, so `**35 149 B**` was invisible and 9 live cells went unverified.
    got = parser.PAYLOAD.findall("| x | `legacy_reference/LICENSE` **35 149 B** · `3972dc9744f6` |")
    check("C12 an emphasised cell is parsed", [("legacy_reference/LICENSE", "35 149", "3972dc9744f6")], got)
    got = parser.PAYLOAD.findall("| x | *`LICENSE`* *1 064 B* · `092d389ac156` |")
    check("C12 italics too", 1, len(got))

    # C13 — TWO payload cells in one row are two published cells, not one.  `p442`'s own
    # Chamilo row publishes a 35 147 B grant and the 1 614 B pointer beside it.
    with tempfile.TemporaryDirectory() as tmp:
        row = ("| [`o/r`](https://github.com/o/r) | GPL-3.0 · `LICENSE` 35 147 B · `aaaaaaaaaaaa` "
               "| 🔴 `license.txt` **1 614 B · `bbbbbbbbbbbb`** | note |")
        build(tmp, {"agents/top.md": [row]},
              [rec("o/r", "LICENSE", "35147", "a" * 12, "REPRODUCES"),
               rec("o/r", "license.txt", "1614", "b" * 12, "REPRODUCES")])
        rc, out = run(tmp)
        check("C13 both cells in one row are covered", 0, rc)
        check("C13 ... and both are counted", True, "2 published cells" in out)
    with tempfile.TemporaryDirectory() as tmp:
        row = ("| [`o/r`](https://github.com/o/r) | GPL-3.0 · `LICENSE` 35 147 B · `aaaaaaaaaaaa` "
               "| 🔴 `license.txt` **1 614 B · `bbbbbbbbbbbb`** | note |")
        build(tmp, {"agents/top.md": [row]},
              [rec("o/r", "LICENSE", "35147", "a" * 12, "REPRODUCES")])
        rc, out = run(tmp)
        check("C13 the SECOND cell cannot ride on the first", 1, rc)
        check("C13 ... and it is the one named", True, "license.txt" in out)

    # C14 — a digest with NO path in its cell (the path is in the column header) must not be
    # mistaken for a commit.  This one cost four live cells a NO-PAYLOAD verdict: the sweep
    # fetched at a tree-ish that was a licence digest.
    line = ("| [`o/r`](https://github.com/o/r) | MIT · 1 071 B · `cccccccccccc` | 🔴 "
            "`legacy_reference/LICENSE` **35 149 B** · `dddddddddddd` | note |")
    heads = [h for h in parser.HEX12.findall(line)
             if h not in set(parser.DIGEST_AFTER_BYTES.findall(line))]
    check("C14 no 12-hex token in a pure-digest row is a HEAD", [], heads)
    line2 = line.replace("| note |", "| `eeeeeeeeeeee` | note |")
    heads2 = [h for h in parser.HEX12.findall(line2)
              if h not in set(parser.DIGEST_AFTER_BYTES.findall(line2))]
    check("C14 ... and a real commit still is", ["e" * 12], heads2)

    print("\ntest_cell_reproduction.py: %d/%d controls passed" % (passed, passed + failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
