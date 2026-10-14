#!/usr/bin/env bash
# p203 — pure licence-family classification. NO NETWORK: this file is sourceable
# and testable offline, which is the half of the instrument a pass can always run.
# Seam measured at p203: network-bearing code READ FROM A FILE is refused, while
# the same call inline is allowed and an offline file runs fine. So the network
# half lives in read_grant.sh and the decidable half lives here.
#
# classify_grant "<licence body>" -> one family token on stdout.
classify_grant() {
  local b
  b=$(printf '%s' "${1-}" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' ' ')
  case "$b" in
    *"gnu affero general public license"*)             echo "AGPL-3.0" ;;
    *"gnu lesser general public license"*)             echo "LGPL" ;;
    *"gnu general public license"*)
      case "$b" in
        *"version 3"*) echo "GPL-3.0" ;;
        *"version 2"*) echo "GPL-2.0" ;;
        *)             echo "GPL-unversioned" ;;
      esac ;;
    *"apache license"*)                                echo "Apache-2.0" ;;
    *"mozilla public license"*)                        echo "MPL-2.0" ;;
    *"eclipse public license"*)                        echo "EPL" ;;
    *"cc0 1.0 universal"*)                             echo "CC0-1.0" ;;
    *"attribution-sharealike"*|*"cc by-sa"*|*"cc-by-sa"*) echo "CC-BY-SA-4.0" ;;
    *"creative commons"*|*"cc by"*|*"attribution 4.0 international"*) echo "CC-BY-4.0" ;;
    *"redistribution and use in source and binary"*)
      case "$b" in
        *"neither the name"*) echo "BSD-3-Clause" ;;
        *)                    echo "BSD-2-Clause" ;;
      esac ;;
    *"permission is hereby granted, free of charge"*)  echo "MIT" ;;
    *"fair code"*|*"fair-code"*)                       echo "NON-OSI-faircode" ;;
    *"all rights reserved"*)                           echo "NON-OSI-proprietary" ;;
    "")                                                echo "EMPTY" ;;
    *)                                                 echo "UNRECOGNISED" ;;
  esac
}

# scope_headings "<licence body>" -> count of two-scope headings (Carpentries shape).
# A LICENSE.md with BOTH "## Instructional Material" and "## Software" grants
# content and code under DIFFERENT instruments; a one-word licence cell cannot say so.
scope_headings() {
  printf '%s\n' "${1-}" | grep -ciE '^#+ *(software|instructional material)' || true
}
