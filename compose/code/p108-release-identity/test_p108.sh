#!/usr/bin/env bash
# test_p108.sh — OFFLINE tests for pick_latest.sh. No network: every case reads
# a file in fixtures/. Two fixtures are REAL captures (moodle, kolibri); three
# are hand-built to pin the traps P108-A..C.
set -uo pipefail
cd "$(dirname "$0")"
pass=0; fail=0
chk() { # chk <label> <expected> <actual>
  if [ "$2" = "$3" ]; then pass=$((pass+1)); printf 'ok   %s\n' "$1"
  else fail=$((fail+1)); printf 'FAIL %s\n       expected: %s\n       actual:   %s\n' "$1" "$2" "$3"; fi
}
f() { ./pick_latest.sh < "fixtures/$1"; }
col() { printf '%s\n' "$1" | cut -f"$2"; }

# --- P108-C: version sort, not lexical -------------------------------------
r=$(f trap_v10.txt)
chk "trap_v10: tags_uniq=3"            "3"        "$(col "$r" 1)"
chk "trap_v10: stable_n=3"             "3"        "$(col "$r" 2)"
chk "trap_v10: prerel_n=0"             "0"        "$(col "$r" 3)"
chk "trap_v10: latest is v10 not v9"   "v10.0.0"  "$(col "$r" 4)"
chk "trap_v10: sha of v10"             "2222222222222222222222222222222222222222" "$(col "$r" 5)"

# --- P108-A/B: peeled rows dropped, prereleases never pinned ----------------
r=$(f trap_annotated.txt)
chk "annotated: tags_uniq=3 (5 rows, 2 peeled)" "3" "$(col "$r" 1)"
chk "annotated: stable_n=1"            "1"        "$(col "$r" 2)"
chk "annotated: prerel_n=1 (rc1)"      "1"        "$(col "$r" 3)"
chk "annotated: latest stable = v1.0.0 NOT v2.0.0-rc1" "v1.0.0" "$(col "$r" 4)"
chk "annotated: sha is the TAG row, not the peeled row" "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" "$(col "$r" 5)"

# --- P1040: no tags is zero, unread is handled by census.sh not here --------
r=$(f empty.txt)
chk "empty: tags_uniq=0"               "0"        "$(col "$r" 1)"
chk "empty: stable_n=0"                "0"        "$(col "$r" 2)"
chk "empty: latest=- (no pin offered)" "-"        "$(col "$r" 4)"
chk "empty: sha=-"                     "-"        "$(col "$r" 5)"

# --- real captures ----------------------------------------------------------
r=$(f moodle.real.txt)
mt=$(col "$r" 1); ms=$(col "$r" 2); ml=$(col "$r" 4); msha=$(col "$r" 5)
chk "moodle: tags_uniq matches independent count" \
    "$(grep $'\trefs/tags/' fixtures/moodle.real.txt | grep -vc '\^{}$')" "$mt"
chk "moodle: latest_stable is a real ref in the capture" "yes" \
    "$(grep -qx "$(grep $'\trefs/tags/' fixtures/moodle.real.txt | sed 's#.*\trefs/tags/##' | grep -x "$ml" | head -1)" <<< "$ml" && echo yes || echo no)"
chk "moodle: sha is 40 hex"            "40"       "$(printf '%s' "$msha" | grep -cE '^[0-9a-f]{40}$' >/dev/null && printf '%s' "${#msha}" || printf 'bad')"
chk "moodle: stable_n > 0"             "yes"      "$([ "$ms" -gt 0 ] && echo yes || echo no)"

r=$(f kolibri.real.txt)
kt=$(col "$r" 1); kl=$(col "$r" 4)
chk "kolibri: tags_uniq matches independent count" \
    "$(grep $'\trefs/tags/' fixtures/kolibri.real.txt | grep -vc '\^{}$')" "$kt"
chk "kolibri: latest_stable has no prerelease suffix" "yes" \
    "$(printf '%s' "$kl" | grep -qE '^(v?[0-9]+\.[0-9]+(\.[0-9]+)?|-)$' && echo yes || echo no)"

# --- inflation factor stays auditable (P107-C regression) -------------------
raw=$(grep -c $'\trefs/tags/' fixtures/moodle.real.txt)
chk "moodle: raw tag rows exceed uniq (annotated repo, so P107-C applies)" "yes" \
    "$([ "$raw" -gt "$mt" ] && echo yes || echo no)"


# ============ appended: lane 2, project-prefixed releases (P108-D/E) =======
r=$(f trap_prefix.txt)
chk "prefix: no bare semver"           "0"                "$(col "$r" 2)"
chk "prefix: prefix_n=3"               "3"                "$(col "$r" 6)"
chk "prefix: picks 21.0.3 not 20.3.3"  "OpenOLAT_21.0.3"  "$(col "$r" 7)"
chk "prefix: sha of 21.0.3"            "2222222222222222222222222222222222222222" "$(col "$r" 8)"
chk "prefix: class=prefixed"           "prefixed"         "$(col "$r" 9)"

# P108-E: a build number must NOT parse as a version
r=$(f trap_stamp.txt)
chk "stamp: prefix_n=0 (1791293242 is not a version)" "0" "$(col "$r" 6)"
chk "stamp: offers no pin"              "-"        "$(col "$r" 7)"
chk "stamp: class=stamp"                "stamp"    "$(col "$r" 9)"

# classes are exhaustive and mutually exclusive
chk "class: empty -> none"              "none"     "$(col "$(f empty.txt)" 9)"
chk "class: bare semver -> semver"      "semver"   "$(col "$(f trap_v10.txt)" 9)"

# real capture: dspace-style v10 trap under a prefix is the live P108-C case
r=$(f moodle.real.txt)
chk "moodle: class is decided, not blank" "yes" \
    "$(printf '%s' "$(col "$r" 9)" | grep -qE '^(semver|prefixed|stamp|none)$' && echo yes || echo no)"


# ============ appended: P108-G, a trailing year is a date not a version =====
r=$(f trap_date.txt)
chk "date: prefix_n=0 (16.01.2017 is a date)" "0"      "$(col "$r" 6)"
chk "date: offers no pin"                     "-"      "$(col "$r" 7)"
chk "date: class=stamp not prefixed"          "stamp"  "$(col "$r" 9)"

# CalVer survives: the year leads, so it is a real version scheme
r=$(f trap_calver.txt)
chk "calver: prefix_n=2"                      "2"                "$(col "$r" 6)"
chk "calver: picks 2026.07.1"                 "dados-2026.07.1"  "$(col "$r" 7)"
chk "calver: class=prefixed"                  "prefixed"         "$(col "$r" 9)"

printf '\n%d passed / %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
