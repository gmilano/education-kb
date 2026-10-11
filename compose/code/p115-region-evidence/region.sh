#!/usr/bin/env bash
# region.sh -- REGION-EVIDENCE census over this KB's shelf addresses.
#
# WHY THIS AXIS, AND WHY NOW. Eight passes have measured this shelf:
#   p107 tag COUNT              how much ref traffic
#   p108 release IDENTITY       can I pin it
#   p109 commit RECENCY         is it alive
#   p110 author CONCENTRATION   what happens if they stop
#   p111 verification SURFACE   can the tree tell me when I broke it
#   p112 dependency CLOSURE     does it resolve to the same bytes twice
#   p113 provider BINDING       whose model does it call
#   p114 lock REACH             does the lock reach the manifest
#
# Every one of them published its figures by region, and every one of them
# published the same caveat: the regional read describes 104 of 296 rows,
# because `orgs.region.tsv` (P112-L) places an ORG only when this KB already
# records its home. p113 opened `Gap 403` on it, p114 corroborated it from an
# independent axis, and `intel/market.md` pre-registered the remedy:
#
#   Gap 403  "The remedy is offline, zero-egress and bounded -- extend the
#             placement file -- which makes it the cheapest open item on this
#             page."
#
# p115 runs that remedy and MEASURES whether it is in fact cheap. It asks the
# only question about region a repository can answer about itself:
#
#   does the tree COMMIT an address that places it?
#
# Ninth axis in nine passes and the FIFTH read from the TREE. It is also the
# first pass whose axis is the brief's own `region` field rather than a
# property of the code -- and the brief is explicit about why it matters:
# "A finding with no region attached is worth less than one that is placed."
#
# CHANNEL. Anonymous git lane only, re-probed live this pass (P107-A, P247,
# P249 -- all carried, none re-discovered):
#   git ls-remote / git fetch                 rc=0
#   raw.githubusercontent.com/<slug>/HEAD/..  200
#   api.github.com                            403
#   every non-GitHub host                     000 / connect_rejected (P798)
# Tree from a depth-1 blob-filtered fetch; evidence-file BODIES from a
# batched lazy blob fetch against the same promisor remote (P111-H, reused by
# p112, p114 and reused again here).
#
# MODES -- every rule this instrument adds is also measurable as a CONTROL,
# so none of its claims rests on assertion:
#   (default)          layer S + layer R, stoplist on, vanity class on
#   P115_NO_STOP=1     stoplist disabled      -> measures P115-E's contribution
#   P115_NO_VANITY=1   vanity class as `cc`   -> measures P115-D's contribution
#   P115_NO_R=1        layer R not read       -> measures layer R's contribution
#   P115_CAP=<n>       structured blobs read per repo (default 40)
#   P115_TOK=<dir>     keep each row's TOKEN STREAM in <dir>, so the controls
#                      re-derive from the SAME snapshot instead of refetching
#                      (P115-Q)
#   P115_BASE=<url>    transport swap, so the suite drives this same code
#                      against real git repositories over file:// (never a mock)
set -uo pipefail
cd "$(dirname "$0")"

list="${1:-addresses.txt}"
workroot="${P115_WORK:-${TMPDIR:-/tmp}/p115work}"
BASE="${P115_BASE:-https://github.com}"
NO_STOP="${P115_NO_STOP:-0}"
NO_VANITY="${P115_NO_VANITY:-0}"
NO_R="${P115_NO_R:-0}"
TOK="${P115_TOK:-}"
CAP="${P115_CAP:-40}"

mkdir -p "$workroot"
[ -n "$TOK" ] && mkdir -p "$TOK"

# ---- the two committed maps, as this run will use them --------------------
cmap="$workroot/maps/country.region.tsv"
smap="$workroot/maps/stoplist.tsv"
mkdir -p "$workroot/maps"
if [ "$NO_VANITY" = 1 ]; then
  # P115-D's control: a vanity ccTLD is read as a country code.
  awk -F'\t' 'BEGIN{OFS="\t"} /^#/{print;next} NF>=3 && $2=="vanity"{$2="cc"} {print}' \
      country.region.tsv > "$cmap"
else
  cp country.region.tsv "$cmap"
fi
if [ "$NO_STOP" = 1 ]; then
  # P115-E's control: no host is excluded for being a service.
  printf '# stoplist DISABLED for this run (P115_NO_STOP=1)\n' > "$smap"
else
  cp stoplist.tsv "$smap"
fi

# 38 columns. `verdict` is column 21 and it is the only column a reader
# should ever filter a REGION on: columns 26-31 are the nested-declaration
# contrast and 32-37 the README ceiling, and neither is folded into it.
printf 'slug\trc\tfiles\tvendored\tstruct\troot_struct\tstruct_read\tkinds\tcapped\twideline\tdom_0\tstop_0\tgtld_0\tvanity_0\tq_0\tunk_0\tcc_0\tnreg_0\tregions_0\tregion_0\tverdict\ttyped\ttyped_ev\tq_ev\tev_0\tclass_0\tdom_1\tcc_1\tnreg_1\tregion_1\tverdict_1\tev_1\tdom_r\tcc_r\tnreg_r\tregion_r\trverdict\tev_r\tinst\n'

while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac

  d="$workroot/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$d" "$d.ev" "$d.kinds" "$d.body" "$d.tok"; mkdir -p "$d"
  git init -q --bare "$d" 2>/dev/null

  case "$slug" in
    *://*) url="$slug" ;;
    *)     url="$BASE/$slug" ;;
  esac

  git --git-dir="$d" remote add origin "$url" 2>/dev/null
  git --git-dir="$d" config remote.origin.promisor true
  git --git-dir="$d" config remote.origin.partialclonefilter blob:none

  if ! git --git-dir="$d" fetch -q --depth=1 --filter=blob:none origin HEAD 2>/dev/null; then
    if ! git --git-dir="$d" fetch -q --depth=1 origin HEAD 2>/dev/null; then
      # P1040. AN UNREAD ROW IS NEVER ZERO.
      # 31 columns, every one of them explicit: rc=1, UNREAD in the verdict
      # column (20), and NOTHING in the figure columns -- an unread row that
      # printed 0 would be counted as "no evidence found" by every reader.
      printf '%s\t1' "$slug"
      i=3; while [ $i -le 20 ]; do printf '\t'; i=$((i+1)); done
      printf '\tUNREAD'
      i=22; while [ $i -le 39 ]; do printf '\t'; i=$((i+1)); done
      printf '\n'
      rm -rf "$d"; continue
    fi
  fi

  tree=$(git --git-dir="$d" ls-tree -r FETCH_HEAD 2>/dev/null)
  if [ -z "$tree" ]; then
    printf '%s\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t0\t-\t-\tempty-tree\t0\t-\t-\t-\t-\t0\t0\t0\t-\tn-none\t-\t0\t0\t0\t-\tr-none\t-\t0\n' "$slug"
    rm -rf "$d"; continue
  fi

  printf '%s\n' "$tree" | awk -v cap="$CAP" -f evidence.awk > "$d.ev"

  # ---- stage B: the sha -> kind map, and the bodies ----------------------
  # <sha> TAB <layer>:<kind>, layer 0 = ROOT, 1 = nested, R = readme.
  # A blob that appears at BOTH depths (identical content committed twice)
  # must read as the ROOT one, so the sort puts `0:` first and the dedup
  # keeps the first line per sha -- never the last.
  awk -F'\t' -v nor="$NO_R" 'BEGIN{OFS="\t"}
      $1=="S" { print $3, ($4 == 0 ? "0:" : "1:") $2 }
      $1=="R" && nor!="1" { print $3, "R:readme" }' "$d.ev" \
    | sort -u | sort -k1,1 -k2,2 | awk -F'\t' '!seen[$1]++' > "$d.kinds"

  : > "$d.body"
  if [ -s "$d.kinds" ]; then
    # P112-I, carried: bodies go to a FILE, never a pipe into an early-exiting
    # reader. P1040: a timeout is a declared short read, not a zero.
    cut -f1 "$d.kinds" | timeout 180 git --git-dir="$d" cat-file --batch > "$d.body" 2>/dev/null
  fi

  awk -f tokens.awk "$d.kinds" "$d.body" > "$d.tok"
  # stage A's own counters travel with the tokens. With layer R switched off
  # the readme COUNTER is dropped too: left in, the row would report
  # `r-no-address` -- "there is a README and it holds no address" -- when the
  # truth is "layer R was not read at all". A control that misreports its own
  # reason is worse than no control.
  if [ "$NO_R" = 1 ]; then
    awk -F'\t' '$1=="C" && $2!="readme"' "$d.ev" >> "$d.tok"
  else
    awk -F'\t' '$1=="C"' "$d.ev" >> "$d.tok"
  fi

  # P115-O. THE KEY CLASS MUST INCLUDE DIGITS, AND THIS IS NOT A NITPICK.
  # p112 and p114 quote their `eval` keys with `[a-z_]*`, which is right for
  # THEIR key names. This pass's layer keys are `region_0`, `dom_1`, `cc_r`
  # -- and `[a-z_]*` does not match a digit, so `region_0=North America`
  # passed through UNQUOTED and the shell ran `America` as a command. The row
  # still printed; it printed with the region column EMPTY and an extra line
  # of output. A copied idiom is a parameter too.
  # P115-Q. THE TOKEN STREAM IS KEPT SO THE CONTROLS DO NOT REFETCH.
  # p112 and p114 ran their controls as SEPARATE censuses, hours or minutes
  # apart, and a control fetched from a different snapshot of 296 moving
  # repositories is measuring two things at once. Everything downstream of
  # this point is pure stage C, so the three controls of this pass are
  # re-derived from these exact bytes by `controls.sh` -- same window, same
  # trees, zero extra egress, and re-runnable by any later pass.
  [ -n "$TOK" ] && cp "$d.tok" "$TOK/$(printf '%s' "$slug" | tr '/' '_').tok"

  eval "$(awk -f place.awk "$cmap" "$smap" "$d.tok" \
          | sed 's/^\([a-z_0-9]*\)=\(.*\)$/\1="\2"/')"

  rm -rf "$d" "$d.ev" "$d.kinds" "$d.body" "$d.tok"

  printf '%s\t0\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$files" "$vendored" "$struct" "$root_struct" "$struct_read" \
    "$kinds" "$capped" "$wideline" \
    "$dom_0" "$stop_0" "$gtld_0" "$vanity_0" "$q_0" "$unk_0" "$cc_0" \
    "$nreg_0" "$regions_0" "$region_0" "$verdict" \
    "$typed" "$typed_ev" "$q_ev" "$ev_0" "$class_0" \
    "$dom_1" "$cc_1" "$nreg_1" "$region_1" "$verdict_1" "$ev_1" \
    "$dom_r" "$cc_r" "$nreg_r" "$region_r" "$rverdict" "$ev_r" "$inst"
done < "$list"
