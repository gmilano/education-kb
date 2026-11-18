import sys
target='intel/market.md'
mapping=[('### North America','scratchpad/p889/reg-na.md'),
         ('### EMEA','scratchpad/p889/reg-emea.md'),
         ('### APAC','scratchpad/p889/reg-apac.md'),
         ('### LATAM','scratchpad/p889/reg-latam.md'),
         ('### Global','scratchpad/p889/reg-global.md')]
lines=open(target,encoding='utf-8').read().split('\n')
start=next(i for i,l in enumerate(lines) if l.startswith('## Opportunities by region'))
# collect region heading indices within the section, in reverse so inserts don't shift earlier ones
targets=[]
for head,blk in mapping:
    idx=[i for i,l in enumerate(lines) if i>start and l.strip()==head]
    assert len(idx)==1, f"{head}: found {len(idx)} occurrences after Opportunities heading"
    targets.append((idx[0],head,blk))
for idx,head,blk in sorted(targets,reverse=True):
    body=open(blk,encoding='utf-8').read().rstrip('\n').split('\n')
    lines[idx+1:idx+1]=['']+body
    print(f"{head}: +{len(body)} lines after line {idx+1}")
open(target,'w',encoding='utf-8').write('\n'.join(lines))
