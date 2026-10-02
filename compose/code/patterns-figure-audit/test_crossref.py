#!/usr/bin/env python3
"""Positive controls for the --crossref attribution rules (pase 49).

Pase 49 ran --crossref and got 7 STALE findings. None of them was real, and the
reason took two tries to find -- which is why these checks exist:

  * First reading: the prose "already says the right number and quotes the old
    one as history". True of one line, and it produced a correction rule.
  * Then the control was run, and the rule turned out to be satisfied by
    COINCIDENCE: the window the instrument actually handed it was **5.635
    characters** long. Every KB file opens with a long `>` blockquote with no
    blank line in it, so the "paragraph" window swallowed the whole file header
    and a suite named 4.000 characters away was read as the figure's owner.

So the real defect was the WINDOW, and the measurement that proves it is that
bounding the window pushed `unattributed` UP from 31 to 36: five attributions
had been manufactured by window size alone.

A fix that only removes findings is a mute button, not an instrument. These
checks pin down that the false ones go and the real ones stay.

    python3 test_crossref.py
"""
import sys

from extract_figures import figure_window, records_correction, resolve_owners

CHECKS = []


def ck(label, got, want):
    ok = got == want
    CHECKS.append(ok)
    print("%s %s%s" % ("PASS" if ok else "FAIL", label,
                       "" if ok else "  -> got %r, want %r" % (got, want)))


# -- figure_window: the defect that produced all 7 false findings -----------
# A blockquote header with no blank line, exactly the shape of all eight files.
BLOCKQUOTE = [
    "> Bases sobre las cuales construir, verificado repo por repo.",
    "> Leer la columna Licencia antes de proponer.",
    "> El barrido del pase 48 recorrio proctoring-reach-audit y mas.",
    "> Relleno que menciona mcp-allowlist-gateway muy lejos del numero.",
    "> La linea del medio con 23 aserciones vive aca.",
    "> Y una linea posterior que tambien es parte del blockquote.",
    "> Otra mas, para que el run sea largo.",
]
win = figure_window(BLOCKQUOTE, 5)          # the "23 aserciones" line
ck("prose window stays bounded to the line +/- 1",
   win, " ".join(BLOCKQUOTE[3:6]))
ck("prose window does NOT swallow the whole blockquote run",
   "proctoring-reach-audit" in win, False)
ck("prose window DOES keep the line one below (the condition can sit there)",
   "linea posterior" in win, True)

# The original rationale this bound preserves: prose is hard-wrapped at ~100
# chars, so a condition one line down must still be visible.
WRAPPED = ["texto previo", "la suite da 20/20 aserciones",
           "con la ruta a un checkout de seb-server"]
ck("a condition wrapped onto the next line is still in the window",
   "con la ruta" in figure_window(WRAPPED, 2), True)

# A table row is a self-contained record: the window is the row, never the
# neighbouring rows (markdown tables carry no blank line between them).
TABLE = ["| SEB proctoring | 11/11 checks | MIT |",
         "| UniTime gate | 46 aserciones | MIT |",
         "| allowlist | 34 aserciones | MIT |"]
ck("table row window is exactly the row", figure_window(TABLE, 2), TABLE[1])
ck("table row window excludes the neighbouring rows",
   "11/11" in figure_window(TABLE, 2), False)
ck("a prose line next to a table does not absorb the table rows",
   figure_window(["prose with 23 aserciones", "| a | 46 | b |"], 1),
   "prose with 23 aserciones")

# -- records_correction: the conjunct that keeps the rule falsifiable --------
# A marker ALONE must not excuse a figure: "hoy" is ordinary Spanish and
# appears throughout this KB.
ck("marker but NO current value -> still a defect",
   records_correction("hoy la suite publica 11/11 checks", [37]), False)
ck("current value but NO marker -> still a defect",
   records_correction("la suite da 11/11 checks y tambien 37 cosas", [37]),
   False)
ck("neither marker nor value -> still a defect",
   records_correction("la puerta expone 11/11 checks", [37]), False)
ck("empty window -> not a correction", records_correction("", [37]), False)
ck("no measured value available -> cannot claim a correction",
   records_correction("hoy **37/37**", [None]), False)
# The real foundations.md:30 shape: old value quoted, new value stated beside it.
ck("old value quoted WITH today's value beside it -> history",
   records_correction("<<11/11 checks>> (hoy **37/37**), y <<23>> (hoy 46)",
                      [37, 46]), True)
# A live catalogue row quoting a stale count is the case this KB was burned by
# (verticals/solutions.md:1690, pase 48). It must stay a defect.
ck("live catalogue row, stale count -> still a defect",
   records_correction("| SEB proctoring | 11/11 checks | MIT |", [37]), False)
# A digit inside a larger number must not count as today's value.
ck("today's value must not match inside a longer number",
   records_correction("hoy el barrido midio 1.836 y 3.711 cifras", [83]),
   False)

# -- resolve_owners: one figure must not become N findings -------------------
MEAS = {"proctoring-reach-audit": (19, "", ""),
        "mcp-allowlist-gateway": (34, "", ""),
        "sebserver-mcp-gate": (37, "", "")}

ck("figure matching one of several named suites -> charged to THAT one",
   resolve_owners(["proctoring-reach-audit", "mcp-allowlist-gateway"], 34,
                  MEAS),
   (["mcp-allowlist-gateway"], False))
ck("figure matching NONE of several named -> ambiguous, not charged to each",
   resolve_owners(["proctoring-reach-audit", "mcp-allowlist-gateway"], 23,
                  MEAS),
   (["proctoring-reach-audit", "mcp-allowlist-gateway"], True))
ck("ONE named suite, figure does not match -> a plain defect, not ambiguous",
   resolve_owners(["sebserver-mcp-gate"], 11, MEAS),
   (["sebserver-mcp-gate"], False))
ck("ONE named suite, figure matches -> charged, not ambiguous",
   resolve_owners(["sebserver-mcp-gate"], 37, MEAS),
   (["sebserver-mcp-gate"], False))
ck("a conditional value counts as ownership",
   resolve_owners(["proctoring-reach-audit", "mcp-allowlist-gateway"], 20,
                  MEAS),
   (["proctoring-reach-audit"], False))

# The old code did `named = owners` INSIDE the per-figure loop, which
# permanently narrowed the suite list for every LATER figure on the same line.
_named = ["proctoring-reach-audit", "mcp-allowlist-gateway"]
resolve_owners(_named, 34, MEAS)
ck("resolve_owners does not mutate its argument",
   _named, ["proctoring-reach-audit", "mcp-allowlist-gateway"])

print("\n%d/%d checks passed" % (sum(CHECKS), len(CHECKS)))
sys.exit(0 if all(CHECKS) else 1)
