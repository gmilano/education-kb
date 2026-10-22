#!/usr/bin/env python3
"""`p374-regional-leg` — what makes a regional leg work, as a checkable rule.

🟢 `Gap 489` (`p373`): this base has published **four** attributions for the regional legs'
yield — `ACTION PJ` (the organ), `ACTION QJ` (shape was never the defect), `P870`
(jurisdiction phrasing), `Gap 476` (language) — **in four files, none citing another**. There
was no single place where *"what makes a regional leg work"* was recorded, and that is why
`p372` repeated `p206`'s two-variables-at-once error with `p207`'s correction already committed.

🔴 `ACTION p373-A` asked for a **per-jurisdiction corpus-language column**. Building it as
specified would have wired a **refuted** theory into a standing gate. `p373`'s account — that
what decides a leg is the language *the jurisdiction publishes in* — was tested out of sample
at `p374` on a prediction registered **before** the measurement, and Japan refuted it: MEXT
publishes in Japanese and the **English** leg was productive anyway, through `MLex` and English
news wires. So the column here is the one that fits all six measured cells: **does a
cross-border specialist press channel cover this jurisdiction in the query's language.**

The three questions this instrument keeps apart — folding them is what produced four answers:

  1. **did the leg NAME a jurisdiction?**          — `names_a_jurisdiction`
  2. **is a published NIL admissible?**            — `nil_is_admissible`   (two limbs, `J2`)
  3. **may a language be called REDUNDANT?**       — `redundancy_is_admissible` (`J3`)

🔵 Question 3 is the one no prior pass asked. `p373` concluded Portuguese was "redundant" for
Brazil because the English leg returned more. `p374` ran both legs for Japan and both were
productive — but the Japanese leg returned the **pilot-school count 66 → 281**, an operational
figure the English leg never mentioned. Two legs can both be productive and still not be
substitutes, so "redundant" needs a **fact-class** test, not a count.
"""

#: 🔴 The CLOSED region vocabulary. Five values, exactly. This is not this instrument's
#: invention — it is the standing contract of every shelf in this tree, and `gate-region-headings`
#: enforces it on the headings. It is repeated here because the register is a tenth file that
#: the heading gate does not read, and an unchecked tenth file is how a vocabulary drifts.
#: 🔵 "Latam", "Europe", "Brazil" are the three real drift cases this base has seen.
REGIONS = ("North America", "EMEA", "APAC", "LATAM", "Global")

#: 🔴 Region LABELS are not jurisdictions. This is `J2` limb 1's whole content, and it is the
#: thing `I4` could not see. `p373`'s cell 1 was an in-language leg whose only placename was
#: "EMEA"; it returned an explicit nil for every EMEA country except the language's own
#: ("keine Daten zur Akzeptanz in anderen EMEA-Laendern") and `I4` would have PASSED it as a
#: properly-controlled nil, because an in-language leg had indeed been run.
_REGION_LABELS = {r.casefold() for r in REGIONS} | {
    "emea", "apac", "latam", "latin america", "europe", "asia", "asia-pacific",
    "north america", "global", "worldwide", "eu", "european union",
}


def names_a_jurisdiction(placenames):
    """`J2` limb 1. True only if some placename is NOT merely a region label.

    A country or an organ counts; `KMK`, `MEXT`, `CNE`, `Germany`, `Japan` all count.
    A region label never counts, however many of them a query carries.
    """
    for p in placenames or ():
        if p and p.strip() and p.strip().casefold() not in _REGION_LABELS:
            return True
    return False


def nil_limbs(leg, sibling_legs):
    """The two limbs alone, with no reference to whether the nil is still on offer.

    `I4` (`p372`): refuse a published regional nil unless an in-language leg was run.
    🔴 Satisfiable without naming a jurisdiction (`p373` cell 1), and it OVER-FIRES — it would
    demand a Portuguese leg for Brazil, where English + organ returns more.

    `J2`'s test: a nil is sound only if the leg **named a jurisdiction** AND another leg for the
    **same jurisdiction** was run **in a different language**.

    Returns (sound, reason).
    """
    if leg["verdict"] != "NIL":
        return True, "not-a-nil"
    if not names_a_jurisdiction(leg.get("placenames")):
        return False, "LIMB-1: the leg named no jurisdiction, only a region label"
    same = [s for s in sibling_legs
            if s["jurisdiction"] == leg["jurisdiction"]
            and s["language"] != leg["language"]]
    if not same:
        return False, "LIMB-2: no leg in another language was run for this jurisdiction"
    return True, "both limbs satisfied"


def nil_is_admissible(leg, sibling_legs):
    """`J2` as the gate enforces it: soundness AND disposition must agree.

    🔴 The point of the disposition limb. `p373` cell 1 is an in-language leg naming only
    "EMEA" that published an explicit nil for the rest of the region. `I4` would have passed
    it. `J2` finds it unsound — and a gate that merely went red would leave this base with a
    red gate and the bad nil still on the shelf. So the rule is: **an unsound nil must be
    marked WITHDRAWN.** The defect is recorded rather than deleted, the nil stops being
    citable as evidence about its region, and the gate is green because the retraction is
    committed.

    🟢 This is also the instrument's own negative control: flip `p373-c1`'s disposition back
    to `PUBLISHED` and `J2` must go red.
    """
    sound, why = nil_limbs(leg, sibling_legs)
    if leg["verdict"] != "NIL":
        return True, "not-a-nil"
    disposition = leg.get("nil_disposition", "-")
    if sound:
        if disposition.startswith("WITHDRAWN"):
            return False, ("a SOUND nil is marked %s -- a nil that passes both limbs may not "
                           "be retracted silently" % disposition)
        return True, "both limbs satisfied, nil stands as published"
    if disposition.startswith("WITHDRAWN"):
        return True, "unsound (%s) and correctly marked %s" % (why, disposition)
    return False, "%s -- and it is still marked %s" % (why, disposition)


def redundancy_is_admissible(jurisdiction, language, legs):
    """`J3`. May a pass call `language` REDUNDANT for `jurisdiction`?

    Only if a leg in that language AND a leg in another language both ran for that
    jurisdiction, both were productive, and they returned the SAME fact class.

    🔴 Japan is the negative control: English and Japanese legs both PRODUCTIVE, fact classes
    `policy-milestones` vs `operational-detail`. Calling either redundant is refused.
    """
    mine = [l for l in legs if l["jurisdiction"] == jurisdiction and l["language"] == language]
    others = [l for l in legs if l["jurisdiction"] == jurisdiction and l["language"] != language]
    if not mine or not others:
        return False, "a language cannot be called redundant until BOTH legs have run"
    if any(l["verdict"] == "NIL" for l in mine + others):
        return False, "one of the legs returned NIL -- that is necessity, not redundancy"
    classes = {l["fact_class"] for l in mine + others}
    if len(classes) > 1:
        return False, ("the legs returned DIFFERENT fact classes (%s) -- productive is not "
                       "the same as substitutable" % ", ".join(sorted(classes)))
    return True, "both productive, same fact class"


def region_is_in_vocabulary(region):
    """`J1`. The closed five-value vocabulary, compared exactly — never case-folded.

    🔵 Folded comparison is wrong here on purpose: `latam` is not an admissible spelling of
    `LATAM` on a shelf, and the compiler buckets on the literal.
    """
    return region in REGIONS


def verdict_is_consistent(leg):
    """`J4`. A leg cannot be a NIL and carry facts, or be PRODUCTIVE and carry none."""
    n = leg.get("fact_count", 0)
    if leg["verdict"] == "NIL":
        return n == 0, "a NIL leg carrying %d facts" % n
    if leg["verdict"] in ("PRODUCTIVE", "PARTIAL"):
        return n > 0, "a %s leg carrying no facts" % leg["verdict"]
    return False, "unknown verdict %r" % leg["verdict"]
