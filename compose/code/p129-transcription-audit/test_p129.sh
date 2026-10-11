#!/usr/bin/env bash
# test_p129.sh — fully offline. No network, no GitHub, no proxy.
cd "$(dirname "$0")" || exit 1
pass=0; fail=0
ok(){ if [ "$2" = "$3" ]; then pass=$((pass+1)); else fail=$((fail+1)); echo "FAIL: $1"; echo "  want: $3"; echo "  got : $2"; fi; }
has(){ case "$2" in *"$3"*) pass=$((pass+1));; *) fail=$((fail+1)); echo "FAIL: $1 (missing '$3')"; echo "  got : $2";; esac; }
hasnt(){ case "$2" in *"$3"*) fail=$((fail+1)); echo "FAIL: $1 (unexpected '$3')"; echo "  got : $2";; *) pass=$((pass+1));; esac; }

# ---- the counting rule -------------------------------------------------------
ok "annotated mix: 5 lines, 2 deref, 3 real" \
   "$(./count_tags.sh < fixtures/ls-remote-annotated.txt)" "$(printf '5\t2\t3\tv1.2.0')"
ok "lightweight: no inflation at all" \
   "$(./count_tags.sh < fixtures/ls-remote-lightweight.txt)" "$(printf '3\t0\t3\tv1.2.0')"
ok "no tags: zero, not an error" \
   "$(./count_tags.sh < fixtures/ls-remote-empty.txt)" "$(printf '0\t0\t0\t')"

# ---- the holder census ------------------------------------------------------
h(){ python3 -I holder.py < "fixtures/$1"; }
has "MIT with an unfilled holder field" "$(h licence-mit-placeholder.txt)" "MIT	PLACEHOLDER"
has "a leading © before the word Copyright is still a holder" \
    "$(h licence-mit-leading-copyright.txt)" "NAMED"
has "GPL-3's own FSF line is the LICENCE TEXT's holder, not the work's" \
    "$(h licence-gpl3-head.txt)" "DOCUMENT-TEXT"
hasnt "GPL-3 prose ('copyright on the Program') is not a holder line" \
      "$(h licence-gpl3-head.txt)" "on the Program"
hasnt "the GPL 'how to apply' placeholder is outside the operative text" \
      "$(h licence-gpl3-head.txt)" "name of author"
has "Apache-2.0 names no licensor in its operative text" \
    "$(h licence-apache2-appendix.txt)" "Apache-2.0	NO-HOLDER-IN-OPERATIVE-TEXT"
has "BSL-1.1 is read as BSL even though it names MIT as its Change License" \
    "$(h licence-bsl11-change-license-mit.txt)" "BSL-1.1 (NOT OSI)"
hasnt "BSL-1.1 is never classified MIT" "$(h licence-bsl11-change-license-mit.txt)" "	MIT	"
has "a markdown-link holder is named BY REFERENCE, not unfilled" \
    "$(h licence-bsd-link-holder.txt)" "HOLDER-BY-REFERENCE"

# ---- the repair, as a scope rather than a token -----------------------------
r(){ python3 -I - "$1" "$2" "$3" <<'PY'
import sys, importlib.util
spec = importlib.util.spec_from_file_location("rt", "repair_tags.py")
rt = importlib.util.module_from_spec(spec); spec.loader.exec_module(rt)
line, n = rt.repair_line(open(sys.argv[1]).read().rstrip("\n"), int(sys.argv[2]), int(sys.argv[3]))
print("%d|%s" % (n, line))
PY
}
out=$(r fixtures/md-apparatus-not-relived.md 194 108)
ok "a figure inside the apparatus is never re-corrected" "${out%%|*}" "0"
out=$(r fixtures/md-bold-span.md 194 108)
has "the bold span is closed before the marker" "$out" '**108 tags** ⚠️ **was 194 tags**<!--corrected-->'
hasnt "no nested emphasis is emitted" "$out" '**108 tags ⚠️'
out=$(r fixtures/md-two-forms-one-line.md 295 296)
ok "both forms on one line are corrected" "${out%%|*}" "2"
has "the bare column figure is corrected" "$out" '**296** ⚠️ **was 295 tags**<!--corrected-->'
has "the prose figure is corrected" "$out" '296 tags ⚠️ **was 295 tags**<!--corrected-->'
out=$(r fixtures/md-two-forms-one-line.md 295 296); out=$(printf '%s' "$out" | sed 's/^[0-9]*|//')
out2=$(printf '%s\n' "$out" > /tmp/p129t.md; r /tmp/p129t.md 295 296)
ok "re-running the repair is a no-op (idempotent)" "${out2%%|*}" "0"

# ---- grouping and plural ----------------------------------------------------
g(){ python3 -I -c "
import importlib.util; spec=importlib.util.spec_from_file_location('rt','repair_tags.py')
rt=importlib.util.module_from_spec(spec); spec.loader.exec_module(rt); print(rt.grouped($1), rt.noun($1))"; }
NNBSP=$(python3 -I -c "print('\u202f', end='')")
ok "a 4-digit figure is grouped the way this corpus groups bytes" "$(g 5896)" "5${NNBSP}896 tags"
ok "one tag is singular" "$(g 1)" "1 tag"

echo
echo "$pass passed / $fail failed"
[ "$fail" -eq 0 ]
