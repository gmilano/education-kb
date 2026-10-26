#!/usr/bin/env python3
"""p455 -- is a single registry read EVIDENCE? Measured, because this pass's
own instrument gave two different answers for the same URL minutes apart.

Run B of `followup.py` read `registry.npmjs.org/pawnote` as
`1.6.2 / GPL-3.0-or-later / LiterateInk/Pawnote.js`. Run F, a few minutes
later, read the SAME URL as an empty record. Every licence cell this base has
sourced from a registry rests on one read, so the flap rate is not a curiosity
-- it is the error bar on a whole channel.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch
from followup import slug_from

N = 6
print(f"[G] {N} consecutive reads of the same registry URLs")
for kind, name in [("npm", "pawnote"), ("npm", "webuntis"), ("pypi", "pronotepy")]:
    seen = []
    for i in range(N):
        r = fetch.registry(kind, name)
        seen.append((r["status"], r["version"], r["declared"], slug_from(r["backlink"])))
    uniq = sorted(set(seen))
    verdict = "STABLE" if len(uniq) == 1 else f"FLAPPING ({len(uniq)} distinct)"
    print(f"  {kind}:{name:12} {verdict}")
    for u in uniq:
        print(f"      {seen.count(u)}/{N}  status={u[0]} v={u[1]!r} declared={u[2]!r} addr={u[3]!r}")

print("\n[H] the back-linked address npm names for `pawnote`, case variants")
for addr in ["LiterateInk/Pawnote.js", "LiterateInk/pawnote",
             "literateink/Pawnote.js", "LiterateInk/Pawnote"]:
    g = fetch.grant(addr)
    print(f"  {addr:28} {g['verdict']:20} {g.get('path', g.get('live_path',''))}"
          f"@{g.get('ref','')} {g.get('bytes',0)}B {g.get('sha','')}")
