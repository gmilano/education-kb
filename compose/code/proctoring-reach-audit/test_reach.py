#!/usr/bin/env python3
"""The five controls of passes 44/45, applied to the THIRD code artefact of this
KB -- pass 46, action 2, gap 96.

The first two artefacts (unitime-mcp-gate, sebserver-mcp-gate) are route tables,
and the controls were written for route tables. This artefact is a
CLASSIFICATION: "which SPI methods talk to the remote". Controls (a) and (b) are
about route syntax and have no subject here; they are reported N/A rather than
quietly dropped, because a skipped control reads exactly like a passed one.

Control (e) is the one that earns the pass. For a route table it reads "no read
verb that writes". Generalised: "nothing classified as local may reach the
network". That is what caught the defect.

Run:  python3 test_reach.py [path-to-seb-server-checkout]
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPI_COUNT = 14

checks = []


def check(ok, label, detail=""):
    checks.append((bool(ok), label, detail))
    print("  %-4s %s%s" % ("ok" if ok else "FAIL", label, ("  -- " + detail) if detail else ""))


def load(path):
    rows, comments = [], []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("#"):
            comments.append(line)
            continue
        if not line or line.startswith("provider\t"):
            continue
        f = line.split("\t")
        rows.append({
            "provider": f[0], "kind": f[1], "method": f[2], "line": int(f[3]),
            "is_spi": f[4] == "yes", "direct": int(f[5]),
            "depth": None if f[6] == "-" else int(f[6]), "reaches": f[7] == "yes",
        })
    return rows, comments


def main():
    tsv = os.path.join(HERE, "reach.tsv")
    if not os.path.exists(tsv):
        sys.exit("reach.tsv missing: run extract_reach.py first")
    rows, comments = load(tsv)

    # If a checkout is given, the table must REGENERATE identically. A committed
    # table nobody can reproduce is a transcription, which is what this KB keeps
    # catching itself doing.
    if len(sys.argv) > 1:
        gen = subprocess.run(
            [sys.executable, os.path.join(HERE, "extract_reach.py"), sys.argv[1]],
            capture_output=True, text=True, check=True).stdout
        check(gen.strip() == open(tsv, encoding="utf-8").read().strip(),
              "reach.tsv regenerates byte-identically from the checkout")

    print("\n-- coverage --")
    for provider in ("JITSI_MEET", "ZOOM"):
        spi = [r for r in rows if r["provider"] == provider and r["is_spi"]]
        check(len(spi) == SPI_COUNT, "%s: all %d SPI methods present" % (provider, SPI_COUNT),
              "found %d" % len(spi))
        check(all(r["kind"] == "method" for r in spi),
              "%s: no SPI row is a constructor" % provider)

    print("\n-- control (a): no route carries an unresolved ${...} --")
    check(not any("${" in r["method"] for r in rows),
          "N/A for this artefact (no route column) and vacuously true",
          "this piece classifies methods, it does not publish routes")

    print("\n-- control (b): every route absolute and context-qualified --")
    check(True, "N/A for this artefact: it publishes no routes",
          "declared N/A, not skipped -- the SPI is a Java interface, not a URL space")

    print("\n-- control (c): no row is a class declaration --")
    ctors = [r for r in rows if r["kind"] == "ctor"]
    check(len(ctors) == 8, "the 8 constructors are LABELLED ctor, not counted as methods",
          "%d labelled" % len(ctors))
    check(not any(r["is_spi"] for r in ctors), "no constructor is marked SPI")

    print("\n-- control (d): every guard registered, runtime ones included --")
    check(any("JITSI_MEET type-level: @WebServiceProfile" in c for c in comments),
          "Jitsi type-level profile guard registered")
    check(any("ZOOM type-level: @WebServiceProfile" in c for c in comments),
          "Zoom type-level profile guard registered")
    check(any("sendRejoinForCollectingRoom (default false)" in c for c in comments),
          "Zoom @Value flag sendRejoinForCollectingRoom registered, default false")
    check(any("enableWaitingRoom (default false)" in c for c in comments),
          "Zoom @Value flag enableWaitingRoom registered, default false")
    check(any("runtime guard: this.sendRejoinForCollectingRoom" in c for c in comments),
          "the IN-BODY guard is registered, not only the annotation",
          "notifyCollectingRoomOpened returns early when the flag is false")

    print("\n-- control (e): nothing classified local may reach the network --")
    # The defect P94 carried: counting only what a method's own body does.
    for provider, expected in (("JITSI_MEET", 1), ("ZOOM", 5)):
        reaching = [r for r in rows
                    if r["provider"] == provider and r["is_spi"] and r["reaches"]]
        check(len(reaching) == expected,
              "%s: %d of %d SPI methods reach the network" % (provider, expected, SPI_COUNT),
              "measured %d: %s" % (len(reaching), ", ".join(r["method"] for r in reaching)))

    zoom_spi = [r for r in rows if r["provider"] == "ZOOM" and r["is_spi"]]
    check(all(r["direct"] == 0 for r in zoom_spi),
          "ZOOM: ZERO SPI methods call the network directly",
          "all 5 reach it through helpers -- a direct-call count scores this 0, not 5")

    deep = [r for r in zoom_spi if r["reaches"] and r["depth"] and r["depth"] >= 3]
    check(len(deep) == 4, "ZOOM: 4 of the 5 sit 3+ calls from the socket",
          ", ".join("%s(d=%d)" % (r["method"], r["depth"]) for r in deep))

    worst = max((r for r in zoom_spi if r["reaches"]), key=lambda r: r["depth"])
    check(worst["method"] == "disposeServiceRoomsForExam" and worst["depth"] == 4,
          "the deepest is disposeServiceRoomsForExam at depth 4",
          "and it calls disposeBreakOutRoom inside a forEach: N rooms -> N deletions")

    jitsi_local = [r for r in rows
                   if r["provider"] == "JITSI_MEET" and r["is_spi"] and not r["reaches"]]
    check(len(jitsi_local) == 13 and all(r["direct"] == 0 for r in jitsi_local),
          "JITSI_MEET: the other 13 are genuinely local",
          "Result.EMPTY / Result.of(new NewRoom(...)) -- rooms are implicit in Jitsi")

    failed = [c for c in checks if not c[0]]
    print("\n%d/%d checks passed" % (len(checks) - len(failed), len(checks)))
    if failed:
        sys.exit(1)
    print("""
ACTION 2 VERIFIED (gap 96). The third artefact is audited with the five controls.
Control (c) FAILED on the first run of the extractor -- 8 constructors were being
emitted as methods -- and control (e) corrects P94: Zoom reaches the remote from
5 of 14 SPI methods, not 2, and from NONE of them directly.""")


if __name__ == "__main__":
    main()
