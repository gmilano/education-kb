#!/bin/bash
# P322 — barrido del campo `license` POR ITEM, paralelo, para tasa POR CURSO.
#
# DOS defectos que este script tuvo en su primera version del pase 104, y los controles
# que ahora los impiden (ambos de la familia P171/P319: el instrumento reporta un estado
# que no midio):
#
#   E1 COMILLA EN LA RUTA.  `xargs -I{}` procesa comillas por defecto, asi que
#      `content-pool/a343428l'hopital2/...` (la regla de L'Hopital) llegaba al curl SIN
#      la comilla -> 404 -> y el cuerpo «404: Not Found» entraba al clasificador como si
#      fuera el item.  Se arregla con `-d '\n'` (sin procesamiento de comillas).
#      Control: C11 en test_classify.py.
#   E2 EL CODIGO HTTP NO SE MIRABA.  `curl -s` sin comprobar el status entrega el cuerpo
#      de error como si fuera payload.  Sobrevivio de CASUALIDAD: «404: Not Found» no
#      parsea como JSON.  Un 404 que devolviera JSON se habria publicado como dato.
#      Ahora el status se exige 200 y una ruta irrecuperable sale como NO-LEIDA, que es
#      un estado del CANAL y NO una clase de licencia: no se mezcla en la tasa.
set -u
WORK="${WORK:-/tmp/t322}"; STEP="${STEP:-11}"; PAR="${PAR:-12}"
RAW="https://raw.githubusercontent.com/CAHLR/OATutor-Content/HEAD"
export RAW P322DIR="$(pwd)"
git -C "$WORK" ls-tree -r --name-only HEAD | grep -E '^content-pool/[^/]+/[^/]+\.json$' | sort > "$WORK/all_items.txt"
awk -v s="$STEP" 'NR%s==1' "$WORK/all_items.txt" > "$WORK/sample_p.txt"

one(){
  p="$1"
  out=$(curl -s --max-time 30 -w $'\n%{http_code}' "$RAW/$p")
  code=$(printf '%s' "$out" | tail -1)
  body=$(printf '%s' "$out" | sed '$d')
  if [ "$code" != "200" ]; then
    printf '%s\tNO-LEIDA\thttp=%s\t-\n' "$p" "$code"; return
  fi
  printf '%s' "$body" | P322PATH="$p" python3 -c "
import sys,json,os,re
sys.path.insert(0,os.environ['P322DIR'])
from classify_item import classify
p=os.environ['P322PATH']
def flat(s):  # ninguna celda puede traer tab ni newline: romperia el TSV
    return re.sub(r'[\t\r\n]+',' ',str(s))[:90]
try: d=json.load(sys.stdin)
except Exception: print(f'{p}\tPARSE-FAIL\t-\t-'); raise SystemExit
c,det=classify(d)
print(f\"{p}\t{c}\t{flat(det)}\t{flat(d.get('courseName') or '-')}\")
"
}
export -f one
printf 'path\tclase\tdetalle\tcourseName\n'
# -d '\n' desactiva el procesamiento de comillas de xargs: es el arreglo de E1.
xargs -a "$WORK/sample_p.txt" -d '\n' -I{} -P "$PAR" bash -c 'one "$1"' _ {}
