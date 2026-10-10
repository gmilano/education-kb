#!/usr/bin/env bash
# p1035 limb C — name WHICH ECL text each Apereo-lineage payload carries.
#
# Pass 104 measured four byte counts for one declared licence family:
# Sakai 11 120, Opencast 11 340, lap-sakai-extractor 11 087, opendashboard-legacy
# 9 919. P1025 says size is not identity. This limb pins each payload by sha256
# and reports what the TEXT declares, so "it's ECL" becomes checkable.
#
# Usage: bash ecl.sh <tsv: slug<TAB>filename>
#
# It also AUDITS p1029's classifier against these payloads. ECL-2.0 is an
# Apache-2.0 derivative with a different patent clause, and classify_payload
# has no ECL branch — so whatever it returns for an ECL text is recorded here
# as a measured property of the instrument, not assumed.

set -u
cd "$(dirname "$0")"
. ./classify.sh

export GIT_TERMINAL_PROMPT=0
IN="${1:-lost-addresses.ecl-identity-4.2026-10-10.txt}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# declared_name <file> -> the licence the TEXT names, by its own title line.
declared_name() {
  local f="$1" t
  t=$(tr -d '\r' < "$f")
  # CORRECTED in-pass: the version may sit on its own line below the title, so a
  # title-only match splits ONE grant into two families on line-wrapping alone.
  # Both strings must be sought independently of each other.
  case "$t" in
    *"Educational Community License"*)
      case "$t" in
        *"Version 2.0"*) echo "ECL-2.0" ; return 0 ;;
      esac
      echo "ECL-NO-VERSION-ANYWHERE" ; return 0 ;;
  esac
  case "$t" in
    *"Apache License"*) echo "APACHE-TITLED" ; return 0 ;;
  esac
  echo "NO-TITLE-MATCH"
}

# classify_ecl <file> -> the bucket an ECL text BELONGS in.
# p1029's classify_payload returns UNRECOGNISED for ECL, because the ECL text
# names "Apache 2.0 license" in lower case and never the string "Apache
# License". ECL-2.0 IS the Apache-2.0 text with section 3's patent grant
# narrowed to education, so it is PERMISSIVE and Globant can build on it.
classify_ecl() {
  local f="$1" t
  t=$(tr -d '\r' < "$f")
  case "$t" in
    *"Educational Community License"*)
      case "$t" in
        *"scope of the patent grant in section 3"*) echo "PERMISSIVE/ECL-2.0" ; return 0 ;;
      esac
      echo "PERMISSIVE/ECL-UNPINNED" ; return 0 ;;
  esac
  echo "NOT-ECL"
}

printf 'slug\tfile\tbytes\tsha256\tdeclared_by_text\tp1029_classifier\tcorrect_bucket\tp1029_blind\n'

while IFS=$'\t' read -r slug name; do
  case "$slug" in ''|'#'*) continue ;; esac
  [ -n "${name:-}" ] || name=LICENSE

  if ! timeout 60 git ls-remote --symref "https://github.com/${slug}" HEAD > "$TMP/h" 2>/dev/null; then
    printf '%s\t%s\tABSENT\t-\t-\t-\t-\n' "$slug" "$name"; continue
  fi
  ref=$(sed -n 's#^ref: refs/heads/\([^[:space:]]*\)[[:space:]]*HEAD$#\1#p' "$TMP/h" | head -1)
  [ -z "$ref" ] && ref=$(awk '$2=="HEAD"{print $1; exit}' "$TMP/h")

  code=$(curl -sS --max-time 45 -o "$TMP/p" -w '%{http_code}' \
           "https://raw.githubusercontent.com/${slug}/${ref}/${name}" 2>/dev/null || echo 000)
  if [ "$code" != "200" ]; then
    printf '%s\t%s\tHTTP-%s\t-\t-\t-\t-\n' "$slug" "$name" "$code"; continue
  fi

  bytes=$(wc -c < "$TMP/p" | tr -d ' ')
  sum=$(sha256sum "$TMP/p" | cut -d' ' -f1)
  decl=$(declared_name "$TMP/p")
  cls=$(classify_payload "$TMP/p")
  correct=$(classify_ecl "$TMP/p")

  # Two distinct failure modes, and only reading the payload separates them:
  #   MISLABEL  — an ECL text returned as Apache-2.0 (a wrong grant)
  #   INVISIBLE — an ECL text returned as UNRECOGNISED (a permissive row that
  #               lands in NEITHER the permissive nor the copyleft bucket)
  blind="-"
  case "$correct" in
    PERMISSIVE/*)
      case "$cls" in
        Apache-2.0)    blind="MISLABEL-AS-APACHE" ;;
        UNRECOGNISED)  blind="INVISIBLE-TO-CENSUS" ;;
        *)             blind="OK/$cls" ;;
      esac ;;
  esac

  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$name" "$bytes" "$sum" "$decl" "$cls" "$correct" "$blind"
done < "$IN"
