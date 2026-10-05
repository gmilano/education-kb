#!/bin/bash
# P322 — barrido del campo `license` POR ITEM sobre OATutor-Content.
#
# Canal (P275): el arbol se ENUMERA con un clon --filter=blob:none --no-checkout, nunca
# se adivinan rutas (P319).  El payload de cada item se lee de raw.githubusercontent.
#
# Muestreo SISTEMATICO (cada N-esimo item del arbol ordenado), no aleatorio sin semilla:
# es reproducible por quien tenga el mismo arbol.
#
#   WORK=/tmp/t322 STEP=33 sh sweep_items.sh > result.$(date +%F).tsv
set -u
WORK="${WORK:-/tmp/t322}"
STEP="${STEP:-33}"
REPO="https://github.com/CAHLR/OATutor-Content"
RAW="https://raw.githubusercontent.com/CAHLR/OATutor-Content/HEAD"

if [ ! -d "$WORK/.git" ]; then
  git clone --filter=blob:none --no-checkout --depth 1 "$REPO" "$WORK" >&2 || exit 1
fi
git -C "$WORK" ls-tree -r --name-only HEAD \
  | grep -E '^content-pool/[^/]+/[^/]+\.json$' | sort > "$WORK/all_items.txt"

awk -v s="$STEP" 'NR%s==1' "$WORK/all_items.txt" > "$WORK/sample.txt"

export RAW
fetch_one() {
  p="$1"
  body=$(curl -s --max-time 25 "$RAW/$p")
  printf '%s' "$body" | python3 -c "
import sys,json,os
sys.path.insert(0,os.environ['P322DIR'])
from classify_item import classify
p=os.environ['P322PATH']
try: d=json.load(sys.stdin)
except Exception: print(f'{p}\tPARSE-FAIL\t-\t-'); raise SystemExit
c,det=classify(d)
print(f\"{p}\t{c}\t{det}\t{(d.get('courseName') or '-')}\")
"
}
export -f fetch_one
export P322DIR="$(pwd)"

printf 'path\tclase\tdetalle\tcourseName\n'
while read -r p; do
  P322PATH="$p" fetch_one "$p"
done < "$WORK/sample.txt"
