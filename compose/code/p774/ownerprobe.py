#!/usr/bin/env python3
"""p774 owner-only link sweep -- ACTION p773-F (carried from p772-G, unrun twice).

An owner-only link (`github.com/<owner>` with no repository) cannot be probed on
the ref channel, so this uses the HTTP channel on the account page. p772's sweep
already found `28` `topics/` pages and `7` EXISTS-BUT-EMPTY repositories hiding in
this base's address population; the same question applies to owner links -- a
renamed or deleted organisation is a dead citation that looks alive.

States: OK(user|org) · 404-ABSENT · OTHER-<code>
"""
import sys, urllib.request, urllib.error, re
from concurrent.futures import ThreadPoolExecutor
UA = {"User-Agent": "Mozilla/5.0 (compatible; kb-ingest-owner-probe/1.0)"}

def probe(owner):
    url = f"https://github.com/{owner}"
    try:
        r = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(r, timeout=25) as f:
            body = f.read(200000).decode("utf-8", "replace")
            kind = "org" if re.search(r'"?is_?organization"?\s*:\s*true|/orgs/'
                                      + re.escape(owner), body, re.I) else "user"
            # a renamed account 200s at the NEW name; record the canonical one
            canon = re.search(r'<meta property="profile:username" content="([^"]+)"', body)
            c = canon.group(1) if canon else owner
            flag = "" if c.lower() == owner.lower() else f"\tRENAMED->{c}"
            return f"{owner}\tOK({kind}){flag}"
    except urllib.error.HTTPError as e:
        return f"{owner}\t{'404-ABSENT' if e.code == 404 else f'OTHER-{e.code}'}"
    except Exception as e:
        return f"{owner}\tERROR({type(e).__name__})"

if __name__ == "__main__":
    owners = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    with ThreadPoolExecutor(max_workers=8) as ex:
        for line in ex.map(probe, owners):
            print(line, flush=True)
