#!/usr/bin/env bash
# p250 — the shared probe for `ACTION XJ` (slug repair) and `ACTION XK` (tier B/C reach).
#
# Channels, re-calibrated this pass before any negative was believed:
#   existence : github.com/<slug>/info/refs?service=git-upload-pack
#               200 = EXISTS, 401 = ABSENT.  p249's channel map recorded the 200 but not
#               the 401, so no earlier pass could separate ABSENT from grantless without
#               a second request.  One request now does both.
#   payload   : raw.githubusercontent.com/<slug>/HEAD/<path>
#               200 = FOUND, 404 = absent-at-the-path-probed (p222's rule: never
#               "unlicensed").  `HEAD` resolves whatever the default branch is called.
#
# usage: probe.sh <slugs-file> <tiers: A|AB|ABC>
set -uo pipefail
TIER_A=(LICENSE-CODE LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.txt COPYING COPYING.txt
        COPYING.md COPYING.LESSER license.txt license.md License.txt copying.txt LICENSE.rst NOTICE)
TIER_B=(docs/License.txt docs/LICENSE docs/LICENSE.txt docs/license.txt html/license.txt
        public/COPYING.txt public/LICENSE public/license.txt LICENSE/LICENSE licenses/LICENSE
        LICENSES/LICENSE legal/LICENSE doc/LICENSE app/LICENSE src/LICENSE)
TIER_C=(version.php composer.json package.json pyproject.toml setup.py)

slugs=$1; tiers=${2:-A}
paths=("${TIER_A[@]}")
[[ $tiers == AB || $tiers == ABC ]] && paths+=("${TIER_B[@]}")
[[ $tiers == ABC ]] && paths+=("${TIER_C[@]}")

printf 'slug\texists_code\texistence\tgrant_path\tpath_tier\tbytes\tsha256_16\tfamily\n'
while IFS= read -r slug; do
  [[ -z $slug || $slug == \#* ]] && continue
  ec=$(curl -s -o /dev/null -w '%{http_code}' --max-time 25 \
       "https://github.com/$slug/info/refs?service=git-upload-pack")
  case $ec in
    200) ex=EXISTS ;;
    401|404) ex=ABSENT ;;
    *) ex="UNDECIDED-$ec" ;;
  esac
  if [[ $ex != EXISTS ]]; then
    printf '%s\t%s\t%s\t-\t-\t-\t-\t-\n' "$slug" "$ec" "$ex"; continue
  fi
  found=
  for p in "${paths[@]}"; do
    body=$(curl -s --max-time 25 -w '\n%{http_code}' \
           "https://raw.githubusercontent.com/$slug/HEAD/$p")
    code=${body##*$'\n'}; text=${body%$'\n'*}
    [[ $code != 200 ]] && continue
    n=${#text}
    (( n < 1 )) && continue              # byte-floor=1B (p1058: a 0-byte grant is an ABSENCE)
    h=$(printf '%s' "$text" | sha256sum | cut -c1-16)
    tier=A; for b in "${TIER_B[@]}"; do [[ $p == "$b" ]] && tier=B; done
    for c in "${TIER_C[@]}"; do [[ $p == "$c" ]] && tier=C; done
    fam=UNRECOGNISED
    grep -qi 'MIT License' <<<"$text" && fam=MIT
    grep -qi 'Apache License' <<<"$text" && fam=Apache-2.0
    grep -qi 'BSD 3-Clause\|Redistributions of source code' <<<"$text" && fam=BSD-like
    grep -qi 'GNU AFFERO' <<<"$text" && fam=AGPL-3.0
    grep -qi 'GNU LESSER' <<<"$text" && fam=LGPL
    grep -qi 'Mozilla Public License' <<<"$text" && fam=MPL-2.0
    grep -qi 'Educational Community License' <<<"$text" && fam=ECL-2.0
    grep -qi 'This is free and unencumbered' <<<"$text" && fam=Unlicense
    grep -qi 'Creative Commons' <<<"$text" && fam=CC
    [[ $tier == C ]] && fam="MANIFEST-CLAIM-NOT-A-PAYLOAD"
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$ec" "$ex" "$p" "$tier" "$n" "$h" "$fam"
    found=1; break
  done
  [[ -z $found ]] && printf '%s\t%s\t%s\t-\tNONE-AT-TIER-%s\t-\t-\tNO-GRANT-AT-TIER-%s\n' \
      "$slug" "$ec" "$ex" "$tiers" "$tiers"
done < "$slugs"
