#!/usr/bin/env bash
# p1029 — probe each owner/repo address: does it resolve anonymously, at which
# ref, with how many tags, and with WHICH licence payload (bytes + sha256).
#
# Usage: bash probe.sh <addresses-file>   # TSV on stdout, counts on stderr
#
# Every row carries a 200-CONTROL: a byte count for README.md at the same ref.
# Without it, "no licence payload" and "the raw host refused us" are the same
# observation (P1005). A row whose control is also non-200 is reported
# NOCONTROL, never ABSENT-of-grant.

set -u
cd "$(dirname "$0")"
. ./classify.sh

export GIT_TERMINAL_PROMPT=0
ADDR_FILE="${1:-lost-addresses.input-99.2026-10-10.txt}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

LICENCE_NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE.rst MIT-LICENSE LICENSE-MIT LICENSE-APACHE"

n_live=0; n_absent=0; n_grant=0; n_nogrant=0; n_nocontrol=0

printf 'slug\tstatus\tref\thead_sha\ttags\tlicence\tfile\tbytes\tsha256\tcontrol\n'

while IFS= read -r slug; do
  case "$slug" in ''|'#'*) continue ;; esac
  url="https://github.com/${slug}"

  if ! timeout 60 git ls-remote --symref "$url" HEAD > "$TMP/head" 2>"$TMP/err"; then
    printf '%s\tABSENT\t-\t-\t-\t-\t-\t-\t-\t-\n' "$slug"
    n_absent=$((n_absent+1))
    continue
  fi
  ref=$(head_ref "$TMP/head")
  sha=$(head_sha "$TMP/head")

  # A repo can resolve with a detached or tag-only HEAD: no branch name.
  # Fall back to the SHA for the raw path, which raw.githubusercontent serves.
  rawref="$ref"
  [ "$rawref" = "-" ] && rawref="$sha"

  timeout 60 git ls-remote --tags "$url" > "$TMP/tags" 2>/dev/null || : > "$TMP/tags"
  tags=$(count_tags "$TMP/tags")

  lic="ABSENT"; licfile="-"; bytes="-"; sum="-"
  for name in $LICENCE_NAMES; do
    code=$(curl -sS --max-time 45 -o "$TMP/payload" \
             -w '%{http_code}' \
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
  if [ "$ctl" = "200" ]; then
    ctl="200/$(wc -c < "$TMP/ctl" | tr -d ' ')B"
  fi

  status="LIVE"
  if [ "$lic" = "ABSENT" ]; then
    case "$ctl" in
      200/*) status="LIVE-NOGRANT"; n_nogrant=$((n_nogrant+1)) ;;
      *)     status="LIVE-NOCONTROL"; n_nocontrol=$((n_nocontrol+1)) ;;
    esac
  else
    n_grant=$((n_grant+1))
  fi
  n_live=$((n_live+1))

  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$status" "$ref" "$sha" "$tags" "$lic" "$licfile" "$bytes" "$sum" "$ctl"
done < "$ADDR_FILE"

printf 'live=%d absent=%d with_grant=%d no_grant=%d no_control=%d\n' \
  "$n_live" "$n_absent" "$n_grant" "$n_nogrant" "$n_nocontrol" >&2
