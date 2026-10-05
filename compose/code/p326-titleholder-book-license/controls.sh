#!/usr/bin/env bash
# Controles del instrumento p326. Un barrido que SOLO sabe decir "CC BY-NC-SA" no mide nada.
set -u
RAW="https://raw.githubusercontent.com"
echo "--- C1: collection inventado en repo REAL -> debe ser NO-ALCANZABLE (404) ---"
curl -sS -o /dev/null -w 'calculus-volume-99: %{http_code}\n' --max-time 25 \
  "$RAW/openstax/osbooks-calculus-bundle/main/collections/calculus-volume-99.collection.xml"
echo "--- C2: repo inventado -> 404 ---"
curl -sS -o /dev/null -w 'osbooks-inventado-999: %{http_code}\n' --max-time 25 \
  "$RAW/openstax/osbooks-inventado-999/main/META-INF/books.xml"
echo "--- C3: el clasificador PUEDE devolver algo distinto de CC BY-NC-SA ---"
for t in "openstax/openstax-cms/main/LICENSE" "openstax/os-webview/main/LICENSE"; do
  h=$(curl -sS --max-time 25 "$RAW/$t" 2>/dev/null | head -1 | tr -d '\r')
  printf '%-40s primera linea: %s\n' "$t" "${h:0:60}"
done
echo "--- C4: main vs master vs HEAD deben dar el MISMO payload (sha256 del collection) ---"
for b in main master HEAD; do
  s=$(curl -sS --max-time 25 "$RAW/openstax/osbooks-calculus-bundle/$b/collections/calculus-volume-1.collection.xml" 2>/dev/null | sha256sum | cut -c1-16)
  printf '  %-6s %s\n' "$b" "$s"
done
echo "--- C5: por que tres conteos de bytes distintos para la MISMA familia ---"
for r in osbooks-calculus-bundle osbooks-college-algebra-bundle osbooks-prealgebra-bundle; do
  f=$(curl -sS --max-time 25 "$RAW/openstax/$r/main/LICENSE" 2>/dev/null)
  printf '  %-34s bytes=%s lineas=%s sha256=%s\n' "$r" "$(printf '%s' "$f" | wc -c | tr -d ' ')" "$(printf '%s' "$f" | wc -l | tr -d ' ')" "$(printf '%s' "$f" | sha256sum | cut -c1-16)"
done
