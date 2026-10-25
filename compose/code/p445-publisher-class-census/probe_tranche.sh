#!/usr/bin/env bash
# p445 — first-hand verification of every address this pass touches, in the p444 schema.
# Sources the shared library (lib/probe_payload.sh) rather than re-rolling the loop: the
# library carries P171 (GPL-3.0 §13), P834 (trailing-newline sizing) and P441 (an absence
# is only a finding when the tree was ENUMERATED).
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
. "$HERE/../lib/probe_payload.sh"

printf 'slug\thead_sha\tgrant_path\tpublishable_cell\tfamily\thead_date\tfile_count\n'
for slug in "$@"; do
  # Existence and the REAL default ref, never assumed.
  if ! timeout 30 git ls-remote "https://github.com/$slug" HEAD >/dev/null 2>&1; then
    printf '%s\tUNRESOLVED\tUNRESOLVED\tUNRESOLVED\tUNRESOLVED\tUNRESOLVED\t0\n' "$slug"
    continue
  fi
  d=$(mktemp -d)
  if ! timeout 180 git clone --quiet --filter=blob:none --no-checkout --depth 1 \
        "https://github.com/$slug" "$d/r" >/dev/null 2>&1; then
    printf '%s\tCLONE-FAILED\t-\t-\t-\t-\t0\n' "$slug"; rm -rf "$d"; continue
  fi
  sha=$(git -C "$d/r" rev-parse HEAD 2>/dev/null | cut -c1-12)
  hdate=$(git -C "$d/r" log -1 --format=%cs 2>/dev/null)
  fcount=$(git -C "$d/r" ls-tree -r --name-only HEAD 2>/dev/null | wc -l | tr -d ' ')
  rm -rf "$d"

  # Every grant path in the COMPLETE tree, then each payload measured where it landed.
  rows=$(probe_repo_all "$slug" 2>/dev/null)
  if [ -z "$rows" ]; then
    printf '%s\t%s\tNO-GRANT-PATH\tNO-PAYLOAD\tNO-PAYLOAD\t%s\t%s\n' \
      "$slug" "$sha" "$hdate" "$fcount"; continue
  fi
  echo "$rows" | while IFS=$'\t' read -r _r _b fn bytes fam _holder; do
    case "$fn" in
      ABSENCE-ENUMERATED|NO-PAYLOAD|UNRESOLVED)
        printf '%s\t%s\tNO-GRANT-PATH\t%s\t%s\t%s\t%s\n' \
          "$slug" "$sha" "$fn" "$fn" "$hdate" "$fcount" ;;
      *)
        printf '%s\t%s\t%s\t%s B\t%s\t%s\t%s\n' \
          "$slug" "$sha" "$fn" "$bytes" "$fam" "$hdate" "$fcount" ;;
    esac
  done
done
