#!/usr/bin/env python3
"""Barrido de la accion A del pase 110, con el detector de `P344`.

Canal: `raw.githubusercontent.com` (payload, no pagina renderizada).
10 nombres de archivo x 2 ramas + README en 4 ortografias x 3 refs.
El control negativo va en el MISMO lote (`P320`).
"""
import csv, hashlib, json, subprocess, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import detect_claim as D

RAW = 'https://raw.githubusercontent.com'
NAMES = ['LICENSE', 'LICENSE.md', 'LICENSE.txt', 'LICENSE.TXT', 'LICENCE',
         'LICENCE.md', 'COPYING', 'COPYING.md', 'LICENSE-MIT', 'LICENSE.rst']
BRANCHES = ['main', 'master']
READMES = ['README.md', 'readme.md', 'Readme.md', 'README.MD']


def fetch(url):
    """Devuelve (codigo, bytes). `curl` y no una libreria: es el canal que el
    resto de este arbol usa, y hay que medir el MISMO canal."""
    p = subprocess.run(['curl', '-sS', '--max-time', '25', '-w', '\n%{http_code}', url],
                       capture_output=True)
    out = p.stdout
    i = out.rfind(b'\n')
    if i < 0:
        return '000', b''
    return out[i + 1:].decode().strip(), out[:i]


def sweep(slug):
    hits, probes, codes = [], 0, {}
    for b in BRANCHES:
        for n in NAMES:
            probes += 1
            c, body = fetch(f'{RAW}/{slug}/{b}/{n}')
            codes[c] = codes.get(c, 0) + 1
            if c == '200':
                hits.append({'path': f'{b}/{n}', 'bytes': len(body),
                             'sha256': hashlib.sha256(body).hexdigest()[:12]})
    ref, body = '-', b''
    for b in BRANCHES + ['HEAD']:
        for r in READMES:
            if ref != '-':
                break
            c, bd = fetch(f'{RAW}/{slug}/{b}/{r}')
            if c == '200':
                ref, body = f'{b}/{r}', bd
        if ref != '-':
            break
    claims = D.detect(body.decode('utf-8', 'replace')) if ref != '-' else \
        {'badge_md': [], 'badge_html': [], 'tree': [], 'prose': [], 'families': []}
    return {'slug': slug, 'hits': hits, 'probes': probes, 'codes': codes,
            'readme_ref': ref, 'readme_bytes': len(body), 'claims': claims,
            'veredicto': D.verdict(claims, len(hits), ref != '-')}


def main(targets_file, out_tsv, out_json):
    slugs = [l.strip() for l in open(targets_file, encoding='utf-8') if l.strip()]
    rows, raw = [], []
    for s in slugs:
        r = sweep(s)
        raw.append(r)
        c = r['claims']
        rows.append({
            'slug': s,
            'license_file_hits': len(r['hits']),
            'probes': r['probes'],
            'codes': ';'.join(f'{k}x{v}' for k, v in sorted(r['codes'].items())),
            'readme_ref': r['readme_ref'],
            'readme_bytes': r['readme_bytes'],
            'badge_md': len(c['badge_md']),
            'badge_html': len(c['badge_html']),
            'tree': len(c['tree']),
            'prose': len(c['prose']),
            'families': ','.join(c['families']) or '-',
            'veredicto': r['veredicto'],
        })
        print(f"{s:<52} file={len(r['hits'])} readme={r['readme_ref']:<16} "
              f"md={len(c['badge_md'])} html={len(c['badge_html'])} "
              f"tree={len(c['tree'])} prose={len(c['prose'])} -> {r['veredicto']}",
              file=sys.stderr)
    with open(out_tsv, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter='\t')
        w.writeheader()
        w.writerows(rows)
    with open(out_json, 'w', encoding='utf-8') as fh:
        json.dump(raw, fh, indent=1, ensure_ascii=False)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
