#!/usr/bin/env bash
# ACTION Z — read a repository's grant as a SET of (path -> token) pairs.
#
# WHY. Every licence instrument in this KB up to p122 reduced a repository to
# ONE token: scan_licences.sh probed paths in order and STOPPED at the first
# 200. p122 then measured its own prose census at a 95 % false-positive rate
# and found the cause was structural -- the pages record grants per artifact
# ("MIT code / CC BY-NC-SA data", "MIT (LICENSE-CODE) - LICENSE is CC-BY-4.0
# for docs") and a one-token census is LESS precise than the text it audits.
# A census cannot be more precise than its data model. So the model changes:
# read EVERY grant file and emit one row per file.
#
# Branch comes from resolve_head.sh (ACTION Y). No main/master guessing.
#
# Stage 1 HEADs every (address x path); stage 2 GETs only the hits and
# classifies them in ONE python pass. 21 paths x 1327 addresses is 27 k
# probes, so the body is never fetched speculatively.
#
# usage: grant_set.sh HEADS_TSV CACHE_DIR > grants.tsv
#   HEADS_TSV: address <TAB> EXISTS|ABSENT <TAB> branch   (resolve_head.sh)
# output: address <TAB> branch <TAB> path <TAB> bytes <TAB> token
#         address <TAB> branch <TAB> -    <TAB> 0     <TAB> NO-FILE
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
HEADS="$1"; CACHE="$2"; mkdir -p "$CACHE"

# Paths in no priority order -- ALL are read. LICENSE-CODE / LICENSE-DOCS /
# LICENSE-DADOS are ACTION Z's additions: the split-grant filenames this KB's
# own prose cites and which no previous probe ever requested. DESCRIPTION is
# the R/CRAN grant field that makes a bare LICENSE stub readable.
PATHS="${PATHS:-LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt COPYING COPYING.txt COPYING.LESSER LICENSE.rst LICENSE-CODE LICENSE-CODE.md LICENSE-DOCS LICENSE-DOCS.md LICENSE-DADOS LICENSE-DATA LICENSE-MIT LICENSE-APACHE DESCRIPTION license.txt license.md}"

slug() { printf '%s' "$1" | tr '/' '~'; }

head_one() {
  local addr="$1" br="$2" p="$3" url code
  url="https://raw.githubusercontent.com/${addr}/${br}/${p}"
  code="$(curl -sI -o /dev/null -w '%{http_code}' --max-time 20 "$url" 2>/dev/null)"
  [ "$code" = "200" ] && printf '%s\t%s\t%s\n' "$addr" "$br" "$p"
  return 0
}
export -f head_one

get_one() {
  local addr="$1" br="$2" p="$3" out
  out="${CACHE}/$(printf '%s' "$addr" | tr '/' '~')__$(printf '%s' "$p" | tr '/' '~')"
  curl -sL -o "$out" --max-time 25 \
    "https://raw.githubusercontent.com/${addr}/${br}/${p}" 2>/dev/null
  return 0
}
export -f get_one
export CACHE

# ---- stage 1: which grant files exist -------------------------------------
awk -F'\t' -v P="$PATHS" '$2=="EXISTS"{n=split(P,a," ");for(i=1;i<=n;i++)print $1"\t"$3"\t"a[i]}' \
  "$HEADS" \
| xargs -P 24 -n 3 bash -c 'head_one "$0" "$1" "$2"' > "${CACHE}/hits.tsv"

# ---- stage 2: fetch the hits and classify in one pass ---------------------
xargs -P 16 -n 3 bash -c 'get_one "$0" "$1" "$2"' < "${CACHE}/hits.tsv"

python3 -I "${HERE}/classify_set.py" "${CACHE}/hits.tsv" "$CACHE"

# ---- addresses with no readable grant file at all -------------------------
awk -F'\t' '$2=="EXISTS"{print $1"\t"$3}' "$HEADS" | sort -u > "${CACHE}/exists.tsv"
cut -f1 "${CACHE}/hits.tsv" | sort -u > "${CACHE}/withgrant.txt"
join -t$'\t' -v1 <(sort -t$'\t' -k1,1 "${CACHE}/exists.tsv") "${CACHE}/withgrant.txt" \
  | awk -F'\t' '{print $1"\t"$2"\t-\t0\tNO-FILE"}'
