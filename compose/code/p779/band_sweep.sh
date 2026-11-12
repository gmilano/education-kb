#!/bin/bash
# p779 instrument (p778-B): measure the licence-grant BYTE LENGTH of every
# shelved repository graded Apache-2.0, on the raw channel at the default branch
# (raw accepts the literal ref `HEAD`).  Emits: slug, filename, http, bytes.
# A 404 on every candidate filename is emitted as NOFILE so an absence is a
# measurement and not a silent gap.
probe() {
  slug="$1"
  for f in LICENSE LICENSE.txt LICENSE.md LICENCE COPYING LICENSE-APACHE; do
    out=$(timeout 25 curl -sSI "https://raw.githubusercontent.com/$slug/HEAD/$f" 2>/dev/null \
      | awk 'BEGIN{c=0;l=0} /^HTTP/{c=$2} tolower($0)~/^content-length:/{gsub("\r","");l=$2} END{print c" "l}')
    code=${out% *}; len=${out#* }
    if [ "$code" = "200" ]; then printf "%s\t%s\t200\t%s\n" "$slug" "$f" "$len"; return; fi
  done
  printf "%s\t-\tNOFILE\t0\n" "$slug"
}
export -f probe
cut -f1 "$1" | xargs -P 10 -I{} bash -c 'probe "$@"' _ {}
