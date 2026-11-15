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
ptmp=$(mktemp -d)
trap 'rm -rf "$ptmp"' EXIT
gfile=-; gbytes=-; gsha=-
# p831 -- D9 BACKPORT.  `grantprobe.sh` was written at p773 precisely because a missing
# lowercase `license.txt` produced a false NO-GRANT-AT-ROOT on ERPNext.  The repair was
# applied there and NEVER backported to this sibling, which carried `license` and
# `license.md` but not `license.txt` -- so this probe reported NO-GRANT-AT-ROOT for
# `Kosudo/nextSIS` (GPL-3.0, 39,890 B) and `frappe/lms` (AGPL-3.0, 33,893 B), both of
# which ship exactly that filename.  The list below is now `grantprobe.sh`'s.
for f in LICENSE LICENSE.md LICENSE.txt LICENSE.rst LICENCE LICENCE.md LICENCE.txt \
         license license.md license.txt licence licence.txt License License.md License.txt \
         COPYING COPYING.txt COPYING.md copying copying.txt COPYRIGHT NOTICE \
         LICENSE-MIT LICENSE-APACHE LICENSE-APACHE-2.0 LICENSE.APACHE2 \
         MIT-LICENSE MIT-LICENSE.txt LICENSE.BSD docs/LICENSE .github/LICENSE; do
  u="https://raw.githubusercontent.com/$s/$br/$f"
  # p831 -- P834 REPAIR, and the census's own LOWER-BOUND disclaimer made concrete.
  # This site captured the body into `body`, sliced it into a SECOND variable
  # (`payload`), and measured THAT.  `p253-captured-body-census` reads shell source
  # lexically and states it "cannot see a body that reaches a measurement through a
  # second variable" -- so this genuinely CAPTURED-LIVE site graded BODY-ONLY and the
  # gate stayed quiet about it.  Both captures also lost the trailing-newline run, so
  # the bytes read short and the sha256 was unreproducible.  The payload now goes to a
  # FILE and the FILE is measured; the status comes back on its own channel.
  code=$(timeout 20 curl -sSL --max-time 20 -o "$ptmp/payload" \
         -w '%{http_code}' "$u" 2>/dev/null)
  if [ "$code" = "200" ]; then
    gbytes=$(wc -c < "$ptmp/payload" | tr -d ' ')
    gsha=$(sha256sum "$ptmp/payload" | cut -c1-12)
    gfile="$f"; break
  fi
done
[ "$gfile" = "-" ] && gfile=NO-GRANT-AT-ROOT
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$s" "$st" "$br" "${hd:0:12}" "$gfile" "$gbytes" "$gsha"
