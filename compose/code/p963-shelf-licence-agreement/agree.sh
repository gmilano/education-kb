#!/usr/bin/env bash
# p963 -- SHELF/REGISTER LICENCE AGREEMENT GATE  (pass 92, 2026-10-10)
#
# Discharges `Gap 356`, declared in pass 86 and carried untouched through four passes, each time
# with the same note: "it would have caught P953 and P957". It would also have caught P960, which
# is the defect that finally made it worth building -- and P960's cost was a WRONG CLIENT
# RECOMMENDATION, not an internal inconsistency:
#
#   verticals/solutions.md  "for a Brazilian public-sector SIS -> i-educar (LGPL-3.0), link, don't absorb"
#   agents/trending.md      "portabilis/i-educar | LGPL | GPL-2.0 | LATAM -- Brazilian municipal school system"
#
# Same slug, same repository, same commit, two families -- and the advice that reached a reader was
# built on the wrong one. You cannot "link, don't absorb" a GPL-2.0 codebase into a closed
# deliverable. A grep could have found it. This is that grep.
#
#   ./agree.sh <kb-root> [census.tsv]
#
# CURRENT shelf files must agree with each other and with the census. The `*/trending.md` files are
# APPEND-ONLY HISTORY: a past pass's superseded verdict living there is correct by construction, so
# they are reported in a separate INFORMATIONAL section and never fail the gate. That distinction is
# the whole reason this check is buildable at all -- a naive sweep over every .md drowns in history.
set -u
ROOT="${1:?usage: agree.sh <kb-root> [census.tsv]}"
CENSUS="${2:-}"

CURRENT="agents/top.md repos/foundations.md verticals/solutions.md intel/market.md intel/trends.md compose/patterns.md README.md"
FAMS='MIT|Apache-2\.0|BSD|ISC|ECL-2\.0|Zlib|MPL-2\.0|CC0-1\.0|0BSD|AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-3\.0|LGPL-2\.1|EUPL-1\.2|CC-BY-NC-SA-4\.0|CC-BY-NC|CC-BY-SA|CC-BY-4\.0|BSL-1\.1|FAIRCODE'

# slug <TAB> family <TAB> file -- one row per (slug, family) claim.
#
# CELL-AWARE, and the first draft of this gate was NOT, which cost it a false positive on its
# very first run -- recorded here rather than quietly fixed, because it is the same class of
# error the gate exists to catch.
#
# `agents/top.md` carries a "what is widely claimed | what the payload says" table. Its
# `frappe/lms` row reads:
#     | `frappe/lms` | a comparison lists it as **MIT** | **AGPL-3.0**, `license.txt`, 33 893 B |
# A first-bolded-family harvest reads **MIT** -- the REFUTED claim -- and reports the shelf as
# disagreeing with itself. The refutation table is the shelf being CAREFUL, and a naive gate
# punishes exactly the rows that did the work.
#
# What separates them is measurable and is the shelf's own convention: a VERDICT cell carries the
# payload's byte count (`**AGPL-3.0** . 33 893 B`, `**MIT** . 1 072 B`), and a cell quoting someone
# else's claim never does. So: harvest per `|`-cell, and keep only families in a cell that also
# carries a byte figure. Falls back to nothing rather than guessing.
harvest() {
  local f rel
  for rel in $1; do
    f="$ROOT/$rel"; [ -f "$f" ] || continue
    grep -nE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' "$f" 2>/dev/null |
    while IFS= read -r line; do
      slug=$(printf '%s' "$line" | grep -oE 'github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' | head -1 | sed 's#github\.com/##')
      [ -z "$slug" ] && continue
      # split the row into cells and keep the LAST cell that holds BOTH a family and a byte figure
      fam=$(printf '%s' "$line" | tr '|' '\n' | grep -E "[0-9][0-9  .,]*B([^a-zA-Z]|$)|bytes" |
            grep -oE "\*\*($FAMS)\*\*" | tail -1 | tr -d '*')
      [ -n "$slug" ] && [ -n "$fam" ] && printf '%s\t%s\t%s\n' "$slug" "$fam" "$rel"
    done
  done
}

echo "=== p963 shelf/register licence agreement -- $(date -u +%Y-%m-%dT%H:%MZ) ==="
echo
cur=$(harvest "$CURRENT" | sort -u)
echo "claims harvested from CURRENT shelf files: $(printf '%s\n' "$cur" | grep -c .)"
echo "distinct slugs:                            $(printf '%s\n' "$cur" | cut -f1 | sort -u | grep -c .)"
echo

fails=0
echo "--- (1) CURRENT shelf files disagreeing with EACH OTHER ---"
dis=$(printf '%s\n' "$cur" | awk -F'\t' '{print $1"\t"$2}' | sort -u | cut -f1 | uniq -d)
if [ -z "$dis" ]; then echo "  none"; else
  for s in $dis; do
    echo "  DISAGREEMENT  $s"
    printf '%s\n' "$cur" | awk -F'\t' -v s="$s" '$1==s{printf "      %-18s %s\n",$2,$3}' | sort -u
    fails=$((fails+1))
  done
fi
echo

echo "--- (2) CURRENT shelf vs census TSV ---"
if [ -z "$CENSUS" ] || [ ! -f "$CENSUS" ]; then echo "  SKIPPED (no census passed)"; else
  while IFS= read -r row; do
    s=$(printf '%s' "$row" | cut -f1); shelf=$(printf '%s' "$row" | cut -f2); where=$(printf '%s' "$row" | cut -f3)
    meas=$(awk -F'\t' -v s="$s" '$1==s{print $5; exit}' "$CENSUS")
    [ -z "$meas" ] && continue
    case "$meas" in NO-LICENCE-PAYLOAD*|SPLIT-GRANT*|ABSENT) continue ;; esac
    # A first-match census names ONE file's family. Where the repo is a verified multi-file split,
    # the shelf may legitimately cite a different file's family -- see splits.tsv for the evidence.
    if [ -f "$(dirname "$0")/splits.tsv" ] &&
       grep -qP "^\Q$s\E\t\Q$shelf\E\t" "$(dirname "$0")/splits.tsv" 2>/dev/null; then
      printf '  split-exempt  %-46s shelf=%-16s census=%-16s (%s)\n' "$s" "$shelf" "$meas" "$where"
      continue
    fi
    if [ "$shelf" != "$meas" ]; then
      printf '  MISMATCH      %-46s shelf=%-16s census=%-16s (%s)\n' "$s" "$shelf" "$meas" "$where"
      fails=$((fails+1))
    fi
  done <<< "$cur"
  [ "$fails" -eq 0 ] && echo "  none"
fi
echo
echo "--- (3) INFORMATIONAL: append-only history naming a different family (never a failure) ---"
hist=$(harvest "agents/trending.md repos/trending.md" | sort -u)
printf '%s\n' "$cur" | cut -f1 | sort -u | while read -r s; do
  [ -z "$s" ] && continue
  cf=$(printf '%s\n' "$cur"  | awk -F'\t' -v s="$s" '$1==s{print $2}' | sort -u | tr '\n' ',' | sed 's/,$//')
  hf=$(printf '%s\n' "$hist" | awk -F'\t' -v s="$s" '$1==s{print $2}' | sort -u | tr '\n' ',' | sed 's/,$//')
  [ -n "$hf" ] && [ "$cf" != "$hf" ] && printf '  history-differs  %-44s current=%-14s history=%s\n' "$s" "$cf" "$hf"
done
echo
echo "FAILURES: $fails"
[ "$fails" -eq 0 ]
