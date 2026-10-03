#!/bin/bash
R="$1"; RAW="https://raw.githubusercontent.com/$R"
code(){ curl -s -m 12 -o /dev/null -w "%{http_code}" "$1" 2>/dev/null; }
for br in main master; do
  for f in COPYING.txt COPYING.md LICENSE-MIT LICENSE-APACHE LICENSE-APACHE-2.0 LICENSE.rst LICENCE LICENCE.md license license.md License License.md LICENSE-MIT.md UNLICENSE COPYRIGHT NOTICE; do
    c=$(code "$RAW/$br/$f")
    if [ "$c" = "200" ]; then
      txt=$(curl -s -m 12 "$RAW/$br/$f" | tr -d '\r' | grep -m1 -vE '^[[:space:]]*$' | cut -c1-80)
      printf "%s\tLICENCIADO-por-nombre-alterno\t%s:%s\t%s\n" "$R" "$br" "$f" "$txt"; exit 0
    fi
  done
done
printf "%s\tsin-licencia-CONFIRMADO\t-\t16 nombres alternos tambien 404\n" "$R"
