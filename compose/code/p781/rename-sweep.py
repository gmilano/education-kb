#!/usr/bin/env python3
"""p781 rename-sweep: T810 at scale, as a SET-DIFFERENCE detector.

Method (discovered this pass, and it is cheaper than p780-B's one-call-per-slug):
  A search/repositories query carrying N `repo:` qualifiers returns exactly the
  slugs that EXIST. Dead slugs are silently DROPPED, not 422'd -- the 422 fires
  only when EVERY slug in the batch is dead. So requested-minus-returned is the
  dead set, at 1/40th the call cost.
CONTROLS, all blocking, run before any target:
  C1 all-alive batch must return N of N
  C2 a batch with exactly one known-dead slug must report that slug missing
  C3 an all-dead batch must be detected as 422 and sub-probed, never recorded alive
  C4 total_count must equal len(items), or the batch is truncated and is re-split
"""
import subprocess, json, sys, time

BATCH = 40

def search(slugs):
    q = ' '.join('repo:' + s for s in slugs)
    p = subprocess.run(['gh','api','-X','GET','search/repositories','-f','q='+q,
                        '-f','per_page=100'], capture_output=True, text=True, timeout=90)
    if p.returncode != 0:
        if '"status":"422"' in p.stdout or '422' in p.stderr:
            return 'ALL_DEAD', []
        return 'ERROR:'+p.stderr.strip()[:120], []
    d = json.loads(p.stdout)
    items = [it['full_name'] for it in d.get('items', [])]
    # C4: truncation guard
    if d.get('total_count', 0) != len(items):
        return 'TRUNCATED', items
    return 'OK', items

def probe(slugs, depth=0):
    """Returns (alive_set, dead_list). Recurses on ALL_DEAD/TRUNCATED."""
    if not slugs: return set(), []
    st, items = search(slugs)
    time.sleep(2.1)                      # 30 req/min search budget
    if st == 'OK':
        alive = set()
        low = {s.lower(): s for s in slugs}
        for it in items:
            if it.lower() in low: alive.add(low[it.lower()])
            else: alive.add(it)          # returned under a DIFFERENT name = rename
        dead = [s for s in slugs if s not in alive]
        return alive, dead
    if st in ('ALL_DEAD','TRUNCATED'):
        if len(slugs) == 1:
            return (set(), list(slugs)) if st == 'ALL_DEAD' else ({slugs[0]}, [])
        mid = len(slugs)//2
        a1,d1 = probe(slugs[:mid], depth+1); a2,d2 = probe(slugs[mid:], depth+1)
        return a1|a2, d1+d2
    print(f'  !! {st}', file=sys.stderr)
    return set(slugs), []                # fail SAFE: never manufacture a death

# ---- CONTROLS ----
print('CONTROLS', file=sys.stderr)
a,d = probe(['HKUDS/DeepTutor','moodle/moodle','oppia/oppia','frappe/education'])
assert len(a)==4 and not d, f'C1 FAILED {a} {d}'; print('  C1 all-alive 4/4 PASS', file=sys.stderr)
a,d = probe(['HKUDS/DeepTutor','openedx/edx-platform','oppia/oppia'])
assert d==['openedx/edx-platform'], f'C2 FAILED {d}'; print('  C2 one-dead isolated PASS', file=sys.stderr)
a,d = probe(['openedx/edx-platform','RoundTable02/socrates-skill'])
assert len(d)==2, f'C3 FAILED {a} {d}'; print('  C3 all-dead sub-probed 2/2 PASS', file=sys.stderr)

# ---- SWEEP ----
slugs = [l.split('\t')[0] for l in open('/tmp/p781/slugs.tsv')]
print(f'SWEEP {len(slugs)} distinct slugs, batch={BATCH}', file=sys.stderr)
alive_all, dead_all = set(), []
for i in range(0, len(slugs), BATCH):
    chunk = slugs[i:i+BATCH]
    a,d = probe(chunk)
    alive_all |= a; dead_all += d
    if d: print(f'  [{i:5d}] DEAD: {d}', file=sys.stderr)
    if (i//BATCH) % 20 == 0:
        print(f'  [{i:5d}/{len(slugs)}] dead so far={len(dead_all)}', file=sys.stderr)

with open('/tmp/p781/dead-slugs.txt','w') as fh:
    for s in dead_all: fh.write(s+'\n')
print(f'\nRESULT\tdistinct={len(slugs)}\talive={len(slugs)-len(dead_all)}\tdead={len(dead_all)}')
