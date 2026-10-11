#!/usr/bin/env python3
"""p129 ACTION AT instrument: census the HOLDER line of a licence payload, not just the token.

A grant with no identifiable licensor cannot be relied on, and the standard texts of Apache-2.0,
GPL and MPL all CONTAIN a placeholder holder line inside their 'how to apply' instructions.
So the operative text is truncated at the instruction boundary before the holder is read.
"""
import re, sys

BOUNDARIES = [
    "APPENDIX: How to apply the Apache License",
    "How to Apply These Terms to Your New Programs",
    "END OF TERMS AND CONDITIONS",
    "Exhibit A - Source Code Form License Notice",
]
# A NOTICE, not the word: the remainder must open with a year, a year range or a placeholder.
# Without this, the wrapped prose of GPL-3 ('copyright on the Program, and are irrevocable')
# reads as a holder line and every copyleft payload returns a spurious NAMED holder.
COPY = re.compile(r'^\s*(?:#|//|\*)?\s*(?:©|\(c\)|\(C\))?\s*copyright\b\s*(?:\(c\)|©|\(C\))?\s*'
                  r'((?:\d{4}|\[|<|\(c\)|\(C\)|©).*)$', re.I)
STEWARD = re.compile(r'Free Software Foundation|Creative Commons|Open Source Initiative'
                     r'|Mozilla Foundation|Apereo Foundation, Inc\.$', re.I)
# <http://fsf.org/> is an address, not an unfilled field; only <name of author> shapes count.
PLACEHOLDER = re.compile(
    r'\[[^\]]*\]|<(?![^>]*(?:://|@|\.org|\.com))[^>]*>|\byour name\b|\bname of (?:the )?(?:author|copyright owner|copyright holder)s?\b'
    r'|\bcopyright holders?\b|\bfullname\b|\bowner\b|\byyyy\b|\bxxxx+\b|\bauthors?/institution\b'
    r'|\bTODO\b|\bPROJECT ?NAME\b|\bORGANI[SZ]ATION\b', re.I)
YEARONLY = re.compile(r'^[\s\d,–—-]*(?:present)?[\s.,]*$', re.I)

def family(text):
    t = text[:4000]
    if "Business Source License" in t: return "BSL-1.1 (NOT OSI)"
    if "PolyForm" in t: return "PolyForm (NOT OSI)"
    if "Server Side Public License" in t: return "SSPL (NOT OSI)"
    for sig, name in [("Apache License","Apache-2.0"),("MIT License","MIT"),
                      ("GNU AFFERO GENERAL PUBLIC LICENSE","AGPL"),
                      ("GNU LESSER GENERAL PUBLIC LICENSE","LGPL"),
                      ("GNU GENERAL PUBLIC LICENSE","GPL"),
                      ("Mozilla Public License","MPL-2.0"),
                      ("Redistribution and use in source and binary forms","BSD"),
                      ("ISC License","ISC"),
                      ("Creative Commons","CC"),
                      ("Educational Community License","ECL"),
                      ("Open Software License","OSL"),
                      ("This is free and unencumbered software released into the public domain","Unlicense")]:
        if sig.lower() in t.lower(): return name
    return "UNKNOWN"

def operative(text):
    cut = len(text)
    for b in BOUNDARIES:
        i = text.find(b)
        if i != -1: cut = min(cut, i)
    return text[:cut]

def holders(text):
    out = []
    for line in operative(text).splitlines():
        m = COPY.match(line)
        if not m: continue
        rest = m.group(1).strip().rstrip('.')
        rest = re.sub(r'^\(c\)\s*', '', rest, flags=re.I)
        out.append(rest)
    return out

MDLINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def classify(hs):
    if not hs: return "NO-HOLDER-IN-OPERATIVE-TEXT", ""
    if all(STEWARD.search(h) for h in hs):
        return "DOCUMENT-TEXT", hs[0]
    hs = [h for h in hs if not STEWARD.search(h)]
    for h in hs:
        if not PLACEHOLDER.search(h) and not YEARONLY.match(re.sub(r'^\s*[\d,–-]+\s*','',h)) \
           and re.search(r'[A-Za-z]{2,}', re.sub(r'^\s*[\d,–-]+\s*','',h)):
            return "NAMED", h
    h = hs[0]
    # '[Submitty team](AUTHORS.md)' is a licensor NAMED BY REFERENCE, not an unfilled field.
    # The reference still has to resolve, so the verdict says where to look rather than passing it.
    if MDLINK.search(h): return "HOLDER-BY-REFERENCE", h
    if PLACEHOLDER.search(h): return "PLACEHOLDER", h
    return "UNFILLED", h

if __name__ == "__main__":
    text = sys.stdin.read()
    hs = holders(text)
    verdict, h = classify(hs)
    print("%s\t%s\t%s\t%d" % (family(text), verdict, h.replace("\t"," ")[:120], len(hs)))
