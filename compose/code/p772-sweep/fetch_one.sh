#!/bin/bash
# p772 — fetch ONE grant payload. D9 fix: the previous version used ${slug//\//~}
# whose "~" was TILDE-EXPANDED to /root, so every output path pointed into a
# non-existent directory and every 200 response was silently discarded.
slug="$1"; br="$2"
safe=$(printf '%s' "$slug" | tr '/' '_')
out="payloads/$safe"
[ -s "$out.body" ] && exit 0
for name in LICENSE LICENSE.txt LICENSE.md COPYING LICENCE LICENSE.rst license COPYING.txt LICENSE-MIT LICENSE-APACHE; do
  code=$(curl -s -o "$out.tmp" -w '%{http_code}' --max-time 20 \
         "https://raw.githubusercontent.com/$slug/$br/$name")
  if [ "$code" = "200" ] && [ -s "$out.tmp" ]; then
    mv "$out.tmp" "$out.body"; printf '%s\n' "$name" > "$out.name"; exit 0
  fi
done
rm -f "$out.tmp"; printf 'NONE\n' > "$out.name"
