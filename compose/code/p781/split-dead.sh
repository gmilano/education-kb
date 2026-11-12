# p781 two-channel death classifier, extending T810.
# search `repo:` miss + ls-remote OK   -> RENAMED-or-UNINDEXED (content alive, address stale)
# search `repo:` miss + ls-remote FAIL -> DELETED-or-PRIVATE   (truly gone)
# git follows GitHub's rename redirect, which is exactly why it separates the two.
while read -r slug; do
  [ -z "$slug" ] && continue
  if timeout 25 git ls-remote --symref "https://github.com/$slug" HEAD >/dev/null 2>&1; then
    echo -e "RENAMED-OR-UNINDEXED\t$slug"
  else
    echo -e "DELETED-OR-PRIVATE\t$slug"
  fi
done < /tmp/p781/dead-genuine.txt
echo "SPLIT-DONE"
