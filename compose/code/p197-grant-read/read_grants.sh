#!/bin/bash
# p197 -- lee la CONCESION DESDE LOS BYTES para una lista de slugs, por el canal de arbol.
#
# Responde tres acciones pre-registradas por p196 con UN solo instrumento:
#   * las 3 filas OWN-GRANT-AT-ROOT que p196 encontro y NO leyo;
#   * las filas del padron que ningun censo alcanzo nunca;
#   * las filas nuevas del canal MCP, que no se publican sin concesion leida.
#
# Canal (P441, el unico que distingue «no hay concesion» de «no hay concesion DONDE MIRE»):
#   git clone --filter=blob:none --no-checkout --depth 1   # commit + arboles, sin blobs
#   git ls-tree -r --name-only HEAD                        # arbol COMPLETO, sin paginar
#   git cat-file -p HEAD:<ruta> > fichero                  # el blob, traido a demanda
#
# Reglas que NO se reescriben aqui:
#   `lib/licence_path.sh`   -- que ruta es una concesion y cual esta vendorizada (p196)
#   `lib/license_family.sh` -- que familia es un payload (P171, P551, P560, P845, T232...)
#   `lib/payload_measure.sh`-- los bytes se miden DE UN FICHERO, nunca de `$(...)` (P834)
set -u
HERE="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}" 2>/dev/null || printf '%s' "${BASH_SOURCE[0]}")")" && pwd)"
LIB="$HERE/../lib"
. "$LIB/licence_path.sh"    || { echo "FATAL: licence_path.sh"    >&2; exit 2; }
. "$LIB/license_family.sh"  || { echo "FATAL: license_family.sh"  >&2; exit 2; }
. "$LIB/payload_measure.sh" || { echo "FATAL: payload_measure.sh" >&2; exit 2; }
for f in is_licence_path is_bundled family_of size_of_file; do
  declare -F "$f" >/dev/null 2>&1 || { echo "FATAL: $f no definida" >&2; exit 2; }
done

IN="${1:?lista de slugs}"; OUT="${2:?tsv de salida}"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
printf 'slug\texists\tpaths_in_tree\tscope\tlicence_path\tbytes\tfamily\tverdict\n' > "$OUT"

n=0
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  case "$slug" in \#*) continue ;; esac
  n=$((n+1)); d="$WORK/r$n"

  # 1. EXISTENCIA primero, y por su propio canal: un repo que no esta no es un repo sin
  #    concesion.  Los dos estados se publican distintos o el censo miente en el agregado.
  #
  # 🔴 Y SON TRES ESTADOS, NO DOS.  La v1 de este instrumento usaba `ls-remote --exit-code -h`
  # y leia su `2` ("ninguna ref coincide") como ABSENT: dos filas de este estante
  # --`cdweaver1992/edfi-mcp-server` y `openfresno/edgenuity-aeries-grade-passback`-- son
  # repositorios que EXISTEN y estan VACIOS.  El canal de p107 (`--heads --tags` sin
  # `--exit-code`) las daba alcanzables con 0 heads y 0 tags, y los dos canales se
  # contradecian sobre dos filas por una diferencia de BANDERA, no de mundo.  Un repo
  # ausente contesta `128` (git pide credenciales); uno vacio contesta `0` sin refs.
  refs="$(GIT_TERMINAL_PROMPT=0 timeout 60 git ls-remote --heads --tags "https://github.com/$slug" 2>/dev/null)"; rc=$?
  if [ "$rc" -ne 0 ]; then
    printf '%s\tNO\t-\t-\t-\t-\t-\tABSENT\n' "$slug" >> "$OUT"
    printf '%-58s ABSENT (rc=%s)\n' "$slug" "$rc"; continue
  fi
  if [ -z "$refs" ]; then
    printf '%s\tEMPTY\t0\t-\t-\t-\t-\tEMPTY-REPO\n' "$slug" >> "$OUT"
    printf '%-58s EMPTY-REPO (existe, sin refs)\n' "$slug"; continue
  fi
  if ! git clone --filter=blob:none --no-checkout --depth 1 -q \
        "https://github.com/$slug" "$d" 2>/dev/null; then
    printf '%s\tYES\t-\t-\t-\t-\t-\tCLONE-FAILED\n' "$slug" >> "$OUT"
    printf '%-58s CLONE-FAILED\n' "$slug"; continue
  fi
  tree="$d/.tree"; git -C "$d" ls-tree -r --name-only HEAD > "$tree" 2>/dev/null || : > "$tree"
  np=$(wc -l < "$tree" | tr -d ' ')

  # 2. Las rutas de concesion del arbol COMPLETO, separadas en raiz / subarbol / vendorizada.
  root=""; sub=""; bun=""
  while IFS= read -r path; do
    [ -z "$path" ] && continue
    is_licence_path "$path" || continue
    if is_bundled "$path"; then bun="$bun$path"$'\n'
    elif [ "$path" = "$(basename "$path")" ]; then root="$root$path"$'\n'
    else sub="$sub$path"$'\n'; fi
  done < "$tree"

  pick=""; scope=""
  if [ -n "$root" ]; then pick="$(printf '%s' "$root" | head -1)"; scope=ROOT
  elif [ -n "$sub" ]; then pick="$(printf '%s' "$sub" | head -1)"; scope=SUBTREE
  elif [ -n "$bun" ]; then pick="$(printf '%s' "$bun" | head -1)"; scope=BUNDLED
  else
    printf '%s\tYES\t%s\tNONE\t-\t0\t-\tABSENCE-ENUMERATED\n' "$slug" "$np" >> "$OUT"
    printf '%-58s ABSENCE-ENUMERATED (%s rutas)\n' "$slug" "$np"; continue
  fi

  # 3. Los BYTES.  A fichero, y medidos del fichero (P834).
  blob="$d/.payload"
  if ! git -C "$d" cat-file -p "HEAD:$pick" > "$blob" 2>/dev/null; then
    printf '%s\tYES\t%s\t%s\t%s\t-\t-\tBLOB-UNREACHABLE\n' "$slug" "$np" "$scope" "$pick" >> "$OUT"
    printf '%-58s BLOB-UNREACHABLE %s\n' "$slug" "$pick"; continue
  fi
  bytes="$(size_of_file "$blob")"
  fam="$(family_of "$(cat "$blob")")"
  # Un payload por debajo del umbral de `Gap 421` no es una concesion aunque se llame LICENSE:
  # se marca, no se descarta, y el numero viaja con la fila.
  verd=READ
  [ "$bytes" -lt 400 ] && verd=SHORT-PAYLOAD
  [ "$fam" = "UNCLASSIFIED" ] && verd=UNCLASSIFIED
  printf '%s\tYES\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$np" "$scope" "$pick" "$bytes" "$fam" "$verd" >> "$OUT"
  printf '%-58s %-8s %-22s %8s B  %s\n' "$slug" "$scope" "$fam" "$bytes" "$verd"
  rm -rf "$d"
done < "$IN"

echo "--- $OUT"
awk -F'\t' 'NR>1{v[$8]++} END{for(k in v) printf "%-22s %s\n", k, v[k]}' "$OUT"
