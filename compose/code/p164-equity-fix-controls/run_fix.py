"""ACTION IL — emit the margin table and the falsifier judgement."""
import sys
sys.path.insert(0, ".")
import fixed_gate as F, script_equity as base, corpus

FLOOR = base.MIN_LETTER_RATIO

def main():
    mismatches = sum(1 for r in corpus.CORPUS
                     if F.gibberish_check_patched(r[3]) != base.gibberish_check(r[3]))
    assert mismatches == 0, f"fidelity gate FAILED: {mismatches} mismatches"

    rows = []
    for tag, script, label, text in [(r[0], r[1], r[2], r[3]) for r in corpus.CORPUS]:
        out = {}
        for k, kw in F.VARIANTS.items():
            rej, why, ratio, ent = F.gibberish_check_patched(text, **kw)
            out[k] = (rej, why, ratio)
        up_r = out["upstream"][2]
        fx_r = out["step2+3"][2]
        rows.append((tag, script, label, up_r, fx_r,
                     (up_r - FLOOR) if up_r is not None else None,
                     (fx_r - FLOOR) if fx_r is not None else None,
                     out["upstream"][0], out["step2+3"][0],
                     out["upstream"][1], out["step2+3"][1]))

    with open("result.2026-10-13-p164.tsv", "w", encoding="utf-8") as fh:
        fh.write("tag\tscript\tlabel\tratio_upstream\tratio_fixed\tmargin_upstream\t"
                 "margin_fixed\trejected_upstream\trejected_fixed\treason_upstream\treason_fixed\n")
        for r in rows:
            fh.write("\t".join("" if v is None else
                               (f"{v:.3f}" if isinstance(v, float) else str(v))
                               for v in r) + "\n")

    print(f"fidelity gate: {mismatches} mismatches vs p163 replication -- PASS")
    print(f"\nletter-ratio floor = {FLOOR}\n")
    print(f"{'tag':<14}{'ratio up':>10}{'ratio fix':>11}{'margin up':>11}{'margin fix':>12}  verdict")
    print("-" * 78)
    for tag, script, label, ur, fr, um, fm, urej, frej, _, frs in rows:
        if ur is None:
            continue
        v = "REJECT:" + str(frs) if frej else "accept"
        print(f"{tag:<14}{ur:>10.3f}{fr:>11.3f}{um:>11.3f}{fm:>12.3f}  {v}")

    valid = [r for r in rows if not r[0].startswith("CTRL") and r[3] is not None]
    print(f"\nvalid rows: margin spread upstream = "
          f"{min(r[5] for r in valid):.3f}..{max(r[5] for r in valid):.3f} "
          f"({max(r[5] for r in valid)/min(r[5] for r in valid):.1f}x)")
    print(f"valid rows: margin spread fixed    = "
          f"{min(r[6] for r in valid):.3f}..{max(r[6] for r in valid):.3f} "
          f"({max(r[6] for r in valid)/min(r[6] for r in valid):.1f}x)")

    print("\n=== FALSIFIER (ACTION IL) ===")
    print("Refuted if treating combining marks as letters lets ANY of the two")
    print("negative controls through.")
    fired = False
    for cid in ("CTRL-mash", "CTRL-symbols"):
        rej3, why3, r3, _ = F.gibberish_check_patched(
            [c for c in corpus.CORPUS if c[0] == cid][0][3], **F.VARIANTS["step3"])
        rejb, whyb, rb, _ = F.gibberish_check_patched(
            [c for c in corpus.CORPUS if c[0] == cid][0][3], **F.VARIANTS["step2+3"])
        through = (not rej3) or (not rejb)
        fired = fired or through
        print(f"  {cid:<13} step3={'REJECT:'+str(why3) if rej3 else 'ACCEPTED'}"
              f"  step2+3={'REJECT:'+str(whyb) if rejb else 'ACCEPTED'}"
              f"  (ratio {rb:.3f})")
    print(f"\nVERDICT: falsifier {'FIRED -- ACTION IL REFUTED' if fired else 'SILENT -- ACTION IL DISCHARGED'}")

if __name__ == "__main__":
    main()
