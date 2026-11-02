#!/bin/bash
# srch.sh "<query>" [per_page] -> TSV: full_name license stars forks pushed default_branch desc
q="$1"; pp="${2:-20}"
gh api -X GET search/repositories -f q="$q" -f per_page="$pp" -f sort=stars -f order=desc 2>/dev/null \
 | python3 -I -c '
import json,sys
try: d=json.load(sys.stdin)
except Exception as e: print("ERR",e); sys.exit()
for it in d.get("items",[]):
    lic=(it.get("license") or {}).get("spdx_id") or "NONE"
    print("\t".join([it["full_name"],lic,str(it["stargazers_count"]),str(it["forks_count"]),
      (it.get("pushed_at") or "")[:10],it.get("default_branch") or "",(it.get("description") or "")[:150]]))
'
