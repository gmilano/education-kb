#!/usr/bin/env bash
# parse_refs.sh — parse `git ls-remote --tags --heads` output into a census row.
#
# Reads ls-remote output on stdin, writes TAB-separated:
#   heads <TAB> tags_raw <TAB> tags_uniq <TAB> head_sha40
#
# The load-bearing rule (P107-C): `git ls-remote --tags` emits an ANNOTATED tag
# TWICE — once as refs/tags/X and once as the dereferenced refs/tags/X^{}. A
# census that counts `refs/tags/` lines overstates the release ladder by up to
# 2x. tags_uniq excludes the ^{} lines; tags_raw keeps them so the inflation
# factor stays auditable.
set -uo pipefail

in=$(cat)

heads=$(printf '%s\n' "$in" | grep -c $'\trefs/heads/' || true)
tags_raw=$(printf '%s\n' "$in" | grep -c $'\trefs/tags/' || true)
tags_uniq=$(printf '%s\n' "$in" | grep $'\trefs/tags/' | grep -vc '\^{}$' || true)

# HEAD: ls-remote --heads does not emit a bare "HEAD" row, so fall back to
# refs/heads/{main,master} in that order. Full 40 chars, never abbreviated (Gap 380).
head_sha=$(printf '%s\n' "$in" | awk -F'\t' '$2=="HEAD"{print $1; exit}')
[ -n "$head_sha" ] || head_sha=$(printf '%s\n' "$in" | awk -F'\t' '$2=="refs/heads/main"{print $1; exit}')
[ -n "$head_sha" ] || head_sha=$(printf '%s\n' "$in" | awk -F'\t' '$2=="refs/heads/master"{print $1; exit}')
[ -n "$head_sha" ] || head_sha="-"

printf '%s\t%s\t%s\t%s\n' "${heads:-0}" "${tags_raw:-0}" "${tags_uniq:-0}" "$head_sha"
