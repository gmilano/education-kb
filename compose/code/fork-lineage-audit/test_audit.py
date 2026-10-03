#!/usr/bin/env python3
"""Control OBLIGATORIO del fork-lineage-audit (P126: un instrumento sin control positivo
no mide, afirma).

El par de control es el que el pase 62 midio de primera mano:
  - DEBE detectar fork sobre Dymayo/moodler-mcp
  - DEBE NO detectarlo sobre GhaithAlHallak8/moodler-mcp (la madre)
Si las dos ramas no se comportan distinto, el instrumento no discrimina y su salida no vale.
"""
import io, os, sys
from audit_lineage import lineage, surface, audit, divergence

HERE = os.path.dirname(os.path.abspath(__file__))

def fx(name):
    with io.open(os.path.join(HERE, 'fixtures', name), encoding='utf-8') as f:
        return f.read()

fails = []
def check(label, got, want):
    if got != want:
        fails.append('%s: got %r, want %r' % (label, got, want))
    else:
        print('  ok  %-58s %r' % (label, got))

print('== CONTROL POSITIVO/NEGATIVO: el par moodler-mcp (medido en el pase 62) ==')
check('fork detectado en el FORK',
      lineage(fx('dymayo-moodler-mcp.txt')), 'GhaithAlHallak8/moodler-mcp')
check('fork NO detectado en la MADRE',
      lineage(fx('ghaithalhallak8-moodler-mcp.txt')), None)

print('== el instrumento discrimina (las dos ramas diferentes) ==')
check('las dos ramas diferen',
      lineage(fx('dymayo-moodler-mcp.txt')) != lineage(fx('ghaithalhallak8-moodler-mcp.txt')),
      True)

print('== SUPERFICIE: la descripcion se hereda, el README no (P160) ==')
parent = audit('vishalsachdev/canvas-mcp', fx('vishalsachdev-canvas-mcp.txt'))
fork   = audit('BartMassey-upstream/canvas-mcp', fx('bartmassey-canvas-mcp.txt'))
check('madre: no es fork', parent['fork_of'], None)
check('fork: declara su madre', fork['fork_of'], 'vishalsachdev/canvas-mcp')
check('madre: techo de tools', parent['tools'], 103)
check('fork: techo de tools', fork['tools'], 139)
check('divergencia de superficie', divergence(parent, fork), 36)

print('== la descripcion heredada NO alcanza para medir: 102 en las dos ==')
# La linea de `description` es identica en madre y fork; si el instrumento leyera solo esa
# linea, la divergencia daria 0 y seria un falso "identico" (la forma de P151/extractores).
desc_only_parent = 'Canvas LMS MCP server - up to 102 tools and 8 agent skills'
desc_only_fork   = 'Canvas LMS MCP server - up to 102 tools and 8 agent skills'
check('leyendo SOLO la descripcion la divergencia se borra',
      surface(desc_only_fork) - surface(desc_only_parent), 0)
check('y por eso el README es obligatorio', divergence(parent, fork) != 0, True)

print('== caso sin cifra de tools: no inventa ==')
check('repo sin "N tools" -> None', surface('Un repo cualquiera sin cifra'), None)
check('texto vacio -> None', lineage(''), None)

print('== P161: el README promete licencia; el instrumento NO la afirma ==')
dm = audit('DMontgomery40/mcp-canvas-lms', fx('dmontgomery40-mcp-canvas-lms.txt'))
check('no es fork', dm['fork_of'], None)
check('lee la cifra de tools que declara', dm['tools'], 54)

print()
if fails:
    print('FALLARON %d asercion(es):' % len(fails))
    for f in fails:
        print('  - ' + f)
    sys.exit(1)
print('TODAS LAS ASERCIONES PASAN (13)')
