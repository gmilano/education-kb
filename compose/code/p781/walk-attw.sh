set -o pipefail
D=/tmp/p781/attw-fresh
echo "CLONE START $(date -u +%H:%M:%S)"
if timeout 600 git clone --filter=blob:none --no-checkout --single-branch https://github.com/DFE-Digital/apply-for-teacher-training "$D" 2>&1 | tail -3; then
  cd "$D" || exit 9
  echo "DEFAULT_BRANCH=$(git rev-parse --abbrev-ref HEAD)"
  echo "COMMITS_TOTAL=$(git rev-list --count HEAD)"
  echo "COMMITS_SINCE_2026=$(git rev-list --count --since=2026-01-01 HEAD)"
  echo "--- licence events, default branch only (T813), since 2026-01-01 ---"
  timeout 420 git log --since=2026-01-01 --diff-filter=AMDR --name-status --date=short \
    --format="COMMIT%x09%h%x09%ad%x09%an%x09%s" -- \
    "*LICENSE*" "*LICENCE*" "*COPYING*" "*license*" "*licence*" "*copying*" 2>&1
  echo "WALK_EXIT=$?"
  echo "--- full history, licence events (bounded; report UNFINISHED not 0 per T814) ---"
  timeout 300 git log --diff-filter=AMDR --name-status --date=short \
    --format="COMMIT%x09%h%x09%ad%x09%an%x09%s" -- \
    "*LICENSE*" "*LICENCE*" "*COPYING*" 2>&1
  echo "FULL_WALK_EXIT=$?"
else
  echo "CLONE_FAILED_OR_TIMEOUT -- publish UNFINISHED, never 0 (T814)"
fi
echo "DONE $(date -u +%H:%M:%S)"
