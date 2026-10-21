#!/bin/sh
# `p367-bare-slug-channel` — the ONLINE leg of `ACTION ZZ-bv`.
#
# Channel B's four offline arms are allowed to be imprecise; this script is what
# makes that honest.  It adjudicates every channel-B survivor with
# `git ls-remote --symref`, the only instrument in this environment that can say a
# repository exists, and it prints the survivor PRECISION rather than asserting it.
#
#   probe_slugs.sh adjudicate <candidates file>   -> slug<TAB>LIVE|NO-REF<TAB>head
#   probe_slugs.sh refset <slugs file>            -> slug<TAB>fingerprint of ALL refs
#
# 🔴 The `refset` mode exists because a shared `HEAD` sha does NOT prove one
# repository.  `p366`'s identity test stopped at `HEAD`; two addresses serving the
# same commit may be a rename-redirect OR a fork nobody has pushed to since.  The
# full-ref-set fingerprint separates `SAME-REF-SET` from `SAME-HEAD-ONLY` — and it
# still cannot separate a redirect from a pristine fork, which is stated in the
# README rather than papered over.
set -u
PAR=${PAR:-6}

one_head() {
    out=$(timeout 25 git ls-remote --symref "https://github.com/$1" HEAD 2>/dev/null)
    if [ -n "$out" ]; then
        h=$(printf '%s\n' "$out" | awk '/HEAD$/ && $1 !~ /^ref:/ {print substr($1,1,10); exit}')
        printf '%s\tLIVE\t%s\n' "$1" "$h"
    else
        printf '%s\tNO-REF\t-\n' "$1"
    fi
}

one_refset() {
    fp=$(timeout 30 git ls-remote "https://github.com/$1" 2>/dev/null \
         | awk '{print $1" "$2}' | sort | md5sum | cut -c1-12)
    printf '%s\t%s\n' "$1" "$fp"
}

mode=${1:-}
arg=${2:-}

# 🔴 The per-slug CHILD branch must be dispatched BEFORE the empty-input guard, and
# p367's first draft got that backwards.  `xargs` re-invokes this script with a SLUG
# in $2, not a file; the guard's `[ ! -s "$arg" ]` was therefore true for every one
# of the 823 children and the whole sweep printed 823 refusals and measured nothing.
# 🟢 It is the `P541` defect class arriving through the guard built to prevent it —
# an instrument that reports a refusal when what it means is "I was handed a
# different kind of argument".  Caught because the sweep was LOUD; a guard that had
# exited 0 would have published an empty adjudication as a clean result.
if [ "${P367_CHILD:-}" = "head" ]; then one_head "$arg"; exit 0; fi
if [ "${P367_CHILD:-}" = "refset" ]; then one_refset "$arg"; exit 0; fi

file=$arg
case "$mode" in
  adjudicate|refset) ;;
  *) echo "usage: probe_slugs.sh adjudicate|refset <slugs file>" >&2; exit 2 ;;
esac
# P541: an instrument that takes its population by argument must refuse an empty one.
if [ -z "$file" ] || [ ! -s "$file" ]; then
    echo "p367-probe-slugs: no non-empty slug file given — refusing to publish a verdict over nothing" >&2
    exit 2
fi

self=$0
# 🔴 NEWLINE-delimited, never whitespace-delimited, and p367's control harness
# learned this the expensive way.  A default `xargs -a` splits on SPACES: fed a
# population sampled from the REJECTED set — whose members legitimately contain
# spaces and pipes, since that is often why they were rejected — it tore each row
# into fragments and probed the fragments.  🔴 It then reported two of them LIVE,
# which read exactly like two false rejections by the filter and were nothing of the
# kind.  🟢 The fragments were still worth having: they are how the GLUED-SLUG miss
# class below was found.  But a control that manufactures its own findings is worse
# than no control, so the delimiter is pinned here.
if [ "$mode" = adjudicate ]; then
    tr '\n' '\0' < "$file" | P367_CHILD=head xargs -0 -n1 -P"$PAR" "$self" adjudicate
else
    tr '\n' '\0' < "$file" | P367_CHILD=refset xargs -0 -n1 -P"$PAR" "$self" refset
fi
