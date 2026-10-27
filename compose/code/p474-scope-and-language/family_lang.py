"""p474 - Gap 473-C: a licence-title reader that is not keyed on English only,
plus Gap 474 scope axis: a grant may be scoped to subtrees.

Anchored on the title block (p454/p455 rule: the one region a preamble cannot
reach), extended with pt/es renderings. Size is never consulted (p467 Gap 466-C).
"""

# --- title layer: (family, [title substrings in any supported language]) ---
TITLES = [
    ("AGPL", ["GNU AFFERO GENERAL PUBLIC LICENSE",
              "LICENCA PUBLICA GERAL AFFERO GNU",      # pt, accent-folded
              "LICENCIA PUBLICA GENERAL AFFERO DE GNU",
              "LICENCIA PUBLICA GENERAL AFFERO GNU"]),  # es
    ("LGPL", ["GNU LESSER GENERAL PUBLIC LICENSE",
              "LICENCA PUBLICA GERAL MENOR DO GNU",
              "LICENCIA PUBLICA GENERAL REDUCIDA DE GNU"]),
    ("GPL",  ["GNU GENERAL PUBLIC LICENSE",
              "LICENCA PUBLICA GERAL GNU", "LICENCA PUBLICA GERAL DO GNU",
              "LICENCIA PUBLICA GENERAL DE GNU", "LICENCIA PUBLICA GENERAL GNU"]),
    ("ECL",  ["EDUCATIONAL COMMUNITY LICENSE"]),
    ("APACHE", ["APACHE LICENSE"]),
    ("MIT",  ["MIT LICENSE", "LICENCA MIT", "LICENCIA MIT"]),
    ("BSD",  ["BSD ", "REDISTRIBUTION AND USE IN SOURCE AND BINARY FORMS"]),
    ("CC",   ["CREATIVE COMMONS", "ATTRIBUTION 4.0 INTERNATIONAL"]),
    ("MPL",  ["MOZILLA PUBLIC LICENSE"]),
]

VERSION_TOKENS = [
    ("3", ["VERSION 3", "VERSAO 3", "VERSION 3,"]),
    ("2.1", ["VERSION 2.1", "VERSAO 2.1"]),
    ("2.0", ["VERSION 2.0", "VERSAO 2.0", "VERSION 2,0"]),
    ("2", ["VERSION 2", "VERSAO 2"]),
    ("1.3", ["VERSION 1.3", "VERSAO 1.3"]),
]

OR_LATER = ["ANY LATER VERSION", "QUALQUER VERSAO POSTERIOR",
            "CUALQUIER VERSION POSTERIOR"]

# --- scope layer (new in p474): one file, several grants, scoped to subtrees ---
SPLIT_MARKERS = [
    "DUAS LICENCAS", "DOS LICENCIAS", "TWO LICENSES", "TWO LICENCES",
    "NOT ONE WORK AND IS NOT UNDER ONE LICENSE",
    "USA DUAS LICENCAS", "THIS REPOSITORY USES TWO",
    "ESTE REPOSITORIO USA DUAS",
]
NONCOMMERCIAL = ["CC BY-NC", "BY-NC", "NONCOMMERCIAL", "NON-COMMERCIAL",
                 "NAO COMERCIAL", "NO COMERCIAL"]
UNLICENSED_RESERVATION = [
    "NAO SAO COBERTOS", "NAO LICENCIADOS", "NOT LICENSED",
    "DOES NOT HOLD THOSE COPYRIGHTS", "DOES NOT RELICENSE",
    "NOT PART OF THIS GRANT", "NO OTHER EXPRESS OR IMPLIED LICENSES",
]

_FOLD = str.maketrans("ÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇÑáàâãäéèêëíìîïóòôõöúùûüçñ",
                      "AAAAAEEEEIIIIOOOOOUUUUCNaaaaaeeeeiiiiooooouuuucn")

def _norm(text):
    return text.translate(_FOLD).upper()

def read_title(payload: str):
    """Return (family, version, or_later) from the title block, any language."""
    head = _norm("\n".join([l for l in payload.splitlines() if l.strip()][:6]))
    body = _norm(payload)
    family = None
    for fam, needles in TITLES:
        if any(n in head for n in needles):
            family = fam
            break
    version = None
    if family:
        for ver, needles in VERSION_TOKENS:
            if any(n in head for n in needles):
                version = ver
                break
    or_later = family in ("GPL", "LGPL", "AGPL") and any(n in body for n in OR_LATER)
    return family, version, or_later

def read_scope(payload: str, family=None):
    """Return scope class. SPLIT = several grants scoped to subtrees in one file.

    The `reserved and nc` fallback fires ONLY when the title block yielded no
    family. Measured reason (p474 defect 1): a standard GPL-2.0 body contains
    both "noncommercial" (section 3c) and "not licensed" (section 2), so the
    fallback graded `ipti/br.tag` -- a plain whole-work GPL-2.0 -- as
    SPLIT_SCOPE. When a title block names a known whole-work licence, its own
    clauses belong to that licence and are not a split-scope declaration.
    """
    body = _norm(payload)
    split = any(m in body for m in SPLIT_MARKERS)
    nc = any(m in body for m in NONCOMMERCIAL)
    reserved = any(m in body for m in UNLICENSED_RESERVATION)
    if split or (family is None and reserved and nc):
        return "SPLIT_SCOPE", {"noncommercial_part": nc, "reserved_part": reserved}
    return "WHOLE_WORK", {"noncommercial_part": nc, "reserved_part": reserved}

def grade(payload: str):
    fam, ver, orl = read_title(payload)
    scope, flags = read_scope(payload, family=fam)
    return {"family": fam, "version": ver, "or_later": orl,
            "scope": scope, **flags,
            # a single SPDX-ish cell is only sound for a whole-work grant
            "single_cell_sound": scope == "WHOLE_WORK" and fam is not None}
