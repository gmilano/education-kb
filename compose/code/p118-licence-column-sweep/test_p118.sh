#!/usr/bin/env bash
# P118 test suite. Fully offline: every fixture is a REAL licence file this
# pass captured to streams/, or a markdown fixture built here on disk. No
# network, no mocks of the thing under test -- classify2.sh and extract.sh are
# the real scripts, run on real bytes.
set -u
PASS=0; FAIL=0
ok()   { PASS=$((PASS+1)); }
bad()  { FAIL=$((FAIL+1)); printf 'FAIL: %s\n  expected: %s\n  actual:   %s\n' "$1" "$2" "$3"; }
chk()  { if [ "$2" = "$3" ]; then ok; else bad "$1" "$2" "$3"; fi }

TD=$(mktemp -d); trap 'rm -rf "$TD"' EXIT

# ---------------------------------------------------------------- classify2.sh
# 1. The P117-K trap, structurally. GPL-3's section 13 is titled "Remote Network
#    Interaction; Use with the GNU Affero General Public License", so every GPL-3
#    file CONTAINS the AGPL's name. p117's v1 classifier read three GPL-3 repos
#    as AGPL-3.0 because of it. These are the real files.
for g in 'OtterDen-Lab%Autograder@main@LICENSE' 'ahmedEid1%lumen@main@LICENSE'; do
  [ -f "streams/$g" ] || continue
  chk "GPL-3 not read as AGPL [$g]" "GPL-3.0" "$(./classify2.sh "streams/$g")"
  # and the trap really is present in the fixture, else the test proves nothing
  if grep -qi 'GNU Affero General Public License' "streams/$g"; then ok
  else bad "fixture $g must contain the AGPL cross-reference" "present" "absent"; fi
done

# 2. A real AGPL-3 file is still AGPL-3, i.e. the fix did not over-correct.
[ -f 'streams/openedx%edx-ora2@master@LICENSE' ] && \
  chk "real AGPL-3 stays AGPL-3" "AGPL-3.0" "$(./classify2.sh 'streams/openedx%edx-ora2@master@LICENSE')"

# 3. Version normalisation (fault F1): LGPL "Version 3" must spell as 3.0, not 3.
[ -f 'streams/bigbluebutton%bigbluebutton@main@LICENSE' ] && \
  chk "LGPL version spells x.0" "LGPL-3.0" "$(./classify2.sh 'streams/bigbluebutton%bigbluebutton@main@LICENSE')"
# GPL *2* must not be reported as GPL-3.0 by a defaulted version.
[ -f 'streams/portabilis%i-educar@master@LICENSE' ] && \
  chk "GPL-2 version read, not defaulted" "GPL-2.0" "$(./classify2.sh 'streams/portabilis%i-educar@master@LICENSE')"

# 4. Multi-grant files (fault F2) report the plurality, never a positional guess.
[ -f 'streams/PrairieLearn%PrairieLearn@master@LICENSE' ] && \
  chk "multi-grant reported as MULTI" "MULTI-GRANT:AGPL-3.0,MIT" \
      "$(./classify2.sh 'streams/PrairieLearn%PrairieLearn@master@LICENSE')"

# 5. Permissive singles.
[ -f 'streams/huggingface%transformers@main@LICENSE' ] && \
  chk "Apache-2.0" "Apache-2.0" "$(./classify2.sh 'streams/huggingface%transformers@main@LICENSE')"
[ -f 'streams/microsoft%ai-agents-for-beginners@main@LICENSE' ] && \
  chk "MIT" "MIT" "$(./classify2.sh 'streams/microsoft%ai-agents-for-beginners@main@LICENSE')"

# 6. Degenerate inputs: empty and absent must not be silently classified.
: > "$TD/empty"; chk "empty file -> EMPTY" "EMPTY" "$(./classify2.sh "$TD/empty")"
printf 'this file grants nothing at all\n' > "$TD/noise"
chk "no grant -> UNKNOWN" "UNKNOWN" "$(./classify2.sh "$TD/noise")"

# 7. A hand-built GPL-3 section-13 fragment: the trap in isolation, so the test
#    survives even if the captured streams are pruned.
cat > "$TD/gpl3frag" <<'FX'
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
  13. Use with the GNU Affero General Public License.
  Notwithstanding any other provision of this License, you have permission to
  link or combine any covered work with a work licensed under version 3 of the
  GNU Affero General Public License into a single combined work.
FX
chk "section-13 fragment -> GPL-3.0" "GPL-3.0" "$(./classify2.sh "$TD/gpl3frag")"

# ----------------------------------------------------------------- extract.sh
# 8. HEADER AND SEPARATOR ROWS MUST NOT BECOME DATA. A table header reading
#    "| Nombre | Repo | Licencia |" has been compiled into this KB as an entity
#    literally named "nombre" before now. The extractor requires a real slug AND
#    a licence token in the SAME row, so a header carries neither and is dropped.
cat > "$TD/fix.md" <<'FX'
---
industry: education
---
| Nombre | Repo | Licencia | Descripcion |
|---|---|---|---|
| Example | https://github.com/OWNER/REPO | MIT | placeholder |
| Tutor | [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | Open edX installer |
| no licence here | [`a/b`](https://github.com/a/b) | - | prose only |
Plain prose naming https://github.com/c/d under MIT is not a column.
FX
out=$(./extract.sh "$TD/fix.md")
chk "header row dropped"        "" "$(printf '%s' "$out" | grep -i 'nombre' || true)"
chk "separator row dropped"     "" "$(printf '%s' "$out" | grep -F -- '|---|' || true)"
chk "licence-less row dropped"  "" "$(printf '%s' "$out" | cut -f3 | grep -x 'a/b' || true)"
chk "prose line dropped"        "" "$(printf '%s' "$out" | cut -f3 | grep -x 'c/d' || true)"
chk "real row kept"             "overhangio/tutor" "$(printf '%s' "$out" | grep -w 'AGPL-3.0' | cut -f3)"
# The OWNER/REPO placeholder row IS extracted -- it has a slug and a token. That
# is correct behaviour for the extractor and a real defect in any page carrying
# it, so the sweep must surface it rather than hide it.
chk "placeholder row surfaced, not hidden" "OWNER/REPO" "$(printf '%s' "$out" | grep -w 'MIT' | cut -f3)"

# ------------------------------------------------------------------ verdict.sh
# 9. Family tolerance: a row saying "GPL" about a GPL-3.0 tree is not wrong, but
#    a row saying "GPL" about an AGPL-3.0 tree IS -- network copyleft is a
#    different obligation and the whole point of Gap 406.
printf 'x/y\tmain\tLICENSE\tGPL-3.0\t1\n'  > "$TD/m.tsv"
printf 'p/q\tmain\tLICENSE\tAGPL-3.0\t1\n' >> "$TD/m.tsv"
printf 'f.md\t1\tx/y\tGPL\n'  > "$TD/c.tsv"
printf 'f.md\t2\tp/q\tGPL\n' >> "$TD/c.tsv"
V=$(awk -F'\t' 'NR==FNR{m[$1]=$4;next}{meas=m[$3];v="WRONG";n=split($4,T,",");
  for(i=1;i<=n;i++){t=T[i]; if(t==meas){v="AGREE";break}
    if(t=="GPL"&&meas~/^GPL-/){v="AGREE";break}}
  print v"\t"$3}' "$TD/m.tsv" "$TD/c.tsv")
chk "GPL token tolerates GPL-3.0" "AGREE" "$(printf '%s' "$V" | awk '$2=="x/y"{print $1}')"
chk "GPL token is WRONG on AGPL"  "WRONG" "$(printf '%s' "$V" | awk '$2=="p/q"{print $1}')"

printf '\n%s passed / %s failed\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ]
