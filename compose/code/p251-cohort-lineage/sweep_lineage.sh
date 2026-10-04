#!/bin/sh
# P251 — topologia de un cohorte por TRES canales independientes, no por la ausencia
# de menciones en el indice propio.
#
# Canal de verificacion: raw.githubusercontent.com con ref literal `HEAD` (P170),
# CALIBRADO antes de usarse (P249). Si la calibracion falla el barrido NO corre:
# un 403 uniforme no es el estado de los repos, es el estado del canal (P247).
#
# Emite TSV: slug  lic_code  lic_bytes  lic_sha16  holder  pkg_name  pkg_repo  cites
#
# Uso:  sh sweep_lineage.sh [archivo-de-slugs]
set -u
RAW="https://raw.githubusercontent.com"
IN="${1:-slugs.input.txt}"

# --- compuerta de calibracion (P249): una URL buena Y una inexistente ---
GOOD="$RAW/r-huijts/canvas-mcp/HEAD/LICENSE"
BAD="$RAW/r-huijts/canvas-mcp-does-not-exist-xyz999/HEAD/LICENSE"
cg=$(curl -s -o /dev/null -w '%{http_code}' "$GOOD" 2>/dev/null)
cb=$(curl -s -o /dev/null -w '%{http_code}' "$BAD" 2>/dev/null)
if [ "$cg" != "200" ] || [ "$cb" != "404" ]; then
  echo "UNCALIBRATED-NO-DISCRIMINATION good=$cg bad=$cb — no se corre el barrido (P249)" >&2
  exit 3
fi
echo "# canal CALIBRADO: good=$cg bad=$cb" >&2

printf 'slug\tlic_code\tlic_bytes\tlic_sha16\tholder\tpkg_name\tpkg_repo\tcites\n'
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  case "$slug" in \#*) continue ;; esac
  tmp=$(mktemp)
  code=$(curl -s -o "$tmp" -w '%{http_code}' "$RAW/$slug/HEAD/LICENSE" 2>/dev/null)
  if [ "$code" = "200" ]; then
    bytes=$(wc -c <"$tmp" | tr -d ' ')
    sha=$(sha256sum "$tmp" | cut -c1-16)
    holder=$(grep -i -m1 'copyright' "$tmp" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//' | tr '\t' ' ')
    [ -z "$holder" ] && holder='-'
  else
    bytes=0; sha='-'; holder='-'
  fi
  rm -f "$tmp"

  pj=$(curl -s "$RAW/$slug/HEAD/package.json" 2>/dev/null)
  pname=$(printf '%s' "$pj" | grep -m1 '"name"' | sed 's/.*:[[:space:]]*"//; s/".*//')
  [ -z "$pname" ] && pname='-'
  prepo=$(printf '%s' "$pj" | grep -m1 -o 'github\.com[/:][A-Za-z0-9_.-]*/[A-Za-z0-9_.-]*' | head -1 | sed 's|github\.com[/:]||; s|\.git$||')
  [ -z "$prepo" ] && prepo='-'

  rd=$(curl -s "$RAW/$slug/HEAD/README.md" 2>/dev/null)
  cites=$(printf '%s' "$rd" | grep -o -i -E 'r-huijts|vishalsachdev|bruchris' | tr 'A-Z' 'a-z' | sort -u | paste -sd, - )
  [ -z "$cites" ] && cites='-'

  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$code" "$bytes" "$sha" "$holder" "$pname" "$prepo" "$cites"
done < "$IN"
