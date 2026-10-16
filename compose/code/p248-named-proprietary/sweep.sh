#!/bin/bash
# Blast-radius sweep: family_of + commercial_use_ok over every FIXTURE PAYLOAD.
# The population is defined by EXCLUSION of script/data extensions, so it is reproducible
# and its count is printed rather than quoted from a previous pass.
cd /tmp/education-kb || exit 1
. compose/code/lib/license_family.sh
out="$1"
: > "$out"
find compose/code -path '*fixtures*' -type f \
  ! -name '*.py' ! -name '*.sh' ! -name '*.json' ! -name '*.tsv' \
  ! -name '*.expected' ! -name '*.toml' ! -name '*.xml' \
  | sort | while read -r f; do
    p=$(cat "$f")
    fam=$(osi_family_of "$p")
    if commercial_use_ok "$p"; then c=ALLOWED; else c=DENIED; fi
    printf '%s\t%s\t%s\n' "$f" "$fam" "$c" >> "$out"
  done
wc -l < "$out"
