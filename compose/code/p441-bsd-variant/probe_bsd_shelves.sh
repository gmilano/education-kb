#!/usr/bin/env bash
# p441 — EVERY BSD ROW THIS BASE SELLS, PROBED LIVE AND GRADED BY THE NEW PROFILE.
#
# 🔵 The loop is SOURCED, never rewritten: `lib/probe_payload.sh` exists because two
# passes re-wrote it by hand and re-imported `P171` both times (its own header, lines
# 6–12).  `p440` recorded sourcing it with `set +u`; the same idiom is used here.
#
# Usage: probe_bsd_shelves.sh [slug ...]      TSV on stdout.
#        With no argument it probes the ten BSD rows live on this base's shelves.
# 🔴 `set -u` IS DELIBERATELY NOT RESTORED AFTER THE SOURCE, AND THE FIRST DRAFT OF THIS
# FILE PROVED WHY.  It sourced the loop under `set +u`, restored `set -u` on the next
# line, and reported 🔴 `NO-PAYLOAD` for ALL ELEVEN shelved repositories — while a bare
# `curl` against the first of them returned `200` and 1 516 B in the same shell.  The
# nil was my own shell option, and a nil reads exactly like coverage: eleven rows of
# "this base sells licences it cannot reach".  `probe_repo` uses unset variables
# internally by design, which is why its own header says to source it with `set +u`;
# the option stays off for the CALLS, not merely for the source.
set -o pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
LIB="$HERE/../lib"
set +u
# shellcheck disable=SC1091
. "$LIB/probe_payload.sh"

SLUGS=("$@")
if [ "${#SLUGS[@]}" -eq 0 ]; then
  SLUGS=(
    Open-TutorAi/open-tutor-ai-CE     # agents/top.md — the row Gap 440-A named
    jupyterlab/jupyter-ai
    QuantStack/jupyter-ai-tutor
    ucbds-infra/otter-grader
    ucbds-infra/ottr
    jupyterhub/ltiauthenticator
    jupyterhub/jupyterhub
    jupyter/nbgrader
    jupyterlite/jupyterlite
    OpenOLAT/qtiworks
    open-webui/open-webui             # 🔴 the shelf itself says "not stock BSD-3"
  )
fi

OUT="${OUT:-$HERE/payloads}"
mkdir -p "$OUT"
printf 'slug\tbranch\tfile\tbytes\tfamily\tsha256_12\tlocal\n'
for slug in "${SLUGS[@]}"; do
  row="$(probe_repo "$slug" 2>/dev/null | tail -1)"
  branch=$(printf '%s' "$row" | cut -f2)
  file=$(printf '%s' "$row" | cut -f3)
  bytes=$(printf '%s' "$row" | cut -f4)
  fam=$(printf '%s' "$row" | cut -f5)
  if [ "$file" = "NO-PAYLOAD" ] || [ -z "$file" ]; then
    printf '%s\t%s\tNO-PAYLOAD\t0\t-\t-\t-\n' "$slug" "${branch:--}"
    continue
  fi
  dest="$OUT/$(printf '%s' "$slug" | tr '/' '_').payload"
  code=$(curl -sS -o "$dest" --max-time 25 -w '%{http_code}' \
         "https://raw.githubusercontent.com/$slug/$branch/$file" 2>/dev/null)
  if [ "$code" != "200" ]; then
    printf '%s\t%s\t%s\t%s\t%s\tHTTP-%s\t-\n' "$slug" "$branch" "$file" "$bytes" "$fam" "$code"
    continue
  fi
  d=$(sha256sum "$dest" | cut -c1-12)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$branch" "$file" \
         "$(wc -c < "$dest" | tr -d ' ')" "$fam" "$d" "$dest"
done
