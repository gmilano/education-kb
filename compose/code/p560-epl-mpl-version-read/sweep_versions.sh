#!/usr/bin/env bash
# p560 — EPL/MPL VERSION SWEEP.
#
# Why this instrument exists (P560/P561, pass 46 del 2026-10-07).  `lib/license_family.sh` is this
# KB's SHARED hardened control.  Pass 45 fixed P551 in it: a CC payload's VERSION was being
# STAMPED (`-4.0`) rather than READ, so a CC-BY-SA-3.0 treebank was published as 4.0.  The fix was
# correct and it shipped with a suite.
#
# IT DID NOT TRAVEL ONE LINE UP.  The two branches immediately above the CC branch are:
#
#     printf '%s' "$t" | grep -qi 'Mozilla Public License' && { echo "MPL-2.0"; return; }
#     printf '%s' "$t" | grep -qi 'Eclipse Public License' && { echo "EPL";     return; }
#
# The first STAMPS a version it never read -- MPL-1.1 and MPL-1.0 exist and are returned as
# `MPL-2.0`, which is P551 verbatim, in the same file, one line away from its own fix.
# The second does not stamp but COLLAPSES: every EPL payload, 1.0 and 2.0 alike, answers `EPL`.
#
# WHY THE COLLAPSE IS NOT COSMETIC, measured against THIS KB's own shelf.  The education ERPs
# this base recommends are copyleft: `openeducat/openeducat_erp` is LGPL-3.0 and
# `frappe/education` + ERPNext are GPL-3.0.  So "may I combine this component with the ERP I am
# standing up?" is a live question on every engagement, and it is the ONE question on which EPL-1.0
# and EPL-2.0 differ:
#
#   * EPL-1.0 is GPL-INCOMPATIBLE.  The FSF says so and so does the Eclipse Foundation's own FAQ.
#   * EPL-2.0 added the "Secondary Licenses" clause (section 1, 'Exhibit A'), under which the
#     steward MAY designate GPL-2.0-or-later compatibility.  It is an option, not automatic.
#
# `EPL` answers neither.  A family string that cannot distinguish "GPL-incompatible" from
# "GPL-compatible if designated" is not an answer to the question the shelf asks of it.
#
# THE ORDER OF THE TWO VERSION PROBES IS MEASURED, NOT CHOSEN.  `eclipse/paho.mqtt.java` ships a
# 519 B payload that names BOTH "Eclipse Public License v2.0" AND "Eclipse Distribution License
# v1.0".  A loose `1\.0` probe run first classifies it EPL-1.0 -- the wrong verdict, on the
# GPL-compatibility axis, from a payload that states 2.0 in its title line.  So the probes are
# ANCHORED to the phrase "Eclipse Public License" and 2.0 is tested first; the fixture is the real
# paho payload and the negative control lives in `test_versions.sh`.
#
# P542 applied to this instrument: with no corpus it exits 2 rather than reporting a clean sweep.
set -uo pipefail

LIB="${1:-}"
CORPUS="${2:-}"
[ -n "$LIB" ] && [ -n "$CORPUS" ] || {
  echo "usage: $0 <license_family.sh> <corpus-dir>" >&2
  echo "p560: REFUSED — no library/corpus given, nothing judged" >&2; exit 2; }
[ -f "$LIB" ] || { echo "p560: REFUSED — not a file: $LIB" >&2; exit 2; }
[ -d "$CORPUS" ] || { echo "p560: REFUSED — not a directory: $CORPUS" >&2; exit 2; }

# shellcheck source=/dev/null
. "$LIB"

shopt -s nullglob
payloads=("$CORPUS"/*.LICENSE "$CORPUS"/*.payload)
[ "${#payloads[@]}" -gt 0 ] || {
  echo "p560: REFUSED — corpus is empty, a clean sweep over nothing is not a clean sweep" >&2
  exit 2; }

printf 'payload\tbytes\ttitle_version_in_payload\tfamily_of\tverdict\n'
collapsed=0
for p in "${payloads[@]}"; do
  body=$(cat "$p")
  sz=$(printf '%s' "$body" | wc -c | tr -d ' ')
  norm=$(printf '%s' "$body" | tr -s '[:space:]' ' ' | head -c 4000)

  # What the PAYLOAD states, read independently of the classifier under test.
  stated='-'
  if printf '%s' "$norm" | grep -qiE 'eclipse public licen[cs]e,? *-? *(v\.?|version)? ?2\.0'; then
    stated='EPL-2.0'
  elif printf '%s' "$norm" | grep -qiE 'eclipse public licen[cs]e,? *-? *(v\.?|version)? ?1\.0'; then
    stated='EPL-1.0'
  elif printf '%s' "$norm" | grep -qiE 'mozilla public licen[cs]e,? *-? *(v\.?|version)? ?2\.0|\bMPL ?2\.0'; then
    stated='MPL-2.0'
  elif printf '%s' "$norm" | grep -qiE 'mozilla public licen[cs]e,? *-? *(v\.?|version)? ?1\.1|\bMPL ?1\.1'; then
    stated='MPL-1.1'
  fi

  fam=$(family_of "$body")

  verdict='OK'
  if [ "$stated" != '-' ] && [ "$stated" != "$fam" ]; then
    verdict='DIVERGENT'
    collapsed=$((collapsed + 1))
  fi

  printf '%s\t%s\t%s\t%s\t%s\n' "$(basename "$p")" "$sz" "$stated" "$fam" "$verdict"
done

echo "p560: ${#payloads[@]} payloads, $collapsed divergent (payload states a version the classifier does not return)" >&2
exit 0
