#!/usr/bin/env bash
# p640 — byte-exact licence oracle over raw.githubusercontent.com using curl GET.
# Repairs the three failures 639-G characterised:
#   (i)   AFFERO is tested before GPL, on the whole payload  -> no AGPL->GPL mis-grade
#   (ii)  CC0 and non-English payloads are graded            -> fewer UNGRADED
#   (iii) case variants + more filenames + source-file headers -> fewer false NO-PAYLOAD
# Negative control: a fabricated slug must return 404. curl -sI must NOT be used: the proxy's
# CONNECT reply is "200 Connection Established" for real AND fabricated slugs (637-E).
set -uo pipefail
BODY=$(mktemp)
trap "rm -f $BODY" EXIT
BRANCHES="main master"
NAMES="LICENSE LICENSE.md LICENSE.txt license license.md license.txt License LICENCE licence COPYING COPYING.txt LICENSE-MIT MIT-LICENSE.txt LICENSE.rst"
HDRS="version.php lib.php setup.py pyproject.toml package.json"

grade() { # stdin = payload
  local p; p=$(tr '[:upper:]' '[:lower:]')
  case "$p" in
    *"affero general public license"*) echo "AGPL-3.0"; return;; # (i) AFFERO FIRST
  esac
  case "$p" in
    *"elastic license"*)                echo "ELASTIC-2.0-source-available"; return;;
    *"educational community license"*)  echo "ECL-2.0"; return;;
    *"apache license"*)                 echo "APACHE-2.0"; return;;
    *"lesser general public license"*)  echo "LGPL"; return;;
    *"general public license"*)         echo "GPL"; return;;
    *"mozilla public license"*)         echo "MPL-2.0"; return;;
    *"cc0 1.0 universal"*|*"creative commons legal code"*"cc0"*) echo "CC0-1.0"; return;; # (ii)
    *"attribution-noncommercial"*|*"noncommercial"*) echo "CC-BY-NC-nonfree"; return;;
    *"attribution-sharealike"*)         echo "CC-BY-SA-4.0"; return;;
    *"creative commons attribution"*)   echo "CC-BY"; return;;
    *"permission is hereby granted, free of charge"*) echo "MIT"; return;;
    *"redistribution and use in source and binary forms"*) echo "BSD"; return;;
    *"unlicense"*)                      echo "UNLICENSE"; return;;
    *"licencia"*|*"licença"*|*"许可证"*|*"授权"*) echo "NON-ENGLISH-PAYLOAD-needs-read"; return;; # (ii)
  esac
  echo "UNGRADED"
}

probe() { # $1=slug -> slug <TAB> channel <TAB> bytes <TAB> grade
  local slug="$1" b n url code size body
  for b in $BRANCHES; do for n in $NAMES; do
    url="https://raw.githubusercontent.com/$slug/$b/$n"
    read -r code size < <(curl -s -o "$BODY" -w '%{http_code} %{size_download}' --max-time 20 "$url")
    if [ "$code" = "200" ] && [ "$size" -gt 0 ]; then
      printf '%s\t%s\t%s\t%s\n' "$slug" "$b/$n" "$size" "$(grade < "$BODY")"; return
    fi
  done; done
  # (iii) third channel: source-file headers (639-G's ACTION MO)
  for b in $BRANCHES; do for n in $HDRS; do
    url="https://raw.githubusercontent.com/$slug/$b/$n"
    read -r code size < <(curl -s -o "$BODY" -w '%{http_code} %{size_download}' --max-time 20 "$url")
    if [ "$code" = "200" ] && [ "$size" -gt 0 ]; then
      g=$(head -c 4000 "$BODY" | grep -ioE "GNU (Affero )?General Public License(,? either )?(version [0-9]+)?( or later)?|Apache License|MIT License" | head -1)
      if [ -n "$g" ]; then printf '%s\tHEADER:%s\t%s\t%s\n' "$slug" "$b/$n" "$size" "HEADER:$g"; return; fi
    fi
  done; done
  printf '%s\t%s\t%s\t%s\n' "$slug" "NO-PAYLOAD" "0" "NO-PAYLOAD-not-where-we-looked"
}
for s in "$@"; do probe "$s"; done
