#!/usr/bin/env bash
# p609 — 607-C's named fix: reject a non-repository AT EXTRACTION TIME, not at promotion time.
# 603-A / 606-F / 607-C are one defect in the shared {owner}/{repo} extraction step.
# Two stages: (1) SHAPE, offline and free; (2) EXISTENCE, the 606-E probe, only for shape-passers.
# Usage: p609-address-rejector.sh [--shape-only] slug...
# TSV out: address  stage  verdict  reason
set -u
SHAPE_ONLY=0; [ "${1:-}" = "--shape-only" ] && { SHAPE_ONLY=1; shift; }

# first segments that are never a GitHub owner in this base's artifacts
BASE_DIRS='evidence|ingest|agents|repos|intel|verticals|compose|archive|scratchpad|docs|raw|assets|figures|scripts|tools|configs|examples|data|code|results'
# github.com path prefixes and git refs that get mis-extracted as owners
NOT_OWNER='main|master|develop|blob|tree|topics|orgs|sponsors|settings|features|about|pricing|login|join|search|trending|collections|events|marketplace|apps|users|new|notifications|explore|readme|license'
# second segments that are a file or ref fragment, never a repo name
NOT_REPO='license|licence|license\.md|license\.txt|readme|readme\.md|copying|main|master|head'

printf 'address\tstage\tverdict\treason\n'
for a in "$@"; do
  v=PASS; r=''; st=SHAPE
  segs=$(printf '%s' "$a" | awk -F/ '{print NF}')
  own=${a%%/*}; rep=${a#*/}
  if   [ "$segs" -ne 2 ];                                       then v=REJECT; r="not 2 path segments ($segs)"
  elif printf '%s' "$own" | grep -qiE "^($BASE_DIRS)$";          then v=REJECT; r="owner is a repository directory of this base"
  elif printf '%s' "$own" | grep -qiE "^($NOT_OWNER)$";          then v=REJECT; r="owner is a git ref or github.com path prefix"
  elif printf '%s' "$rep" | grep -qiE "^($NOT_REPO)$";           then v=REJECT; r="repo segment is a file or ref fragment"
  elif ! printf '%s' "$own" | grep -qE '^[A-Za-z0-9]([A-Za-z0-9-]{0,38})$'; then v=REJECT; r="owner violates GitHub owner charset"
  elif ! printf '%s' "$rep" | grep -qE '^[A-Za-z0-9._-]{1,100}$';then v=REJECT; r="repo violates GitHub repo charset"
  fi
  if [ "$v" = PASS ] && [ "$SHAPE_ONLY" = 0 ]; then
    st=EXISTENCE
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 "https://github.com/$a/info/refs?service=git-upload-pack")
    case "$code" in
      200) v=PASS;   r="606-E probe 200" ;;
      401) v=REJECT; r="606-E probe 401 — address absent" ;;
      *)   v=INDETERMINATE; r="606-E probe returned $code — not a verdict" ;;
    esac
  fi
  printf '%s\t%s\t%s\t%s\n' "$a" "$st" "$v" "$r"
done
