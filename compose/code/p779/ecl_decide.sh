#!/bin/bash
# p779 (p778-B): the bytes decide. For each Apache-2.0-graded repo in the
# 11.0-11.5 kB band, read the FIRST 200 BYTES of the grant it actually ships and
# classify the title line. ECL-2.0 announces itself in the first 52 bytes
# ("Educational Community License, Version 2.0"); canonical Apache-2.0 opens
# with a centred "Apache License / Version 2.0, January 2004". Anything else is
# emitted as OTHER and is a finding in its own right, not a silent pass.
decide() {
  slug="$1"; f="$2"; len="$3"
  head200=$(timeout 25 curl -sS -r 0-199 "https://raw.githubusercontent.com/$slug/HEAD/$f" 2>/dev/null | tr -d '\000')
  if   printf '%s' "$head200" | grep -qi "Educational Community License"; then v=ECL-2.0
  elif printf '%s' "$head200" | grep -qi "Apache License"; then v=Apache-2.0
  elif [ -z "$head200" ]; then v=EMPTY
  else v=OTHER
  fi
  first=$(printf '%s' "$head200" | sed -n '1p' | cut -c1-70 | tr -d '\t')
  printf "%s\t%s\t%s\t%s\t%s\n" "$slug" "$f" "$len" "$v" "$first"
}
export -f decide
awk -F'\t' '{print $1"|"$2"|"$3}' "$1" | xargs -P 10 -I{} bash -c 'IFS="|" read -r a b c <<< "$1"; decide "$a" "$b" "$c"' _ {}
