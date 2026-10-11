#!/bin/sh
# ACTION F - the 5 addresses p118 left unread because their LICENSE is a PROSE
# INDEX naming sibling files. Follow the index: fetch the named siblings from
# the DEFAULT branch (P118-C) and record the grant each one actually carries.
set -u
OUT=evidence-f
probe() { # slug branch path
  url="https://raw.githubusercontent.com/$1/$2/$3"
  code=$(curl -s -o "$OUT/$(echo "$1$3" | tr '/' '_')" -w '%{http_code}' "$url")
  size=$(wc -c < "$OUT/$(echo "$1$3" | tr '/' '_')" 2>/dev/null || echo 0)
  printf '%-44s %-26s http=%s %7s B\n' "$1" "$3" "$code" "$size"
}
for spec in \
  "bncc-dev/bncc-pacotes main LICENSE" \
  "bncc-dev/bncc-pacotes main LICENSE-CODIGO.md" \
  "bncc-dev/bncc-pacotes main LICENSE-DADOS.md" \
  "bncc-dev/bncc-benchmark main LICENSE" \
  "bncc-dev/bncc-benchmark main LICENSE-CODIGO.md" \
  "bncc-dev/bncc-benchmark main LICENSE-DADOS.md" \
  "learning-commons-org/evaluators main LICENSE" \
  "learning-commons-org/evaluators main LICENSE.md" \
  "learning-commons-org/knowledge-graph main LICENSE" \
  "learning-commons-org/knowledge-graph main LICENSE.md" \
  "leemonade/leemons main LICENSE" \
  "leemonade/leemons main LICENSE.md" \
  ; do
  set -- $spec; probe "$1" "$2" "$3"
done
