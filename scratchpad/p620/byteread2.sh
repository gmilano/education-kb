#!/bin/bash
# byteread2.sh <slug> : LADDER v2 (p620-B fix) — adds LICENSE-MIT / MIT-LICENSE / docs/ / packages/ rungs
s="$1"; tmp=$(mktemp -d)
m=$(curl -s -o /dev/null -w '%{http_code}' "https://raw.githubusercontent.com/$s/main/README.md")
ms=$(curl -s -o /dev/null -w '%{http_code}' "https://raw.githubusercontent.com/$s/master/README.md")
if [ "$m" = "404" ] && [ "$ms" = "200" ]; then br=master; elif [ "$m" = "200" ]; then br=main; else br=main; fi
n=$(basename "$s")
for p in LICENSE LICENSE.md LICENSE.txt COPYING COPYING.txt LICENCE LICENCE.md license license.md License License.md \
         LICENSE-MIT MIT-LICENSE MIT-LICENSE.txt LICENSE-APACHE LICENSE-2.0.txt LICENSE.rst \
         docs/LICENSE docs/LICENSE.md legal/LICENSE licenses/LICENSE .github/LICENSE "packages/$n/LICENSE" "src/LICENSE"; do
  r=$(curl -s -o "$tmp/l" -w '%{http_code} %{size_download}' "https://raw.githubusercontent.com/$s/$br/$p")
  c=${r%% *}; b=${r##* }
  if [ "$c" = "200" ] && [ "$b" -gt 50 ]; then
    t=$(grep -m1 -vE '^[[:space:]]*$' "$tmp/l" | head -c 70 | tr -d '\r')
    h=$(grep -m1 -oiE 'copyright[^A-Za-z0-9]*(\(c\))?[[:space:]]*[0-9]{4}([-–][0-9a-z]{4,7})?[,]?[[:space:]]*[^<]{0,45}' "$tmp/l" | head -c 80 | tr -d '\r')
    echo -e "$s\t$br\t$p\t${b}B\t$t\t$h"; rm -rf "$tmp"; exit 0
  fi
done
echo -e "$s\t$br\tNIL_24_PATHS\t-\t-\t-"
rm -rf "$tmp"
