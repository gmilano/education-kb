#!/bin/sh
# p141-contact-migration — ACTION DB: when did `oscm@edx.org` and `oscm@openedx.org` diverge,
# and was either touched after the Axim rename?
#
# For each repository and each address: the files carrying it at HEAD, and every commit that
# added or removed the string (`git log -S`, the pickaxe), oldest last.
#
# Usage: ./trace_contact.sh /path/to/clone ...
for repo in "$@"; do
  echo "######## $repo  (HEAD $(git -C "$repo" log -1 --format='%h %cI'))"
  for addr in oscm@edx.org oscm@openedx.org; do
    echo "--- [$addr]"
    echo "    at HEAD in: $(git -C "$repo" grep -l "$addr" HEAD 2>/dev/null | sed 's/^HEAD://' | tr '\n' ' ')"
    git -C "$repo" log --format='    %cI %h %an <%ae> | %s' -S"$addr" --all
  done
done
