#!/usr/bin/env python3
"""
origin_strip.py — origin evidence over STRIPPED README text.  (instrument, pass p899)

Acceptance test it was written against: intel/open-gaps.md `898-G1`.

  "No origin placement may be written from a score computed over unstripped text, and no
   placement may rest on a repository *name*. The instrument strips fenced code, inline code
   and URLs, then scores *exclusive* markers only."

WHY THIS EXISTS
---------------
p898 scored `luumlabs/aula` at ES=64, PT=83 on raw README bytes and would have published the
KB's first LATAM-origin headline off it. After stripping, the same README scores PT*=0, ES*=1:
the 147 raw hits were `.com` inside URLs and romance-looking tokens inside fenced code. The
repo's README is English; `aula` is merely a Spanish/Portuguese *word*.

The failure mode is asymmetric and that is the dangerous part. This KB's standing finding is
that LATAM-origin supply is near zero, so a false positive lands exactly where the KB has the
least evidence and a reader has no counterexample. Hence: exclusive markers only, stripped text
only, and `aula` is pinned below as a known-good NEGATIVE fixture.

WHAT IT DOES NOT DO
-------------------
It does not establish origin. It yields *content evidence* for origin, which per `884-G5` is
the only channel still open to this session: `gh api users/{login}` is 403 and `search/users`
returns 20 fields with no `location`, `company` or `name` among them. A LANG verdict is a
hint to be corroborated, never a placement on its own. Absence of markers means ENGLISH-OR-
UNKNOWN and is NEVER evidence of Anglophone origin — most of the world publishes in English.
"""
import re, sys, unicodedata

# --- the stripper -------------------------------------------------------------------------
FENCE  = re.compile(r"```.*?```|~~~.*?~~~", re.S)
INLINE = re.compile(r"`[^`\n]*`")
URL    = re.compile(r"https?://\S+|www\.\S+|\b[\w.-]+\.(?:com|org|net|io|dev|ai|br|mx|cn|jp|kr|in|uk|eu)\b",
                    re.I)
IMG    = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINKD  = re.compile(r"\[[^\]]*\]\([^)]*\)")
HTML   = re.compile(r"<[^>]+>")
BADGE  = re.compile(r"^\s*\[!\[.*$", re.M)

def strip(text: str) -> str:
    """Remove every span that carries no natural-language origin signal."""
    for pat in (FENCE, BADGE, IMG, LINKD, HTML, INLINE, URL):
        text = pat.sub(" ", text)
    return text

# --- exclusive markers only ---------------------------------------------------------------
# Each marker must be IMPOSSIBLE (or near enough) in English prose. Shared Romance tokens
# ("la", "de", "no", "con") are deliberately absent: they are what produced p898's 147
# false hits.
PT_EXCL = ["ã", "õ", "ç", "ção", "você", "não", "são", "está", "português", "aprendizagem",
           "ensino", "aluno", "professor", "conteúdo", "educação"]
ES_EXCL = ["ñ", "¿", "¡", "ción", "qué", "más", "español", "aprendizaje", "enseñanza",
           "alumno", "profesor", "educación", "también"]

SCRIPTS = {
    "CJK":       (0x4E00, 0x9FFF),
    "KANA":      (0x3040, 0x30FF),
    "HANGUL":    (0xAC00, 0xD7AF),
    "DEVANAGARI":(0x0900, 0x097F),
    "ARABIC":    (0x0600, 0x06FF),
    "CYRILLIC":  (0x0400, 0x04FF),
    "THAI":      (0x0E00, 0x0E7F),
}

def score(text: str) -> dict:
    low = text.lower()
    out = {"PT": sum(low.count(m) for m in PT_EXCL),
           "ES": sum(low.count(m) for m in ES_EXCL)}
    for name, (lo, hi) in SCRIPTS.items():
        out[name] = sum(1 for ch in text if lo <= ord(ch) <= hi)
    return out

# A marker count this low is noise (a stray accent, one borrowed word, an author's name).
THRESHOLD = 5

# A language SWITCHER ("English · Русский · 简体中文") or a supported-languages LIST
# ("हिन्दी Hindi · বাংলা Bengali · मराठी Marathi ...") is evidence of TRANSLATION or of a
# TARGET MARKET. It is not evidence of origin, and it is dense: every hit falls inside one
# short span. Real prose in a language is dispersed across the whole document. Measured on
# p899's own candidates: `virgiliojr94/book-to-skill` CYRILLIC=7 and
# `Orenda-Project/rumi-platform` DEVANAGARI=11 are both single-span, and both would have been
# published as regional placements without this test.
MIN_SPREAD = 0.10   # hits must span >=10% of the document to count as prose


def positions(text: str, cls: str) -> list:
    """Character offsets of every hit for one marker class."""
    if cls in SCRIPTS:
        lo, hi = SCRIPTS[cls]
        return [i for i, ch in enumerate(text) if lo <= ord(ch) <= hi]
    markers = PT_EXCL if cls == "PT" else ES_EXCL
    low, out = text.lower(), []
    for m in markers:
        start = 0
        while (i := low.find(m, start)) != -1:
            out.append(i)
            start = i + 1
    return sorted(out)


def spread(text: str, cls: str) -> float:
    """Fraction of the document the hits for `cls` span. 0.0 == all in one place."""
    p = positions(text, cls)
    if len(p) < 2 or not text:
        return 0.0
    return (p[-1] - p[0]) / len(text)


def verdict(sc: dict, text: str = None) -> str:
    hits = {k: v for k, v in sc.items() if v >= THRESHOLD}
    if not hits:
        return "ENGLISH-OR-UNKNOWN"
    # CJK vs KANA: Japanese READMEs carry both; kana is the discriminator.
    if hits.get("KANA", 0) >= THRESHOLD:
        hits.pop("CJK", None)
    if text is not None:
        dispersed = {k: v for k, v in hits.items() if spread(text, k) >= MIN_SPREAD}
        if not dispersed:
            top = max(hits, key=hits.get)
            return f"LANGUAGE-LIST({top}={hits[top]})"
        hits = dispersed
    top = max(hits, key=hits.get)
    return f"{top}={hits[top]}"


def analyse(raw: str) -> dict:
    s = strip(raw)
    sc = score(s)
    return {"raw": score(raw), "stripped": sc, "verdict": verdict(sc, s),
            "spread": {k: round(spread(s, k), 3) for k, v in sc.items() if v >= THRESHOLD}}

if __name__ == "__main__":
    data = open(sys.argv[1], encoding="utf-8", errors="replace").read()
    r = analyse(data)
    nz = lambda d: {k: v for k, v in d.items() if v}
    print(f"raw      : {nz(r['raw'])}")
    print(f"stripped : {nz(r['stripped'])}")
    print(f"VERDICT  : {r['verdict']}")
