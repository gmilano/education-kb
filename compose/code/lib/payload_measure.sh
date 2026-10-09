# SHARED PAYLOAD MEASUREMENT — the NETWORK-FREE half of the probe.  Source this, or call
# `lib/measure`.  Do not rewrite it.
#
# Pass 74 of 2026-10-09, closing `Gap 328`.
#
# ─── Why this file exists, and why `Gap 328`'s own remedy was wrong ───────────────────────
#
# `Gap 328` recorded the blocker as the SOURCED-LIBRARY CALLING CONVENTION and the remedy as
# "make the shared probe invocable as a plain script with arguments".  Pass 74 measured the
# boundary and 🔴 BOTH HALVES OF THAT ARE FALSE:
#
#   | what                                             | result in this environment      |
#   |--------------------------------------------------|---------------------------------|
#   | `python3 -I` an offline instrument from the clone | 🟢 runs                         |
#   | `. lib/license_family.sh`  (no network)           | 🟢 runs, classifies correctly   |
#   | `. lib/probe_payload.sh`   (contains `curl`)      | 🔴 DENIED `[Code from External]`|
#   | `curl raw.githubusercontent.com/...`              | 🔴 DENIED `[Exfil Scouting]`    |
#
# 🔵 Sourcing is not the blocker — `license_family.sh` sources fine and is sourced by this
# file.  The blocker is the NETWORK LIMB.  A "plain script with arguments" that still calls
# `curl` is refused identically, so the remedy as written would have bought nothing.
#
# 🟢 The real seam is NETWORK vs NOT.  Everything that can be measured without the network —
# sizing, licence family, holder, word-bounded protocol counts — lives here and is testable
# offline.  `probe_payload.sh` keeps only the fetch and delegates the measuring to this file.
# A pass that cannot fetch still gets every control it would otherwise hand-roll, which is
# the failure `P834`/`P831` were both bought with.
#
# ─── The defect this file fixes in the shelf's own instrument ─────────────────────────────
#
# 🔴 `probe_payload.sh` committed `P834` itself, in the pass-15 code that `P834` was later
# written to warn about:
#
#     body=$(_raw "$repo" "$br" "$fn")              # <- strips ALL trailing newlines
#     sz=$(printf '%s' "$body" | wc -c | tr -d ' ')  # <- so this is low by that many bytes
#
# 🟢 Measured offline, with the negative control `P126`-2 requires (a payload with NO trailing
# newline, where the two methods must AGREE):
#
#     trailing newlines | 0 | 1 | 3
#     delta (bytes low) | 0 | 1 | 3
#
# 🔵 So `P834` as recorded ("one byte low") is itself an understatement: `$(…)` strips the
# ENTIRE trailing run, not one byte.  For licence payloads the run is almost always 1, which
# is why the shelf saw +1 — but the rule must be stated as "all trailing newlines".
#
# 🟢 `size_of_file` is the byte-exact primitive: `wc -c < file` never round-trips through a
# variable.  `size_of_capture_BROKEN` is the defect, kept ONLY so the suite can assert the
# case where the instrument can fail.  Never call it to measure anything.
#
# ⚠️ Scope, stated because the house style requires it: a trailing-newline error changes the
# SIZE and never the FAMILY.  `family_of`/`holder_of` are newline-insensitive, so every family
# verdict this shelf published stands; only byte counts moved.

_MEASURE_LIB_DIR="${_MEASURE_LIB_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
# P171 lives here and is NOT re-implemented.  lib/README.md: "una regla que hay que recordar
# no es un control."
. "$_MEASURE_LIB_DIR/license_family.sh"

# ── sizing ───────────────────────────────────────────────────────────────────────────────

# Byte-exact size of a payload on disk.  THE sizing primitive for this repository.
size_of_file() {
  [ -f "$1" ] || { printf '0\n'; return 1; }
  wc -c < "$1" | tr -d ' '
}

# The `P834` defect, preserved as a control.  NEVER use this to publish a figure; it exists
# so `test_measure.sh` can assert that the correct primitive and this one DISAGREE on a
# payload with a trailing newline and AGREE on one without.
size_of_capture_BROKEN() {
  local b; b=$(cat "$1" 2>/dev/null)
  printf '%s' "$b" | wc -c | tr -d ' '
}

# How many trailing newlines a payload carries — the exact size of the `P834` error for it.
trailing_newlines() {
  local n; n=$(( $(size_of_file "$1") - $(size_of_capture_BROKEN "$1") ))
  printf '%s\n' "$n"
}

# ── classification (delegated, never re-implemented) ─────────────────────────────────────

# family_of/holder_of take the payload TEXT.  Both are newline-insensitive, so reading the
# file through `$(cat …)` here is correct and is not a `P834` violation: the capture feeds the
# CLASSIFIER, never the SIZE.
family_of_file() { local b; b=$(cat "$1" 2>/dev/null); family_of "$b"; }
holder_of_file() { local b; b=$(cat "$1" 2>/dev/null); holder_of "$b"; }

# ── word-bounded counting (`P831`) ───────────────────────────────────────────────────────

# `P831` was bought with `tooLTIp` and `muLTI-tenancy` counted as LTI hits.  A substring grep
# over a file list overcounts; `-w` is the fix and it is a CONTROL here, not a reminder.
#
#   count_word_in_file <path> <word>
count_word_in_file() {
  [ -f "$1" ] || { printf '0\n'; return 1; }
  grep -oiwE -- "$2" "$1" 2>/dev/null | wc -l | tr -d ' '
}

# Count word-bounded hits over a newline-separated list of PATHS on stdin — the shape a
# `git ls-tree` / `ls-remote` enumeration actually arrives in (`P829`).
count_word_in_pathlist() {
  grep -oiwE -- "$1" 2>/dev/null | wc -l | tr -d ' '
}

# ── the TSV row, from a local payload ────────────────────────────────────────────────────

# Same six fields, same order as `probe_repo`, so the two are interchangeable downstream:
#   repo <TAB> branch <TAB> filename <TAB> bytes <TAB> family <TAB> holder
#
#   measure_payload_file <path> [repo] [branch] [filename]
measure_payload_file() {
  local path="$1" repo="${2:--}" br="${3:--}" fn="${4:-}"
  [ -z "$fn" ] && fn=$(basename "$path")
  if [ ! -f "$path" ]; then
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$br" "NO-PAYLOAD" "0" "NO-PAYLOAD" "-"; return
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$repo" "$br" "$fn" "$(size_of_file "$path")" "$(family_of_file "$path")" "$(holder_of_file "$path")"
}
