#!/usr/bin/env bash
# Regression suite for p784 (Gap 282) AND the Gap 281 fixture assertion.
#
# Runs OFFLINE against committed fixtures.  Every network-dependent assertion is in the
# `--live` block at the bottom and is SKIPPED by default -- P713: an oracle's answer is
# not durable, so a suite that needs the network is a suite that goes red for reasons
# that are not defects.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
FX="$HERE/fixtures"
pass=0; fail=0
. <(sed -n '/^family() {/,/^}/p' "$HERE/probe.sh")

ck() { # ck <label> <expected> <actual>
  if [ "$2" = "$3" ]; then pass=$((pass+1)); printf '  ok   %-54s %s\n' "$1" "$3"
  else fail=$((fail+1)); printf '  FAIL %-54s expected=%s actual=%s\n' "$1" "$2" "$3"; fi
}

echo "== Gap 281 -- an UPPERCASED GPL-2.0 payload must NOT be read as LGPL"
# Why this fixture exists, measured pass 61 and not supposed:
#   `lib/license_family.sh:323` gates LGPL with a case-SENSITIVE `case` glob applied to the
#   WHOLE payload.  GPL-2.0's preamble names the LGPL at line 18 -- "(Some other Free
#   Software Foundation software is covered by the GNU Lesser General Public License
#   instead.)" -- at byte offset 849 of the real lxHive payload.  Title-cased, the glob
#   misses and the payload correctly falls through to the GPL branch.  UPPERCASED, the glob
#   HITS and the function emits LGPL for a GPL-2.0 text.  Pass 60 declared this unmeasured;
#   the fixture below is the instance, derived by `tr` from the REAL 18 092 B payload.
#   The mutation class is real, not synthetic: `p288/fixtures/agpl-3.0-kuali-kfs-reflowed`
#   is a REAL reflowed GNU payload already on this shelf.
ck "real lxHive GPL-2.0 (control)"      "GPL-2.0" "$(family "$(cat "$FX/gpl2-real-lxhive.LICENSE")")"
ck "UPPERCASED lxHive GPL-2.0"          "GPL-2.0" "$(family "$(cat "$FX/gpl2-uppercased-lxhive.LICENSE")")"

echo "== the fixture really does contain the trap (guards against a vacuous green, P126 pt.2)"
# If a future edit removed the uppercase LGPL mention, both assertions above would pass
# while testing NOTHING.  These two assert the trap is still present and still absent.
n_up=$(grep -c 'GNU LESSER GENERAL PUBLIC LICENSE' "$FX/gpl2-uppercased-lxhive.LICENSE" || true)
n_re=$(grep -c 'GNU LESSER GENERAL PUBLIC LICENSE' "$FX/gpl2-real-lxhive.LICENSE" || true)
ck "uppercased fixture contains the caps LGPL string" "1" "$n_up"
ck "real fixture does NOT contain it (caps)"          "0" "$n_re"
# And the offset is what puts it outside a title-block window:
off=$(python3 -I -c "d=open('$FX/gpl2-uppercased-lxhive.LICENSE','rb').read();print(d.find(b'GNU LESSER GENERAL PUBLIC LICENSE'))")
ck "caps LGPL mention sits beyond the 400 B title block" "849" "$off"

echo "== families this classifier must get right (title-line rule, P753/P773)"
ck "AGPL-3.0 title"   "AGPL-3.0"        "$(family '          GNU AFFERO GENERAL PUBLIC LICENSE
                   Version 3, 19 November 2007')"
ck "LGPL-3.0 title"   "LGPL-3.0"        "$(family '          GNU LESSER GENERAL PUBLIC LICENSE
                   Version 3, 29 June 2007')"
ck "LGPL-2.1 title"   "LGPL-2.1"        "$(family '          GNU LESSER GENERAL PUBLIC LICENSE
                   Version 2.1, February 1999')"
ck "GPL-3.0 title"    "GPL-3.0"         "$(family '          GNU GENERAL PUBLIC LICENSE
                   Version 3, 29 June 2007')"
ck "MIT"              "MIT"             "$(family 'MIT License

Copyright (c) 2026')"
ck "Apache-2.0"       "Apache-2.0"      "$(family '                 Apache License
                       Version 2.0, January 2004')"
ck "CC BY-NC-SA 4.0"  "CC-BY-NC-SA-4.0" "$(family 'Attribution-NonCommercial-ShareAlike 4.0 International')"
ck "unknown -> UNCLASSIFIED, never a guess" "UNCLASSIFIED" "$(family 'Copyright 2026. All rights reserved.')"

echo "== Gap 282 -- the scope verdict, offline"
# The verdict function is the part p784 adds over every prior probe, so it is asserted
# on families directly rather than over the network.
verdict() { # verdict <fam>...
  local n; n=$(printf '%s\n' "$@" | sort -u | wc -l | tr -d ' ')
  if [ "$#" -eq 0 ]; then echo UNGRANTED; elif [ "$n" -gt 1 ]; then echo PARTITIONED; else echo SINGLE; fi
}
ck "one grant -> SINGLE"                      "SINGLE"      "$(verdict MIT)"
ck "same family twice -> SINGLE"              "SINGLE"      "$(verdict MIT MIT)"
ck "K12-KGraph shape -> PARTITIONED"          "PARTITIONED" "$(verdict CC-BY-NC-SA-4.0 MIT)"
ck "no grant -> UNGRANTED"                    "UNGRANTED"   "$(verdict)"

echo
echo "  passed=$pass failed=$fail"
[ "$fail" -eq 0 ] || exit 1

if [ "${1:-}" = "--live" ]; then
  echo
  echo "== LIVE (network; skipped unless --live).  Expected verdicts, measured pass 61:"
  echo "   haolpku/K12-KGraph @865bc35 -> PARTITIONED (CC-BY-NC-SA-4.0 data + MIT code)"
  bash "$HERE/probe.sh" haolpku/K12-KGraph 865bc35; echo "   exit=$? (3 expected)"
  echo "   leogaggl/lxHive  @cffee6d -> SINGLE GPL-2.0 (NOT LGPL -- P773)"
  bash "$HERE/probe.sh" leogaggl/lxHive cffee6d; echo "   exit=$? (0 expected)"
fi
