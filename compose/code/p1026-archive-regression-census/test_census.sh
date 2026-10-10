#!/usr/bin/env bash
# Tests for p1026 census.sh. Offline: builds a fixture tree, no network.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
pass=0; fail=0
ok()   { pass=$((pass+1)); printf 'ok   %s\n' "$1"; }
no()   { fail=$((fail+1)); printf 'FAIL %s — %s\n' "$1" "$2"; }

fixture() {
  d="$(mktemp -d)"
  mkdir -p "$d/archive/snap" "$d/live" "$d/compose/code/p1026-archive-regression-census"
  cat > "$d/archive/snap/a.md" <<'EOF'
[kept](https://github.com/org/kept) [lost](https://github.com/org/lost)
[ctrl](https://github.com/ghost/nope-nope-nope) [case](https://github.com/Org/CaseRepo)
EOF
  cat > "$d/live/l.md" <<'EOF'
[kept](https://github.com/org/kept) [new](https://github.com/org/brandnew)
[case](https://github.com/org/caserepo)
EOF
  printf 'ghost/nope-nope-nope\n' > "$d/compose/code/p1026-archive-regression-census/excluded-controls.txt"
  printf '%s\n' "$d"
}

# 1 — an address in the archive and in no live page is LOST
d="$(fixture)"
out="$(EXCLUDE="$d/compose/code/p1026-archive-regression-census/excluded-controls.txt" \
       bash "$HERE/census.sh" "$d" "$d/archive" 2>/dev/null)"
printf '%s\n' "$out" | grep -qP '^LOST\torg/lost$' \
  && ok "lost address reported" || no "lost address reported" "got: $out"

# 2 — an address present in both is NOT reported
printf '%s\n' "$out" | grep -q 'org/kept' \
  && no "kept address silent" "org/kept was reported" || ok "kept address silent"

# 3 — a live-only address is never reported (the census is one-directional)
printf '%s\n' "$out" | grep -q 'org/brandnew' \
  && no "live-only silent" "org/brandnew was reported" || ok "live-only silent"

# 4 — case folding: archive 'Org/CaseRepo' matches live 'org/caserepo'
printf '%s\n' "$out" | grep -qi 'caserepo' \
  && no "case folded" "CaseRepo reported despite lowercase live hit" || ok "case folded"

# 5 — an excluded control is classed CONTROL, never LOST
printf '%s\n' "$out" | grep -qP '^CONTROL\tghost/nope-nope-nope$' \
  && ok "control classed, not lost" || no "control classed, not lost" "got: $out"

# 6 — SELF-REFERENCE: a committed result file must not suppress the next run
d2="$(fixture)"
printf 'LOST\thttps://github.com/org/lost\n' > "$d2/compose/code/p1026-archive-regression-census/result.2026-01-01.tsv"
out2="$(EXCLUDE="$d2/compose/code/p1026-archive-regression-census/excluded-controls.txt" \
        bash "$HERE/census.sh" "$d2" "$d2/archive" 2>/dev/null)"
printf '%s\n' "$out2" | grep -qP '^LOST\torg/lost$' \
  && ok "own result does not erase the finding" \
  || no "own result does not erase the finding" "got: $out2"

# 7 — a result file copied OUTSIDE the instrument dir is excluded by NAME too
d3="$(fixture)"
printf 'https://github.com/org/lost\n' > "$d3/live/held-only-in-a-worklist.2026-01-01.txt"
out3="$(EXCLUDE="$d3/compose/code/p1026-archive-regression-census/excluded-controls.txt" \
        bash "$HERE/census.sh" "$d3" "$d3/archive" 2>/dev/null)"
printf '%s\n' "$out3" | grep -qP '^LOST\torg/lost$' \
  && ok "name-based exclusion travels" || no "name-based exclusion travels" "got: $out3"

# 8 — a missing archive dir is an empty census, not a crash
d4="$(fixture)"
bash "$HERE/census.sh" "$d4" "$d4/nosuchdir" >/dev/null 2>&1 \
  && ok "missing archive exits 0" || no "missing archive exits 0" "non-zero exit"

# 9 — a missing exclude file degrades to no exclusions, not a crash
d5="$(fixture)"
out5="$(EXCLUDE="$d5/nosuchfile" bash "$HERE/census.sh" "$d5" "$d5/archive" 2>/dev/null)"
printf '%s\n' "$out5" | grep -qP '^LOST\tghost/nope-nope-nope$' \
  && ok "no exclude file → control falls through as LOST" \
  || no "no exclude file → control falls through as LOST" "got: $out5"

printf '\n%d passed, %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
