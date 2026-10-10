#!/usr/bin/env bash
# grant-ladder-v3 (pass 91, 2026-10-09)
#
# Resolves a GitHub slug to (existence, default branch, HEAD SHA, licence read from the payload, bytes).
#
# WHY v3 EXISTS — two defects in v2, both verifiable:
#   1. v2 probed 12 filenames. Its README and six shelf rows claimed "17"; five more claimed "16".
#      `frappe/lms` carries its grant at `license.txt` (lowercase) — a name v2 NEVER TRIED — so v2
#      would have returned NO-LICENCE-PAYLOAD for an AGPL-3.0 repo. Every "no grant" verdict produced
#      by v2 is therefore an upper bound, not a measurement.
#   2. v2's classifier did not know ECL-2.0 (Educational Community License) and returned
#      OTHER/unclassified for `sakaiproject/sakai` and `opencast/opencast` — two PERMISSIVE platforms.
#      Pass 90 recorded "any future version must recognise ECL by name". This is that version.
#
# The name list is printed by `--names` and its length by `--count`, so the shelf can never again
# publish a filename count the instrument does not have.
set -u
export GIT_TERMINAL_PROMPT=0 GIT_ASKPASS=/bin/true

# 24 candidate filenames. Ordered: exact-common first, then case variants, then split-grant names.
NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md LICENCE.txt
COPYING COPYING.txt COPYING.md COPYING.LESSER
license license.txt license.md License License.md LICENSE.rst LICENSE.markdown
LICENSE-MIT LICENSE-APACHE LICENSE-BSD LICENSE-CODE COPYRIGHT COPYRIGHT.txt NOTICE"

ALL=0
if [ "${1:-}" = "--all" ]; then ALL=1; shift; fi

case "${1:-}" in
  --names) echo $NAMES | tr ' ' '\n' | grep -c . ; echo $NAMES | tr ' ' '\n' | grep . ; exit 0 ;;
  --count) echo $NAMES | tr ' ' '\n' | grep -c . ; exit 0 ;;
esac

NCOUNT=$(echo $NAMES | tr ' ' '\n' | grep -c .)

classify() {
  head -c 4000 "$1" | tr 'A-Z' 'a-z' | python3 -I -c '
import sys
t = sys.stdin.read()
# ECL FIRST: it is Apache-2.0-derived, so an Apache test would swallow it. Education has its own family.
if "educational community license" in t:                       print("ECL-2.0")
elif "european union public licence" in t or "eupl" in t:      print("EUPL-1.2")
elif "apache license" in t and "version 2.0" in t:             print("Apache-2.0")
elif "gnu affero" in t:                                        print("AGPL-3.0")
elif "gnu lesser" in t or "lesser general public" in t:        print("LGPL-3.0")
elif "gnu general public" in t:                                print("GPL-3.0" if "version 3" in t else "GPL")
elif "mozilla public" in t:                                    print("MPL-2.0")
elif "business source license" in t:                           print("BSL-1.1-NOT-OSI")
elif "fair code license" in t or "fair-code" in t:             print("FAIRCODE-NOT-OSI")
elif "sustainable use license" in t:                           print("SUL-NOT-OSI")
elif "permission is hereby granted, free of charge" in t:
    # ISC and MIT share this opening; ISC omits the "sublicense" grant and the "MERCHANTABILITY" triplet
    print("ISC" if "sublicense" not in t and "internet systems consortium" in t else "MIT")
elif "permission to use, copy, modify, and/or distribute" in t: print("ISC")
elif "redistribution and use in source and binary" in t:       print("BSD")
elif "this software is provided as-is" in t and "zlib" in t:   print("Zlib")
# CC BEFORE the public-domain test: a CC BY-NC-SA summary contains the words "public domain"
# in its Notices section, and pass 91 measured this instrument reporting NC-copyleft as PD.
# Dropping an unclassified row is conservative; calling NC content public domain is not.
elif "cc0 1.0 universal" in t or ("creative commons" in t and "cc0" in t):
    print("CC0-1.0")
elif "creative commons" in t or "creativecommons.org" in t:
    if "noncommercial" in t or "by-nc" in t:
        print("CC-BY-NC-SA" if ("sharealike" in t or "share-alike" in t or "by-nc-sa" in t) else "CC-BY-NC")
    else:
        print("CC-BY-SA" if ("sharealike" in t or "by-sa" in t) else "CC-BY")
elif "unlicense" in t or "public domain" in t:                 print("Unlicense/PD")
else:                                                          print("OTHER/unclassified")
'
}

for slug in "$@"; do
  out=$(timeout 30 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  if [ -z "$out" ]; then echo -e "$slug\tABSENT\t-\t-\t-\t-"; continue; fi
  ref=$(echo "$out" | awk '/^ref:/{print $2}' | sed 's#refs/heads/##')
  sha=$(echo "$out" | awk '!/^ref:/{print $1; exit}')
  found=""; every=""
  for n in $NAMES; do
    r=$(timeout 20 curl -s -o "/tmp/lic.$$" -w "%{http_code} %{size_download}" \
        "https://raw.githubusercontent.com/$slug/$sha/$n" 2>/dev/null)
    code=${r%% *}; bytes=${r##* }
    if [ "$code" = "200" ] && [ "$bytes" -gt 200 ] 2>/dev/null; then
      k=$(classify "/tmp/lic.$$")
      [ -z "$found" ] && found="$n|$k|$bytes"
      every="$every $n=$k:${bytes}B"
      [ "$ALL" = "0" ] && break
    fi
  done
  rm -f "/tmp/lic.$$"
  if [ -z "$found" ]; then
    echo -e "$slug\tEXISTS\t$ref\t${sha:0:7}\tNO-LICENCE-PAYLOAD/${NCOUNT}\t-"
  elif [ "$ALL" = "1" ]; then
    nk=$(echo $every | tr ' ' '\n' | grep -c .)
    distinct=$(echo $every | tr ' ' '\n' | sed 's/.*=//;s/:.*//' | sort -u | tr '\n' ',' | sed 's/,$//')
    tag="SINGLE"; [ "$(echo "$distinct" | tr -cd ',' | wc -c)" -gt 0 ] && tag="SPLIT-GRANT"
    echo -e "$slug\tEXISTS\t$ref\t${sha:0:7}\t$tag[$distinct]\t${nk} file(s):$every"
  else
    echo -e "$slug\tEXISTS\t$ref\t${sha:0:7}\t$(echo "$found"|cut -d'|' -f2)\t$(echo "$found"|cut -d'|' -f1):$(echo "$found"|cut -d'|' -f3)B"
  fi
done
