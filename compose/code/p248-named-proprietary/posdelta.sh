#!/bin/bash
# What POSITION A (the name above every anchor) would have changed, measured without
# taking the risk: a payload an anchor already claims AND that carries a proprietary name.
cd /tmp/education-kb || exit 1
. compose/code/lib/license_family.sh
printf 'file\tfamily_now\tname_found\tposition_A_would_say\tcommercial_now\n'
awk -F'\t' '{print $1}' "$1" | while read -r f; do
  p=$(cat "$f")
  fam=$(osi_family_of "$p")
  case "$fam" in NAMED-PROPRIETARY*) continue ;; esac
  nm=$(named_proprietary_of "$p")
  [ -z "$nm" ] && continue
  if commercial_use_ok "$p"; then c=ALLOWED; else c=DENIED; fi
  printf '%s\t%s\t%s\tNAMED-PROPRIETARY (%s)\t%s\n' "$f" "$fam" "$nm" "$nm" "$c"
done
