#!/bin/sh
# p885: grant ladder that resolves the DEFAULT BRANCH before probing licence bytes.
#
# Discharges `884-G2`. The p884 ladder (compose/code/p213-grant-resolver) probed
# exactly two refs, `main` and `master`. p884 found the defect on
# `cilt-uct/sakai-skin-vula` (default `r/23.x`) and correctly called the read that
# did succeed "luck, not method" -- the repo happens to retain a `master` branch.
#
# p885 MEASURED the exposure instead of reasoning about it, over the 6,486-repo
# re-sweep of the 33 capped organisations (evidence/resweep-884G1.*.tsv):
#
#   344 / 6,486  (5.3%)  default branch is neither `main` nor `master`
#   201 of those carry a resolvable licence
#    49 of those are PERMISSIVE
#    13 of those 49 (26.5%) have NO `main` and NO `master` branch at all
#
# Those 13 are not "lucky" -- the two-name ladder reports NO-GRANT-FILE on a
# repository that carries a real permissive grant. That is p845's
# manufactured-absence class, in the grant channel. One of the 13 is
# `ox-it/wl-roster2` (ECL-2.0, Sakai), which is this KB's own subject area.
#
# Calibration, recorded because it bounds the claim: on the three fixtures that DO
# retain a `master` branch (`odoo/odoo` @ `20.0`, `openeducat/openeducat_erp` @
# `19.0`, `cilt-uct/sakai-skin-vula` @ `r/23.x`) the `master` bytes and the
# default-ref bytes are byte-identical (sha256_12 abc09dad5f84 / 528f84036800 /
# 0688f62d04f1). So this defect manufactures ABSENCE; it does not substitute a
# wrong grant. Both failure modes are repaired below, but only the first was found.
#
# usage: fetch_grants.sh <slugs-file> <out-dir>
SLUGS="$1"; OUT="$2"; mkdir -p "$OUT"

# Resolve the default branch over `git ls-remote --symref`, the channel this KB has
# measured as open for every pass since p881. Empty output = unresolved, and the
# caller must fall through rather than guess.
default_ref() {
  git ls-remote --symref "https://github.com/$1" HEAD 2>/dev/null \
    | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}'
}

PATHS="LICENSE LICENSE.md LICENSE.txt license.txt COPYING COPYING.txt COPYING.TXT LICENCE"

probe_ref() {   # slug ref outfile  ->  prints "path<TAB>bytes<TAB>sha" on hit
  for path in $PATHS; do
    code=$(curl -sS -o "$3" -w '%{http_code}' --max-time 30 \
            "https://raw.githubusercontent.com/$1/$2/$path" 2>/dev/null)
    if [ "$code" = "200" ]; then
      printf '%s\t%s\t%s\n' "$path" "$(stat -c%s "$3")" "$(sha256sum "$3" | cut -c1-12)"
      return 0
    fi
  done
  return 1
}

fetch_one() {
  slug="$1"; out="$2"
  o=${slug%%/*}; r=${slug##*/}
  key="${o}__${r}"
  f="$out/$key.body"

  # ---- p885 FIX: the resolved default branch is probed FIRST. -----------------
  dref=$(default_ref "$slug")
  if [ -n "$dref" ]; then
    if hit=$(probe_ref "$slug" "$dref" "$f"); then
      printf '%s\t%s\t%s\t200\t%s\t%s\tsymref\n' "$slug" "$dref" \
        "$(echo "$hit" | cut -f1)" "$(echo "$hit" | cut -f2)" "$(echo "$hit" | cut -f3)"
      return 0
    fi
  fi

  # ---- fallback: the historical two-name ladder, for repos whose default ref
  # ---- carries no licence file but an older branch does.
  for ref in main master; do
    [ "$ref" = "$dref" ] && continue
    if hit=$(probe_ref "$slug" "$ref" "$f"); then
      printf '%s\t%s\t%s\t200\t%s\t%s\tfallback\n' "$slug" "$ref" \
        "$(echo "$hit" | cut -f1)" "$(echo "$hit" | cut -f2)" "$(echo "$hit" | cut -f3)"
      return 0
    fi
  done

  # ---- SPLIT-FILE DUAL GRANT, carried forward from p884 on its evidence.
  # `RWTH-OS/eduOS-rs` is dual LICENSE-APACHE + LICENSE-MIT; one `license.spdx_id`
  # field cannot express two grants, and a studio told "Apache-2.0" alone silently
  # loses the MIT option it is entitled to. p885 adds the resolved default ref to
  # the refs this arm tries, for the same reason as above.
  for ref in $dref main master; do
    [ -z "$ref" ] && continue
    a=""; m=""
    for ap in LICENSE-APACHE LICENSE-APACHE-2.0 LICENSE.APACHE; do
      c=$(curl -sS -o "$f" -w '%{http_code}' --max-time 30 \
           "https://raw.githubusercontent.com/$slug/$ref/$ap" 2>/dev/null)
      [ "$c" = "200" ] && { a="$ap"; break; }
    done
    for mp in LICENSE-MIT LICENSE.MIT; do
      c=$(curl -sS -o "$out/$key.body2" -w '%{http_code}' --max-time 30 \
           "https://raw.githubusercontent.com/$slug/$ref/$mp" 2>/dev/null)
      [ "$c" = "200" ] && { m="$mp"; break; }
    done
    if [ -n "$a" ] && [ -n "$m" ]; then
      b1=$(stat -c%s "$f"); b2=$(stat -c%s "$out/$key.body2")
      s1=$(sha256sum "$f" | cut -c1-12); s2=$(sha256sum "$out/$key.body2" | cut -c1-12)
      printf '%s\t%s\t%s+%s\t200\t%s+%s\t%s+%s\tdual\n' \
        "$slug" "$ref" "$a" "$m" "$b1" "$b2" "$s1" "$s2"
      return 0
    fi
    rm -f "$out/$key.body2"
  done

  rm -f "$f" "$out/$key.body2"
  # The unresolved default ref is reported, so a 404 can never again be mistaken
  # for "this repository has no licence" when the truth is "we probed two guesses".
  printf '%s\t%s\t-\t404\t-\t-\tno-grant\n' "$slug" "${dref:-UNRESOLVED}"
}

if [ -n "$SLUGS" ]; then
  while IFS= read -r slug; do
    [ -n "$slug" ] && fetch_one "$slug" "$OUT"
  done < "$SLUGS"
fi
