#!/usr/bin/env bash
# p868 — discharge of `867-G5`: the raw channel RESOLVES the default ref instead of guessing it.
#
# WHY THIS EXISTS.  `p830`'s byte-read path interpolates a branch name into a
# `raw.githubusercontent.com` URL.  `p867` measured three default refs in `31` that are
# neither `main` nor `master` (`openedx/paragon` -> `release-23.x`,
# `datacurso/moodle-local_assign_ai` -> `MOODLE_405_STABLE`,
# `Tanzania-AI-Community/twiga` -> `development`) and its own first probe of `ubc/compair`
# returned a `404` for exactly that reason before a clone resolved it.
#
# 🔴 A `404` from a guessed ref is INDISTINGUISHABLE, in a log, from a repository with no
# grant at that path — which is the one inference this base's whole licence discipline
# exists to prevent.  So the ref is resolved from `search/repositories` FIRST, recorded in
# the evidence row, and the counterfactual is recorded with it: would a `main` assumption
# have 404ed here?  That count is `867-G5`'s acceptance test.
#
# CHANNELS, as re-measured this pass: `gh api repos/{owner}/{repo}` is 403 for this session
# and `gh api search/repositories` is 200, so `repo:` is the only field channel available.
set -uo pipefail
OUT="${1:?usage: p868-byteread-ref.sh out.tsv [addr ...]}"
shift
LADDER=(LICENSE LICENSE.md LICENSE.txt LICENSE.TXT license.txt LICENCE LICENCE.md LICENCE.txt COPYING LICENSE-MIT NOTICE)

printf 'address\tdefault_ref\tref_is_main\tgrant_path\thttp\tbytes\tsha256_12\tfirst_line\tmain_would_404\tnote\n' > "$OUT"

for addr in "$@"; do
  ref=$(gh api -X GET search/repositories -f q="repo:$addr" -f per_page=1 \
          --jq '.items[0].default_branch // "-"' 2>/dev/null)
  [ -z "$ref" ] && ref="-"
  sleep 2.2
  is_main="no"; [ "$ref" = "main" ] && is_main="yes"

  found=""; code=""; size=""; sha=""; first=""; note=""
  for path in "${LADDER[@]}"; do
    url="https://raw.githubusercontent.com/$addr/$ref/$path"
    body=$(curl -sS --max-time 25 -w '\n%{http_code}' "$url" 2>/dev/null)
    code="${body##*$'\n'}"
    payload="${body%$'\n'*}"
    if [ "$code" = "200" ]; then
      found="$path"
      size=$(printf '%s' "$payload" | wc -c | tr -d ' ')
      sha=$(printf '%s' "$payload" | sha256sum | cut -c1-12)
      first=$(printf '%s' "$payload" | grep -m1 -v '^[[:space:]]*$' | cut -c1-90 | tr -d '\t')
      break
    fi
  done

  # the counterfactual `867-G5` asked for: same ladder, `main` assumed
  main404="n/a"
  if [ -n "$found" ]; then
    if [ "$is_main" = "yes" ]; then
      main404="no"
    else
      mc=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 20 \
             "https://raw.githubusercontent.com/$addr/main/$found" 2>/dev/null)
      [ "$mc" = "200" ] && main404="no" || main404="YES"
    fi
  fi

  [ -z "$found" ] && { found="-"; note="no grant at any of the ${#LADDER[@]} probed names"; }
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$addr" "$ref" "$is_main" "$found" "${code:--}" "${size:--}" "${sha:--}" \
    "${first:--}" "$main404" "${note:--}" >> "$OUT"
done

echo "--- probes: $(( $(wc -l < "$OUT") - 1 ))" >&2
echo "--- would have 404ed on a main assumption: $(awk -F'\t' 'NR>1 && $9=="YES"' "$OUT" | wc -l)" >&2
echo "--- no grant found: $(awk -F'\t' 'NR>1 && $4=="-"' "$OUT" | wc -l)" >&2
