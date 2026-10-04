#!/usr/bin/env python3
"""
Suite del pase 94. Offline: corre sobre los payloads capturados en `fixtures/`.

    python3 test_license_probe.py

Las dos aserciones que mandan:
  - `openedx/XBlock` queda LICENCIADO y su payload lo NOMBRA el manifiesto (P279).
  - `alfredang/ai-mms` NO toma la licencia de su `composer.json`, porque ese
    manifiesto se nombra `openmage/magento-lts` (P280).
"""

import json
import os
import sys

from license_probe import (
    RAMAS_PROBADAS,
    VARIANTES_PROBADAS,
    clasificar,
    licencia_declarada_en_manifiesto,
    nombre_declarado_en_manifiesto,
    payloads_nombrados_por_manifiesto,
    pertenece_al_repo,
)

AQUI = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(AQUI, "fixtures")

ok = 0
fallos = []


def check(cond, etiqueta):
    global ok
    if cond:
        ok += 1
        print(f"  ok   {etiqueta}")
    else:
        fallos.append(etiqueta)
        print(f"  FALLA {etiqueta}")


def leer(nombre):
    with open(os.path.join(FIX, nombre), encoding="utf-8") as fh:
        return fh.read()


print("== fixtures presentes ==")
for n in (
    "ai-mms.composer.json",
    "xblock.pyproject.toml",
    "xblock.LICENSE.TXT.head",
    "ai-mms.README.head",
):
    check(os.path.exists(os.path.join(FIX, n)), f"fixture {n}")

composer_aimms = leer("ai-mms.composer.json")
pyproj_xblock = leer("xblock.pyproject.toml")
licencia_xblock = leer("xblock.LICENSE.TXT.head")
readme_aimms = leer("ai-mms.README.head")

print("\n== P279: el payload se NOMBRA, no se adivina ==")
nombrados = payloads_nombrados_por_manifiesto(pyproj_xblock, "pyproject.toml")
check(nombrados == ["LICENSE.TXT"], "pyproject de XBlock nombra exactamente LICENSE.TXT")
check("LICENSE.TXT" not in VARIANTES_PROBADAS, "LICENSE.TXT NO estaba en las variantes")
check("LICENSE.txt" in VARIANTES_PROBADAS, "la variante probada era LICENSE.txt (minuscula)")
check(
    "LICENSE.TXT".lower() == "LICENSE.txt".lower(),
    "las dos solo difieren en caja: el canal es sensible a MAYUSCULAS",
)
check(len(VARIANTES_PROBADAS) == 11, "la lista fija tenia 11 variantes")
check(len(RAMAS_PROBADAS) == 3, "y 3 ramas")
check(
    licencia_declarada_en_manifiesto(pyproj_xblock, "pyproject.toml") == ["Apache-2.0"],
    "pyproject de XBlock declara Apache-2.0",
)
check("Apache License" in licencia_xblock, "el payload LICENSE.TXT abre con 'Apache License'")

print("\n== P280: el manifiesto tiene que DESCRIBIR al repo ==")
nom = nombre_declarado_en_manifiesto(composer_aimms, "composer.json")
check(nom == "openmage/magento-lts", "composer.json de ai-mms se nombra openmage/magento-lts")
check(
    licencia_declarada_en_manifiesto(composer_aimms, "composer.json") == ["OSL-3.0", "AFL-3.0"],
    "y declara OSL-3.0 + AFL-3.0",
)
check(
    pertenece_al_repo(nom, "alfredang/ai-mms") is False,
    "el discriminador `name` lo declara AJENO a alfredang/ai-mms",
)
check(
    pertenece_al_repo("openmage/magento-lts", "openmage/magento-lts") is True,
    "y PROPIO en su repo de origen",
)
check(pertenece_al_repo(None, "x/y") is None, "sin dato no se afirma ni se niega")
check(
    pertenece_al_repo("fork-owner/XBlock", "openedx/XBlock") is True,
    "compara por PROYECTO, no por owner: un fork sigue siendo el mismo paquete",
)
check(
    "Tertiary Courses LMS" in readme_aimms and "OpenMage" in readme_aimms,
    "el README de ai-mms se declara LMS sobre OpenMage LTS",
)

print("\n== veredictos de punta a punta ==")
v_xblock = clasificar(
    "openedx/XBlock",
    payloads={"LICENSE.TXT": licencia_xblock},
    manifiestos={"pyproject.toml": pyproj_xblock},
)
check(v_xblock["veredicto"] == "LICENCIADO", "XBlock: LICENCIADO")
check(v_xblock["licencia"] == ["Apache-2.0"], "XBlock: Apache-2.0 leido del PAYLOAD")
check(v_xblock["procedencia"] == "payload:LICENSE.TXT", "XBlock: procedencia = payload")
check(
    any("P279" in n for n in v_xblock["notas"]),
    "XBlock: la nota P279 queda registrada",
)

v_aimms = clasificar(
    "alfredang/ai-mms",
    payloads={},
    manifiestos={"composer.json": composer_aimms},
    rutas_presentes=("app/Mage.php", "index.php", "composer.lock"),
)
check(v_aimms["veredicto"] == "SIN LICENCIA PROPIA", "ai-mms: SIN LICENCIA PROPIA")
check(v_aimms["licencia"] is None, "ai-mms: NO se le adjudica licencia")
check(
    v_aimms["manifiesto_ajeno"] == "openmage/magento-lts",
    "ai-mms: el manifiesto ajeno queda nombrado",
)
check(v_aimms["derivado_de"] == "openmage/magento-lts", "ai-mms: derivacion detectada por app/Mage.php")
check(
    any("el riesgo SUBE" in n for n in v_aimms["notas"]),
    "ai-mms: la consecuencia se declara (el riesgo SUBE, no baja)",
)
check(
    any("P280" in n for n in v_aimms["notas"]),
    "ai-mms: la nota P280 queda registrada",
)

v_vacio = clasificar("alguien/nada", payloads={}, manifiestos={})
check(v_vacio["veredicto"] == "AUSENCIA CONFIRMADA", "sin nada: AUSENCIA CONFIRMADA")
check("33 sondas" in v_vacio["procedencia"], "y la procedencia publica el tamano del barrido")

print("\n== ledger medido en vivo el 2026-10-04 ==")
ledger = os.path.join(AQUI, "relicense.2026-10-04.tsv")
check(os.path.exists(ledger), "el ledger existe")
if os.path.exists(ledger):
    filas = [
        l.rstrip("\n").split("\t")
        for l in open(ledger, encoding="utf-8")
        if l.strip() and not l.startswith("#") and not l.startswith("repo\t")
    ]
    check(len(filas) == 8, "8 filas re-medidas (las 8 que esta base marca SIN LICENCIA)")
    check(
        all(f[3] == "ALCANZADO" for f in filas),
        "8/8 con testigo alcanzado: la ausencia es medida, no falta de alcance",
    )
    check(
        sum(1 for f in filas if f[4] == "AUSENCIA-CONFIRMADA") == 8,
        "8/8 AUSENCIA CONFIRMADA: los veredictos de esta base se sostienen",
    )
    check(
        sum(1 for f in filas if f[5] != "-") == 1,
        "exactamente 1 de las 8 devolvio licencia de manifiesto",
    )
    check(
        [f[0] for f in filas if f[5] != "-"] == ["alfredang/ai-mms"],
        "y es alfredang/ai-mms",
    )

print(f"\n=== {ok}/{ok + len(fallos)} aserciones ===")
if fallos:
    for f in fallos:
        print(f"  - {f}")
    sys.exit(1)
print("verde")
