#!/usr/bin/env bash
# test_p107.sh — OFFLINE test for parse_refs.sh. No network. Fixtures are real
# `git ls-remote` payloads captured at pass 107.
set -uo pipefail
cd "$(dirname "$0")"
pass=0; fail=0
ck(){ # ck <label> <expected> <actual>
  if [ "$2" = "$3" ]; then pass=$((pass+1));
  else fail=$((fail+1)); printf 'FAIL %-52s expected=%s actual=%s\n' "$1" "$2" "$3"; fi; }

row(){ ./parse_refs.sh < "fixtures/$1"; }
f(){ printf '%s' "$1" | cut -f"$2"; }

# --- unitime: 101 unique tags behind 202 raw lines (the 2x inflation) ---
U=$(row unitime.refs)
ck "unitime heads"      "45"  "$(f "$U" 1)"
ck "unitime tags_raw"   "202" "$(f "$U" 2)"
ck "unitime tags_uniq"  "101" "$(f "$U" 3)"
ck "unitime sha is 40ch" "40" "$(f "$U" 4 | tr -d '\n' | wc -c | tr -d ' ')"

# --- academico: the UNRELEASED case. 0 tags must survive as 0, not as empty ---
A=$(row academico.refs)
ck "academico heads"     "10" "$(f "$A" 1)"
ck "academico tags_raw"   "0" "$(f "$A" 2)"
ck "academico tags_uniq"  "0" "$(f "$A" 3)"

# --- bncc-dados: every tag annotated, so raw is exactly 2x uniq ---
B=$(row bncc-dados.refs)
ck "bncc heads"          "1" "$(f "$B" 1)"
ck "bncc tags_raw"       "6" "$(f "$B" 2)"
ck "bncc tags_uniq"      "3" "$(f "$B" 3)"
ck "bncc sha40"         "daabd7dd63ae0cac0aa520b6189e79f95c24f583" "$(f "$B" 4)"

# --- the inflation is real, not a parser artefact: raw > uniq wherever
#     annotated tags exist, and never less ---
for fx in unitime bncc-dados academico; do
  R=$(row "$fx.refs"); r=$(f "$R" 2); u=$(f "$R" 3)
  ck "$fx raw>=uniq" "ok" "$([ "$r" -ge "$u" ] && echo ok || echo no)"
done

# --- empty input must not crash and must report zeros, not blanks (P1040:
#     an unread row is unread, never zero — so zeros must be EXPLICIT) ---
E=$(printf '' | ./parse_refs.sh)
ck "empty heads"   "0" "$(f "$E" 1)"
ck "empty tags"    "0" "$(f "$E" 2)"
ck "empty sha"     "-" "$(f "$E" 4)"

# --- a lightweight tag must NOT be discounted: synthesise one ---
S=$(printf 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\trefs/heads/main\nbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\trefs/tags/v1\n' | ./parse_refs.sh)
ck "lightweight tags_raw"  "1" "$(f "$S" 2)"
ck "lightweight tags_uniq" "1" "$(f "$S" 3)"
ck "lightweight sha"  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" "$(f "$S" 4)"

printf '\n%s passed / %s failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
