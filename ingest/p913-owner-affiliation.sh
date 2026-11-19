#!/usr/bin/env bash
# p913 — OWNER-AXIS affiliation classifier.  Discharges `912-G2`.
#
# WHY THIS EXISTS.  `912-F4` established the rule that an owner's affiliation must be adjudicated
# from its repositories' PAYLOADS and never from its name matching an acronym, because an
# owner-level homonym does not inflate a count — it FABRICATES AN INSTITUTION, and an
# institutional claim is the kind this base publishes to clients.  `912-G2` registered the
# instrument.  This is it.
#
# ── WHAT THE OWNER CHANNEL CAN AND CANNOT SAY (measured in p913, three states not two) ──
#   `gh api search/repositories -f q="user:X"`:
#     • HTTP 422 "Validation Failed"  → X does NOT exist, or is invisible to this token.
#       p913's negative control (`zzqqxxnotanowner913zz`, chosen to not exist) returns this.
#     • HTTP 200, total_count 0       → X EXISTS and has zero public repositories.
#     • HTTP 200, total_count N>0     → X exists and is occupied; adjudicate the payloads.
#   🔵 The 200/0 state is what "registered and empty" actually looks like, and it is DISTINCT
#   from 422.  `verticals/solutions.md` published `🟢 exists / 0 public repositories` for four
#   examination boards (WAEC, NABTEB, KNEC, CENEVAL); all four return **422**, byte-identical to
#   the nonexistent control, while JAMB returns **200/0**.  Only JAMB's cell was supportable.
#   See `913-F2`.
#
#   🔴 `p912`'s named second owner channel — plain HTTPS GET of the GitHub profile page — is
#   UNAVAILABLE here and fails in a SILENTLY-SHAPED way: the session's git proxy answers every
#   `github.com/<anything>` with an identical 403 JSON body ("sessions are bound to their
#   configured repositories"), 249 bytes, for a real owner and for the nonexistent control alike.
#   A channel that returns one answer for every input distinguishes nothing and must not be cited
#   as corroboration.
#
# ── THREE DEFECTS p913 FOUND IN THIS SCRIPT'S OWN FIRST CUT, all three now controls ──
#   🔴 1. SUBSTRING COLLISION — the `912-F2` class, on the term axis inside the owner instrument.
#      The first cut used `grep -oiF "exam"` and scored `neco` as AFFILIATED on `exam×3`.  The
#      three matches were "**Exam**ple" ×2 and "**exam**ine" ×1 in a 2009 Ruby web-server README.
#      It would have published Nigeria's examinations council as a real estate.  Fix: every term
#      is matched on WORD BOUNDARIES with an optional plural, `\b<term>s?\b`, never as a substring.
#   🔴 2. `break 3` READ ONE README PER OWNER, NOT ALL OF THEM.  The first cut broke out of the
#      repository loop on the first README it found, then reported "ZERO domain terms in any
#      payload".  An absence claim over one file dressed as an absence claim over an estate.
#      Fix: every probed repository is read, and `readmes_read` is REPORTED so the denominator of
#      any absence claim is visible.
#   🔴 3. `200 / total_count 0` WAS COLLAPSED INTO "OCCUPIED-UNRELATED".  It is the opposite: an
#      owner that exists with nothing in it.  `jamb` was misverdicted by the first cut.
#
# ── EVIDENCE WEIGHTING ──  A hit in a repository's DESCRIPTION or TOPICS is authored metadata and
# counts on its own.  A hit only in README prose is boilerplate-prone (defect 1), so it needs TWO
# DISTINCT terms before it carries an affiliation claim; one term alone is reported
# AMBIGUOUS-SINGLE-TERM and is NOT an affiliation.
#
# RULE ENFORCED HERE (Gap 245 class): the negative control runs in EVERY invocation and the script
# REFUSES to emit if the control does not 422.  A classifier whose "absent" verdict has not been
# shown to be reachable on this run is not evidence.
set -uo pipefail

OUT="${1:?usage: p913-owner-affiliation.sh OUT.tsv owner:term[,term...] [owner:terms ...]}"; shift
if [ "$#" -eq 0 ]; then
  echo "🔴 refusing empty owner list (Gap 245): nothing to measure" >&2; exit 2
fi
CONTROL="zzqqxxnotanowner913zz"
MAXREPO=20
D=$(mktemp -d); trap 'rm -rf "$D"' EXIT

probe_owner() {  # $1=owner -> prints "HTTP<TAB>TOTAL"; leaves json in $D/body on 200
  local o="$1" body rc
  body=$(gh api -X GET search/repositories -f q="user:$o" -f per_page=100 2>"$D/err"); rc=$?
  if [ $rc -ne 0 ]; then
    if grep -qi 'validation failed\|422' "$D/err" 2>/dev/null; then printf '422\t-\n'; return; fi
    printf 'ERR\t-\n'; return
  fi
  printf '%s' "$body" > "$D/body"
  printf '200\t%s\n' "$(jq -r '.total_count' "$D/body")"
}

read -r c_http _ < <(probe_owner "$CONTROL"); sleep 3
if [ "$c_http" != "422" ]; then
  echo "🔴 REFUSING TO EMIT: negative control '$CONTROL' returned '$c_http', not 422." >&2
  echo "   The 'absent' verdict is not reachable on this run, so no verdict here is evidence." >&2
  exit 3
fi
echo "🟢 negative control OK: '$CONTROL' → 422 (absent is reachable and distinguishable)" >&2

printf 'owner\tdomain_terms\thttp\trepos_total\tprobed\treadmes_read\tmeta_terms\treadme_terms\tverdict\tevidence\n' > "$OUT"

for spec in "$@"; do
  owner="${spec%%:*}"; terms="${spec#*:}"
  read -r http tot < <(probe_owner "$owner"); sleep 3

  case "$http" in
    422) printf '%s\t%s\t422\t-\t0\t0\t-\t-\tABSENT-OR-INVISIBLE\tbyte-identical to negative control %s — this owner is NOT established as registered\n' \
           "$owner" "$terms" "$CONTROL" >> "$OUT"; continue ;;
    200) : ;;
    *)   printf '%s\t%s\t%s\t-\t0\t0\t-\t-\tCHANNEL-ERROR\tno verdict\n' "$owner" "$terms" "$http" >> "$OUT"; continue ;;
  esac

  if [ "${tot:-0}" -eq 0 ]; then
    printf '%s\t%s\t200\t0\t0\t0\t-\t-\tREGISTERED-EMPTY\towner exists on the channel and publishes nothing — distinct from 422 (913-F2)\n' \
      "$owner" "$terms" >> "$OUT"; continue
  fi

  mapfile -t repos < <(jq -r '.items[].full_name' "$D/body" | head -$MAXREPO)
  jq -r '[.items[] | (.description // "") + " " + ((.topics // []) | join(" "))] | .[]' "$D/body" > "$D/meta"
  : > "$D/readme"; nread=0
  for r in "${repos[@]}"; do
    for br in main master; do
      for f in README.md readme.md README.rst README README.txt; do
        code=$(curl -sS -o "$D/rm" -w '%{http_code}' \
               "https://raw.githubusercontent.com/$r/$br/$f" 2>/dev/null)
        [ "$code" = "200" ] || continue
        head -c 20000 "$D/rm" >> "$D/readme"; nread=$((nread+1)); break 2
      done
    done
  done

  mh=0; rh=0; mev=""; rev=""
  IFS=',' read -ra TA <<< "$terms"
  for t in "${TA[@]}"; do
    [ -z "$t" ] && continue
    pat="\\b${t}s?\\b"
    n=$(grep -oiE -- "$pat" "$D/meta"   2>/dev/null | wc -l | tr -d ' ')
    m=$(grep -oiE -- "$pat" "$D/readme" 2>/dev/null | wc -l | tr -d ' ')
    [ "${n:-0}" -gt 0 ] && { mh=$((mh+1)); mev="$mev${mev:+,}$t×$n"; }
    [ "${m:-0}" -gt 0 ] && { rh=$((rh+1)); rev="$rev${rev:+,}$t×$m"; }
  done

  if   [ "$mh" -gt 0 ]; then v="AFFILIATED-BY-PAYLOAD"; ev="metadata: ${mev}${rev:+ | readme: $rev}"
  elif [ "$rh" -ge 2 ]; then v="AFFILIATED-BY-PAYLOAD"; ev="readme-only, $rh distinct terms: $rev"
  elif [ "$rh" -eq 1 ]; then v="AMBIGUOUS-SINGLE-TERM"; ev="ONE term in README prose only ($rev) over $nread readme(s) — NOT an affiliation (defect 1)"
  else v="OCCUPIED-UNRELATED"; ev="${#repos[@]} repositories, $nread readme(s) read, ZERO domain terms in metadata or prose — owner-level homonym (912-F4)"
  fi
  printf '%s\t%s\t200\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$owner" "$terms" "$tot" "${#repos[@]}" "$nread" "${mh}/${#TA[@]}" "${rh}/${#TA[@]}" "$v" "$ev" >> "$OUT"
done
cat "$OUT"
