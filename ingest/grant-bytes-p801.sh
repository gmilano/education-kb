#!/usr/bin/env bash
# p801 — grant BYTES over the git smart-HTTP transport (T954).
# Channel note: curl -sI and api.github.com both refuse in this session (T923, eighth pass),
# but `git -c protocol.version=2 fetch --depth 1 --filter=blob:none` resolves and
# `git cat-file blob` lazily fetches the payload. This yields LICENCE BYTES, which the
# rendered-HTML channel (T952) cannot. Negative control: an invented address fails with an
# auth challenge, never a silent empty success.
# Usage: grant-bytes-p801.sh <slugs-file> <workdir> <out.tsv>
set -uo pipefail
SLUGS=$1; W=$2; OUT=$3
mkdir -p "$W"
printf 'slug\tstatus\thead_commit\tlicence_path\tbytes\tsha256_raw\tsha256_norm\tfamily\tnorm_bytes\n' > "$OUT"

family() {  # $1 = file
  local f=$1
  if   grep -qi 'GNU AFFERO GENERAL PUBLIC LICENSE' "$f"; then echo AGPL-3.0
  elif grep -qi 'GNU LESSER GENERAL PUBLIC LICENSE'  "$f"; then echo LGPL
  elif grep -qi 'GNU GENERAL PUBLIC LICENSE'         "$f"; then echo GPL
  elif grep -qi 'Apache License'                     "$f"; then echo Apache-2.0
  elif grep -qi 'Permission is hereby granted, free of charge' "$f"; then
       grep -qi 'Portions of this software are licensed as follows' "$f" && echo MIT-dual || echo MIT
  elif grep -qi 'Redistribution and use in source and binary forms' "$f"; then
       grep -qi 'Neither the name' "$f" && echo BSD-3-Clause || echo BSD-2-Clause
  elif grep -qi 'Mozilla Public License'             "$f"; then echo MPL-2.0
  else echo UNCLASSIFIED; fi
}

while read -r slug; do
  [ -z "$slug" ] && continue
  case "$slug" in \#*) continue;; esac
  d="$W/$(echo "$slug" | tr '/' '_')"
  rm -rf "$d"; mkdir -p "$d"; ( cd "$d" && git init -q . && git remote add origin "https://github.com/$slug" ) || true
  if ! ( cd "$d" && timeout 300 git -c protocol.version=2 fetch -q --depth 1 --filter=blob:none origin HEAD 2>/dev/null ); then
    printf '%s\tFETCH_REFUSED\t-\t-\t-\t-\t-\t-\t-\n' "$slug" >> "$OUT"; continue
  fi
  head=$( cd "$d" && git rev-parse FETCH_HEAD 2>/dev/null )
  # root tree, pick the licence payload: exact LICENSE, then LICENSE.md/.txt, then COPYING
  # D1 (p801): awk IGNORECASE is a gawk extension and is IGNORED by this awk, so a lowercase
  # `license.txt` was reported as NO_ROOT_LICENCE_BLOB. Case folding now happens in grep -iE.
  line=$( cd "$d" && git cat-file -p FETCH_HEAD^{tree} 2>/dev/null | awk '$2=="blob"' \
          | grep -iE '[[:space:]](LICENSE|LICENCE|COPYING)(\.md|\.txt|\.rst)?$' | head -1 )
  if [ -z "$line" ]; then
    printf '%s\tNO_ROOT_LICENCE_BLOB\t%s\t-\t-\t-\t-\t-\t-\n' "$slug" "$head" >> "$OUT"; continue
  fi
  bsha=$( echo "$line" | awk '{print $3}' ); bpath=$( echo "$line" | awk '{print $4}' )
  if ! ( cd "$d" && timeout 240 git cat-file blob "$bsha" > "$d/payload" 2>/dev/null ); then
    printf '%s\tBLOB_REFUSED\t%s\t%s\t-\t-\t-\t-\t-\n' "$slug" "$head" "$bpath" >> "$OUT"; continue
  fi
  bytes=$( wc -c < "$d/payload" | tr -d ' ' )
  raw=$( sha256sum "$d/payload" | cut -d' ' -f1 )
  # normalised clause: drop copyright/holder lines, collapse whitespace — holder names must not move the hash
  grep -vi 'copyright' "$d/payload" | tr -s '[:space:]' ' ' | sed 's/^ //; s/ $//' > "$d/norm"
  norm=$( sha256sum "$d/norm" | cut -d' ' -f1 ); nbytes=$( wc -c < "$d/norm" | tr -d ' ' )
  printf '%s\tOK\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$head" "$bpath" "$bytes" "$raw" "$norm" "$(family "$d/payload")" "$nbytes" >> "$OUT"
done < "$SLUGS"
