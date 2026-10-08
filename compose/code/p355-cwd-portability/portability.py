#!/usr/bin/env python3
"""`P355` — una suite que lee por ruta RELATIVA mide menos desde otro `cwd`, y lo ANUNCIA;
la que lee un default EFIMERO mide menos y NO lo anuncia. La accion A pre-registrada por el
pase 111 sumo las dos clases en una prediccion, y las dos se comportan al revés.

La accion pedia barrer los directorios de `compose/code/` buscando rutas absolutas
efimeras (`/tmp/`, `$TMPDIR`, `/var/tmp`) y correr **cada** suite desde un `cwd` distinto
del suyo, y predijo **>=3** suites mas que fallan o se saltan por una de las dos causas.

Sale CONFIRMADA en la letra (**4**), y el reparto es lo que importa:

  por ruta EFIMERA   0 suites nuevas   -> `P352` es un espécimen, no una clase
  por `cwd` ASUMIDO  4 suites          -> la clase real, y ninguna es de `/tmp`

🔴 **Y la severidad va al revés de la cantidad.** Las 4 del `cwd` asumido FALLAN
RUIDOSAMENTE (codigo 1, traceback o total degradado). La unica de ruta efimera -`p345`,
el espécimen de `P352`- pasaba en VERDE publicando «21/21» mientras no medía nada. La clase
de 4 miembros se delata; la de 1 miembro mentia.

Uso:  python3 portability.py [raiz-del-kb]
"""
import os, re, subprocess, sys

EFIMERA = re.compile(r'/tmp/|\$TMPDIR|\bTMPDIR\b|/var/tmp')

# `P615` (pase 50 del 2026-10-08). El vocabulario de arriba son rutas EFIMERAS, y se deja
# INTACTO para que `resultado.2026-10-05.tsv` siga siendo reproducible. Lo que no cubria es
# una ruta ABSOLUTA A LA RAIZ DEL REPO (`. /home/<user>/<algo>-kb/...`): la misma clase
# --una suite que solo corre en la maquina que la escribio-- con una forma de fallo PEOR,
# porque no crashea ni calla: ACUSA a su dependencia. `P614` es el especimen, en
# `p550/test_sweep.sh:144`, y sobrevivio 112 pases de este barrido por vocabulario.
ABSOLUTA = re.compile(r'^\s*(?:\.|source)\s+/(?:home|Users|root)/'
                      r'|^[^#]*\b(?:\.|source)\s+/(?:home|Users|root)/[^/\s]+/[^/\s]*-kb/')

# Una linea COMENTADA no es una invocacion. Sin esta guarda el barrido marca el comentario
# que DOCUMENTA el defecto --el de `p550` cita la ruta vieja textualmente-- y un detector que
# castiga el acto de corregir se apaga en una semana (la leccion de `P598` v1).
def _es_comentario(l):
    return l.lstrip().startswith('#')


def suites(root):
    """Las suites del arbol: `test_*.py` y `test*.sh` bajo `compose/code/`."""
    out = []
    base = os.path.join(root, 'compose', 'code')
    for dp, _dn, fn in os.walk(base):
        for f in sorted(fn):
            if (f.startswith('test_') and f.endswith('.py')) or \
               (f.startswith('test') and f.endswith('.sh')):
                out.append(os.path.relpath(os.path.join(dp, f), root).replace(os.sep, '/'))
    return sorted(set(out))


def ephemeral_refs(root, rel):
    """Lineas de la suite que nombran una ruta efimera. La clase de `P352`."""
    with open(os.path.join(root, rel), encoding='utf-8', errors='replace') as fh:
        return [(i, l.rstrip('\n')) for i, l in enumerate(fh, 1)
                if EFIMERA.search(l) or (ABSOLUTA.search(l) and not _es_comentario(l))]


def run(root, rel, cwd, timeout=300):
    """Corre una suite y devuelve (codigo, salida). `cwd` decide la pregunta del pase."""
    d, f = os.path.split(rel)
    runner = 'python3' if f.endswith('.py') else 'sh'
    target = f if cwd == os.path.join(root, d) else os.path.join(root, rel)
    try:
        p = subprocess.run([runner, target], cwd=cwd, capture_output=True,
                           text=True, timeout=timeout)
        return p.returncode, (p.stdout or '') + (p.stderr or '')
    except subprocess.TimeoutExpired:
        return 124, '(timeout)'


def shape(out):
    """Como SE VE el fallo. La distincion que la accion A no pre-registro.

    CRASH            traceback, sin total: imposible de confundir con una medicion.
    TOTAL-DEGRADADO  publica un `N/M` bien formado y MENOR: se parece a una medicion.
    SILENCIOSO       codigo 0, ni total ni traceback.
    """
    if 'Traceback (most recent call last)' in out:
        return 'CRASH'
    if re.search(r'\b\d+\s*/\s*\d+\b', out) or re.search(r'Ran \d+ test', out):
        return 'TOTAL-DEGRADADO'
    return 'SILENCIOSO'


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else
                           os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        '..', '..', '..'))
    foreign = os.path.dirname(root)   # un `cwd` ajeno que SIEMPRE existe
    ss = suites(root)
    print('# raiz=%s  suites=%d  cwd-ajeno=%s' % (root, len(ss), foreign))
    print('suite\texit_propio\texit_ajeno\tforma_ajeno\trefs_efimeras')
    rotas, efim = [], []
    for rel in ss:
        d = os.path.join(root, os.path.dirname(rel))
        ax, _ao = run(root, rel, d)
        bx, bo = run(root, rel, foreign)
        refs = ephemeral_refs(root, rel)
        if refs:
            efim.append((rel, refs))
        forma = shape(bo) if bx != 0 else '-'
        print('%s\t%d\t%d\t%s\t%d' % (rel, ax, bx, forma, len(refs)))
        if ax == 0 and bx != 0:
            rotas.append((rel, forma))
    print()
    print('# === ACCION A, contra su prediccion ===')
    print('# pedia: >=3 suites MAS que fallan o se saltan por ruta efimera o cwd asumido')
    print('# medido: %d' % len(rotas))
    print('# veredicto: %s' % ('CONFIRMADA' if len(rotas) >= 3
                               else 'REFUTADA' if len(rotas) == 0 else 'CLASE-CHICA'))
    print('# --- el reparto por CAUSA, que la prediccion sumo en una sola cifra')
    print('#   por cwd ASUMIDO : %d' % len(rotas))
    print('#   por ruta EFIMERA: %d  (suites que la nombran: %d)'
          % (sum(1 for r, _ in rotas if ephemeral_refs(root, r)), len(efim)))
    print('# --- y la FORMA del fallo, que decide la severidad')
    for rel, forma in rotas:
        print('#   %-58s %s' % (rel, forma))
    for rel, refs in efim:
        print('# ruta efimera nombrada en %s: %s' % (rel, refs[0][0]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
