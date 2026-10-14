#!/bin/bash
# p197 -- segunda mitad de la lectura: las filas ABSENCE-ENUMERATED, por el canal de
# CABECERA DE FUENTE, con el instrumento de p139 (`headers.py`, 24 tests) SIN reescribirlo.
#
# Por que hace falta: `ABSENCE-ENUMERATED` dice «ningun FICHERO del arbol es un texto de
# concesion».  No dice «no hay concesion»: `P742` registra la concesion dentro del cuerpo de
# un fichero, y el mundo de los plugins de Moodle la pone en la cabecera de cada `.php` por
# convencion del propio proyecto.  Publicar esas filas como «sin licencia» seria el mismo
# error que una lista de nombres, un canal mas abajo.
#
# Clona a profundidad 1 CON blobs (son arboles chicos) y corre `p139/headers.py` sobre la
# raiz.  Salida: slug  text_files  with_grant  classes  strongest  vendored  verdict
set -u
HERE="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}" 2>/dev/null || printf '%s' "${BASH_SOURCE[0]}")")" && pwd)"
HEADERS="$HERE/../p139-source-header-grant/headers.py"
[ -f "$HEADERS" ] || { echo "FATAL: falta $HEADERS" >&2; exit 2; }
IN="${1:?lista}"; OUT="${2:?tsv}"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
printf 'slug\ttext_files\twith_grant\tclasses\tstrongest\tvendored\tverdict\n' > "$OUT"
n=0
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  n=$((n+1)); d="$WORK/r$n"
  if ! git clone --depth 1 -q "https://github.com/$slug" "$d" 2>/dev/null; then
    printf '%s\t-\t-\t-\t-\t-\tCLONE-FAILED\n' "$slug" >> "$OUT"
    printf '%-46s CLONE-FAILED\n' "$slug"; continue
  fi
  # `-I` aisla el interprete: el arbol clonado es dato ajeno y no debe poder sembrar un
  # modulo en el path de import.
  row="$(python3 -I "$HEADERS" "$d" 2>/dev/null)" || row=""
  if [ -z "$row" ]; then
    printf '%s\t-\t-\t-\t-\t-\tPROBE-FAILED\n' "$slug" >> "$OUT"
    printf '%-46s PROBE-FAILED\n' "$slug"; rm -rf "$d"; continue
  fi
  tf="$(printf '%s' "$row" | cut -f1)"; wg="$(printf '%s' "$row" | cut -f2)"
  cl="$(printf '%s' "$row" | cut -f3)"; st="$(printf '%s' "$row" | cut -f4)"
  vd="$(printf '%s' "$row" | cut -f5)"
  # El veredicto dice lo que SE MIDIO, no mas.  `headers.py` reconoce SPDX, linea de
  # copyright y las frases operativas de MIT/Apache/(A)GPL -- NO reconoce una declaracion
  # CC.  Y esta pasada tiene la prueba en el propio corpus: `xiaolai/the-craft-of-selfteaching`
  # declara CC-BY-NC-ND en su README y esta base lo sabe desde p854, con fixture.  Llamarlo
  # «sin concesion en ninguna parte» seria publicar el limite del instrumento como un hecho
  # del repositorio.
  case "$st" in
    NONE)                      verd=NO-HEADER-GRANT ;;
    SPDX|GRANT_*)              verd=HEADER-GRANT ;;
    COPYRIGHT)                 verd=NOTICE-ONLY ;;   # titularidad sin concesion operativa
    *)                         verd="$st" ;;
  esac
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$tf" "$wg" "$cl" "$st" "$vd" "$verd" >> "$OUT"
  printf '%-46s %5s ficheros %5s con concesion  %-28s %s\n' "$slug" "$tf" "$wg" "$cl" "$verd"
  rm -rf "$d"
done < "$IN"
echo "--- $OUT"
awk -F'\t' 'NR>1{v[$7]++} END{for(k in v) printf "%-22s %s\n", k, v[k]}' "$OUT"
