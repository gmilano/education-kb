#!/usr/bin/env python3
"""`P348` — contar por FIGURA sobresamplea justo las unidades que no ceden.

La accion C pre-registrada por el pase 110 pedia medir la clasificacion de cesion de `P346`
sobre las **13.371 unidades** completas, y predijo que la tasa `RESOLUBLE` CAERIA por debajo
del 58,0 % de las figuras, *«porque las figuras viven en los problemas de OpenStax, que son
los que traen CC BY 4.0»*.

Sale REFUTADA, y por dos motivos distintos que se apilan:

1. **La direccion es la contraria.** Sobre las 13.371 unidades la tasa es **76,4 %**, no
   «menos de 58,0 %». Tener figura es un predictor NEGATIVO de cesion resoluble, no positivo.

2. **Y los dos numeros no eran comparables.** El 58,0 % cuenta ARCHIVOS DE FIGURA (2.443);
   el 76,4 % cuenta PROBLEMAS (13.371). Puestos en la misma unidad -el problema- la capa con
   figura da **63,4 %**, no 58,0 %. Los 5,4 pp de diferencia son FORMA DEL DENOMINADOR, no
   cesion. Es `P344` otra vez, un pase despues y en otra forma.

El mecanismo esta MEDIDO y no supuesto: las unidades mal cedidas cargan **mas figuras por
unidad** que las bien cedidas, asi que un conteo ponderado por figura las pesa mas.

  RESOLUBLE        1,411 figuras/unidad
  NO-RESOLUBLE     1,764 figuras/unidad   (+25,0 %)
  NO-ES-CESION     3,021 figuras/unidad   (mas del DOBLE: la peor cubeta es la mas pesada)

Reusa `clasificar` de `p345-oer-four-forms/entregabilidad.py` — el mismo instrumento que
produjo el 58,0 %. Reescribirlo habria hecho la comparacion incomparable por una tercera via.
"""
import collections, csv, gzip, os, sys

P345 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'p345-oer-four-forms')


def _clasificar():
    """Importa `clasificar` de `p345-oer-four-forms/entregabilidad.py`.

    🔵 La primera version de este modulo cargaba la funcion partiendo el FUENTE en
    `lic = {}` y haciendo `exec` del trozo de arriba, porque importar ese modulo
    disparaba su cuerpo de reporte y pedia un censo en `/tmp`. El arreglo de `P352`
    volvio importable al modulo, asi que el truco sobra: se importa y listo. Un
    lector que reusa por `exec` de un fragmento depende de donde cae una linea.
    """
    import importlib.util
    ruta = os.path.join(P345, 'entregabilidad.py')
    spec = importlib.util.spec_from_file_location('p345_entregabilidad', ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.clasificar


clasificar = _clasificar()


def cargar_censo(path=None):
    """`problem_id` -> (license, oer). Las 13.371 unidades del pase 110."""
    path = path or os.path.join(P345, 'censo-unidades.2026-10-05.tsv.gz')
    op = gzip.open if path.endswith('.gz') else open
    out = {}
    with op(path, 'rt', encoding='utf-8') as fh:
        for r in csv.DictReader(fh, delimiter='\t'):
            out[r['problem_id']] = (r['license'], r.get('oer', ''))
    return out


def cargar_figuras(path=None):
    """Las 2.443 filas de figura, atribuidas a su problema por RUTA (`P345`)."""
    path = path or os.path.join(P345, 'corte-figuras.2026-10-05.tsv')
    with open(path, encoding='utf-8') as fh:
        return [r['problem_id'] for r in csv.DictReader(fh, delimiter='\t')]


def tasa(unidades, censo):
    """(resoluble, total, porcentaje) sobre un conjunto de UNIDADES."""
    total = len(unidades)
    res = sum(1 for u in unidades if clasificar(censo.get(u, ('', ''))[0])[0] == 'RESOLUBLE')
    return (res, total, 100.0 * res / total if total else 0.0)


def tasa_por_figura(figuras, censo):
    """(resoluble, total, porcentaje) ponderado por ARCHIVO DE FIGURA.
    Es el conteo que produjo el 58,0 % del pase 110."""
    total = len(figuras)
    res = sum(1 for p in figuras if clasificar(censo.get(p, ('', ''))[0])[0] == 'RESOLUBLE')
    return (res, total, 100.0 * res / total if total else 0.0)


def figuras_por_unidad(figuras, censo):
    """clase de cesion -> (unidades, figuras, figuras/unidad). El MECANISMO."""
    por_unidad = collections.Counter(figuras)
    acum = collections.defaultdict(lambda: [0, 0])
    for u, n in por_unidad.items():
        cls = clasificar(censo.get(u, ('', ''))[0])[0]
        acum[cls][0] += 1
        acum[cls][1] += n
    return {k: (v[0], v[1], v[1] / v[0]) for k, v in acum.items()}


def factor_de_sesgo(figuras, censo):
    """Cuanto MAS pesa una unidad no-resoluble en un conteo por figura.
    >1 significa que contar por figura sobresamplea lo que no cede."""
    fpu = figuras_por_unidad(figuras, censo)
    res_u = fpu.get('RESOLUBLE', (0, 0, 0))
    otras = [(v[0], v[1]) for k, v in fpu.items() if k != 'RESOLUBLE']
    if not otras or not res_u[0]:
        return None
    u_otras = sum(x[0] for x in otras)
    f_otras = sum(x[1] for x in otras)
    return (f_otras / u_otras) / res_u[2]


def informe(censo=None, figuras=None):
    censo = censo if censo is not None else cargar_censo()
    figuras = figuras if figuras is not None else cargar_figuras()
    con_fig = set(figuras)
    todas = list(censo)
    sin_fig = [u for u in todas if u not in con_fig]
    out = {
        'corpus': tasa(todas, censo),
        'con_figura': tasa([u for u in todas if u in con_fig], censo),
        'sin_figura': tasa(sin_fig, censo),
        'por_figura': tasa_por_figura(figuras, censo),
        'figuras_por_unidad': figuras_por_unidad(figuras, censo),
        'factor_de_sesgo': factor_de_sesgo(figuras, censo),
    }
    return out


if __name__ == '__main__':
    r = informe()
    print('=== LA COMPARACION, EN LA MISMA UNIDAD (el problema) ===')
    for k in ('corpus', 'con_figura', 'sin_figura'):
        res, tot, pc = r[k]
        print('%-14s %6d resoluble / %6d unidades = %5.1f %%' % (k, res, tot, pc))
    res, tot, pc = r['por_figura']
    print()
    print('=== EL CONTEO DEL PASE 110, ponderado por ARCHIVO DE FIGURA ===')
    print('%-14s %6d resoluble / %6d figuras  = %5.1f %%' % ('por_figura', res, tot, pc))
    print()
    print('ACCION C pedia: tasa del corpus POR DEBAJO de 58,0 %%')
    print('ACCION C medido: %.1f %% -> REFUTADA (%+.1f pp)' % (r['corpus'][2], r['corpus'][2] - 58.0))
    print('de los cuales FORMA DEL DENOMINADOR: %+.1f pp (58,0 -> %.1f por unidad)'
          % (r['con_figura'][2] - r['por_figura'][2], r['con_figura'][2]))
    print()
    print('=== EL MECANISMO: figuras por unidad, por clase ===')
    for k, (u, f, fpu) in sorted(r['figuras_por_unidad'].items(), key=lambda x: -x[1][0]):
        print('%-22s unidades %5d  figuras %5d  figuras/unidad %.3f' % (k, u, f, fpu))
    print()
    print('FACTOR DE SESGO (no-resoluble / resoluble): %.3f' % r['factor_de_sesgo'])
