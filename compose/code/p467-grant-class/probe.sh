#!/bin/bash
# p467 -- first-hand payload probe. Two channels only, per p450/p465:
#   git ls-remote --symref   -> tree identity (HEAD sha) + default branch
#   raw.githubusercontent    -> payload BYTES, captured with curl -o (never
#                               through command substitution, per Gap 465-A)
# The probe the ingest brief prescribes -- curl -sI https://github.com/<addr> --
# returns 403 for a live AND a nonexistent address from this host and is not
# used anywhere.
set -u
addr="$1"; out="$2"
mkdir -p "$out/$addr"
if ! timeout 45 git ls-remote --symref "https://github.com/$addr" HEAD > "$out/$addr/ref.txt" 2>"$out/$addr/ref.err"; then
  echo -e "$addr\tUNRESOLVED\t\t\t" ; exit 0
fi
br=$(sed -n 's#^ref: refs/heads/\(.*\)\tHEAD$#\1#p' "$out/$addr/ref.txt" | head -1)
head=$(awk '$1 ~ /^[0-9a-f]{40}$/ {print substr($1,1,12); exit}' "$out/$addr/ref.txt")
[ -z "$br" ] && br=main
for p in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.md LICENSE.rst license License.md; do
  code=$(timeout 40 curl -s -o "$out/$addr/payload" -w "%{http_code}" \
         "https://raw.githubusercontent.com/$addr/$br/$p" 2>/dev/null)
  if [ "$code" = "200" ] && [ -s "$out/$addr/payload" ]; then
    b=$(wc -c < "$out/$addr/payload" | tr -d ' ')
    d=$(sha256sum "$out/$addr/payload" | cut -c1-12)
    echo -e "$addr\t$head\t$br\t$p\t$b\t$d"; exit 0
  fi
done
rm -f "$out/$addr/payload"
echo -e "$addr\t$head\t$br\tNO-ROOT-GRANT\t0\t"
