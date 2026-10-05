#!/usr/bin/env python3
"""P317 -- el eje de CORPUS, que no es el eje de LICENCIA DE DATOS.

El pase 101 dejo pre-registrada esta afirmacion: «la licencia por CAPA es la norma en la
capa de observacion de aula». La prediccion contaba «piezas con licencia de datos DISTINTA
de la del codigo» sobre un denominador de 9 repos.

Medirla destapo que la pregunta estaba mal planteada, y este modulo es la pregunta corregida.
Comparar «licencia de datos declarada» contra «licencia de codigo» sólo puede ver los repos
que DECLARAN algo. El caso peor para un entregable no declara nada: es el repo que
REDISTRIBUYE un corpus ajeno y no le pone cesion, de modo que el unico archivo de licencia
del arbol --el del codigo-- queda cubriendo material que no es del titular.

Son DOS ejes ortogonales, y el defecto de la prediccion fue colapsarlos en uno:

    eje A  -- ¿el repo REDISTRIBUYE corpus?   (se mide ENUMERANDO el arbol, P275)
    eje B  -- ¿el repo DECLARA terminos de datos?  (se mide leyendo payload, P314)

    A=si B=no  -> CORPUS-SIN-CESION      el caso peor, y el que un barrido de licencias no ve
    A=si B=si  -> CORPUS-CON-TERMINOS
    A=no B=si  -> DATOS-DECLARADOS       aca vive el positivo de P315
    A=no B=no  -> SIN-CORPUS

P319: la ausencia de `data/README.md` NO es ausencia de datos. `rosewang2008/edu-convokit`
da 404 en `data/README.md` y redistribuye 115 archivos de corpus bajo `data/`. Un barrido de
paths adivinados lo publica como «sin datos»: un falso negativo que esconde el caso peor.
Ver el control negativo C3 en `test_corpus_axis.py`.
"""

# Nombres de directorio de PRIMER NIVEL que significan «acá vive un corpus». Cerrada a
# proposito: `src/feat/test_data/` de kaldi tiene un .wav y es un fixture de prueba
# unitaria, no un corpus redistribuido. Un eje que cuente payload en cualquier parte del
# arbol llama corpus a todo fixture, y entonces el eje no discrimina nada.
DATA_DIR_NAMES = frozenset({
    "data", "dataset", "datasets", "corpus", "corpora",
    "wave", "waves", "audio", "train", "test", "dev", "eval",
    "transcripts", "annotations",
})

# Extensiones de PAYLOAD de corpus. `.md` no esta: una tarjeta de dataset es una
# DECLARACION (eje B), no corpus (eje A). Es justo la distincion que hace que
# `classroom_discourse_intelligence` --cuyo `data/` tiene UN archivo, su README-- salga
# correctamente como «no redistribuye», que es lo que ese repo afirma de si mismo.
PAYLOAD_EXT = frozenset({
    ".csv", ".tsv", ".xlsx", ".xls", ".json", ".jsonl",
    ".wav", ".mp3", ".flac", ".parquet", ".arff", ".zip", ".txt",
})

# Manifiestos y configuracion que viven con extension de payload y no son corpus.
NOT_CORPUS_BASENAMES = frozenset({
    "package.json", "package-lock.json", "tsconfig.json", "composer.json",
    "composer.lock", "jsconfig.json", "requirements.txt", "pyproject.toml",
    "setup.json", "angular.json", "manifest.json", "tsconfig.node.json",
})

# Umbral declarado. Un corpus redistribuido es un reparto de archivos, no un archivo
# suelto; y el umbral se publica con el conteo de cada repo al lado para que el lector
# re-derive el veredicto en vez de creerlo.
CORPUS_MIN_FILES = 20


def _ext(path):
    i = path.rfind(".")
    return path[i:].lower() if i > 0 else ""


def corpus_files(tree):
    """Los archivos de payload de corpus bajo un directorio de datos de PRIMER NIVEL.

    `tree` es la enumeracion completa del arbol (una ruta por linea), tal como la da
    `git ls-tree --name-only -r HEAD` sobre un clon sin blobs (P275).
    """
    out = []
    for raw in tree:
        path = raw.strip()
        if not path or "/" not in path:
            continue
        top = path.split("/", 1)[0].lower()
        if top not in DATA_DIR_NAMES:
            continue
        base = path.rsplit("/", 1)[-1].lower()
        if base in NOT_CORPUS_BASENAMES:
            continue
        if _ext(path) in PAYLOAD_EXT:
            out.append(path)
    return out


def redistributes_corpus(tree, threshold=CORPUS_MIN_FILES):
    """Eje A. Devuelve (bool, conteo)."""
    n = len(corpus_files(tree))
    return (n >= threshold, n)


# --- eje B: ¿declara terminos de DATOS? -------------------------------------------------
# Se lee del PAYLOAD, nunca de un badge: P314 registro que el canal secundario del pase 101
# leyo una licencia del BADGE de shields.io, y un badge es una imagen con texto adentro que
# no concede nada.

_NC_MARKERS = ("noncommercial", "non-commercial", "by-nc")
_COMMERCIAL_OK_MARKERS = (
    "for both commercial and non-commercial",
    "commercial and non-commercial purposes",
)


def data_terms_in_text(text):
    """La familia de licencia de DATOS que un texto declara, o None.

    Devuelve una tupla (familia, comercial_ok) o None si el texto no declara terminos.
    """
    if not text:
        return None
    low = text.lower()

    # Orden: la concesion EXPLICITA de uso comercial se evalua ANTES de los marcadores NC,
    # porque la frase con la que speechocean762 concede --«for both commercial and
    # non-commercial purposes»-- CONTIENE la subcadena «non-commercial». Es exactamente el
    # defecto que P308 pago sobre el Unlicense: el texto mas permisivo clasificado como
    # NONCOMMERCIAL por token-matching. El orden aca es el arreglo, no una preferencia.
    for marker in _COMMERCIAL_OK_MARKERS:
        if marker in low:
            return ("DECLARADA-PERMISIVA-SIN-ARCHIVO", True)

    if "creative commons" in low or "cc by" in low or "cc-by" in low:
        nc = any(m in low for m in _NC_MARKERS)
        sa = "sharealike" in low or "share-alike" in low or "-sa" in low
        fam = "CC-BY" + ("-NC" if nc else "") + ("-SA" if sa else "") + "-4.0"
        return (fam, not nc)

    if any(m in low for m in _NC_MARKERS):
        return ("NONCOMMERCIAL-NOT-OSI", False)

    return None


def verdict(ships_corpus, data_terms, code_family):
    """La matriz 2x2 de los dos ejes. `data_terms` es la salida de data_terms_in_text."""
    declares = data_terms is not None
    if ships_corpus and not declares:
        return "CORPUS-SIN-CESION"
    if ships_corpus and declares:
        return "CORPUS-CON-TERMINOS"
    if not ships_corpus and declares:
        fam = data_terms[0]
        # «distinta de la del codigo» es la UNIDAD que el pase 101 pre-registro.
        if code_family and fam != code_family:
            return "DATOS-DECLARADOS-DISTINTOS"
        return "DATOS-DECLARADOS-IGUALES"
    return "SIN-CORPUS"


# --- el control negativo C3, como codigo y no como prosa --------------------------------

GUESSED_DATA_PATHS = (
    "data/README.md", "data/LICENSE", "datasets/README.md", "datasets/LICENSE",
    "corpus/README.md", "corpus/LICENSE", "DATA_LICENSE", "LICENSE-DATA",
)


def pathguess_sees_corpus(tree):
    """El instrumento VIEJO: adivinar paths en vez de enumerar el arbol.

    Existe para que su fracaso sea un ASERTO. Sobre `edu-convokit` devuelve False
    teniendo el repo 115 archivos de corpus: ese False es P319.
    """
    present = {p.strip() for p in tree}
    return any(g in present for g in GUESSED_DATA_PATHS)
