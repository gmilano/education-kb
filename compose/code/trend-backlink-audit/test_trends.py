#!/usr/bin/env python3
"""Controls for the trend-citation resolver (pase 49).

The instrument returned "0 dangling out of 700". A zero is the one result that
has to be earned: this KB's own rule (tendencia 216) is that the positive
control goes BEFORE publishing, because an instrument that cannot find a defect
reports zero for the same reason a correct base does.

    python3 test_trends.py
"""
import os
import sys
import tempfile

import audit_trends as A

CHECKS = []


def ck(label, got, want):
    ok = got == want
    CHECKS.append(ok)
    print("%s %s%s" % ("PASS" if ok else "FAIL", label,
                       "" if ok else "  -> got %r, want %r" % (got, want)))


def defs_of(text):
    fd, path = tempfile.mkstemp(suffix=".md")
    with os.fdopen(fd, "w") as fh:
        fh.write(text)
    try:
        return A.defined_trends(path)
    finally:
        os.unlink(path)


# -- form 1: the numbered header that holds trends 1-196 --------------------
d = defs_of("## 57. La capa de analitica del LMS es permisiva\n")
ck("form 1: numbered header defines the trend", 57 in d, True)
ck("form 1: and names its form", d.get(57, ("",))[0], "numbered-header")
d = defs_of("## 12. Titulo con emoji\n")
ck("form 1: works with a leading emoji",
   36 in defs_of("## \U0001f535 36. La pregunta sin respuesta\n"), True)

# -- form 2: the RANGE header, and the reason pase 48's grep failed ---------
# A range header names only its two ENDPOINTS. The trends between them appear
# in no header text at all -- that, not "210 lives in a row", is why a grep of
# headers for a middle number finds nothing.
d = defs_of("## \U0001f535 Las tendencias 197–210, del pase 47\n")
ck("form 2: the range endpoint resolves", 210 in d, True)
ck("form 2: a number INSIDE the range resolves too", 203 in d, True)
ck("form 2: the full range is declared",
   all(n in d for n in range(197, 211)), True)
ck("form 2: and nothing past the range", 211 in d, False)
ck("form 2: an en-dash range parses",
   197 in defs_of("## Tendencias 197–210\n"), True)
ck("form 2: an em-dash range parses",
   160 in defs_of("## Tendencias 157—166 — el pase 42\n"), True)
ck("form 2: a plain-hyphen range parses",
   160 in defs_of("## Tendencias 157-166\n"), True)
ck("form 2: an absurd range is refused, not expanded",
   defs_of("## Tendencias 1-999\n"), {})

# -- form 3: the table row, and the namespace it SHARES with gaps -----------
TREND_TBL = ("## \U0001f535 Las tendencias 211–219, del pase 48\n"
             "\n| # | Tendencia | Evidencia |\n|---|---|---|\n"
             "| **217** | Una cifra condicional | dos condiciones |\n")
ck("form 3: a row under a trends header is a trend", 217 in defs_of(TREND_TBL),
   True)

# The decisive case: gaps use the SAME `| **N** |` shape. Crediting a gap row
# as a trend would silence a real dangling citation.
GAP_TBL = ("## \U0001f535 Estado de gaps al cierre del pase 48\n"
           "\n| Gap | Estado | Resolucion |\n|---|---|---|\n"
           "| **103** | CERRADO con codigo | mcp-allowlist-gateway |\n")
ck("a GAP row is NOT counted as a trend definition",
   103 in defs_of(GAP_TBL), False)
ck("a gap table yields no trend definitions at all", defs_of(GAP_TBL), {})

# A trends header followed by a gaps header must end the trend context.
MIXED = ("## Las tendencias 211–212, del pase 48\n"
         "| **211** | una | dos |\n"
         "## Estado de gaps al cierre\n"
         "| **104** | CERRADO | dos |\n")
d = defs_of(MIXED)
ck("trend context ENDS at the next, non-trend header",
   (211 in d, 104 in d), (True, False))

# -- citation parsing: the shapes this base actually writes -----------------
def cites_in(line):
    out = []
    for m in A.cite_matches(line):
        blob = m.group(1)
        nums = [int(x) for x in A.NUM.findall(blob)]
        import re as _re
        ranged = (_re.search(r"\d\s*(?:%s|\s+a\s+)\s*\d" % A.DASH, blob)
                  and len(nums) == 2)
        if ranged and nums[0] < nums[1] and nums[1] - nums[0] < 100:
            nums = list(range(nums[0], nums[1] + 1))
        out.extend(nums)
    return out

ck("a single citation parses", cites_in("lo dice la tendencia 216"), [216])
ck("a citation in bold parses", cites_in("la tendencia **216** lo dice"), [216])
ck("a list of citations parses",
   cites_in("las tendencias 213, 216 y 217 lo dejan"), [213, 216, 217])
ck("a RANGE citation expands to its members",
   cites_in("las tendencias 197–199 del pase 47"), [197, 198, 199])
ck("plural with 'e' parses", cites_in("las tendencias 8 e 9"), [8, 9])
ck("a line with no citation yields none",
   cites_in("el gap 103 quedo cerrado con codigo"), [])
ck("'gap N' is never read as a trend citation",
   cites_in("gap 65 y gap 92 siguen abiertos"), [])

# --- P295 (pase 97): la forma con que esta base ANUNCIA sus tendencias --------------------
# El pase 96 escribio "**Ocho tendencias nuevas, numeradas 745-752**" y el control devolvia
# CERO, asi que las ocho quedaron sin seccion y nada lo marco.
ck("la forma del pase 96 ('tendencias nuevas, numeradas N-M') se lee",
   cites_in("Ocho tendencias nuevas, numeradas 745-752"),
   list(range(745, 753)))
ck("y con el guion largo igual",
   cites_in("**Ocho tendencias nuevas, numeradas 745\u2013752** (el pase 95 cerro en 744)"),
   list(range(745, 753)))
ck("'tendencias numeradas N a M' se lee",
   cites_in("Tendencias numeradas 745 a 752"), list(range(745, 753)))
ck("singular numerada tambien", cites_in("una tendencia numerada 751"), [751])

# Los NEGATIVOS, que son la razon por la que el ancla es `numerad*` y no "cualquier palabra":
# si se permitiera texto libre, un anio se leeria como cita (y `\d{1,3}` lo truncaria a 3).
ck("un anio NO es una cita, con 'de' en el medio",
   cites_in("las tendencias de 2026 muestran otra cosa"), [])
ck("un anio NO es una cita, ni con el ancla ausente",
   cites_in("las tendencias nuevas de 2026 son ocho"), [])
ck("'numerad*' sin la palabra tendencia no es una cita",
   cites_in("las filas numeradas 1-5 de la tabla"), [])
ck("el texto intermedio esta ACOTADO: 60 caracteres no cuelan",
   cites_in("tendencias " + "x" * 60 + " numeradas 745-752"), [])
ck("una cita ya legible no se cuenta DOS veces",
   cites_in("Ver tendencias 706-711."), [706, 707, 708, 709, 710, 711])

print("\n%d/%d checks passed" % (sum(CHECKS), len(CHECKS)))
sys.exit(0 if all(CHECKS) else 1)
