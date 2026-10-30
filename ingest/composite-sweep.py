#!/usr/bin/env python3
"""composite-sweep.py -- p554. Two defect classes found on ONE row, swept across the
whole p554 sample so the base learns how wide each is.

🔴 554-C  COMPOSITE GRANTS. `pupilfirst/pupilfirst`'s `LICENSE` opens with
   "Portions of this software are licensed as follows:" and assigns CC BY-SA 4.0 to
   `docs/`, MIT to client-side JS, and MIT to everything else -- the operative MIT
   text follows BELOW. `grant-verdict.py` reads the TITLE BLOCK (12 lines / 700 B,
   Gap 553-A's fix) and so sees only the CARVE-OUTS. It returns CC-BY-4.0 for a
   repository that is governed by MIT. 🔵 553-A's fix is the direct cause: the window
   that stopped a licence CITING another licence from poisoning the family now stops
   the instrument from reaching the governing grant of a composite file.

🔴 554-D  CC SHORT FORMS. `spdx_of` matches `ATTRIBUTION-SHAREALIKE` and
   `ATTRIBUTION-NONCOMMERCIAL` -- the words in Creative Commons' CANONICAL TITLES. A
   file that writes the SHORT form (`CC BY-SA 4.0`, `CC BY-NC 4.0`) matches neither,
   falls through to the bare `CREATIVE COMMONS` arm, and is reported as plain
   **CC-BY-4.0**. 🔴 That collapses a ShareAlike (copyleft, reaches derivatives) and a
   NonCommercial (not shippable at all) into a plain attribution licence. The error
   runs in the PERMISSIVE direction, which is the direction that reaches a proposal.

This module does not fix either. It MEASURES them, so a successor knows whether it is
patching one row or forty.

USAGE  python3 -I ingest/composite-sweep.py --file sample.txt
"""
import concurrent.futures as cf
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location("gv", os.path.join(HERE, "grant-verdict.py"))
gv = importlib.util.module_from_spec(_s)
_s.loader.exec_module(gv)

COMPOSITE = [
    r"portions of this (software|repository|work) are licen[cs]ed",
    r"licen[cs]ed as follows",
    r"all content residing under",
    r"the following (files|directories|components) are licen[cs]ed",
    r"dual[- ]licen[cs]ed",
]
# 🔴 the forms 554-D proves invisible to `spdx_of`
SHORT = {
    "CC-BY-SA": r"cc[ -]by[ -]sa",
    "CC-BY-NC": r"cc[ -]by[ -]nc",
    "CC-BY-ND": r"cc[ -]by[ -]nd",
}
CANONICAL = {
    "CC-BY-SA": "attribution-sharealike",
    "CC-BY-NC": "attribution-noncommercial",
    "CC-BY-ND": "attribution-noderiv",
}


def one(slug):
    branch, sha = gv.symref(slug)
    if not branch:
        return slug, "DEAD-OR-PRIVATE", "", "", ""
    body = None
    name = None
    for n in ("LICENSE", "LICENSE.md", "LICENSE.txt", "license.txt", "LICENCE",
              "COPYING", "LICENSE.TXT"):
        b = gv.get(f"https://raw.githubusercontent.com/{slug}/{branch}/{n}")
        if b and not b.startswith(b"404"):
            body, name = b.decode("utf-8", "replace"), n
            break
    if body is None:
        return slug, "NO-GRANT-FILE", "", "", ""
    low = body.lower()
    comp = [p for p in COMPOSITE if re.search(p, low)]
    # 554-D: a short form present while its CANONICAL title is absent is invisible
    blind = [k for k, pat in SHORT.items()
             if re.search(pat, low) and CANONICAL[k] not in low]
    tb = gv.title_block(body)
    reported = gv.spdx_of(body)
    # what the family would be if the window were the WHOLE file
    whole = gv.spdx_of(body if len(body) < 700 else body)
    governing = ""
    if comp:
        # the governing grant of a composite file is the one whose OPERATIVE text is
        # present, which is below the window -- report what the body actually carries
        if "permission is hereby granted, free of charge" in low:
            governing = "MIT (operative text present below the window)"
        elif "redistribution and use in source and binary" in low:
            governing = "BSD (operative text present below the window)"
        elif "apache license" in low:
            governing = "Apache-2.0 (named below the window)"
    return (slug, f"{name}[{len(body)}B]", reported,
            "COMPOSITE:" + ";".join(c[:28] for c in comp) if comp else "-",
            (f"554-D-BLIND:{'+'.join(blind)}" if blind else "-")
            + (f" | GOVERNING={governing}" if governing else ""))


def main():
    args = sys.argv[1:]
    if args[:1] == ["--file"]:
        slugs = [l.strip() for l in open(args[1]) if l.strip() and not l.startswith("#")]
    else:
        slugs = args
    print("repo\tgrant_file\tspdx_of_reports\tcomposite_554C\tshortform_554D")
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(one, slugs):
            print("\t".join(r), flush=True)


if __name__ == "__main__":
    main()
