#!/usr/bin/env bash
# alias-sweep.sh — p543, delivering Gap 542-C in the environment that exists.
#
# 542-C asked for "a redirect check on every held address". p543 measured that
# the HTTP redirect channel is GONE: github.com returns 403 at this gateway for
# every path (p380's HTML channel, which p542 still read sidebars from three
# hours earlier). So the asked-for instrument cannot be built.
#
# What CAN be built: `git ls-remote` is live, and a rename leaves the old and
# new addresses serving the SAME object graph. Identical HEAD sha therefore
# identifies an alias pair without any redirect header. Calibrated on the case
# p542 found by hand: MeetYourAI/AIProf and TheFlameFoundation/AIBot-Prof-Helper
# both answer 9125548dab00.
#
# LIMIT, stated because it bounds the verdict: this finds alias PAIRS already
# on the shelf. It cannot name the new address of a repo renamed away to an
# address this base has never recorded -- ls-remote follows the rename
# silently and reports no name at all. That half of 542-C stays open.
#
# USAGE  ./alias-sweep.sh file-with-addresses.txt
set -uo pipefail
printf 'address\tstate\thead_sha\tdefault_branch\n'
while read -r slug; do
  [ -z "$slug" ] && continue
  out=$(git ls-remote --symref "https://github.com/${slug}" HEAD 2>/dev/null)
  if [ -z "$out" ]; then printf '%s\tDEAD/PRIVATE\t-\t-\n' "$slug"; continue; fi
  br=$(printf '%s\n' "$out" | awk '/^ref:/{print $2}' | sed 's#refs/heads/##')
  sha=$(printf '%s\n' "$out" | awk '!/^ref:/ && $2=="HEAD"{print substr($1,1,12)}')
  printf '%s\tLIVE\t%s\t%s\n' "$slug" "${sha:--}" "${br:--}"
done < "$1"
