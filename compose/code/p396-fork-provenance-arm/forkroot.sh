#!/bin/bash
# p396 fork-provenance arm. 395-A asked for one HTML read per address; HTML is
# WebFetch-only here, so this does it in git instead: a fork SHARES the
# upstream's root commit. Shell-executable, no HTML, no API.
root_of() {
  d=$(mktemp -d)
  git clone --filter=blob:none --no-checkout -q "https://github.com/$1" "$d" 2>/dev/null || { echo "CLONE-FAIL"; rm -rf "$d"; return; }
  git -C "$d" rev-list --max-parents=0 HEAD 2>/dev/null | sort | tr '\n' ',' | cut -c1-40
  rm -rf "$d"
}
a_root=$(root_of "$1"); b_root=$(root_of "$2")
if [ "$a_root" = "CLONE-FAIL" ] || [ "$b_root" = "CLONE-FAIL" ]; then v="INCONCLUSIVE"
elif [ "$a_root" = "$b_root" ]; then v="SHARED-ROOT -> FORK LINEAGE"
else v="DISTINCT-ROOT -> INDEPENDENT"; fi
printf '%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "${a_root:0:12}" "${b_root:0:12}" "$v"
