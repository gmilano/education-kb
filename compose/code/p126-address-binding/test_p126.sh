#!/bin/sh
# p126 -- ACTION AJ, AK, AL, AM. Fully offline: no network, no clock, no git.
#
# Every markdown fixture is a real construction copied off this KB's own live
# pages; `al-learnpress-readme.txt` carries the real plugin header bytes of
# `LearnPress/learnpress`. Each assertion names the clause it serves.
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
F="$HERE/fixtures"
PASS=0; FAIL=0

ok() { PASS=$((PASS+1)); printf '  ok   %s\n' "$1"; }
no() { FAIL=$((FAIL+1)); printf '  FAIL %s\n' "$1"; }
chk() { # chk NAME EXPECTED ACTUAL
    if [ "$2" = "$3" ]; then ok "$1"; else
        no "$1"; printf '         expected [%s]\n         actual   [%s]\n' "$2" "$3"
    fi
}

py() { python3 -I -c "$1"; }
PRE="import sys
sys.path.insert(0,'$HERE')
sys.path.insert(0,'$HERE/../p125-retraction-cue')
"

echo "== AJ: a token binds to an ADDRESS, not to a line =="

# AJ.1 the clause's own first example: one cell per platform, one token each.
chk "AJ.1  two-address row binds each token to its own repo" \
 "instructure/canvas-lms=AGPL-3.0 moodle/moodle=GPL-3.0" \
 "$(py "$PRE
import binding
l=open('$F/md-two-address-cell.md',encoding='utf-8').read()
print(' '.join('%s=%s'%(a,t) for a,t in sorted(binding.bound_pairs(l))))")"

# AJ.2 three addresses, three tokens, one cell -- nearest-address resolution.
chk "AJ.2  three-address cell binds all three correctly" \
 "instructure/canvas-lms=AGPL-3.0 moodle/moodle=GPL-3.0 openedx/edx-platform=AGPL-3.0" \
 "$(py "$PRE
import binding
l=open('$F/md-three-address-cell.md',encoding='utf-8').read()
print(' '.join('%s=%s'%(a,t) for a,t in sorted(binding.bound_pairs(l))))")"

# AJ.3 the row p125 called the defect worth the pass. The parenthetical short
# name is the only signal that resolves it; cell and distance both fail.
chk "AJ.3  short name beats cell and distance (pyBKT/catsim)" \
 "cahlr/pybkt=MIT douglasrizzo/catsim=BSD-3-Clause" \
 "$(py "$PRE
import binding
from correction_form import in_marked, marked_regions
l=open('$F/md-shortname-binding.md',encoding='utf-8').read()
r=marked_regions(l)
print(' '.join(sorted('%s=%s'%(a,t) for at,t,a in binding.bind(l)
      if a and not in_marked(l,at,r))))")"

# AJ.4 the clause's SECOND example. The referent -- the validator -- is named
# in prose, not as an address, so binding cannot reach it. This is why AJ's
# estimate of 15 was wrong: it counted a shape it could only half-resolve.
chk "AJ.4  prose referent is unreachable by binding" \
 "1edtech/openbadges-specification=Apache-2.0" \
 "$(py "$PRE
import binding
l=open('$F/md-spec-vs-validator.md',encoding='utf-8').read()
print(' '.join('%s=%s'%(a,t) for a,t in sorted(binding.bound_pairs(l))))")"

echo "== AK: old and new values are SETS, and need AJ underneath =="

# AK.1 the survivor is published on a DIFFERENT row from the correction, so a
# per-line live set cannot see it.
chk "AK.1  survivor CC-BY-SA-4.0 absent from the correction row's own live set" \
 "old-row-live=MIT new-row-live=CC-BY-SA-4.0,MIT" \
 "$(py "$PRE
from correction_form import in_marked, marked_regions, norm_token, vocab
def live(p):
    l=open(p,encoding='utf-8').read(); r=marked_regions(l)
    return ','.join(sorted({norm_token(m.group(0)) for m in vocab().finditer(l)
                            if not in_marked(l,m.start(),r)}))
print('old-row-live=%s new-row-live=%s'
      % (live('$F/md-split-survivor-old.md'), live('$F/md-split-survivor-new.md')))")"

# AK.2 unbound, the union hands pyBKT's MIT to catsim and launders the defect.
chk "AK.2  unbound survivor set wrongly gives catsim MIT" \
 "catsim-survives=BSD-3-Clause,MIT" \
 "$(py "$PRE
import grant_set
grant_set.BIND=False
s=grant_set.new_sets(['$F/md-shortname-binding.md'])
print('catsim-survives=%s'%','.join(sorted(s['douglasrizzo/catsim'])))")"

# AK.3 bound, it does not. This is the whole composition result.
chk "AK.3  bound survivor set keeps catsim's MIT superseded" \
 "catsim-survives=BSD-3-Clause" \
 "$(py "$PRE
import grant_set
grant_set.BIND=True
s=grant_set.new_sets(['$F/md-shortname-binding.md'])
print('catsim-survives=%s'%','.join(sorted(s['douglasrizzo/catsim'])))")"

echo "== AM: mark at write time -- and WHICH writer =="

# AM.1 p125's own defect-table header is unreadable by its own recogniser.
chk "AM.1  classify_header cannot read 'the page said'" \
 "None" \
 "$(py "$PRE
import correction_form as cf
print(cf.classify_header('| # | where | the page said | the file says | how it was missed |'))")"

# AM.2 so that table is not a correction table to p125's writer, and its
# quoted OLD values read as live claims on every page it was copied onto.
chk "AM.2  mark_forms sees no correction table there" \
 "0" \
 "$(py "$PRE
import mark_forms
print(len(mark_forms.table_hits('$F/md-page-said-header.md')))")"

# AM.3 three added spellings make it readable; the old column is 2, new is 3.
chk "AM.3  the added spellings make the header readable" \
 "([2], 3) hits=1" \
 "$(py "$PRE
import repair, mark_forms, correction_form as cf
repair.patch_header_vocabulary()
print('%s hits=%d'
      % (cf.classify_header('| # | where | the page said | the file says | how it was missed |'),
         len(mark_forms.table_hits('$F/md-page-said-header.md'))))")"

# AM.4 an inline cue inside a table CELL is reached by `mark_forms` -- this is
# why AM reproduces at all, and the opposite of what the older writer implies.
chk "AM.4  mark_forms reaches an inline cue inside a table cell" \
 "1/4/5/10 GPL-3.0" \
 "$(py "$PRE
import mark_forms
from correction_form import MARKER
l=open('$F/md-inline-cue-in-cell.md',encoding='utf-8').read().replace(MARKER,'')
h=mark_forms.cue_hits(l)[0]
print('%s %s'%(h[0],h[1]))")"

# AM.5 THE HAZARD. Two writers ship side by side in p125's directory and
# nothing says which is live. The superseded one has no APPARATUS guard, so on
# pages the live one has already converged it proposes dozens more marks --
# including a pass's own prose ABOUT the marker. This pass made that error.
# The invariant is asserted, not the figure: the superseded writer's false
# positives GROW with every pass that writes about the apparatus (50 on p125's
# pages, 57 once p126's sections were added), so pinning the number would make
# this test fail every pass for the wrong reason.
chk "AM.5  live writer converged; superseded writer has not" \
 "mark_forms=0 correction_form>=50 live-is-lower=True" \
 "$(py "$PRE
import os, mark_forms, correction_form as cf
os.chdir('$HERE/../../..')
P=['agents/top.md','agents/trending.md','repos/foundations.md',
   'repos/trending.md','verticals/solutions.md','intel/market.md',
   'intel/trends.md','intel/open-gaps.md','compose/patterns.md','README.md']
a=sum(mark_forms.apply_marks(p, dry=True)[0] for p in P)
b=sum(cf.apply_marks(p, dry=True) for p in P)
print('mark_forms=%d correction_form%s live-is-lower=%s'
      % (a, '>=50' if b>=50 else '=%d'%b, a<b))")"

# AM.6 the reproduction figure itself, pinned: p125's OWN writer accounts for
# every one of the 81 rows it marked.
chk "AM.6  mark_forms reproduces 81 of 81 of p125's marks" \
 "81 81" \
 "$(awk -F'[ \t]+' '/^# TOTAL/{print $3, $5}' "$HERE/out/am-reproduction.txt")"

echo "== AL: the extended grant-path list =="

# AL.1 the two conventions ACTION AI named are present in the probe list.
chk "AL.1  probe list carries the dual-filename and WordPress conventions" \
 "LICENSE.GPL=yes LICENSE.MPL=yes readme.txt=yes" \
 "$(for p in LICENSE.GPL LICENSE.MPL readme.txt; do
      if sed -n '/^NEW=/,/"$/p' "$HERE/probe_paths.sh" | grep -q "$p"
      then printf '%s=yes ' "$p"; else printf '%s=no ' "$p"; fi
    done | sed 's/ $//')"

# AL.2 the grant is in a FIELD of the plugin header, not in a licence file.
chk "AL.2  learnpress readme.txt declares GPLv3 in its plugin header" \
 "License: GPLv3|License URI: https://www.gnu.org/licenses/gpl-3.0.html" \
 "$(grep -i '^license' "$F/al-learnpress-readme.txt" | tr -d '\r' \
    | paste -sd'|' -)"

# AL.3 the census it was built for returned ONE address, not the three its
# clause required -- recorded here so the number cannot drift.
chk "AL.3  probe output: NEW-path grants found = 1" \
 "1" \
 "$(awk -F'\t' 'NR>1 && $3=="NEW" && $4==200' "$HERE/out/al-probe.tsv" \
    | wc -l | tr -d ' ')"

chk "AL.4  probe output carries no proxy noise (no 000/403)" \
 "0" \
 "$(awk -F'\t' 'NR>1 && ($4=="000" || $4=="403")' "$HERE/out/al-probe.tsv" \
    | wc -l | tr -d ' ')"

echo "== P126-A: committed evidence must be findable again =="

# A.1 p125's residue, as committed, is 36 records.
chk "A.1   ac-after.triples holds 36 records" \
 "36" "$(grep -c '|' "$HERE/../p125-retraction-cue/out/ac-after.triples")"

# A.2 and its baseline 61, so the newly-surfaced set is exactly AJ's 15.
chk "A.2   baseline 61, newly surfaced 15 (AJ's clause set)" \
 "61 15" \
 "$(py "$PRE
def r(p):
    return {l.strip() for l in open(p,encoding='utf-8') if '|' in l}
b=r('$HERE/../p125-retraction-cue/out/ac-baseline.triples')
a=r('$HERE/../p125-retraction-cue/out/ac-after.triples')
print(len(b), len(a-b))")"

# A.3 not one of the 36 recorded lines names the address it is filed under.
chk "A.3   recorded lines naming their own address = 0 of 36" \
 "0" \
 "$(py "$PRE
import os, repair_search
root='$HERE/../../..'
n=0
for l in open('$HERE/../p125-retraction-cue/out/ac-after.triples',encoding='utf-8'):
    l=l.strip()
    if '|' not in l: continue
    where,addr,tok=l.split('|'); page,ln=where.rsplit(':',1)
    try: lines=open(os.path.join(root,page),encoding='utf-8').readlines()
    except OSError: continue
    i=int(ln)
    if 1<=i<=len(lines) and addr.lower() in repair_search.addrs_on(lines[i-1]):
        n+=1
print(n)")"

echo
printf '%d passed / %d failed\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ] || exit 1
