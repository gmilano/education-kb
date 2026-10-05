#!/usr/bin/env python3
"""Suite de `P419`. Cada caso es un ENCABEZADO real de un payload medido el pase 124."""
import sys
from identidad_copyleft import familia, menciones_cruzadas

# Encabezados reales, con el relleno centrado tal como vienen en el payload
GPL3 = ('                    GNU GENERAL PUBLIC LICENSE\n'
        '                       Version 3, 29 June 2007\n\n'
        ' Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>\n\n'
        '                            Preamble\n\n'
        '  The GNU General Public License is a free, copyleft license for software.\n'
        '  13. Use with the GNU Affero General Public License.\n')
GPL2 = ('                    GNU GENERAL PUBLIC LICENSE\n'
        '                       Version 2, June 1991\n\n'
        ' Copyright (C) 1989, 1991 Free Software Foundation, Inc.,\n'
        ' 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA\n\n'
        '  we recommend the GNU Lesser General Public License instead.\n')
AGPL3 = ('                    GNU AFFERO GENERAL PUBLIC LICENSE\n'
         '                       Version 3, 19 November 2007\n\n'
         ' Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>\n')
APACHE = ('\n                                 Apache License\n'
          '                           Version 2.0, January 2004\n'
          '                        http://www.apache.org/licenses/\n')
MIT = ('MIT License\n\nCopyright (c) 2025 Someone\n\n'
       'Permission is hereby granted, free of charge, to any person obtaining a copy\n')
CHINO = ('版权所有 (c) 2021，猿究生\n保留所有权利。\n'
         '感谢您选择 cloud-learning 在线教育产品。\n')
GPL_SIN_VERSION = ('                    GNU GENERAL PUBLIC LICENSE\n\n'
                   ' Everyone is permitted to copy and distribute verbatim copies\n')

CASOS = [
    ('ahmedEid1/lumen — GPL-3.0 que NOMBRA Affero en §13', GPL3, 'GPL-3.0'),
    ('course-tencent-cloud — GPL-2.0 que NOMBRA la Lesser', GPL2, 'GPL-2.0'),
    ('koakademy — AGPL-3.0 de verdad, Affero EN EL ENCABEZADO', AGPL3, 'AGPL-3.0'),
    ('geli — Apache-2.0 con encabezado centrado y linea vacia primera', APACHE, 'Apache-2.0'),
    ('flat — MIT', MIT, 'MIT'),
    ('cloud-learning-ce — EULA propietario en chino (`P421`)', CHINO, 'UNCLASSIFIED'),
    ('GPL sin version: no se infiere (`P286`)', GPL_SIN_VERSION, 'GPL-?'),
]

CASOS_CRUZADAS = [
    ('GPL-3.0 menciona AGPL en el cuerpo', GPL3, ['AGPL']),
    ('GPL-2.0 menciona LGPL en el cuerpo', GPL2, ['LGPL']),
    ('AGPL-3.0 real: Affero esta en el ENCABEZADO, no es mencion cruzada', AGPL3, []),
]


def main():
    fallos = 0
    print('— identidad leida del ENCABEZADO —')
    for nombre, texto, esperado in CASOS:
        fam, ev = familia(texto)
        ok = fam == esperado
        print(f"{'🟢' if ok else '🔴'} {fam:14s} (esperado {esperado:14s}) {nombre}")
        if not ok:
            fallos += 1
            print(f'     evidencia: {ev}')

    print('\n— menciones CRUZADAS: parentesco, nunca identidad —')
    for nombre, texto, esperado in CASOS_CRUZADAS:
        got = menciones_cruzadas(texto)
        ok = got == esperado
        print(f"{'🟢' if ok else '🔴'} {str(got):14s} (esperado {str(esperado):14s}) {nombre}")
        if not ok:
            fallos += 1

    total = len(CASOS) + len(CASOS_CRUZADAS)
    print(f'\n{total - fallos}/{total} casos en verde')
    return 1 if fallos else 0


if __name__ == '__main__':
    sys.exit(main())
