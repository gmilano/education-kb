#!/bin/bash
# P114 three-value license scan over raw.githubusercontent.com
# Output TSV: org/repo <TAB> verdict <TAB> artifact <TAB> first-line-of-text
R="$1"
RAW="https://raw.githubusercontent.com/$R"
code() { curl -s -m 12 -o /dev/null -w "%{http_code}" "$1" 2>/dev/null; }
for br in main master; do
  for f in LICENSE LICENSE.md LICENSE.txt COPYING; do
    c=$(code "$RAW/$br/$f")
    if [ "$c" = "200" ]; then
      txt=$(curl -s -m 12 "$RAW/$br/$f" 2>/dev/null | tr -d '\r' | grep -m1 -vE '^[[:space:]]*$' | cut -c1-90)
      printf "%s\tlicenciado\t%s:%s\t%s\n" "$R" "$br" "$f" "$txt"
      exit 0
    fi
  done
done
# step 3: reachability control
for br in main master develop; do
  for f in README.md package.json pyproject.toml setup.py README.rst; do
    c=$(code "$RAW/$br/$f")
    if [ "$c" = "200" ]; then
      printf "%s\tsin-licencia\t%s:%s(200)\tausencia MEDIDA: repo responde\n" "$R" "$br" "$f"
      exit 0
    fi
  done
done
printf "%s\tindeterminado\t-\tel canal no llego\n" "$R"
