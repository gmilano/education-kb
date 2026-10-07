#!/usr/bin/env python3
"""Suite de `P429`. La referencia es EXTERNA al instrumento (`P417`): los 4 primeros
casos son las 4 afirmaciones REALES del listicle del pase 125, cada una con su lectura
de primera mano del sidebar de GitHub, y no «lo que el instrumento ya hace»."""
import sys
from audit_claim import riesgo

# (nombre, afirmada, primera_mano, veredicto_esperado, riesgo_esperado)
CASOS = [
    # --- los 4 reales del pase 125, medidos contra el sidebar de GitHub ---
    ('sakai (real)',      'ECL-2.0',    'ECL-2.0',    'ACIERTO',  'COSMETICA'),
    ('chamilo (real)',    'GPL-3.0',    'GPL-3.0',    'ACIERTO',  'COSMETICA'),
    ('formalms (real)',   'Apache-2.0', 'NINGUNA',    'REFUTADA', 'BLOQUEANTE'),
    ('open edx (real)',   None,         'AGPL-3.0',   'OMITIDA',  'HOSPEDAJE'),

    # --- el eje que decide la entrega, en los dos sentidos ---
    ('MIT dicho, AGPL real',   'MIT',      'AGPL-3.0', 'REFUTADA', 'HOSPEDAJE'),  # motivo: USO EN RED
    ('AGPL dicho, MIT real',   'AGPL-3.0', 'MIT',      'REFUTADA', 'HOSPEDAJE'),
    # `P419` en su forma pura: GPL-3.0 vs AGPL-3.0 difieren SOLO en uso en red
    ('GPL3 dicho, AGPL real',  'GPL-3.0',  'AGPL-3.0', 'REFUTADA', 'HOSPEDAJE'),

    # --- discrepancias que NO mueven la entrega: el instrumento no debe inflar ---
    ('MIT dicho, Apache real', 'MIT',      'Apache-2.0', 'REFUTADA', 'COSMETICA'),
    ('GPL2 dicho, GPL3 real',  'GPL-2.0',  'GPL-3.0',    'REFUTADA', 'COSMETICA'),

    # --- el error que FAVORECE al cliente no se cobra como bloqueante ---
    ('nada dicho, MIT real',   'NINGUNA',  'MIT',        'REFUTADA', 'COSMETICA'),

    # --- omision inocua: no nombro la cesion y lo medido es permisivo ---
    ('omitida, MIT real',      None,       'MIT',        'OMITIDA',  'COSMETICA'),
    # --- omision sobre un repo que no cede: bloqueante, no cosmetica ---
    ('omitida, sin cesion',    None,       'NINGUNA',    'OMITIDA',  'BLOQUEANTE'),

    # --- P562 (pase 46): las familias EPL/MPL versionadas que P560 hizo EMITIBLES ---
    # Antes de P560 el clasificador devolvia `EPL` a secas y caia en NO_CLASIFICADA, asi que un
    # componente EPL declarado MIT se reportaba como discrepancia SIN CLASE.  Ahora la clase
    # existe, y un permisivo-dicho / copyleft-real es una refutacion que mueve la entrega.
    ('MIT dicho, EPL-2.0 real',    'MIT',     'EPL-2.0',         'REFUTADA', 'BLOQUEANTE'),
    ('MIT dicho, EPL-1.0 real',    'MIT',     'EPL-1.0',         'REFUTADA', 'BLOQUEANTE'),
    ('MIT dicho, MPL-1.1 real',    'MIT',     'MPL-1.1',         'REFUTADA', 'BLOQUEANTE'),
    # Y la version sin leer sigue siendo copyleft: «es algun EPL» ya decide la entrega.
    ('MIT dicho, EPL sin version', 'MIT',     'EPL-UNVERSIONED', 'REFUTADA', 'BLOQUEANTE'),
    # NEG: dentro de la MISMA clase la discrepancia de VERSION no se infla a bloqueante.
    ('EPL2 dicho, EPL1 real',      'EPL-2.0', 'EPL-1.0',         'REFUTADA', 'COSMETICA'),
    ('MPL2 dicho, MPL1.1 real',    'MPL-2.0', 'MPL-1.1',         'REFUTADA', 'COSMETICA'),
]


def main():
    ok = 0
    for nombre, af, pm, ev, er in CASOS:
        v, r, m = riesgo(af, pm)
        bien = (v == ev and r == er)
        # 🔴 `P430`: el veredicto no alcanza. El defecto de la v1 era invisible en
        # (veredicto, riesgo) y visible SOLO en el motivo, asi que toda discrepancia
        # cuyo riesgo es HOSPEDAJE tiene que NOMBRAR el uso en red.
        if bien and r == 'HOSPEDAJE' and v == 'REFUTADA':
            bien = ('USO EN RED' in m)
        ok += bien
        print(f'{"PASS" if bien else "FAIL"}  {nombre:24s} -> {v}/{r}'
              + ('' if bien else f'   ESPERADO {ev}/{er}')
              + f'\n          {m}')
    print(f'\n{ok}/{len(CASOS)}')
    return 0 if ok == len(CASOS) else 1


if __name__ == '__main__':
    sys.exit(main())
