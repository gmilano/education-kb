#!/usr/bin/env python3
"""Run `count_tools.drift` over unpacked npm payloads and emit a TSV.

    python3 -I run_drift.py <unpacked-package-dir> [...]

Each directory is the `package/` root of a tarball already downloaded and sha1-verified
by `p138-npm-payload-licence`. Nothing in them is executed.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import count_tools  # noqa: E402


def main(argv):
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    rows = []
    print("package\tsource_files\tidiom\tbuild_tools\tdocumented\tundocumented\t"
          "write_tools\tundocumented_writes\tphantom\tdisagrees\tundocumented_names")
    for d in argv[1:]:
        r = count_tools.drift(d)
        rows.append(r)
        print("\t".join([
            r["package"] or Path(d).name,
            str(r["source_files"]),
            r["idiom"],
            str(len(r["build_tools"])),
            str(len(r["documented"])),
            str(len(r["undocumented"])),
            str(len(r["write_tools"])),
            str(len(r["undocumented_writes"])),
            str(len(r["phantom"])),
            "YES" if r["disagrees"] else "no",
            ",".join(r["undocumented"][:8]) or "-",
        ]))

    n = len(rows)
    dis = sum(1 for r in rows if r["disagrees"])
    tot_u = sum(len(r["undocumented"]) for r in rows)
    tot_uw = sum(len(r["undocumented_writes"]) for r in rows)
    print(f"\n# rows={n} disagree={dis} ({100 * dis // n if n else 0}%) "
          f"threshold=a third ({'NOT REFUTED' if n and dis * 3 >= n else 'REFUTED'})")
    print(f"# undocumented_tools={tot_u} of which WRITE={tot_uw} "
          f"({100 * tot_uw // tot_u if tot_u else 0}%)")
    for r in rows:
        if r["undocumented_writes"]:
            print(f"#   {r['package']}: {', '.join(r['undocumented_writes'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
