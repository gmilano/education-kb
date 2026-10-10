#!/usr/bin/env bash
# bind.sh -- PROVIDER-BINDING census over this KB's shelf addresses.
#
# WHY THIS AXIS, AND WHY NOW. Six passes have measured this shelf:
#   p107 tag COUNT              how much ref traffic
#   p108 release IDENTITY       can I pin it
#   p109 commit RECENCY         is it alive
#   p110 author CONCENTRATION   what happens if they stop
#   p111 verification SURFACE   can the tree tell me when I broke it
#   p112 dependency CLOSURE     does it resolve to the same bytes twice
#
# Every one of those six is a question about the REPOSITORY. None of them asks
# the question a regulated buyer asks first, and this KB has been ANSWERING it
# in prose for a hundred passes without ever deriving it: the EMEA pages sell
# sovereignty, the LATAM pages sell cost, and both rest on the claim that the
# shelf can be made to talk to a model the client controls. `OPENAI_API_KEY`
# appears in zero markdown files of this KB -- the claim has never once been
# read off a tree.
#
# So p113 asks: WHICH MODEL CAN THIS BE MADE TO TALK TO? It is the third axis
# read from the TREE (p111, p112) and the first one that is about EGRESS rather
# than about the repository's own hygiene. It is the axis that decides whether
# p112's `pinned` verdict means anything in Frankfurt or Sao Paulo: a perfectly
# reproducible dependency set that can only reach one hosted endpoint is
# reproducible and unusable.
#
# CHANNEL. Anonymous git lane only, re-probed live at pass 113:
#   git ls-remote / git fetch                 rc=0
#   raw.githubusercontent.com/<slug>/HEAD/..  200
#   api.github.com                            403   (P107-A, session scoping)
# Tree from a depth-1 blob-filtered fetch; selected bodies from one batched
# lazy blob fetch against the same promisor remote (the P111-H mechanism).
#
# ---------------------------------------------------------------------------
# DISCIPLINES. P113-A..D live in select.awk and P113-E..H in tokens.awk, each
# beside the code it governs. These four are properties of this driver.
#
# P113-I  THE ERROR DIRECTION IS STATED BEFORE THE FIGURES ARE. This reads
#   DECLARATIONS -- manifests, environment templates, compose files, Modelfiles
#   -- and not program text. A repository that drives Ollama over plain HTTP
#   with `requests` and declares nothing therefore reads `no-model` or
#   `hosted-only` when it is in fact local. So:
#     `local` and `broker` are LOWER BOUNDS. `hosted-only` is an UPPER BOUND.
#   That is the opposite direction from p111/p112, whose textual reads could
#   only ever flatter a row, and it is the alarmist direction P111-F warns
#   about -- so it is said here, in the code, before any number is published.
#   The two mitigations are in the instrument, not in the prose: compose files
#   are read (an `ollama` service is a declaration) and `Modelfile` is selected
#   on its NAME, since nothing but a local runtime ships one.
#
# P113-J  `no-model` IS A REAL VERDICT ON THIS SHELF AND NOT A MISS. This shelf
#   is half specifications, corpora, LMS platforms and classical-ML libraries;
#   p112 found 34 of 296 rows declaring no dependencies at all. A row that
#   binds to no model is correctly reported as binding to no model, and the
#   `prose` column shows when a README nonetheless talks about one -- which is
#   the interesting case and must not be hidden inside the verdict.
#
# P113-K  AN UNREAD ROW IS NEVER ZERO (P1040). rc!=0 emits UNREAD with empty
#   metrics, so a fetch failure can never be arithmetically confused with a
#   repository that genuinely declares no provider.
#
# P113-L  THE NO-BODY CONTROL IS PART OF THE PASS, NOT AN OPTION. P113_NO_BODY=1
#   runs the identical tree walk and skips every body read, so this pass's
#   contribution over a filename-only read is MEASURED on this shelf rather
#   than asserted. p112 established that discipline at P112-F; a figure
#   published without its control run is an opinion.
# ---------------------------------------------------------------------------
#
# VERDICT LADDER (one per row, worst to best, by the strongest form of model
# control the TREE declares):
#   UNREAD       fetch failed; no claim made
#   no-model     nothing in any declaration names a model (P113-J)
#   hosted-only  a hosted provider, no abstraction, no endpoint override ->
#                the model is somebody else's and changing it is a code change
#   override     a configurable endpoint -> can be pointed at a self-hosted
#                OpenAI-compatible gateway without touching the code
#   broker       a provider-abstraction layer -> substitutable by config
#                (an aggregator is substitutable and NOT egress-free, P113-H)
#   local        a local inference runtime is declared -> runs with no egress
#
# Output TSV:
#   slug rc files stripped selected capped read anom local broker override
#   hosted prose selfname verdict
set -uo pipefail
cd "$(dirname "$0")"

list="${1:-addresses.txt}"
workroot="${P113_WORK:-${TMPDIR:-/tmp}/p113work}"
# BASE lets the suite point this same code at real git repositories served over
# file:// -- the script is never handed a mock, only a different transport.
BASE="${P113_BASE:-https://github.com}"
NO_BODY="${P113_NO_BODY:-0}"        # P113-L
CAP="${P113_CAP:-800}"              # P113-D, and see the note below.
# P113-D IN PRACTICE, TWICE. The first full run of this shelf used a cap of 60
# and clipped NINE rows -- five of them `instructure/canvas-lms`,
# `moodle/moodle`, `sakaiproject/sakai`, `kuali/rice` and `leemonade/leemons`,
# i.e. exactly the platform tier a reader of this KB cares most about, each
# reporting `no-model` off a TRUNCATED read. Raised to 400, and TWO rows still
# clipped: canvas-lms and sakai, both still `no-model`, both still truncated.
# A cap that binds on the rows that matter is not a safeguard, it is a silent
# miss. So the selectable set was MEASURED instead of guessed -- canvas-lms 551,
# sakai 498, moodle 64 -- and the default is 800, above every row on this shelf,
# with the published run verified at `capped = 0` on all 296.

mkdir -p "$workroot"

printf 'slug\trc\tfiles\tstripped\tselected\tcapped\tread\tanom\tlocal\tbroker\toverride\thosted\tprose\tselfname\tverdict\n'

while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac

  d="$workroot/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$d" "$d.map" "$d.body"; mkdir -p "$d"
  git init -q --bare "$d" 2>/dev/null

  case "$slug" in
    *://*) url="$slug" ;;
    *)     url="$BASE/$slug" ;;
  esac

  # Promisor config FIRST, so the body stage has a remote to resolve against.
  git --git-dir="$d" remote add origin "$url" 2>/dev/null
  git --git-dir="$d" config remote.origin.promisor true
  git --git-dir="$d" config remote.origin.partialclonefilter blob:none

  if ! git --git-dir="$d" fetch -q --depth=1 --filter=blob:none origin HEAD 2>/dev/null; then
    # One retry without the filter: a few servers refuse partial clone. Blobs
    # then arrive eagerly, so the body stage still works, offline.
    if ! git --git-dir="$d" fetch -q --depth=1 origin HEAD 2>/dev/null; then
      printf '%s\t1\t\t\t\t\t\t\t\t\t\t\t\t\tUNREAD\n' "$slug"      # P113-K
      rm -rf "$d"
      continue
    fi
  fi

  tree=$(git --git-dir="$d" ls-tree -r FETCH_HEAD 2>/dev/null)
  if [ -z "$tree" ]; then
    printf '%s\t0\t0\t0\t0\t0\t0\t0\t-\t-\t-\t-\t-\t-\tno-model\n' "$slug"
    rm -rf "$d"
    continue
  fi

  sel=$(printf '%s\n' "$tree" | awk -v CAP="$CAP" -f select.awk)
  tally=$(printf '%s\n' "$sel" | sed -n 's/^#tally\t//p')
  files=$(printf '%s' "$tally" | cut -f1); stripped=$(printf '%s' "$tally" | cut -f2)
  selected=$(printf '%s' "$tally" | cut -f3); capped=$(printf '%s' "$tally" | cut -f4)
  printf '%s\n' "$sel" | grep -v '^#tally' > "$d.map"

  read=0; anom=0; loc='-'; brk='-'; ovr='-'; hos='-'; pro='-'; sfn='-'
  if [ "$selected" -gt 0 ] && [ "$NO_BODY" != 1 ]; then      # P113-L
    # One batched lazy fetch materialises every selected blob; bodies go to a
    # FILE and the classifier reads the FILE (P112-I: pipefail plus an
    # early-exiting reader inverts a signal).
    cut -f1 "$d.map" | timeout 240 git --git-dir="$d" cat-file --batch \
      > "$d.body" 2>/dev/null
    if [ -s "$d.body" ]; then
      out=$(awk -v map="$d.map" -v slug="$slug" -f tokens.awk < "$d.body")
      read=$(printf '%s' "$out" | cut -f1); anom=$(printf '%s' "$out" | cut -f2)
      loc=$(printf '%s' "$out"  | cut -f3); brk=$(printf '%s' "$out"  | cut -f4)
      ovr=$(printf '%s' "$out"  | cut -f5); hos=$(printf '%s' "$out"  | cut -f6)
      pro=$(printf '%s' "$out"  | cut -f7); sfn=$(printf '%s' "$out" | cut -f8)
    fi
  fi
  # P113-P  A FILENAME CAN BE THE DECLARATION. Nothing but a local runtime
  # ships a `Modelfile` -- it is Ollama's build recipe -- and its CONTENTS
  # (`FROM llama3`) carry no token the table could match. The suite caught this
  # as a `no-model` verdict on a repository whose whole purpose is local
  # inference. So the modelfile KIND is credited from the tree, before any body
  # is read, and it is the one signal on this axis that survives the no-body
  # control (P113-L).
  if grep -q "$(printf '\tmodelfile\t')" "$d.map" 2>/dev/null; then
    if [ "$loc" = '-' ]; then loc=modelfile
    else loc=$(printf '%s,modelfile' "$loc" | tr ',' '\n' | sort -u | paste -sd, -)
    fi
  fi
  rm -f "$d.map" "$d.body"; rm -rf "$d"

  if   [ "$loc" != '-' ]; then verdict=local
  elif [ "$brk" != '-' ]; then verdict=broker
  elif [ "$ovr" != '-' ]; then verdict=override
  elif [ "$hos" != '-' ]; then verdict=hosted-only
  else                         verdict=no-model          # P113-J
  fi

  printf '%s\t0\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$files" "$stripped" "$selected" "$capped" "$read" "$anom" \
    "$loc" "$brk" "$ovr" "$hos" "$pro" "$sfn" "$verdict"
done < "$list"
