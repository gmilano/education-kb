#!/usr/bin/env bash
# controls.sh — re-derive a CONTROL run from the token streams `region.sh`
# kept with `P115_TOK`, without touching the network.
#
# Usage: ./controls.sh <tokdir> <addresses> <mode>
#        mode: default | nostop | novanity | nor | flat
#
# P115-Q. Everything downstream of the token stream is pure stage C, so a
# control that only changes a MAP (nostop, novanity) or drops a LAYER (nor)
# is exactly reproducible from the saved stream. The gain is not speed, it is
# that the control and the census read the SAME snapshot of 296 moving
# repositories, which a separately fetched control cannot.
#
# `nor` is derived by removing layer-R tokens and the readme counter, which
# is precisely what `P115_NO_R=1` does upstream — and the suite asserts that
# the two agree row for row.
#
# `flat` relabels every layer-1 token as layer 0, which reproduces this
# instrument's OWN behaviour before the depth split. It is how `P115-N` stops
# being an anecdote about `moodle/moodle` and becomes a figure for the whole
# shelf: the rows the flat read would have placed, and the regions it would
# have given them.
set -uo pipefail
cd "$(dirname "$0")"

tokdir="${1:?tokdir}"
list="${2:-addresses.txt}"
mode="${3:-default}"

tmp="${TMPDIR:-/tmp}/p115ctl.$$"
mkdir -p "$tmp"
trap 'rm -rf "$tmp"' EXIT

case "$mode" in
  novanity) awk -F'\t' 'BEGIN{OFS="\t"} /^#/{print;next} NF>=3 && $2=="vanity"{$2="cc"} {print}' \
              country.region.tsv > "$tmp/country.tsv"
            cp stoplist.tsv "$tmp/stop.tsv" ;;
  nostop)   cp country.region.tsv "$tmp/country.tsv"
            printf '# stoplist DISABLED (mode nostop)\n' > "$tmp/stop.tsv" ;;
  *)        cp country.region.tsv "$tmp/country.tsv"
            cp stoplist.tsv "$tmp/stop.tsv" ;;
esac

printf 'slug\trc\tfiles\tvendored\tstruct\troot_struct\tstruct_read\tkinds\tcapped\twideline\tdom_0\tstop_0\tgtld_0\tvanity_0\tq_0\tunk_0\tcc_0\tnreg_0\tregions_0\tregion_0\tverdict\ttyped\ttyped_ev\tq_ev\tev_0\tclass_0\tdom_1\tcc_1\tnreg_1\tregion_1\tverdict_1\tev_1\tdom_r\tcc_r\tnreg_r\tregion_r\trverdict\tev_r\tinst\n'

while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac
  f="$tokdir/$(printf '%s' "$slug" | tr '/' '_').tok"

  if [ ! -f "$f" ]; then
    # P1040. An unread row is never zero -- and here it is never INVENTED
    # either: no saved stream means this control cannot speak for the row.
    printf '%s\t1' "$slug"
    i=3; while [ $i -le 20 ]; do printf '\t'; i=$((i+1)); done
    printf '\tNO-STREAM'
    i=22; while [ $i -le 39 ]; do printf '\t'; i=$((i+1)); done
    printf '\n'
    continue
  fi

  case "$mode" in
    nor)  awk -F'\t' '!($1=="D" && $2=="R") && $1!="I" && !($1=="C" && $2=="readme")' "$f" > "$tmp/row.tok" ;;
    flat) awk -F'\t' 'BEGIN{OFS="\t"} $1=="D" && $2=="1" {$2="0"} {print}' "$f" > "$tmp/row.tok" ;;
    *)    cp "$f" "$tmp/row.tok" ;;
  esac

  eval "$(awk -f place.awk "$tmp/country.tsv" "$tmp/stop.tsv" "$tmp/row.tok" \
          | sed 's/^\([a-z_0-9]*\)=\(.*\)$/\1="\2"/')"

  printf '%s\t0\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$files" "$vendored" "$struct" "$root_struct" "$struct_read" \
    "$kinds" "$capped" "$wideline" \
    "$dom_0" "$stop_0" "$gtld_0" "$vanity_0" "$q_0" "$unk_0" "$cc_0" \
    "$nreg_0" "$regions_0" "$region_0" "$verdict" \
    "$typed" "$typed_ev" "$q_ev" "$ev_0" "$class_0" \
    "$dom_1" "$cc_1" "$nreg_1" "$region_1" "$verdict_1" "$ev_1" \
    "$dom_r" "$cc_r" "$nreg_r" "$region_r" "$rverdict" "$ev_r" "$inst"
done < "$list"
