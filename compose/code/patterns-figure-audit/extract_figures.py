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
    python3 extract_figures.py --all           # all eight KB files, per file (pase 48)
    python3 extract_figures.py <path>          # any one file
    python3 extract_figures.py --crossref      # re-run every suite, find stale quotes
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
ROOT = os.path.abspath(os.path.join(KB, ".."))

#: The eight KB files. Pase 47 swept only patterns.md because it is the most
#: cited asset; pase 48 (action 2) sweeps all eight, because trends.md and
#: market.md are the two largest files in the base and neither had ever been
#: measured by this instrument.
KB_FILES = [
    "agents/top.md", "agents/trending.md",
    "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md", "intel/trends.md",
    "compose/patterns.md",
]

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


def sweep_all() -> int:
    """Action 2 of pase 48: the inventory per file, over the eight KB files."""
    print("%-26s %8s %8s %8s %8s" % ("file", "lines", "KB", "figures", "per-kline"))
    total_f = total_l = 0
    rows = []
    for rel in KB_FILES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print("%-26s %8s" % (rel, "MISSING"))
            continue
        text = open(path).read()
        nlines = len(text.split("\n"))
        items = inventory(text)
        total_f += len(items)
        total_l += nlines
        rows.append((rel, items))
        print("%-26s %8d %8d %8d %8.1f" % (
            rel, nlines, round(len(text.encode()) / 1024), len(items),
            1000.0 * len(items) / nlines))
    print("%-26s %8d %8s %8d %8.1f" % ("TOTAL", total_l, "", total_f,
                                       1000.0 * total_f / total_l))

    print("\n-- by unit, across the eight files --")
    agg: dict[str, int] = {}
    for _, items in rows:
        for it in items:
            agg[it["unit"]] = agg.get(it["unit"], 0) + 1
    print("%-12s %6s  %-6s %s" % ("unit", "count", "here?", "instrument"))
    repro = norepro = 0
    for unit, _ in UNITS:
        n = agg.get(unit, 0)
        if not n:
            continue
        instr, ok = INSTRUMENTS[unit]
        repro += n if ok else 0
        norepro += 0 if ok else n
        print("%-12s %6d  %-6s %s" % (unit, n, "yes" if ok else "NO", instr.split("  ")[0]))
    print("\nreproducible in this environment : %d" % repro)
    print("NOT reproducible here            : %d" % norepro)
    print("\n\u26a0 A figure counted here is a figure FOUND, not a figure VERIFIED.")
    print("  Hand-verification is per-figure and only the ones over this base's own")
    print("  code are reproducible; see VERIFIED below and the README.")
    return 0


def main() -> int:
    if "--crossref" in sys.argv:
        return crossref()
    if "--all" in sys.argv:
        return sweep_all()
    paths = [a for a in sys.argv[1:] if not a.startswith("--")]
    target = os.path.abspath(paths[0]) if paths else PATTERNS
    text = open(target).read()
    items = inventory(text)
    tsv = "--tsv" in sys.argv

    if tsv:
        print("line\tunit\tvalue\ttext\treproducible_here\tinstrument")
        for it in items:
            instr, ok = INSTRUMENTS[it["unit"]]
            print("%s\t%s\t%s\t%s\t%s\t%s" % (
                it["line"], it["unit"], it["value"], it["text"], "yes" if ok else "no", instr))
        return 0

    print("%s: %d lines" % (os.path.relpath(target, ROOT), len(text.split("\n"))))
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




# ---------------------------------------------------------------------------
# --crossref: pase 48, action 2. The defect pase 47 did NOT see.
#
# Pase 47 found "11/11 checks" stale in compose/patterns.md and corrected it
# THERE. The same figure was still being quoted as a live measurement in four
# other files. The defect is therefore not "a figure goes stale when the suite
# grows" -- it is that A CORRECTION DOES NOT PROPAGATE, because one measurement
# is quoted in up to ten places across eight files.
#
# So the instrument has to be cross-file: run each suite, then find every
# quotation of a check count anywhere in the KB and report which ones no longer
# match. Attribution is by the suite's directory name appearing in the same
# line; a quotation with no suite name in the line is reported as UNATTRIBUTED
# rather than guessed, because guessing is what produced the stale figures.
# ---------------------------------------------------------------------------

#: suite directory -> (command, env/arg note). The count is MEASURED, not stored.
SUITES = {
    "openedx-course-generator": ("python3 test_plan.py", ""),
    "unitime-mcp-gate": ("python3 test_gate.py", ""),
    "sebserver-mcp-gate": ("python3 test_gate.py", ""),
    "seb-proctoring-validator": ("sh run_test.sh", ""),
    "aiact-50-2-marking": ("python3 test_marking.py", "24 with SCORM_SCHEMAS + --with-xmllint"),
    "aiact-50-2-pack": ("python3 test_pack.py", "27 bare; more with --with-xmllint"),
    "proctoring-reach-audit": ("python3 test_reach.py", "20 with a seb-server path"),
    "mcp-allowlist-gateway": ("python3 test_gateway.py", ""),
}

#: suite -> {count: the condition that produces it}. A quotation of one of these
#: is correct ONLY where the condition travels with it.
CONDITIONAL = {
    "aiact-50-2-marking": {24: "--with-xmllint + SCORM_SCHEMAS", 23: "bare"},
    "aiact-50-2-pack": {37: "with both schema dirs", 27: "bare"},
    "proctoring-reach-audit": {20: "with a seb-server path", 19: "bare"},
}

#: Tokens that show a condition is stated near the figure.
COND_TOKENS = re.compile(
    r"xmllint|SCORM_SCHEMAS|sin [ée]l|sin ellos?|bare|con los dos|"
    r"con la ruta|with the path|condicional|exige|requiere|--with-",
    re.I)

QUOTE_RX = re.compile(
    r"(?:\*\*)?(\d{1,3})\s*/\s*(\d{1,3})(?:\*\*)?\s*(?:checks?|aserciones?)"
    r"|(?:\*\*)?(\d{1,3})(?:\*\*)?\s+aserciones?"
    r"|\(\s*(?:\*\*)?(\d{1,3})(?:\*\*)?\s*\)\s*(?:checks?|aserciones?)",
    re.I)

#: Tokens showing the window is RECORDING A CORRECTION, not making a claim.
#: Pase 49 ran --crossref and got 7 STALE. Reading all 7 showed every one sat on
#: prose that already carried the RIGHT number and quoted the wrong one as
#: history ("«11/11 checks» (hoy **37/37**)"). Acting on them would have
#: re-broken correct text -- the exact opposite of what this file exists for.
CORRECTION_RX = re.compile(
    r"\bhoy\b|\u2192|quedaron?\s+corregidas?|corregidas?\s+donde|VENCIDA|"
    r"se\s+\*{0,2}reemplaza|cifra\s+del\s+pase|la\s+subi\u00f3|pas\u00f3\s+a",
    re.I)


def records_correction(window: str, todays) -> bool:
    """True when the window quotes a figure IN ORDER TO record it was already
    corrected.

    Two conjuncts, and the second is what keeps this falsifiable: a correction
    marker alone is not enough, because "hoy" also appears in ordinary prose.
    The window must ALSO carry a current measured value. Prose that says "hoy"
    without stating the right number stays a defect and stays reported.
    """
    if not CORRECTION_RX.search(window):
        return False
    return any(re.search(r"(?<!\d)%d(?!\d)" % t, window) for t in todays if t)


def figure_window(lines, lineno):
    """The text a figure is read in context of.

    Pase 48 set the rule as "table row => the row; prose => the paragraph", and
    the implementation grew the prose window while lines were non-blank and not
    table rows. Pase 49 measured what that actually returns on these files:
    **5.635 and 9.914 characters**. Every one of the eight KB files opens with a
    long `>` blockquote carrying no blank line, so the "paragraph" swallowed the
    whole header -- and a suite named 4.000 characters away was read as the
    owner of the figure. That is how 7 STALE findings appeared on prose that
    never mentioned those suites near the number.

    The original rationale was narrow and correct: prose is hard-wrapped at
    ~100 chars, so a condition can sit one line below the figure. One line
    below is therefore the window -- bounded, not a run.
    """
    i = lineno - 1
    if lines[i].lstrip().startswith("|"):
        return lines[i]
    lo = max(0, i - 1)
    hi = min(len(lines) - 1, i + 1)
    out = []
    for j in range(lo, hi + 1):
        if lines[j].lstrip().startswith("|") and j != i:
            continue
        out.append(lines[j])
    return " ".join(out)


def resolve_owners(named, val, measured):
    """Which of the suites named in a window a figure belongs to.

    A figure matching one named suite belongs to THAT one (pase 48). Pase 49
    adds the case pase 48 left open: when the figure matches NONE of them, the
    old code reported it against EVERY named suite, turning one figure into N
    findings -- 3 figures became 7 STALE. Ownership is unknown there, and this
    instrument's standing rule is that unknown is reported, never guessed.

    Returns (suites_to_charge, ambiguous).
    """
    owners = [d for d in named
              if measured.get(d, (None,))[0] == val
              or val in CONDITIONAL.get(d, {})]
    if owners:
        return owners, False
    if len(named) > 1:
        return named, True
    return named, False


def measure_suites() -> dict:
    """Run every suite and count its PASS lines. The count is the instrument's
    answer, never a number copied from prose."""
    got = {}
    for d, (cmd, note) in sorted(SUITES.items()):
        wd = os.path.join(CODE, d)
        if not os.path.isdir(wd):
            got[d] = (None, "directory missing", note)
            continue
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                           cwd=wd, timeout=300)
        out = (p.stdout or "") + (p.stderr or "")
        n = len([l for l in out.split("\n") if l.startswith("PASS")])
        m = re.search(r"(\d+)\s*/\s*(\d+)\s+checks passed", out)
        if m:
            n = int(m.group(2))
        got[d] = (n or None, cmd, note)
    return got


def crossref() -> int:
    measured = measure_suites()
    print("-- every suite, re-measured by running it --")
    print("%-28s %7s  %s" % ("suite", "today", "command / condition"))
    for d, (n, cmd, note) in measured.items():
        print("%-28s %7s  %s%s" % (d, n if n else "ERR", cmd,
                                   ("  [" + note + "]") if note else ""))

    print("\n-- every check-count quotation in the eight files, attributed --")
    stale = live_ok = unattributed = conditional = 0
    corrected = ambiguous = 0
    findings = []
    for rel in KB_FILES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        lines = open(path).read().split("\n")
        for lineno, line in enumerate(lines, 1):
            hits = list(QUOTE_RX.finditer(line))
            if not hits:
                continue
            # The window FOLLOWS THE DOCUMENT'S STRUCTURE, which is the whole
            # lesson of this instrument:
            #   * a table row is a self-contained record -> the window is the row.
            #     Widening it to the "paragraph" swallows the neighbouring rows,
            #     because markdown tables carry no blank line between them, and
            #     then every suite named in the table is attributed to every
            #     figure in it (pase 48 measured exactly that: 3 findings became
            #     9, and 6 of those were manufactured by the window).
            #   * prose is hard-wrapped at ~100 chars -> the window is the
            #     paragraph, or the condition one line down is missed.
            window = figure_window(lines, lineno)
            named = [d for d in SUITES if d in window]
            for m in hits:
                g = [x for x in m.groups() if x]
                val = int(g[-1]) if len(g) == 1 else int(g[1])
                if not named:
                    unattributed += 1
                    continue
                # Disambiguation: a window may name several suites (pase 48 found
                # one paragraph citing proctoring-reach-audit AND
                # seb-proctoring-validator). A figure that matches one of them
                # belongs to THAT one; charging it to all of them manufactures a
                # finding. If it matches none, every named suite is reported,
                # because then the figure is wrong for all of them.
                # NB: the old code did `named = owners` INSIDE this loop,
                # which permanently narrowed the list for every later figure on
                # the same line. Resolution is per-figure now.
                charge, ambig = resolve_owners(named, val, measured)
                todays = [measured.get(d, (None,))[0] for d in named]
                if val not in todays and records_correction(window, todays):
                    corrected += 1
                    continue
                if ambig:
                    ambiguous += 1
                    findings.append(("AMBIG", rel, lineno, "/".join(charge),
                                     val, None, "",
                                     re.sub(r"\s+", " ", line)[:105]))
                    continue
                for d in charge:
                    today = measured.get(d, (None,))[0]
                    if today is None:
                        continue
                    alt = CONDITIONAL.get(d, {})
                    if val == today:
                        live_ok += 1
                    elif val in alt:
                        if COND_TOKENS.search(window):
                            live_ok += 1          # correct AND conditioned
                        else:
                            conditional += 1
                            findings.append(("COND", rel, lineno, d, val, today,
                                             alt[val],
                                             re.sub(r"\s+", " ", line)[:105]))
                    else:
                        stale += 1
                        findings.append(("STALE", rel, lineno, d, val, today, "",
                                         re.sub(r"\s+", " ", line)[:105]))
    for kind, rel, lineno, d, val, today, cond, ctx in findings:
        if kind == "AMBIG":
            print("  AMBIG  %s:%d  %s quotes %s -- matches NONE of the suites"
                  " named here; owner NOT guessed" % (rel, lineno, d, val))
        elif kind == "STALE":
            print("  STALE  %s:%d  %s quotes %s, today %s" % (rel, lineno, d, val, today))
        else:
            print("  COND   %s:%d  %s quotes %s -- real, but only %r, and the"
                  " condition is NOT stated in the paragraph"
                  % (rel, lineno, d, val, cond))
        print("         %s" % ctx)
    print("\nattributed and matching today : %d" % live_ok)
    print("attributed and STALE          : %d" % stale)
    print("attributed, real but UNCONDITIONED : %d" % conditional)
    print("quoted AS ALREADY CORRECTED (history, not a defect) : %d" % corrected)
    print("AMBIGUOUS (matches none of several named suites, not guessed) : %d"
          % ambiguous)
    print("unattributed (no suite name on the line, NOT guessed) : %d" % unattributed)
    print("\n⚠ An append-only dated section is HISTORY: a count that was true when")
    print("  written stays. Only a LIVE reference row is a defect. This tool reports")
    print("  the location; it does not decide, because rewriting a dated section")
    print("  would destroy the time series those files exist to keep.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
