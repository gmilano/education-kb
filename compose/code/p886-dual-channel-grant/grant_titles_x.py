"""p886 — the licence-title rows this KB's classifier was missing, found by
running `885-G1`'s own acceptance test against the shelves it audits.

Why this exists
---------------
`885-G1` (p885) asks that every shelved row carry a licence verdict from TWO
channels: the `search/repositories` metadata field AND the licence bytes on the
`--symref`-resolved default branch. p886 ran that test over all 163 shelf rows and
the gate disagreed with the shelf on 15 of them.

NONE of the 15 was a shelf error. Every one was an INSTRUMENT error, and they fail
in the direction that is hardest to notice -- the gate reports "no grant" or
"unrecognised" on a row whose grant the shelf already byte-read and recorded
correctly. An unattended gate of that quality does not verify a shelf; it degrades
it. The four title families below are the classifier half of the repair.

1. IBERIAN GNU TITLES.  `portabilis/i-diario` carries the AGPL-3.0 body in
   PORTUGUESE -- `LICENÇA PÚBLICA GERAL AFFERO GNU`, `Versão 3, 19 de novembro de
   2007`. `repos/foundations.md` records it correctly *because p878 searched in
   Portuguese and a human read the bytes*; `classify_grant.py` returns
   `no recognised licence title`. This is `883-G2`'s class (the MulanPSL fullwidth
   comma) in a new language, and it is not incidental which language: this KB's
   LATAM supply is exactly the supply most likely to ship a translated GNU body,
   so the abstention is biased against the region the rotation prompt asks to
   serve as well as any other.

   The earliest-title rule stays sound in both languages for the same structural
   reason it is sound in English: `AFFERO` / `MENOR` / `REDUCIDA` sit BETWEEN the
   invariant head of the title and `GNU`, so the three GNU titles cannot overlap
   as strings and the GPL pattern cannot match an AGPL body.

2. ODbL.  `withmarbleapp/os-taxonomy` is a share-alike *database* licence. Both
   shelves already flag it in red as "not a code licence", but the classifier
   abstained, so the gate could not corroborate the flag it most needs to.

3. BARE-TOKEN GRANTS.  `frappe/education` ships a 19-byte `license.txt` reading
   `License: GNU GPL V3`. There is no licence body to classify. That is a real
   declaration and a real copyleft obligation, and it must not be reported as an
   absence -- but it must also not be reported with the same confidence as a
   byte-read body, so it returns a DISTINCT family suffix (`-DECLARED`) rather
   than being silently folded into `GPL-3.0`.

4. ADDITIONAL-TERMS RIDERS.  `opendatalab/MinerU` is Apache-2.0 "subject to the
   additional terms below", which add a commercial-licence threshold and a hosted
   attribution obligation. `agents/top.md` already warns that a substring grep for
   `additional terms` false-positives on 100% of Apache-2.0 bodies, because
   Apache-2.0 §5 contains the phrase "without any additional terms or conditions".
   That warning is correct and it is why the pattern here is anchored on the
   SUBORDINATING construction ("subject to the additional terms"), never on the
   bare phrase. The `p872` false-positive set is carried as a control below.
"""
import re

# (family, pattern). Earliest match in document order wins, per p227.
TITLES_X = [
    # --- 1. Iberian GNU titles ------------------------------------------------
    # Accents are optional at every position: translated bodies in the wild appear
    # both with and without them, and a hard accent requirement reproduces the
    # very false absence this row removes.
    ("AGPL-3.0", r"LICEN[ÇC]A\s+P[ÚU]BLICA\s+GERAL\s+AFFERO\s+GNU"),
    ("AGPL-3.0", r"LICEN[CS]IA\s+P[ÚU]BLICA\s+GENERAL\s+AFFERO\s+(?:DE\s+)?GNU"),
    ("LGPL",     r"LICEN[ÇC]A\s+P[ÚU]BLICA\s+GERAL\s+MENOR\s+GNU"),
    ("LGPL",     r"LICEN[CS]IA\s+P[ÚU]BLICA\s+GENERAL\s+REDUCIDA\s+(?:DE\s+)?GNU"),
    ("GPL",      r"LICEN[ÇC]A\s+P[ÚU]BLICA\s+GERAL\s+GNU"),
    ("GPL",      r"LICEN[CS]IA\s+P[ÚU]BLICA\s+GENERAL\s+(?:DE\s+)?GNU"),
    # --- 2. Open Data Commons -------------------------------------------------
    ("ODbL-1.0", r"Open\s+Data\s+Commons\s+Open\s+Database\s+Licen[cs]e"),
    ("ODbL-1.0", r"\bODbL\b"),
    ("ODC-BY-1.0", r"Open\s+Data\s+Commons\s+Attribution\s+Licen[cs]e"),
]

# Iberian version lines, so a translated GNU body resolves to an exact identifier
# instead of `GPL-?` / `LGPL-?`.
VER3_X = re.compile(r"Vers[ãa]o\s+3,?\s+19\s+de\s+novembro\s+de\s+2007"
                    r"|Versi[óo]n\s+3,?\s+19\s+de\s+noviembre\s+de\s+2007", re.I)
VER2_X = re.compile(r"Vers[ãa]o\s+2,?\s+junho\s+de\s+1991"
                    r"|Versi[óo]n\s+2,?\s+junio\s+de\s+1991", re.I)
VER21_X = re.compile(r"Vers[ãa]o\s+2\.1,?\s+fevereiro\s+de\s+1999"
                     r"|Versi[óo]n\s+2\.1,?\s+febrero\s+de\s+1999", re.I)

# --- 3. bare-token grants ----------------------------------------------------
# Deliberately requires the WHOLE payload to be short. A long body that merely
# mentions "GPL V3" in passing is not a bare-token grant, and treating it as one
# would be p227's substring trap again.
BARE_TOKEN_MAX_BYTES = 200
_BARE = [
    ("AGPL-3.0", r"\bAGPLv?3\b|\bAGPL[- ]3\.0\b|GNU\s+AGPL"),
    ("GPL-3.0",  r"\bGPLv?3\b|\bGPL[- ]?V?3(\.0)?\b"),
    ("GPL-2.0",  r"\bGPLv?2\b|\bGPL[- ]?V?2(\.0)?\b"),
    ("LGPL-3.0", r"\bLGPLv?3\b"),
    ("Apache-2.0", r"\bApache[- ]2(\.0)?\b"),
    ("MIT",      r"\bMIT\b"),
    ("BSD-3-Clause", r"\bBSD[- ]3\b"),
    ("ISC",      r"\bISC\b"),
]
# AGPL before GPL: "AGPL" contains no "GPLv3" token but "GNU AGPL" would fall to
# the GPL row if GPL were tested first on some spellings.
_BARE_C = [(f, re.compile(p, re.I)) for f, p in _BARE]


def bare_token_grant(body):
    """A payload too short to be a licence body, carrying a licence NAME.

    Returns (family, note) or None. The family carries a `-DECLARED` suffix so no
    downstream consumer can mistake a one-line declaration for a byte-read body.
    """
    raw = body.strip()
    if not raw or len(raw.encode("utf-8")) > BARE_TOKEN_MAX_BYTES:
        return None
    # A real licence body always carries operative language; a declaration does not.
    if re.search(r"permission\s+is\s+hereby|terms\s+and\s+conditions|"
                 r"redistribution\s+and\s+use", raw, re.I):
        return None
    for fam, rx in _BARE_C:
        if rx.search(raw):
            return (fam + "-DECLARED",
                    "%d-byte payload declares a licence by NAME; no body to read"
                    % len(raw.encode("utf-8")))
    return None


# --- 4. additional-terms rider ----------------------------------------------
# Anchored on the SUBORDINATING construction. The bare phrase "additional terms"
# appears in Apache-2.0 §5 ("without any additional terms or conditions") and
# therefore matches 100% of Apache-2.0 bodies -- p872 measured that on seven of
# this KB's own rows and correctly discarded the flag rather than publishing it.
RIDER = re.compile(
    r"subject\s+to\s+the\s+additional\s+terms"
    r"|supplemented\s+by\s+these\s+additional\s+terms"
    r"|additional\s+terms\s+below"
    r"|except\s+to\s+the\s+extent\s+expressly\s+modified", re.I)


def additional_terms_rider(body):
    """True when a body SUBORDINATES its own grant to extra terms."""
    return bool(RIDER.search(body))
