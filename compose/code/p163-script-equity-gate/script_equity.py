#!/usr/bin/env python3
"""p163-script-equity-gate — ACTION IG.

Faithful Python replication of OpenOLAT's two length/quality gates on the
GRADED path, so their behaviour on non-Latin scripts can be measured without
a JVM:

  src/main/java/org/olat/core/commons/services/ai/essay/GibberishPreFilter.java
  src/main/java/org/olat/core/commons/services/ai/essay/AiGradingTier.java

Read at openolat/openolat HEAD e4be14f0d1bb5840cba54136f753d97e4bfa5b60.

Fidelity rules, because the bias we are hunting lives in exactly these details:

  * Java String.length() and String.substring() count UTF-16 CODE UNITS, not
    code points. An astral character is TWO units. We model the string as an
    explicit UTF-16 unit sequence.
  * Java Character.isLetter(cp) is true for general categories Lu, Ll, Lt,
    Lm, Lo -- and FALSE for Mn and Mc, the combining marks that carry the
    vowels of Devanagari and Thai.
  * GibberishPreFilter divides a CODE-POINT letter count by a CODE-UNIT
    total. That mixed denominator is reproduced, not corrected.
  * Declared approximation: Java's toLowerCase(Locale.ROOT) is modelled by
    str.lower(). The two agree on every script measured here (lowercasing is
    the identity on Han, Kana, Hangul, Arabic, Devanagari and Thai), so the
    approximation cannot move any non-Latin verdict.

Usage:
  script_equity.py              -> run the corpus, write TSV to stdout
  script_equity.py --self-test  -> see test_script_equity.py instead
"""

import math
import sys
import unicodedata

# ---------------------------------------------------------------- constants, from the Java source

ENTROPY_THRESHOLD = 1.5
MIN_LETTER_RATIO = 0.45
MIN_LENGTH_FOR_ENTROPY_CHECK = 15

SHORT_WORD_THRESHOLD = 150
MEDIUM_WORD_THRESHOLD = 400

LETTER_CATEGORIES = {"Lu", "Ll", "Lt", "Lm", "Lo"}


# ---------------------------------------------------------------- UTF-16 model

def utf16_units(text):
    """The string as a list of UTF-16 code units, the way Java stores it."""
    units = []
    for ch in text:
        cp = ord(ch)
        if cp > 0xFFFF:
            cp -= 0x10000
            units.append(0xD800 + (cp >> 10))
            units.append(0xDC00 + (cp & 0x3FF))
        else:
            units.append(cp)
    return units


def code_points_of(units):
    """Decode a UTF-16 unit list back to code points, as codePointAt() walks it."""
    out = []
    i = 0
    n = len(units)
    while i < n:
        u = units[i]
        if 0xD800 <= u <= 0xDBFF and i + 1 < n and 0xDC00 <= units[i + 1] <= 0xDFFF:
            out.append(0x10000 + ((u - 0xD800) << 10) + (units[i + 1] - 0xDC00))
            i += 2
        else:
            out.append(u)
            i += 1
    return out


def is_java_letter(cp):
    """Character.isLetter(int): true for Lu, Ll, Lt, Lm, Lo only."""
    try:
        return unicodedata.category(chr(cp)) in LETTER_CATEGORIES
    except ValueError:
        return False


def is_java_whitespace(cp):
    """Character.isWhitespace(int), close enough for the corpus here."""
    ch = chr(cp)
    if ch in (" ", " ", " "):
        return False  # non-breaking: Java says NOT whitespace
    return ch.isspace()


# ---------------------------------------------------------------- GibberishPreFilter

def _letter_ratio(units):
    """letters counted per CODE POINT, divided by the CODE UNIT length."""
    if not units:
        return 0.0
    letters = sum(1 for cp in code_points_of(units) if is_java_letter(cp))
    return letters / len(units)


def _trigram_entropy(units):
    """Shannon entropy over 3-CODE-UNIT substrings."""
    if len(units) < 3:
        return 0.0
    counts = {}
    total = 0
    for i in range(0, len(units) - 2):
        tri = (units[i], units[i + 1], units[i + 2])
        counts[tri] = counts.get(tri, 0) + 1
        total += 1
    if total == 0:
        return 0.0
    entropy = 0.0
    for c in counts.values():
        p = c / total
        entropy -= p * (math.log(p) / math.log(2))
    return entropy


def gibberish_check(answer):
    """Returns (rejected: bool, reason: str|None, letter_ratio, entropy).

    letter_ratio / entropy are None where the Java code returns before
    computing them, so a measurement is never reported that the gate did
    not actually take.
    """
    if answer is None or answer.strip() == "":
        return (False, None, None, None)

    normalised = "".join(answer.split())  # Java: replaceAll("\\s+", "")
    units = utf16_units(normalised)

    if len(units) < MIN_LENGTH_FOR_ENTROPY_CHECK:
        return (False, "below-min-length", None, None)

    ratio = _letter_ratio(units)
    if ratio < MIN_LETTER_RATIO:
        return (True, "letter-ratio", ratio, None)

    entropy = _trigram_entropy(utf16_units(normalised.lower()))
    if entropy < ENTROPY_THRESHOLD:
        return (True, "entropy", ratio, entropy)

    return (False, None, ratio, entropy)


# ---------------------------------------------------------------- AiGradingTier

def _is_cjk(cp):
    """The three ranges the Java source actually lists."""
    return (
        (0x3040 <= cp <= 0x30FF)    # Hiragana + Katakana
        or (0x4E00 <= cp <= 0x9FFF)  # CJK Unified Ideographs
        or (0xAC00 <= cp <= 0xD7AF)  # Hangul Syllables
    )


def count_words(text):
    """AiGradingTier.countWords, including its CJK branch. Returns (words, cjk_ratio, branch)."""
    units = utf16_units(text)
    cjk = 0
    total = 0
    for cp in code_points_of(units):
        if not is_java_whitespace(cp):
            total += 1
            if _is_cjk(cp):
                cjk += 1
    ratio = (cjk / total) if total else 0.0
    if total > 0 and ratio > 0.30:
        return (max(1, total // 3), ratio, "cjk-charcount/3")
    return (len(text.strip().split()), ratio, "whitespace-split")


def classify(answer, medium_word_threshold=MEDIUM_WORD_THRESHOLD):
    if answer is None or answer.strip() == "":
        return ("SHORT", 0, 0.0, "blank")
    words, ratio, branch = count_words(answer)
    if words <= SHORT_WORD_THRESHOLD:
        tier = "SHORT"
    elif words <= medium_word_threshold:
        tier = "MEDIUM"
    else:
        tier = "LONG"
    return (tier, words, ratio, branch)
