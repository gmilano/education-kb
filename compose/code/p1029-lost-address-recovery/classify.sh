#!/usr/bin/env bash
# Pure functions for p1029. No network, no filesystem outside the paths given.
# Sourced by probe.sh and exercised directly by test_probe.sh.

# classify_payload <file> -> prints a licence family name on stdout.
# Order is load-bearing: AFFERO and LESSER must be tested before plain GPL,
# because both contain the string "GNU GENERAL PUBLIC LICENSE" by reference.
classify_payload() {
  local f="$1"
  [ -s "$f" ] || { echo "EMPTY"; return 0; }
  local t
  t=$(tr -d '\r' < "$f")

  case "$t" in
    *"GNU AFFERO GENERAL PUBLIC LICENSE"*) echo "AGPL-3.0"; return 0 ;;
    *"GNU LESSER GENERAL PUBLIC LICENSE"*) echo "LGPL-3.0"; return 0 ;;
  esac
  case "$t" in
    *"Apache License"*)
      case "$t" in *"Version 2.0"*) echo "Apache-2.0"; return 0 ;; esac
      echo "Apache-OTHER"; return 0 ;;
  esac
  case "$t" in
    *"GNU GENERAL PUBLIC LICENSE"*)
      case "$t" in
        *"Version 3"*) echo "GPL-3.0"; return 0 ;;
        *"Version 2"*) echo "GPL-2.0"; return 0 ;;
      esac
      echo "GPL-OTHER"; return 0 ;;
  esac
  case "$t" in
    *"Permission is hereby granted, free of charge"*) echo "MIT"; return 0 ;;
    *"Permission to use, copy, modify, and/or distribute this software for any purpose"*) echo "ISC"; return 0 ;;
    *"This is free and unencumbered software released into the public domain"*) echo "Unlicense"; return 0 ;;
    *"Mozilla Public License Version 2.0"*) echo "MPL-2.0"; return 0 ;;
    *"Eclipse Public License"*) echo "EPL"; return 0 ;;
  esac
  case "$t" in
    *"Redistribution and use in source and binary forms"*)
      case "$t" in
        *"Neither the name"*) echo "BSD-3-Clause"; return 0 ;;
      esac
      echo "BSD-2-Clause"; return 0 ;;
  esac
  case "$t" in
    *"Creative Commons"*) echo "CC-FAMILY"; return 0 ;;
  esac
  echo "UNRECOGNISED"
}

# count_tags <ls-remote --tags output file> -> unique tag count.
# Peeled entries (refs/tags/x^{}) name the SAME tag as their annotated parent,
# so counting raw lines over-counts annotated tags by one each. This is why the
# figure differs from a naive `wc -l` (dspace: 226 lines, 136 tags).
count_tags() {
  local f="$1"
  [ -f "$f" ] || { echo 0; return 0; }
  sed -n 's#.*refs/tags/##p' "$f" | sed 's/\^{}$//' | sort -u | grep -c . || true
}

# head_ref <ls-remote --symref HEAD output file> -> default branch name, or "-".
head_ref() {
  local f="$1"
  [ -f "$f" ] || { echo "-"; return 0; }
  local r
  r=$(sed -n 's#^ref: refs/heads/\([^[:space:]]*\)[[:space:]]*HEAD$#\1#p' "$f" | head -1)
  [ -n "$r" ] && echo "$r" || echo "-"
}

# head_sha <ls-remote --symref HEAD output file> -> HEAD SHA, or "-".
head_sha() {
  local f="$1"
  [ -f "$f" ] || { echo "-"; return 0; }
  local s
  s=$(awk '$2=="HEAD"{print $1; exit}' "$f")
  [ -n "$s" ] && echo "$s" || echo "-"
}
