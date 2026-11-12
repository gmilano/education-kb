#!/usr/bin/env bash
# p798 — byte-verify a candidate shelf row's GRANT on the blobless-clone channel.
#
# Channel choice is T923's: `curl -sI` returns 403 for a live address and for an invented one
# alike, so it cannot verify existence here. A blobless bare clone can, and it also yields the
# licence file's BYTES, its blob sha and the HEAD commit sha — which is T927's rule, that a byte
# size without a commit sha beside it is a snapshot and not a verification.
#
# Usage: ingest/p798-grant-byte-verify.sh ADDRESS_FILE OUT_TSV
set -uo pipefail
ADDRS="${1:?address file}"; OUT="${2:?out tsv}"
WORK=$(mktemp -d)
printf 'addr\tlive\thead_commit_sha\tlicence_file\tbytes\tblob_sha\ttitle_line\tarchived\tpushed\n' > "$OUT"
grep -vE '^\s*(#|$)' "$ADDRS" | while read -r addr; do
  d="$WORK/$(echo "$addr" | tr '/' '_')"
  if ! git clone --filter=blob:none --no-checkout --depth 1 -q "https://github.com/$addr" "$d" 2>/dev/null; then
    printf '%s\tNO\t-\t-\t-\t-\t-\t-\t-\n' "$addr" >> "$OUT"; continue
  fi
  head_sha=$(git -C "$d" rev-parse HEAD 2>/dev/null | cut -c1-12)
  meta=$(gh api "repos/$addr" --jq '[(.archived|tostring),(.pushed_at[0:10])]|@tsv' 2>/dev/null || printf '?\t?')
  arch=$(cut -f1 <<<"$meta"); push=$(cut -f2 <<<"$meta")
  found=0
  while read -r mode type blob size name; do
    [[ "$type" != blob ]] && continue
    case "$name" in
      LICEN[CS]E*|COPYING*|COPYRIGHT*|NOTICE*|TRADEMARK*|BRAND*|LICENSES*) : ;;
      *) continue ;;
    esac
    git -C "$d" cat-file blob "$blob" > "$d/.lic" 2>/dev/null || continue
    title=$(grep -m1 -vE '^\s*$' "$d/.lic" | tr -d '\r' | cut -c1-70)
    printf '%s\tYES\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$addr" "$head_sha" "$name" "$size" "$(cut -c1-12 <<<"$blob")" "$title" "$arch" "$push" >> "$OUT"
    found=1
  done < <(git -C "$d" ls-tree -l HEAD 2>/dev/null)
  [[ $found -eq 0 ]] && printf '%s\tYES\t%s\tNO-LICENCE-FILE-IN-ROOT\t0\t-\t-\t%s\t%s\n' "$addr" "$head_sha" "$arch" "$push" >> "$OUT"
  rm -rf "$d"
done
rm -rf "$WORK"
echo "rows: $(($(wc -l < "$OUT")-1))"
