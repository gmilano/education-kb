#!/bin/sh
# ACTION JQ (p172). Same MARK/PROV regexes and same two measurements as pass 45's
# scan_marking.sh, so the numbers are comparable; only the row set differs.
set -u
WORK=${2:-/tmp/aiact502-p172}; ROWS="$1"
mkdir -p "$WORK/trees"
MARK='c2pa|watermark|synthid|content.?credential|invisible-watermark|imwatermark'
PROV='provenance|generated.*true|source_labels'
printf 'layer\trepo\tverdict\tfiles\tmark_hits\tprov_hits\tmanifests\tmanifest_dep_hits\n' > "$WORK/result.tsv"
awk -F'\t' '!/^#/ && NF && $3!="no"{print $1"\t"$2"\t"$3}' "$ROWS" | while IFS="$(printf '\t')" read -r layer slug verdict; do
  safe=$(echo "$slug" | tr '/' '_')
  br=$(timeout 60 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  [ -n "$br" ] || { printf '%s\t%s\t%s\tUNREACHABLE\n' "$layer" "$slug" "$verdict" >> "$WORK/result.tsv"; continue; }
  if [ ! -s "$WORK/trees/$safe.txt" ]; then
    timeout 300 git clone --depth 1 --filter=blob:none --no-checkout --quiet "https://github.com/$slug" "$WORK/c_$safe" 2>/dev/null || { printf '%s\t%s\t%s\tCLONE-FAILED\n' "$layer" "$slug" "$verdict" >> "$WORK/result.tsv"; continue; }
    git -C "$WORK/c_$safe" ls-tree -r HEAD --name-only > "$WORK/trees/$safe.txt"
    rm -rf "$WORK/c_$safe"
  fi
  files=$(wc -l < "$WORK/trees/$safe.txt" | tr -d ' ')
  mark=$(grep -ciE "$MARK" "$WORK/trees/$safe.txt" || true)
  prov=$(grep -ciE "$PROV" "$WORK/trees/$safe.txt" || true)
  man=0; dep=0
  for m in $(grep -E '^(package\.json|requirements[^/]*\.txt|pyproject\.toml|Pipfile|environment\.yml|go\.mod|pom\.xml)$' "$WORK/trees/$safe.txt" || true); do
    man=$((man+1))
    n=$(timeout 40 curl -s --max-time 25 "https://raw.githubusercontent.com/$slug/$br/$m" | grep -ciE "$MARK" || true)
    dep=$((dep+n))
  done
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$layer" "$slug" "$verdict" "$files" "$mark" "$prov" "$man" "$dep" >> "$WORK/result.tsv"
done
echo "--- result ---"; cat "$WORK/result.tsv"
