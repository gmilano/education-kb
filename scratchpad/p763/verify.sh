#!/bin/bash
# p763 licence byte-read. Payload written to a FILE and the FILE measured
# (p762 INS lesson: $(...) strips trailing newlines and corrupts length+sha).
PATHS="LICENSE LICENSE.md LICENSE.txt LICENSE.TXT license license.txt license.md LICENCE LICENCE.md LICENCE.txt COPYING COPYING.txt COPYING.md NOTICE LICENSE-APACHE LICENSE-MIT LICENSE.rst"
: > verified.tsv ; : > nopayload.tsv
PROBES=0
while IFS=$'\t' read -r REPO BR STARS; do
  [ -z "$REPO" ] && continue
  FOUND=""
  for P in $PATHS; do
    PROBES=$((PROBES+1))
    OUT="payload/$(echo "${REPO}_${BR}_${P}" | tr '/' '~')"
    CODE=$(curl -s -o "$OUT" -w '%{http_code}' --max-time 25 "https://raw.githubusercontent.com/${REPO}/${BR}/${P}")
    if [ "$CODE" = "200" ] && [ -s "$OUT" ]; then
      LEN=$(stat -c%s "$OUT")
      SHA=$(sha256sum "$OUT" | cut -c1-12)
      FIRST=$(head -c 400 "$OUT" | tr '\n\t' '  ' | sed 's/  */ /g' | cut -c1-110)
      printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$REPO" "$STARS" "$BR" "$P" "$LEN" "$SHA" "$FIRST" >> verified.tsv
      FOUND=1
      break
    else
      rm -f "$OUT"
    fi
  done
  if [ -z "$FOUND" ]; then
    printf '%s\t%s\t%s\tNO-PAYLOAD-AT-%s-PATHS\n' "$REPO" "$STARS" "$BR" "$(echo $PATHS | wc -w)" >> nopayload.tsv
  fi
done < cand.tsv
echo "PROBES=$PROBES"
echo "--- RESOLVED: $(wc -l < verified.tsv) ---"
column -t -s$'\t' verified.tsv | cut -c1-175
echo "--- NO PAYLOAD: $(wc -l < nopayload.tsv) ---"
cat nopayload.tsv
