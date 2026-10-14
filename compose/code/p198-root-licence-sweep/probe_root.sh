#!/bin/bash
# Stage A: filename list over the raw lane.  Sound for a POSITIVE (bytes in hand);
# NOT sound for a NEGATIVE -- that is what Stage B (tree enumeration) is for.
SP="$1"; set -u
NAMES="LICENSE LICENSE.txt LICENSE.TXT LICENSE.md LICENSE.rst License License.txt license license.txt LICENCE LICENCE.md COPYING COPYING.txt COPYING.md LICENSE-2.0.txt LICENSE.GPL UNLICENSE"
printf "slug\tbranch\tpath\thttp\tfamily\tgrant\tbytes\n"
while read -r slug; do
  [ -z "$slug" ] && continue
  br=""
  for cand in main master develop; do
    if curl -s -o /dev/null --max-time 20 -w '' "https://raw.githubusercontent.com/$slug/$cand/README.md" 2>/dev/null; then :; fi
  done
  # resolve the real default branch from the git lane, not by guessing
  br=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  [ -z "$br" ] && { printf "%s\tNO-REMOTE\t-\t-\t-\t-\t-\n" "$slug"; continue; }
  found=0
  for n in $NAMES; do
    o="$SP/payloads/root_$(echo "${slug}_${n}" | tr '/.' '__')"
    code=$(curl -s -L --max-time 20 -w '%{http_code}' -o "$o" "https://raw.githubusercontent.com/$slug/$br/$n")
    if [ "$code" = "200" ]; then
      res=$(python3 -I "$SP/classify.py" "$o")
      printf "%s\t%s\t%s\t200\t%s\n" "$slug" "$br" "$n" "$res"
      found=1; break
    fi
    rm -f "$o"
  done
  [ "$found" = "0" ] && printf "%s\t%s\tLIST-MISS\t404\tNEEDS-STAGE-B\t-\t-\n" "$slug" "$br"
done < "$SP/slugs.txt"
