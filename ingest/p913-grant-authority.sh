#!/usr/bin/env bash
# p913 — THE GRANT AUTHORITY.  Retires `p880-licence-byteread.sh` AND supersedes
# `p912-grant-family.sh`.  Discharges `912-G1`.
#
# `912-G1` asked for p880 to be retired against p912's two controls.  Running p912's instrument
# over the whole shelf discharged that and found a THIRD defect, inherited by p912 unchanged, in
# the licence family that matters most to this industry.
#
# ── 913-F1.  EVERY GPL-3.0 PAYLOAD ON THIS SHELF READ AS AGPL-3.0. ──
# GPL-3.0's own text names the Affero licence three times, in section 13 ("Use with the GNU
# Affero General Public License").  Both p880 and p912 grade with:
#     grep -qi "GNU AFFERO GENERAL PUBLIC LICENSE"                        -> AGPL-3.0
#     grep -qi "GNU GENERAL PUBLIC LICENSE" && ! grep -qi "AFFERO|LESSER" -> GPL
# The first line fires on a genuine GPL-3.0 payload and the AFFERO guard then SUPPRESSES the GPL
# branch, so the GPL branch cannot fire on GPL-3.0 at all.  Measured discriminators:
#     true GPL-3.0  : title line `GNU GENERAL PUBLIC LICENSE`,        3 Affero mentions, ~35,147-35,151 B
#     true AGPL-3.0 : title line `GNU AFFERO GENERAL PUBLIC LICENSE`, 15 Affero mentions,  34,523 B
# 🔵 It errs in BOTH directions and both are commercially live.  AGPL-3.0 s.13 imposes a
# NETWORK-USE source-disclosure obligation that GPL-3.0 does not: reporting Koha, Chamilo or ILIAS
# as AGPL OVERSTATES the obligation and wrongly kills a hosted design, while a repository
# published as MIT that is really AGPL (`OpenPronounce/OpenPronounce`) UNDERSTATES it.
#
# ── 913-F2.  THIS IS A REGRESSION OF A FIX THIS BASE ALREADY MADE AND DOCUMENTED. ──
# `ingest/licence-grade-titleline-p640.sh` carries, in its own header comment:
#   "p640 — grade on the TITLE LINE, not substring-over-payload. Both p639's grader and p640's
#    first grader failed on the GNU family because GPL-3.0 names AFFERO 3x (s.13) and AGPL-3.0
#    names 'GNU GENERAL PUBLIC LICENSE' 5x. Title-line grading is the only sound discriminator."
# p880 replaced title-line grading with body-substring grading and reintroduced the defect.  p912
# audited p880 for precisely this collision class (Boost is a PREFIX-COLLISION of the MIT trigger
# phrase) and did not generalise its own rule to the GNU family.  🔴 The process lesson is the
# transferable one: A CORRECTION PASS MUST READ THE INSTRUMENT HISTORY, because the defect it is
# about to find may already have a committed fix that a later instrument dropped.
#
# ── WHAT THIS SCRIPT IS ──  The union of every grant fix this base has made:
#   • p640's TITLE-LINE adjudication, restored, and it is the primary rule (913-F1).
#   • p640's MIT SIZE BAND: an MIT-phrased payload outside ~1000-1250 B is a narrowed derivative.
#   • p912's CREATIVE COMMONS family, which p880 could not see at all (T25, T32).
#   • p912's BOOST-BEFORE-MIT specificity rule (Boost prefix-collides with the MIT phrase).
#   • p880's CUMULATIVE/CONJUNCTIVE detection, kept: a payload may carry more than one grant, and
#     a conjunctive payload is never collapsed to one family.
# The body is consulted ONLY where the title line does not name a licence, and when it is, the
# verdict says so (`BODY-`), because a body verdict is weaker evidence than a title verdict.
set -uo pipefail
OUT="${1:?usage: p913-grant-authority.sh OUT.tsv (then either: slug... | --from-tsv FILE)}"; shift
if [ "$#" -eq 0 ]; then echo "🔴 refusing empty input (Gap 245)" >&2; exit 2; fi

D=$(mktemp -d); trap 'rm -rf "$D"' EXIT
NAMES=(LICENSE LICENSE.txt LICENSE.md LICENSE.TXT LICENCE LICENCE.txt COPYING COPYING.txt
       license license.txt license.md licence licence.txt LICENSE.rst LICENSE-MIT LICENSE-APACHE)

# ---- the adjudicator.  $1 = payload file, $2 = bytes.  Prints "families<TAB>verdict<TAB>note". ----
adjudicate() {
  local B="$1" bytes="$2" title t fam=() v note=""
  title=$(head -c 300 "$B" | tr -d '\357\273\277' | tr '\n' ' ' | sed 's/  */ /g;s/^ //')
  t=$(printf '%s' "$title" | tr '[:upper:]' '[:lower:]')
  # ---- PRIMARY: the title line.  specific-before-generic throughout. ----
  case "$t" in
    *"gnu affero general public license"*)  fam=("AGPL-3.0") ;;
    *"gnu lesser general public license"*)  fam=("LGPL") ;;
    *"gnu general public license"*)         fam=("GPL") ;;   # 913-F1: reached only via the title
    *"boost software license"*)             fam=("BSL-1.0") ;;
    *"apache license"*)                     fam=("Apache-2.0") ;;
    *"mozilla public license"*)             fam=("MPL") ;;
    *"educational community license"*)      fam=("ECL-2.0") ;;
    *"elastic license"*)                    fam=("Elastic") ;;
    # 913-F7: Open Data Commons.  `withmarbleapp/os-taxonomy` is **ODbL** — a share-alike
    # licence for a DATABASE, which is exactly the asset class `T25` says the licence trap moved
    # to.  The shelf published it as `proprietary`.  No prior instrument in this base had a
    # detector for the data-licence family at all.
    *"open database license"*|*"odbl"*)     fam=("ODbL-1.0") ;;
    *"open data commons attribution"*)      fam=("ODC-By") ;;
    *"public domain dedication and license"*|*"odc pddl"*) fam=("PDDL-1.0") ;;
    *"cc0 1.0 universal"*)                  fam=("CC0-1.0") ;;
    *"attribution-sharealike"*)             fam=("CC-BY-SA") ;;
    *"attribution-noncommercial"*)          fam=("CC-BY-NC") ;;
    *"creative commons attribution"*)       fam=("CC-BY") ;;
    *"creative commons"*)                   fam=("CC-UNSPECIFIED") ;;
    # 913-F5: the Mulan family.  `ECNU/EduWork` (East China Normal University) is
    # 木兰宽松许可证 第2版 / Mulan Permissive Software License v2 — OSI-approved, permissive,
    # bilingual, and carrying an Apache-style PATENT grant with litigation-termination that MIT
    # does not have.  p880 and p912 both report it `UNKNOWN-TEMPLATE` (zero detectors), and the
    # shelf published it as **MIT**.  This is the licence family of Chinese education supply,
    # which `T20`/`T29` record as a measured single-country phenomenon, so the blind spot is
    # aimed exactly at the tier this base says is distinctive.
    *"木兰宽松许可证"*|*"mulan permissive software license"*) fam=("MulanPSL-2.0") ;;
    *"木兰公共许可证"*|*"mulan public license"*)              fam=("MulanPubL-2.0") ;;
    *"mit license"*)                        fam=("MIT") ;;
    *"bsd "*|*"bsd-"*)                      fam=("BSD") ;;
    *"isc license"*)                        fam=("ISC") ;;
    *"the unlicense"*|*"unlicense"*)        fam=("Unlicense") ;;
  esac

  # ── 913-F6.  A TRANSLATED licence title is invisible to a title-line grader, and that is the
  # cost of 913-F1's fix: the body-grep it replaced would have caught "AFFERO" in any language.
  # `portabilis/i-diario` is AGPL-3.0 titled "LICENCA PUBLICA GERAL AFFERO GNU" (with cedilla and
  # acute accents); p913's first cut graded it UNKNOWN-TEMPLATE while the SHELF HAD IT RIGHT.
  # This base's `T20`/`T29` record vernacular supply as a measured phenomenon, so translated
  # grants are the predictable blind spot of a title-line instrument.
  #
  # 🔴 AND THE FIRST FIX FOR IT WAS A SILENT NO-OP, for a reason worth committing: this container
  # runs `LC_CTYPE=POSIX`, under which `tr '[:upper:]' '[:lower:]'` LEAVES ACCENTED CAPITALS
  # UNTOUCHED — the title folds to "licenCa pUblica geral affero gnu".  A pattern written with
  # lowercase accented characters can therefore NEVER match, and it fails as a no-op rather than
  # as an error.  Every test below is keyed on ASCII-only tokens (`licen`, `affero`, `geral`,
  # `menor`), which do fold correctly under POSIX.
  # Gated on size: a translated licence TEXT is long (a translated GPL/AGPL is ~35 kB).  A SHORT
  # payload that merely names a licence is a reference, not a text, and belongs to the
  # BY-REFERENCE stage below, which keeps the version and says the text is not present — a
  # strictly better verdict.  Without this gate the stage shadowed it (`parmentelat/nbautoeval`,
  # 289 B, graded `CC-UNSPECIFIED` and losing the `-SA`).
  if [ "${#fam[@]}" -eq 0 ] && [ "$bytes" -ge 600 ] && printf '%s' "$t" | grep -qi 'licen'; then
    if   printf '%s' "$t" | grep -qi 'affero'; then
      fam=("AGPL-3.0"); note="TRANSLATED grant title, graded on ASCII tokens (913-F6)"
    elif printf '%s' "$t" | grep -qiE 'lesser|menor|reducida|amoindrie'; then
      fam=("LGPL"); note="TRANSLATED grant title, graded on ASCII tokens (913-F6)"
    elif printf '%s' "$t" | grep -qiE 'geral|generale|general'; then
      fam=("GPL"); note="TRANSLATED grant title, graded on ASCII tokens (913-F6)"
    elif printf '%s' "$t" | grep -qiE 'creative common|comun creativ|comum criativ'; then
      fam=("CC-UNSPECIFIED"); note="TRANSLATED grant title, graded on ASCII tokens (913-F6)"
    fi
  fi

  if [ "${#fam[@]}" -gt 0 ]; then
    v="${fam[0]}"
    # p640's MIT size band, applied to a TITLE-matched MIT too.
    if [ "$v" = "MIT" ] && { [ "$bytes" -lt 1000 ] || [ "$bytes" -gt 1250 ]; }; then
      v="MIT-TITLE-OUT-OF-BAND"; note="MIT title at ${bytes} B, outside the 1000-1250 B MIT band — read the modifications"
    fi
    # a second LIVE family in the body of a title-graded payload is still a conjunctive obligation
    # 913-F3: a title names ONE licence; a payload may still carry others.  p880's control
    # (apereo/java-cas-client = Apache-2.0 notice + a separate JA-SIG BSD-3-Clause grant) is
    # the reason this runs for EVERY title-graded family, not just the GNU ones.
    local extra=() head_fam="${fam[0]}"
    [ "$head_fam" != "Apache-2.0" ] && grep -qi "apache license" "$B" && extra+=("Apache-2.0")
    [ "$head_fam" != "MIT" ] && [ "$head_fam" != "BSL-1.0" ] \
      && grep -q "Permission is hereby granted, free of charge" "$B" && extra+=("MIT")
    [ "$head_fam" != "BSD" ] \
      && grep -qi "Redistribution and use in source and binary" "$B" && extra+=("BSD")
    [ "$head_fam" != "MPL" ] && grep -qi "mozilla public license" "$B" && extra+=("MPL")
    case "$head_fam" in CC-*|CC0-*) : ;; *)
      grep -qi "creative commons" "$B" && extra+=("CC-UNSPECIFIED") ;; esac
    if [ "${#extra[@]}" -gt 0 ]; then
      fam+=("${extra[@]}"); v="CONJUNCTIVE"
      note="title grants ${fam[0]} and the body carries ${#extra[@]} further family/families — notice obligation of ${#fam[@]}"
    fi
    case "$v" in CC-*|CC0-*) note="${note:+$note; }Creative Commons grant — content licence, read scope before building on it" ;; esac
    printf '%s\t%s\t%s\n' "$(IFS=+; echo "${fam[*]}")" "$v" "$note"; return
  fi

  # ---- FALLBACK: no licence title. ----
  # 913-F8, three classes of payload that NAME a grant without reproducing it.  All three were
  # graded UNKNOWN-TEMPLATE by p913's first cut and in two of the three the SHELF WAS RIGHT, so
  # "unknown" would have destroyed a correct cell.
  #   (a) MANIFEST-DEFERRED — the R convention: `DESCRIPTION` says `License: MIT + file LICENSE`
  #       and LICENSE carries only YEAR and COPYRIGHT HOLDER (`LJKelly3141/coursepack`, 41 B).
  #       The grant is in the PACKAGE MANIFEST, which is the axis gate `905-G1` already watches.
  #   (b) BY-REFERENCE — the payload cites a licence and a URL instead of reproducing the text
  #       (`parmentelat/nbautoeval`, 289 B, "Creative Common Licence CC BY-SA 4.0" — note the
  #       singular "Common", which a `Creative Commons` grep misses by one letter).
  #   (c) SPLIT-BY-ASSET-TYPE — one repository, two grants, divided by what the asset IS
  #       (`bncc-dev/bncc-benchmark`: "Código — MIT" for code, another grant for content).  This
  #       is `T25` and gate `904-G1` in a single payload, declared in prose and in Portuguese.
  if [ "$bytes" -lt 120 ] && grep -qiE "copyright holder|titular" "$B" \
     && ! grep -qiE "permission|redistribution|warranty" "$B"; then
    printf 'none	MANIFEST-DEFERRED	%s B carrying only a copyright holder and year — the grant is declared in the PACKAGE MANIFEST (R: DESCRIPTION `License:`), not here.  Read the manifest (905-G1); do NOT read this as ungranted
' "$bytes"; return
  fi
  # locale-safe: ASCII tokens only, for the reason given in 913-F6.
  if [ "$bytes" -lt 4000 ] && grep -qiE '(^|[^A-Za-z])MIT([^A-Za-z]|$)' "$B" \
     && grep -qiE 'CC[ -]?BY' "$B"; then
    local sfam="MIT(code)"
    if grep -qiE 'CC[ -]?BY[ -]?SA' "$B"; then sfam="$sfam+CC-BY-SA(content)"
    else sfam="$sfam+CC-BY(content)"; fi
    printf '%s\tSPLIT-BY-ASSET-TYPE\tone repository, two grants divided by ASSET TYPE and declared in prose (%s B) — a single licence cell cannot express it, and the permissive half is the CODE while the data/content half is attribution- or share-alike-bound (T25, gate 904-G1)\n' "$sfam" "$bytes"; return
  fi
  if [ "$bytes" -lt 600 ]; then
    local rfam=""
    grep -qiE "CC[ -]?BY[ -]?SA" "$B" && rfam="CC-BY-SA"
    [ -z "$rfam" ] && grep -qiE "CC[ -]?BY[ -]?NC" "$B" && rfam="CC-BY-NC"
    [ -z "$rfam" ] && grep -qiE "CC0" "$B" && rfam="CC0-1.0"
    [ -z "$rfam" ] && grep -qiE "CC[ -]?BY\b" "$B" && rfam="CC-BY"
    [ -z "$rfam" ] && grep -qiE "creative common" "$B" && rfam="CC-UNSPECIFIED"
    [ -z "$rfam" ] && grep -qiE "\bMIT\b" "$B" && rfam="MIT"
    [ -z "$rfam" ] && grep -qiE "apache" "$B" && rfam="Apache-2.0"
    [ -z "$rfam" ] && grep -qiE "\bAGPL\b" "$B" && rfam="AGPL-3.0"
    [ -z "$rfam" ] && grep -qiE "\bGPL\b" "$B" && rfam="GPL"
    if [ -n "$rfam" ]; then
      printf '%s	BY-REFERENCE-%s	the grant is NAMED and linked, not reproduced (%s B) — binding, but the scope cannot be read from this repository; fetch the referenced text before relying on it
' "$rfam" "$rfam" "$bytes"; return
    fi
  fi
  local bfam=() boost=0
  grep -qi "Boost Software License" "$B" && { bfam+=("BSL-1.0"); boost=1; }
  grep -qi "Apache License" "$B" && bfam+=("Apache-2.0")
  [ "$boost" -eq 0 ] && grep -q "Permission is hereby granted, free of charge" "$B" && bfam+=("MIT")
  grep -qi "Redistribution and use in source and binary" "$B" && bfam+=("BSD")
  # 913-F1: in the body the GNU families are decided by COUNT, never by presence.
  if grep -qi "general public license" "$B"; then
    local na; na=$(grep -oic "affero" "$B")
    if   [ "$na" -ge 10 ]; then bfam+=("AGPL-3.0")
    elif grep -qi "GNU LESSER GENERAL PUBLIC LICENSE" "$B"; then bfam+=("LGPL")
    else bfam+=("GPL"); note="GNU family graded from the body: ${na} Affero mention(s) — GPL-3.0 s.13 names Affero 3x"
    fi
  fi
  grep -qi "Mozilla Public License" "$B" && bfam+=("MPL")
  grep -qiE "木兰宽松许可证|mulan permissive software license" "$B" && bfam+=("MulanPSL-2.0")
  grep -qiE "木兰公共许可证|mulan public license" "$B" && bfam+=("MulanPubL-2.0")
  if   grep -qi "CC0 1.0 Universal" "$B"; then bfam+=("CC0-1.0")
  elif grep -qi "Creative Commons Attribution-ShareAlike" "$B"; then bfam+=("CC-BY-SA")
  elif grep -qi "Creative Commons Attribution-NonCommercial" "$B"; then bfam+=("CC-BY-NC")
  elif grep -qi "Creative Commons Attribution" "$B"; then bfam+=("CC-BY")
  elif grep -qiE "Creative Commons?" "$B"; then bfam+=("CC-UNSPECIFIED"); fi
  grep -qi "non-commercial\|noncommercial" "$B" && bfam+=("NONCOMMERCIAL-TERM")

  if [ "${#bfam[@]}" -eq 0 ]; then
    v="UNKNOWN-TEMPLATE"
    if [ "$bytes" -lt 200 ] && grep -qiE "GPL|MIT|Apache|BSD" "$B"; then
      v="DECLARATION-ONLY"
      note="${bytes} B, names a licence but carries NO licence text: $(tr -d '\n' < "$B" | cut -c1-60)"
    else
      note="no licence title and no grant phrase; title block was: $(printf '%s' "$title" | cut -c1-60)"
    fi
  elif [ "${#bfam[@]}" -eq 1 ]; then v="BODY-${bfam[0]}"
    note="${note:+$note; }graded from the body, not a licence title — weaker evidence than a title verdict"
  else v="BODY-CONJUNCTIVE"
    note="${note:+$note; }${#bfam[@]} families in the body, no licence title — notice obligation of ${#bfam[@]}"
  fi
  printf '%s\t%s\t%s\n' "$(IFS=+; echo "${bfam[*]:-none}")" "$v" "$note"
}

printf 'repo\tbranch\tpath\thttp\tbytes\tsha256_12\tfamilies\tverdict\tnote\n' > "$OUT"

emit() {  # $1=slug $2=branch $3=path  (branch/path known -> no API call)
  local slug="$1" br="$2" f="$3" code bytes m res
  code=$(curl -sS --max-time 30 -o "$D/x" -w '%{http_code}' \
         "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
  if [ "$code" != "200" ]; then
    printf '%s\t%s\t%s\t%s\t0\t-\tnone\tPAYLOAD-GONE\twas readable when the input TSV was made\n' \
      "$slug" "$br" "$f" "$code" >> "$OUT"; return
  fi
  bytes=$(wc -c < "$D/x" | tr -d ' '); m=$(sha256sum "$D/x" | cut -c1-12)
  res=$(adjudicate "$D/x" "$bytes")
  # 913-F4: dual-grant detection.  A repository carrying BOTH LICENSE-MIT and LICENSE-APACHE is
  # offered under EITHER (the Rust convention); reporting one of the two is a half-truth, and the
  # obligation a client inherits is the one they CHOOSE, not the one the filename list hit first.
  case "$f" in
    LICENSE-MIT|LICENSE-APACHE)
      local o oc
      [ "$f" = "LICENSE-MIT" ] && o="LICENSE-APACHE" || o="LICENSE-MIT"
      oc=$(curl -sS --max-time 20 -o /dev/null -w '%{http_code}' \
           "https://raw.githubusercontent.com/$slug/$br/$o" 2>/dev/null)
      if [ "$oc" = "200" ]; then
        res=$(printf 'MIT+Apache-2.0\tDUAL-MIT-OR-Apache-2.0\tboth LICENSE-MIT and LICENSE-APACHE are present and readable — the licensee ELECTS one; this is a disjunctive offer, not a conjunctive obligation')
      fi ;;
  esac
  printf '%s\t%s\t%s\t200\t%s\t%s\t%s\n' "$slug" "$br" "$f" "$bytes" "$m" "$res" >> "$OUT"
}

if [ "$1" = "--from-tsv" ]; then
  # re-adjudicate rows already located by a previous instrument: branch+path are FACTS in the
  # input, so this path makes NO search-API call at all.
  tail -n +2 "$2" | while IFS=$'\t' read -r repo _db br path http _rest; do
    [ "$http" = "200" ] || { printf '%s\t%s\t%s\t%s\t0\t-\tnone\tNO-PAYLOAD-IN-INPUT\tcarried through from the input TSV\n' \
        "$repo" "${br:--}" "${path:--}" "$http" >> "$OUT"; continue; }
    emit "$repo" "$br" "$path"
  done
else
  for slug in "$@"; do
    db=$(gh api -X GET search/repositories -f q="repo:$slug" --jq '.items[0].default_branch // ""' 2>/dev/null); sleep 2
    branches=(); [ -n "$db" ] && branches+=("$db")
    for b in main master develop; do [ "$b" != "$db" ] && branches+=("$b"); done
    found=0
    for br in "${branches[@]}"; do for f in "${NAMES[@]}"; do
      code=$(curl -sS --max-time 30 -o "$D/p" -w '%{http_code}' \
             "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
      [ "$code" = "200" ] || continue
      emit "$slug" "$br" "$f"; found=1; break 2
    done; done
    [ $found -eq 0 ] && printf '%s\t-\t-\t404\t0\t-\tnone\tNO-LICENCE-FILE-FOUND\tsearched %d names over %d branches\n' \
      "$slug" "${#NAMES[@]}" "${#branches[@]}" >> "$OUT"
  done
fi
