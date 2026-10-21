#!/bin/bash
# `p349-payload-digest` — `ACTION ZZ-ad`'s instrument: THE THIRD IDENTITY QUESTION.
#
# p348 found two rows on the agent shelf that neither identity gate this base owns can
# see as one thing:
#
#   | question                                           | instrument            | the k12 pair |
#   | same ADDRESS, case-folded?                         | `gate-fold-identity`  | 🔴 blind     |
#   | same HEAD?                                         | `gate-identity-online`| 🔴 blind     |
#   | same PAYLOAD?                                      | 🔴 none — until this  | 🟢 catches   |
#
# `anthropics/k12-teacher-skills` and `learning-commons-org/agent-skills` are different
# owners, different HEADs, different layouts — and ship BYTE-IDENTICAL skill bodies.  The
# cost is a DENOMINATOR error that lands on the client: a studio told "there are two open
# K-12 teacher skill packs" has been told something false.
#
# 🔵 It also closes the hole `p349-name-collision` declares.  The name pre-filter cannot
# see a transfer that RENAMED the repository; a payload digest does not read the address
# at all, so a renamed transfer is still one payload.  Two instruments, opposite blind
# spots, and neither is a proof of absence alone.
#
#   payload_digest.sh <probes.tsv>   # cols: slug <TAB> path   (header line skipped)
#     -> TSV: slug  path  head  bytes  sha256_16  state
#
# States, kept distinct because an absent payload and an equal payload are not the same
# answer (`p244`'s absence states, applied to a digest):
#   OK           — fetched at the pin, digest printed
#   NO-PAYLOAD   — the path does not exist at the pin (404); digest column reads `-`
#   NO-PIN       — the address itself does not resolve
set -uo pipefail
IN="${1:?usage: payload_digest.sh <probes.tsv>}"
printf 'slug\tpath\thead\tbytes\tsha256_16\tstate\n'
tail -n +2 "$IN" | while IFS=$'\t' read -r slug path; do
  [ -z "${slug:-}" ] && continue
  case "$slug" in \#*) continue;; esac
  head_sha="$(timeout 45 git ls-remote "https://github.com/$slug" HEAD 2>/dev/null | awk 'NR==1{print substr($1,1,12)}')"
  if [ -z "$head_sha" ]; then
    printf '%s\t%s\tNO-PIN\t-\t-\tNO-PIN\n' "$slug" "$path"; continue
  fi
  body="$(mktemp)"
  code="$(curl -sS --max-time 40 -o "$body" -w '%{http_code}' \
          "https://raw.githubusercontent.com/$slug/$head_sha/$path" 2>/dev/null || echo 000)"
  if [ "$code" != "200" ]; then
    printf '%s\t%s\t%s\t-\t-\tNO-PAYLOAD(%s)\n' "$slug" "$path" "$head_sha" "$code"
    rm -f "$body"; continue
  fi
  printf '%s\t%s\t%s\t%s\t%s\tOK\n' "$slug" "$path" "$head_sha" \
    "$(wc -c < "$body" | tr -d ' ')" "$(sha256sum "$body" | cut -c1-16)"
  rm -f "$body"
done
