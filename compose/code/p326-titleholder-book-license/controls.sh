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
# `ACTION XY` (p253): este control publicaba bytes Y sha256 DESDE LA CAPTURA, que es `P834`.
# Medido: `osbooks-calculus-bundle` daba 21443 / ced5bed6eec9c127 cuando el payload es
# 21444 B / 61288b08584b5130 — y la corrida final de saltos de linea es 1 en ese payload y
# 0 en los otros dos, que es exactamente por que dos de tres coincidian. Ahora se imprimen
# AMBOS canales, etiquetados, porque la pregunta de este control es la diferencia misma.
for r in osbooks-calculus-bundle osbooks-college-algebra-bundle osbooks-prealgebra-bundle; do
  __f=$(mktemp)
  curl -sS --max-time 25 -o "$__f" "$RAW/openstax/$r/main/LICENSE" 2>/dev/null
  f=$(cat "$__f")
  printf '  %-34s FILED bytes=%s sha256=%s | CAPTURED bytes=%s sha256=%s | trailing=%s\n' \
    "$r" \
    "$(wc -c < "$__f" | tr -d ' ')" "$(sha256sum "$__f" | cut -c1-16)" \
    "$(printf '%s' "$f" | wc -c | tr -d ' ')" "$(printf '%s' "$f" | sha256sum | cut -c1-16)" \
    "$(( $(wc -c < "$__f" | tr -d ' ') - $(printf '%s' "$f" | wc -c | tr -d ' ') ))"
  rm -f "$__f"
done
