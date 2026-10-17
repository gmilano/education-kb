#!/bin/bash
# p276 enumeration: ls-remote positive control -> blobless no-checkout clone -> ls-tree -r
# Plain git only. Nothing from any cloned tree is ever executed (--no-checkout: no worktree).
OUT=/tmp/claude-0/-home-user-globant-kb/82d92b6c-5932-59e6-97db-f80aa200d3b6/scratchpad/trees
mkdir -p "$OUT"
while read -r slug; do
  [ -z "$slug" ] && continue
  safe=$(echo "$slug" | tr '/' '__')
  sha=$(timeout 60 git ls-remote "https://github.com/$slug" HEAD 2>/dev/null | awk '{print $1}' | head -1)
  if [ -z "$sha" ]; then
    echo -e "$slug\tDOES_NOT_RESOLVE\t-\t0\tFAIL"
    continue
  fi
  d="$OUT/$safe"
  rm -rf "$d"
  if ! timeout 180 git clone --depth 1 --filter=blob:none --no-checkout \
        "https://github.com/$slug" "$d" >/dev/null 2>&1; then
    echo -e "$slug\tRESOLVES\t$sha\t0\tCLONE_FAIL"
    continue
  fi
  all=$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null)
  n=$(printf '%s\n' "$all" | grep -c . )
  printf '%s\n' "$all" > "$OUT/$safe.paths"
  lic=$(printf '%s\n' "$all" | grep -iE '(^|/)(licen[cs]e|copying|notice|unlicense|eupl|copyright)' \
        | grep -viE '(^|/)(vendor|node_modules|custompackages|libraries|third_party|thirdparty|precompiled-icons|plugins|samples)(/|$)' \
        | grep -viE '\.(php|java|vue|py|js|ts|jsx|tsx|go|rb|cs|png|svg|jpg|gif)$' | paste -sd, -)
  [ -z "$lic" ] && lic="NONE_IN_TREE"
  echo -e "$slug\tRESOLVES\t$sha\t$n\t$lic"
done
