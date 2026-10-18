#!/usr/bin/env bash
# `ACTION p289`'s ONLINE half.  P237: this file has NO classifier.  It resolves the ref,
# walks the licence-path ladder, and records what each payload IS.  `restatement.py`
# decides what the text MEANS.
#
# usage: probe.sh <slugs-file> <out-dir>
#
# 🔴 The point of this probe is the pair, not the file.  A repository that splits its grant
# by directory serves MORE THAN ONE licence payload, and grading it on the first 200 is how
# a dual-licensed curriculum repo gets filed under its CODE licence while the DATA it exists
# to publish sits under another one.  So every rung that answers 200 is recorded, each with
# its own verdict, and nothing stops at the first hit.
set -u
export GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/true
HERE="$(cd "$(dirname "$0")" && pwd)"
SLUGS="${1:?usage: probe.sh <slugs-file> <out-dir>}"
OUT="${2:?usage: probe.sh <slugs-file> <out-dir>}"
mkdir -p "$OUT"

# T272: the ladder is PRINTABLE and lives in one place.  British AND American spellings,
# because `oak-open-curriculum-ecosystem` serves `LICENCE` and 404s at `LICENSE`.
#
# 🔴 `p283`'s ladder ratchet REJECTED this file's first ladder as `CASE-UNVARIED/no-upper-ext`
# — a hand-written list of uppercase stems with lowercase extensions only.  That is the same
# defect `p288` was built to fix one family over: `anastasasenov/bbmcps` serves lower-case
# `readme.md` and 404s at `README.md` on every ref, so a ladder that does not vary CASE
# publishes a FALSE ABSENCE.  The ladder is therefore GENERATED as a cross product of
# stem x extension with both varied, which is the only shape that closes the case axis.
# 🔵 The literals live IN the `for` lists, not in a variable the loop expands.  p284's
# generator finding is that a ladder assembled through an indirection is graded on the
# indirection, so a cross product that varies case is invisible unless the cross product
# is written where it can be read.
PATHS=""
for _s in LICENSE LICENCE License Licence license licence \
          DATA-LICENSE DATA-LICENCE data-license data-licence \
          CODE-LICENSE CODE-LICENCE code-license code-licence \
          DATA_LICENSE CODE_LICENSE; do
  for _e in "" .md .MD .txt .TXT; do
    PATHS="$PATHS $_s$_e"
  done
done

# The GNU `COPYING` convention gets its own cross product so the case axis is closed for
# that family too and not merely for `licence`.
for _s in COPYING Copying copying; do
  for _e in "" .md .TXT; do
    PATHS="$PATHS $_s$_e"
  done
done

# 🔴 The directory rungs are ENUMERATED, not crossed.  p289's first ladder crossed stems x
# extensions x directories and reached **597 requests per repository** against an original
# 18 — a fix measured and rejected, exactly as `p286` rejected its own first fix.  A ladder
# is for the COMMON spellings; exhaustive recovery is `pass275-grant-enumeration`'s job, and
# `p288` proved that is what actually finds an odd spelling (`bbmcps` serves lower-case
# `readme.md`, and the TREE found it after the ladder had published a false absence).
PATHS="$PATHS docs/LICENSE.md docs/LICENCE.md data/LICENSE.md data/LICENCE.md ontology/LICENSE.md"

printf 'slug\tref\thead_sha\tpath\thttp\tbytes\tsha256_12\tclassification\tattribution\tbody_vs_summary\tauthority_host\n'
while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  case "$slug" in \#*) continue ;; esac

  symref=$(git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  ref=$(printf '%s' "$symref" | awk '/^ref:/{sub("refs/heads/","",$2);print $2;exit}')
  # p288: the `ref: refs/heads/main\tHEAD` line also ends in HEAD, so anchor on the OID.
  sha=$(printf '%s' "$symref" | awk '$1 ~ /^[0-9a-f]{40}$/ && $2=="HEAD"{print substr($1,1,12);exit}')
  if [ -z "$ref" ]; then
    printf '%s\tNO-REF\t-\t-\t-\t-\t-\tNO-GRANT\t-\t-\t-\n' "$slug"
    continue
  fi

  hits=0
  for p in $PATHS; do
    code=$(curl -sL --max-time 30 -o "$OUT/body.tmp" \
             -w '%{http_code}' "https://raw.githubusercontent.com/$slug/$ref/$p" 2>/dev/null)
    [ "$code" = "200" ] || continue
    hits=$((hits + 1))
    bytes=$(wc -c < "$OUT/body.tmp" | tr -d ' ')
    # p1058: a 200 with an EMPTY body is not a grant.
    if [ "$bytes" -eq 0 ]; then
      printf '%s\t%s\t%s\t%s\t200\t0\t-\tNO-GRANT\tNONE\tNO-SUMMARY\t-\n' "$slug" "$ref" "$sha" "$p"
      continue
    fi
    dig=$(sha256sum "$OUT/body.tmp" | cut -c1-12)
    safe=$(printf '%s' "$slug" | tr '/' '_')
    # 🔴 `$safe__` parses as the variable `safe__`, not `safe` followed by `__`.
    # `set -u` caught it on the first run; without it this would have written every
    # payload to the same path and graded the LAST one five times.
    keep="$OUT/${safe}__$(printf '%s' "$p" | tr '/' '_')"
    cp "$OUT/body.tmp" "$keep"
    read -r cls attr bvs host <<EOF
$(python3 -I -c "
import sys
sys.path.insert(0,'$HERE')
from restatement import classify_payload, attribution_verdict, body_vs_summary_attribution, named_external_authority
t=open('$keep',encoding='utf-8',errors='replace').read()
a=named_external_authority(t)
print(classify_payload(t), attribution_verdict(t), body_vs_summary_attribution(t), (a[1] if a else '-'))
")
EOF
    printf '%s\t%s\t%s\t%s\t200\t%s\t%s\t%s\t%s\t%s\t%s\n' \
      "$slug" "$ref" "$sha" "$p" "$bytes" "$dig" "$cls" "$attr" "$bvs" "$host"
  done

  if [ "$hits" -eq 0 ]; then
    printf '%s\t%s\t%s\t-\t404\t-\t-\tNO-GRANT\tNONE\tNO-SUMMARY\t-\n' "$slug" "$ref" "$sha"
  fi
done < "$SLUGS"
rm -f "$OUT/body.tmp"
