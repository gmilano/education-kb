#!/usr/bin/env bash
# p550 — INVERSION ORACLE.
#
# The sweep proves a divergent shadow EXISTS.  This oracle measures what it would COST, which
# is the difference between "dead code, tidy it up sometime" and "the shelf's licence verdicts
# depend on source order".
#
# Method: extract both bodies of `commercial_use_ok` from the shared control, bind the shadowed
# one under a second name, and run BOTH over every real licence payload in this tree.  No
# synthetic fixtures -- the question is what happens to THIS KB's shelf, so the corpus is this
# KB's own payloads.
#
# P542 applied to this oracle: with no payload corpus it exits 2.
set -uo pipefail

LIB="${1:-}"
CORPUS_ROOT="${2:-}"
[ -n "$LIB" ] && [ -n "$CORPUS_ROOT" ] || {
  echo "usage: $0 <license_family.sh> <corpus-root>" >&2
  echo "p550-oracle: REFUSED — no library/corpus given, nothing judged" >&2; exit 2; }
[ -f "$LIB" ] || { echo "p550-oracle: REFUSED — not a file: $LIB" >&2; exit 2; }
[ -d "$CORPUS_ROOT" ] || { echo "p550-oracle: REFUSED — not a directory: $CORPUS_ROOT" >&2; exit 2; }

n_defs=$(grep -cE '^commercial_use_ok\(\)' "$LIB")
if [ "$n_defs" -lt 2 ]; then
  echo "p550-oracle: no shadow in $LIB (n_defs=$n_defs) — nothing to invert" >&2
  echo "SHADOW-ABSENT"
  exit 0
fi

# shellcheck source=/dev/null
. "$LIB"   # live resolution, whatever the file's order yields

# Bind definition #1 (the shadowed one) as shadow_cuo.
eval "shadow_cuo() {
$(awk '/^commercial_use_ok\(\)/{c++} c==1 && !/^commercial_use_ok\(\)/ {print} c==1 && /^}/{exit}' "$LIB")"

mapfile -t payloads < <(find "$CORPUS_ROOT" -type f \
  \( -iname '*LICENSE*' -o -iname 'COPYING*' \) ! -name '*.py' ! -name '*.sh' | sort)

[ "${#payloads[@]}" -gt 0 ] || {
  echo "p550-oracle: REFUSED — corpus held no licence payload, nothing judged" >&2; exit 2; }

printf 'payload\tfamily\tlive\tshadowed\tinverts\n'
inv=0; tot=0
for f in "${payloads[@]}"; do
  p=$(cat "$f") || continue
  [ -n "$p" ] || continue
  tot=$((tot+1))
  if commercial_use_ok "$p"; then a=ALLOWED; else a=PROHIBITED; fi
  if shadow_cuo       "$p"; then b=ALLOWED; else b=PROHIBITED; fi
  fam=$(family_of "$p")
  if [ "$a" != "$b" ]; then v=YES; inv=$((inv+1)); else v=no; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "${f#"$CORPUS_ROOT"/}" "$fam" "$a" "$b" "$v"
done

echo "p550-oracle: payloads=$tot inverted=$inv" >&2
[ "$inv" -eq 0 ]
