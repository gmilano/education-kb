#!/usr/bin/env bash
# gap_reqname.sh — sizes the blind spot this pass found in its OWN inherited
# classifier, rather than reporting it as an anecdote.
#
# P114-K  `*_requirements.txt` IS INVISIBLE TO P112-A, AND THE ERROR IS IN THE
#   DIRECTION THAT MATTERS. P112-A matches a Python requirement file on an
#   ANCHORED basename: `^requirements([-_.]<suffix>)?\.txt$`. That is the
#   right call against `docs/requirements.rst`, which is prose about a
#   curriculum and is on this shelf. But it does not match the other half of
#   the convention -- `dev_requirements.txt`, `system_requirements.txt`,
#   `base-requirements.txt` -- and those are requirement files too.
#
#   p114 found this while VERIFYING its own Submitty row by hand. Submitty
#   carries four requirement files; the classifier sees one. The three it
#   cannot see live in `.setup/pip/` and the first of them is pinned
#   throughout (`ruff==0.16.8`, `sqlalchemy==2.0.52`).
#
#   The error direction: an unseen requirement file can only cost a row
#   COVERAGE it has earned, never grant coverage it has not. So every reach
#   figure p114 publishes is, on this axis, a LOWER bound -- the opposite
#   direction from P114-B's generosity, which is why both are stated and
#   neither is quietly netted against the other.
#
# This probe makes NO verdict and changes NO published row. It counts, per
# repository, the paths the anchored rule misses, so the next pass can decide
# the rule change against a measured cost instead of a guess.
#
# Output TSV: slug rc seen_by_p114 missed missed_paths
set -uo pipefail
cd "$(dirname "$0")"
list="${1:-addresses.txt}"
workroot="${P114K_WORK:-${TMPDIR:-/tmp}/p114kwork}"
BASE="${P114_BASE:-https://github.com}"
mkdir -p "$workroot"
printf 'slug\trc\tseen_by_p114\tmissed\tmissed_paths\n'
while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac
  d="$workroot/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$d"; mkdir -p "$d"; git init -q --bare "$d" 2>/dev/null
  case "$slug" in *://*) url="$slug" ;; *) url="$BASE/$slug" ;; esac
  git --git-dir="$d" remote add origin "$url" 2>/dev/null
  if ! git --git-dir="$d" fetch -q --depth=1 --filter=blob:none origin HEAD 2>/dev/null; then
    if ! git --git-dir="$d" fetch -q --depth=1 origin HEAD 2>/dev/null; then
      printf '%s\t1\t\t\t\n' "$slug"; rm -rf "$d"; continue   # P1040
    fi
  fi
  git --git-dir="$d" ls-tree -r --name-only FETCH_HEAD 2>/dev/null \
  | awk -v slug="$slug" '
      # the vendor/residue strip, so upstream trees never inflate either count
      tolower($0) ~ /(^|\/)(node_modules|vendor|bower_components|third_party|\.venv|venv|site-packages|\.tox)\// { next }
      tolower($0) ~ /\.egg-info\// { next }
      { n = split($0, a, "/"); b = tolower(a[n]) }
      # what P112-A / P114 already see
      b ~ /^requirements([-_.][a-z0-9._-]+)?\.txt$/ { seen++; next }
      # the other half of the convention: <something>_requirements.txt
      b ~ /requirements([-_.][a-z0-9._-]+)?\.txt$/ {
        missed++
        if (length(paths) < 300) paths = (paths == "" ? $0 : paths ";" $0)
      }
      END { printf "%s\t0\t%d\t%d\t%s\n", slug, seen+0, missed+0, (paths=="" ? "-" : paths) }'
  rm -rf "$d"
done < "$list"
