"""
p164 / ACTION IL — P163-A steps 2 and 3 applied to the p163 replication.

Registered step 3: count Mn/Mc (combining marks) as letters for the ratio.
Carried step 2 (measured separately so each is attributable): count the
ratio's DENOMINATOR in code points rather than UTF-16 code units.

ACTION IL does not ask whether the fix helps the nine scripts — p163 predicted
that. It asks whether the fix COSTS the control: does treating combining marks
as letters let either negative control through?

FIDELITY NOTE (p164): upstream strips whitespace BEFORE the ratio
(`replaceAll("\\s+","")`), so the ratio is letters/non-whitespace-units. The
first p164 draft of this file omitted the strip and produced ratios that
disagreed with p163's recorded TSV (en 0.823 vs 0.976). Corrected here; the
pipeline below is base.gibberish_check with ONLY the ratio limb swapped.
"""
import unicodedata
import script_equity as base

MARK_CATEGORIES = {"Mn", "Mc"}


def is_letter_or_mark(cp):
    """P163-A step 3: a Mn/Mc code point is PART OF a letter, not symbol spam."""
    try:
        cat = unicodedata.category(chr(cp))
    except ValueError:
        return False
    return cat in base.LETTER_CATEGORIES or cat in MARK_CATEGORIES


def letter_ratio_units(units, *, marks_count=False, codepoint_denominator=False):
    if not units:
        return 0.0
    pred = is_letter_or_mark if marks_count else base.is_java_letter
    cps = list(base.code_points_of(units))
    letters = sum(1 for cp in cps if pred(cp))
    denom = len(cps) if codepoint_denominator else len(units)
    return letters / denom if denom else 0.0


def gibberish_check_patched(answer, *, marks_count=False, codepoint_denominator=False):
    """base.gibberish_check with ONLY the letter-ratio limb swapped.

    The empty guard, the whitespace strip, the min-length guard and the
    trigram-entropy limb are upstream's, untouched — so any change in verdict
    is attributable to the ratio change alone.
    Returns (rejected, reason, ratio, entropy) exactly as upstream does.
    """
    if answer is None or answer.strip() == "":
        return (False, None, None, None)

    normalised = "".join(answer.split())
    units = base.utf16_units(normalised)

    if len(units) < base.MIN_LENGTH_FOR_ENTROPY_CHECK:
        return (False, "below-min-length", None, None)

    ratio = letter_ratio_units(units, marks_count=marks_count,
                               codepoint_denominator=codepoint_denominator)
    if ratio < base.MIN_LETTER_RATIO:
        return (True, "letter-ratio", ratio, None)

    entropy = base._trigram_entropy(base.utf16_units(normalised.lower()))
    if entropy < base.ENTROPY_THRESHOLD:
        return (True, "entropy", ratio, entropy)

    return (False, None, ratio, entropy)


VARIANTS = {
    "upstream": dict(marks_count=False, codepoint_denominator=False),
    "step2": dict(marks_count=False, codepoint_denominator=True),
    "step3": dict(marks_count=True, codepoint_denominator=False),
    "step2+3": dict(marks_count=True, codepoint_denominator=True),
}
