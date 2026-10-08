#!/usr/bin/env bash
# p550 suite — offline, no network, no clone.  Mutants included: a test that cannot fail on a
# broken instrument is not a test (this KB's own P542 lesson, applied before publishing).
set -uo pipefail
cd "$(dirname "$0")"
pass=0; fail=0
ok()   { pass=$((pass+1)); printf 'ok   %s\n' "$1"; }
bad()  { fail=$((fail+1)); printf 'FAIL %s  (%s)\n' "$1" "${2:-}"; }
chk()  { if [ "$2" = "$3" ]; then ok "$1"; else bad "$1" "want=$3 got=$2"; fi; }

TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT

# ---------- fixtures, written here so the suite is self-contained ----------
mkdir -p "$TMP/t"
cat > "$TMP/t/divergent.sh" <<'EOF'
f() { return 0; }
f() { return 1; }
EOF
cat > "$TMP/t/identical.sh" <<'EOF'
g() { return 0; }
g() { return 0; }
EOF
cat > "$TMP/t/single.sh" <<'EOF'
h() { return 0; }
EOF
cat > "$TMP/t/lib.PRE-P999-CONTROL-2026-01-01.sh" <<'EOF'
k() { return 0; }
k() { return 1; }
EOF
cat > "$TMP/t/py_divergent.py" <<'EOF'
def d():
    return 0
def d():
    return 1
EOF
# P550c direction 1 -- a heredoc that merely CONTAINS two definitions is not a duplicate.
{ printf 'emit() {\n'
  printf '  cat <<%sX%s\n' "'" "'"
  printf 'bait() { return 0; }\n'
  printf 'bait() { return 1; }\n'
  printf 'X\n}\n'; } > "$TMP/t/heredoc_bait.sh"
# P550c direction 2 -- stripping must not HIDE a real duplicate that follows a heredoc.
{ printf 'emit() {\n'
  printf '  cat <<%sX%s\n' "'" "'"
  printf 'noise\n'
  printf 'X\n}\n'
  printf 'real() { return 0; }\n'
  printf 'real() { return 1; }\n'; } > "$TMP/t/heredoc_then_real.sh"

out=$(./sweep_dupdefs.sh "$TMP/t" 2>/dev/null); rc=$?

# ---------- P542: refusals ----------
./sweep_dupdefs.sh >/dev/null 2>&1; chk "P542 no args -> exit 2" "$?" 2
./sweep_dupdefs.sh /nonexistent-xyz >/dev/null 2>&1; chk "P542 bad root -> exit 2" "$?" 2
mkdir -p "$TMP/empty"
./sweep_dupdefs.sh "$TMP/empty" >/dev/null 2>&1; chk "P542 root with no source -> exit 2" "$?" 2

# ---------- classification ----------
chk "divergent shell pair -> SHADOWED-DIVERGENT" \
  "$(echo "$out" | awk -F'\t' '$1 ~ /divergent.sh$/ {print $5}')" "P550-SHADOWED-DIVERGENT"
chk "identical shell pair -> REDUNDANT-IDENTICAL (not padded as a finding)" \
  "$(echo "$out" | awk -F'\t' '$1 ~ /identical.sh$/ {print $5}')" "P550-REDUNDANT-IDENTICAL"
chk "frozen control snapshot -> FROZEN-CONTROL, declared not accused" \
  "$(echo "$out" | awk -F'\t' '$1 ~ /PRE-P999-CONTROL/ {print $5}')" "P550-FROZEN-CONTROL"
chk "python divergent pair detected" \
  "$(echo "$out" | awk -F'\t' '$1 ~ /py_divergent.py$/ {print $5}')" "P550-SHADOWED-DIVERGENT"
chk "single definition is not reported at all" \
  "$(echo "$out" | awk -F'\t' '$1 ~ /single.sh$/ {print $5}' | wc -l | tr -d ' ')" "0"
chk "divergent findings exit non-zero" "$rc" "1"

# clean tree -> exit 0
mkdir -p "$TMP/clean"; cp "$TMP/t/single.sh" "$TMP/clean/"
./sweep_dupdefs.sh "$TMP/clean" >/dev/null 2>&1; chk "clean tree -> exit 0" "$?" 0

# ---------- P550c: the two directions of the quoted-text defect ----------
chk "P550c heredoc-quoted definitions are NOT reported (no over-accusation)" \
  "$(echo "$out" | awk -F'\t' '$1 ~ /heredoc_bait.sh$/ {print $3}' | wc -l | tr -d ' ')" "0"
chk "P550c a real duplicate AFTER a heredoc is still reported (no false negative)" \
  "$(echo "$out" | awk -F'\t' '$1 ~ /heredoc_then_real.sh$/ {print $5}')" "P550-SHADOWED-DIVERGENT"

# ---------- MUTANTS ----------
# DECLARED ASYMMETRY.  The exit code is a convenience; the TABLE is the evidence.  The first
# cut of this suite asserted on the exit code alone and two mutants walked through it (M2
# dropped the counter, M3 forced the final test true) because both leave the published rows
# CORRECT and only the status lies.  That is P541's shape inside this instrument, so the
# instrument was changed -- the status is now computed from the emitted rows -- and the suite
# now reads the rows.  A mutant is killed when the TABLE stops being right, or when a status
# derived from a right table stops matching it.
mut_table() { # name, sed-expr, expected-class, file-regex-to-inspect
  local n="$1" e="$2" want="$3" probe="${4:-/divergent.sh$}"
  cp sweep_dupdefs.sh "$TMP/m.sh"; cp strip_quoted.awk "$TMP/strip_quoted.awk"
  sed -i "$e" "$TMP/m.sh"
  local got
  got=$(bash "$TMP/m.sh" "$TMP/t" 2>/dev/null | awk -F'\t' -v re="$probe" '$1 ~ re {print $5}')
  if [ "$got" = "$want" ]; then
    bad "mutant killed: $n" "table unchanged (still $got)"
  else ok "mutant killed: $n"; fi
}
mut_table "M1 misclassify divergence as identical" \
  's/class=P550-SHADOWED-DIVERGENT/class=P550-REDUNDANT-IDENTICAL/' "P550-SHADOWED-DIVERGENT"
mut_table "M2 drop the frozen-control exemption" \
  's/class=P550-FROZEN-CONTROL/class=P550-SHADOWED-DIVERGENT/' "P550-FROZEN-CONTROL" "PRE-P999-CONTROL"
mut_table "M3 compare only the first body (never see divergence)" \
  's/\[ "\$bi" = "\$b1" \] || differ=yes/:/' "P550-SHADOWED-DIVERGENT"

# M4: force the status true.  The table stays right, so this is caught by comparing the
# status AGAINST the table -- which is what the instrument now does internally.
cp sweep_dupdefs.sh "$TMP/m4.sh"; cp strip_quoted.awk "$TMP/strip_quoted.awk"
sed -i 's/\[ "\$findings" -eq 0 \]/true/' "$TMP/m4.sh"
m4tab=$(bash "$TMP/m4.sh" "$TMP/t" 2>/dev/null | awk -F'\t' '$5=="P550-SHADOWED-DIVERGENT"' | wc -l | tr -d ' ')
bash "$TMP/m4.sh" "$TMP/t" >/dev/null 2>&1; m4rc=$?
if [ "$m4tab" -gt 0 ] && [ "$m4rc" -eq 0 ]; then
  ok "M4 status/table disagreement is observable (table=$m4tab, status=0)"
else bad "M4 status/table disagreement is observable" "table=$m4tab rc=$m4rc"; fi

# ---------- the oracle ----------
./oracle_inversion.sh >/dev/null 2>&1; chk "P542 oracle no args -> exit 2" "$?" 2
./oracle_inversion.sh "$TMP/t/single.sh" "$TMP/t" >/dev/null 2>&1
chk "oracle on a lib with no shadow -> exit 0, SHADOW-ABSENT" "$?" 0
chk "oracle reports SHADOW-ABSENT when there is no duplicate" \
  "$(./oracle_inversion.sh "$TMP/t/single.sh" "$TMP/t" 2>/dev/null)" "SHADOW-ABSENT"
# P542 for the oracle's corpus channel.  NOTE the library used: the shared control was
# repaired by this very pass, so it now has ONE definition and the oracle correctly
# short-circuits on SHADOW-ABSENT before it ever looks at a corpus.  Reaching the corpus
# check therefore needs a library that still carries a shadow, and the tree has a real one:
# the frozen PRE-P308 control snapshot.  (The first cut of this test pointed at the live
# library and passed only because the library was still broken -- a test whose premise was
# the defect it was written alongside.)
SHADOWED_LIB=../p308-phrase-anchor-sweep/license_family.PRE-P308-CONTROL-2026-10-04.sh
chk "the frozen control still carries a shadow (premise of the next test)" \
  "$(grep -cE '^commercial_use_ok\(\)' "$SHADOWED_LIB")" "2"
mkdir -p "$TMP/nolic"; cp "$TMP/t/single.sh" "$TMP/nolic/"
./oracle_inversion.sh "$SHADOWED_LIB" "$TMP/nolic" >/dev/null 2>&1
chk "P542 oracle with no payload corpus -> exit 2" "$?" 2
# And the repaired shared control must now answer SHADOW-ABSENT -- this is the pass's fix,
# asserted rather than asserted-about.
chk "repaired shared control reports SHADOW-ABSENT" \
  "$(./oracle_inversion.sh ../lib/license_family.sh .. 2>/dev/null)" "SHADOW-ABSENT"
chk "repaired shared control has exactly one commercial_use_ok" \
  "$(grep -cE '^commercial_use_ok\(\)' ../lib/license_family.sh)" "1"

# ---------- the shared control must stay sound regardless ----------
# Whatever this pass does to the duplicate, the LIVE gate must answer these three.
# `P614` (pase 50 del 2026-10-08). Esta linea decia:
#     . /home/user/education-kb/compose/code/lib/license_family.sh
# una ruta ABSOLUTA a la raiz del repo, en la maquina del pase que la escribio. En cualquier
# otro clon el `source` FALLA, `commercial_use_ok` queda SIN DEFINIR, y entonces:
#   - `commercial_use_ok "$UNL"` -> «command not found» -> exit != 0 -> se reporta PROHIBITED
#   - `declare -f commercial_use_ok | grep -c NO-CESSION` -> 0
# o sea que la suite ACUSA al control compartido de dos defectos que NO TIENE. Medido este
# pase: con el lib sourceado por ruta relativa las dos aserciones pasan, y `p550` quedo ROJO
# en HEAD sin que ningun pase lo mirara -- la evidencia exacta de `Gap 255`.
#
# La ruta ahora es relativa, como las lineas 138/140 de esta misma suite ya la usaban. Y el
# `source` REHUSA en vez de degradar: una dependencia que no carga no puede volver a
# disfrazarse de defecto del control compartido (la leccion de Gap 243/245, aplicada al
# source y no solo a argv).
LIB=../lib/license_family.sh
if [ ! -r "$LIB" ]; then
  echo "REFUSE: no se puede leer $LIB desde $(pwd) — la suite no juzga nada sin el control compartido" >&2
  exit 2
fi
. "$LIB"
if ! declare -F commercial_use_ok >/dev/null; then
  echo "REFUSE: $LIB se cargo pero no define commercial_use_ok" >&2
  exit 2
fi
NC=$'Creative Commons Attribution-NonCommercial 4.0 International\nYou may not use the material for commercial purposes.'
if commercial_use_ok "$NC"; then bad "live gate: CC-BY-NC prohibited" "returned ALLOWED"; else ok "live gate: CC-BY-NC prohibited"; fi
UNL=$'This is free and unencumbered software released into the public domain.\nAnyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.'
if commercial_use_ok "$UNL"; then ok "live gate: Unlicense allowed (P308 anchor)"; else bad "live gate: Unlicense allowed" "returned PROHIBITED"; fi
chk "live gate: NO-CESSION branch present (hardened body is live)" \
  "$(declare -f commercial_use_ok | grep -c 'NO-CESSION')" "1"

echo
echo "$((pass))/$((pass+fail))"
[ "$fail" -eq 0 ]
