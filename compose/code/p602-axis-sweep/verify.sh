#!/usr/bin/env bash
# p602 grant verifier.
#
# Contract, inherited from this base's hard-won rules:
#   * the REAL default branch is read with `git ls-remote --symref`, never assumed to be
#     main/master.  p601 found `develop`/`development`/`gh-pages`; this pass expects a
#     versioned-branch family (`MOODLE_*_STABLE`) and must not mis-report those as grantless.
#   * the grant payload is fetched TO A FILE and measured with `lib/measure --size`.
#     `P834`: a byte count taken from `$(curl …)` loses the trailing newline run.
#   * the family comes from `lib/license_family.sh` via `measure --family`.  `P171`: a
#     classifier that greps the BODY for "affero" labels every GPL-3.0 payload AGPL-3.0.
#   * the ladder carries LOWERCASE-WITH-EXTENSION names because `p600` measured
#     `frappe/education` keeping its grant at `license.txt` (19 B).  A ladder of only
#     UPPERCASE + bare `license` loses it, which is `p600`'s own casing finding
#     re-imported as a defect.  See `evidence/grant-path-casing.2026-11-01-p600.tsv`.
#   * EVERY repo gets its OWN fabricated-path control, which must return 404.  A 200 there
#     means the host is serving soft content and every byte count in the row is void.
set -uo pipefail
LIST="${1:?candidate list: owner/repo per line}"
OUT="${2:?output tsv}"
WORK="$(mktemp -d)"; trap 'rm -rf "$WORK"' EXIT
MEASURE="$(cd "$(dirname "$0")/../lib" && pwd)/measure"
[ -x "$MEASURE" ] || { echo "lib/measure not executable" >&2; exit 2; }
RAW=https://raw.githubusercontent.com
LADDER="LICENSE LICENSE.md LICENSE.txt LICENSE.rst LICENCE LICENCE.md LICENCE.txt license license.md license.txt license.rst licence licence.md licence.txt COPYING COPYING.txt copying copying.txt COPYRIGHT copyright.txt LICENSE-MIT MIT-LICENSE LICENSE-APACHE NOTICE UNLICENSE unlicense"
printf 'repo\tdefault_branch\tgrant_path\tbytes\tfamily\tholder\tctl404\tstatus\n' > "$OUT"
while IFS= read -r repo; do
  repo="${repo%%[[:space:]]*}"; [ -z "$repo" ] && continue
  case "$repo" in \#*) continue;; esac
  # 1. real default branch, from the symref, not from a guess
  br=$(timeout 60 git ls-remote --symref "https://github.com/$repo" HEAD 2>/dev/null \
        | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  if [ -z "$br" ]; then
    printf '%s\t?\t-\t0\t-\t-\t-\tUNREACHABLE\n' "$repo" >> "$OUT"; continue
  fi
  # 2. per-repo fabricated-path control: must be 404
  ctl=$(timeout 45 curl -sS -o /dev/null -w '%{http_code}' \
        "$RAW/$repo/$br/LICENSE-P602-FABRICATED-CONTROL-ZZQ" 2>/dev/null)
  # 3. walk the ladder, fetch to a FILE
  found=""; 
  for p in $LADDER; do
    f="$WORK/payload"
    code=$(timeout 45 curl -sS -o "$f" -w '%{http_code}' "$RAW/$repo/$br/$p" 2>/dev/null)
    if [ "$code" = "200" ] && [ -s "$f" ]; then found="$p"; break; fi
  done
  if [ -z "$found" ]; then
    printf '%s\t%s\t-\t0\t-\t-\t%s\tNO-GRANT-FILE\n' "$repo" "$br" "$ctl" >> "$OUT"; continue
  fi
  bytes=$("$MEASURE" --size "$WORK/payload")
  fam=$("$MEASURE" --family "$WORK/payload")
  hol=$("$MEASURE" --family "$WORK/payload" >/dev/null 2>&1; "$MEASURE" "$WORK/payload" 2>/dev/null | awk -F'\t' '{print $6}')
  [ -z "$hol" ] && hol='-'
  st=OK; [ "$ctl" != "404" ] && st="CONTROL-FAILED-$ctl"
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$br" "$found" "$bytes" "$fam" "$hol" "$ctl" "$st" >> "$OUT"
done < "$LIST"
