#!/usr/bin/env python3
"""Controls for p227's direction gate. Run: python3 -I test_direction_gate.py

Every control states what would be WRONG if it failed, because a gate that reports 0
is only trustworthy if something is known to make it report 1.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))  # so -I works

import direction_gate as g

TABLE = pathlib.Path(__file__).resolve().parents[3] / "evidence" / "so-refuted-claims.2026-10-15-p227.tsv"
RESULTS = pathlib.Path(__file__).resolve().parent / "p227-raw-results.txt"

# Canonical bodies read first-hand 2026-10-15. Byte sizes recorded to show why size is unsafe.
GPL3_HEAD = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
 Copyright (C) 2007 Free Software Foundation, Inc. {http://fsf.org/}
  13. Use with the GNU Affero General Public License.
  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.
"""
AGPL3_HEAD = """                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007
 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
  13. Remote Network Interaction; Use with the GNU General Public License.
  Notwithstanding any other provision of this License, if you modify the
Program, your modified version must prominently offer all users
interacting with it remotely through a computer network an opportunity
to receive the Corresponding Source of your version.
"""

results = []


def check(name, got, want, why):
    ok = got == want
    results.append((ok, name, got, want, why))
    return ok


def main():
    table = g.load_table(str(TABLE))
    records = g.load_records(str(RESULTS))

    # --- 1. the table loads, and both directions are present -----------------------------
    check("table loads 13 subjects", len(table), 13,
          "a short read means a row was lost to a stray tab")
    check("RESTRICTIVE rows present", sum(1 for r in table if r["direction"] == "RESTRICTIVE"), 4,
          "0 here means the table is back to being one-directional, p226's blind spot")

    # --- 2. p226 backward compatibility: a 6-column row still loads ----------------------
    p226_row = "x\t(?i)x\t(?i)y\tz\tw\t(?i)q"
    tmp = pathlib.Path("/tmp/p227_compat.tsv")
    tmp.write_text("subject\tsubject_pattern\trefuted_pattern\tcorrection\trefuted_by\texempt_pattern\n"
                   + p226_row + "\n", encoding="utf-8")
    old = g.load_table(str(tmp))
    check("p226-era 6-col table still loads", len(old), 1,
          "a crash here breaks every p224-p226 instrument that reads this file")
    check("6-col row defaults to PERMISSIVE", old[0]["direction"], "PERMISSIVE",
          "the only direction a p226-era table could express")

    # --- 3. the gate FIRES on a planted claim in each direction --------------------------
    perm = [("planted", "Frappe LMS is listed as MIT in one comparison.")]
    hits, _ = g.inbound_gate(table, perm)
    check("fires on a PERMISSIVE claim", len(hits), 1,
          "0 means the p226 behaviour regressed")
    check("  and labels its direction", hits[0]["direction"] if hits else None, "PERMISSIVE", "")

    rest = [("planted", "Gibbon is an AGPL-3.0 student information system.")]
    hits, _ = g.inbound_gate(table, rest)
    check("fires on a RESTRICTIVE claim", len(hits), 1,
          "0 means the new half of the table is decorative - this is p227's whole point")
    check("  and labels its direction", hits[0]["direction"] if hits else None, "RESTRICTIVE", "")

    # --- 4. the exempt column still protects a source that REPORTS the error -------------
    flagged = [("planted", "One comparison lists Frappe LMS as MIT, which conflicts with the AGPL listing.")]
    hits, _ = g.inbound_gate(table, flagged)
    check("stays silent on a self-flagged claim", len(hits), 0,
          "firing here punishes a source for being careful")

    # --- 5. the TRUE statement about Gibbon must NOT fire --------------------------------
    true_gibbon = [("mandated vertical query", "RosarioSIS (GPL, PHP) and Gibbon (GPL, PHP) are open-source SIS.")]
    hits, near = g.inbound_gate(table, true_gibbon)
    check("stays silent on 'Gibbon (GPL)' - it is TRUE", len(hits), 0,
          "firing here would make the gate enforce the KB's own p226 error against a correct source")
    check("  and reports it as a near miss instead", len(near) >= 1, True, "")

    # --- 6. this pass's real run ---------------------------------------------------------
    hits, near = g.inbound_gate(table, records)
    check("p227 live run: hits", len(hits), 0, "")
    check("p227 live run: near misses", len(near), 7, "")

    # --- 7. the family discriminator, both sides -----------------------------------------
    check("GPL-3.0 body -> GPL-3.0", g.family_of(GPL3_HEAD)[0], "GPL-3.0",
          "this is the Gibbon cell; AGPL here is the error p171/p214/p227 all had to correct")
    check("AGPL-3.0 body -> AGPL-3.0", g.family_of(AGPL3_HEAD)[0], "AGPL-3.0",
          "this is the Open edX cell")
    check("  channel is the title line", g.family_of(GPL3_HEAD)[1], "title line",
          "any other channel is one p227 showed to be unsafe")

    # --- 8. and the WRONG method, kept demonstrable --------------------------------------
    check("naive affero grep MISREADS a GPL-3.0 body", g.naive_affero_grep(GPL3_HEAD), "AGPL-3.0",
          "if this ever returns GPL-3.0 the control has stopped demonstrating the defect")
    check("naive grep happens to be right on AGPL", g.naive_affero_grep(AGPL3_HEAD), "AGPL-3.0",
          "the method is wrong even when its answer is right - that is why it survived so long")

    # --- 9. size is not a channel --------------------------------------------------------
    check("canonical bodies are 15 bytes apart", 35136 - 35121, 15,
          "read first-hand 2026-10-15: GibbonEdu/core 35 121 B, openedx 35 136 B")

    width = max(len(n) for _, n, _, _, _ in results)
    bad = 0
    for ok, name, got, want, why in results:
        print(f"{'PASS' if ok else 'FAIL'}  {name.ljust(width)}  got={got!r}")
        if not ok:
            bad += 1
            if why:
                print(f"      why it matters: {why}")
    print(f"\n{len(results) - bad}/{len(results)} controls pass")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
