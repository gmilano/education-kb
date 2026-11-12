#!/usr/bin/env bash
# p797 — ACTION p796-C: the BRAND layer is a separate licence question from the CODE layer.
#
# p796 found 3 of 3 checked rows carrying a brand-asset restriction the root `LICENSE` does not
# mention (T914). It checked the rows it had already recommended. This extends the same read to
# every platform address in the base and grades the result THREE-STATE, because the obvious
# instrument here produces false alarms: Apache-2.0 clause 6 and MPL-2.0 clause 3.4 BOTH decline
# to grant trademark rights, in every repository that carries them. A gate that reports those as
# findings would report ~half the base and mean nothing (`p796-G`: control for the false alarm,
# not only the false zero).
#
# Channel: blobless bare clone (`p796`, 176 addresses / 16s). NOT `curl -sI` — T923 established
# that returns 403 for a live address and for an invented one alike, so it cannot distinguish them.
#
# ONLINE. Stays out of `make hooks` by the same rule as `carried-existence-sweep`.
#
# Usage:  ingest/p797-brand-layer-gate.sh ADDRESS_FILE OUT_TSV [WORKDIR] [PARALLEL]
#   ADDRESS_FILE  one `owner/repo` per line, `#` comments allowed
#   OUT_TSV       machine output: one row per candidate FILE, not per repository
set -uo pipefail

ADDRS="${1:?address file}"
OUT="${2:?output tsv}"
WORK="${3:-$(mktemp -d)}"
PAR="${4:-10}"

mkdir -p "$WORK"

# Files that can carry a brand grant or restriction. The root tree only: p796's census showed the
# root is where every instance it found lives, and a recursive read is 100x the bytes.
CAND_RE='^(LICEN[CS]E|COPYING|COPYRIGHT|NOTICE|TRADEMARK|TRADEMARKS|BRAND|BRANDING|BRAND_GUIDELINES|LICENSE_HISTORY|LICENSES|THIRD|NOTICES)'
# Brand-layer vocabulary. Deliberately wide; the three-state grade below is what removes the noise.
# v2 — CORRECTED. v1 matched `icon` as a SUBSTRING and so reported it on every GPL-3.0 row in the
# base, because GPL-3.0 section 0 says "semiconductor masks". 17 rows carried a term they do not
# contain. Word boundaries, and `trade names` kept separate because it is Apache-2.0 clause 6
# boilerplate rather than a bespoke restriction.
TERM_RE='\b(logos?|logotypes?|wordmarks?|word marks?|icons?|branding|brand names?|brand assets?|trade ?-?marks?|NoDerivs|BY-ND|white[ -]?labell?(ing|ed)?|visual identity|trade names)\b'

probe() {
    local slug="$1"
    local safe="${slug//\//__}"
    local d="$WORK/$safe.git"
    rm -rf "$d"
    if ! git clone --filter=blob:none --bare --quiet "https://github.com/$slug" "$d" 2>"$WORK/$safe.err"; then
        printf '%s\tCLONE_FAIL\t\t\t\t\t%s\n' "$slug" "$(tr -d '\n' < "$WORK/$safe.err" | cut -c1-160)"
        return
    fi
    local head_sha
    head_sha=$(git -C "$d" rev-parse HEAD 2>/dev/null) || head_sha="NO_HEAD"
    local files
    files=$(git -C "$d" ls-tree HEAD --name-only 2>/dev/null)
    local n_cand=0
    while IFS= read -r f; do
        [ -z "$f" ] && continue
        printf '%s' "$f" | grep -qiE "$CAND_RE" || continue
        n_cand=$((n_cand+1))
        local bytes sha hits terms otype
        otype=$(git -C "$d" cat-file -t "HEAD:$f" 2>/dev/null) || otype="MISSING"
        if [ "$otype" != "blob" ]; then
            # v2 — CORRECTED. `cat-file -s` returns a size for a TREE too, so v1 published
            # `sakaiproject/sakai:licenses` as a 4,380 B licence file. It is a directory.
            printf '%s\t%s\tNOT_A_BLOB:%s\t-\t0\t\t%s\n' "$slug" "$f" "$otype" "$head_sha"
            continue
        fi
        bytes=$(git -C "$d" cat-file -s "HEAD:$f" 2>/dev/null) || bytes="DIR_OR_MISSING"
        sha=$(git -C "$d" rev-parse "HEAD:$f" 2>/dev/null) || sha="-"
        if [ "$bytes" = "DIR_OR_MISSING" ]; then
            printf '%s\t%s\t%s\t%s\t\t\t%s\n' "$slug" "$f" "$bytes" "$sha" "$head_sha"
            continue
        fi
        # hits = count of matching lines; terms = the distinct vocabulary actually present
        local body
        body=$(git -C "$d" cat-file blob "HEAD:$f" 2>/dev/null)
        hits=$(printf '%s' "$body" | grep -icE "$TERM_RE")
        terms=$(printf '%s' "$body" | grep -oiE "$TERM_RE" | tr 'A-Z' 'a-z' | sed 's/  */ /g' | sort -u | paste -sd, -)
        printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$f" "$bytes" "$sha" "$hits" "$terms" "$head_sha"
    done <<< "$files"
    if [ "$n_cand" -eq 0 ]; then
        printf '%s\tNO_CANDIDATE_FILE\t0\t-\t0\t\t%s\n' "$slug" "$head_sha"
    fi
}
export -f probe
export WORK CAND_RE TERM_RE

printf 'repo\tfile\tbytes\tblob_sha1\tmatch_lines\tterms_present\thead_sha1\n' > "$OUT"
grep -vE '^\s*(#|$)' "$ADDRS" | xargs -P "$PAR" -I{} bash -c 'probe "$@"' _ {} >> "$OUT"

echo "── rows: $(( $(wc -l < "$OUT") - 1 ))   clone failures: $(grep -c CLONE_FAIL "$OUT" || true)"
echo "── work: $WORK"
