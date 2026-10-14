#!/usr/bin/env bash
# p207 — L1: the LOCATOR has the same disease p206 fixed in the READER.
#
# raw.githubusercontent.com is case-sensitive. This KB's path lists have always
# been fixed-case enumerations ("LICENSE", "LICENSE.md", "LICENSE.txt", ...),
# so a repository that spells its file LICENSE.TXT returns 404 on every form
# and is recorded as UNGRANTED. openedx/XBlock -- Apache-2.0, 11 358 B, in this
# KB's foundations table -- is exactly that repository.
#
# An absence is only reportable after the case variants have been tried. This
# is M2/M4 discipline applied to a filename: "we did not find it" and "it is
# not there" are different claims.
licence_paths() {
  local b e
  for b in LICENSE LICENCE License Licence license licence COPYING Copying copying; do
    for e in "" .txt .TXT .md .MD .rst .RST .text .html; do printf '%s%s\n' "$b" "$e"; done
  done
}
# fetch_licence <owner/repo> -> prints "<path>\t<bytes>" and writes body to $2
fetch_licence() {
  local repo="$1" out="${2:-/dev/null}" p code
  while IFS= read -r p; do
    code=$(curl -sS --max-time 18 -o "$out" -w '%{http_code}' \
      "https://raw.githubusercontent.com/$repo/HEAD/$p" 2>/dev/null)
    if [ "$code" = "200" ]; then printf '%s\t%s\n' "$p" "$(wc -c < "$out" | tr -d ' ')"; return 0; fi
  done < <(licence_paths)
  return 1
}
