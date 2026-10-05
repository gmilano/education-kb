#!/usr/bin/env python3
"""Suite de P317. OFFLINE: corre sobre los arboles congelados en `fixtures/`.

Los fixtures NO son inventados: son la enumeracion `git ls-tree -r` de los arboles reales,
medida en el pase 102 por el canal de P275 (clon sin blobs). Se congelan para que la suite
corra sin red y para que un pase futuro pueda ver si el arbol CAMBIO.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from corpus_axis import (  # noqa: E402
    corpus_files, redistributes_corpus, data_terms_in_text, verdict,
    pathguess_sees_corpus, CORPUS_MIN_FILES,
)

HERE = os.path.dirname(os.path.abspath(__file__))
_ok = 0
_fail = []


def check(label, got, want):
    global _ok
    if got == want:
        _ok += 1
        print("PASS  %s" % label)
    else:
        _fail.append(label)
        print("FAIL  %s -- got %r want %r" % (label, got, want))


def tree(name):
    with open(os.path.join(HERE, "fixtures", "tree-%s.txt" % name)) as fh:
        return fh.read().splitlines()


# ---------------------------------------------------------------------------------------
# C3 -- EL CONTROL NEGATIVO QUE MANDA (P319).
# El instrumento viejo (adivinar paths) tiene que FRACASAR sobre edu-convokit, y el nuevo
# (enumerar el arbol) tiene que verlo. Sin este par de aserciones, P319 es prosa.
# ---------------------------------------------------------------------------------------
ec = tree("edu-convokit")
check("C3 pathguess NO ve el corpus de edu-convokit (falso negativo)",
      pathguess_sees_corpus(ec), False)
check("C3 enumerar el arbol SI lo ve", redistributes_corpus(ec)[0], True)
check("C3 y el conteo es el reparto real, no un booleano",
      redistributes_corpus(ec)[1], 111)

# C8 -- el censo SIN COMPUERTA DE UBICACION infla, y la inflacion se mide aca. El primer
# censo de este pase contaba payload en TODO el arbol y dio 115: los 4 de mas son los
# prompts `edu_convokit/prompts/conversation/*.txt`, que son plantillas de codigo y no
# corpus. Un conteo de datos que no gatea por UBICACION cuenta el codigo como dato.
_ungated = [p for p in ec if p.lower().endswith(
    (".csv", ".tsv", ".xlsx", ".json", ".wav", ".zip", ".txt"))
    and p.rsplit("/", 1)[-1].lower() not in ("requirements.txt", "package.json")]
check("C8 el censo sin compuerta de ubicacion da 115", len(_ungated), 115)
check("C8 y la compuerta descuenta exactamente los 4 prompts",
      len(_ungated) - redistributes_corpus(ec)[1], 4)

# Los tres corpus vendored estan, por nombre: el hallazgo no es «hay datos», es CUALES.
_ecf = corpus_files(ec)
check("C3 vendorea talkmoves", sum(1 for p in _ecf if p.startswith("data/talkmoves/")), 29)
check("C3 vendorea ncte", sum(1 for p in _ecf if p.startswith("data/ncte/")), 29)
check("C3 vendorea amber", sum(1 for p in _ecf if p.startswith("data/amber/")), 45)
# La huella que ligo el corpus vendored al upstream: el nombre con ESPACIO antes de .xlsx.
check("C3 la huella de identidad del upstream viaja en el nombre",
      "data/talkmoves/Boats and Fish 4_Grade 4 .xlsx" in _ecf, True)

# ---------------------------------------------------------------------------------------
# C2 -- CONTROL POSITIVO. El positivo conocido de P315 tiene que reproducirse, y en los DOS
# ejes: declara CC BY-NC-SA 4.0 y NO redistribuye (es lo que el repo afirma de si mismo).
# Un instrumento que no reproduce un positivo conocido no sostiene ningun negativo.
# ---------------------------------------------------------------------------------------
cdi = tree("classroom-discourse-intelligence")
check("C2 CDI no redistribuye corpus", redistributes_corpus(cdi)[0], False)
check("C2 y su data/ tiene CERO payload (solo la tarjeta)", redistributes_corpus(cdi)[1], 0)
CDI_CARD = (
    "# Dataset Card - TalkMoves\n## License\n"
    "CC BY-NC-SA 4.0. **Non-commercial** and ShareAlike restrictions apply. "
    "This repository does not redistribute the source corpus.\n"
)
check("C2 la tarjeta declara la familia NC-SA",
      data_terms_in_text(CDI_CARD), ("CC-BY-NC-SA-4.0", False))
check("C2 veredicto de P315 reproducido",
      verdict(False, data_terms_in_text(CDI_CARD), "MIT"), "DATOS-DECLARADOS-DISTINTOS")

# ---------------------------------------------------------------------------------------
# C5 -- EL DEFECTO DE P308, QUE ESTE MODULO PODIA REINTRODUCIR.
# «for both commercial and non-commercial purposes» CONTIENE «non-commercial». Un detector
# por token lo llama NC e INVIERTE el veredicto sobre el texto mas permisivo del corpus.
# ---------------------------------------------------------------------------------------
SO_README = (
    "This corpus aims to provide a free public dataset for the pronunciation scoring task.\n"
    "* It is available for free download for both commercial and non-commercial purposes.\n"
)
check("C5 la concesion comercial explicita NO se lee como NC",
      data_terms_in_text(SO_README), ("DECLARADA-PERMISIVA-SIN-ARCHIVO", True))
check("C5 y el NC desnudo si se lee como NC",
      data_terms_in_text("Released for non-commercial research use only."),
      ("NONCOMMERCIAL-NOT-OSI", False))

# ---------------------------------------------------------------------------------------
# C4 -- UN FIXTURE DE PRUEBA NO ES UN CORPUS. kaldi tiene UN .wav, en `src/feat/test_data/`.
# Un eje que cuente payload en cualquier parte del arbol lo llama corpus redistribuido.
# ---------------------------------------------------------------------------------------
kaldi = tree("kaldi-payload-slice")
check("C4 el .wav de prueba unitaria de kaldi no es corpus",
      redistributes_corpus(kaldi), (False, 0))
check("C4 y el path existe en el fixture (la asercion no es vacua)",
      any("src/feat/test_data/test.wav" in p for p in kaldi), True)
check("C4 un data/ de PRIMER nivel con el mismo archivo SI contaria",
      redistributes_corpus(["data/x%d.wav" % i for i in range(CORPUS_MIN_FILES)])[0], True)
check("C4 y uno por debajo del umbral no",
      redistributes_corpus(["data/x%d.wav" % i for i in range(CORPUS_MIN_FILES - 1)])[0],
      False)

# ---------------------------------------------------------------------------------------
# C6 -- una tarjeta de dataset es DECLARACION (eje B), no corpus (eje A). Si `.md` contara
# como payload, CDI saldria «redistribuye» y contradiria lo que su propio README afirma.
# ---------------------------------------------------------------------------------------
check("C6 un data/README.md no es payload de corpus",
      corpus_files(["data/README.md", "LICENSE"]), [])

# ---------------------------------------------------------------------------------------
# C7 -- un badge no concede nada (P314). La URL de shields.io trae el nombre de la licencia.
# ---------------------------------------------------------------------------------------
BADGE = "[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](x)"
check("C7 un badge de shields.io no se lee como concesion de datos",
      data_terms_in_text(BADGE), None)

# ---------------------------------------------------------------------------------------
# C1 -- LOS DOS EJES SON ORTOGONALES, y el caso obligatorio es que DISIENTAN: el peor
# veredicto de esta carpeta sale de A=si, B=no, que es la celda que un barrido de licencias
# declaradas no puede alcanzar.
# ---------------------------------------------------------------------------------------
check("C1 A=si B=no -> el caso peor", verdict(True, None, "MIT"), "CORPUS-SIN-CESION")
check("C1 A=si B=si", verdict(True, ("X", True), "MIT"), "CORPUS-CON-TERMINOS")
check("C1 A=no B=si, misma familia", verdict(False, ("MIT", True), "MIT"),
      "DATOS-DECLARADOS-IGUALES")
check("C1 A=no B=no", verdict(False, None, "MIT"), "SIN-CORPUS")

# ---------------------------------------------------------------------------------------
# El reparto completo de la cohorte de 9, como aserto. Es el DENOMINADOR que el pase 101
# pre-registro: 9 repos, no «los que aparezcan».
# ---------------------------------------------------------------------------------------
COHORT = {
    "edu-convokit": True,
    "educoder": False,
    "classroom-discourse-intelligence": False,
    "classroom-attendance": False,
    "attention-monitor": False,
    "student-eye": False,
    "openpronounce": False,
    "kaldi-payload-slice": False,
    "speechocean762": True,
}
for name, want in sorted(COHORT.items()):
    check("cohorte: %s redistribuye=%s" % (name, want),
          redistributes_corpus(tree(name))[0], want)
check("cohorte: 2 de 9 redistribuyen corpus",
      sum(1 for n in COHORT if redistributes_corpus(tree(n))[0]), 2)

# speechocean762 ES el corpus: su arbol es WAVE/ + train/ + test/ y no trae archivo de
# licencia en ninguna parte. La ausencia se sostiene porque el arbol esta ENUMERADO.
so = tree("speechocean762")
check("speechocean762: el arbol enumerado no tiene archivo de licencia",
      [p for p in so if os.path.basename(p).lower().startswith(("licen", "copying"))], [])
check("speechocean762: y el payload es el corpus entero",
      redistributes_corpus(so)[1], 5245)

print("\n%d/%d" % (_ok, _ok + len(_fail)))
if _fail:
    print("FALLAN: %s" % ", ".join(_fail))
    sys.exit(1)
