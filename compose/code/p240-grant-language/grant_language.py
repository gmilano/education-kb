#!/usr/bin/env python3
"""p240-grant-language — the axis 239 passes of grant reading never recorded: LANGUAGE.

p228-p239 spent twelve passes establishing that a licence must be READ FIRST-HAND from
`raw.githubusercontent.com` rather than taken from the GitHub API field.  That instrument
is sound and this pass used it on 40 repositories.  What none of those passes recorded is
the LANGUAGE of the payload they read.

Measured this pass, on the 35 grants read first-hand:

    35 payloads read
    34 Latin-script (MIT/Apache/GPL/AGPL template texts, 511 B - 35 149 B)
     1 NON-ENGLISH: heronerar/OpenGaokao, LICENSE, 15 992 B, main @ a75b65aaa494
       -> 4 466 of 4 807 letters are CJK (92.9%)
       -> first clause: 禁止商业使用  ("commercial use is prohibited")
       -> the payload itself states it is NOT an OSI-approved licence
       -> lib/license_family.sh BEFORE p240:  commercial_use_ok -> ALLOWED

That last line is the finding.  The shared classifier's commercial branch is a token
match, and every token in it was English.  A payload that prohibits commercial use in
Chinese returned the same verdict as a payload that grants it.  P312 fixed exactly this
shape for `CC-BY-NC` -- a family whose NAME says NonCommercial returning ALLOWED -- and
the fix did not travel across languages because nothing had ever handed the classifier a
non-English payload.

WHY THE TOKEN LIST IS NOT THE FIX.  p240 extended the list (zh/ja/ko/es/pt/fr/de/it) and
that closes the specimen, but a token list is a closed vocabulary over an open world: the
next restriction will arrive in a language the list does not carry, and it will again be
INVISIBLE rather than wrong.  This instrument asks the other question --

    is this payload in a script the token match cannot be trusted over?

-- and answers it from the text itself, with no vocabulary at all.  A payload that is
non-Latin AND fires no known restriction token is reported `NON-ENGLISH-GRANT-UNREAD`,
which is a REFUSAL TO CLEAR, not a verdict of permissive.  An unread grant stops being
indistinguishable from a permissive one.

Threshold: NON_LATIN_PCT = 20.0% of LETTERS (not of bytes -- a UTF-8 byte count inflates
every non-Latin script by 2-3x and would make the threshold a function of the encoding).
Measured separation on this pass's 35: the one non-English payload is at 92.9% and the
next highest is 0.0%, so the interval (0, 92.9) is UNMEASURED and stated as such.  20.0 is
set low deliberately: this gate's error cost is asymmetric.  A false `UNREAD` costs one
human read; a false `CLEAR` costs the deliverable.

No network.  Reads one payload and classifies it.
"""
import os
import sys
import unicodedata

NON_LATIN_PCT = 20.0

# Restriction phrases, by language.  Kept in step with `lib/license_family.sh`'s
# commercial branch ON PURPOSE: two lists that drift are P255 (three instruments, three
# answers, one payload).  T272: printable via `--reach`, so the next pass EXTENDS it
# instead of copying it.
RESTRICTION_TOKENS = {
    "zh": ("禁止商业使用", "禁止商用", "非商业使用", "非商业性使用", "仅限个人非商业",
           "商业使用必须", "商业用途需", "商业用途请", "不得用于商业"),
    "ja": ("商用利用禁止", "商用利用は禁止", "非営利"),
    "ko": ("비상업적",),
    "es": ("uso no comercial", "usos no comerciales", "fines no comerciales",
           "prohibido el uso comercial"),
    "pt": ("uso nao comercial", "uso não comercial", "fins nao comerciais",
           "fins não comerciais", "proibido o uso comercial"),
    "fr": ("usage non commercial", "fins non commerciales", "à des fins non commerciales"),
    "de": ("nicht-kommerziell", "nicht kommerzielle nutzung", "keine kommerzielle nutzung"),
    "it": ("uso non commerciale",),
    "en": ("non-commercial", "noncommercial", "not-for-profit", "non-profit purposes",
           "obtain a commercial license", "commercial licence must"),
}

_SCRIPT_KEYS = ("CJK", "HIRAGANA", "KATAKANA", "HANGUL", "CYRILLIC", "GREEK",
                "ARABIC", "HEBREW", "DEVANAGARI", "THAI", "LATIN")


def script_of(ch):
    """Unicode script family of one character, by NAME, never by codepoint range.

    A range table is a second source of truth that goes stale; `unicodedata` ships with
    the interpreter and is the one this KB already depends on.
    """
    try:
        name = unicodedata.name(ch)
    except ValueError:
        return "OTHER"
    for key in _SCRIPT_KEYS:
        if key in name:
            return key
    return "OTHER"


def script_profile(text):
    """-> (letters, non_latin_letters, pct, dominant_non_latin_script)

    Counts LETTERS, so punctuation, digits and the licence's own formatting cannot move
    the ratio.  A grant is mostly prose; its letters are what carries the grant.
    """
    letters = [c for c in text if c.isalpha()]
    counts = {}
    non_latin = 0
    for c in letters:
        s = script_of(c)
        if s != "LATIN":
            non_latin += 1
            counts[s] = counts.get(s, 0) + 1
    pct = round(100.0 * non_latin / len(letters), 1) if letters else 0.0
    dominant = max(counts, key=counts.get) if counts else "LATIN"
    return len(letters), non_latin, pct, dominant


def restrictions_found(text):
    """-> sorted list of "lang:token" for every restriction phrase present."""
    low = text.lower()
    hits = []
    for lang, tokens in RESTRICTION_TOKENS.items():
        for t in tokens:
            if t in low:
                hits.append("%s:%s" % (lang, t))
    return sorted(hits)


def verdict(text):
    """-> (verdict, detail)

    LATIN-SCRIPT                  the English/Latin token match applies; nothing to add.
    NON-ENGLISH-GRANT-RESTRICTED  non-Latin, and a known restriction phrase fires.
    NON-ENGLISH-GRANT-UNREAD      non-Latin, and NO known phrase fires.  This is a
                                  REFUSAL TO CLEAR: the payload has not been read by any
                                  vocabulary this KB owns, and silence is not permission.
    """
    letters, non_latin, pct, dominant = script_profile(text)
    hits = restrictions_found(text)
    if pct < NON_LATIN_PCT:
        return "LATIN-SCRIPT", {
            "letters": letters, "non_latin": non_latin, "pct": pct,
            "dominant": "LATIN", "restrictions": hits,
        }
    v = "NON-ENGLISH-GRANT-RESTRICTED" if hits else "NON-ENGLISH-GRANT-UNREAD"
    return v, {
        "letters": letters, "non_latin": non_latin, "pct": pct,
        "dominant": dominant, "restrictions": hits,
    }


def may_publish(text):
    """True only when the payload is clearable WITHOUT a human read of a foreign text."""
    return verdict(text)[0] == "LATIN-SCRIPT"


def main(argv):
    if len(argv) >= 2 and argv[1] == "--reach":
        total = sum(len(v) for v in RESTRICTION_TOKENS.values())
        print("languages=%d tokens=%d threshold=%.1f%%-of-letters"
              % (len(RESTRICTION_TOKENS), total, NON_LATIN_PCT))
        for lang in sorted(RESTRICTION_TOKENS):
            print("--- %s" % lang)
            for t in RESTRICTION_TOKENS[lang]:
                print("    %s" % t)
        return 0
    if len(argv) < 2:
        sys.stderr.write("usage: grant_language.py <payload-path> | --reach\n")
        return 2
    path = argv[1]
    if not os.path.exists(path):
        sys.stderr.write("no such payload: %s\n" % path)
        return 2
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    v, d = verdict(text)
    print("%s\t%s\tletters=%d non_latin=%d (%.1f%%) dominant=%s"
          % (v, os.path.basename(path), d["letters"], d["non_latin"], d["pct"], d["dominant"]))
    for r in d["restrictions"]:
        print("  - restriction: %s" % r)
    return 0 if v == "LATIN-SCRIPT" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
