#!/usr/bin/env python3
"""p781 shelf writer: prepend a new `## ` section immediately after the YAML
frontmatter and set `updated:` to the pass date, so that ACTION p780-G's two
checks (newest section names the pass; YAML updated: equals the heading date)
both pass by construction rather than by luck.
"""
import sys, re, io

def write(path, section, date):
    src = io.open(path, encoding='utf-8').read()
    m = re.match(r'^(---\n.*?\n---\n)', src, re.S)
    if not m:
        raise SystemExit(f'{path}: no YAML frontmatter')
    fm, body = m.group(1), src[m.end():]
    fm = re.sub(r'(?m)^updated:.*$', f'updated: {date}', fm)
    out = fm + '\n' + section.rstrip('\n') + '\n\n' + body.lstrip('\n')
    io.open(path, 'w', encoding='utf-8').write(out)
    print(f'  wrote {path}  (+{len(section)} B)')

if __name__ == '__main__':
    path, secfile, date = sys.argv[1], sys.argv[2], sys.argv[3]
    write(path, io.open(secfile, encoding='utf-8').read(), date)
