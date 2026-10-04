#!/bin/sh
# Barrido EN VIVO del instrumento del pase 94. Uso: sh sweep.sh <org/repo> [org/repo ...]
# Imprime, por repo: testigo (alcance), payload hallado, y manifiestos con licencia + su `name`.
# El canal es raw.githubusercontent.com porque curl -sI contra github.com/ devuelve 403 aqui.
VARIANTES="LICENSE LICENSE.txt LICENSE.TXT LICENSE.md LICENCE LICENCE.txt COPYING COPYING.txt LICENSE-APACHE LICENSE-MIT license license.txt"
RAMAS="main master develop"
code() { curl -sI -o /dev/null -w '%{http_code}' --max-time 15 "$1"; }
for r in "$@"; do
  echo "== $r"
  t=""
  for n in README.md readme.md README.rst README.txt README; do
    for b in $RAMAS; do
      [ "$(code https://raw.githubusercontent.com/$r/$b/$n)" = 200 ] && { t="$b/$n"; break 2; }
    done
  done
  [ -n "$t" ] && echo "   testigo: $t (ALCANZADO)" || echo "   testigo: NINGUNO -> veredicto INDETERMINADO, no 'ausencia'"
  p=""
  for n in $VARIANTES; do
    for b in $RAMAS; do
      [ "$(code https://raw.githubusercontent.com/$r/$b/$n)" = 200 ] && { p="$b/$n"; break 2; }
    done
  done
  [ -n "$p" ] && echo "   payload: $p" || echo "   payload: ninguno en $(echo $VARIANTES | wc -w) variantes x $(echo $RAMAS | wc -w) ramas"
  for f in composer.json package.json pyproject.toml setup.cfg Cargo.toml; do
    for b in $RAMAS; do
      body=$(curl -s --max-time 15 "https://raw.githubusercontent.com/$r/$b/$f")
      echo "$body" | grep -qi '"license"\|^license\|license-files' || continue
      nm=$(echo "$body" | grep -m1 '"name"\|^name' | cut -c1-80)
      lc=$(echo "$body" | grep -im1 '"license"\|^license' | cut -c1-60)
      lf=$(echo "$body" | grep -m1 'license-files' | cut -c1-60)
      echo "   $b/$f -> name:[$nm] license:[$lc] ${lf:+license-files:[$lf]}"
      echo "      ^ P280: si 'name' no coincide con el PROYECTO de $r, la licencia NO es de esta fila"
      break
    done
  done
done
