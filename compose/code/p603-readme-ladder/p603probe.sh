#!/usr/bin/env bash
# p603 grant probe. The base's compose/code/lib/probe_payload.sh could NOT be sourced this
# pass (the harness denied executing code from the cloned repo), so this is an independent
# implementation that honours the four defects that library documents, by name:
#   D1 default branch is NOT main/master -> resolved with ls-remote --symref, never assumed
#   D2 payload can sit in a mixed-case subdirectory -> README licence LINK tried
#   D3 British spelling LICENCE is a real payout (1 in 44)
#   D4 family is decided from the TITLE LINE only. GPL-3.0 s6 contains "noncommercially"
#      and GPL-3.0 s13 is titled "Use with the GNU Affero GPL": body-keyword matching
#      mis-reads GPL-3.0 as NonCommercial / AGPL. Title anchoring is the fix.
slug="$1"
raw() { curl -sS --max-time 20 "https://raw.githubusercontent.com/$slug/$1/$2" 2>/dev/null; }
br=$(timeout 30 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null \
      | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
if [ -z "$br" ]; then printf '%s\t-\tUNRESOLVED\t0\tUNRESOLVED\n' "$slug"; return 2>/dev/null || exit 0; fi
body=""; found=""
for f in LICENSE LICENSE.md LICENSE.txt COPYING LICENCE LICENSE-MIT COPYING.txt license license.txt LICENSE.rst; do
  b=$(raw "$br" "$f"); case "$b" in ""|*"404: Not Found"*) ;; *) body="$b"; found="$f"; break;; esac
done
if [ -z "$found" ]; then            # D2: README's own licence link
  rd=$(raw "$br" README.md)
  p=$(printf '%s' "$rd" | grep -oiE '\[[^]]*licen[sc]e[^]]*\]\(([^)]+)\)' | head -1 | sed 's/.*(\(.*\))/\1/')
  if [ -n "$p" ]; then case "$p" in http*) ;; *) b=$(raw "$br" "${p#./}")
      case "$b" in ""|*"404: Not Found"*) ;; *) body="$b"; found="$p";; esac;; esac; fi
fi
[ -z "$found" ] && { printf '%s\t%s\tNO-PAYLOAD\t0\tNO-PAYLOAD\n' "$slug" "$br"; exit 0; }
bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
T=$(printf '%s' "$body" | grep -viE '^[[:space:]]*(copyright|\(c\)|all rights)' \
     | grep -vE '^[[:space:]]*$' | head -5 | tr '\n' ' ' | tr -s ' ')
fam=OTHER                                      # D4: title-anchored only
case "$T" in
  *"GNU AFFERO GENERAL PUBLIC LICENSE"*|*"GNU Affero General Public License"*) fam="AGPL-3.0";;
  *"GNU LESSER GENERAL PUBLIC LICENSE"*|*"GNU Lesser General Public License"*) fam="LGPL";;
  *"GNU GENERAL PUBLIC LICENSE"*|*"GNU General Public License"*)
      case "$T" in *"Version 2"*|*"version 2"*) fam="GPL-2.0";; *) fam="GPL-3.0";; esac;;
  *"MIT License"*|*"MIT Licence"*|*"The MIT License"*) fam="MIT";;
  *"Apache License"*) case "$T" in *2.0*) fam="Apache-2.0";; *) fam="Apache";; esac;;
  *"BSD "*|*"Redistribution and use in source and binary"*) fam="BSD";;
  *"Mozilla Public License"*) fam="MPL-2.0";;
  *"Creative Commons"*|*"CC0 "*) fam="CC";;
  *"ISC License"*) fam="ISC";;
  *"Unlicense"*|*"unlicense"*) fam="Unlicense";;
  *"Eclipse Public License"*) fam="EPL";;
esac
printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$found" "$bytes" "$fam"
