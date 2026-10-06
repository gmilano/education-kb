#!/usr/bin/env bash
# Regression tests for lib/probe_payload.sh — pass 15 of 2026-10-06.
# Every case is a REAL repository measured in that pass, not a fixture.  lib/README.md's own
# lesson: "un fixture lo bastante corto para ser comodo es lo bastante corto para no ver el
# defecto."  These hit the network on purpose.
cd "$(dirname "$0")"; . ./probe_payload.sh
pass=0; fail=0
check() { # check <label> <expected-substring> <actual>
  if printf '%s' "$3" | grep -q "$2"; then pass=$((pass+1)); printf '  OK   %s\n' "$1"
  else fail=$((fail+1)); printf '  FAIL %s\n       want ~ %s\n       got    %s\n' "$1" "$2" "$3"; fi
}

# Trap 1 — default branch is a version number / a feature name, never main|master.
check "GibbonEdu/core branch is v31.0.00" "^v31\.0\.00$" "$(probe_default_branch GibbonEdu/core)"
check "rosariosis branch is mobile"       "^mobile$"      "$(probe_default_branch francoisjacquet/rosariosis)"
check "i-educar branch is 2.12"           "^2\.12$"       "$(probe_default_branch portabilis/i-educar)"

# Trap 1 again, end to end: GPL must be reported as GPL, not as ungranted.
check "GibbonEdu/core -> GPL-3.0" "GPL-3.0" "$(probe_repo GibbonEdu/core)"

# The classifier bypass this file exists to prevent: GPL-3.0 §6 says "noncommercially".
check "BetterUntis -> GPL-3.0 not CC"  "GPL-3.0"  "$(probe_repo SapuSeven/BetterUntis)"
check "saspes -> AGPL-3.0 not CC"      "AGPL-3.0" "$(probe_repo sas-fossdev/saspes)"
# And a genuine NonCommercial payload still resolves as one.
check "Somtoday-Mod -> CC-BY-NC-SA" "CC-BY-NC" "$(probe_repo Jona-Zwetsloot/Somtoday-Mod)"

# Trap 2 — licence in a mixed-case subdirectory, found via the README's own link.
check "openSIS-Classic -> docs/License.txt" "docs/License.txt" "$(probe_repo OS4ED/openSIS-Classic)"

# Trap 3 — British spelling.
check "NTU-COOL viewer -> LICENCE" "LICENCE" "$(probe_repo AkizumiFox/NTU-COOL-Assignment-Status-Viewer)"

# A README that points at a licence file that does not exist is DECLARED-NOT-GRANTED,
# which is an upstream ask, not a bare absence.
check "mcp-canvas-lms -> DECLARED-NOT-GRANTED" "DECLARED-NOT-GRANTED" "$(probe_repo DMontgomery40/mcp-canvas-lms)"

# A genuinely silent repository stays NO-PAYLOAD.
check "TOFAN-AI-2026 -> NO-PAYLOAD" "NO-PAYLOAD" "$(probe_repo 781991937/TOFAN-AI-2026)"

# MIT holder is carried by construction; GPL's is NOT-APPLICABLE (P255).
check "pronotepy holder is bain3" "bain3" "$(probe_repo bain3/pronotepy)"

printf '\nprobe_payload.sh: %d passed, %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
