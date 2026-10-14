import re, sys

# Title-block classifier.  The trap this MUST avoid: real GPL-3.0 text contains section 13
# ("Use with the GNU Affero General Public License"), so any classifier that greps the BODY
# for "AFFERO" returns AGPL-3.0 for genuine GPL-3.0.  So: classify on the TITLE block only.
def family(text):
    head = "\n".join(text.splitlines()[:40])
    n = re.sub(r"\s+", " ", head).strip()
    nl = n.lower()
    full = re.sub(r"\s+", " ", text).lower()

    if "gnu affero general public license" in nl:
        return "AGPL-3.0" if "version 3" in nl else "AGPL?"
    if "gnu lesser general public license" in nl:
        if "version 3" in nl: return "LGPL-3.0"
        if "version 2.1" in nl: return "LGPL-2.1"
        return "LGPL?"
    if "gnu general public license" in nl:
        if "version 3" in nl: return "GPL-3.0"
        if "version 2" in nl: return "GPL-2.0"
        return "GPL?"
    if "educational community license" in nl:
        return "ECL-2.0" if "version 2.0" in nl else "ECL?"
    if "apache license" in nl:
        if "version 2.0" in nl: return "Apache-2.0"
        if "version 1.1" in nl: return "Apache-1.1"
        return "Apache?"
    if "mozilla public license" in nl:
        return "MPL-2.0" if "version 2.0" in nl else "MPL?"
    if "eclipse public license" in nl:
        if "v 2.0" in nl or "version 2.0" in nl: return "EPL-2.0"
        if "v 1.0" in nl or "version 1.0" in nl: return "EPL-1.0"
        return "EPL?"
    if "european union public licence" in nl or "eupl" in nl:
        return "EUPL-1.2" if "1.2" in nl else "EUPL?"
    if "creative commons" in nl:
        if "attribution-sharealike" in nl: return "CC-BY-SA"
        if "attribution-noncommercial" in nl: return "CC-BY-NC"
        if "attribution" in nl: return "CC-BY"
        if "cc0" in nl or "zero" in nl: return "CC0"
        return "CC?"
    if "the unlicense" in nl or "unlicense" in nl and "public domain" in full:
        return "Unlicense"
    if "mit license" in nl or "mit licence" in nl:
        return "MIT"
    # MIT with no title block: the operative grant phrase
    if "permission is hereby granted, free of charge" in full:
        return "MIT"
    if "redistribution and use in source and binary forms" in full:
        if "neither the name" in full: return "BSD-3-Clause"
        if "endorse or promote" in full: return "BSD-3-Clause"
        return "BSD-2-Clause"
    if "do what the fuck you want" in nl: return "WTFPL"
    if "isc license" in nl: return "ISC"
    return "NO-FAMILY"

# A grant-bearing text vs a non-grant (template, stub, pointer, header list)
GRANT_PHRASES = [
    "permission is hereby granted", "redistribution and use", "licensed under the apache license",
    "terms and conditions for use, reproduction", "this license applies to any program",
    "everyone is permitted to copy and distribute verbatim copies",
    "you may not use this file except in compliance",
]
def is_grant(text):
    full = re.sub(r"\s+", " ", text).lower()
    return any(p in full for p in GRANT_PHRASES)

if __name__ == "__main__":
    t = open(sys.argv[1], encoding="utf-8", errors="replace").read()
    print(f"{family(t)}\t{'GRANT' if is_grant(t) else 'NON-GRANT'}\t{len(t.encode('utf-8'))}")
