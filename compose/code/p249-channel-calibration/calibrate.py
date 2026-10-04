#!/usr/bin/env python3
"""P249 - la compuerta de CALIBRACION de un canal de verificacion.

El pase 81 pidio `curl -sI` contra `github.com` para las 81 URLs del catalogo,
recibio `403` en 81 de 81 y escribio que el canal marcaba MUERTO el 100 % del
catalogo. La varianza cero sobre 81 muestras no es el estado de 81 repos: es el
estado del canal (P247).

Lo que este modulo agrega es la compuerta que FALTABA: antes de creerle un
NEGATIVO a un canal, el canal se calibra contra una URL que se sabe buena Y una
que se sabe mala. Un canal que contesta lo mismo a las dos no discrimina, y de
un canal que no discrimina NO se puede leer un negativo -- ni uno ni ochenta y uno.

La funcion es PURA (toma codigos, no hace red) para que la suite sea
reproducible sin egreso.
"""

CALIBRATED = "CALIBRATED"
NO_DISCRIMINATION = "UNCALIBRATED-NO-DISCRIMINATION"
GOOD_NOT_OK = "UNCALIBRATED-GOOD-NOT-REACHABLE"
BAD_NOT_404 = "UNCALIBRATED-BAD-NOT-ABSENT"
NO_EGRESS = "UNCALIBRATED-NO-EGRESS"


def classify_channel(good_code, bad_code):
    """Veredicto de calibracion a partir de los dos codigos de control.

    `good_code`: respuesta a una URL que se SABE que existe.
    `bad_code`:  respuesta a una URL que se SABE que no existe.
    """
    good, bad = str(good_code), str(bad_code)
    if good == "000" and bad == "000":
        return NO_EGRESS
    if good == bad:
        # El caso del pase 81: 403 == 403. No discrimina.
        return NO_DISCRIMINATION
    if good != "200":
        return GOOD_NOT_OK
    if bad != "404":
        return BAD_NOT_404
    return CALIBRATED


def may_believe_negative(verdict):
    """Solo un canal CALIBRADO autoriza leer una ausencia como ausencia."""
    return verdict == CALIBRATED


def channel_defect_from_uniformity(codes, min_samples=5):
    """Un barrido entero con UN solo codigo distinto de 200 es defecto de canal.

    Devuelve (es_defecto, motivo). Esta es la lectura que al pase 81 le faltaba
    aplicar a su propio resultado antes de concluir sobre el catalogo.
    """
    codes = [str(c) for c in codes]
    if len(codes) < min_samples:
        return False, "muestra insuficiente (%d < %d)" % (len(codes), min_samples)
    distinct = set(codes)
    if len(distinct) > 1:
        return False, "hay varianza (%d codigos distintos)" % len(distinct)
    only = distinct.pop()
    if only == "200":
        return False, "uniforme en 200: no es un negativo"
    return True, "varianza CERO en %d muestras, todas %s" % (len(codes), only)


def verdict_for_sweep(codes, good_code, bad_code):
    """Lo que se puede AFIRMAR de un barrido, dada la calibracion del canal."""
    cal = classify_channel(good_code, bad_code)
    if not may_believe_negative(cal):
        return "NO-CLAIM", cal
    defect, _ = channel_defect_from_uniformity(codes)
    if defect:
        return "NO-CLAIM", "canal calibrado pero barrido uniforme: revisar"
    return "CLAIMABLE", cal
