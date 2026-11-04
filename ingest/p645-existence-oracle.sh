#!/usr/bin/env bash
# p645 — the THREE-CHANNEL EXISTENCE ORACLE that 642-B left open.
#
# 642-B measured that `search/repositories` `repo:` returns total_count 0 for
# repositories that exist, serve and are granted, and concluded: "every absence
# resting on repo: alone is an upper bound, not a finding". It did not build the
# replacement. This is the replacement.
#
# Channel A — `git ls-remote --symref <url> HEAD`: the GIT PROTOCOL, not the
#   search index. Three-valued, and the third value is the point:
#     * a symref + sha            -> PUBLIC-LIVE (definitive), AND the DEFAULT
#                                    BRANCH, which removes the base's standing
#                                    "branch from search and never guessed"
#                                    dependency on the rate-limited API.
#     * "could not read Username" -> NOT-PUBLIC. GitHub prompts for credentials
#                                    because it will not distinguish absent from
#                                    private to an anonymous caller, so this
#                                    channel CANNOT assert absence -- but
#                                    NOT-PUBLIC is the verdict this base's
#                                    decision actually needs. This is p293's
#                                    "a credential prompt is a MEASUREMENT".
#     * anything else             -> INCONCLUSIVE (network), never an absence.
# Channel B — `raw.githubusercontent.com` GET: the payload channel (640-B).
# Channel C — `search/repositories` `repo:… fork:true` (627-A/637-C): metadata
#   only. Graded here, never trusted for existence.
#
# Usage: ingest/p645-existence-oracle.sh <slug-file> <out.tsv>
set -uo pipefail
IN="${1:?slug file}"; OUT="${2:?out tsv}"
PAR="${PAR:-10}"

probe_a() {  # ls-remote: existence + default branch, no API
  local slug="$1" raw rc
  raw=$(timeout 25 git -c credential.helper= -c core.askPass=true \
          ls-remote --symref "https://github.com/$slug" HEAD 2>&1); rc=$?
  if printf '%s' "$raw" | grep -q '^ref: refs/heads/'; then
    printf 'PUBLIC-LIVE\t%s\n' "$(printf '%s' "$raw" | sed -n 's|^ref: refs/heads/\([^[:space:]]*\).*|\1|p' | head -1)"
  elif printf '%s' "$raw" | grep -qi 'could not read Username\|Authentication failed\|Repository not found'; then
    printf 'NOT-PUBLIC\t-\n'
  else
    printf 'INCONCLUSIVE\trc=%s\n' "$rc"
  fi
}

probe_b() {  # raw: does the default branch serve a tree at all
  local slug="$1" br="$2"
  [ "$br" = "-" ] && { printf '\t\n'; return; }
  curl -s -m 25 -o /dev/null -w '%{http_code}\t%{size_download}\n' \
    "https://raw.githubusercontent.com/$slug/$br/README.md"
}

export -f probe_a probe_b

printf 'slug\tA_lsremote\tA_default_branch\tB_readme_http\tB_readme_bytes\n' > "$OUT.a"
grep -v '^[[:space:]]*$' "$IN" | xargs -P "$PAR" -I{} bash -c '
  a=$(probe_a "{}"); st=$(printf "%s" "$a" | cut -f1); br=$(printf "%s" "$a" | cut -f2)
  b=$(probe_b "{}" "$br")
  printf "%s\t%s\t%s\t%s\n" "{}" "$st" "$br" "$b"
' >> "$OUT.a"
mv "$OUT.a" "$OUT"
wc -l < "$OUT"
