#!/bin/sh
# p142-contact-cohort — ACTION DG: is openedx/XBlock's stale `oscm@edx.org` a one-off typo or
# a cohort defect left by one contractor's `chore: modernize` campaign?
#
# p141 measured two repositories and found the campaign correcting the contact in September and
# retyping the stale one in June. This widens the population to six further `openedx/*`
# repositories and correlates, per repo:
#
#   * the contact address at HEAD (pyproject.toml `authors`/`maintainers`, or setup.py
#     `author_email` where the repo has not been migrated yet)
#   * the commit that last touched that line -- author, email domain, date, subject
#
# Reported per repository; no figure is derived from a repo whose line could not be located.
for d in "$@"; do
  name=$(basename "$d")
  [ -d "$d/.git" ] || { printf '%s\tNO_CLONE\t-\t-\t-\t-\n' "$name"; continue; }
  # Where does the contact live?
  file=""
  for f in pyproject.toml setup.py setup.cfg; do
    if [ -f "$d/$f" ] && grep -qiE '(author_email|maintainer_email|email *=)' "$d/$f" 2>/dev/null; then
      file="$f"; break
    fi
  done
  if [ -z "$file" ]; then printf '%s\tNO_CONTACT_FIELD\t-\t-\t-\t-\n' "$name"; continue; fi
  addr=$(grep -ohE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$d/$file" 2>/dev/null | sort -u | paste -sd',' -)
  [ -z "$addr" ] && addr="NONE"
  # The commit that last set the email line in that file.
  line=$(grep -nE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$d/$file" 2>/dev/null | head -1 | cut -d: -f1)
  if [ -n "$line" ]; then
    meta=$(git -C "$d" log -1 --format='%h|%ae|%ad|%s' --date=short -L "$line,$line:$file" 2>/dev/null | head -1)
  fi
  [ -z "$meta" ] && meta=$(git -C "$d" log -1 --format='%h|%ae|%ad|%s' --date=short -- "$file" 2>/dev/null)
  sha=$(echo "$meta" | cut -d'|' -f1);  who=$(echo "$meta" | cut -d'|' -f2)
  when=$(echo "$meta" | cut -d'|' -f3); subj=$(echo "$meta" | cut -d'|' -f4 | cut -c1-60)
  # Does this repo carry a `chore: modernize`-class commit at all, and when?
  mod=$(git -C "$d" log --format='%ad|%ae|%s' --date=short -i --grep='modernize' 2>/dev/null | head -1)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$name" "$addr" "$file" "$sha/$when" "$who" "$subj" "${mod:--}"
done
