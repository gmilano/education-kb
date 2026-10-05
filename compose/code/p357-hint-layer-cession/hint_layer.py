#!/usr/bin/env python3
"""`P357` — la capa de HINT no HEREDA la cesion de su problema padre: la deja VACIA.

La accion C pre-registrada por el pase 111 pedia medir la clasificacion de cesion de
`P346`/`P348` sobre la capa de *hint* y predijo que la tasa `RESOLUBLE` quedaria
**dentro de +-3 pp** del 76,4 % de los problemas, *«porque el hint hereda el `license`
de su problema padre»*.

La herencia es la hipotesis, y es FALSABLE por lectura directa: cada objeto de hint trae
sus PROPIOS campos `oer` y `license`. Este modulo los lee y los compara con los del padre,
en vez de deducir la herencia del agregado.

Reusa `clasificar` de `p345-oer-four-forms/entregabilidad.py` (`P237`) — el mismo
instrumento que produjo el 58,0 % y el 76,4 %. Un clasificador propio volveria la
comparacion incomparable por una tercera via, que es el defecto que `P344` y `P348`
ya documentaron dos veces.

Uso:  python3 hint_layer.py /ruta/a/OATutor-Content [--tsv salida.tsv]
"""
import collections, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
P345 = os.path.join(HERE, '..', 'p345-oer-four-forms', 'entregabilidad.py')


def _clasificar():
    spec = importlib.util.spec_from_file_location('p345_entregabilidad', P345)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.clasificar


clasificar = _clasificar()


def layer_of(relpath):
    """La capa, por RUTA — la misma particion que `p328/census.py` usa."""
    return 'hint' if '/tutoring/' in relpath else 'problema'


def units(obj, out):
    """Todo dict con clave `license`, en cualquier profundidad. Un `license` es una UNIDAD."""
    if isinstance(obj, dict):
        if 'license' in obj:
            out.append(obj)
        for v in obj.values():
            units(v, out)
    elif isinstance(obj, list):
        for v in obj:
            units(v, out)
    return out


def problem_of(relpath):
    """`content-pool/<id>/...` -> `<id>`. La identidad del problema padre."""
    parts = relpath.split('/')
    return parts[1] if len(parts) > 2 and parts[0] == 'content-pool' else None


def measure(root):
    """Recorre el corpus una vez. Devuelve (conteos por capa, herencia, filas)."""
    pool = os.path.join(root, 'content-pool')
    por_capa = collections.defaultdict(collections.Counter)
    # cesion declarada por el JSON de problema de primer nivel: content-pool/<id>/<id>.json
    padre = {}
    hijos = collections.defaultdict(list)
    vacios = collections.Counter()
    nfiles = 0

    for dp, _dn, fn in os.walk(pool):
        for f in fn:
            if not f.endswith('.json'):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, root).replace(os.sep, '/')
            nfiles += 1
            try:
                with open(p, encoding='utf-8', errors='replace') as fh:
                    obj = json.load(fh)
            except Exception:
                por_capa[layer_of(rel)]['JSON-INVALIDO'] += 1
                continue
            cap = layer_of(rel)
            pid = problem_of(rel)
            for u in units(obj, []):
                lic = u.get('license') or ''
                clase, _ident = clasificar(lic)
                por_capa[cap][clase] += 1
                if not str(lic).strip():
                    vacios[cap] += 1
                if cap == 'hint' and pid:
                    hijos[pid].append(str(lic).strip())
                # el problema de primer nivel declara la cesion del padre
                if cap == 'problema' and pid and rel == 'content-pool/%s/%s.json' % (pid, pid):
                    padre.setdefault(pid, str(lic).strip())
    return por_capa, padre, hijos, vacios, nfiles


def inheritance(padre, hijos):
    """La hipotesis de la accion C, medida DIRECTO: hint.license == padre.license?"""
    t = collections.Counter()
    for pid, lics in hijos.items():
        pl = padre.get(pid)
        for hl in lics:
            if pl is None:
                t['PADRE-NO-MEDIDO'] += 1
            elif hl == pl:
                t['IGUAL-AL-PADRE'] += 1
            elif not hl and pl:
                t['HIJO-VACIO-PADRE-CEDE'] += 1
            elif hl and not pl:
                t['HIJO-CEDE-PADRE-VACIO'] += 1
            else:
                t['DISTINTO-NO-VACIO'] += 1
    return t


def rate(counter):
    tot = sum(counter[k] for k in counter if k != 'JSON-INVALIDO')
    return (counter['RESOLUBLE'], tot, 100.0 * counter['RESOLUBLE'] / tot if tot else 0.0)


PROBLEMAS_PCT = 76.4   # `P348`, pase 111, sobre las 13.371 unidades-problema


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip().splitlines()[-1]); return 2
    root = sys.argv[1]
    por_capa, padre, hijos, vacios, nfiles = measure(root)

    print('=== EL REPARTO POR CAPA (unidades = todo dict con `license`) ===')
    tot_all = 0
    for cap in ('problema', 'hint'):
        r, t, pct = rate(por_capa[cap])
        tot_all += t
        print('%-10s RESOLUBLE %6d / %6d unidades = %5.1f %%   (license vacio: %d)'
              % (cap, r, t, pct, vacios[cap]))
    print('%-10s %d unidades en %d archivos JSON' % ('TOTAL', tot_all, nfiles))
    print()
    for cap in ('problema', 'hint'):
        print('--- %s' % cap)
        for k, v in por_capa[cap].most_common():
            print('      %-22s %6d' % (k, v))
    print()
    _r, _t, hint_pct = rate(por_capa['hint'])
    delta = hint_pct - PROBLEMAS_PCT
    print('=== ACCION C, contra su prediccion ===')
    print('pedia:  tasa RESOLUBLE del hint DENTRO de +-3 pp de %.1f %% (problemas, P348)'
          % PROBLEMAS_PCT)
    print('medido: %.1f %%  ->  delta %+.1f pp  ->  %s'
          % (hint_pct, delta, 'CONFIRMADA' if abs(delta) <= 3.0 else 'REFUTADA'))
    print()
    print('=== LA HIPOTESIS DEL MECANISMO, MEDIDA DIRECTO (no deducida del agregado) ===')
    inh = inheritance(padre, hijos)
    tot = sum(inh.values())
    for k, v in inh.most_common():
        print('   %-26s %6d  (%5.1f %%)' % (k, v, 100.0 * v / tot if tot else 0))
    print('   %-26s %6d' % ('TOTAL hints comparados', tot))
    igual = 100.0 * inh['IGUAL-AL-PADRE'] / tot if tot else 0
    print()
    print('La accion C decia «el hint HEREDA el license de su problema padre».')
    print('Identico al padre: %.1f %% de los hints. La herencia %s es la identidad.'
          % (igual, 'SI' if igual > 95 else 'NO'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
