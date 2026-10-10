#!/usr/bin/env bash
# busfactor.sh — contributor-CONCENTRATION census over this KB's shelf addresses.
#
# WHY THIS AXIS. Three passes have measured the shelf's maintenance: p107 tag
# COUNT (how much ref traffic), p108 release IDENTITY (can I pin it), p109
# commit RECENCY (is it alive). None of them can answer the question an
# engagement actually asks next: if the person keeping it alive stops, does it
# die. A repo can be fresh TODAY and be one unpaid human. p109 ranked such a
# row 🟢 fresh and said nothing was wrong.
#
# CHANNEL. Anonymous git lane only, re-probed live at pass 110:
#   git ls-remote / git fetch          rc=0
#   raw.githubusercontent.com          200
#   api.github.com                     403   (P107-A, session scoping)
# So /contributors cannot be read. Authorship comes from the commit objects
# themselves: a depth-limited, blob-filtered fetch, then `git log`.
#
# ---------------------------------------------------------------------------
# FOUR DISCIPLINES, each of which an earlier draft of this script got wrong.
#
# P110-A  MERGE COMMITS ARE EXCLUDED (`--no-merges`).
#   On a PR-merge workflow the maintainer authors every merge commit. Counting
#   merges attributes one commit per PR to the maintainer and none to the
#   person who wrote it, so the HEALTHIEST repos — the ones with many outside
#   contributors arriving by PR — read as the most concentrated. The bias is
#   not noise; it points the wrong way and is strongest exactly where the
#   answer matters most.
#
# P110-B  AUTHOR IDENTITY, NOT COMMITTER (`%aE`, not `%cE`).
#   This INVERTS p109's choice, for a principled reason. p109 wanted to know
#   when history was written, so committer date was correct. This wants to
#   know WHO WROTE THE CODE. Under "Squash and merge" or "Rebase and merge"
#   GitHub rewrites the committer to the person who clicked the button, so
#   committer-based concentration is 1 for every squash-merge repo on earth
#   while author-based concentration is unchanged. Both figures are emitted
#   so the divergence is visible rather than assumed.
#
# P110-C  BOTS ARE NOT CONTRIBUTORS.
#   dependabot/renovate/weblate/transifex/github-actions commit at machine
#   rates. Left in, a bot becomes the "top author" and the repo reads as
#   concentrated-but-not-solo — the worst of both errors, because it hides a
#   solo human behind a robot. Bots are stripped before any arithmetic and
#   counted separately, so stripping them is auditable rather than silent.
#
# P110-D  THIS IS A WINDOW, NOT A HISTORY.
#   The fetch is depth-limited, so every figure describes a recent WINDOW of
#   history, not the project's life. And DEPTH is a GENERATION limit, not a
#   commit count: measured at pass 110, --depth=200 yielded 200 commits on
#   UniTime but 8 374 on moodle/moodle, because each generation of a
#   merge-heavy history can branch. So the windows are NOT comparable in
#   size, and commits_read is load-bearing output, not diagnostics. A repo with a broad
#   past and a solo present reads solo — which is the correct answer to the
#   engagement question, but is NOT the same claim as "only one person ever
#   worked on it". commits_read is emitted so a saturated window (== DEPTH)
#   can be told from a complete one (< DEPTH).
#
# P110-E  EMAIL IS THE KEY, NAME IS THE CROSS-CHECK.
#   Email is normalised to lower case (Git preserves case; the same human
#   commits as Name@host and name@host). Distinct NAMES are emitted beside
#   distinct emails: when names < emails, one human is using several
#   addresses and the email-based author count OVERSTATES the bench.
#
# P1040  AN UNREAD ROW IS NEVER ZERO. rc!=0 emits UNREAD and empty metrics.
#   A fetch failure must never be arithmetically indistinguishable from a
#   genuinely solo repo.
# ---------------------------------------------------------------------------
#
# Output TSV:
#   slug rc commits_read bots_stripped authors_email authors_name \
#   top_author_share bus_factor committer_bus_factor band
set -uo pipefail
cd "$(dirname "$0")"

list="${1:-addresses.txt}"
DEPTH="${P110_DEPTH:-200}"
# P110_MERGES=1 INCLUDES merge commits. It exists only so the P110-A bias can
# be MEASURED on this shelf rather than asserted from first principles; it is
# never the mode a reported figure comes from.
if [ "${P110_MERGES:-0}" = 1 ]; then MERGEFLAG=""; else MERGEFLAG="--no-merges"; fi
# P110_BOTS_KEEP=1 KEEPS bot commits. Like P110_MERGES it exists only so the
# P110-C distortion can be MEASURED on this shelf, never to report a figure.
KEEPBOTS="${P110_BOTS_KEEP:-0}"
workroot="${P110_WORK:-${TMPDIR:-/tmp}/p110work}"
# BASE lets the test suite point the same code at real git repos served over
# file:// — the script is never given a mock, only a different transport.
BASE="${P110_BASE:-https://github.com}"

# P110-C. Matched against the lower-cased author email AND name.
is_bot() {
  local s="$1"
  case "$s" in
    *"[bot]"*|*dependabot*|*renovate*|*greenkeeper*|*weblate*|*transifex*|\
    *crowdin*|*"github-actions"*|*"actions-user"*|*snyk-bot*|*imgbot*|\
    *allcontributors*|*pre-commit-ci*|*codecov*|*semantic-release*) return 0 ;;
    # P110-F: ONLY the two machine forms. A bare users.noreply.github.com
    # address is the DEFAULT privacy email of a real human.
    "noreply@github.com"|"web-flow@users.noreply.github.com") return 0 ;;
  esac
  return 1
}

band() { # bus_factor -> band   ("" when unread)
  case "$1" in
    1) echo solo ;;
    2) echo pair ;;
    3|4|5) echo small ;;
    *) echo broad ;;
  esac
}

printf 'slug\trc\tcommits_read\tbots_stripped\tauthors_email\tauthors_name\ttop_author_share\tbus_factor\tcommitter_bus_factor\tband\n'

while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac

  d="$workroot/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$d"; mkdir -p "$d"
  git init -q --bare "$d" 2>/dev/null

  url="$slug"
  case "$slug" in
    *://*) url="$slug" ;;
    *)     url="$BASE/$slug" ;;
  esac

  if ! git --git-dir="$d" fetch -q --depth="$DEPTH" --filter=blob:none \
        "$url" HEAD 2>/dev/null; then
    # One retry without the partial-clone filter: a few servers refuse it.
    if ! git --git-dir="$d" fetch -q --depth="$DEPTH" "$url" HEAD 2>/dev/null; then
      printf '%s\t1\t\t\t\t\t\t\t\tUNREAD\n' "$slug"
      rm -rf "$d"
      continue
    fi
  fi

  # P110-A --no-merges; P110-B author AND committer email on each line.
  log=$(git --git-dir="$d" log $MERGEFLAG \
          --format='%aE%x09%aN%x09%cE' FETCH_HEAD 2>/dev/null)
  rm -rf "$d"

  if [ -z "$log" ]; then
    # Reachable but no non-merge commits in the window: readable, not solo.
    printf '%s\t0\t0\t0\t0\t0\t\t\t\tEMPTY\n' "$slug"
    continue
  fi

  printf '%s\n' "$log" | awk -F'\t' -v slug="$slug" -v keepbots="$KEEPBOTS" '
    function lc(s) { return tolower(s) }
    # mirror of is_bot(), applied to email and name
    function bot(s,   i) {
      split("[bot] dependabot renovate greenkeeper weblate transifex crowdin github-actions actions-user snyk-bot imgbot allcontributors pre-commit-ci codecov semantic-release", P, " ")
      for (i in P) if (index(s, P[i]) > 0) return 1
      # P110-F. Exact machine addresses only. NOT a /noreply@github.com$/
      # regex: "<id>+<user>@users.noreply.github.com" is the default privacy
      # email of a real contributor, and that regex deletes real humans --
      # silently, and hardest on privacy-conscious maintainers.
      if (s == "noreply@github.com") return 1
      if (s == "web-flow@users.noreply.github.com") return 1
      return 0
    }
    {
      ae = lc($1); an = lc($2); ce = lc($3)
      if (keepbots != "1" && (bot(ae) || bot(an))) { bots++; next }
      total++
      acount[ae]++
      names[an] = 1
      ccount[ce]++
    }
    END {
      if (total == 0) {
        # every commit in the window was a bot: readable, but no human signal
        printf "%s\t0\t0\t%d\t0\t0\t\t\t\tBOTONLY\n", slug, bots+0
        exit
      }
      # distinct authors
      na = 0; for (a in acount) na++
      nn = 0; for (n in names)  nn++

      # top share, as an integer percentage
      top = 0; for (a in acount) if (acount[a] > top) top = acount[a]
      share = int(top * 100 / total + 0.5)

      # bus factor: fewest authors whose commits exceed 50% of the window.
      # Selection sort over the counts (author sets here are small).
      m = 0; for (a in acount) { m++; v[m] = acount[a] }
      for (i = 1; i <= m; i++)
        for (j = i + 1; j <= m; j++)
          if (v[j] > v[i]) { t = v[i]; v[i] = v[j]; v[j] = t }
      acc = 0; bf = 0
      for (i = 1; i <= m; i++) { acc += v[i]; bf = i; if (acc * 2 > total) break }

      # same arithmetic on the COMMITTER key (P110-B), for the divergence
      cm = 0; for (c in ccount) { cm++; w[cm] = ccount[c] }
      for (i = 1; i <= cm; i++)
        for (j = i + 1; j <= cm; j++)
          if (w[j] > w[i]) { t = w[i]; w[i] = w[j]; w[j] = t }
      cacc = 0; cbf = 0
      for (i = 1; i <= cm; i++) { cacc += w[i]; cbf = i; if (cacc * 2 > total) break }

      bnd = (bf == 1) ? "solo" : (bf == 2) ? "pair" : (bf <= 5) ? "small" : "broad"
      printf "%s\t0\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%s\n", \
        slug, total, bots+0, na, nn, share, bf, cbf, bnd
    }'
done < "$list"
