#!/usr/bin/env python3
"""Suite de P249. El control que importa es el NEGATIVO: un canal que no
discrimina debe ser RECHAZADO, no creido -- y la medicion real del pase 81
(403 en 81 de 81) tiene que salir NO-CLAIM por este instrumento."""
import sys
from calibrate import (
    classify_channel, may_believe_negative, channel_defect_from_uniformity,
    verdict_for_sweep, CALIBRATED, NO_DISCRIMINATION, GOOD_NOT_OK,
    BAD_NOT_404, NO_EGRESS,
)

checks = []


def check(name, got, want):
    ok = got == want
    checks.append(ok)
    print("%-4s %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        print("     esperado: %r" % (want,))
        print("     obtenido: %r" % (got,))


# --- caso bueno: el canal que esta base YA tenia (p170, pase 64) ------------
check("raw+HEAD medido hoy (200 bueno / 404 malo) CALIBRA",
      classify_channel(200, 404), CALIBRATED)
check("un canal calibrado SI autoriza leer una ausencia",
      may_believe_negative(CALIBRATED), True)

# --- EL CONTROL NEGATIVO: la medicion literal del pase 81 ------------------
check("github.com por curl -sI (403 bueno / 403 malo) NO calibra",
      classify_channel(403, 403), NO_DISCRIMINATION)
check("un canal que no discrimina NO autoriza leer una ausencia",
      may_believe_negative(NO_DISCRIMINATION), False)
check("api.github.com (403/403) tampoco calibra",
      classify_channel(403, 403), NO_DISCRIMINATION)

# --- otros modos de fallo, que no son el mismo que el de arriba ------------
check("200 al bueno y 200 al malo: no discrimina",
      classify_channel(200, 200), NO_DISCRIMINATION)
check("sin egreso a ninguno de los dos se nombra aparte",
      classify_channel("000", "000"), NO_EGRESS)
check("el bueno no contesta 200: el canal no esta listo",
      classify_channel(500, 404), GOOD_NOT_OK)
check("el malo contesta algo que no es 404: ausencia no medible",
      classify_channel(200, 403), BAD_NOT_404)
check("404 al bueno y 200 al malo: discrimina AL REVES, no calibra",
      classify_channel(404, 200), GOOD_NOT_OK)

# --- la lectura de uniformidad que al pase 81 le falto aplicar -------------
defect, why = channel_defect_from_uniformity(["403"] * 81)
check("403 en 81 de 81 se lee como DEFECTO DE CANAL", defect, True)
check("y el motivo nombra la varianza cero", "varianza CERO" in why, True)

defect2, _ = channel_defect_from_uniformity(["200"] * 81)
check("200 en 81 de 81 NO es un negativo, asi que no es defecto", defect2, False)

defect3, why3 = channel_defect_from_uniformity(["403", "404", "200", "403", "200", "404"])
check("con varianza real NO se declara defecto de canal", defect3, False)
check("y el motivo nombra la varianza", "varianza" in why3, True)

defect4, why4 = channel_defect_from_uniformity(["403", "403"])
check("dos muestras no alcanzan para declarar defecto", defect4, False)
check("y lo dice por muestra insuficiente", "insuficiente" in why4, True)

# --- el veredicto de punta a punta -----------------------------------------
check("pase 81 de punta a punta: NO se puede afirmar nada del catalogo",
      verdict_for_sweep(["403"] * 81, 403, 403)[0], "NO-CLAIM")
check("un barrido con varianza por canal calibrado SI es afirmable",
      verdict_for_sweep(["200", "404", "200", "404", "200", "200"], 200, 404)[0],
      "CLAIMABLE")
check("canal calibrado pero barrido uniforme en 404: no se afirma",
      verdict_for_sweep(["404"] * 10, 200, 404)[0], "NO-CLAIM")

total = len(checks)
passed = sum(1 for c in checks if c)
print("\n%d/%d checks passed" % (passed, total))
sys.exit(0 if passed == total else 1)
