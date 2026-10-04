#!/usr/bin/env python3
"""Suite OFFLINE de p289.  Imprime su total (README, regla de P126 punto 3)."""
import os
import subprocess
import sys

from maven_license import declared_license_names

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, 'fixtures')
LIB = os.path.join(HERE, '..', 'lib', 'license_family.sh')

n = bad = 0


def check(name, expected, got):
    global n, bad
    n += 1
    if expected == got:
        print('ok   %-62s %s' % (name, got))
    else:
        print('FAIL %-62s esperado=%r obtenido=%r' % (name, expected, got))
        bad += 1


def read(fn):
    with open(os.path.join(FIX, fn), encoding='utf-8') as fh:
        return fh.read()


def family_via_shared_control(name):
    """P237: la familia la decide el control COMPARTIDO, no este instrumento."""
    out = subprocess.run(
        ['sh', '-c', '. "$1"; osi_family_of "$2"', 'x', LIB, name],
        capture_output=True, text=True)
    return out.stdout.strip()


# --- 1. el caso que motiva el instrumento: kuali/kc declara la AGPL en el pom
kc = declared_license_names(read('kc-licenses.pom.xml'))
check('kc: un solo nombre declarado', 1, len(kc))
check('kc: el nombre declarado', 'GNU Affero General Public License, Version 3',
      kc[0] if kc else None)
check('kc: familia via el control compartido (P237)', 'AGPL-3.0 (declaracion)',
      family_via_shared_control(kc[0]) if kc else None)

# --- 2. CONTROL NEGATIVO (P171 en XML): el pom de kc nombra la AGPL en un COMENTARIO.
#        Un lector por grep dice AGPL-3.0; el lector de XML debe decir NADA.
comment_only = read('comment-only.pom.xml')
check('control negativo: el comentario SI nombra la AGPL', True,
      'Affero' in comment_only)
check('control negativo: pero NO hay <licenses>, asi que no hay declaracion', [],
      declared_license_names(comment_only))

# --- 3. un pom REAL sin <licenses>: kuali/rice.  Su licencia es ECL-2.0 y vive en
#        LICENSE.txt, no en el pom -- la ausencia en el manifiesto no es ausencia de licencia.
check('rice: pom real sin <licenses> -> sin declaracion', [],
      declared_license_names(read('rice-nolicenses.pom.xml')))

# --- 4. no se confunde un <licenses> anidado (perfil/plugin) con el del proyecto
nested = '''<?xml version="1.0"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <artifactId>x</artifactId>
  <profiles><profile><licenses><license>
    <name>Do What The Fuck You Want To Public License</name>
  </license></licenses></profile></profiles>
</project>'''
check('un <licenses> anidado en un perfil NO es la licencia del proyecto', [],
      declared_license_names(nested))

# --- 5. varias licencias declaradas (pom dual-licenciado) se devuelven TODAS
dual = '''<?xml version="1.0"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"><licenses>
  <license><name>Apache License, Version 2.0</name></license>
  <license><name>GNU General Public License, Version 2</name></license>
</licenses></project>'''
check('pom dual: devuelve las dos', 2, len(declared_license_names(dual)))

# --- 6. entradas degeneradas: no revienta y no inventa
check('pom ilegible -> sin declaracion', [], declared_license_names('no soy xml <'))
check('raiz que no es <project> -> sin declaracion', [],
      declared_license_names('<settings><licenses><license><name>MIT</name>'
                             '</license></licenses></settings>'))
check('<name> vacio no cuenta', [], declared_license_names(
    '<project xmlns="http://maven.apache.org/POM/4.0.0"><licenses><license>'
    '<name>   </name></license></licenses></project>'))

print('\n%d/%d checks passed' % (n - bad, n))
sys.exit(1 if bad else 0)
