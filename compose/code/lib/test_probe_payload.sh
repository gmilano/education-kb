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

# ── p442: the TREE arm (Gap 441-A).  Live, like everything else in this file.
# The canonical case: the ladder's first hit is a 108 B R-convention STUB and the grant is
# one spelling away.  `probe_repo` returns the stub; `probe_repo_all` must return BOTH, with
# the stub visible rather than authoritative.
check "ottr ladder returns the 108 B stub"  "108" "$(probe_repo ucbds-infra/ottr | cut -f4)"
check "ottr tree finds LICENSE.md too"      "LICENSE.md" "$(probe_tree_paths ucbds-infra/ottr | grep -x 'LICENSE.md')"
check "ottr all-rows carries the 1 555 B grant" "1555" \
      "$(probe_repo_all ucbds-infra/ottr | awk -F'\t' '$3=="LICENSE.md"{print $4}')"
check "ottr all-rows still shows the stub"  "UNCLASSIFIED" \
      "$(probe_repo_all ucbds-infra/ottr | awk -F'\t' '$3=="LICENSE"{print $5}')"
# A COPYLEFT text below the root of a repository whose root grant is permissive: the class
# that costs a client money.  `krzysztofbury/librus-mcp` is MIT at the root and ships a full
# GPL-3.0 at `legacy_reference/LICENSE` beside 20+ Python files.
check "librus-mcp root is MIT"              "MIT" \
      "$(probe_repo_all krzysztofbury/librus-mcp | awk -F'\t' '$3=="LICENSE"{print $5}')"
check "librus-mcp subtree GPL is VISIBLE"   "GPL-3.0" \
      "$(probe_repo_all krzysztofbury/librus-mcp | awk -F'\t' '$3=="legacy_reference/LICENSE"{print $5}')"
# The ladder cannot see it at all — this is the measurement, not an assertion.
check "  ... and the ladder returns ONE row" "1" "$(probe_repo krzysztofbury/librus-mcp | wc -l | tr -d ' ')"
# A second, DIFFERENT obligation at the root: data under ODbL, content under CC BY-SA.
check "os-taxonomy has a second root grant" "LICENSE-CONTENT" \
      "$(probe_tree_paths withmarbleapp/os-taxonomy | grep -x 'LICENSE-CONTENT')"
# The path filter must reject the shapes `P441` priced: a SOURCE file, a badge IMAGE, a
# vendored dependency's grant and an INVENTORY.  Pure function, so it is asserted directly.
for bad in "cms/templates/js/license-selector.underscore" \
           "edci-issuer/licence-EUPL 1.2-brightgreen.svg" \
           "node_modules/left-pad/LICENSE" \
           ".corepack/v1/pnpm/10.34.5/LICENSE" \
           "LICENSES/MIT.txt" \
           "src/licenses.json" \
           "admin/tool/licensemanager/tests/behat/delete_license.feature"; do
  if printf '%s\n' "$bad" | grep -Ei "$PROBE_TREE_RE" | grep -Ev "$PROBE_TREE_SKIP" | grep -q .; then
    fail=$((fail+1)); printf '  FAIL tree filter admits a non-grant path: %s\n' "$bad"
  else
    pass=$((pass+1)); printf '  OK   tree filter rejects %s\n' "$bad"
  fi
done
# ... and must ADMIT the shapes a filename ladder misses, which is the whole point.
for good in "LICENSE.TXT" "licence" "aoe-web-frontend/LICENSE" "COPYING.LESSER" \
            "LICENSE/LICENSE.code" "debian/copyright" "license.txt" "LICENSE-EUPL"; do
  if printf '%s\n' "$good" | grep -Ei "$PROBE_TREE_RE" | grep -Ev "$PROBE_TREE_SKIP" | grep -q .; then
    pass=$((pass+1)); printf '  OK   tree filter admits %s\n' "$good"
  else
    fail=$((fail+1)); printf '  FAIL tree filter rejects a real grant path: %s\n' "$good"
  fi
done

printf '\nprobe_payload.sh: %d passed, %d failed\n' "$pass" "$fail"
[ "$fail" -eq 0 ]
