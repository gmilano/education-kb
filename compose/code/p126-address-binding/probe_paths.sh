#!/bin/sh
# ACTION AL -- the grant-path census, extended by the two conventions
# `ACTION AI` found this KB's toolchain blind to.
#
# STANDARD is the path list prior passes probed. NEW adds the dual-licence
# filename convention (`LICENSE.GPL`, `LICENSE.MPL`, ...) and the WordPress
# plugin header in `readme.txt` -- the convention `P125-A` defect 3 proved
# this corpus blind to on `LearnPress/learnpress`.
#
# Every probe reads the repository's own bytes on its real default branch:
# raw.githubusercontent.com resolves `HEAD` to the default branch, so no
# branch is guessed. Output is TSV; a 200 is a grant file that EXISTS.
#
# usage: probe_paths.sh ADDRESS_FILE > out/al-probe.tsv
set -u

STANDARD="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING
COPYING.txt COPYING.LESSER LICENSE-MIT LICENSE-APACHE LICENSE-CODE
LICENSE-DOCS DESCRIPTION"
NEW="LICENSE.GPL LICENSE.LGPL LICENSE.MPL LICENSE.APACHE LICENSE.BSD
readme.txt README.txt Readme.txt"

probe() {
    addr=$1; path=$2; kind=$3
    code=$(curl -sS -o /dev/null -w "%{http_code}" --max-time 20 \
        "https://raw.githubusercontent.com/$addr/HEAD/$path" 2>/dev/null)
    [ -z "$code" ] && code=000
    printf '%s\t%s\t%s\t%s\n' "$addr" "$path" "$kind" "$code"
}

printf 'address\tpath\tkind\thttp\n'
while IFS= read -r addr; do
    [ -z "$addr" ] && continue
    for p in $STANDARD; do probe "$addr" "$p" STANDARD; done
    for p in $NEW;      do probe "$addr" "$p" NEW; done
done < "$1"
