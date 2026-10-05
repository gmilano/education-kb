#!/usr/bin/env python3
"""Suite de la compuerta. Cada caso es un PAYLOAD medido este pase, no un invento."""
import sys
from gate_cesion import clasificar

MIT_REAL = ('MIT License\n\nCopyright (c) 2025 DaRL-GenAI\n\nPermission is hereby granted, '
            'free of charge, to any person obtaining a copy of this software and associated '
            'documentation files (the "Software"), to deal in the Software without '
            'restriction, including without limitation the rights to use, copy, modify, '
            'merge, publish, distribute, sublicense, and/or sell copies of the Software, '
            'and to permit persons to whom the Software is furnished to do so, subject to '
            'the following conditions:\n\nThe above copyright notice and this permission '
            'notice shall be included in all copies or substantial portions of the '
            'Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, '
            'EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF '
            'MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.\n')
PAGELM = ('# PageLM Community License\n\nCopyright (c) 2025 nullure & recabasic\n\n'
          'Permission is hereby granted, free of charge, to any person obtaining a copy of '
          'this software and associated documentation files (the "Software"), to use, copy, '
          'modify, and run the Software for personal, educational, or non-commercial '
          'research purposes, subject to the terms and conditions set forth herein.\n'
          + ('Revenue Sharing Requirement. ' * 300))
ELASTIC = ('Elastic License 2.0\n\nURL: https://www.elastic.co/licensing/elastic-license\n\n'
           '## Acceptance\n\nBy using the software, you agree to all of the terms and '
           'conditions below.\n' + ('You may not provide the software to third parties as a '
           'hosted or managed service, where the service provides users with access to any '
           'substantial set of the features or functionality of the software. ' * 20))
FAIRCODE = ('# License\n\nPortions of this software are licensed as follows:\n\n- Content '
            'outside of the above mentioned files or restrictions is available under the '
            '"Fair code License" as defined below.\n' + ('terms and conditions ' * 500))
NOMBRAMIENTO = 'License: GNU GPL V3\n'
METADATA = 'MIT'
VACIO = ''

CASOS = [
    ('MIT real (instructional_agents)',      MIT_REAL,     'MIT',   True),
    ('P411 PageLM Community License',        PAGELM,       'NO-OSI', False),
    ('P412 Elastic License 2.0',             ELASTIC,      'NO-OSI', False),
    ('P412 Fair code License',               FAIRCODE,     'NO-OSI', False),
    ('P414 nombramiento de 19 B',            NOMBRAMIENTO, 'NOMBRAMIENTO', False),
    ('P414 campo de metadata de 3 B',        METADATA,     'SIN-CESION', False),
    ('P404 archivo de 0 B',                  VACIO,        'SIN-CESION', False),
]

fallos = 0
for nombre, payload, familia_esperada, usable_esperado in CASOS:
    r = clasificar(payload)
    ok_f = r['familia'].startswith(familia_esperada)
    ok_u = r['usable'] == usable_esperado
    estado = '🟢' if (ok_f and ok_u) else '🔴'
    if not (ok_f and ok_u):
        fallos += 1
    print(f"{estado} {nombre:38} -> {r['familia']:34} usable={'SI' if r['usable'] else 'NO':3} "
          f"({r['bytes']} B)")
    if not (ok_f and ok_u):
        print(f"    esperaba familia~{familia_esperada} usable={usable_esperado}")
print()
print(f"{'🟢 TODO VERDE' if fallos == 0 else f'🔴 {fallos} FALLOS'} — {len(CASOS)} casos")
sys.exit(1 if fallos else 0)
