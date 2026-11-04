#!/usr/bin/env bash
# p646 — THE README FILENAME RESOLVER. Closes 645-D.
#
# 645-D measured that 17 of 203 published addresses return 404 on README.md at
# their OWN default branch, tested 8 of them against 7 filenames, and found
# 8 of 8 serve under a different name. Its verdict: "0 of the 17 is an absence
# and the filename guess is unfixed." It left the resolver UNBUILT -- the 8 were
# resolved by hand. This is the resolver, and it runs over the WHOLE population
# rather than a specimen set, so the README channel can no longer report a
# filename guess as an absence.
#
# Three stages, each cheaper than the next one needs:
#   1. ls-remote --symref  -> existence + DEFAULT BRANCH (p645's channel A).
#      34% of this base's addresses are not on `main`, so asking for README.md
#      on `main` is itself a guess. This removes that one.
#   2. README.md at the resolved default branch -> one curl per address.
#   3. ONLY for a 404: walk the filename set. A 404 here is a FILENAME-GUESS
#      until the walk is exhausted, and only then an absence.
#
# The filename set is p645's 7 plus `README` (extensionless) and
# `docs/README.md`. raw.githubusercontent.com is CASE-SENSITIVE, which is why
# `readme.md` is a distinct candidate and not a duplicate (645-D's own
# adlnet/ADL_LRS resolves exactly there).
#
# Usage: ingest/p646-readme-resolver.sh <slug-file> <out.tsv>
set -uo pipefail
IN="${1:?slug file}"; OUT="${2:?out tsv}"
PAR="${PAR:-12}"

# EXPORTED, not merely set: the resolver runs its walk inside `xargs bash -c`,
# and a non-exported CANDIDATES makes the `for` loop iterate an EMPTY list, so
# every address falls through to "walk-exhausted". That is a silent no-op that
# reports a FALSE ABSENCE -- 645-D's own defect class, reproduced by this
# script's first draft and caught by smoke-testing it against an address whose
# README is known to serve (THU-MAIC/OpenMAIC, 55,386 B). An instrument that
# can only fail silently must be smoke-tested against a KNOWN POSITIVE.
export CANDIDATES="README.md README.rst README.txt readme.md Readme.md README .github/README.md docs/README.md README.markdown"

resolve() {
  local slug="$1" raw rc br code size cand
  raw=$(timeout 25 git -c credential.helper= -c core.askPass=true \
          ls-remote --symref "https://github.com/$slug" HEAD 2>&1); rc=$?
  if printf '%s' "$raw" | grep -q '^ref: refs/heads/'; then
    br=$(printf '%s' "$raw" | sed -n 's|^ref: refs/heads/\([^[:space:]]*\).*|\1|p' | head -1)
  elif printf '%s' "$raw" | grep -qi 'could not read Username\|Authentication failed\|Repository not found'; then
    printf '%s\tNOT-PUBLIC\t-\t-\t-\t-\tNOT-PUBLIC-no-readme-claim\n' "$slug"; return
  else
    printf '%s\tINCONCLUSIVE\t-\t-\t-\t-\tINCONCLUSIVE-rc=%s\n' "$slug" "$rc"; return
  fi

  # stage 2+3: walk, stopping at the first that serves
  for cand in $CANDIDATES; do
    read -r code size < <(curl -s -m 20 -o /dev/null \
        -w '%{http_code} %{size_download}' \
        "https://raw.githubusercontent.com/$slug/$br/$cand"; echo)
    if [ "$code" = "200" ]; then
      if [ "$cand" = "README.md" ]; then
        printf '%s\tPUBLIC-LIVE\t%s\t%s\t%s\t200\tREADME.md-direct\n' "$slug" "$br" "$cand" "$size"
      else
        printf '%s\tPUBLIC-LIVE\t%s\t%s\t%s\t200\tRESOLVED-filename-guess-was-404\n' "$slug" "$br" "$cand" "$size"
      fi
      return
    fi
  done
  printf '%s\tPUBLIC-LIVE\t%s\t-\t-\t404\tNO-README-walk-exhausted\n' "$slug" "$br"
}
export -f resolve
# a known-positive control, asserted before the population runs (see above)
if [ "${SELFTEST:-1}" = "1" ]; then
  ctl=$(resolve THU-MAIC/OpenMAIC | cut -f4)
  [ "$ctl" = "README.md" ] || { echo "SELFTEST FAILED: control resolved [$ctl], expected README.md" >&2; exit 2; }
  echo "selftest: control THU-MAIC/OpenMAIC resolves README.md -- walk is live" >&2
fi

printf 'slug\texistence\tdefault_branch\treadme_file\tbytes\thttp\tverdict\n' > "$OUT.part"
grep -vE '^[[:space:]]*$' "$IN" | xargs -P "$PAR" -I{} bash -c 'resolve "{}"' >> "$OUT.part"
mv "$OUT.part" "$OUT"
printf 'rows: %s\n' "$(( $(wc -l < "$OUT") - 1 ))"
