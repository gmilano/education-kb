#!/bin/bash
# ACTION p764-B widened: licence-family paths across language ecosystems AND capitalisation,
# plus COPYING.LESSER probed whenever a GPL-family title is seen (INS-003 / INS-004).
# stdin: repo<TAB>branch   stdout TSV: repo branch channel path bytes sha12 titleline
PATHS="LICENSE LICENSE.md LICENSE.txt LICENSE.rst License License.md License.txt license license.md license.txt \
LICENCE LICENCE.md LICENCE.txt Licence Licence.md Licence.txt licence licence.md licence.txt \
LICENSE-MIT LICENSE-APACHE LICENSE-2.0.txt COPYING COPYING.txt COPYING.md Copying COPYRIGHT Copyright.txt \
docs/LICENSE doc/LICENSE .github/LICENSE LICENSES/LICENSE"
MANIFESTS="package.json pyproject.toml setup.py setup.cfg DESCRIPTION composer.json Cargo.toml pom.xml build.gradle \
version.php gemspec Gemfile *.gemspec go.mod pubspec.yaml Project.toml"
LESSER="COPYING.LESSER COPYING.LIB LICENSE.LESSER lgpl.txt LICENSE-LGPL"
OUT=$1
: > "$OUT"
while IFS=$'\t' read -r repo branch; do
  [ -z "$repo" ] && continue
  found=0
  for p in $PATHS; do
    f="$SD/lic/$(echo "${repo}_${p}" | tr '/.*' '___')"
    code=$(curl -sL --max-time 25 -o "$f" -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$branch/$p")
    if [ "$code" = "200" ] && [ -s "$f" ]; then
      b=$(wc -c < "$f" | tr -d ' '); s=$(sha256sum "$f" | cut -c1-12)
      fl=$(head -c 500 "$f" | tr -d '\r' | tr '\n\t' '  ' | sed 's/  */ /g' | sed 's/^ *//' | cut -c1-150)
      printf "%s\t%s\tgrant\t%s\t%s\t%s\t%s\n" "$repo" "$branch" "$p" "$b" "$s" "$fl" >> "$OUT"
      # INS-004: a GPL-family title must be followed by a COPYING.LESSER probe
      if echo "$fl" | grep -qiE 'GNU (GENERAL|LESSER|AFFERO)'; then
        for l in $LESSER; do
          g="$SD/lic/$(echo "${repo}_${l}" | tr '/.*' '___')"
          c2=$(curl -sL --max-time 20 -o "$g" -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$branch/$l")
          if [ "$c2" = "200" ] && [ -s "$g" ]; then
            b2=$(wc -c < "$g" | tr -d ' '); s2=$(sha256sum "$g" | cut -c1-12)
            f2=$(head -c 300 "$g" | tr -d '\r' | tr '\n\t' '  ' | sed 's/  */ /g' | cut -c1-120)
            printf "%s\t%s\tlesser\t%s\t%s\t%s\t%s\n" "$repo" "$branch" "$l" "$b2" "$s2" "$f2" >> "$OUT"
            break
          else rm -f "$g"; fi
        done
      fi
      found=1; break
    else rm -f "$f"; fi
  done
  if [ $found -eq 0 ]; then
    mfound=0
    for m in $MANIFESTS; do
      f="$SD/lic/$(echo "${repo}_${m}" | tr '/.*' '___')"
      code=$(curl -sL --max-time 25 -o "$f" -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$branch/$m")
      if [ "$code" = "200" ] && [ -s "$f" ]; then
        lic=$(grep -i -m2 -E '"?licen[sc]e"?\s*[:=]' "$f" | tr -d '\r' | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-140)
        if [ -n "$lic" ]; then
          b=$(wc -c < "$f" | tr -d ' '); s=$(sha256sum "$f" | cut -c1-12)
          printf "%s\t%s\tmanifest\t%s\t%s\t%s\t%s\n" "$repo" "$branch" "$m" "$b" "$s" "$lic" >> "$OUT"
          mfound=1; break
        fi
      fi
      rm -f "$f"
    done
    [ $mfound -eq 0 ] && printf "%s\t%s\tNONE\t-\t-\t-\tno payload across %d licence paths + %d manifests\n" "$repo" "$branch" $(echo $PATHS|wc -w) $(echo $MANIFESTS|wc -w) >> "$OUT"
  fi
done
