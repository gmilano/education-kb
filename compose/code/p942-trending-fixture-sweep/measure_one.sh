#!/usr/bin/env bash
# p942 item A - measure every grant payload a slug serves, on the ladder that
# p941's branch census showed is actually needed (main is NOT a safe single probe:
# it was wrong about 60 of 275 shelf rows).
#
# For each 200 on the ladder, emit:
#   slug  branch  path  raw_bytes  raw_sha12  stripped_bytes  stripped_sha12
# "stripped" = trailing newlines removed, which is the defect signature p940/p941
# identified: a fixture computed over a stripped payload cannot be reproduced by a
# reader who fetches the file as served.
set -u
slug="$1"
tmp=$(mktemp)
for br in main master; do
  for path in LICENSE LICENSE.md LICENSE.txt COPYING; do
    code=$(curl -sS -o "$tmp" -w '%{http_code}' --max-time 25 \
      "https://raw.githubusercontent.com/${slug}/${br}/${path}" 2>/dev/null || echo 000)
    if [ "$code" = "200" ]; then
      rb=$(wc -c < "$tmp" | tr -d ' ')
      rs=$(sha256sum "$tmp" | cut -c1-12)
      sb=$(printf '%s' "$(cat "$tmp")" | wc -c | tr -d ' ')
      ss=$(printf '%s' "$(cat "$tmp")" | sha256sum | cut -c1-12)
      printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$path" "$rb" "$rs" "$sb" "$ss"
    fi
  done
done
rm -f "$tmp"
