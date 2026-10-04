#!/usr/bin/env python3
"""Regression tests for the two defects this instrument shipped with and then fixed.

D1 -- CASE.  raw.githubusercontent.com is case-sensitive.  The first build probed only
     uppercase names (plus LICENCE) and returned NO-CESSION for frappe/education and
     frappe/erpnext, both of which carry `license.txt` in LOWERCASE.  Two false absences.

D2 -- FAMILY FROM THE BODY.  The first build classified the family with an AGPL-first grep
     over the whole text.  GPL-3.0 section 13 is headed "Use with the GNU Affero General
     Public License", so EVERY GPL-3.0 text matched AGPL first.  It misread GibbonEdu/core
     (GPL-3.0) as AGPL-3.0 and would have published a correction to pass 70 that was itself
     wrong.  This is P171 restated: classify on the DECLARATION, never on a body grep.

Run: python3 test_family.py
"""
import subprocess, sys, pathlib

HERE = pathlib.Path(__file__).parent
SWEEP = HERE / "sweep_erp.sh"

GPL3_HEAD = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
"""
# The clause that broke the first build.  It lives in the BODY of every GPL-3.0 text.
GPL3_S13 = """
  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.
"""
AGPL3_HEAD = """                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
"""

LIB = HERE.parent / "lib" / "license_family.sh"

def family_of(text: str) -> str:
    """Call the shell function under test, so the test exercises the shipped code.

    P312 (pase 101).  Este arnes EXTRAIA el cuerpo de `family_of` del propio `sweep_erp.sh`
    con `sed -n "/^family_of() {/,/^}/p"`, o sea que estaba acoplado al TEXTO de la copia y
    no a su COMPORTAMIENTO.  Cuando el pase 101 cerro P237 y rewireo la copia a
    `lib/license_family.sh`, el `sed` dejo de encontrar la funcion y las tres aserciones de
    D2 --las que guardan P171, el par GPL/AGPL-- devolvieron cadena VACIA y fallaron.

    El defecto no es del rewiring: es que un control escrito contra el LAYOUT de un archivo
    se rompe con la consolidacion que P237 pide, justo cuando mas hace falta que siga
    midiendo.  Ahora apunta a la libreria, que es donde vive el comportamiento, y por eso
    el control sobrevive al proximo movimiento de codigo.  Las fixtures no se tocaron.
    """
    out = subprocess.run(["bash", "-c",
        f'. "{LIB}"; family_of "$1"', "_", text], capture_output=True, text=True)
    return out.stdout.strip()

def check(name, got, want):
    ok = got == want
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got!r}, want {want!r}")
    return ok

def main():
    results = []
    # D2: a full GPL-3.0 text -- title GPL, body mentioning AGPL -- must classify GPL-3.0.
    results.append(check("D2 GPL-3.0 with sec.13 AGPL clause",
                         family_of(GPL3_HEAD + GPL3_S13), "GPL-3.0"))
    # D2 control: a real AGPL-3.0 text must still classify AGPL-3.0, or the fix overshot.
    results.append(check("D2 control: real AGPL-3.0",
                         family_of(AGPL3_HEAD), "AGPL-3.0"))
    # D2 ordering: AGPL must win only from the TITLE, never from a trailing mention.
    results.append(check("D2 GPL-3.0 body-only AGPL mention never wins",
                         family_of(GPL3_HEAD + GPL3_S13 * 3), "GPL-3.0"))
    # D1: the case matrix must contain the lowercase form that the first build missed.
    names = (HERE / "names.case-matrix.txt").read_text().split()
    results.append(check("D1 case matrix includes lowercase license.txt",
                         "license.txt" in names, True))
    results.append(check("D1 case matrix still includes uppercase LICENSE",
                         "LICENSE" in names, True))
    print()
    print(f"{sum(results)}/{len(results)} passed")
    return 0 if all(results) else 1

if __name__ == "__main__":
    sys.exit(main())
