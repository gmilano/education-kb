#!/bin/bash
# Pase 52, accion 1: re-medir los paquetes de registro del pase 50 cuyo veredicto
# de licencia salio de la lista de 4 nombres que el pase 51 probo incompleta.
#
# Tres instrumentos por objetivo, en orden:
#   (a) los 20 nombres de licencia x {main,master} sobre raw.githubusercontent.com
#   (b) control de alcanzabilidad y despues control del HERMANO (tendencia 255)
#   (c) probe ANCLADO por tarball (tendencias 258 y 259), con el ancla CORREGIDA
#       por este pase: insensible a mayusculas, y SIGUE anclada a la raiz de
#       package/ para no admitir node_modules (tendencia 259).
#
# Uso:  ./remeasure.sh < targets.txt      (lineas "paquete|org/repo", "-" si no hay repo)
# Salida TSV: pkg <TAB> repo <TAB> paso <TAB> veredicto <TAB> artefacto <TAB> primera-linea

NAMES20="LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt COPYING.md LICENSE-MIT LICENSE-APACHE LICENSE-APACHE-2.0 LICENSE.rst LICENCE LICENCE.md license license.md License License.md LICENSE-MIT.md UNLICENSE COPYRIGHT NOTICE"
# El ancla CORREGIDA en el pase 52. La del pase 51 era '^package/(LICEN[CS]E|COPYING)[^/]*$'
# y es CASE-SENSITIVE: se perdio 'package/license' con 35.121 bytes de GPL-3.0.
ANCHOR='^package/(licen[cs]e|copying)([._-][A-Za-z0-9]+)?$'

code(){ curl -s -m 12 -o /dev/null -w "%{http_code}" "$1" 2>/dev/null; }
firstline(){ curl -s -m 12 "$1" 2>/dev/null | tr -d '\r' | grep -m1 -vE '^[[:space:]]*$' | cut -c1-90; }

probe_repo(){   # $1=org/repo
  local R="$1" RAW="https://raw.githubusercontent.com/$1"
  for br in main master; do
    for f in $NAMES20; do
      if [ "$(code "$RAW/$br/$f")" = "200" ]; then
        printf "licenciado\t%s:%s\t%s\n" "$br" "$f" "$(firstline "$RAW/$br/$f")"; return 0
      fi
    done
  done
  for br in main master develop; do
    for f in README.md package.json pyproject.toml setup.py README.rst; do
      if [ "$(code "$RAW/$br/$f")" = "200" ]; then
        printf "sin-licencia\t%s:%s(200)\tausencia MEDIDA sobre 20 nombres x 2 ramas\n" "$br" "$f"; return 1
      fi
    done
  done
  printf "indeterminado\t-\tel canal no llego al repo\n"; return 2
}

while IFS='|' read -r PKG REPO; do
  [ -z "$PKG" ] && continue
  if [ "$REPO" = "-" ]; then
    printf "%s\t-\tA/B\tsin-repo-declarado\t-\tno hay org/repo utilizable\n" "$PKG"
  else
    printf "%s\t%s\tA/B\t%s\n" "$PKG" "$REPO" "$(probe_repo "$REPO")"
  fi
  TB=$(curl -s -m 20 "https://registry.npmjs.org/$PKG/latest" 2>/dev/null \
        | python3 -c 'import sys,json;print(json.load(sys.stdin).get("dist",{}).get("tarball",""))' 2>/dev/null)
  if [ -n "$TB" ]; then
    T=$(mktemp); curl -s -m 60 -o "$T" "$TB" 2>/dev/null
    LIST=$(tar -tzf "$T" 2>/dev/null)
    FN=$(printf '%s\n' "$LIST" | grep -i -m1 -E "$ANCHOR")
    DEEP=$(printf '%s\n' "$LIST" | grep -icE 'licen[cs]e|copying')
    if [ -n "$FN" ]; then
      TXT=$(tar -xzOf "$T" "$FN" 2>/dev/null | tr -d '\r' | grep -m1 -vE '^[[:space:]]*$' | cut -c1-90)
      printf "%s\t%s\tC-tarball\tlicenciado-en-tarball\t%s\traiz=1 recursivo=%s | %s\n" "$PKG" "${REPO:--}" "$FN" "$DEEP" "$TXT"
    else
      printf "%s\t%s\tC-tarball\tsin-licencia-en-tarball\t-\traiz=0 recursivo=%s (ancla obligatoria, tend.259)\n" "$PKG" "${REPO:--}" "$DEEP"
    fi
    rm -f "$T"
  else
    printf "%s\t%s\tC-tarball\tno-resuelve-tarball\t-\tel registro no devolvio dist.tarball\n" "$PKG" "${REPO:--}"
  fi
done
