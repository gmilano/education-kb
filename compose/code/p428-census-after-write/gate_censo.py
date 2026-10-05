#!/usr/bin/env python3
"""Compuerta de CENSO: una cifra de censo tiene que declarar su MOMENTO de medicion.

🆕 `P428` — pase 124 del 2026-10-05. Cierra la accion N, pre-registrada por los pases
122, 123 y 124 y no construida en ninguno de los tres.

EL DEFECTO, MEDIDO EN TRES PASES CONSECUTIVOS
---------------------------------------------
Un censo del corpus se corre ANTES de escribir el pase, porque es el denominador que
decide que entra. Pero la cifra se PUBLICA dentro del mismo pase que agrega filas, asi
que queda vieja en el instante en que se escribe:

    pase 122 -> censo daba 10 pre-escritura y 13 post-escritura
    pase 123 -> idem, y la accion N quedo sin construir
    pase 124 -> 645 pre-escritura / 655 post-escritura (delta = 10)

🔴 Ninguna de esas cifras esta MAL medida: estan mal ETIQUETADAS. El lector no puede
saber si `645` es el corpus contra el que se decidio o el corpus que quedo.

LA REGLA
--------
Toda cifra de censo se publica con su momento: `PRE` (denominador con el que se decidio)
o `POST` (estado en que queda el arbol). Una cifra `POST` que no coincide con la medicion
posterior a la escritura esta `DESFASADO`. Una cifra sin momento es el defecto mismo
(`SIN-MOMENTO`) — es la clase que los pases 122/123 publicaron sin verlo.

🔵 Y la asimetria que importa: una cifra `PRE` NO se invalida por el delta (es correcta
para lo que decidio), pero debe publicar el delta para que el lector pueda derivar el
POST. Por eso `PRE` sin delta declarado tambien falla.
"""
import sys

MOMENTOS = ('PRE', 'POST')


def clasificar_censo(declarado, medido_post, momento=None, delta_declarado=None):
    """Veredicto de una cifra de censo publicada.

    declarado      -- la cifra que el pase escribio
    medido_post    -- el censo re-corrido DESPUES de escribir
    momento        -- 'PRE' | 'POST' | None
    delta_declarado-- delta que el pase publico junto a una cifra PRE
    """
    v = {'declarado': declarado, 'medido_post': medido_post,
         'momento': momento, 'delta_real': medido_post - declarado,
         'veredicto': None, 'motivo': ''}

    if momento not in MOMENTOS:
        v.update(veredicto='SIN-MOMENTO',
                 motivo='P428: la cifra no dice si es el denominador (PRE) o el estado (POST)')
        return v

    if momento == 'POST':
        if declarado == medido_post:
            v.update(veredicto='OK', motivo='cifra POST reproduce el censo posterior a la escritura')
        else:
            v.update(veredicto='DESFASADO',
                     motivo=f'P428: declara POST={declarado} y el censo posterior da {medido_post}')
        return v

    # momento == 'PRE'
    if delta_declarado is None:
        v.update(veredicto='PRE-SIN-DELTA',
                 motivo='P428: una cifra PRE es correcta para lo que decidio, pero sin el delta '
                        'publicado el lector no puede derivar el POST')
    elif delta_declarado != v['delta_real']:
        v.update(veredicto='DELTA-ERRADO',
                 motivo=f'P428: declara delta={delta_declarado} y el real es {v["delta_real"]}')
    else:
        v.update(veredicto='OK', motivo='cifra PRE con su delta publicado y verificado')
    return v


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('uso: gate_censo.py DECLARADO MEDIDO_POST PRE|POST [DELTA]', file=sys.stderr)
        sys.exit(2)
    delta = int(sys.argv[4]) if len(sys.argv) > 4 else None
    r = clasificar_censo(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], delta)
    print(f"{r['veredicto']:14s} declarado={r['declarado']} post={r['medido_post']} "
          f"delta_real={r['delta_real']} | {r['motivo']}")
    sys.exit(0 if r['veredicto'] == 'OK' else 1)
