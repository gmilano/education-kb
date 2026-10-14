#!/usr/bin/env bash
# p208 -- ACTION PT, the seeding half. Builds a SCRATCH COPY of the KB's
# markdown with N deliberately wrong licence cells, so the audit can be asked
# whether it finds them. Nothing here touches the published tree.
#
# Each seed names the shape it tests, because PT's answer turned out to be
# conditional on the shape rather than uniform:
#   D = the true family is printed at exactly ONE site  -> seeding it removes
#       the family from the union the audit compares against
#   M = the true family is printed at TWO OR MORE sites -> the union still
#       contains it after seeding, so no comparison can fire
set -u
SRC="${1:?source kb dir}"; DST="${2:?scratch dir}"
rm -rf "$DST"; mkdir -p "$DST"
( cd "$SRC" && tar cf - agents repos verticals intel compose/patterns.md evidence/permissive-half-census.2026-10-14-p207.tsv ) | ( cd "$DST" && tar xf - )
mkdir -p "$DST/compose"

# seed <repo> <true-token-regex> <replacement> <shape>
seed() {
  local repo="$1" pat="$2" rep="$3" shape="$4" hit
  hit=$(grep -rlZ --include='*.md' -F "$repo" "$DST" | tr '\0' '\n' | while read -r f; do
          grep -nE "$pat" "$f" | grep -F "$repo" | head -1 | sed "s|^|$f:|"; done | head -1)
  if [ -z "$hit" ]; then printf '%s\tSEED-FAILED\t%s\n' "$repo" "$shape"; return 1; fi
  local file line
  file=${hit%%:*}; line=$(printf '%s' "$hit" | cut -d: -f2)
  sed -i "${line}s/${pat}/${rep}/" "$file"
  printf '%s\t%s\t%s\t%s:%s\n' "$repo" "SEEDED->$rep" "$shape" "${file#$DST/}" "$line"
}
printf 'repo\tseed\tshape\tsite\n'
seed '2022764025/Lecture-Hunter'      'MIT'          'AGPL-3.0' 'D1 current-state table cell, single truth site'
seed 'DecoyLex/ltix'                  'MIT'          'GPL-3.0'  'D2 single truth site, different file'
seed '0voice/Awesome-CS-OpenCourse'   'CC0-1\.0'     'MIT'      'D3 single truth site, non-code grant'
seed 'HKUDS/DeepTutor'                'Apache-2\.0'  'MIT'      'M1 150 mention lines, truth at many sites'
seed 'openedx/edx-platform'           'AGPL-3\.0'    'MIT'      'M2 158 mention lines, truth at many sites'
