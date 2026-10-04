#!/usr/bin/env python3
"""Suite de `manifest_license.py`. Reproduce: `python3 test_manifest_license.py`

Los DOS controles del pase 94 son casos obligatorios y tiran de payloads REALES capturados
(`fixtures/`, enlazados a los del p280 — no se re-copian):

- control POSITIVO  `openedx/XBlock`   -> el manifiesto NOMBRA `LICENSE.TXT` y es del repo.
- control NEGATIVO  `alfredang/ai-mms` -> el manifiesto es de `openmage/magento-lts`:
  su licencia NO es atribuible, y publicarla habria sido una licencia FALSA (P280).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from manifest_license import (read_manifest, ownership, OWN, WEAK, FOREIGN, NONAME)

HERE = os.path.dirname(os.path.abspath(__file__))
ok = fail = 0


def check(label, got, want):
    global ok, fail
    if got == want:
        ok += 1
    else:
        fail += 1
        print("  FAIL %-58s got=%r want=%r" % (label, got, want))


# Los payloads de los dos controles son los que CAPTURO el pase 94: se leen de su carpeta,
# no se re-copian aqui (una segunda copia es una segunda verdad que se desincroniza).
P280_FIXTURES = os.path.join(HERE, os.pardir, "p280-manifest-ownership", "fixtures")


def fixture(name):
    with open(os.path.join(P280_FIXTURES, name), encoding="utf-8", errors="replace") as fh:
        return fh.read()


# ---------------------------------------------------------------- control POSITIVO (P279)
x = read_manifest("pyproject.toml", fixture("xblock.pyproject.toml"), "openedx/XBlock")
check("xblock: manifiesto parseado", x is not None, True)
check("xblock: nombre declarado", x["name"], "XBlock")
check("xblock: licencia declarada", x["license"], "Apache-2.0")
check("xblock: NOMBRA el archivo", x["license_files"], ["LICENSE.TXT"])
check("xblock: la caja de la extension se conserva",
      x["license_files"][0].endswith(".TXT"), True)
check("xblock: propiedad", x["ownership"], OWN)
check("xblock: atribuible", x["attributable"], True)
# El hueco de P279 EN SU FORMA EXACTA: la variante que el barrido viejo probo no es la real.
check("xblock: 'LICENSE.txt' != 'LICENSE.TXT' (el hueco de P279)",
      "LICENSE.txt" in x["license_files"], False)

# ---------------------------------------------------------------- control NEGATIVO (P280)
a = read_manifest("composer.json", fixture("ai-mms.composer.json"), "alfredang/ai-mms")
check("ai-mms: manifiesto parseado", a is not None, True)
check("ai-mms: nombre declarado es de OTRO proyecto", a["name"], "openmage/magento-lts")
check("ai-mms: licencia declarada (lista composer)", a["license"], "OSL-3.0 OR AFL-3.0")
check("ai-mms: propiedad", a["ownership"], FOREIGN)
check("ai-mms: NO atribuible -> no se publica", a["attributable"], False)

# ---------------------------------------------------------------- eje de PROPIEDAD (P280)
check("prop: identico", ownership("openedx/XBlock", "XBlock"), OWN)
check("prop: caja distinta", ownership("openedx/XBlock", "xblock"), OWN)
check("prop: manifiesto con scope npm", ownership("r-huijts/canvas-mcp", "@r-huijts/canvas-mcp"), OWN)
check("prop: sufijo extra es contencion", ownership("loyaniu/moodle-mcp", "moodle-mcp-server"), OWN)
check("prop: ajeno", ownership("alfredang/ai-mms", "openmage/magento-lts"), FOREIGN)
check("prop: sin nombre", ownership("a/b", None), NONAME)
check("prop: nombre vacio", ownership("a/b", "   "), NONAME)
# Solapamiento SOLO por stopword no es prueba de propiedad: `*-mcp-server` esta por todas
# partes en esta base, y dos piezas distintas comparten ese token sin ser la misma.
check("prop: solapamiento solo por stopword -> FOREIGN",
      ownership("owentaylor/canvas-mcp", "powerschool-mcp"), FOREIGN)
check("prop: solapamiento significativo parcial -> WEAK",
      ownership("foo/canvas-grades-sync", "canvas-roster-tool"), WEAK)

# ---------------------------------------------------------------- formas de `license`
check("pyproject: license={file=...} NOMBRA archivo",
      read_manifest("pyproject.toml", '[project]\nname="p"\nlicense = {file = "COPYING"}\n', "x/p")["license_files"],
      ["COPYING"])
check("pyproject: license={text=...} es expresion",
      read_manifest("pyproject.toml", '[project]\nname="p"\nlicense = {text = "MIT"}\n', "x/p")["license"],
      "MIT")
check("pyproject: comentario no se lee como valor",
      read_manifest("pyproject.toml", '[project]\nname="p"\nlicense = "MIT"  # no AGPL\n', "x/p")["license"],
      "MIT")
check("cargo: license-file singular",
      read_manifest("Cargo.toml", '[package]\nname="p"\nlicense-file = "LICENSE-MIT"\n', "x/p")["license_files"],
      ["LICENSE-MIT"])
check("package.json: license objeto {type}",
      read_manifest("package.json", '{"name":"p","license":{"type":"MIT","url":"u"}}', "x/p")["license"],
      "MIT")
check("package.json: licenses[] legado",
      read_manifest("package.json", '{"name":"p","licenses":[{"type":"BSD-3-Clause"}]}', "x/p")["license"],
      "BSD-3-Clause")
check("package.json: JSON roto -> lectura laxa",
      read_manifest("package.json", '{"name":"p","license":"MIT",}', "x/p")["license"],
      "MIT")
check("setup.cfg: sin comillas y license_files",
      read_manifest("setup.cfg", "[metadata]\nname = p\nlicense = MIT\nlicense_files = LICENSE.rst\n", "x/p")["license_files"],
      ["LICENSE.rst"])
check("manifiesto sin ninguna de las tres claves -> None",
      read_manifest("package.json", '{"dependencies":{"x":"1"}}', "x/p"), None)
check("manifiesto desconocido -> None",
      read_manifest("go.mod", "module x\n", "x/p"), None)
check("payload vacio -> None", read_manifest("package.json", "", "x/p"), None)

# Un `license` que NOMBRA archivo no es una EXPRESION de licencia: no se puede publicar
# `COPYING` en la columna de licencia.  Las dos cosas van a campos distintos.
f = read_manifest("pyproject.toml", '[project]\nname="p"\nlicense = {file = "COPYING"}\n', "x/p")
check("archivo nombrado no contamina la expresion", f["license"], None)

print("%d/%d" % (ok, ok + fail))
sys.exit(1 if fail else 0)
