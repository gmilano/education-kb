#!/usr/bin/env bash
# `p444/probe.sh` — the repository probe for pass 444, built on the shared controls.
#
# Channel, per `p442`: existence and default branch from `git ls-remote`; EVERY grant path
# from `git ls-tree -r` over a BLOBLESS clone (so the root row is never mistaken for the
# whole grant); every payload measured FROM THE FILE via `lib/measure` (so `P834`'s
# trailing-newline run survives into the published cell).
#
# No `curl`.  The fetch half of `probe_payload.sh` is network-denied on this host and this
# probe exists to get the same rows through the git channel instead.
#
# Usage: probe.sh <slugfile> <outdir>   slugfile = one `owner/name` per line, `#` comments ok
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
LIB="$HERE/../lib"
. "$LIB/licence_path.sh"

# 🔴 THE ROOT CAUSE, not just the symptom.  A `git clone` of a slug that 404s does not
# fail: it PROMPTS for a username on the terminal, and with the loop's stdin attached that
# prompt swallows the remaining slug file in one read.  The 321-slug sweep died on the
# first dead address on the shelf.  `</dev/null` and FD 3 stop the swallow; this stops the
# prompt, so a dead address fails FAST and is RECORDED as absent instead of hanging.
export GIT_TERMINAL_PROMPT=0
export GIT_ASKPASS=/bin/true
export GCM_INTERACTIVE=never

SLUGS="${1:?need a slug file}"
OUT="${2:?need an output dir}"
mkdir -p "$OUT/payloads"
TSV="$OUT/probe.tsv"
printf 'slug\thead_sha\tdefault_branch\tgrant_paths\tpath\tbytes\tsha12\tfamily\n' > "$TSV"

while read -r slug <&3; do
  case "$slug" in ''|\#*) continue ;; esac
  url="https://github.com/$slug"

  # --- existence + default branch, without cloning -------------------------------------
  lsr=$(timeout 90 git ls-remote --symref "$url" HEAD 2>/dev/null </dev/null) || {
    printf '%s\tABSENT-OR-UNREACHABLE\t-\t-\t-\t-\t-\t-\n' "$slug" >> "$TSV"; continue; }
  head_sha=$(printf '%s\n' "$lsr" | awk '$2=="HEAD"{print $1; exit}')
  defbr=$(printf '%s\n' "$lsr" | awk '$1=="ref:"{sub("refs/heads/","",$2); print $2; exit}')
  [ -n "$head_sha" ] || { printf '%s\tNO-HEAD\t-\t-\t-\t-\t-\t-\n' "$slug" >> "$TSV"; continue; }

  # --- blobless clone, no checkout: the whole path list, none of the bytes --------------
  wt="$OUT/clones/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$wt"
  timeout 180 git clone --filter=blob:none --no-checkout --depth 1 "$url" "$wt" >/dev/null 2>&1 </dev/null || {
    printf '%s\t%s\t%s\tCLONE-FAILED\t-\t-\t-\t-\n' "$slug" "$head_sha" "${defbr:--}" >> "$TSV"; continue; }

  # --- EVERY grant path, bundled copies excluded (p442) --------------------------------
  mapfile -t allpaths < <(git -C "$wt" ls-tree -r --name-only HEAD 2>/dev/null)
  grants=()
  for p in "${allpaths[@]}"; do
    is_bundled "$p" && continue
    is_licence_path "$p" && grants+=("$p")
  done
  n=${#grants[@]}

  if [ "$n" -eq 0 ]; then
    printf '%s\t%s\t%s\t0\tNO-GRANT-PATH\t-\t-\tNO-PAYLOAD\n' "$slug" "$head_sha" "${defbr:--}" >> "$TSV"
  else
    for p in "${grants[@]}"; do
      safe=$(printf '%s__%s' "$(printf '%s' "$slug" | tr '/' '_')" "$(printf '%s' "$p" | tr '/' '_')")
      f="$OUT/payloads/$safe"
      git -C "$wt" show "HEAD:$p" > "$f" 2>/dev/null || { printf '%s\t%s\t%s\t%s\t%s\tFETCH-FAILED\t-\t-\n' "$slug" "$head_sha" "${defbr:--}" "$n" "$p" >> "$TSV"; continue; }
      bytes=$("$LIB/measure" --size "$f")
      sha12=$("$LIB/measure" --sha "$f")
      fam=$("$LIB/measure" --family "$f")
      printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$head_sha" "${defbr:--}" "$n" "$p" "$bytes" "$sha12" "$fam" >> "$TSV"
    done
  fi

  # --- the README, kept for the Gap 443-C comparator ------------------------------------
  for rp in README.md README.rst README README.txt readme.md Readme.md README.markdown; do
    if git -C "$wt" cat-file -e "HEAD:$rp" 2>/dev/null; then
      git -C "$wt" show "HEAD:$rp" > "$OUT/payloads/$(printf '%s' "$slug" | tr '/' '_')__READMEFILE" 2>/dev/null
      printf '%s\t%s\n' "$slug" "$rp" >> "$OUT/readme-paths.tsv"
      break
    fi
  done

  # Writable disk is a fixed per-session allowance and a 321-slug sweep is the run that
  # finds the ceiling.  The payloads are the evidence; the clone is scaffolding.
  [ "${KEEP_CLONES:-0}" = "1" ] || rm -rf "$wt"
done 3< "$SLUGS"
# 🔴 THE ASSERTION THIS INSTRUMENT SHIPPED WITHOUT, and the omission cost a whole sweep.
#
# First run over 321 shelf slugs processed NINE and exited 0.  Cause: `git` inside a
# `while read` loop reads the loop's stdin, so `git ls-remote`/`git clone` ATE the slug
# file.  Fixed above (FD 3 + `</dev/null`), but the reason it went unnoticed for a whole
# sweep is that nothing compared the input count to the output count.
#
# 🔵 `lib/measure` exists because "a pass cannot mistake a silent failure for a measurement
# of zero".  This loop reintroduced exactly that, one level up: the MEASUREMENTS were all
# sound and the POPULATION was silently 3% of what was asked for.  A guarantee at the cell
# level is not a guarantee at the sweep level.
want=$(grep -cvE '^[[:space:]]*(#|$)' "$SLUGS")
got=$(tail -n +2 "$TSV" | cut -f1 | sort -u | wc -l)
echo "wrote $TSV  (slugs asked: $want, slugs reported: $got)"
if [ "$want" -ne "$got" ]; then
  echo "INCOMPLETE SWEEP: asked $want, reported $got" >&2
  exit 3
fi
