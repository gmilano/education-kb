#!/bin/sh
# field_check.sh -- the question P308 owes after proving the anchors fragile:
#                   IS THE DEFECT ACTUALLY FIRING ON PAYLOADS AS SHIPPED?
#
# Proving an anchor fragile and proving repos trip it are two different claims, and this base
# has already been burned for sliding from one to the other (P286, pase 95: a population rate
# extrapolated from a single positive control was wrong by a factor of ~28).  So this script
# reports a SMALL-SAMPLE COUNT with its denominator enumerated, and refuses to scale it.
#
# WHY THE DENOMINATOR IS SMALL, AND IT IS A LIMIT OF THE ENVIRONMENT, NOT OF THE METHOD.
# The honest sweep is the whole 215-slug inventory.  The environment DENIES enumerating
# destinations in batch (`[Exfil Scouting]`) -- the same blocker the pase 96 declared when its
# own pre-registered population measurement could not be run.  So the denominator here is the
# payloads this pase fetched ONE BY ONE, each named in the sweep it came from: the two
# fixtures of this instrument plus the candidates of the pase-100 rotated axis.
#
# Columns: slug, bytes, family under the REPAIRED control, family under the PRE-FIX control,
# and whether they DISAGREE (which is the defect firing in the field).
# Invocation:  sh field_check.sh
cd "$(dirname "$0")"
. ../lib/license_family.sh

# THE PRE-FIX CONTROL IS THE REAL PRE-FIX FUNCTION, not a replica of it.
# The first cut of this script hand-wrote a replica of the cascade, and the replica produced a
# FALSE POSITIVE on its first run: it omitted the declaration fallback, so frappe/education
# (19 B, "License: GNU GPL V3") came back as a DISAGREEMENT that had nothing to do with reflow.
# A control that differs from its subject in more than the one variable under test cannot
# attribute what it finds -- which is P126 pt.2 wearing a different hat.  So the superseded
# function is committed verbatim beside this script and sourced in a SUBSHELL, and the only
# difference between the two sides is the P308 repair.
PREFIX_CONTROL=license_family.PRE-P308-CONTROL-2026-10-04.sh
pre_family_of() {
  printf '%s' "$1" > "$TMPP"
  sh -c ". ./$PREFIX_CONTROL; family_of \"\$(cat '$TMPP')\""
}
TMPP=$(mktemp); trap 'rm -f "$TMPP"' EXIT

printf 'slug\tbytes\tfamily_repaired\tfamily_prefix\tdisagree\tcommercial\tholder\n'
dis=0; tot=0
row() { # row <slug> <file>
  [ -f "$2" ] || return 0
  p=$(cat "$2"); b=$(wc -c < "$2" | tr -d ' ')
  a=$(family_of "$p"); o=$(pre_family_of "$p")
  tot=$((tot+1)); d=no; [ "$a" = "$o" ] || { d=YES; dis=$((dis+1)); }
  c=$(commercial_use_ok "$p" && echo allowed || echo PROHIBITED)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$1" "$b" "$a" "$o" "$d" "$c" "$(holder_of "$p")"
}
for spec in \
  "FWU-DE/mem-mcp|fixtures/unlicense-FWU-DE-mem-mcp.LICENSE" \
  "adlnet/xapi-lab|fixtures/mit-adlnet-xapi-lab.LICENSE" \
  "kuali/kfs|../p288-agpl-casefold/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE" \
  "moodle/moodle|../p184-holder-mismatch/fixtures/gpl-3.0-moodle-COPYING.txt" \
  "OpenEMIS/core|../p255-holder-shared-control/fixtures/gpl-2.0-openemis-core-LICENSE.txt" \
  "HKUDS/DeepTutor|../p184-holder-mismatch/fixtures/apache-2.0-deeptutor.txt" \
  "frappe/education|../p255-holder-shared-control/fixtures/declaration-19B-frappe-education-license.txt" \
  "katoj65/emis|../p255-holder-shared-control/fixtures/mit-holder-no-year-katoj65.txt" \
  "Halleck45/OpenPronounce|fixtures/mit-Halleck45-OpenPronounce.LICENSE" \
  "YuanGongND/gopt|fixtures/bsd3-YuanGongND-gopt.LICENSE" \
  "Submitty/Submitty|fixtures/bsd3-Submitty-Submitty.LICENSE-md.txt" \
  "autolab/Autolab|fixtures/apache-autolab-Autolab.LICENSE" \
  "INGInious/INGInious|fixtures/inginious-INGInious.LICENSE" \
  "kaldi-asr/kaldi|fixtures/kaldi-asr-kaldi.COPYING" \
  "Ovsyanka83/autograder|fixtures/gpl-Ovsyanka83-autograder.LICENSE" \
  "speechsuper/SpeechSuper-API-Samples|fixtures/mit-speechsuper-API-Samples.LICENSE" \
  "mikhailvs/loqui|fixtures/mit-mikhailvs-loqui.LICENSE" \
  "Priyamakeshwari/TeachGPT|fixtures/mit-TITLELESS-Priyamakeshwari-TeachGPT.LICENSE-md.txt" \
  ; do row "${spec%%|*}" "${spec##*|}"; done
printf '\n# payloads measured as shipped: %s\n' "$tot"
printf '# the defect FIRING on a payload as shipped: %s\n' "$dis"
printf '# NOT extrapolated to the 215-slug inventory (P286): batch enumeration is denied here.\n'
