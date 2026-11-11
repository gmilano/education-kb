#!/bin/bash
# args: repo<TAB>branch  on stdin ; emits TSV: repo branch channel path bytes sha12 firstline
PATHS="LICENSE LICENSE.md LICENSE.txt License License.md License.txt LICENCE LICENCE.md Licence.txt license license.md license.txt LICENSE-MIT LICENSE-APACHE LICENSE.rst COPYING COPYING.txt Copyright.txt docs/LICENSE"
MANIFESTS="package.json pyproject.toml setup.py DESCRIPTION composer.json Cargo.toml pom.xml version.php"
OUT=$1
: > "$OUT"
while IFS=$'\t' read -r repo branch; do
  [ -z "$repo" ] && continue
  found=0
  for p in $PATHS; do
    f="$SD/lic/$(echo "${repo}_${p}" | tr '/.' '__')"
    code=$(curl -sL --max-time 25 -o "$f" -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$branch/$p")
    if [ "$code" = "200" ] && [ -s "$f" ]; then
      b=$(wc -c < "$f" | tr -d ' '); s=$(sha256sum "$f" | cut -c1-12)
      fl=$(head -c 400 "$f" | tr '\n\t' '  ' | sed 's/  */ /g' | cut -c1-150)
      printf "%s\t%s\tgrant\t%s\t%s\t%s\t%s\n" "$repo" "$branch" "$p" "$b" "$s" "$fl" >> "$OUT"
      found=1; break
    else rm -f "$f"; fi
  done
  if [ $found -eq 0 ]; then
    mfound=0
    for m in $MANIFESTS; do
      f="$SD/lic/$(echo "${repo}_${m}" | tr '/.' '__')"
      code=$(curl -sL --max-time 25 -o "$f" -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$branch/$m")
      if [ "$code" = "200" ] && [ -s "$f" ]; then
        lic=$(grep -i -m2 -E '"?licen[sc]e"?\s*[:=]' "$f" | tr '\n' ' ' | cut -c1-120)
        if [ -n "$lic" ]; then
          b=$(wc -c < "$f" | tr -d ' '); s=$(sha256sum "$f" | cut -c1-12)
          printf "%s\t%s\tmanifest\t%s\t%s\t%s\t%s\n" "$repo" "$branch" "$m" "$b" "$s" "$lic" >> "$OUT"
          mfound=1; break
        fi
      fi
      rm -f "$f"
    done
    [ $mfound -eq 0 ] && printf "%s\t%s\tNONE\t-\t-\t-\tno payload across %d license paths + %d manifests\n" "$repo" "$branch" $(echo $PATHS|wc -w) $(echo $MANIFESTS|wc -w) >> "$OUT"
  fi
done
