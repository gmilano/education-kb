#!/usr/bin/env bash
# licence-grant-gate (p897) — byte-read a repo's licence grant before it enters a client deliverable.
#
# Why this exists: GitHub's SPDX detector classifies the REPOSITORY ROOT ONLY. OS4ED/openSIS-Classic
# keeps its GPL-2.0 at docs/License.txt and is therefore reported as licence NONE — indistinguishable,
# in any table, from genuinely unlicensed code. This gate probes the directory axis as well as the
# filename axis, and prints bytes + sha256 so the grant is evidence, not an assertion.
#
# Usage: ./probe-grant.sh owner/repo [owner/repo ...]
set -uo pipefail

BRANCHES="main master develop"
DIRS="" # root first
DIRS="$DIRS docs/ doc/ legal/ LICENSES/ .github/"
NAMES="LICENSE LICENSE.md LICENSE.txt LICENSE.TXT license.txt License.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE.rst LICENSE-MIT LICENSE-APACHE NOTICE"

probe() {
  local repo="$1" hits=0 tmp
  tmp="$(mktemp)"
  echo "=== $repo ==="
  for b in $BRANCHES; do
    for d in "" $DIRS; do
      for n in $NAMES; do
        local url="https://raw.githubusercontent.com/${repo}/${b}/${d}${n}"
        local code
        code=$(curl -s -o "$tmp" -w '%{http_code}' --max-time 20 "$url" || echo 000)
        if [ "$code" = "200" ]; then
          printf '  HIT %-10s %-16s %8sB  sha256_12=%s\n' \
            "$b" "${d}${n}" "$(wc -c < "$tmp")" "$(sha256sum "$tmp" | cut -c1-12)"
          printf '      first: %s\n' "$(grep -m1 -vE '^[[:space:]]*$' "$tmp" | cut -c1-100)"
          hits=$((hits+1))
        fi
      done
    done
  done
  rm -f "$tmp"
  if [ "$hits" -eq 0 ]; then
    echo "  NO GRANT FOUND — $(echo $BRANCHES | wc -w) branches x $(( $(echo $DIRS | wc -w) + 1 )) dirs x $(echo $NAMES | wc -w) names"
    echo "  => treat as UNLICENSED (all rights reserved). Do NOT ship."
  fi
}

[ $# -eq 0 ] && { echo "usage: $0 owner/repo [...]"; exit 2; }
for r in "$@"; do probe "$r"; done
