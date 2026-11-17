#!/usr/bin/env bash
# p869 — 868-G5: re-ground the EXISTENCE predicate on the CLONE channel.
# Reads addresses on stdin, one per line. Two independent channels per address:
#   meta  : gh api search/repositories q=repo:<addr>  -> total_count, or the HTTP status
#   clone : git ls-remote https://github.com/<addr>   -> HEAD sha, or p293's cred-prompt
# p293 convention: a credential PROMPT is the private/deleted signature, not an error.
# Declared: the meta arm distinguishes a HARD 422 refusal from a SOFT total_count=0,
# because p868's census recorded both as one "unresolved" class and they are not the same.
set -u
printf 'address\tmeta\tclone_head\tclone_verdict\tverdict\n'
while IFS= read -r a; do
  [ -z "$a" ] && continue
  raw=$(gh api -X GET search/repositories -f q="repo:$a" --jq '.total_count' 2>&1)
  if   printf '%s' "$raw" | grep -q '"status":"422"'; then m="REFUSED-422"
  elif printf '%s' "$raw" | grep -qE '^[0-9]+$';      then m="$raw"
  else m="ERR"; fi
  out=$(GIT_TERMINAL_PROMPT=0 timeout 40 git ls-remote "https://github.com/$a" HEAD 2>&1)
  if   printf '%s' "$out" | grep -qE '^[0-9a-f]{40}'; then h=$(printf '%s' "$out"|head -1|cut -c1-12); cv="ALIVE"
  elif printf '%s' "$out" | grep -q 'could not read Username'; then h="cred-prompt"; cv="ABSENT-OR-PRIVATE"
  else h=$(printf '%s' "$out"|head -1|cut -c1-30); cv="INCONCLUSIVE"; fi
  if [ "$cv" = "ALIVE" ] && { [ "$m" = "REFUSED-422" ] || [ "$m" = "0" ]; }; then v="FALSE-ABSENT"
  elif [ "$cv" = "ALIVE" ] && [ "$m" = "1" ]; then v="AGREE-ALIVE"
  elif [ "$cv" = "ABSENT-OR-PRIVATE" ]; then v="AGREE-ABSENT"
  else v="INCONCLUSIVE"; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$a" "$m" "$h" "$cv" "$v"
done
