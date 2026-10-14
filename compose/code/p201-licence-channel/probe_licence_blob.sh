#!/bin/bash
# p201-licence-channel — resolve a repo's grant from BYTES, not from a licence field.
#
# Why this exists (pass 201, 2026-10-14).  p200 declared `polimediaupv/paella` "declared,
# ungranted" after probing five CAPITALISED path forms on three branches -- in the same pass
# in which it discovered a lowercase `license.txt` on `frappe/erpnext`.  The grant was at
# `license.txt` on `develop`: 9 915 B, ECL-2.0, with the section 3 education narrowing on
# line 7.  A path vocabulary is a shared instrument, not a per-row habit (`Gap 454`).
#
# Two measured facts this script encodes:
#   1. 11 of 35 education repos measured in p201 use NEITHER `main` NOR `master`
#      (release_11, 15.0, release, dev, v2, mobile, develop).  Resolve the branch FIRST or
#      a third of the shelf reports a false "no licence file".
#   2. The GitHub API's licence field resolved 23/32 of `topic:lms stars:>200`; blobs lifted
#      it to 29/32.  NOASSERTION means "GitHub could not match the text", not "unlicensed":
#      6/6 NOASSERTION rows had a readable grant.
#
# It deliberately does NOT classify.  Classification belongs to `lib/license_family.sh`
# (`family_of`, suite 207/207, and 65/65 on p201's blobs).  A pass that writes its own
# classifier re-earns the GPL/AGPL section-13 defect -- `P237`, four recorded times.
#
# usage: probe_licence_blob.sh <owner/repo> [<owner/repo> ...]
# output: TSV -- slug  branch  path  bytes  sha256
#         or   slug  branch  NO-BLOB-IN-<n>-PATHS  -  -

set -u

# The path vocabulary, in probe order.  Every form here was observed on a real repository:
#   license.txt        frappe/erpnext (35 149 B), polimediaupv/paella (9 915 B)
#   docs/License.txt   OS4ED/openSIS-Classic (17 286 B, UTF-8 BOM intact)
#   COPYING.txt        moodle/moodle (35 147 B)
#   LICENSE.txt        h5p/h5p-php-library (35 146 B), overhangio/tutor (34 523 B)
#   LICENSE.md         codelitdev/courselit (34 143 B), leemonade/leemons (10 830 B)
LICENCE_PATHS="LICENSE LICENSE.md LICENSE.txt license.txt License.txt LICENCE LICENCE.txt
LICENSE.TXT license COPYING COPYING.txt COPYING.LESSER docs/License.txt docs/LICENSE
LICENSE/LICENSE"

resolve_branch() {
  git ls-remote --symref "https://github.com/$1" HEAD 2>/dev/null |
    awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}'
}

probe_one() {
  local slug="$1" branch n=0
  branch=$(resolve_branch "$slug")
  if [ -z "$branch" ]; then
    printf '%s\tUNREACHABLE\t-\t-\t-\n' "$slug"
    return 1
  fi
  local tmp; tmp=$(mktemp)
  for p in $LICENCE_PATHS; do
    n=$((n+1))
    local code
    code=$(curl -s -o "$tmp" -w '%{http_code}' --max-time 25 \
             "https://raw.githubusercontent.com/$slug/$branch/$p")
    if [ "$code" = "200" ]; then
      printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$branch" "$p" \
             "$(wc -c < "$tmp" | tr -d ' ')" "$(sha256sum < "$tmp" | cut -c1-12)"
      rm -f "$tmp"; return 0
    fi
  done
  rm -f "$tmp"
  printf '%s\t%s\tNO-BLOB-IN-%d-PATHS\t-\t-\n' "$slug" "$branch" "$n"
  return 2
}

[ $# -eq 0 ] && { echo "usage: $0 <owner/repo> [...]" >&2; exit 2; }
printf 'slug\tbranch\tpath\tbytes\tsha256_12\n'
rc=0
for s in "$@"; do probe_one "$s" || rc=1; done
exit $rc
