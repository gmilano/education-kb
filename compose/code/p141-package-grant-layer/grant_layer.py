"""p141-package-grant-layer — `ACTION DA`: does consolidation keep per-package licence posture?

p140 pre-registered:

> Check whether `openedx-core`'s **six consolidated top-level packages** each retain their own
> licence posture, or whether consolidation flattened them to one AGPL-3.0 grant. 🔴 *Refuted
> if any of the six carries a per-package licence differing from the distribution's
> `AGPL-3.0-only` -- which would make `T18`'s per-file notice question live again at the
> package layer.*

🔴 **NOT REFUTED: zero of six differs, because zero of six declares anything at all.**

The question p140 asked assumed the interesting failure was DISAGREEMENT between layers. The
measured failure is SILENCE: the distribution declares `AGPL-3.0-only` and ships 35 139 bytes
of licence text in `dist-info/licenses/`, and below that boundary there is not one licence
file, not one SPDX header and not one copyright line in 237 Python files.

🔵 **Why that is the sharper result.** A studio does not usually install `openedx-core` and
leave it there -- it lifts a subtree, `openedx_tagging/` or `openedx_content/`, into its own
codebase. The moment that subtree leaves the wheel it carries NO grant, and AGPL-3.0-only is
the most reciprocal obligation on these shelves. The licence is correct and discoverable at
exactly one layer, and the layer people copy from is not it.

Measures three populations per top-level package: licence/notice FILES, SPDX identifier
headers, and bare copyright lines.
"""

import os
import re
import sys
import zipfile

LICENCE_NAME = re.compile(r"(LICEN[SC]E|COPYING|NOTICE)", re.IGNORECASE)
SPDX = re.compile(rb"SPDX-License-Identifier")
COPYRIGHT = re.compile(rb"Copyright|copyright|\(c\)\s*\d{4}|\xc2\xa9")

COLS = ["package", "py_files", "licence_files", "spdx_headers", "copyright_lines", "verdict"]


def survey_wheel(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    dist_info = sorted({n.split("/")[0] for n in names if n.endswith(".dist-info")
                        or "/" in n and n.split("/")[0].endswith(".dist-info")})
    tops = sorted({n.split("/")[0] for n in names
                   if "/" in n and not n.split("/")[0].endswith(".dist-info")})
    rows = []
    for top in tops:
        members = [n for n in names if n.startswith(top + "/")]
        py = [n for n in members if n.endswith(".py")]
        lic = [n for n in members if LICENCE_NAME.search(os.path.basename(n))]
        spdx = cr = 0
        for n in py:
            try:
                b = z.read(n)
            except KeyError:
                continue
            if SPDX.search(b):
                spdx += 1
            if COPYRIGHT.search(b):
                cr += 1
        verdict = ("SILENT" if not (lic or spdx or cr) else "DECLARES")
        rows.append(dict(zip(COLS, [top, len(py), len(lic), spdx, cr, verdict])))
    # the distribution layer, for contrast
    di = [n for n in names if ".dist-info/" in n and LICENCE_NAME.search(os.path.basename(n))]
    dist_bytes = sum(z.getinfo(n).file_size for n in di)
    return rows, di, dist_bytes, dist_info


def main(argv):
    if not argv:
        print("usage: grant_layer.py <wheel.whl>", file=sys.stderr)
        return 2
    rows, di, dist_bytes, _ = survey_wheel(argv[0])
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    print("\n# distribution layer: %d licence file(s), %d bytes: %s"
          % (len(di), dist_bytes, ",".join(di)), file=sys.stderr)
    print("# package layer: %d packages, %d .py files, %d licence files, %d SPDX, %d copyright"
          % (len(rows), sum(r["py_files"] for r in rows),
             sum(r["licence_files"] for r in rows),
             sum(r["spdx_headers"] for r in rows),
             sum(r["copyright_lines"] for r in rows)), file=sys.stderr)
    silent = [r["package"] for r in rows if r["verdict"] == "SILENT"]
    print("# SILENT packages: %d of %d -> %s" % (len(silent), len(rows), silent),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
