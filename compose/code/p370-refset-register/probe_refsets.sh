#!/usr/bin/env bash
# p370 — the ONLINE half. One `git ls-remote` per register address, output kept verbatim
# under ./refsets/ so the offline fingerprint can be re-derived without the network.
# Usage: ./probe_refsets.sh <register.tsv> <outdir>
set -uo pipefail
reg="${1:?register tsv}"; out="${2:?outdir}"
mkdir -p "$out"
tail -n +2 "$reg" | awk -F'\t' 'NF>1{print $2}' | sort -fu | while read -r addr; do
  [ -z "$addr" ] && continue
  f="$out/$(echo "$addr" | tr '/' '%').refs"
  if [ -s "$f" ]; then continue; fi
  timeout 60 git ls-remote --symref "https://github.com/$addr" > "$f" 2>"$f.err"
  printf '%s\t%s\t%s\n' "$addr" "$?" "$(wc -l < "$f")"
done
