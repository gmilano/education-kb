#!/bin/bash
# p773 probe -- written from scratch. Ref channel (git ls-remote) + grant payload
# read on the raw channel. api.github.com is not called for any verdict.
export GIT_TERMINAL_PROMPT=0
s="$1"
out=$(timeout 25 git ls-remote --symref "https://github.com/$s" 2>&1)
rc=$?
nrefs=$(printf '%s\n' "$out" | grep -cE '^[0-9a-f]{40}\s')
sym=$(printf '%s\n' "$out" | awk '/^ref:/{print $2; exit}')
hd=$(printf '%s\n' "$out" | grep -oE '^[0-9a-f]{40}[[:space:]]+HEAD$' | awk '{print $1}')
if [ -n "$hd" ]; then
  st=RESOLVES
elif [ $rc -eq 124 ]; then
  st=TIMEOUT; printf '%s\t%s\t-\t-\t-\t-\t-\n' "$s" "$st"; exit 0
elif [ "$nrefs" = "0" ] && printf '%s' "$out" | grep -qi "could not read Username\|Authentication failed\|not found"; then
  st=ABSENT-OR-PRIVATE; printf '%s\t%s\t-\t-\t-\t-\t-\n' "$s" "$st"; exit 0
elif [ "$nrefs" = "0" ]; then
  st=EXISTS-BUT-EMPTY; printf '%s\t%s\t-\t-\t-\t-\t-\n' "$s" "$st"; exit 0
else
  st=OTHER; printf '%s\t%s\t-\t-\t-\t-\t-\n' "$s" "$st"; exit 0
fi
br="${sym#refs/heads/}"; [ -z "$br" ] && br=HEAD
# p772-C: WIDER filename list + LICENSE-* globbing, graded NO-GRANT-AT-ROOT
gfile=-; gbytes=-; gsha=-
for f in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt \
         LICENSE-MIT LICENSE-APACHE LICENSE-APACHE-2.0 license license.md \
         LICENSE.rst COPYRIGHT NOTICE; do
  u="https://raw.githubusercontent.com/$s/$br/$f"
  body=$(timeout 20 curl -sSL --max-time 20 -w '\n%{http_code}' "$u" 2>/dev/null)
  code=$(printf '%s' "$body" | tail -n1)
  if [ "$code" = "200" ]; then
    payload=$(printf '%s' "$body" | sed '$d')
    gbytes=$(printf '%s' "$payload" | wc -c | tr -d ' ')
    gsha=$(printf '%s' "$payload" | sha256sum | cut -c1-12)
    gfile="$f"; break
  fi
done
[ "$gfile" = "-" ] && gfile=NO-GRANT-AT-ROOT
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$s" "$st" "$br" "${hd:0:12}" "$gfile" "$gbytes" "$gsha"
