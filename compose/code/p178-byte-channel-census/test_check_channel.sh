#!/bin/bash
# Suite for the `ACTION KU` gate. Fixtures are built in a scratch tree so the
# test never depends on the live state of the repository it guards - the defect
# `P355` records about instruments that only pass in their own cwd.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
pass=0; fail=0
ck() { if [ "$2" = "$3" ]; then pass=$((pass+1)); else fail=$((fail+1)); printf 'FAIL %s: want %s got %s\n' "$1" "$3" "$2"; fi; }

T=$(mktemp -d); mkdir -p "$T/compose/code/zz-fixture" "$T/ingest"
cp "$HERE/check_channel.sh" "$T/compose/code/zz-fixture/check_channel.sh"

# 1. clean tree -> exit 0
printf '%s\n' 'b=$(cat f); wc -c < f' > "$T/compose/code/zz-fixture/clean.sh"
( cd "$T/compose/code/zz-fixture" && bash check_channel.sh >/dev/null 2>&1 )
ck "clean tree exits 0" "$?" "0"

# 2. a live stripping site -> exit 1
printf '%s\n' 'bytes=$(printf '"'"'%s'"'"' "$body" | wc -c | tr -d '"'"' '"'"')' \
  > "$T/compose/code/zz-fixture/dirty.sh"
( cd "$T/compose/code/zz-fixture" && bash check_channel.sh >/dev/null 2>&1 )
ck "live stripping site exits 1" "$?" "1"

# 3. the SAME idiom inside a comment -> exit 0 (documentation is not a defect)
printf '%s\n' '# bytes=$(printf '"'"'%s'"'"' "$body" | wc -c)' > "$T/compose/code/zz-fixture/dirty.sh"
( cd "$T/compose/code/zz-fixture" && bash check_channel.sh >/dev/null 2>&1 )
ck "commented idiom exits 0" "$?" "0"

# 4. the mechanism itself, measured - the control `P126`-2 requires
printf 'x\n' > "$T/one"; printf 'x' > "$T/none"; printf 'x\n\n\n' > "$T/three"
for f in one none three; do
  full=$(wc -c < "$T/$f" | tr -d ' ')
  b=$(cat "$T/$f"); strip=$(printf '%s' "$b" | wc -c | tr -d ' ')
  printf '%s\t%s\n' "$f" "$((full - strip))"
done > "$T/deltas"
ck "0 trailing newlines -> delta 0" "$(awk '$1=="none"{print $2}' "$T/deltas")" "0"
ck "1 trailing newline  -> delta 1" "$(awk '$1=="one"{print $2}'  "$T/deltas")" "1"
ck "3 trailing newlines -> delta 3" "$(awk '$1=="three"{print $2}' "$T/deltas")" "3"

rm -rf "$T"
printf '%s/%s\n' "$pass" "$((pass+fail))"
[ "$fail" -eq 0 ]
