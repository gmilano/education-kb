#!/bin/bash
# p397 — `396-F`'s arm returns "FORK LINEAGE" on a shared root. That label is a STRING
# matched to a PROPERTY (`Trend 25`): a shared root commit is shared ANCESTRY, which is
# equally implied by a true fork, an org RENAME, a repository TRANSFER and a re-push.
# p397's shelf run proved this matters: 15 of 19 shared a root and several are renames.
#
# The discriminator is cheap and needs no HTML: compare HEAD as well as root.
#   shared root + same HEAD      -> SAME-REPO  (alias/redirect: ONE artefact, two addresses)
#   shared root + different HEAD -> DIVERGENT-FORK (two artefacts, one ancestry)
#   distinct root                -> INDEPENDENT
probe() {
  d=$(mktemp -d)
  if ! git clone --filter=blob:none --no-checkout -q "https://github.com/$1" "$d" 2>/dev/null; then
    echo "FAIL FAIL"; rm -rf "$d"; return
  fi
  r=$(git -C "$d" rev-list --max-parents=0 HEAD 2>/dev/null | sort | tr '\n' ',' | cut -c1-12)
  h=$(git -C "$d" rev-parse --short=12 HEAD 2>/dev/null)
  echo "$r $h"
  rm -rf "$d"
}
read -r a_root a_head <<<"$(probe "$1")"
read -r b_root b_head <<<"$(probe "$2")"
if [ "$a_root" = "FAIL" ] || [ "$b_root" = "FAIL" ]; then v="INCONCLUSIVE-UNRESOLVABLE"
elif [ "$a_root" != "$b_root" ]; then v="INDEPENDENT"
elif [ "$a_head" = "$b_head" ]; then v="SAME-REPO-ALIAS"
else v="DIVERGENT-FORK"; fi
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "${a_root%,}" "${b_root%,}" "$a_head" "$b_head" "$v"
