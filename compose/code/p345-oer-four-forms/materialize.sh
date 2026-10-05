#!/usr/bin/env bash
# Accion C del pase 110. Materializa `CAHLR/OATutor-Content` en LOTES, guardando
# el parcial de cada lote, para que un limite de tiempo deje una muestra
# ACUMULABLE en vez de perder la corrida (la deuda de los pases 108 y 109).
# Canal: `git cat-file --batch` sobre el clon sin blobs — un solo proceso para
# todo el lote, que es lo que lo hace terminar.
set -euo pipefail
REPO=${1:?repo}
OUT=${2:?outdir}
LOTE=${3:-2000}
mkdir -p "$OUT"
cd "$REPO"
SHA=$(git rev-parse HEAD)
echo "$SHA" > "$OUT/sha.txt"

# unidades = los JSON de problema de primer nivel: content-pool/<id>/<id>.json
git ls-tree -r -z --name-only HEAD | tr '\0' '\n' \
  | grep -E '^content-pool/[^/]+/[^/]+\.json$' \
  | awk -F/ '$2 == substr($3,1,length($3)-5)' > "$OUT/unidades.txt"
TOT=$(wc -l < "$OUT/unidades.txt" | tr -d ' ')
echo "unidades=$TOT lote=$LOTE sha=$SHA" >&2

i=0; lote=0
while [ "$i" -lt "$TOT" ]; do
  lote=$((lote+1))
  part="$OUT/lote-$(printf '%03d' $lote).tsv"
  if [ -s "$part" ]; then i=$((i+LOTE)); continue; fi   # ya hecho: acumulable
  sed -n "$((i+1)),$((i+LOTE))p" "$OUT/unidades.txt" > "$OUT/.batch"
  # un unico cat-file para todo el lote
  while read -r p; do printf 'HEAD:%s\n' "$p"; done < "$OUT/.batch" \
    | git cat-file --batch 2>/dev/null \
    | python3 -c '
import sys, json, re
data = sys.stdin.buffer.read()
# formato --batch: "<sha> <type> <size>\n<payload>\n"
pos = 0
rows = []
while pos < len(data):
    nl = data.find(b"\n", pos)
    if nl < 0: break
    hdr = data[pos:nl].decode("utf-8", "replace").split()
    if len(hdr) < 3:
        pos = nl + 1; continue
    size = int(hdr[2]); start = nl + 1
    payload = data[start:start+size]
    pos = start + size + 1
    try:
        o = json.loads(payload.decode("utf-8", "replace"))
    except Exception:
        rows.append(("?", "", "", "", "JSON-INVALIDO")); continue
    rows.append((o.get("id",""), o.get("oer","") or "", o.get("license","") or "",
                 o.get("courseName","") or "", "OK"))
for r in rows:
    print("\t".join(x.replace("\t"," ").replace("\n"," ") for x in r))
' > "$part"
  echo "lote $lote -> $(wc -l < "$part" | tr -d ' ') filas" >&2
  i=$((i+LOTE))
done
rm -f "$OUT/.batch"
cat "$OUT"/lote-*.tsv > "$OUT/unidades-oer.tsv"
echo "total filas: $(wc -l < "$OUT/unidades-oer.tsv" | tr -d ' ')" >&2
