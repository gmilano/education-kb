#!/bin/bash
# P212 -- WHERE DOES THE ACTOR COME FROM?  The axis orthogonal to pass 71's write-gate ladder.
#
# Pass 71 built a four-rung ladder for the WRITE GATE (P207) and then wrote its own
# limit, on `nitsuah/bb-mcp`: "la politica se hace cumplir, la IDENTIDAD no se autentica".
# That limit is not a defect of one piece.  It is a SECOND AXIS, and this instrument
# measures it: the gate says what the server refuses to DO; the actor binding says
# WHO it refuses it for.  A policy table evaluated against an actor the caller
# declares is a policy table evaluated against a self-declared input.
#
# Rungs, strongest first.  The rung is read from the CODE or from the project's own
# configuration contract, never from a claim in the README:
#   A1 ACTOR-FROM-UPSTREAM-SESSION  the actor is whoever the stored credential belongs
#                                   to; the upstream platform decides their rights.
#                                   The caller cannot name a different actor.
#   A2 ACTOR-FROM-LOCAL-CONFIG      declared at deploy time, pinned server-side, and a
#                                   conflicting value in the CALL is rejected.
#   A3 ACTOR-FROM-CALL-ARGUMENT     the caller states who it is on every call.
#   A4 NO-ACTOR-MODELLED            one site-wide credential performs everything; the
#                                   SUBJECT is a call argument and there is no actor.
#
# Each row carries the file and the deciding line, fetched live from the payload
# channel (P172: raw.githubusercontent.com; api.github.com and github.com are 403 here).
#
# TSV: slug \t rung \t file \t deciding-evidence
set -u
row() { # slug  file  regex  rung
  local slug="$1" file="$2" rx="$3" rung="$4" body line
  body=$(curl -s --max-time 25 "https://raw.githubusercontent.com/${slug}/HEAD/${file}" 2>/dev/null)
  if [ -z "$body" ]; then
    printf '%s\t%s\t%s\tUNREACHABLE (payload channel returned nothing)\n' "$slug" "$rung" "$file"; return; fi
  line=$(printf '%s' "$body" | grep -n -m1 -E "$rx" | tr -d '\r' | cut -c1-240)
  [ -z "$line" ] && line="PATTERN-NOT-FOUND -- rung NOT confirmed on this file"
  printf '%s\t%s\t%s\t%s\n' "$slug" "$rung" "$file" "$line"
}

row felipedias-ie/blackboard-mcp      src/server.ts  'signed-in student or instructor'            A1-ACTOR-FROM-UPSTREAM-SESSION
row chrischall/infinitecampus-mcp     README.md      'accesses your own Campus Parent account'    A1-ACTOR-FROM-UPSTREAM-SESSION
row codit04/techmcp                   README.md      'roll_number'                                A1-ACTOR-FROM-UPSTREAM-SESSION
row SwarupRock/attendai               README.md      'teacher_id. that disagrees with the session'  A2-ACTOR-FROM-LOCAL-CONFIG
row nitsuah/bb-mcp                    src/auth.ts    'required .caller_identity. parameter'       A3-ACTOR-FROM-CALL-ARGUMENT
row peancor/moodle-mcp-server         src/index.ts   'MOODLE_API_TOKEN'                           A4-NO-ACTOR-MODELLED
# Sub-case, recorded rather than forced into a rung: the credential IS a real upstream
# one (so the upstream decides rights, like A1) but it arrives IN A TOOL CALL and a
# second tool changes the actor mid-session without re-authenticating.  The rung alone
# does not describe this piece; the switch does.
row oliverhruby/edupage-mcp           README.md      'switch_to_student'                          A1*-UPSTREAM-SESSION-CALLER-SUPPLIED-AND-SWITCHABLE
