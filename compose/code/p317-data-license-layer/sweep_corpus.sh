#!/bin/sh
# P317 -- los DOS ejes de la pregunta de datos, medidos de primera mano.
#
# CANAL (P247, medido en el pase 102 y no heredado):
#   github.com (web) / api.github.com / codeload -> 403.  raw.githubusercontent.com -> 200.
#   El arbol se ENUMERA con un clon sin blobs, que es el canal de P275 y el unico que
#   sostiene una AUSENCIA. Es lo que distingue este barrido del de paths adivinados, y el
#   control negativo de P319 (en `test_corpus_axis.py`) mide exactamente esa diferencia.
#
# CONTROLES (sin ellos no se publica ningun negativo):
#   C1  slug inventado -> el clon DEBE fallar. Si no falla, el canal no discrimina.
#   C2  control POSITIVO: `devissaputra/classroom_discourse_intelligence` DEBE volver
#       DATOS-DECLARADOS-DISTINTOS, el positivo conocido de P315. Un instrumento que no
#       reproduce un positivo conocido no sostiene ningun negativo sobre los otros 8.
#   C3  P319, offline y como aserto, en `test_corpus_axis.py`.
#
# El clasificador de licencias NO se inlinea (P237, regla de `lib/`).
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
. "$HERE/../lib/license_family.sh"
WORK=${WORK:-$(mktemp -d)}
RAW=https://raw.githubusercontent.com
export HERE

tree_of() { # $1=slug -> enumera el arbol COMPLETO (P275)
  d="$WORK/$(echo "$1" | tr '/' '-')"
  [ -d "$d" ] || git clone -q --filter=blob:none --no-checkout --depth 1 \
    "https://github.com/$1" "$d" 2>/dev/null || return 1
  git -C "$d" ls-tree --name-only -r HEAD 2>/dev/null
}

payload() { curl -sL --max-time 25 "$RAW/$1/HEAD/$2" 2>/dev/null; }

has_path() { grep -qxF "$2" "$1"; }

code_family() { # $1=slug  $2=archivo de listado
  for n in LICENSE LICENSE.md LICENSE.txt LICENSE.TXT COPYING COPYING.txt LICENCE; do
    if has_path "$2" "$n"; then
      p=$(payload "$1" "$n")
      [ -n "$p" ] && { family_of "$p"; return; }
    fi
  done
  # P314: la concesion puede vivir en el CUERPO del README y no haber archivo alguno.
  if printf '%s' "$(payload "$1" README.md)" \
     | grep -q 'Permission is hereby granted, free of charge'; then
    echo "MIT-EN-README-SIN-ARCHIVO"; return
  fi
  echo "SIN-ARCHIVO-DE-LICENCIA"
}

data_terms() { # $1=slug  $2=archivo de listado -> "FAMILIA|comercial@donde" o vacio
  for cand in data/README.md datasets/README.md corpus/README.md \
              data/LICENSE DATA_LICENSE README.md; do
    has_path "$2" "$cand" || continue
    body=$(payload "$1" "$cand")
    [ -n "$body" ] || continue
    out=$(printf '%s' "$body" | python3 -c '
import sys, os
sys.path.insert(0, os.environ["HERE"])
from corpus_axis import data_terms_in_text
r = data_terms_in_text(sys.stdin.read())
if r:
    print("%s|%s" % (r[0], "comercial-OK" if r[1] else "comercial-PROHIBIDO"))
')
    [ -n "$out" ] && { echo "$out@$cand"; return; }
  done
}

echo "== C1: compuerta de slug inventado =="
if tree_of "gmilano/zzz-fake-repo-p317-pase102" >/dev/null 2>&1; then
  echo "NO-CLAIM: el canal no discrimina slugs" >&2; exit 1
fi
echo "slug falso RECHAZADO (el canal discrimina)"
echo

printf 'slug\tcohorte\tlicencia_codigo\tarchivos_corpus\tterminos_datos\tveredicto\n'

grep -v '^#' "$HERE/targets.tsv" | while IFS="$(printf '\t')" read -r slug cohort published; do
  [ -n "${slug:-}" ] || continue
  L="$WORK/list-$(echo "$slug" | tr '/' '-').txt"
  if ! tree_of "$slug" > "$L" 2>/dev/null || [ ! -s "$L" ]; then
    printf '%s\t%s\tCLONE-FAIL\t-\t-\tNO-CLAIM\n' "$slug" "$cohort"; continue
  fi
  cf=$(code_family "$slug" "$L")
  dt=$(data_terms "$slug" "$L")
  row=$(python3 - "$L" "${dt:-}" "$cf" <<'PY'
import os, sys
sys.path.insert(0, os.environ["HERE"])
from corpus_axis import redistributes_corpus, verdict
tree = open(sys.argv[1]).read().splitlines()
dt_raw, cf = sys.argv[2], sys.argv[3]
ships, n = redistributes_corpus(tree)
dt = (dt_raw.split("@")[0].split("|")[0], "comercial-OK" in dt_raw) if dt_raw else None
print("%d\t%s\t%s" % (n, dt_raw or "NINGUNO", verdict(ships, dt, cf)))
PY
)
  printf '%s\t%s\t%s\t%s\n' "$slug" "$cohort" "$cf" "$row"
done
