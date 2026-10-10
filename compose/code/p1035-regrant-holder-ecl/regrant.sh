#!/usr/bin/env bash
# p1035 limb A — re-probe the rows p1029 classified LIVE-NOGRANT / LIVE-NOCONTROL.
# Question: has a grant APPEARED, or a control become reachable, since 2026-10-10?
#
# Usage: bash regrant.sh <addresses-file>    # TSV on stdout, counts on stderr
#
# Identical filename list and control discipline as p1029 (P1005), so the diff
# against result.2026-10-10.tsv is mechanical rather than interpretive.

set -u
cd "$(dirname "$0")"
. ./classify.sh

export GIT_TERMINAL_PROMPT=0
ADDR_FILE="${1:-lost-addresses.nogrant-recheck-26.2026-10-10.txt}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

LICENCE_NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE.rst MIT-LICENSE LICENSE-MIT LICENSE-APACHE"

n=0; n_grant=0; n_nogrant=0; n_nocontrol=0; n_absent=0

printf 'slug\tstatus\tref\thead_sha\ttags\tlicence\tfile\tbytes\tsha256\tcontrol\n'

while IFS= read -r slug; do
  case "$slug" in ''|'#'*) continue ;; esac
  url="https://github.com/${slug}"
  n=$((n+1))

  if ! timeout 60 git ls-remote --symref "$url" HEAD > "$TMP/head" 2>"$TMP/err"; then
    printf '%s\tABSENT\t-\t-\t-\t-\t-\t-\t-\t-\n' "$slug"
    n_absent=$((n_absent+1))
    continue
  fi
  ref=$(head_ref "$TMP/head"); sha=$(head_sha "$TMP/head")
  rawref="$ref"; [ "$rawref" = "-" ] && rawref="$sha"

  timeout 60 git ls-remote --tags "$url" > "$TMP/tags" 2>/dev/null || : > "$TMP/tags"
  tags=$(count_tags "$TMP/tags")

  lic="ABSENT"; licfile="-"; bytes="-"; sum="-"
  for name in $LICENCE_NAMES; do
    code=$(curl -sS --max-time 45 -o "$TMP/payload" -w '%{http_code}' \
             "https://raw.githubusercontent.com/${slug}/${rawref}/${name}" 2>/dev/null || echo 000)
    if [ "$code" = "200" ]; then
      licfile="$name"
      bytes=$(wc -c < "$TMP/payload" | tr -d ' ')
      sum=$(sha256sum "$TMP/payload" | cut -c1-16)
      lic=$(classify_payload "$TMP/payload")
      break
    fi
  done

  ctl=$(curl -sS --max-time 45 -o "$TMP/ctl" -w '%{http_code}' \
          "https://raw.githubusercontent.com/${slug}/${rawref}/README.md" 2>/dev/null || echo 000)
  [ "$ctl" = "200" ] && ctl="200/$(wc -c < "$TMP/ctl" | tr -d ' ')B"

  status="LIVE"
  if [ "$lic" = "ABSENT" ]; then
    case "$ctl" in
      200/*) status="LIVE-NOGRANT"; n_nogrant=$((n_nogrant+1)) ;;
      *)     status="LIVE-NOCONTROL"; n_nocontrol=$((n_nocontrol+1)) ;;
    esac
  else
    n_grant=$((n_grant+1))
  fi

  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$status" "$ref" "$sha" "$tags" "$lic" "$licfile" "$bytes" "$sum" "$ctl"
done < "$ADDR_FILE"

printf 'probed=%d absent=%d grant_appeared=%d still_nogrant=%d still_nocontrol=%d\n' \
  "$n" "$n_absent" "$n_grant" "$n_nogrant" "$n_nocontrol" >&2
