#!/bin/sh
# Pass 45, action 3 (gap 91): measure whether the exposed rows of agents/top.md
# can mark their output as artificially generated, per EU AI Act Article 50(2).
#
# It measures two things and infers neither:
#   1. the FILE LIST of every exposed repo (blob-filtered clone, so no blobs are
#      downloaded), grepped for marking artifacts;
#   2. the ROOT MANIFESTS, grepped for a marking DEPENDENCY.
#
# Why the file list and not a code search: github.com answers 403 to curl in this
# environment and api.github.com answers 200 with a body that denies access
# (established in pass 37), so `git` is the only reliable channel.
#
#   sh scan_marking.sh [workdir]
set -e
WORK=${1:-/tmp/aiact502}
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$WORK/trees"

# Anything that would satisfy or approach Art. 50(2): a mark IN the artifact.
MARK='c2pa|watermark|synthid|content.?credential|invisible-watermark|imwatermark'
# Weaker, but the nearest hook: a structured record of where content came from.
PROV='provenance|generated.*true|source_labels'

exposed=$(grep -v '^#' "$HERE/rows.tsv" | awk -F'\t' '$3!="no"{print $1}' | grep -v '^pypi:\|^npm:')
printf 'repo\tfiles\tmark_hits\tprov_hits\tmanifests\tmanifest_dep_hits\n' > "$WORK/result.tsv"

for slug in $exposed; do
  safe=$(echo "$slug" | tr '/' '_')
  br=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null \
       | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  [ -n "$br" ] || { printf '%s\tUNREACHABLE\n' "$slug" >> "$WORK/result.tsv"; continue; }

  if [ ! -s "$WORK/trees/$safe.txt" ]; then
    git clone --depth 1 --filter=blob:none --no-checkout --quiet \
        "https://github.com/$slug" "$WORK/c_$safe" 2>/dev/null || continue
    git -C "$WORK/c_$safe" ls-tree -r HEAD --name-only > "$WORK/trees/$safe.txt"
    rm -rf "$WORK/c_$safe"
  fi

  files=$(wc -l < "$WORK/trees/$safe.txt" | tr -d ' ')
  mark=$(grep -ciE "$MARK" "$WORK/trees/$safe.txt" || true)
  prov=$(grep -ciE "$PROV" "$WORK/trees/$safe.txt" || true)

  man=0; dep=0
  for m in $(grep -E '^(package\.json|requirements[^/]*\.txt|pyproject\.toml|Pipfile|environment\.yml|go\.mod|pom\.xml)$' "$WORK/trees/$safe.txt" || true); do
    man=$((man+1))
    n=$(curl -s --max-time 25 "https://raw.githubusercontent.com/$slug/$br/$m" \
        | grep -ciE "$MARK" || true)
    dep=$((dep+n))
  done
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$files" "$mark" "$prov" "$man" "$dep" >> "$WORK/result.tsv"
done

echo "--- totals ---"
awk -F'\t' 'NR>1 && $2!="UNREACHABLE" {r++; f+=$2; m+=$3; p+=$4; n+=$5; d+=$6}
  END {printf "repos scanned          : %d\nfiles listed           : %d\nmarking artifacts      : %d\nprovenance artifacts   : %d\nroot manifests read    : %d\nmarking dependencies   : %d\n", r, f, m, p, n, d}' "$WORK/result.tsv"
echo "detail: $WORK/result.tsv"
