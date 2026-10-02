#!/usr/bin/env python3
"""Control OFFLINE del ancla de licencia dentro del tarball. Sin red.

Por que existe (pase 52). El pase 51 declaro OBLIGATORIA el ancla
'^package/(LICEN[CS]E|COPYING)[^/]*$' para no contar las licencias de
node_modules (tendencia 259, 144 archivos ajenos en tutors-publish-npm).
El ancla cumple eso y tiene un defecto propio: es CASE-SENSITIVE, y
@learninglocker/xapi-agents envia su licencia en 'package/license'
(minuscula, sin extension) con 35.121 bytes de GPL-3.0 adentro.

El ancla corregida tiene que cumplir DOS cosas a la vez:
  1. encontrar la licencia escrita con cualquier capitalizacion;
  2. seguir rechazando todo lo que no este en la RAIZ de package/,
     que es la unica razon por la que el ancla existe.

    python3 test_anchor.py
"""
import re
import sys

OLD = re.compile(r'^package/(LICEN[CS]E|COPYING)[^/]*$')
NEW = re.compile(r'^package/(licen[cs]e|copying)([._-][A-Za-z0-9]+)?$', re.I)

# (ruta, se_espera_que_cuente, por_que)
CASES = [
    ("package/LICENSE",                      True,  "el caso corriente"),
    ("package/LICENSE.md",                   True,  "con extension"),
    ("package/LICENSE.txt",                  True,  "con extension"),
    ("package/COPYING",                      True,  "convencion GNU"),
    ("package/COPYING.txt",                  True,  "convencion GNU/Moodle (tendencia 252)"),
    ("package/LICENCE",                      True,  "grafia britanica (tendencia 256)"),
    ("package/LICENSE-MIT",                  True,  "doble licencia estilo Rust (tendencia 252)"),
    ("package/LICENSE-APACHE",               True,  "idem"),
    # El hallazgo del pase 52:
    ("package/license",                      True,  "MINUSCULA: @learninglocker/xapi-agents, GPL-3.0"),
    ("package/license.md",                   True,  "minuscula con extension"),
    ("package/License",                      True,  "capitalizacion mixta"),
    # Lo que el ancla NO debe admitir, que es su unica razon de ser:
    ("package/node_modules/@iktakahiro/markdown-it-katex/LICENSE", False,
                                                    "tendencia 259: licencia AJENA"),
    ("package/node_modules/foo/license",     False,  "idem, en minuscula"),
    ("package/dist/LICENSE",                 False,  "no esta en la raiz del paquete"),
    ("package/src/license_check.js",         False,  "codigo, no licencia"),
    ("package/licenses.json",                False,  "inventario, no texto de licencia"),
    ("package/LICENSES",                     False,  "plural: directorio/inventario, no el texto"),
    ("package/README.md",                    False,  "no es licencia"),
    ("package/package.json",                 False,  "no es licencia"),
    ("LICENSE",                              False,  "fuera de package/"),
]

def main():
    fails = 0
    print("== el ancla corregida cumple las dos condiciones ==")
    for path, want, why in CASES:
        got = bool(NEW.match(path))
        ok = got == want
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'} {'cuenta  ' if want else 'rechaza '} {path:62s} {why}")

    print("\n== el defecto que este pase encontro, demostrado ==")
    regressions = [p for p, want, _ in CASES
                   if want and not OLD.match(p) and NEW.match(p)]
    for p in regressions:
        print(f"PASS el ancla del pase 51 PERDIA  {p}")
    if not regressions:
        print("FAIL no se reprodujo el defecto; el test no prueba nada")
        fails += 1

    print("\n== control positivo de la tendencia 259, con el ancla nueva ==")
    # El tarball real de tutors-publish-npm 4.1.3: 144 coincidencias recursivas
    # y CERO en la raiz. El ancla nueva tiene que seguir dando cero.
    trap = [f"package/node_modules/pkg{i}/LICENSE" for i in range(72)] + \
           [f"package/node_modules/pkg{i}/license" for i in range(72)]
    hits = [p for p in trap if NEW.match(p)]
    ok = len(hits) == 0
    fails += not ok
    print(f"{'PASS' if ok else 'FAIL'} 144 licencias de node_modules -> raiz={len(hits)} (debe ser 0)")

    total = len(CASES) + len(regressions) + 1
    print(f"\n{total - fails}/{total} controles pasados")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
