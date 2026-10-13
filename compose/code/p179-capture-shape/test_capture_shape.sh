#!/usr/bin/env bash
# Suite for `ACTION KY`'s instruments.  `P355`: every fixture is built in a scratch tree, so the
# suite never depends on the repository it guards and can run in any order.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
pass=0; fail=0
ok()  { printf 'ok   %-62s %s\n' "$1" "${2:-}"; pass=$((pass + 1)); }
no()  { printf 'FAIL %-62s %s\n' "$1" "${2:-}"; fail=$((fail + 1)); }
chk() { [ "$2" = "$3" ] && ok "$1" "$2" || no "$1" "got '$2' want '$3'"; }

T=$(mktemp -d); trap 'rm -rf "$T"' EXIT

echo "== 1. The class-C channel is AMBIGUOUS, not merely lossy =="
if bash "$HERE/ambiguity_proof.sh" >"$T/amb.out" 2>&1; then
  ok "ambiguity_proof exits 0 (three sizes -> one byte string)" "$(grep -c AMBIGUOUS "$T/amb.out")"
else
  no "ambiguity_proof exits 0" "it exited non-zero — the 6 class-C readings would be wrong"
fi
chk "and the three recoveries share ONE md5" \
  "$(awk -F'\t' 'NR>1 && NF>3 {print $4}' "$T/amb.out" | sort -u | wc -l | tr -d ' ')" "1"
chk "while the true sizes are THREE distinct values" \
  "$(awk -F'\t' 'NR>1 && NF>3 {print $2}' "$T/amb.out" | sort -u | wc -l | tr -d ' ')" "3"

echo
echo "== 2. The trailing-run census reads the run, and does not assume it is 1 =="
mkdir -p "$T/corpus"
printf 'no trailing newline' > "$T/corpus/run0"
printf 'one\n' > "$T/corpus/run1"
printf 'three\n\n\n' > "$T/corpus/run3"
bash "$HERE/trailing_census.sh" "$T/corpus" > "$T/cen.tsv"
chk "run0 -> 0" "$(awk -F'\t' '$1=="run0"{print $4}' "$T/cen.tsv")" "0"
chk "run1 -> 1" "$(awk -F'\t' '$1=="run1"{print $4}' "$T/cen.tsv")" "1"
chk "run3 -> 3 (the ENTIRE run, which 'P834 = +1 byte' gets wrong)" \
  "$(awk -F'\t' '$1=="run3"{print $4}' "$T/cen.tsv")" "3"
bash "$HERE/trailing_census.sh" "$T/nonexistent" >/dev/null 2>&1
chk "refuses a missing corpus with exit 2 (a census over nothing)" "$?" "2"

echo
echo "== 3. The capture gate flags the CAPTURE, and only when a count follows =="
mkdir -p "$T/tree/compose/code/subject" "$T/tree/ingest"
cat > "$T/tree/compose/code/subject/bad.sh" <<'EOF'
body=$(curl -sS "https://example.invalid/LICENSE")
bytes=$(printf '%s' "$body" | wc -c)
EOF
cat > "$T/tree/compose/code/subject/good_fetch.sh" <<'EOF'
code=$(curl -sS -o "$dest" -w '%{http_code}' "https://example.invalid/LICENSE")
bytes=$(wc -c < "$dest")
EOF
cat > "$T/tree/compose/code/subject/classify_only.sh" <<'EOF'
body=$(curl -sS "https://example.invalid/LICENSE")
family=$(printf '%s' "$body" | grep -o MIT)
EOF
bash "$HERE/capture_gate.sh" "$T/tree" > "$T/g1.out" 2>&1
chk "flags capture-then-size" \
  "$(grep -c 'subject/bad.sh' "$T/g1.out")" "1"
chk "does NOT flag the -o FILE idiom (the body never enters a variable)" \
  "$(grep -c 'good_fetch.sh' "$T/g1.out")" "0"
chk "does NOT flag a classify-only capture (newline-insensitive, and correct)" \
  "$(grep -c 'classify_only.sh' "$T/g1.out")" "0"
rm "$T/tree/compose/code/subject/bad.sh"
bash "$HERE/capture_gate.sh" "$T/tree" >/dev/null 2>&1
chk "exits 0 on a clean tree" "$?" "0"

echo
echo "== 4. The fetch idiom this repository was missing =="
. "$HERE/../lib/fetch_payload_to_file.sh"
chk "fetch_payload_to_file is defined" "$(type -t fetch_payload_to_file)" "function"
chk "fetch_raw_to_file is defined" "$(type -t fetch_raw_to_file)" "function"
printf 'payload\n' > "$T/written"
. "$HERE/../lib/payload_measure.sh" 2>/dev/null || true
if [ "$(type -t size_of_file)" = "function" ]; then
  chk "size_of_file on a WRITTEN file keeps the trailing run" "$(size_of_file "$T/written")" "8"
else
  no "size_of_file reachable from the fetch idiom" "payload_measure.sh did not source"
fi

echo
printf '%s/%s\n' "$pass" "$((pass + fail))"
[ "$fail" -eq 0 ]
