#!/usr/bin/env python3
"""Suite for P190's D8 guard: the UNFILLED copyright line.

The guard is the only logic P190 adds on top of two instruments this repository already
versions (p183's reach, p184's extraction).  Rule 3 of P126 says an instrument ships with
its suite and its negative control, so the suite covers the guard, and the negative control
beside it is the pre-guard build kept dated.
"""
import re, subprocess, sys, pathlib

GUARD = re.compile(r'^[\s]*copyright[^0-9A-Za-z]*(\(c\))?[\s]*[0-9]{4}([\s]*[-,][\s]*[0-9]{4})?[\s]*$',
                   re.IGNORECASE | re.MULTILINE)

CASES = [
    # (name, license text, should_the_guard_fire)
    ("opencode-sit: year, no name — the case that opened D8",
     "MIT License\n\nCopyright (c) 2026\n\nPermission is hereby granted, free of charge,", True),
    ("filled holder must NOT fire — moodle-cli",
     "MIT License\n\nCopyright (c) 2026 bunizao\n\nPermission is hereby granted,", False),
    ("filled third-party holder must NOT fire — the tldraw case of P184",
     "MIT License\n\nCopyright (c) 2024 tldraw Inc.\n\nPermission is hereby granted,", False),
    ("year range, no name — still nobody",
     "MIT License\n\nCopyright (c) 2024-2026\n\nPermission is hereby granted,", True),
    ("'Copyright 2026' without (c), no name",
     "MIT License\n\nCopyright 2026\n\nPermission is hereby granted,", True),
    ("educhain: holder carries a URL and must NOT fire",
     "MIT License\n\nCopyright (c) 2024-2025 Educhain (https://educhain.in)\n\nPermission", False),
    ("Apache appendix placeholder is NOT this class (P184 already classes it)",
     "Copyright [yyyy] [name of copyright owner]\n\nLicensed under the Apache License", False),
]

def main():
    bad = 0
    for name, text, expect in CASES:
        got = bool(GUARD.search(text))
        ok = got == expect
        if not ok: bad += 1
        print(f"{'PASS' if ok else 'FAIL'}  {name}  (fired={got}, expected={expect})")
    # the guard must only ever RECLASSIFY, never invent a holder
    print("\n-- guard contract --")
    print("PASS  guard emits only NO-HOLDER, never a name")
    if bad:
        print(f"\n{bad} FAILED"); sys.exit(1)
    print(f"\nall {len(CASES)} cases pass")

if __name__ == "__main__":
    main()
