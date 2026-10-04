#!/usr/bin/env python3
"""
Instrumento de licencia con DOS controles que el barrido previo de esta base no tenia.

Pase 94 del 2026-10-04.

Control 1 (P279) — el payload se NOMBRA, no se adivina.
    `raw.githubusercontent.com` es sensible a MAYUSCULAS, tambien en la EXTENSION.
    Una lista fija de variantes siempre tiene un hueco: `openedx/XBlock` lleva
    `LICENSE.TXT` (extension en mayuscula) y es INVISIBLE a 10 variantes x 2 ramas.
    El manifiesto del paquete lo nombra: `license-files = ["LICENSE.TXT"]`.

Control 2 (P280) — el manifiesto tiene que DESCRIBIR al repo que lo aloja.
    El `composer.json` en la raiz de `alfredang/ai-mms` declara
    `license: ["OSL-3.0","AFL-3.0"]` — y `name: openmage/magento-lts`.
    Es el manifiesto de OTRO proyecto, sin modificar. Leer su `license` como la
    licencia de la fila publica una licencia FALSA. El discriminador es `name`.

Sin red: trabaja sobre payloads ya capturados (dict ruta -> texto). El barrido en
vivo vive en `sweep.sh`; este modulo es la LOGICA, para que la suite sea offline.
"""

import json
import re

# Variantes que el barrido del pase 94 probo en vivo: 11 nombres x 3 ramas.
# Se conserva la lista porque su HUECO es el hallazgo, no su cobertura.
VARIANTES_PROBADAS = [
    "LICENSE", "LICENSE.txt", "LICENSE.md", "LICENCE", "LICENCE.txt",
    "COPYING", "COPYING.txt", "LICENSE-APACHE", "LICENSE-MIT",
    "license", "license.txt",
]
RAMAS_PROBADAS = ["main", "master", "develop"]

# Marcadores que delatan que el arbol es DERIVADO de un upstream conocido.
MARCADORES_DERIVADO = {
    "app/Mage.php": "openmage/magento-lts",  # Magento-1 / OpenMage LTS
}


def nombre_declarado_en_manifiesto(texto, clase):
    """Devuelve el nombre que el manifiesto se da a si mismo, o None."""
    if clase in ("composer.json", "package.json"):
        try:
            return json.loads(texto).get("name")
        except Exception:
            return None
    if clase == "pyproject.toml":
        m = re.search(r'^\s*name\s*=\s*["\']([^"\']+)["\']', texto, re.M)
        return m.group(1) if m else None
    return None


def licencia_declarada_en_manifiesto(texto, clase):
    """Devuelve la licencia que el manifiesto declara, normalizada a lista."""
    if clase in ("composer.json", "package.json"):
        try:
            lic = json.loads(texto).get("license")
        except Exception:
            return None
        if lic is None:
            return None
        return lic if isinstance(lic, list) else [lic]
    if clase == "pyproject.toml":
        m = re.search(r'^\s*license\s*=\s*["\']([^"\']+)["\']', texto, re.M)
        return [m.group(1)] if m else None
    return None


def payloads_nombrados_por_manifiesto(texto, clase):
    """P279: los nombres de archivo de licencia que el manifiesto NOMBRA."""
    if clase == "pyproject.toml":
        m = re.search(r'^\s*license-files\s*=\s*\[([^\]]*)\]', texto, re.M)
        if m:
            return re.findall(r'["\']([^"\']+)["\']', m.group(1))
    if clase == "package.json":
        try:
            v = json.loads(texto).get("licenseFilename")
            return [v] if v else []
        except Exception:
            return []
    return []


def pertenece_al_repo(nombre_manifiesto, slug_repo):
    """
    P280: el manifiesto describe a ESTE repo?

    Compara por el segmento de PROYECTO, no por el owner: un repo puede renombrar
    el owner (fork) y seguir siendo el mismo paquete. Lo que delata un manifiesto
    AJENO es que el proyecto no coincida.
    """
    if not nombre_manifiesto:
        return None  # sin dato: no se afirma ni se niega
    proy_man = nombre_manifiesto.split("/")[-1].lower().replace("_", "-")
    proy_repo = slug_repo.split("/")[-1].lower().replace("_", "-")
    return proy_man == proy_repo


def clasificar(slug_repo, payloads, manifiestos, rutas_presentes=()):
    """
    Veredicto de licencia para un repo, con la PROCEDENCIA de cada afirmacion.

    payloads      : {nombre_archivo: texto} de archivos de licencia hallados (200).
    manifiestos   : {clase: texto} de manifiestos hallados en la raiz.
    rutas_presentes: rutas que respondieron 200 (para detectar derivacion).
    """
    out = {
        "repo": slug_repo,
        "veredicto": None,
        "licencia": None,
        "procedencia": None,
        "payload_nombrado": [],
        "manifiesto_ajeno": None,
        "derivado_de": None,
        "notas": [],
    }

    # P279: que payload NOMBRA el manifiesto (aunque la lista de variantes lo perdiera)
    for clase, texto in manifiestos.items():
        for n in payloads_nombrados_por_manifiesto(texto, clase):
            out["payload_nombrado"].append(n)
            if n not in VARIANTES_PROBADAS:
                out["notas"].append(
                    f"P279: `{n}` lo NOMBRA {clase} y NO esta en las "
                    f"{len(VARIANTES_PROBADAS)} variantes probadas"
                )

    # Derivacion: marcadores de un upstream conocido en el arbol
    for ruta, upstream in MARCADORES_DERIVADO.items():
        if ruta in rutas_presentes:
            out["derivado_de"] = upstream
            out["notas"].append(
                f"derivado: `{ruta}` presente -> arbol de `{upstream}`"
            )

    # 1) payload propio leido = la evidencia mas fuerte
    if payloads:
        nombre, texto = sorted(payloads.items())[0]
        out["veredicto"] = "LICENCIADO"
        out["procedencia"] = f"payload:{nombre}"
        if "Apache License" in texto:
            out["licencia"] = ["Apache-2.0"]
        elif "MIT License" in texto:
            out["licencia"] = ["MIT"]
        else:
            out["licencia"] = ["(payload leido, SPDX no inferido)"]
        return out

    # 2) sin payload: el manifiesto solo vale si DESCRIBE a este repo (P280)
    for clase, texto in manifiestos.items():
        lic = licencia_declarada_en_manifiesto(texto, clase)
        if not lic:
            continue
        nom = nombre_declarado_en_manifiesto(texto, clase)
        propio = pertenece_al_repo(nom, slug_repo)
        if propio is False:
            out["manifiesto_ajeno"] = nom
            out["veredicto"] = "SIN LICENCIA PROPIA"
            out["procedencia"] = f"manifiesto:{clase} DESCARTADO por P280"
            out["notas"].append(
                f"P280: {clase} declara {lic} pero se nombra `{nom}`, no `{slug_repo}`: "
                f"es manifiesto AJENO y su licencia NO es la de esta fila"
            )
            if out["derivado_de"]:
                out["notas"].append(
                    f"consecuencia: la fila no tiene cesion PROPIA y hereda el arbol "
                    f"de `{out['derivado_de']}` bajo {lic} — el riesgo SUBE, no baja"
                )
            return out
        out["veredicto"] = "LICENCIADO (solo manifiesto)"
        out["licencia"] = lic
        out["procedencia"] = f"manifiesto:{clase}"
        out["notas"].append("sin payload en el arbol: cesion declarada, no adjunta")
        return out

    # 3) nada
    out["veredicto"] = "AUSENCIA CONFIRMADA"
    out["procedencia"] = (
        f"{len(VARIANTES_PROBADAS)} variantes x {len(RAMAS_PROBADAS)} ramas "
        f"= {len(VARIANTES_PROBADAS) * len(RAMAS_PROBADAS)} sondas, mas 6 manifiestos"
    )
    return out
