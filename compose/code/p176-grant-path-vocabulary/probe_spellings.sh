#!/bin/bash
# `ACTION KJ` - re-probe every licence-ABSENCE verdict in this KB for the paths
# `P50`'s list never carried: the British spelling, and `COPYING.md`.
#
# The rule: a path EXISTS when raw.githubusercontent.com answers 200 for it on
# the repository's default branch. A 404 is an absence AT THAT PATH on THAT
# BRANCH - never an absence in the repository, which is what `T209` taught and
# what the word "exhaustive" has been used for in this KB without earning it.
#
# Usage: bash probe_spellings.sh <owner/repo> [<branch>]
set -u
REPO="${1:?owner/repo}"
BRANCH="${2:-}"
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt \
COPYING COPYING.md COPYING.txt License License.md license license.md \
LICENSE-MIT LICENSE-APACHE NOTICE"
if [ -z "$BRANCH" ]; then
  for b in main master; do
    if curl -sfI "https://raw.githubusercontent.com/$REPO/$b/README.md" >/dev/null 2>&1 \
    || curl -sfI "https://raw.githubusercontent.com/$REPO/$b/readme.md" >/dev/null 2>&1; then
      BRANCH="$b"; break
    fi
  done
  [ -z "$BRANCH" ] && BRANCH=main
fi
for p in $PATHS; do
  code=$(curl -s -o /dev/null -w '%{http_code}' "https://raw.githubusercontent.com/$REPO/$BRANCH/$p")
  bytes="-"
  if [ "$code" = "200" ]; then
    bytes=$(curl -s "https://raw.githubusercontent.com/$REPO/$BRANCH/$p" | wc -c | tr -d ' ')
  fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$REPO" "$BRANCH" "$p" "$code" "$bytes"
done
