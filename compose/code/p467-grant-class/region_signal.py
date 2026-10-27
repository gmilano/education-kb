#!/usr/bin/env python3
"""p467 -- a REGION SIGNAL over the probed population, with its limits declared.

The ingest brief is explicit that an unplaced finding is worth less than a
placed one. This base's region cells are mostly argued from prose; nothing here
has ever MEASURED a region distribution over a supply population. This does, on
one axis that can be read first-hand from the payload bytes already fetched: the
SCRIPT AND LANGUAGE the project documents itself in.

🔴 What this is NOT. Language is not domicile. A Chinese-language README does not
prove a Chinese maintainer, English does not prove North America, and a
multinational project documents itself in English wherever it sits. So this axis
yields `UNPLACED` for English, which is the single largest bucket by
construction, and it is published as a SIGNAL with a denominator, never as a
market share. Its one defensible use is the direction the brief cares about:
where NON-English education supply concentrates, and which regions return
nothing.
"""
import re, sys, os, collections

CJK   = re.compile(r"[一-鿿]")
HANGUL= re.compile(r"[가-힯]")
KANA  = re.compile(r"[぀-ヿ]")
CYR   = re.compile(r"[Ѐ-ӿ]")
ARAB  = re.compile(r"[؀-ۿ]")
DEVA  = re.compile(r"[ऀ-ॿ]")
THAI  = re.compile(r"[฀-๿]")

# Latin-script languages, detected on stopwords in running prose. Portuguese and
# Spanish are kept APART because only one of them places LATAM unambiguously:
# Portuguese outside Portugal is Brazil, while Spanish is LATAM *or* Spain, so
# Spanish alone yields `LATAM|EMEA` and is counted as its own bucket rather than
# being assigned.
# 🔴 THE FIRST CUT OF THIS LIST WAS WRONG IN THE SAME DIRECTION ELEVEN TIMES,
# and it was caught by reading the rows it placed, not by the counts.
#
#   * Turkish fired on 11 ENGLISH READMEs, including `ucfopen/UDOIT`
#     (University of Central Florida) and `GarethManning/education-agent-skills`
#     (British English). Cause: the stopword `\bve\b`. In English prose the
#     apostrophe is a word boundary, so "we've", "I've" and "you've" all contain
#     a standalone token `ve`. A two-letter stopword cannot be used at all.
#   * Polish fired on `studentinsights` because its stopword list contained
#     `jest` -- which is the name of the JavaScript test runner the project uses.
#   * Korean fired on a Stanford repository on a single incidental hangul
#     character.
#
# The remedy is the same in all three cases: a language is attributed only on
# tokens that CANNOT occur in English text -- diacritics and language-specific
# orthography -- and never on short function words. Scripts need a count floor,
# not a single character.
LATIN = [
    ("pt", "LATAM",      r"(não|são|também|código|aprendizagem|ensino|você|gratuita|plataforma|ção\b)"),
    ("es", "LATAM|EMEA", r"(ñ|aprendizaje|educación|español|usuario|gratuito|enseñanza|¿|¡)"),
    ("de", "EMEA",       r"(ü\w|ö\w|ä\w|ß|\bund\b|\bnicht\b|\bfür\b|Schule|Lernen)"),
    ("fr", "EMEA",       r"(é\w|è\w|ê\w|à\s|vie scolaire|apprentissage|élèves|logiciel|être)"),
    ("it", "EMEA",       r"(apprendimento|scuola|perché|più\b|della\s|degli\s)"),
    ("pl", "EMEA",       r"(ł|ą|ę|ż|ź|ć|ń\w|ś\w|szkoł)"),
    ("tr", "EMEA",       r"(için|öğrenc|ğ|ş\w|ı\w|Türk)"),
    ("nl", "EMEA",       r"(\bhet\b|\been\b|onderwijs|leren\b|\bvoor\b)"),
]
LATIN_FLOOR = 4  # hits of NON-English orthography, not of function words

def attribute(text):
    """-> (language, region, basis). First match wins; CJK before Latin."""
    # A script needs a COUNT, not a character: one incidental glyph is noise.
    SCRIPT_FLOOR = 8
    han, hang, kana = len(CJK.findall(text)), len(HANGUL.findall(text)), len(KANA.findall(text))
    cyr, arab = len(CYR.findall(text)), len(ARAB.findall(text))
    deva, thai = len(DEVA.findall(text)), len(THAI.findall(text))
    best = max(han, hang, kana, cyr, arab, deva, thai)
    if best >= SCRIPT_FLOOR:
        if hang == best:
            return "ko", "APAC", f"{hang} hangul"
        if kana == best or (kana >= SCRIPT_FLOOR and han >= SCRIPT_FLOOR):
            return "ja", "APAC", f"{kana} kana + {han} han"
        if han == best:
            return "zh", "APAC", f"{han} han"
        if cyr == best:
            return "ru", "EMEA", f"{cyr} cyrillic"
        if arab == best:
            return "ar", "EMEA", f"{arab} arabic"
        if deva == best:
            return "hi", "APAC", f"{deva} devanagari"
        if thai == best:
            return "th", "APAC", f"{thai} thai"
    for lang, region, pat in LATIN:
        hits = len(re.findall(pat, text))
        if hits >= LATIN_FLOOR:
            return lang, region, f"{hits} {lang} non-English orthography hits"
    return "en", "UNPLACED", "english or no non-English signal"


def main():
    index, payroot, gc = sys.argv[1], sys.argv[2], sys.argv[3]
    cls = {}
    for line in open(gc):
        f = line.rstrip("\n").split("\t")
        if len(f) > 8:
            cls[f[0]] = (f[1], f[8])
    reg = collections.Counter(); lang = collections.Counter()
    rows = []
    for line in open(index):
        addr, which = line.rstrip("\n").split("\t")
        p = os.path.join(payroot, addr, "readme")
        if which == "NONE" or not os.path.exists(p):
            l, r, b = "?", "NO-README", "no readme at any path"
        else:
            # The first 4 000 characters: a README's own prose, before the
            # badge walls and English install sections that follow.
            l, r, b = attribute(open(p, encoding="utf-8", errors="replace").read()[:4000])
        stars, gclass = cls.get(addr, ("-1", "?"))
        rows.append((addr, stars, l, r, gclass, b))
        reg[r] += 1; lang[l] += 1
    print("addr\tstars\tlang\tregion_signal\tgrant_class\tbasis")
    for r in sorted(rows, key=lambda x: (x[3], -int(x[1]))):
        print("\t".join(map(str, r)))
    tot = sum(reg.values())
    print(f"\nregion signal over n={tot}", file=sys.stderr)
    for k, v in reg.most_common():
        print(f"{k}\t{v}\t{v/tot:.2f}", file=sys.stderr)
    print("\nlanguages", file=sys.stderr)
    for k, v in lang.most_common():
        print(f"{k}\t{v}", file=sys.stderr)
    # the cut that matters: sellability inside each placed region
    print("\nplaced rows by region x sellable", file=sys.stderr)
    agg = collections.defaultdict(lambda: [0, 0])
    for _, _, _, r, gc_, _ in rows:
        agg[r][0] += 1
        if gc_ in ("PERMISSIVE", "PUBLIC_DOMAIN"):
            agg[r][1] += 1
    for k in sorted(agg):
        n, s = agg[k]
        print(f"{k}\tn={n}\tsellable={s}\t{s/n:.2f}", file=sys.stderr)

if __name__ == "__main__":
    main()
