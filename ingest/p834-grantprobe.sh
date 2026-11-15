#!/usr/bin/env bash
# p834 grant probe v2.
#  - RESTORES the full 31-name filename list (instrument limb of ACTION p833-C; p833 ran at 10).
#  - RESOLVES THE DEFAULT BRANCH FIRST from the search index (D834).  p833 ordered main/master/dev
#    by a hardcoded preference, so the FIRST 200 won even when it sat on a branch the project does
#    not ship.  Measured on yinuoguan/nengdou-ai-review-helper-web: main/LICENSE = Apache-2.0
#    (11,357 B) while the default branch master/LICENSE = MulanPSL-2.0 (9,247 B).  p833's probe
#    returned the Apache limb silently.  T112 hardened the branch axis against false ABSENCE;
#    this hardens it against false PRESENCE ON THE WRONG BRANCH.
#  - Every verdict prints which branch was used, whether it was the DEFAULT, the ref set and the
#    name count, so a verdict is falsifiable on both axes without re-running it.
# Verdicts: GRANT / NO-GRANT-AT-ROOT / EMPTY-REF-SET.
set -u
slug="$1"
dir="${GRANTPROBE_OUT:-$(mktemp -d)}"; mkdir -p "$dir"
heads=$(git ls-remote --heads "https://github.com/$slug" 2>/dev/null | awk '{sub("refs/heads/","",$2); print $2}')
if [ -z "$heads" ]; then echo "$slug :: EMPTY-REF-SET (dead or unreachable address) :: refs=[]"; exit 0; fi
# D834: the DEFAULT branch, from the one metadata channel this session has (search index).
dflt=$(gh api -X GET search/repositories -f q="repo:$slug" --jq '.items[0].default_branch' 2>/dev/null)
case "$dflt" in ""|null) dflt=""; esac
ordered=$(printf '%s\n' $heads | awk -v d="$dflt" '{print ($0==d?0:($0=="main"?1:($0=="master"?2:3)))"\t"$0}' | sort -s -k1,1n | cut -f2 | head -6)
NAMES="LICENSE LICENSE.md LICENSE.txt LICENSE.rst License License.md LICENCE LICENCE.md LICENCE.txt \
license license.md license.txt licence licence.md COPYING COPYING.txt COPYING.md COPYRIGHT \
LICENSE-MIT LICENSE-APACHE MIT-LICENSE MIT-LICENSE.txt UNLICENSE UNLICENSE.txt LICENSE.html \
docs/LICENSE doc/LICENSE LICENSE/LICENSE LICENSES/LICENSE .github/LICENSE LICENSE-2.0.txt"
n=$(printf '%s\n' $NAMES | wc -l)
for br in $ordered; do
  for fn in $NAMES; do
    out="$dir/$(echo "$slug" | tr '/' '%')-$br-$(echo "$fn" | tr '/' '%')"
    code=$(curl -sS --max-time 20 -o "$out" -w '%{http_code}' "https://raw.githubusercontent.com/$slug/$br/$fn" 2>/dev/null)
    if [ "$code" = "200" ]; then
      [ "$br" = "$dflt" ] && isd="DEFAULT" || isd="NON-DEFAULT(default=${dflt:-UNKNOWN})"
      printf '%s :: GRANT at %s/%s [%s] :: bytes=%s sha256=%s :: head="%s" :: refs=[%s] names=%s\n' \
        "$slug" "$br" "$fn" "$isd" "$(wc -c <"$out")" "$(sha256sum "$out" | cut -c1-12)" \
        "$(head -2 "$out" | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-60)" "$(printf '%s ' $ordered)" "$n"
      exit 0
    fi
    rm -f "$out"
  done
done
printf '%s :: NO-GRANT-AT-ROOT :: probed %s filenames x %s refs (default=%s) :: refs=[%s]\n' \
  "$slug" "$n" "$(printf '%s\n' $ordered | wc -l)" "${dflt:-UNKNOWN}" "$(printf '%s ' $ordered)"
