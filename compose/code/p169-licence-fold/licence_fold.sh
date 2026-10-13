#!/bin/sh
# P169-A step 0 - the FOLD, plus the word diff that depends on it.
#
# WHY THIS EXISTS (T205): SPDX's canonical licence texts carry typographic quotation marks
# and a (c) glyph; the FSF's own ASCII bodies carry neither. Diffed raw, an UNMODIFIED
# GPL-3.0 body reads as 71 added / 71 removed words against the SPDX copy and looks
# rewritten. The deviation is the instrument, not the licence.
#
# Usage:  ./licence_fold.sh <canonical-file> <repo-body-file>
# Output: one TSV line - added<TAB>removed, counted on folded word streams.
#
# The fold normalises exactly four classes and NOTHING else, so a real textual change
# still shows:
#   U+201C / U+201D  curly double quotes  -> "
#   U+2018 / U+2019  curly single quotes  -> '
#   U+00A9           (c) glyph            -> (C)
#   http://                               -> https://   (the FSF URL-scheme revision class)

set -eu

fold_stream() {
    perl -CSD -pe 's/[\x{201C}\x{201D}]/"/g;
                   s/[\x{2018}\x{2019}]/\x27/g;
                   s/\x{00A9}/(C)/g;
                   s|http://|https://|g' "$1" \
    | tr -s '[:space:]' '\n' \
    | grep -v '^$'
}

[ $# -eq 2 ] || { echo "usage: $0 <canonical> <body>" >&2; exit 2; }
[ -f "$1" ] || { echo "no such file: $1" >&2; exit 2; }
[ -f "$2" ] || { echo "no such file: $2" >&2; exit 2; }

a=$(mktemp); b=$(mktemp)
trap 'rm -f "$a" "$b"' EXIT
fold_stream "$1" > "$a"
fold_stream "$2" > "$b"

added=$(diff "$a" "$b" | grep -c '^>' || true)
removed=$(diff "$a" "$b" | grep -c '^<' || true)
printf '%s\t%s\n' "$added" "$removed"
