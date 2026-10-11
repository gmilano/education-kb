#!/usr/bin/env bash
# p129 ACTION AS instrument: real tag count = ls-remote --tags lines minus ^{} dereference lines
addr="$1"
out=$(timeout 90 git ls-remote --tags "https://github.com/$addr" 2>/dev/null)
rc=$?
if [ $rc -ne 0 ]; then echo -e "$addr\tERR\tERR\tERR\t$rc"; exit 0; fi
total=$(printf '%s\n' "$out" | grep -c 'refs/tags/')
deref=$(printf '%s\n' "$out" | grep -c 'refs/tags/.*\^{}$')
real=$((total-deref))
latest=$(printf '%s\n' "$out" | grep 'refs/tags/' | grep -v '\^{}$' | sed 's|.*refs/tags/||' | tail -1)
echo -e "$addr\t$total\t$deref\t$real\t$latest"
