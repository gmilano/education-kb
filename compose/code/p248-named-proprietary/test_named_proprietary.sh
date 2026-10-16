#!/usr/bin/env bash
# p248-named-proprietary — controls for ACTION XE's discharge and for the D14 rider port.
#
# Three things are controlled here, and the third is the one that makes the first two safe:
#   (1) the WINDOWLESS name tier               — a name nobody looked for, at any offset
#   (2) the RIDER gate                          — p207's D14, ported to the shared classifier
#   (3) FAMILY-ARM CLOSURE                      — no family osi_family_of can emit may reach
#                                                 commercial_use_ok's default arm
#
# (3) exists because `ACTION XE`'s limb 2 was MEASURED to fire: before this pass the default
# arm PERMITTED, so emitting any new family string without listing it returned ALLOWED.
# This suite fails if a future pass adds a family and forgets the arm.
set -u
cd "$(dirname "$0")" || exit 1
LIB=../lib/license_family.sh
# shellcheck disable=SC1090
. "$LIB"

pass=0; fail=0
check() { # check <name> <got> <want>
  if [ "$2" = "$3" ]; then pass=$((pass+1));
  else fail=$((fail+1)); printf 'FAIL %-58s got=[%s] want=[%s]\n' "$1" "$2" "$3"; fi
}
com() { if commercial_use_ok "$1"; then printf 'ALLOWED'; else printf 'DENIED'; fi; }

KG=../p247-keyed-grant/fixtures
P207=../p207-permissive-half-audit/fixtures

# ---------------------------------------------------------------------------
# 1. PARITY WITH THE PYTHON LIST (P637: two implementations of one predicate are
#    measured against each other, never assumed to agree).
# ---------------------------------------------------------------------------
sh_names=$(__source_available_names | awk -F'\t' 'NF{print $1}' | sort | tr '\n' ' ')
py_names=$(python3 -I -c "
import sys; sys.path.insert(0,'../p247-keyed-grant')
from keyed_grant import SOURCE_AVAILABLE_NAMES as S
print(' '.join(sorted(n for n,_ in S)))
" 2>/dev/null)
check "name list parity shell<->python" "$(echo $sh_names)" "$(echo $py_names)"
check "name list is non-empty" "$([ -n "$sh_names" ] && echo yes || echo no)" "yes"

# ---------------------------------------------------------------------------
# 2. THE WINDOWLESS TIER — the two payloads ACTION XE was registered on.
#    Both returned UNCLASSIFIED -> ALLOWED before this pass; the hoist of ACTION XA
#    could not help either, because neither cause is the ORDER.
# ---------------------------------------------------------------------------
cockroach=$(cat "$KG/cockroachdb.csl-2024.txt")
redpanda=$(cat "$KG/redpanda.community-license.txt")
check "XE-1 cockroachdb family"  "$(osi_family_of "$cockroach")" "NAMED-PROPRIETARY (CockroachDB-CSL)"
check "XE-1 cockroachdb verdict" "$(com "$cockroach")"            "DENIED"
check "XE-2 redpanda family"     "$(osi_family_of "$redpanda")"   "NAMED-PROPRIETARY (RedpandaCommunity)"
check "XE-2 redpanda verdict"    "$(com "$redpanda")"             "DENIED"

# The WINDOW property, stated as a number rather than as a claim: redpanda's own name is at
# offset 2 and its real `Business Source License v.1.1` reference at 4 969 of 24 661 — beyond
# the 4 000-char truncation every anchor in the shared classifier works inside.
off_bsl=$(printf '%s' "$redpanda" | tr -s '[:space:]' ' ' \
          | grep -boiE 'business source licen[cs]e' | head -1 | cut -d: -f1)
check "redpanda BSL ref is beyond the 4000 window" \
      "$([ "${off_bsl:-0}" -ge 4000 ] && echo yes || echo no)" "yes"
check "redpanda earliest name is its OWN (not the BSL at 4969)" \
      "$(named_proprietary_of "$redpanda")" "RedpandaCommunity"

# ---------------------------------------------------------------------------
# 3. NEGATIVE CONTROLS FOR THE NAME CHANNEL — a bare acronym is NOT a name.
#    P312's criterion, which this base already pays for: "BSL" alone matches a Brazilian
#    statute, a bank and a bootloader.
# ---------------------------------------------------------------------------
check "bare BSL is not a name"   "$(named_proprietary_of 'Licensed under the BSL.')"      ""
check "bare SSPL is not a name"  "$(named_proprietary_of 'See SSPL for details.')"        ""
check "bare ELv2 is not a name"  "$(named_proprietary_of 'Distributed under ELv2 terms.')" ""
check "full BSL name IS a match" "$(named_proprietary_of 'This is the Business Source License 1.1')" "BUSL"
check "full SSPL name IS a match" "$(named_proprietary_of 'Server Side Public License, version 1')" "SSPL"

# ---------------------------------------------------------------------------
# 4. THE TIER SITS ABOVE THE <=400 B DECLARATION LEVEL — a constructed inversion.
#    A full proprietary NAME is stronger evidence than a loose token, and before this the
#    `__decl 'apache'` token below returned `Apache-2.0 (declaracion)` -> ALLOWED on it.
# ---------------------------------------------------------------------------
# MEASURED while writing this control, and it changes what the control proves: for a name an
# ANCHOR already knows (`Elastic`), the anchor fires first and returns its own family — the
# tier is never reached, and the verdict is right anyway.  So the inversion has to be built
# on a name that is in the CLOSED LIST and in NO anchor, which is exactly the `VOCABULARY`
# class of ACTION XE.  Both cases are asserted.
tiny_anchor='Licensed under the Elastic License, not Apache 2.0.'
check "tiny payload: a KNOWN anchor still wins"   "$(osi_family_of "$tiny_anchor")" "Elastic"
check "tiny payload: anchor verdict"              "$(com "$tiny_anchor")"           "DENIED"
tiny='Licensed under the CockroachDB Software License, not Apache 2.0.'
check "tiny payload: name beats the apache token" "$(osi_family_of "$tiny")" "NAMED-PROPRIETARY (CockroachDB-CSL)"
check "tiny payload: verdict"                     "$(com "$tiny")"           "DENIED"

# ---------------------------------------------------------------------------
# 5. REAL PERMISSIVE AND COPYLEFT PAYLOADS ARE UNTOUCHED.  This is the direction that
#    costs a correct shelf row (ACTION XG's hazard), so it is controlled explicitly.
# ---------------------------------------------------------------------------
for pair in "mit-canonical:MIT" "apache-2.0.canonical:Apache-2.0" "agpl-3.0:AGPL-3.0" "gpl-3.0:GPL-3.0"; do
  f=${pair%%:*}; want=${pair#*:}
  body=$(cat "$KG/$f.txt")
  check "untouched family  $f" "$(osi_family_of "$body")" "$want"
  check "untouched verdict $f" "$(com "$body")"           "ALLOWED"
done
# "All rights reserved." is a LINE of BSD-2/BSD-3 and of many MIT headers, followed by a
# grant.  p241's positive control, re-asserted here because this pass touched the arm order.
scipy='Copyright (c) 2001-2026 SciPy Developers. All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met.'
check "all-rights-reserved WITH a grant stays allowed" "$(com "$scipy")" "ALLOWED"

# ---------------------------------------------------------------------------
# 6. THE RIDER (D14).  p207 measured this and owns the only classifier in this base that
#    gets it right; p207 is not in `make hooks`, and the two instruments that ARE both
#    returned a confident clean MIT.  The FAMILY stays MIT — the inner grant really is MIT
#    and governs everything the rider does not touch — and the COMMERCIAL verdict flips,
#    because the rider removes the one right a studio deliverable exercises: to Sell.
# ---------------------------------------------------------------------------
cc_mit=$(cat "$P207/commons-clause-mit.txt")
check "D14 rider: family is still the inner grant" "$(osi_family_of "$cc_mit")" "MIT"
check "D14 rider: commercial is DENIED"            "$(com "$cc_mit")"           "DENIED"
check "D14 rider: token"                           "$(rider_restriction "$cc_mit")" "CommonsClause"
# Parity with p207's own predicate, on the same payloads (P637 again).
p207_tok=$(bash -c '. '"$P207"'/../classify.sh 2>/dev/null; rider_token "$(cat '"$P207"'/commons-clause-mit.txt)"')
check "D14 rider parity with p207::rider_token"    "$(rider_restriction "$cc_mit")" "$p207_tok"
check "rider: the SENTENCE form alone fires" \
  "$(rider_restriction 'the grant of rights under the License will not include, and the License does not grant to you, the right to Sell the Software')" \
  "CommonsClause"
check "rider: a plain MIT body does NOT fire" "$(rider_restriction "$(cat "$KG/mit-canonical.txt")")" ""

# ---------------------------------------------------------------------------
# 7. FAMILY-ARM CLOSURE.  The control that makes naming a family safe at all.
#
#    Every family string `osi_family_of` can emit must be matched by an EXPLICIT arm of
#    `commercial_use_ok`'s family `case`.  The arm patterns are read OUT OF THE SOURCE, so
#    this control cannot drift from the code it is checking, and the bare `*` net is
#    excluded on purpose — reaching it is the failure this test exists to catch.
# ---------------------------------------------------------------------------
arms=$(awk '
  /case "\$__f" in/ {inside=1; next}
  inside && /^  esac/ {exit}
  inside && /^[[:space:]]*#/ {next}
  inside && /)/ {
    # The tail is removed FIRST and the closing paren only then, because the first `)` on
    # the line sits INSIDE `(declaracion)` — stripping from it truncated seven arms and the
    # closure control duly reported them uncovered.  Found by this suite, on itself.
    line=$0;
    sub(/[[:space:]]*(return[[:space:]]+[01]|:)[[:space:]]*;;[[:space:]]*$/,"",line);
    sub(/\)[[:space:]]*$/,"",line);
    gsub(/^[[:space:]]+/,"",line); gsub(/[[:space:]]+$/,"",line);
    if (line != "*" && line != "") print line
  }
' "$LIB" | tr '|' '\n' | sed 's/^"//; s/"$//' | sed '/^$/d')
check "arm patterns were extracted from source" \
      "$([ "$(printf '%s\n' "$arms" | wc -l)" -ge 20 ] && echo yes || echo no)" "yes"

# The families this classifier can emit.  The CC branch is built from parts at runtime, so
# concrete instances are enumerated rather than the template.
EMITTED='0BSD
ISC
MIT
Unlicense
PSF-2.0
CC0-1.0
BSD
Apache-1.0
Apache-1.1
Apache-1.x-UNVERSIONED
Apache-2.0
GPL-2.0
GPL-3.0
GPL-UNVERSIONED
AGPL-3.0
LGPL
LGPL-2.1
LGPL-3.0
MPL-1.0
MPL-1.1
MPL-2.0
MPL-UNVERSIONED
EPL
EPL-1.0
EPL-2.0
EPL-UNVERSIONED
ECL-2.0
EUPL
EUPL-1.1
EUPL-1.2
BUSL
Elastic
PolyForm
SUL
FAIRCODE
MULTI-GRANT-FRAMEWORK
UNCLASSIFIED
CC-UNSPECIFIED
CC-BY-4.0
CC-BY-SA-4.0
CC-BY-NC-4.0
CC-BY-NC-SA-4.0
CC-BY-ND-4.0
CC-BY-UNVERSIONED
MIT (declaracion)
BSD (declaracion)
Apache-2.0 (declaracion)
GPL-2.0 (declaracion)
GPL-3.0 (declaracion)
AGPL-3.0 (declaracion)
LGPL (declaracion)
NAMED-PROPRIETARY (CockroachDB-CSL)
NAMED-PROPRIETARY (BUSL)'
# `NO-CESSION (negativa explicita)` is deliberately NOT in the list above: it is denied by
# P299's EARLY RETURN, which sits ABOVE the family `case`, so it never reaches an arm and a
# closure control that demanded an arm for it would be demanding dead code.  It gets its own
# assertion instead, two lines down — the state is covered, just not by the same mechanism.
uncovered=""
while IFS= read -r fam; do
  [ -z "$fam" ] && continue
  hit=no
  while IFS= read -r pat; do
    [ -z "$pat" ] && continue
    # shellcheck disable=SC2254
    case "$fam" in $pat) hit=yes; break ;; esac
  done <<< "$arms"
  [ "$hit" = no ] && uncovered="$uncovered [$fam]"
done <<< "$EMITTED"
# The early-return path, asserted on a REAL payload shape rather than through the stub.
check "NO-CESSION is denied by the early return" \
      "$(com 'This repository has not declared a project-wide reuse license. Nothing here is granted.')" \
      "DENIED"
check "every emitted family is enumerated ($(printf '%s' "$EMITTED" | grep -c .))" \
      "$([ -n "$EMITTED" ] && echo yes || echo no)" "yes"
check "family-arm closure: no emitted family reaches the default arm" "$(echo $uncovered)" ""

# And the net itself now DENIES, so an UNLISTED future family over-restricts (visible,
# costs an opportunity) instead of inventing permission (invisible, costs the deliverable).
osi_family_of_real=$(declare -f osi_family_of)
osi_family_of() { printf 'A-FAMILY-NO-ARM-NAMES-2048'; }
check "default arm DENIES an unlisted family" "$(com 'Permission is hereby granted to do things.')" "DENIED"
eval "$osi_family_of_real"
check "stub restored" "$(osi_family_of "$(cat "$KG/mit-canonical.txt")")" "MIT"

printf '\n%d/%d passed\n' "$pass" "$((pass+fail))"
[ "$fail" -eq 0 ]
