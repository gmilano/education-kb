# SHARED PAYLOAD PROBE — source this, do not rewrite it.
#
# Pass 15 of 2026-10-06 (the SIS/MIS tier).  This file exists because `lib/README.md` states
# the rule and the rule was broken anyway, for the second recorded time:
#
#   * Pass 77 rewrote the FAMILY classifier from scratch and re-imported P171 (GPL-3.0 §13
#     titled "Use with the GNU Affero General Public License" -> every GPL-3.0 read as AGPL).
#     `license_family.sh` was the answer.
#   * Pass 15 of 2026-10-06 rewrote the PROBE LOOP from scratch, did not source
#     `license_family.sh`, and reported four GPL-3.0/AGPL-3.0 payloads as Creative
#     Commons/NonCommercial -- because GPL-3.0 §6 contains the word "noncommercially", a
#     defect THIS BASE had already measured (line 259 of the payload) and already fixed.
#
# 🔵 The diagnosis that produced this file: the family question had a control and the
# SURROUNDING LOOP did not, so every pass still wrote `curl` + `grep` by hand and, while
# writing it, re-chose the classifier too.  A control nobody has to assemble is the only
# kind that gets used.  THIS FILE IS THE LOOP.
#
#   probe_repo <owner/repo> [branch]
#     -> TSV: repo <TAB> branch <TAB> filename <TAB> bytes <TAB> family <TAB> holder
#        filename = NO-PAYLOAD when nothing is found.
#
# Three traps it closes, each measured on real repositories in pass 15 and NOT hypothetical:
#
#   1. DEFAULT BRANCH IS NOT `main`/`master`.  Measured: GibbonEdu/core -> `v31.0.00`,
#      portabilis/i-educar -> `2.12`, francoisjacquet/rosariosis -> `mobile` (3 of the 5
#      highest-starred open SIS platforms in existence).  A hardcoded branch writes all
#      three down as ungranted.  Resolved with `ls-remote --symref`, never assumed.
#   2. THE LICENCE CAN LIVE IN A SUBDIRECTORY, MIXED-CASE.  Measured: OS4ED/openSIS-Classic
#      keeps GPL-2.0 at `docs/License.txt` (17,286 B, with a BOM).  No filename ladder in
#      this base would have found it -- the README's own licence LINK did, in one request.
#      So the README link is tried BEFORE the long ladder, not after.
#   3. BRITISH SPELLING.  Measured: AkizumiFox/NTU-COOL-Assignment-Status-Viewer ships
#      `LICENCE`.  Pass 14 priced the full 20-name case ladder at 0 payouts in 98 repos and
#      told the next pass not to re-buy it; `LICENCE` is one request and paid 1 in 44.
#      The short list below is that finding, not a guess.
#
# ⚠️ What this file deliberately does NOT do: decide whether a component may be USED.  A
# payload answers the COPYRIGHT question only.  The ACCESS question -- may we call this
# system? -- is P26 (the access-rights gate), lives in a third party's Terms of Use, and is
# invisible to every probe in this directory.  Pass 15 found an MIT component that is
# unshippable for exactly that reason.

_PROBE_LIB_DIR="${_PROBE_LIB_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
# Pass 74 of 2026-10-09: `payload_measure.sh` carries the sizing primitive, the word-bounded
# counter and the delegated classifier (it sources `license_family.sh` itself, so `P171` is
# still inherited and still not re-implemented).  THIS FILE KEEPS ONLY THE FETCH.
#
# 🔴 Why: this file committed `P834` in its own pass-15 code — `body=$(_raw …)` strips the
# payload's trailing newline run, so `printf '%s' "$body" | wc -c` was low by that run on
# EVERY repository this probe has ever measured.  `P834` was written about hand-rolled
# probes; the shared instrument the rule points at had the same defect.  Sizing now goes
# through `size_of_file`, which is byte-exact because it never round-trips through a
# variable, and is asserted both ways in `p837-payload-measure/test_measure.sh` (**27/27**).
. "$_PROBE_LIB_DIR/payload_measure.sh"

# Ordered shortest-first: the names that actually paid out in this base's censuses.
PROBE_NAMES="${PROBE_NAMES:-LICENSE LICENSE.md LICENSE.txt LICENCE COPYING COPYING.txt COPYING.TXT}"

# 🔴 p337 — THE SHORT LADDER'S EMPIRICAL BASIS WAS REFUTED, AND THIS FILE'S OWN HEADER
# CARRIES THE REFUTED CLAIM.  Trap 3 above records pass 14 pricing "the full 20-name case
# ladder at 0 payouts in 98 repos" and telling the next pass not to re-buy it.  p336 bought
# one rung of it by hand and it paid immediately: `kitschpatrol/yanki` ships
# `license.txt` — LOWERCASE, 1 071 B, `MIT License`, a real 474-commit project — and this
# ladder, being all-uppercase on every stem, had already published it as
# `REFUSED-UNGRANTED` *"no licence file on 6 paths"*.  A 0-payout price measured once over
# 98 repositories is a PRIOR, not a proof, and a single counterexample refutes the
# generalisation it was used to justify.
#
# 🟢 So the ladder is now GENERATED and case-varied on BOTH halves (stem x extension x
# casing) instead of being a hand-typed list of uppercase spellings.  The economics that
# motivated the short list are preserved exactly, because the loop in `probe_repo` RETURNS
# ON THE FIRST HIT:
#
#   * a repository with a conventional `LICENSE` still costs ONE request — the fast rungs
#     above are emitted first, in their measured order;
#   * the full cross product is only ever walked for a repository that is about to be
#     written down as having NO GRANT, which is precisely the verdict `ACTION ZL` (p336)
#     forbids publishing from a ladder `gate-ladder-case` types `CASE-UNVARIED`.
#
# 🔵 The cost is therefore paid only where the error is expensive, and the rung that
# refuted the prior (`license.txt`) is reachable for every stem this base probes.
# 🔵 Scope held to the vocabulary `ACTION ZL` actually names, not to the widest cross
# product expressible: both licence spellings over three casings and the extension set
# this corpus has been measured to carry, plus the fixed `copying` / public-domain /
# `MIT-LICENSE` rungs that have no stem to vary.  That is ~36 spellings, every one of
# which is a real shape seen on GitHub — NOT the 20-name ladder pass 14 priced, and not a
# combinatorial blow-up bought for its own sake.
PROBE_STEMS="${PROBE_STEMS:-license licence}"
PROBE_FIXED="${PROBE_FIXED:-COPYING COPYING.txt COPYING.TXT copying Copying UNLICENSE UNLICENCE unlicense LICENSE-MIT MIT-LICENSE MIT-LICENSE.txt mit-license.md}"

# Emit the ladder: the measured-fast rungs first, then the case-varied cross product, then
# the fixed rungs.  One pipeline, so `awk` de-duplicates the WHOLE ladder — the fast rungs
# keep their measured position and no spelling is ever requested twice.
#
# 🔴 First draft of this function piped only the `for` loop, leaving the fast rungs
# OUTSIDE the de-duplicator: the ladder came back 82 rungs with all 7 fast spellings
# duplicated.  Caught by running it, not by reading it.
#
# 🔵 TWO THINGS BELOW ARE LOAD-BEARING FOR THE AUDIT THAT CERTIFIES THIS LADDER, and both
# are stated here rather than inline so the generator's own lines stay ADJACENT:
#   1. The extension list is spelled LITERALLY in its `for`, in both cases, never behind a
#      `$VAR` — `p283`'s shell arm reads the `for` list itself (`_SH_FOR_LIST` +
#      `ext_varies`), so a list arriving through a variable is invisible to it.
#   2. The stem-casing derivation (`tr 'a-z' 'A-Z'`) sits WITHIN 8 LINES of that list,
#      which is what `p283`'s p337 arm requires: proximity, not presence, exactly as in
#      `_near`'s docstring.  🔴 An earlier draft of this comment sat BETWEEN the two and
#      pushed them 9 lines apart, and the audit correctly went on typing this file
#      `CASE-UNVARIED` while it provably walked 42 case-varied rungs.  Prose does not get
#      to separate the two halves of a generator it is describing.
# `:` is the empty-extension rung.
probe_ladder() {
  {
    printf '%s\n' $PROBE_NAMES
    local stem ext s
    for stem in $PROBE_STEMS; do
      # 🔴 p337: the first draft derived these casings with `upper=$(printf … | tr …)`.
      # `p253-captured-body-census` graded this file **BODY-ONLY** for it and the offline
      # suite went red — correctly: `$( )` around a content producer is a CAPTURED BODY by
      # its own `capture_shape`, and the census cannot know the capture holds a FILENAME
      # STEM rather than a payload.  🟢 Bash's own case expansions need no subshell at all,
      # so the capture is not justified and not merely annotated away: `${stem^^}` and
      # `${stem^}` remove two forks per stem, keep the census CLEAN, and are the idiom
      # `p283`'s `_SH_STEM_VARY` already reads.
      for s in "$stem" "${stem^^}" "${stem^}"; do
        for ext in : .md .txt .MD .TXT; do
          [ "$ext" = ":" ] && ext=""
          printf '%s%s\n' "$s" "$ext"
        done
      done
    done
    printf '%s\n' $PROBE_FIXED
  } | awk '!seen[$0]++'
}

_raw() { curl -sS --max-time "${PROBE_TIMEOUT:-25}" "https://raw.githubusercontent.com/$1/$2/$3" 2>/dev/null; }

# Resolve the REAL default branch.  Empty output means the repository does not resolve at
# all, which is a different verdict from "no payload" and must not be conflated with it.
probe_default_branch() {
  timeout "${PROBE_TIMEOUT:-25}" git ls-remote --symref "https://github.com/$1" HEAD 2>/dev/null \
    | sed -n 's|^ref: refs/heads/\(.*\)\tHEAD$|\1|p' | head -1
}

# Pull a licence path out of the README's own link.
#
# Two real shapes, and v1 of this function only handled the first:
#   [LICENSE](docs/License.txt)                      <- the word is in the LINK TEXT
#   ...can be found [here](https://github.com/OS4ED/openSIS-Classic/blob/master/docs/License.txt)
#                                                    <- the word is in the URL, text is "here"
# openSIS-Classic -- the repository this trap was discovered on -- is the SECOND shape, so
# matching only on link text fails the very case that motivated the function.  Match either
# side, and normalise a github blob/raw URL back to a repo-relative path.
_readme_license_path() {
  _raw "$1" "$2" README.md \
    | grep -oE '\[[^]]*\]\([^)]+\)' \
    | grep -iE 'licen[sc]e|copying' \
    | sed -E 's/.*\(([^)]+)\).*/\1/' \
    | sed -E 's#^https?://(www\.)?github\.com/[^/]+/[^/]+/(blob|raw)/[^/]+/##' \
    | sed -E 's#^https?://raw\.githubusercontent\.com/[^/]+/[^/]+/[^/]+/##' \
    | sed -E 's/^\.?\///' \
    | grep -viE '^https?://|^#|^mailto:' | head -1
}

# Fetch one candidate path to a FILE, never to a variable, and emit the row from the file.
# 🔵 This is the whole `P834` fix: the payload's bytes are counted where they landed.  Prints
# nothing and returns 1 when the candidate is absent, so the caller keeps walking the ladder.
_row_from_fetch() { # _row_from_fetch <repo> <branch> <path> <filename-for-the-row>
  local repo="$1" br="$2" path="$3" label="$4" tmp rc=1
  tmp=$(mktemp) || return 1
  _raw "$repo" "$br" "$path" > "$tmp"
  if [ -s "$tmp" ] && ! head -1 "$tmp" | grep -q '^404: Not Found$'; then
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$br" "$label" \
      "$(size_of_file "$tmp")" "$(family_of_file "$tmp")" "$(holder_of_file "$tmp")"
    rc=0
  fi
  rm -f "$tmp"
  return "$rc"
}

probe_repo() {
  local repo="$1" br="$2" fn p
  [ -z "$br" ] && br=$(probe_default_branch "$repo")
  if [ -z "$br" ]; then
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "-" "UNRESOLVED" "0" "UNRESOLVED" "-"; return
  fi
  # p337: walks the fast rungs first and returns on the first hit, so a conventional
  # `LICENSE` still costs one request; the case-varied tail is reached only on the path to
  # an absence verdict (`ACTION ZL`).
  for fn in $(probe_ladder); do
    _row_from_fetch "$repo" "$br" "$fn" "$fn" && return
  done
  # Trap 2: ask the README where it says the licence is, before giving up.
  p=$(_readme_license_path "$repo" "$br")
  if [ -n "$p" ]; then
    _row_from_fetch "$repo" "$br" "$p" "$p" && return
    # A README that POINTS at a licence file that is not there is its own verdict: the
    # maintainer believes they granted.  Measured: DMontgomery40/mcp-canvas-lms (103★) says
    # "MIT License - see [LICENSE] file" and ships no such file.  That is an upstream ASK,
    # not a refusal, and it must not be reported as a bare absence.
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$br" "DANGLING-README-LINK:$p" "0" "DECLARED-NOT-GRANTED" "-"; return
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$br" "NO-PAYLOAD" "0" "NO-PAYLOAD" "-"
}
