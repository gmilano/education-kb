#!/bin/sh
# p402 — ref-set identity fingerprint, reusing p370's rule rather than re-spelling it.
#
# p370's rule, inherited verbatim: a redirect serves ONE repository, so two addresses
# are the SAME repository only when their FULL REF SET matches. Identical HEAD alone
# is NOT identity — p370 demoted five pairs from STALE to DISTINCT on exactly that.
#
# Usage: ./refset.sh OWNER/NAME  ->  address<TAB>refs<TAB>head12<TAB>refset_fp12
a="$1"
refs=$(timeout 60 git ls-remote "https://github.com/$a" 2>/dev/null | sort)
if [ -z "$refs" ]; then printf '%s\tUNRESOLVED\t-\t-\n' "$a"; exit 0; fi
n=$(printf '%s\n' "$refs" | grep -c .)
head=$(printf '%s\n' "$refs" | awk '$2=="HEAD"{print substr($1,1,12); exit}')
fp=$(printf '%s\n' "$refs" | sha256sum | cut -c1-12)
printf '%s\t%s\t%s\t%s\n' "$a" "$n" "${head:-NONE}" "$fp"
