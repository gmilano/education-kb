#!/bin/bash
# p773 -- D9 fix: the grant filename list must be CASE-AWARE and wide.
# A missing lowercase license.txt produced a false NO-GRANT-AT-ROOT on ERPNext.
s="$1"; br="$2"
for f in LICENSE LICENSE.md LICENSE.txt LICENSE.rst LICENCE LICENCE.md LICENCE.txt \
         license license.md license.txt licence licence.txt License License.md License.txt \
         COPYING COPYING.txt COPYING.md copying copying.txt COPYRIGHT NOTICE \
         LICENSE-MIT LICENSE-APACHE LICENSE-APACHE-2.0 LICENSE.APACHE2 \
         MIT-LICENSE MIT-LICENSE.txt LICENSE.BSD docs/LICENSE .github/LICENSE; do
  code=$(timeout 15 curl -sS -o /dev/null -w '%{http_code}' --max-time 15 \
         "https://raw.githubusercontent.com/$s/$br/$f" 2>/dev/null)
  if [ "$code" = "200" ]; then
    b=$(timeout 20 curl -sSL --max-time 20 "https://raw.githubusercontent.com/$s/$br/$f" 2>/dev/null)
    printf '%s\t%s\t%s\t%s\n' "$s" "$f" "$(printf '%s' "$b" | wc -c | tr -d ' ')" \
           "$(printf '%s' "$b" | sha256sum | cut -c1-12)"
    exit 0
  fi
done
printf '%s\tNO-GRANT-AT-ROOT\t-\t-\n' "$s"
