#!/bin/sh
# FIXTURE (p174). FABRICATED negative control: a hardcoded path that is NOT a KB
# clone root. The gate is about THIS repository's root, and widening it to every
# absolute path would make it fire on half the tree and be switched off.
. /usr/share/misc/helper.sh
cat /etc/os-release > /dev/null
