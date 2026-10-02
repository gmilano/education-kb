#!/bin/sh
# Pase 47, action 3 (gap 99): does ANY exposed row emit a handle on the SPAN,
# or is every output an opaque block of text?
#
# The component written in pase 46 (../aiact-50-2-marking/) maps, transports and
# asserts per-span provenance. It does NOT classify. Someone has to assign one of
# lineage-skill's 9 labels to each span -- and that is only possible if the
# generator says where the spans ARE. This script answers that one question.
#
# What it measures, and what it does not:
#   * it reads the FILE LIST of every exposed repo from a blob-filtered clone
#     (no blobs downloaded), then fetches ONLY the files whose path suggests a
#     response shape, capped at $CAP per repo, and greps their CONTENT;
#   * so a repo reported `opaque` means "no span handle in the files this script
#     chose to read", NOT "no span handle anywhere". The cap is the honest limit
#     and it is printed in the output.
#
# Why not a code search: github.com answers 403 to curl here and api.github.com
# denies access in the body (established in pass 37). git + raw are the channels.
#
#   sh scan_spans.sh [workdir]
set -e
WORK=${1:-/tmp/aiact502spans}
HERE=$(cd "$(dirname "$0")" && pwd)
ROWS="$HERE/../aiact-50-2-exposure/rows.tsv"
CAP=${CAP:-25}
mkdir -p "$WORK/trees"

# A handle on the span: a boundary a classifier could attach a label to.
STRONG='start_index|end_index|char_start|char_end|start_offset|end_offset|span_start|span_end|chunk_id|chunk_index|chunkId|text_offset|"offsets"|offsets:'
# Adjacent vocabulary: shows the concept exists without giving a boundary.
WEAK='citation|chunk|provenance|source_label|grounding'
# Paths that plausibly define what a generation RETURNS.
CAND='(schema|model|response|citation|chunk|span|generate|generat|chat|tutor|rag|retriev|answer|message|prompt|pipeline|agent)'

exposed=$(grep -v '^#' "$ROWS" | awk -F'\t' '$3!="no"{print $1}' | grep -v '^pypi:\|^npm:')
printf 'repo\tfiles\tcandidates\tread\tstrong\tweak\tverdict\ttokens\n' > "$WORK/result.tsv"

for slug in $exposed; do
  safe=$(echo "$slug" | tr '/' '_')
  br=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null \
       | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  [ -n "$br" ] || { printf '%s\t-\t-\t-\t-\t-\tUNREACHABLE\t-\n' "$slug" >> "$WORK/result.tsv"; continue; }

  if [ ! -s "$WORK/trees/$safe.txt" ]; then
    git clone --depth 1 --filter=blob:none --no-checkout --quiet \
        "https://github.com/$slug" "$WORK/c_$safe" 2>/dev/null || {
      printf '%s\t-\t-\t-\t-\t-\tCLONE_FAILED\t-\n' "$slug" >> "$WORK/result.tsv"; continue; }
    git -C "$WORK/c_$safe" ls-tree -r HEAD --name-only > "$WORK/trees/$safe.txt"
    rm -rf "$WORK/c_$safe"
  fi

  files=$(wc -l < "$WORK/trees/$safe.txt" | tr -d ' ')
  cands=$(grep -iE "$CAND" "$WORK/trees/$safe.txt" \
          | grep -E '\.(py|ts|tsx|js|jsx|java|go|rb|rs|kt|json|yaml|yml)$' \
          | grep -viE '(test|spec|__pycache__|node_modules|\.min\.|dist/|locale|i18n)' || true)
  ncand=$(printf '%s' "$cands" | grep -c . || true)
  read=0; strong=0; weak=0; toks=""
  for f in $(printf '%s\n' "$cands" | head -n "$CAP"); do
    body=$(curl -s --max-time 20 "https://raw.githubusercontent.com/$slug/$br/$f" || true)
    [ -n "$body" ] || continue
    read=$((read+1))
    s=$(printf '%s' "$body" | grep -oiE "$STRONG" | sort -u | tr '\n' ',' || true)
    if [ -n "$s" ]; then strong=$((strong+1)); toks="$toks$s"; fi
    printf '%s' "$body" | grep -qiE "$WEAK" && weak=$((weak+1)) || true
  done
  if [ "$strong" -gt 0 ]; then v=HANDLE
  elif [ "$weak" -gt 0 ]; then v=WEAK
  elif [ "$read" -gt 0 ]; then v=OPAQUE
  else v=NO_CANDIDATES; fi
  t=$(printf '%s' "$toks" | tr ',' '\n' | sort -u | grep -v '^$' | tr '\n' ' ')
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$files" "$ncand" "$read" "$strong" "$weak" "$v" "${t:--}" >> "$WORK/result.tsv"
  printf '%-45s %-12s strong=%s weak=%s read=%s/%s\n' "$slug" "$v" "$strong" "$weak" "$read" "$ncand"
done

echo "--- totals (cap=$CAP files read per repo) ---"
awk -F'\t' 'NR>1{n++; c[$7]++} END {printf "rows scanned: %d\n", n;
  for (k in c) printf "  %-14s %d\n", k, c[k]}' "$WORK/result.tsv"
echo "detail: $WORK/result.tsv"
