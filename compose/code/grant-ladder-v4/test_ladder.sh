#!/usr/bin/env bash
# Regression suite for pass 92.  Offline: every case is a payload COMMITTED in fixtures/,
# fetched once at a pinned SHA and kept, so the suite does not depend on the network or on
# any repo still serving the same bytes.
#
# Two halves, and the second is the one that makes this a fix rather than a trade:
#   POSITIVE -- the seven real payloads that pass 91 got wrong, or that prove it got them right.
#   NEGATIVE -- seven other families that must NOT be stolen by the CC0 anchor P962 adds.
set -u
cd "$(dirname "$0")"
. ../lib/license_family.sh

pass=0; fail=0
check() { # fixture expected label
  local got; got=$(osi_family_of "$(cat "fixtures/$1")")
  if [ "$got" = "$2" ]; then pass=$((pass+1)); printf '  PASS  %-46s %s\n' "$3" "$got"
  else fail=$((fail+1)); printf '  FAIL  %-46s got=%s want=%s\n' "$3" "$got" "$2"; fi
}

echo "POSITIVE -- the rows pass 91 published wrong, and the two it published right"
# v3 said LGPL-3.0 for both of these.  The title block says GNU GPL Version 2.
check oat-sa-tao-core.d9d462a.LICENSE                    GPL-2.0         "oat-sa/tao-core (v3: LGPL-3.0)"
check portabilis-i-educar.cd1da68.LICENSE                GPL-2.0         "portabilis/i-educar (v3: LGPL-3.0)"
# v3 said bare `GPL`: the version IS in the payload, so dropping it discards a datum (P561).
check francoisjacquet-rosariosis.541c509.LICENSE         GPL-2.0         "francoisjacquet/rosariosis (v3: GPL)"
# The two LGPL rows that really are LGPL-3.0.  Controls: the fix is not a blanket re-label.
check celtic-project-LTI-PHP.0ef9cc9.LICENSE             LGPL-3.0        "celtic-project/LTI-PHP (unchanged)"
check OpenEduCat-openeducat_erp.1c95cef.LICENSE          LGPL-3.0        "OpenEduCat/openeducat_erp (unchanged)"
# P962: lib's own CC0 branch was unreachable for this, its canonical text.
check lukeslp-awesome-accessibility.d146ae6.LICENSE      CC0-1.0         "lukeslp/awesome-accessibility (lib: UNCLASSIFIED)"
# The row v3 needed a mid-pass self-catch for, and whose committed TSV still says Unlicense/PD.
check cccareers-open-source-curriculum.dd01b98.LICENSE.md CC-BY-NC-SA-4.0 "cccareers/open-source-curriculum (TSV: Unlicense/PD)"

# P964: the family the FORK knew and the shared library did not. Re-measuring with lib alone
# would have LOST it (FAIRCODE-NOT-OSI -> UNCLASSIFIED), which is why reuse obliges repair.
check leemonade-leemons.b1ca5d8.LICENSE.md               FAIRCODE        "leemonade/leemons (lib before P964: UNCLASSIFIED)"

# P965: a file AT a licence filename that is a FRAMEWORK, not a grant. lib returned CC0-1.0 --
# the most permissive family the document MENTIONS -- for a payload whose operative clause is
# "Gated content isn't yours to redistribute by default".
check learning-commons-org-knowledge-graph.65701e9.LICENSE.md MULTI-GRANT-FRAMEWORK "learning-commons-org/knowledge-graph (lib: CC0-1.0)"

echo
echo "NEGATIVE CONTROL -- the CC0 anchor must steal nothing"
for c in ccby:CC-BY-4.0 mit:MIT apache:Apache-2.0 gpl3:GPL-3.0 agpl:AGPL-3.0 ecl:ECL-2.0 bsd:BSD; do
  f="fixtures/negative-${c%%:*}.LICENSE"; want=${c##*:}
  [ -f "$f" ] || { echo "  SKIP  negative-${c%%:*} (fixture absent)"; continue; }
  got=$(osi_family_of "$(cat "$f")")
  if [ "$got" = "CC0-1.0" ]; then fail=$((fail+1)); printf '  FAIL  %-46s STOLEN by the CC0 anchor\n' "negative-${c%%:*}"
  elif [ "$got" = "$want" ]; then pass=$((pass+1)); printf '  PASS  %-46s %s\n' "negative-${c%%:*}" "$got"
  else fail=$((fail+1)); printf '  FAIL  %-46s got=%s want=%s\n' "negative-${c%%:*}" "$got" "$want"; fi
done

echo
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]
