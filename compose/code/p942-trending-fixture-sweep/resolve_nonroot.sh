#!/usr/bin/env bash
# p942 item B - resolve the grant of a slug that served nothing on the root ladder.
#
# INSTRUMENT NOTE.  p940/p941 used `gh api search/repositories` and this pass
# assumed `gh api repos/{slug}` would serve the default branch.  It does NOT:
# this session's GitHub API is scoped to the repositories attached to it, so
# repos/{slug} on a third-party slug returns 403 "not enabled for this session".
# Attaching 125 third-party repos to read a branch name would be the wrong trade.
# `git ls-remote --symref` answers the same question with no API and no attachment,
# and doubles as the liveness probe.
#
# Emits: slug <TAB> default_branch <TAB> path <TAB> bytes <TAB> sha12
set -u
slug="$1"
sym=$(git ls-remote --symref "https://github.com/${slug}" HEAD 2>/dev/null) || {
  printf '%s\tDEAD-OR-UNREACHABLE\t-\t-\t-\n' "$slug"; exit 0; }
br=$(printf '%s' "$sym" | sed -n 's|^ref: refs/heads/\([^\t ]*\).*|\1|p' | head -1)
[ -z "$br" ] && { printf '%s\tNO-HEAD-SYMREF\t-\t-\t-\n' "$slug"; exit 0; }
tmp=$(mktemp)
for path in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt \
            COPYING COPYING.txt COPYING.md COPYING.LESSER LICENSE.rst \
            license.txt license LICENSE-MIT LICENSE-APACHE docs/License.txt; do
  code=$(curl -sS -o "$tmp" -w '%{http_code}' --max-time 25 \
    "https://raw.githubusercontent.com/${slug}/${br}/${path}" 2>/dev/null || echo 000)
  if [ "$code" = "200" ]; then
    printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "$path" \
      "$(wc -c < "$tmp" | tr -d ' ')" "$(sha256sum "$tmp" | cut -c1-12)"
    rm -f "$tmp"; exit 0
  fi
done
printf '%s\t%s\tNO-GRANT-ON-16-PATH-LADDER\t-\t-\n' "$slug" "$br"
rm -f "$tmp"
