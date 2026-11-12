# p780-E: licence-add commit read on a SECOND estate (openfun, France) to test
# T815 (grant arrives with migration/creation) and T816 (filename form clusters by committer).
# T813: default branch only. T814: an unfinished walk reports UNFINISHED, never 0.
BASE=/tmp/p781/estate
mkdir -p "$BASE"
for slug in "$@"; do
  name=$(echo "$slug" | tr '/' '_')
  D="$BASE/$name"
  if [ -d "$D" ]; then echo "SKIP-EXISTS $slug"; continue; fi
  if timeout 180 git clone --filter=blob:none --no-checkout --single-branch \
      "https://github.com/$slug" "$D" >/dev/null 2>&1; then
    cd "$D" || continue
    br=$(git rev-parse --abbrev-ref HEAD)
    tot=$(git rev-list --count HEAD)
    out=$(timeout 200 git log --diff-filter=AMDR --name-status --date=short \
      --format="EV%x09%h%x09%ad%x09%an%x09%s" -- \
      "*LICENSE*" "*LICENCE*" "*COPYING*" "*license*" "*licence*" 2>&1)
    rc=$?
    if [ $rc -ne 0 ]; then
      echo "REPO	$slug	$br	$tot	WALK-UNFINISHED-rc$rc"
    else
      echo "REPO	$slug	$br	$tot	OK"
      echo "$out" | sed "s|^|  |"
    fi
    cd /tmp || exit
  else
    echo "REPO	$slug	-	-	CLONE-FAILED"
  fi
done
echo "ESTATE-DONE"
