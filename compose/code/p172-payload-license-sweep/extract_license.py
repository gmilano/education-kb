#!/usr/bin/env python3
"""
P172 — extract a license CESSION from an RDF payload.

Three defects found while building this (all the same family as P171: a regex that matches
ONE serialization silently reports absence for the others).  Each has a named control in
test_extract.py:

  D1 predicate-as-URI.  `<http://purl.org/dc/terms/license> <https://...by-sa/4.0/>`
     Taking the FIRST URI of the match returns the PREDICATE and reports it as the license.
  D2 blank-node indirection.  `dct:license [ rdf:value <https://...by/4.0/> ; rdfs:label ... ]`
     The object is a blank node, so the URI is not adjacent to the predicate.
  D3 depth.  A VOID/DCAT dataset description can carry dct:license well past any "header"
     window (jp-cos dataset-20250927.ttl declares it at line 66, beyond 6 KB of prefixes and
     long dct:description literals).  A header-only read reports a false absence.

A declaration is a license PREDICATE bound to a license VALUE.  `terms:license rdf:type
owl:AnnotationProperty` only names the term and cedes nothing.
"""
import re, sys

PRED = re.compile(
    r'(?:(?:terms|dcterms|dct|dc|cc|schema|xhtml)\s*:\s*licen[sc]e'
    r'|<https?://(?:purl\.org/dc/(?:terms|elements/1\.1)|creativecommons\.org/ns)[#/]licen[sc]e>'
    r'|licen[sc]e\s+rdf:resource)', re.I)

# URIs that are predicates/vocabulary, never a cession.
NOT_A_LICENSE = re.compile(
    r'^https?://(?:purl\.org/dc/(?:terms|elements/1\.1)/licen[sc]e$'
    r'|(?:www\.)?w3\.org/|creativecommons\.org/ns[#/]|xmlns\.com/|rdfs\.org/|licensebuttons\.net/)', re.I)

URI = re.compile(r'<(https?://[^>\s]+)>|rdf:resource\s*=\s*"(https?://[^"]+)"')

def find(text, window=400):
    for m in PRED.finditer(text):
        if re.match(r'\s*rdf:type', text[m.end():m.end()+20]):   # a term declaration, not a cession
            continue
        for um in URI.finditer(text, m.end(), min(len(text), m.end() + window)):
            uri = um.group(1) or um.group(2)
            if not NOT_A_LICENSE.match(uri):
                return uri
    return None

if __name__ == '__main__':
    data = sys.stdin.read()
    u = find(data)
    print(u if u else '-')
