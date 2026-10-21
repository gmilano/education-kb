#!/usr/bin/env bash
# `ACTION ZZ-bo`, online leg.  One platform row per invocation, so the driver can be
# parallelised and a single failure cannot poison the sweep.
#
# 🔴 The README ladder is CASE-CLOSED and EXTENSION-CLOSED (`gate-ladder-case`, p283):
# stem case, extension case AND the non-markdown spellings that real platforms ship.
# Moodle's own anchor is `README.txt`; a `README.md`-only ladder would have reported
# this base's largest platform row as having no README at all.
set -uo pipefail
slug="$1"; out="$2"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LADDER=(README.md README.MD Readme.md readme.md README.rst README.txt README readme README.markdown docs/README.md)

ref="$(timeout 60 git ls-remote --symref "https://github.com/${slug}" HEAD 2>/dev/null \
      | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')"
if [[ -z "$ref" ]]; then
  printf '%s\tNO-REF\t-\t0\t-\t-\t-\n' "$slug" >> "$out"; exit 0
fi

tmp="$(mktemp)"; found_path=""; bytes=0
for rung in "${LADDER[@]}"; do
  code="$(timeout 60 curl -sS -L -o "$tmp" -w '%{http_code}' \
          "https://raw.githubusercontent.com/${slug}/${ref}/${rung}" 2>/dev/null)"
  if [[ "$code" == "200" ]]; then
    found_path="$rung"; bytes="$(wc -c < "$tmp" | tr -d ' ')"; break
  fi
done
if [[ -z "$found_path" ]]; then
  printf '%s\t%s\tNO-README\t0\t0\t0\t0\n' "$slug" "$ref" >> "$out"; rm -f "$tmp"; exit 0
fi

mapfile -t comps < <(python3 -I "${HERE}/companion_closure.py" --self "$slug" --readme "$tmp" 2>/dev/null)
same=0; third=0
for line in "${comps[@]}"; do
  [[ "$line" == *$'\t'SAME-OWNER ]] && same=$((same+1))
  [[ "$line" == *$'\t'THIRD-PARTY ]] && third=$((third+1))
  printf '%s\t%s\n' "$slug" "$line" >> "${out}.companions"
done
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "$slug" "$ref" "$found_path" "$bytes" "${#comps[@]}" "$same" "$third" >> "$out"
rm -f "$tmp"
