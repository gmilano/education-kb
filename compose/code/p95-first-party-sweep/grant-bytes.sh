#!/usr/bin/env bash
# P95 stage 2 — BYTE-READ THE GRANT for every repo GitHub left unclassified.
#
# GitHub's licence detector returns NOASSERTION whenever the LICENSE text does
# not match a template byte-for-byte. That is NOT "no licence": on this base it
# has repeatedly meant a real MIT or Apache grant with an added clause, a
# vendored second grant, or — the class p843 named — the Apache-2.0 APPENDIX
# boilerplate used in place of the full 11,357-byte text.
#
# github.com HTML is 403 through this proxy; raw.githubusercontent.com is NOT.
#
# Usage: ./grant-bytes.sh owner/repo [owner/repo ...]
# Output per repo: path, bytes, sha256(12), first non-blank line, and a
#                  BOILERPLATE-ONLY flag when an Apache-2.0 file is < 5,000 B.
set -uo pipefail
APACHE_FULL=11357
tmp=$(mktemp); trap 'rm -f "$tmp"' EXIT
rc=0
for repo in "$@"; do
  echo "### $repo"
  found=""
  for b in main master; do
    for f in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt; do
      code=$(curl -s -o "$tmp" -w '%{http_code}' --max-time 20 \
             "https://raw.githubusercontent.com/$repo/$b/$f" || echo 000)
      [ "$code" = "200" ] || continue
      sz=$(wc -c < "$tmp"); sh=$(sha256sum "$tmp" | cut -c1-12)
      title=$(grep -m1 -v '^[[:space:]]*$' "$tmp" | tr -s ' ' | cut -c1-90)
      echo "  200  $b/$f  ${sz} B  sha256_12=$sh"
      echo "       title: $title"
      if grep -qi 'Apache License' "$tmp" && [ "$sz" -lt 5000 ]; then
        echo "       🟡 BOILERPLATE-ONLY: Apache-2.0 asserted in ${sz} B; the full text is ${APACHE_FULL} B."
        echo "          The grant is by REFERENCE, not by text. Usable, but no byte/text match will grade it."
      fi
      found=1; break 2
    done
  done
  if [ -z "$found" ]; then
    echo "  🔴 NO GRANT PAYLOAD at 7 filenames x 2 branches — all-rights-reserved by default."
    rc=1
  fi
done
exit $rc
