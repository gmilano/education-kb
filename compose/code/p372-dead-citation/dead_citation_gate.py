#!/usr/bin/env python3
"""`gate-dead-citation` — the standing half of `p372`.  OFFLINE: it reads committed evidence.

Three invariants, each one a figure or a failure this base has already paid for:

  `I1`  **The re-derivation holds.**  Every row of the `p372` re-probe carries a class, the
        classes partition the file, and the published counts are re-derivable from the rows
        (`T37`/`recount` applied to `Gap 483`'s quantity).
  `I2`  **No live shelf recommends an absent address.**  A dead address may be CITED in an
        append-only history or as a negative control; it may not be a row that asserts the
        address is usable today.
  `I4`  **A region whose ENGLISH leg returns nothing must be re-asked IN LANGUAGE before the
        nil is published.**  🔴 This base has now found the language axis THREE times —
        `P521` (a Portuguese query returned six trees ten English passes had missed),
        `ACTION ZZ-cc` (*"the prescribed per-region query should name countries, not
        regions"*), and `Gap 476` — and each time it stayed a narrated observation.  At
        `p372` the English EMEA leg returned **0** education-specific facts and the German
        leg returned **4**.  🟢 This invariant is the difference between knowing that and
        doing it every pass.
  `I3`  **A proven successor is REGISTERED, not merely narrated.**  🔴 This is the invariant
        `apereo/opencast` needed: proven at `p230`, written into prose, never wired in, and
        re-adjudicated at `p371` as unknown.  Every `MOVED` row in the re-probe must have a
        successor-register row carrying a first-hand proof.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dead_citation import classify_string, citation_is_a_live_claim, LIVE_SHELVES  # noqa: E402

REPROBE = "evidence/dead-citation-reprobe.2026-10-21-p372.tsv"
REGIONLEG = "evidence/region-leg-inlanguage.2026-10-21-p372.tsv"
VOCAB = ("North America", "EMEA", "APAC", "LATAM")
SUCCESSOR = "evidence/dead-successor-register.2026-10-21-p372.tsv"

#: The partition `p372` published.  A change to the evidence must change these too, which is
#: the point: the figure and the rows cannot drift apart silently.
EXPECTED = {
    "ABSENT-NO-SUCCESSOR-FOUND": 27,
    "OWNER-ALIVE-REPO-ABSENT": 5,
    "NOT-AN-ADDRESS/NEG-CONTROL": 5,
    "NOT-AN-ADDRESS/URL-PATH": 4,
    "EXISTS-EMPTY": 2,
    "MOVED": 1,
    "ALIVE-OTHER-FORGE": 1,
    "NOT-AN-ADDRESS/PLACEHOLDER": 1,
}
TOTAL = 46


def rows(path):
    with open(path, encoding="utf-8") as fh:
        head = None
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if head is None:
                head = parts
                continue
            yield dict(zip(head, parts))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = ap.parse_args().root
    bad = []

    # ---- I1: the re-derivation holds -------------------------------------------------
    rp = list(rows(os.path.join(root, REPROBE)))
    if len(rp) != TOTAL:
        bad.append(f"I1 the re-probe holds {len(rp)} rows, not {TOTAL}")
    counts = {}
    for r in rp:
        counts[r["class_p372"]] = counts.get(r["class_p372"], 0) + 1
    for cls, want in EXPECTED.items():
        if counts.get(cls, 0) != want:
            bad.append(f"I1 class {cls}: rows say {counts.get(cls, 0)}, published figure is {want}")
    for cls in counts:
        if cls not in EXPECTED:
            bad.append(f"I1 class {cls} is in the rows and not in the published partition")
    if sum(counts.values()) != TOTAL:
        bad.append(f"I1 the classes sum to {sum(counts.values())}, not {TOTAL}")

    # 🟢 the string classes must AGREE with the classifier, so the file cannot be
    # hand-edited into a class the code would not assign.
    for r in rp:
        got = classify_string(r["slug"])
        cls = r["class_p372"]
        if cls == "NOT-AN-ADDRESS/URL-PATH" and got != "URL-PATH-FRAGMENT":
            bad.append(f"I1 {r['slug']} is filed URL-PATH; classifier says {got}")
        if cls == "NOT-AN-ADDRESS/PLACEHOLDER" and got != "PLACEHOLDER":
            bad.append(f"I1 {r['slug']} is filed PLACEHOLDER; classifier says {got}")
        if cls == "NOT-AN-ADDRESS/NEG-CONTROL" and got != "NEG-CONTROL":
            bad.append(f"I1 {r['slug']} is filed NEG-CONTROL; classifier says {got}")
        if cls not in ("NOT-AN-ADDRESS/URL-PATH", "NOT-AN-ADDRESS/PLACEHOLDER",
                       "NOT-AN-ADDRESS/NEG-CONTROL") and got != "ADDRESS":
            bad.append(f"I1 {r['slug']} is filed {cls} but is not a well-formed address ({got})")

    # ---- I2: no live shelf recommends an absent address ------------------------------
    absent = {r["slug"] for r in rp
              if r["class_p372"] in ("ABSENT-NO-SUCCESSOR-FOUND", "OWNER-ALIVE-REPO-ABSENT",
                                     "MOVED", "ALIVE-OTHER-FORGE")}
    for shelf in LIVE_SHELVES:
        p = os.path.join(root, shelf)
        if not os.path.exists(p):
            continue
        assert citation_is_a_live_claim(shelf)
        with open(p, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                for slug in absent:
                    # only a LINKED row asserts usability; bare prose mentioning the
                    # address as a past measurement does not.
                    if f"github.com/{slug})" in line or f"github.com/{slug} " in line:
                        bad.append(f"I2 {shelf}:{n} links absent address {slug} as a live row")

    # ---- I3: a proven successor is registered ----------------------------------------
    reg = {r["dead_address"]: r for r in rows(os.path.join(root, SUCCESSOR))}
    for r in rp:
        if r["class_p372"] in ("MOVED", "ALIVE-OTHER-FORGE", "EXISTS-EMPTY"):
            e = reg.get(r["slug"])
            if not e:
                bad.append(f"I3 {r['slug']} is {r['class_p372']} and has NO successor-register row")
            elif not e.get("first_hand_proof", "").strip():
                bad.append(f"I3 {r['slug']} is registered with no first-hand proof")

    # ---- I4: a nil region must have been re-asked in language ------------------------
    rl = os.path.join(root, REGIONLEG)
    if os.path.exists(rl):
        legs = list(rows(rl))
        by_region = {}
        for r in legs:
            by_region.setdefault(r["region"], []).append(r)
        for region in VOCAB:
            rs = by_region.get(region)
            if not rs:
                bad.append(f"I4 region {region} has no leg recorded at all")
                continue
            def nfacts(r):
                head = r["education_specific_dated_facts_returned"].strip()
                return 0 if head.startswith("0") else 1
            english_nil = any(r["query_language"] == "English" and nfacts(r) == 0 for r in rs)
            has_other = any(r["query_language"] != "English" for r in rs)
            if english_nil and not has_other:
                bad.append(
                    f"I4 {region}: the English leg returned 0 education-specific facts and "
                    f"NO in-language leg was run — publish the nil only after re-asking "
                    f"(P521 / ACTION ZZ-cc / Gap 476)")
    else:
        bad.append(f"I4 {REGIONLEG} is missing")

    if bad:
        print(f"🔴 gate-dead-citation — {len(bad)} violation(s):")
        for b in bad:
            print(f"   - {b}")
        return 1
    print(f"🟢 gate-dead-citation — I1 partition re-derives ({TOTAL} rows, "
          f"{len(EXPECTED)} classes) · I2 {len(absent)} absent addresses, none on a live shelf · "
          f"I3 {len(reg)} successor rows, all with first-hand proof · "
          f"I4 every nil English regional leg was re-asked in language")
    return 0


if __name__ == "__main__":
    sys.exit(main())
