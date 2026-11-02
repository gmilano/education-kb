#!/usr/bin/env bash
# p611-grant-gate.sh — the licence gate an education engagement stands up in week one.
#
# Why each step exists (every one is a defect this base measured, not a precaution):
#   1. Resolve the REAL default branch.      p559: a main-only read 404s for 32.4 % of addresses.
#                                            p611-C: one default branch is `produção` (non-ASCII).
#   2. Walk a LADDER of grant paths.         p610-E: omitting COPYING.txt graded the official
#                                            Moodle mobile app "ungranted".
#   3. Grade on the TITLE LINE only.         p611-B: GPL-2.0's own text names the Lesser GPL at
#                                            line 18, so a window substring mis-grades EVERY
#                                            GPL-2.0 file as LGPL.
#   4. Prefer the UPSTREAM a grant names.    p610-A: a fork's grant was paid-commercial while
#                                            naming MIT four times.
#   5. Run a FABRICATED CONTROL every time.  p608-A: an arm that cannot tell a real address from
#                                            an invented one certifies nothing.
#
# Usage: bash ingest/p611-grant-gate.sh <owner/repo> [owner/repo ...]
# Exit:  0 = every address graded; 2 = a control misbehaved (gate is untrustworthy this run).

set -uo pipefail
LADDER=(LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE-MIT LICENSE-APACHE)
CONTROL="openai/totally-not-real-edu-repo-$(date +%s)"

grade() {  # stdin: grant payload -> stdout: SPDX-ish grade, from the TITLE LINE only
  python3 -I -c '
import sys,re
t=sys.stdin.read()
title=" ".join([l.strip() for l in t.splitlines() if l.strip()][:3])
def h(p): return re.search(p,title,re.I)
if   h(r"GNU AFFERO GENERAL PUBLIC LICENSE"): print("AGPL-3.0" if h(r"Version 3") else "AGPL-?")
elif h(r"GNU LESSER GENERAL PUBLIC LICENSE"): print("LGPL-3.0" if h(r"Version 3") else "LGPL-2.1")
elif h(r"GNU GENERAL PUBLIC LICENSE"):
    print("GPL-3.0" if h(r"Version 3") else ("GPL-2.0" if h(r"Version 2") else "GPL-?"))
elif h(r"Apache License"):                    print("Apache-2.0" if h(r"Version 2") else "Apache-?")
elif h(r"MIT License"):                       print("MIT")
elif h(r"Permission is hereby granted, free of charge"): print("MIT-BODY-NO-TITLE")
elif h(r"Redistribution and use in source and binary"):  print("BSD-?")
elif h(r"Mozilla Public License"):            print("MPL-2.0")
elif h(r"Educational Community License"):     print("ECL-2.0")
else:                                         print("UNCLASSIFIED-NEEDS-HUMAN")
'
}

probe() {  # $1=owner/repo -> TSV row
  local r="$1" br payload path code size
  br=$(timeout 45 git ls-remote --symref "https://github.com/$r" HEAD 2>/dev/null \
       | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  if [[ -z "$br" ]]; then printf '%s\tUNREACHABLE\t-\t0\tNO-SUCH-ADDRESS\n' "$r"; return; fi
  for path in "${LADDER[@]}"; do
    read -r code size < <(curl -sL -o /tmp/pg.$$ -w '%{http_code} %{size_download}' \
      "https://raw.githubusercontent.com/$r/$br/$path")
    if [[ "$code" == 200 && "$size" -gt 100 ]]; then
      local g; g=$(grade < /tmp/pg.$$)
      # step 4: does the grant name an upstream to prefer?
      # p611-I: 610-A's upstream is a BARE SLUG ("adriasantacreu/google-classroom-mcp"), not a URL,
      # so a github.com-only regex never fires on the case that motivated the step. But matching
      # bare slugs alone scores 1/4 precision -- stock MIT text contains "and/or" and Apache
      # contains "www.apache.org/licenses". So a slug counts only when PROVENANCE-ANCHORED:
      # it must sit within 200 chars of upstream|fork|original|derived|based on, or be a URL.
      local up=""
      up=$(python3 -I -c '
import re,sys
t=open(sys.argv[1],encoding="utf-8",errors="replace").read()
self_slug=sys.argv[2].lower()
KEY=re.compile(r"upstream|fork(ed)?|original|derived|based on",re.I)
SLUG=re.compile(r"(?:github\.com/)?([A-Za-z0-9][A-Za-z0-9_.-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)")
STOP={"and","or","his","her","s","he","she","input","output","www.apache.org","yes","no"}
for m in SLUG.finditer(t):
    o,r=m.group(1),m.group(2)
    if o.lower() in STOP or "." in o: continue
    slug=f"{o}/{r}"
    if slug.lower()==self_slug: continue
    is_url = t[max(0,m.start()-11):m.start()].lower().endswith("github.com/")
    w=t[max(0,m.start()-200):m.end()+200]
    if is_url or KEY.search(w):
        print(slug); break
' /tmp/pg.$$ "$r" 2>/dev/null || true)
      printf '%s\t%s\t%s\t%s\t%s%s\n' "$r" "$br" "$path" "$size" "$g" \
        "${up:+	UPSTREAM-NAMED:$up}"
      rm -f /tmp/pg.$$; return
    fi
  done
  rm -f /tmp/pg.$$
  printf '%s\t%s\tNO-GRANT\t0\tUNGRANTED-LADDER-EXHAUSTED\n' "$r" "$br"
}

printf 'address\tdefault_branch\tgrant_path\tbytes\tgrade\tnote\n'
for r in "$@"; do probe "$r"; done

# step 5: the control must come back UNREACHABLE, in the same run.
cr=$(probe "$CONTROL" | cut -f2)
printf '%s\t%s\t-\t-\tFABRICATED-CONTROL\n' "$CONTROL" "$cr"
[[ "$cr" == "UNREACHABLE" ]] || { echo "GATE UNTRUSTWORTHY: control resolved" >&2; exit 2; }
