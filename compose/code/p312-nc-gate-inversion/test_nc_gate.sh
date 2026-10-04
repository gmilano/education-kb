#!/bin/bash
# P312 — la compuerta de uso comercial se abria sobre las familias que existe para atrapar.
#
# Corre OFFLINE.  Invocacion:  sh test_nc_gate.sh
#
# Los payloads no son fixtures inventadas: son los textos tal como los declaran los repos
# que el pase 101 midio de primera mano por `raw.githubusercontent.com` (unico canal 200).
set -u
cd "$(dirname "$0")" && . ../lib/license_family.sh

n=0; fail=0
check() { n=$((n+1))
  if [ "$2" = "$3" ]; then printf 'PASS  %-58s %s\n' "$1" "$2"
  else printf 'FAIL  %-58s esperado=%s obtuvo=%s\n' "$1" "$2" "$3"; fail=$((fail+1)); fi; }
cu() { if commercial_use_ok "$1"; then echo ALLOWED; else echo PROHIBITED; fi; }

# ---------------------------------------------------------------------------
# El ESPECIMEN.  `devissaputra/classroom_discourse_intelligence/data/README.md`, leido el
# 2026-10-04: el repo es MIT en el CODIGO y esto en los DATOS.
NCSA_REAL='## License
CC BY-NC-SA 4.0. **Non-commercial** and ShareAlike restrictions apply. This repository does not redistribute the source corpus.'
# El mismo atributo en el texto canonico de Creative Commons.
NCSA_CANON='Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
NonCommercial and ShareAlike restrictions apply.'
NC='Creative Commons Attribution-NonCommercial 4.0 International
You may not use the material for commercial purposes.'
SA='Creative Commons Attribution-ShareAlike 4.0 International'
BY='Creative Commons Attribution 4.0 International'

# --- D1: el ORDEN de dos ramas decidia la respuesta entre atributos ORTOGONALES ---------
# Antes del arreglo: `ShareAlike` iba antes de `NonCommercial` y retornaba primero, asi que
# CC BY-NC-SA volvia `CC-BY-SA-4.0`.  La familia se identificaba y el atributo NC --el unico
# que decide si la pieza entra en un entregable-- se perdia en silencio.
check "D1 CC BY-NC-SA canonico no se degrada a CC-BY-SA" CC-BY-NC-SA-4.0 "$(family_of "$NCSA_CANON")"
check "D1 CC BY-NC conserva NC"                          CC-BY-NC-4.0    "$(family_of "$NC")"
# Positivos de la MISMA rama: el arreglo no puede darle NC a quien no lo tiene.
check "D1 POSITIVO CC BY-SA sigue CC-BY-SA"              CC-BY-SA-4.0    "$(family_of "$SA")"
check "D1 POSITIVO CC BY pelada sigue CC-BY"             CC-BY-4.0       "$(family_of "$BY")"

# --- D2: la COMPUERTA, que es el defecto grave ------------------------------------------
# La premisa de P250 es correcta --«familia OSI identificada -> permite uso comercial POR
# DEFINICION»-- pero el pase 82 puso DETRAS de ella cuatro familias que NO son OSI.
# Resultado: `CC-BY-NC-4.0`, cuyo NOMBRE dice NonCommercial, volvia PERMITIDO, porque la
# compuerta cortocircuitaba el token-match antes de leer la palabra del payload.
check "D2 CC BY-NC-SA uso comercial PROHIBIDO"  PROHIBITED "$(cu "$NCSA_CANON")"
check "D2 CC BY-NC uso comercial PROHIBIDO"     PROHIBITED "$(cu "$NC")"
check "D2 POSITIVO CC BY-SA ALLOWED"            ALLOWED    "$(cu "$SA")"
check "D2 POSITIVO CC BY ALLOWED"               ALLOWED    "$(cu "$BY")"

# --- El especimen REAL, que es prosa y no el texto canonico -----------------------------
# Importa medirlo aparte: el `data/README.md` no trae el titulo de Creative Commons, trae la
# SIGLA.  Antes del arreglo volvia UNCLASSIFIED, y por el camino de UNCLASSIFIED el
# token-match SI corria y acertaba el permiso -- o sea que el especimen daba la respuesta
# correcta por la razon equivocada, y el texto canonico daba la incorrecta.
check "ESPECIMEN data/README.md: NC reconocido por sigla"   CC-BY-NC-SA-4.0 "$(family_of "$NCSA_REAL")"
check "ESPECIMEN data/README.md: comercial PROHIBIDO"     PROHIBITED      "$(cu "$NCSA_REAL")"

# --- Invariante de P308: el arreglo no puede depender del REFLUJO ------------------------
reflow() { tr -s '[:space:]' ' ' | fold -s -w "$1"; }
for w in 70 40; do
  check "REFLUJO $w CC BY-NC-SA sigue NC"       CC-BY-NC-SA-4.0 "$(family_of "$(printf '%s' "$NCSA_CANON" | reflow $w)")"
  check "REFLUJO $w CC BY-NC-SA sigue PROHIBIDO" PROHIBITED     "$(cu "$(printf '%s' "$NCSA_CANON" | reflow $w)")"
done

# --- P237/P313: las tres familias que vivian SOLO en la copia inline de p170 -------------
# Eran la razon DECLARADA en el pase 100 para no rewirear.  Entran a la libreria ANTES del
# rewiring, y las tres prohiben el uso que importa.
check "P313 BUSL clasificada"     BUSL     "$(family_of 'Business Source License 1.1

Licensor: Example Corp')"
check "P313 Elastic clasificada"  Elastic  "$(family_of 'Elastic License 2.0')"
check "P313 PolyForm clasificada" PolyForm "$(family_of 'PolyForm Noncommercial License 1.0.0')"

# --- P313: el control de EQUIVALENCIA del rewiring --------------------------------------
# Las cuatro copias conservan su VOCABULARIO publicado, que es lo que hace comparables los
# TSV ya escritos.  La traduccion agrupa (GPL-3.0 -> GPL) y nunca inventa.
p170_classify() { case "$(family_of "$1")" in GPL-2.0|GPL-3.0) echo GPL;; CC-BY-*) echo CC-BY;;
                  UNCLASSIFIED|NONCOMMERCIAL-NOT-OSI) echo UNKNOWN;; *) family_of "$1";; esac; }
GPL3T='                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007'
check "P313 p170 conserva su vocabulario: GPL agrupado" GPL     "$(p170_classify "$GPL3T")"
check "P313 p170 conserva su vocabulario: CC-BY"        CC-BY   "$(p170_classify "$BY")"
check "P313 p170 conserva su vocabulario: UNKNOWN"      UNKNOWN "$(p170_classify 'texto sin cesion alguna')"
check "P313 p170 NO agrupa lo que no debe: MIT"         MIT     "$(p170_classify 'MIT License
Permission is hereby granted, free of charge')"

printf '\n%d/%d checks passed\n' "$((n-fail))" "$n"
[ "$fail" = 0 ] || exit 1
