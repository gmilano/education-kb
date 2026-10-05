#!/usr/bin/env bash
# Action C (pass 109): P339 tie-breaker. Measure, IN THE SAME ACT:
#   bytes(full), sha256(full), sha256(full minus last byte)
# A published fingerprint equal to the minus-last-byte sha is the P333 signature (instrument defect).
# A published fingerprint equal to the full sha, while the byte count differs by 1, is P327 (file property).
printf 'repo\tpath\tcode\tbytes\tsha_full\tsha_minus1\tlast_byte\n'
while IFS=$'\t' read -r repo path; do
  [ -z "$repo" ] && continue
  url="https://raw.githubusercontent.com/$repo/$path"
  code=$(curl -sS -o /tmp/acq -w '%{http_code}' --max-time 25 "$url" 2>/dev/null || echo 000)
  if [ "$code" != "200" ]; then printf '%s\t%s\t%s\t-\t-\t-\t-\n' "$repo" "$path" "$code"; continue; fi
  b=$(wc -c < /tmp/acq)
  sf=$(sha256sum < /tmp/acq | cut -d' ' -f1 | cut -c1-12)
  head -c $((b-1)) /tmp/acq > /tmp/acq1
  sm=$(sha256sum < /tmp/acq1 | cut -d' ' -f1 | cut -c1-12)
  lb=$(tail -c 1 /tmp/acq | od -An -tx1 | tr -d ' \n')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$path" "$code" "$b" "$sf" "$sm" "$lb"
done
