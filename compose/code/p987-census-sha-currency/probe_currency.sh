#!/bin/sh
# pass96 census staleness audit: is the pinned SHA still the tip of the pinned ref?
slug=$1; ref=$2; pinned=$3
out=$(git ls-remote https://github.com/"$slug" 2>/dev/null)
if [ -z "$out" ]; then printf '%s\t%s\t%s\tNO-REACH\t-\n' "$slug" "$ref" "$pinned"; exit 0; fi
# try ref as branch, then tag, then as-is
tip=$(printf '%s\n' "$out" | awk -v r="$ref" '$2=="refs/heads/"r || $2=="refs/tags/"r {print $1; exit}')
if [ -z "$tip" ]; then printf '%s\t%s\t%s\tREF-GONE\t-\n' "$slug" "$ref" "$pinned"; exit 0; fi
short=$(printf '%s' "$tip" | cut -c1-7)
if [ "$short" = "$pinned" ]; then v=CURRENT; else v=MOVED; fi
printf '%s\t%s\t%s\t%s\t%s\n' "$slug" "$ref" "$pinned" "$v" "$short"
