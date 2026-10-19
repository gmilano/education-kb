#!/usr/bin/env python3
"""p314 — the pinned payloads for the UNTITLED-GRANT class, on two families.

🔴 THE DEFECT THIS ANSWERS, and `p313` found it without being able to measure it.
`p313` read [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub)
first-hand and recorded a `BSD-3-Clause` payload that is a **real, complete
grant** and carries **no title line and zero occurrences of the token `BSD`**.
Its note: *"the title channel returns `None` on the second and every body ladder
keyed on a family name returns nothing, because the token is not in the file."*
🔵 `p313` could not run a single classifier against it — the code channel was
refused in that session — so the blindness was **inferred from the payload's
shape**, never measured.

🟢 THE CODE CHANNEL IS OPEN IN THIS SESSION, so this instrument measures it.

🔴 AND THE CLASS IS BIGGER THAN `p313` COULD HAVE KNOWN. The same shape exists on
`MIT` — **the family that is more than a third of every licence cell this base
publishes** (`p311`'s own standing control). `crewAIInc/crewAI` serves the
complete, verbatim MIT grant body at `1 055` B and it:

  🔴 opens on the **copyright notice**, with no title line at all, and
  🔴 contains **zero occurrences of the token `MIT`** —

while a substring test of the form `"mit" in low`, which is this base's single
most-repeated defect class (`p306`'s `"affero" in low`, `p306`'s `"cc0" in low`),
returns **True** on this file for the wrong reason: it matches inside the word
*permit*, twice, in `"to permit persons"` and `"Permission is hereby granted"`.
🔵 So on one payload the correct answer is unreachable by a title channel and the
right answer is reachable by a broken one. **A classifier can be right here by
accident and this is the fixture that tells the two apart.**

🟢 WHAT THE SET IS FOR. Four payloads, two families, each family carrying a
TITLED and an UNTITLED shape so the arm reads a difference rather than a level:

  `MIT`           `educhain` titled · `crewAI` **untitled**
  `BSD-3-Clause`  `freeCodeCamp` titled · `jupyterhub` **untitled**

🔵 `ACTION p313-R` item 5 asks for exactly the `BSD-3-Clause` half of this and
says why — `301` published cells, and *"do not publish a coverage figure for the
family off one of them"*. The `MIT` half is this pass's own finding and it raises
the stake by two orders of magnitude.

🔵 The remaining rows are the payloads two other `p313-R` items need, pinned here
so neither item has to fetch anything: item 2a's `MPL-2.0` pair-mate and item 4's
four noncommercial notices.
"""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "fixtures")

# 🔵 Prefix + directory listing, NOT a literal filename — `p310`/`p311`'s
# convention, adopted rather than reinvented, and it is load-bearing: spelling a
# licence filename as a literal here makes `p283-ladder-case-audit` read this
# file as a one-rung licence-path ladder and the STANDING ratchet goes red.

# (prefix, canonical family, canonical commercial-use verdict, why it is here)
DECLARED = [
    ("mit-educhain", "MIT", "OK",
     "satvik314/educhain — the TITLED `MIT` control: the family name is the "
     "whole of the first line, which is the shape every title-keyed rung on this "
     "base was written against. `1 092` B, `e3321a1b62cd`. 🟢 It is in the set "
     "to establish that the arm's `MIT` readings are a property of the PAYLOAD "
     "SHAPE and not of the family."),
    ("mit-crewai", "MIT", "OK",
     "crewAIInc/crewAI — 🔴 **THE UNTITLED `MIT` PAYLOAD, AND THIS PASS'S "
     "HEADLINE.** `1 055` B, `28868731966f`. The grant body is the complete, "
     "verbatim MIT text; the file opens on the copyright notice and the family "
     "name appears **nowhere in it**. 🔴 A substring test nevertheless matches "
     "it — inside the word *permit* — so the family that holds more than a third "
     "of this base's published cells has a live payload on which a title channel "
     "is BLIND and a substring channel is RIGHT BY ACCIDENT."),
    ("bsd-3-clause-freecodecamp", "BSD-3-Clause", "OK",
     "freeCodeCamp/freeCodeCamp — the TITLED `BSD-3-Clause` control, `1 513` B, "
     "`e2a20708d0fd`. 🟢 `p313` read these exact bytes and this pass replicates "
     "them first-hand; the pin is `ACTION p313-R` item 5's first half."),
    ("bsd-3-clause-jupyterhub", "BSD-3-Clause", "OK",
     "jupyterhub/jupyterhub — 🔴 **the UNTITLED `BSD-3-Clause` payload**, "
     "`1 475` B, `7069c7e8d60e`, replicated first-hand this pass. No title line, "
     "zero `BSD` tokens, opening instead on the copyright declaration. 🔵 It is "
     "the one permissive row on this base's whole VERTICAL shelf, and `p313` "
     "recorded that no channel here can read it. 🟢 `ACTION p313-R` item 5's "
     "second half, and the reason the item forbids a one-fixture coverage figure "
     "for `301` cells."),
    ("bsd-3-clause-open-tutor-ai-ce", "BSD-3-Clause", "OK",
     "open-tutorai/open-tutor-ai-ce — 🔴 **the THIRD untitled payload, and the "
     "one that costs a studio something.** `1 531` B, `57c341d09920`, read "
     "first-hand this pass. It opens on the copyright declaration, carries all "
     "three clauses including the endorsement clause that makes it 3-Clause "
     "rather than 2-Clause, and contains **zero tokens of ANY licence family** — "
     "not `BSD`, not `MIT`, not `Apache`, not `Mozilla`, not `GNU`. 🟢 This is "
     "an EDUCATION-SPECIFIC AI tutoring platform, not infrastructure, and its "
     "grant is PERMISSIVE — exactly the supply this base exists to find. 🔴 And "
     "it is the supply an automated licence screen drops: no title, no family "
     "token, so the title channel abstains and `P250` turns the abstention into "
     "`PROHIBITED`. 🔵 The untitled shape is therefore not a curiosity of two "
     "infrastructure repositories; it reaches the vertical this base serves."),
    ("mit-ms-ai-agents", "MIT", "OK",
     "microsoft/ai-agents-for-beginners — `1 141` B, `c2cfccb812fe`. 🟡 A "
     "TITLED payload whose title line is **indented by four spaces**, which is a "
     "third distinct title SHAPE on one family (`educhain` bare, `OpenHands` "
     "parenthesised, this one indented). 🔵 It is in the set as the boundary "
     "case between the two arms: the family name IS present, so this is not an "
     "untitled payload, but a title rung anchored with `^` and no leading-space "
     "tolerance would miss it anyway. 🟢 Pinned so the next pass can measure "
     "that separately rather than conflating it with the untitled class."),
    ("mpl-2.0-common-voice", "MPL-2.0", "OK",
     "mozilla/common-voice — `16 726` B, `3f3d9e0024b1`, the pair-mate "
     "`ACTION p313-R` item 2a names. 🔴 It is the same number of bytes as the "
     "`MPL-2.0` fixture `p312` pinned and it is a DIFFERENT FILE "
     "(`fab3dd6bdab2`). 🟢 That makes it the control item 2a asks for in its own "
     "words — *«two payloads of EQUAL length can differ»* — and this base's "
     "`bytes` + `sha` ledger has no shape that would ever put the two rows side "
     "by side. 🔵 The residual difference after `p312`'s step 0b is the URL "
     "SCHEME, which is what step 0c now normalises."),
    ("cc-by-nc-nd-4.0-ud-portuguese-cintil", "CC-BY-NC-ND-4.0", "PROHIBITED",
     "UniversalDependencies/UD_Portuguese-CINTIL — `224` B, `73c169eb6bbf`, "
     "replicating `p313` exactly. 🔴 One sentence naming the family, then a "
     "pointer to where the terms actually live. 🟢 Here as an `is_this_a_grant?` "
     "positive: `ACTION p313-R` item 4."),
    ("cc-by-nc-nd-4.0-mzyphur", "CC-BY-NC-ND-4.0", "PROHIBITED",
     "mzyphur/responsible-ai-in-research-training — `1 470` B, `39b4d330a934`. "
     "🔴 The sharpest of the four: a hand-written PARAPHRASE that is not the "
     "licence it names, adding a prior-written-permission requirement and a "
     "mandatory citation form that the legalcode does not contain. 🔵 It is the "
     "row that shows why a floor alone is not enough — at `1 470` B it is caught "
     "by length, but a paraphrase at full length would not be."),
    ("cc-by-nc-nd-4.0-shule-ai", "CC-BY-NC-ND-4.0", "PROHIBITED",
     "gabrielmahia/shule-ai — `209` B, `9dd285c3704d`. 🔴 Title line, holder, "
     "URL, nothing else — the smallest payload this base has ever pinned, and it "
     "pinned as cleanly as a 35 KB legalcode would have."),
]


def resolve(prefix):
    """The one file in `fixtures/` whose name starts with `prefix`."""
    hits = sorted(n for n in os.listdir(FIX) if n.startswith(prefix))
    if len(hits) != 1:
        raise LookupError("%s resolves to %d files, expected 1" % (prefix, len(hits)))
    return os.path.join(FIX, hits[0])


def load(prefix):
    """Return (text, bytes_len, sha256_12) for a pinned fixture."""
    with open(resolve(prefix), "rb") as fh:
        raw = fh.read()
    return raw.decode("utf-8"), len(raw), hashlib.sha256(raw).hexdigest()[:12]


def declared():
    """(prefix, family, commercial, why, text, bytes, sha12) for every pin."""
    out = []
    for prefix, fam, com, why in DECLARED:
        text, n, sha = load(prefix)
        out.append((prefix, fam, com, why, text, n, sha))
    return out


# 🔵 The two families this arm reads as a TITLED/UNTITLED pair. Derived from
# DECLARED rather than written twice, so adding a shape cannot desynchronise it.
# 🔴 The payloads whose first non-blank line does not name the family. Declared
# as a SET rather than derived, and then CHECKED against the payloads by
# `test_the_untitled_payloads_carry_no_title_line` — a membership that derived
# itself from the same property it is used to test would assert nothing.
UNTITLED = {"mit-crewai", "bsd-3-clause-jupyterhub", "bsd-3-clause-open-tutor-ai-ce"}


def shape_pairs():
    """{family: {"titled": [prefix…], "untitled": [prefix…]}} for the arm's families.

    🔵 Lists, not single prefixes. The first build held one payload per slot and
    `p314` found a THIRD untitled payload within the same hour
    (`open-tutorai/open-tutor-ai-ce`), at which point a one-per-slot shape would
    have forced a choice between measuring it and keeping the structure.
    🔴 That is `ACTION p313-R` item 5's own warning generalised — *"do not publish
    a coverage figure off one of them"* — applied to the instrument rather than to
    the figure.
    """
    pairs = {}
    for prefix, fam, _com, _why in DECLARED:
        if fam not in ("MIT", "BSD-3-Clause"):
            continue
        slot = "untitled" if prefix in UNTITLED else "titled"
        pairs.setdefault(fam, {"titled": [], "untitled": []})[slot].append(prefix)
    return pairs


if __name__ == "__main__":
    for prefix, fam, com, _why, _t, n, sha in declared():
        print("  %-40s %-16s %-11s %6d B  %s" % (prefix, fam, com, n, sha))
