#!/usr/bin/env python3
"""Inventory every MEASUREMENT in compose/patterns.md and name its instrument.

Pase 47, action 2 (gap 101). The pase 46 case is the warning: "481 / 912 lineas"
was CORRECT -- they are non-blank-non-comment lines, while `wc -l` gives
583 / 1.116 -- and because the metric was never written down, nobody could
reproduce it for three passes. A proposal quoting it would have defended a
number that did not add up.

This script does the sweep, so the sweep is repeatable rather than a one-off
list that rots:

    python3 extract_figures.py                 # the inventory, grouped by unit
    python3 extract_figures.py --check         # + re-run the local instruments
    python3 extract_figures.py --tsv           # machine-readable

A figure is "reproducible today" only if a command in THIS environment returns
it. Star counts, commit counts and download counts are not: github.com answers
403 to curl here and api.github.com answers 200 with a body that denies access
(pass 37). That is a property of the channel, and it is reported, not hidden.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KB = os.path.abspath(os.path.join(HERE, "..", ".."))
PATTERNS = os.path.join(KB, "patterns.md")
CODE = os.path.join(KB, "code")

#: Units that denote a measurement. Order matters: longest match first.
UNITS = [
    ("assertions", r"aserciones?|checks?|pruebas?|tests?"),
    ("lines", r"l[íi]neas?|lines?"),
    ("tools", r"tools?"),
    ("methods", r"m[ée]todos?|methods?"),
    ("routes", r"rutas?|endpoints?"),
    ("files", r"archivos?|files?"),
    ("modules", r"m[óo]dulos?"),
    ("classes", r"clases?"),
    ("fields", r"campos?"),
    ("tables", r"tablas?"),
    ("rows", r"filas?|rows?"),
    ("stars", r"★|estrellas?"),
    ("commits", r"commits?"),
    ("downloads", r"descargas?|downloads?"),
    ("percent", r"%"),
]

NUM = r"(?:\*\*)?(\d[\d\.,]*)(?:\*\*)?"
OF = r"(?:\s*de\s+(?:\*\*)?\d[\d\.,]*(?:\*\*)?)?"


def inventory(text: str) -> list[dict]:
    out = []
    for lineno, line in enumerate(text.split("\n"), 1):
        for unit, pat in UNITS:
            # (?![\w...]) rather than \b: \b after a non-word character never
            # fires, and that silently dropped EVERY percentage from the first
            # version of this sweep -- the sweep's own instrument bug, caught by
            # cross-checking its total against a looser grep.
            rx = NUM + OF + r"\s*(?:" + pat + r")(?![\wáéíóúñ])"
            for m in re.finditer(rx, line, re.I):
                out.append(
                    {
                        "line": lineno,
                        "unit": unit,
                        "value": m.group(1),
                        "text": re.sub(r"\s+", " ", m.group(0)).strip(),
                        "context": re.sub(r"\s+", " ", line[max(0, m.start() - 60) : m.end() + 40]),
                    }
                )
    return out


#: The instrument for each unit: the command that returns the figure, and
#: whether that command can run in THIS environment.
INSTRUMENTS = {
    "assertions": (
        "python3 compose/code/<dir>/test_*.py  (count the trailing 'N/N checks passed';"
        " some suites need an argument or an env var -- see per-figure notes)",
        True,
    ),
    "lines": (
        "wc -l <file>  for raw lines; grep -cvE '^[[:space:]]*(#.*)?$' <file> for"
        " non-blank-non-comment. THE TWO DISAGREE: name which one.",
        True,
    ),
    "tools": (
        "echo '{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/list\"}' | <server over stdio>"
        "  -- needs the package installed, so NOT reproducible here",
        False,
    ),
    "methods": (
        "grep -cE '<language method signature>' over a clone; for a Java SPI,"
        " count abstract methods in the interface",
        True,
    ),
    "routes": (
        "grep -oE '@(Get|Post|Put|Delete|Request)Mapping|@Service\\(\"/' over a clone,"
        " or the servlet's <url-pattern>",
        True,
    ),
    "files": ("git ls-tree -r HEAD --name-only | grep -c <pattern>  on a blobless clone", True),
    "modules": ("ls the module directory on a clone, or read the add-on registry", True),
    "classes": ("grep -cE '^class ' <file>", True),
    "fields": ("read the schema / serializer and count declared fields", True),
    "tables": ("grep the migration or the delete cascade for table names", True),
    "rows": ("grep -vc '^#' <the tsv>  for a measured table; count rows of agents/top.md", True),
    "stars": ("github.com -> 403 for curl here; api.github.com denies in the body (pass 37)", False),
    "commits": ("git rev-list --count HEAD on a full clone; the shallow clones here cannot", False),
    "downloads": ("the registry API (pypi.org/npmjs) -- reachable per-case, not swept", False),
    "percent": ("DERIVED: name the numerator and denominator, not the percentage", True),
}

#: Figures checked by hand in pase 47, with the instrument that returns them and
#: what it actually returned. This is the part that turns a list into a finding.
VERIFIED = [
    # (lines in patterns.md, published, instrument, today, verdict)
    ("23, 203", "33 aserciones",
     "python3 compose/code/openedx-course-generator/test_plan.py", "33", "OK"),
    ("608", "23 aserciones, 23 en verde",
     "python3 compose/code/unitime-mcp-gate/test_gate.py", "46", "STALE"),
    ("345", "11/11 checks",
     "python3 compose/code/sebserver-mcp-gate/test_gate.py", "37/37", "STALE"),
    ("423", "20/20",
     "python3 compose/code/proctoring-reach-audit/test_reach.py /path/to/seb-server",
     "20/20 with the path, 19/19 without", "CONDITIONAL"),
    ("5584", "20/20, exige regeneracion byte a byte",
     "idem, and this line DOES state the condition", "20/20", "OK"),
    ("450", "21/21 checks, JDK puro",
     "sh compose/code/seb-proctoring-validator/run_test.sh", "21/21", "OK"),
    ("-", "24/24 (marking, cited in trends and in its README)",
     "SCORM_SCHEMAS=<dir> python3 test_marking.py --with-xmllint",
     "24/24; bare run gives 23/23", "CONDITIONAL"),
    ("445", "481-912 lineas",
     "grep -cvE '^[[:space:]]*(#.*)?$' on the two SEB implementations",
     "481 / 912 non-blank-non-comment; wc -l gives 583 / 1.116", "OK, metric now named"),
    ("521, 615, 5174", "175 lineas de stdlib (P85)",
     "no file in this repository implements it: MCP_ALLOWLIST appears only in"
     " patterns.md, and the two gates that exist use SEB_ALLOW / UNITIME_ALLOW",
     "no measurable artifact", "NOT REPRODUCIBLE"),
    ("616", "~115 lineas de stdlib (UniTime manifest generator)",
     "wc -l compose/code/unitime-mcp-gate/extract_surface.py",
     "186 raw / 152 non-blank-non-comment", "NEITHER"),
    ("5681", "9 checks de scorm_validate",
     "grep -oE 'push\\(\"[a-z0-9-]+\"' src/validate.ts | sort -u | wc -l",
     "9 distinct ids (15 call sites -- the distinct id is the right count)", "OK"),
]


def run(cmd: str) -> str:
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=KB)
    return (p.stdout or p.stderr).strip()


def main() -> int:
    text = open(PATTERNS).read()
    items = inventory(text)
    tsv = "--tsv" in sys.argv

    if tsv:
        print("line\tunit\tvalue\ttext\treproducible_here\tinstrument")
        for it in items:
            instr, ok = INSTRUMENTS[it["unit"]]
            print("%s\t%s\t%s\t%s\t%s\t%s" % (
                it["line"], it["unit"], it["value"], it["text"], "yes" if ok else "no", instr))
        return 0

    print("compose/patterns.md: %d lines" % len(text.split("\n")))
    print("measurements found : %d\n" % len(items))
    by_unit: dict[str, int] = {}
    for it in items:
        by_unit[it["unit"]] = by_unit.get(it["unit"], 0) + 1
    print("%-12s %5s  %-9s %s" % ("unit", "count", "here?", "instrument"))
    repro = norepro = 0
    for unit, _ in UNITS:
        n = by_unit.get(unit, 0)
        if not n:
            continue
        instr, ok = INSTRUMENTS[unit]
        repro += n if ok else 0
        norepro += 0 if ok else n
        print("%-12s %5d  %-9s %s" % (unit, n, "yes" if ok else "NO", instr.split("  ")[0]))
    print("\nreproducible in this environment : %d" % repro)
    print("NOT reproducible here            : %d  (stars, commits, downloads, tool counts)" % norepro)

    print("\n-- figures checked by hand in pase 47 --")
    for ln, pub, instr, got, verdict in VERIFIED:
        flag = {"OK": "ok  ", "STALE": "STALE", "CONDITIONAL": "COND", "NEITHER": "NEITH",
                "NOT REPRODUCIBLE": "GONE"}.get(verdict, "ok  ")
        print("  [%-5s] L%-16s %s" % (flag, ln, pub))
        print("           instrument: %s" % instr)
        print("           today     : %s" % got)

    if "--check" in sys.argv:
        print("\n-- re-running the local instruments --")
        for name, cmd in (
            ("openedx-course-generator",
             "cd code/openedx-course-generator && python3 test_plan.py 2>&1 | grep -ciE '^PASS '"),
            ("unitime-mcp-gate",
             "cd code/unitime-mcp-gate && python3 test_gate.py 2>&1 | grep -ciE '^PASS '"),
            ("sebserver-mcp-gate",
             "cd code/sebserver-mcp-gate && python3 test_gate.py 2>&1 | grep -oE '[0-9]+/[0-9]+ checks' | tail -1"),
            ("proctoring-reach-audit",
             "cd code/proctoring-reach-audit && python3 test_reach.py 2>&1 | grep -oE '[0-9]+/[0-9]+ checks' | tail -1"),
            ("aiact-50-2-marking",
             "cd code/aiact-50-2-marking && python3 test_marking.py 2>&1 | grep -oE '[0-9]+/[0-9]+ checks' | tail -1"),
            ("aiact-50-2-pack",
             "cd code/aiact-50-2-pack && python3 test_pack.py 2>&1 | grep -oE '[0-9]+/[0-9]+ checks' | tail -1"),
            ("P85 gateway (175 lines)",
             "grep -rl MCP_ALLOWLIST code/ 2>/dev/null"
             " | grep -v patterns-figure-audit | head -1 || true"),
        ):
            print("  %-26s -> %s" % (name, run(cmd) or "(nothing)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
