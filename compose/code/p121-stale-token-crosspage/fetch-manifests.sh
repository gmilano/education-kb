#!/usr/bin/env bash
# P121 ACTION Q. Fetch package.json / composer.json / pyproject.toml for every
# address in p118's 249-address census, on its MEASURED DEFAULT BRANCH.
# p120 had a denominator of 4 and flagged the thinness itself; this widens it.
set -u
OUT="$(dirname "$0")/manifests"
fetch() {
  slug="$1"; branch="$2"; file="$3"
  safe="${slug//\//__}__${file}"
  code=$(curl -sS -o "$OUT/$safe" -w '%{http_code}' --max-time 20 \
     "https://raw.githubusercontent.com/$slug/$branch/$file" 2>/dev/null || echo 000)
  if [ "$code" != "200" ]; then rm -f "$OUT/$safe"; fi
}
export -f fetch; export OUT
while IFS=$'\t' read -r slug branch status; do
  [ -z "${slug:-}" ] && continue
  for f in package.json composer.json pyproject.toml; do echo -e "$slug\t$branch\t$f"; done
done | xargs -P 12 -I{} bash -c 'IFS=$'"'"'\t'"'"' read -r s b f <<< "{}"; fetch "$s" "$b" "$f"'
