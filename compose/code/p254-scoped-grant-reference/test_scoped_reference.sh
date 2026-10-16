#!/usr/bin/env bash
# p254 — `P1065`: a licence file may NAME a licence that governs a DIFFERENT PATH.
#
# `ACTION XA` (p246, discharged p247) hoisted the five source-available anchors above every
# OSI anchor, because a BSL payload's mandatory `Change License:` names an OSI licence and
# the OSI anchors matched first — the `BUSL` branch was dead code by construction.  XA
# pre-registered the inverse risk as its LIMB 2: a real OSI payload that merely MENTIONS the
# BSL.  p247 measured that population with GitHub's code-search API, found it empty at
# measurable reach, and published it as a MEASURED UPPER BOUND, not a proof of vacuity.
#
# 🔴 p254 broke the bound with a first-hand payload, found on the ordinary row channel:
# `steveyeow/Feynman` — root `LICENSE`, 1 217 B, `aa8325eadd7fea1c`, ref `849c336c378c`.
# A canonical MIT text plus a 150 B note saying `app/pro/` is BSL 1.1.  The repository is
# DUAL-SCOPE and both grants are real; the defect was reading a POINTER as a GRANT.
#
# 🔵 Why it mattered beyond one row: the verdict also suppressed a holder that is present
# (`Copyright (c) 2026 Steve Yao`), because `holder_of_file` answers
# `NOT-APPLICABLE (BUSL: holder not in the license text by construction)` for the family.
# One misread family silently took the attribution with it.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
LIB="$HERE/../lib"
# `payload_measure.sh` is the file-taking half: `family_of` and `holder_of` take the payload
# TEXT, `family_of_file`/`holder_of_file` take a PATH.  P237's rule is to use the shared
# classifier rather than a fresh one, and this is the shared classifier's own front door.
. "$LIB/payload_measure.sh"
FIX="$HERE/fixtures"
FAILS=0

ck() { # ck <name> <got> <want>
  if [ "$2" != "$3" ]; then printf 'FAIL %s\n  got:  %s\n  want: %s\n' "$1" "$2" "$3"; FAILS=$((FAILS+1)); fi
}

# ── the subject: the counterexample itself ─────────────────────────────────────────────
ck "root grant is MIT, not BUSL" \
   "$(family_of_file "$FIX/feynman-root.mit-plus-busl-note.txt")" "MIT"
ck "the holder survives the fix" \
   "$(holder_of_file "$FIX/feynman-root.mit-plus-busl-note.txt")" "Copyright (c) 2026 Steve Yao"
ck "stripping the note changes nothing (the note is the only difference)" \
   "$(family_of_file "$FIX/feynman-root.note-stripped.control.txt")" "MIT"

# ── the other half of the SAME repository must still refuse ────────────────────────────
ck "app/pro/ is a real BSL grant and stays BUSL" \
   "$(family_of_file "$FIX/feynman-pro.busl-1.1.txt")" "BUSL"
ck "…and it is refused for commercial use" \
   "$(commercial_use_ok "$(cat "$FIX/feynman-pro.busl-1.1.txt")" && echo ALLOWED || echo REFUSED)" "REFUSED"

# ── P1062 must NOT regress: every real BSL payload this base holds ─────────────────────
for f in "$HERE/../p247-keyed-grant/fixtures/iaga-sentinel.busl-1.1.txt" \
         "$HERE/../p247-keyed-grant/fixtures/sdv.busl-1.1.txt" \
         "$HERE/../p246-payload-integrity/fixtures/iaga-sentinel.busl-1.1.txt" \
         "$HERE/../p205-grant-classifier-fix/fixtures/bsl-1.1.txt" \
         "$HERE/../p129-transcription-audit/fixtures/licence-bsl11-change-license-mit.txt"; do
  [ -f "$f" ] || continue
  ck "P1062 holds: $(basename "$f") is still BUSL" "$(family_of_file "$f")" "BUSL"
done

# ── the DISCRIMINANT, pinned: BSL 1.1's mandatory parameters ───────────────────────────
# A governed payload carries them; a cross-reference does not.  Measured, not assumed.
params() { grep -ciE '(licensor|licensed work|change date|change license)[[:space:]]*:' "$1"; }
ck "the governed payload carries parameters" \
   "$([ "$(params "$FIX/feynman-pro.busl-1.1.txt")" -ge 1 ] && echo yes || echo no)" "yes"
ck "the cross-reference carries none" \
   "$(params "$FIX/feynman-root.mit-plus-busl-note.txt")" "0"

# ── the control that keeps the fix from being a weakening ──────────────────────────────
# A mention with NO parameters AND no identifiable OSI body must still come back BUSL: the
# anchor is only ever lost to a POSITIVELY identified family, never to UNCLASSIFIED.
# `UNCLASSIFIED` falls through to `commercial_use_ok`'s token match, which is the direction
# P1063 already paid for.
TMP="$(mktemp)"; printf 'Some notice. This thing is under the Business Source License 1.1 somehow.\n' > "$TMP"
# 🟢 The verdict here is `NAMED-PROPRIETARY (BUSL)`, not `BUSL`, and that is p248's windowless
# name tier doing its job rather than a surprise: the payload NAMES a family without carrying
# a grant body, which is precisely the tier `ACTION XE` built.  What P1065 has to preserve is
# the REFUSAL, and it does — the name is never lost to `UNCLASSIFIED`.
ck "a bare mention with no OSI body is still refused by name (no weakening)" \
   "$(family_of_file "$TMP")" "NAMED-PROPRIETARY (BUSL)"
ck "…and is still refused" \
   "$(commercial_use_ok "$(cat "$TMP")" && echo ALLOWED || echo REFUSED)" "REFUSED"

# ── the shape of the FIRST attempt at this fix, pinned as a defect ─────────────────────
# The first discriminant used `^[[:space:]]*(Licensor|…)`.  `$t` has already been through
# `tr -s '[:space:]' ' '`, so it is ONE line and `^` matches only byte 0 — the regex
# returned all four real BSL payloads to their Change License.  The 332-fixture diff caught
# it; reading the patch had not.  Recorded as a measurement so it cannot come back quietly.
ONE_LINE="$(tr -s '[:space:]' ' ' < "$FIX/feynman-pro.busl-1.1.txt")"
ck "anchored regex finds NOTHING once the text is squeezed (why the first fix failed)" \
   "$(printf '%s' "$ONE_LINE" | grep -ciE '^[[:space:]]*(licensor|licensed work)[[:space:]]*:')" "0"
ck "unanchored regex still finds it" \
   "$([ "$(printf '%s' "$ONE_LINE" | grep -ciE '(licensor|licensed work)[[:space:]]*:')" -ge 1 ] && echo yes || echo no)" "yes"

if [ "$FAILS" -ne 0 ]; then echo "p254-scoped-grant-reference: FAIL ($FAILS failing)"; exit 1; fi
echo "p254-scoped-grant-reference: PASS"
