#!/usr/bin/env python3
"""p495 — the prose-claim gate's own suite.

Loaded by explicit path, not by name: `make` runs the suites under `python3 -I`,
which strips the script's own directory from `sys.path` (the `p229` finding, and
`p355-cwd-portability`'s class).  A sibling `import check_claims` dies there while
passing by hand, which is exactly how a working gate stays a one-off.
"""
import os, sys, shutil, tempfile, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("p495_check_claims", os.path.join(HERE, "check_claims.py"))
cc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cc)

PASS, FAIL = [], []


def control(name, got, want):
    (PASS if got == want else FAIL).append(name)
    if got != want:
        print("   🔴 %-44s got %r, want %r" % (name, got, want))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def register(path, rows):
    body = ["claim_id\tgrep_key\trequired_file\tpass_of_record\twhy_it_matters"]
    body += ["\t".join(r) for r in rows]
    write(path, "\n".join(body) + "\n")


def verdicts(root, reg):
    return {r["claim_id"]: r["verdict"] for r in cc.grade(root, cc.read_register(reg))}


def refusal(root, reg):
    try:
        cc.grade(root, cc.read_register(reg))
    except SystemExit as exc:
        return str(exc)
    return "NO-REFUSAL"


def main():
    tmp = tempfile.mkdtemp(prefix="p495-")
    try:
        root = os.path.join(tmp, "kb")
        reg = os.path.join(tmp, "reg.tsv")

        # --- the detector's core: present / lost / archive-only -------------
        write(os.path.join(root, "intel/market.md"), "Singapore published the agentic AI framework in 2026.\n")
        write(os.path.join(root, "archive/2026-10-19-p315-pre-rewrite/intel-market.md"),
              "Singapore published the agentic AI framework in 2026. AI Verify is voluntary.\n")
        write(os.path.join(root, "scratchpad/p444/notes.md"), "a EMEA vendor share figure\n")
        register(reg, [
            ("C-PRESENT", "agentic AI framework", "intel/market.md", "p494", "the APAC sales asset"),
            ("C-LOST", "a fact nobody holds any more", "intel/market.md", "p494", "gone outright"),
            ("C-ARCHIVE", "AI Verify is voluntary", "intel/market.md", "p315", "the procurement gate"),
            ("C-SCRATCH", "a EMEA vendor share figure", "intel/market.md", "p491", "the EMEA gap"),
            ("C-NOFILE", "anything", "intel/missing.md", "p495", "target removed"),
        ])
        v = verdicts(root, reg)
        control("PRESENT in the required file", v["C-PRESENT"], "PRESENT")
        control("CLAIM-LOST when absent everywhere", v["C-LOST"], "CLAIM-LOST")
        control("ARCHIVE-ONLY is the p494 signature", v["C-ARCHIVE"], "ARCHIVE-ONLY")
        control("scratchpad/ counts as archive, not held", v["C-SCRATCH"], "ARCHIVE-ONLY")
        control("NO-SUCH-FILE when the target is gone", v["C-NOFILE"], "NO-SUCH-FILE")
        control("archive detail names the surviving file",
                "p315-pre-rewrite" in [r["detail"] for r in cc.grade(root, cc.read_register(reg))
                                       if r["claim_id"] == "C-ARCHIVE"][0], True)

        # --- exit codes: a loss must FAIL the gate --------------------------
        control("exit 1 while any claim is lost", cc.main(["x", root, reg]), 1)
        register(reg, [("C-PRESENT", "agentic AI framework", "intel/market.md", "p494", "ok")])
        control("exit 0 when every claim is present", cc.main(["x", root, reg]), 0)

        # --- a claim held in BOTH places is held ---------------------------
        write(os.path.join(root, "intel/market.md"),
              "Singapore published the agentic AI framework. AI Verify is voluntary.\n")
        register(reg, [("C-BOTH", "AI Verify is voluntary", "intel/market.md", "p315", "held and archived")])
        control("held in target AND archive is PRESENT", verdicts(root, reg)["C-BOTH"], "PRESENT")

        # --- the key is a LITERAL, graded exactly --------------------------
        register(reg, [("C-CASE", "ai verify is voluntary", "intel/market.md", "p315", "case differs")])
        control("the grep key is case-sensitive", verdicts(root, reg)["C-CASE"], "CLAIM-LOST")

        # --- refusals: this gate never passes by default -------------------
        control("missing register REFUSES", "does not pass by default" in refusal(root, os.path.join(tmp, "nope.tsv")), True)
        register(reg, [("C-BLANK", "", "intel/market.md", "p495", "blank key")])
        control("a BLANK grep_key REFUSES", "BLANK grep_key" in refusal(root, reg), True)
        register(reg, [("C-DUP", "x", "intel/market.md", "p495", "a"), ("C-DUP", "y", "intel/market.md", "p495", "b")])
        control("a duplicate claim_id REFUSES", "duplicate claim_id" in refusal(root, reg), True)
        register(reg, [("C-NOTGT", "x", "", "p495", "no target")])
        control("a row with no required_file REFUSES", "names no required_file" in refusal(root, reg), True)
        register(reg, [])
        control("an EMPTY register REFUSES", "register is empty" in refusal(root, reg), True)
        write(reg, "claim_id\tgrep_key\trequired_file\tpass_of_record\twhy_it_matters\n\tx\tintel/market.md\tp495\tz\n")
        control("a row with no claim_id REFUSES", "no claim_id" in refusal(root, reg), True)

        # --- a key may cross a LINE WRAP (p495's own first failure) --------
        write(os.path.join(root, "intel/trends.md"),
              "It is that **the integration layer inherits the\nauthority of the system**, and none\nof its defences.\n")
        register(reg, [
            ("C-WRAP", "the integration layer inherits the authority of the system", "intel/trends.md", "p495", "wrapped prose"),
            ("C-WRAP-MULTI", "and none of its defences", "intel/trends.md", "p495", "spans two wraps"),
            ("C-WRAP-ABSENT", "the integration layer inherits nothing", "intel/trends.md", "p495", "still absent"),
        ])
        v = verdicts(root, reg)
        control("a key crossing a line wrap is PRESENT", v["C-WRAP"], "PRESENT")
        control("a key crossing two wraps is PRESENT", v["C-WRAP-MULTI"], "PRESENT")
        control("wrap-tolerance does not invent matches", v["C-WRAP-ABSENT"], "CLAIM-LOST")

        # --- a nested archive dir is still an archive ----------------------
        write(os.path.join(root, "intel/market.md"), "nothing here\n")
        write(os.path.join(root, "evidence/archive/old.md"), "a nested archived claim\n")
        write(os.path.join(root, "archive-notes/live.md"), "a live note in a lookalike dir\n")
        register(reg, [
            ("C-NESTED", "a nested archived claim", "intel/market.md", "p495", "nested archive"),
            ("C-LOOKALIKE", "a live note in a lookalike dir", "intel/market.md", "p495", "archive-notes is not archive/"),
        ])
        v = verdicts(root, reg)
        control("a NESTED archive/ dir is an archive", v["C-NESTED"], "ARCHIVE-ONLY")
        control("`archive-notes/` is NOT archive/", v["C-LOOKALIKE"], "CLAIM-LOST")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("── p495-prose-claim-gate suite: %d controls, %d passed, %d FAILED"
          % (len(PASS) + len(FAIL), len(PASS), len(FAIL)))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
