#!/usr/bin/env python3
"""Insert a pass section directly after a shelf's YAML frontmatter.

Append-only applies to SECTIONS: the new dated section goes at the top of the
body and the whole history stays below it, untouched. The frontmatter is
rewritten only to move `updated:` forward, and `region:` is never touched --
it is a closed vocabulary of exactly five values and p774's gate-regions found
the vocabulary intact base-wide.
"""
import io, re, sys

def main(shelf, section_path, updated="2026-11-11"):
    s = io.open(shelf, encoding="utf-8").read()
    new = io.open(section_path, encoding="utf-8").read().rstrip() + "\n\n"
    m = re.match(r"\A---\n(.*?\n)---\n", s, re.S)
    if not m:
        raise SystemExit(f"{shelf}: no YAML frontmatter -- refusing to write")
    fm, body = m.group(1), s[m.end():]
    before = fm
    fm = re.sub(r"^updated:.*$", f"updated: {updated}", fm, flags=re.M)
    if "updated:" not in fm:
        fm = fm.rstrip("\n") + f"\nupdated: {updated}\n"
    # region: must remain one of the five closed values
    rm = re.search(r"^region:\s*(.+?)\s*$", fm, re.M)
    if rm:
        allowed = {"North America", "EMEA", "APAC", "LATAM", "Global"}
        vals = {v.strip() for v in rm.group(1).split("|")}
        bad = vals - allowed
        if bad:
            raise SystemExit(f"{shelf}: region vocabulary violation {bad}")
    out = "---\n" + fm + "---\n\n" + new + body.lstrip("\n")
    io.open(shelf, "w", encoding="utf-8").write(out)
    print(f"  {shelf}: +{len(new)} B  (frontmatter updated:{'' if before==fm else ' bumped'})")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
