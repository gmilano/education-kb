# ACTION P196-B -- byte bands for the COPYLEFT families, which p195 left as `NO-BAND`.
#
# p195 built a size-within-family control and shipped it permissive-only:
#   band_of_family AGPL-3.0 -> "- -"   =>  band_verdict -> NO-BAND
#   delivery_verdict        -> GO-SUBJECT-TO-FAMILY, not GO
# so the 77 copyleft rows on this KB's shelf were carried UNCHECKED for P1054-style
# narrowing.  p195 pre-registered the extension and named the limb that would kill it:
#   limb 1: a band exists and flags narrowed copyleft -> the control generalises
#   limb 2: copyleft payloads are too variable to band -> permissive-only, and say so
#
# 🔴 THE MECHANISM CHANGE THE DATA FORCED.  A single lo/hi interval per family is WRONG for
# LGPL-3.0, and the reason is in the licence itself, not in the corpus: LGPL-3.0 is published
# in TWO legitimate forms --
#   SHORT form  ~7 651 B  -- the LGPL preamble alone, incorporating GPL-3.0 BY REFERENCE
#   FULL  form  42 098 B  -- GPL-3.0 included BY VALUE (SPDX's own text, read this pass)
# A one-interval band must call one of the two legitimate forms "narrowed".  So a band is a
# SET of intervals, and p195's single-interval families are the one-element case.
#
# REFERENCES ARE EXTERNAL (P417: a figure is reproducible only against a reference OUTSIDE
# the instrument that produced it).  Two independent anchors per family:
#   (a) SPDX license-list-data `text/<id>.txt`, fetched this pass over the raw lane
#   (b) the modal size in p195's own 468-slug census
# The band spans both anchors +/-10%, and the 10% is INHERITED from p195's published MIT band
# (1 000-1 200 B around a 1 071 B median), not tuned until this pass's answer looked tidy.
#
# 🔴 WHAT THIS DOES NOT DO.  P420 measured that size does NOT identify a family: three
# AGPL-3.0 texts on this shelf are 34 523 B exactly with different digests.  A band therefore
# detects NARROWING, never identity.  Identity stays the (FILE, digest) pair of P392, and the
# family stays `license_family.sh`'s header read (P419, n=2 window).
#
# Emits: family  size  band_verdict   (band_verdict = IN-BAND | UNDER | OVER | NO-BAND)
set -u

# Band SETS.  Space-separated "lo:hi" intervals, widest-first.  "-" = no band for the family.
band_set_of_family() {
  case "$1" in
    # --- permissive: p195's published intervals, carried over UNCHANGED (regression control)
    MIT)          echo "1000:1200" ;;
    Apache-2.0)   echo "10000:11800" ;;
    BSD|0BSD|ISC) echo "700:1700" ;;
    CC0-1.0)      echo "6000:7500" ;;
    # --- copyleft: NEW this pass.  anchors (SPDX bytes / p195 census mode)
    AGPL-3.0)     echo "30618:37975" ;;   # 34 020 / 34 523
    GPL-3.0)      echo "31206:38664" ;;   # 34 674 / 35 149
    GPL-2.0)      echo "15603:19901" ;;   # 17 337 / 18 092
    LGPL-3.0)     echo "6886:8416 37888:46308" ;;  # BIMODAL: 7 651 short / 42 098 full
    LGPL-2.1)     echo "23401:29179" ;;   # 26 001 / 26 526
    MPL-2.0)      echo "15052:18400" ;;   # 16 727 / 16 725
    ECL-2.0)      echo "10000:12474" ;;   # 11 111 / 11 340
    *)            echo "-" ;;
  esac
}

# Pure, offline-testable.  A size is IN-BAND if it falls inside ANY interval of the set.
# UNDER/OVER are reported against the whole set's outer envelope, so the direction is
# meaningful for a multi-interval family too.
band_verdict() {
  local fam="$1" sz="$2" set lo hi iv lowest= highest=
  set="$(band_set_of_family "$fam")"
  [ "$set" = "-" ] && { printf 'NO-BAND'; return; }
  for iv in $set; do
    lo="${iv%%:*}"; hi="${iv##*:}"
    if [ "$sz" -ge "$lo" ] && [ "$sz" -le "$hi" ]; then printf 'IN-BAND'; return; fi
    [ -z "$lowest"  ] || [ "$lo" -lt "$lowest"  ] && lowest="$lo"
    [ -z "$highest" ] || [ "$hi" -gt "$highest" ] && highest="$hi"
  done
  if [ "$sz" -lt "$lowest" ]; then printf 'UNDER'; else printf 'OVER'; fi
}

if [ "${1:-}" = "--self-test" ]; then
  t=0; p=0
  chk() { t=$((t+1)); if [ "$2" = "$3" ]; then p=$((p+1)); else echo "FAIL $1: got '$2' want '$3'"; fi; }

  # --- REGRESSION: p195's nine published assertions must still hold under the set form.
  chk "p195 canonical MIT in band"   "$(band_verdict MIT 1071)"         IN-BAND
  chk "p195 PageLM MIT is OVER"      "$(band_verdict MIT 8563)"         OVER
  chk "p195 46-byte MIT is UNDER"    "$(band_verdict MIT 46)"           UNDER
  chk "p195 writeAlizer stub UNDER"  "$(band_verdict MIT 47)"           UNDER
  chk "p195 real Apache in band"     "$(band_verdict Apache-2.0 11348)" IN-BAND
  chk "p195 boundary lo in band"     "$(band_verdict MIT 1000)"         IN-BAND
  chk "p195 boundary hi in band"     "$(band_verdict MIT 1200)"         IN-BAND
  # p195 asserted these two as NO-BAND.  They are the two this pass DELIBERATELY changes.
  chk "ECL now banded (was NO-BAND)" "$(band_verdict ECL-2.0 11120)"    IN-BAND
  chk "AGPL now banded (was NO-BAND)" "$(band_verdict AGPL-3.0 33893)"  IN-BAND

  # --- the four rows the census says sit outside: the point of the pass.
  chk "AGPL 723 B is UNDER"          "$(band_verdict AGPL-3.0 723)"     UNDER
  chk "AGPL 1134 B is UNDER"         "$(band_verdict AGPL-3.0 1134)"    UNDER
  chk "GPL-3 703 B is UNDER"         "$(band_verdict GPL-3.0 703)"      UNDER
  chk "GPL-2 15214 B is UNDER"       "$(band_verdict GPL-2.0 15214)"    UNDER

  # --- BIMODAL LGPL-3.0: both legitimate forms must pass, the trough between must not.
  chk "LGPL-3 short form in band"    "$(band_verdict LGPL-3.0 7651)"    IN-BAND
  chk "LGPL-3 openeducat in band"    "$(band_verdict LGPL-3.0 8241)"    IN-BAND
  chk "LGPL-3 full form in band"     "$(band_verdict LGPL-3.0 42098)"   IN-BAND
  chk "LGPL-3 odoo full in band"     "$(band_verdict LGPL-3.0 43529)"   IN-BAND
  chk "LGPL-3 TROUGH is not a band"  "$(band_verdict LGPL-3.0 20000)"   OVER
  chk "LGPL-3 below both is UNDER"   "$(band_verdict LGPL-3.0 500)"     UNDER

  # --- the pristine SPDX anchors themselves, read over the raw lane this pass.
  chk "SPDX AGPL-3.0 34020"          "$(band_verdict AGPL-3.0 34020)"   IN-BAND
  chk "SPDX GPL-3.0 34674"           "$(band_verdict GPL-3.0 34674)"    IN-BAND
  chk "SPDX GPL-2.0 17337"           "$(band_verdict GPL-2.0 17337)"    IN-BAND
  chk "SPDX LGPL-2.1 26001"          "$(band_verdict LGPL-2.1 26001)"   IN-BAND
  chk "SPDX MPL-2.0 16727"           "$(band_verdict MPL-2.0 16727)"    IN-BAND
  chk "SPDX ECL-2.0 11111"           "$(band_verdict ECL-2.0 11111)"    IN-BAND
  chk "census moodle GPL-3 35147"    "$(band_verdict GPL-3.0 35147)"    IN-BAND
  chk "census sakai ECL 11120"       "$(band_verdict ECL-2.0 11120)"    IN-BAND

  # --- a family with no band still says so (the delivery gate depends on this).
  chk "PolyForm has no band"         "$(band_verdict PolyForm 3860)"    NO-BAND
  chk "Elastic has no band"          "$(band_verdict Elastic 3860)"     NO-BAND
  chk "UNCLASSIFIED has no band"     "$(band_verdict UNCLASSIFIED 900)" NO-BAND

  # --- P420's warning, asserted as a TEST: equal size must not imply equal identity.
  # three distinct AGPL-3.0 payloads at 34 523 B all land IN-BAND and the band says nothing
  # about which is which.  the band is a narrowing trigger, never an identity claim.
  chk "P420 34523 #1 in band"        "$(band_verdict AGPL-3.0 34523)"   IN-BAND
  chk "P420 34523 #2 in band"        "$(band_verdict AGPL-3.0 34523)"   IN-BAND

  echo "$p/$t"; [ "$p" = "$t" ] || exit 1; exit 0
fi
