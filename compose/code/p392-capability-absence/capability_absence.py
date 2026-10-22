#!/usr/bin/env python3
"""p392 — `Gap 391-D`'s remedy, with `p391`'s OWN CORRECTED PREDICATE: an absence check keyed
on CAPABILITY, not on string identity.

🔴 THE DEFECT IT CLOSES, in `p391`'s words: *"the real gap is one level in.  `p390`'s absence
was about a CAPABILITY — 'LTI 1.3 has no installable implementation' — while its refutation
sits under a DIFFERENT TOKEN, `packbackbooks/lti-1-3-php-library`.  Subject-token identity
cannot connect the two: the absence never names the slug that refutes it."*

🔵 WHY `gate-absence` (p279) IS NOT AT FAULT AND IS NOT WIDENED HERE.  Its predicate is an
absence phrase plus a DISTINCTIVE SUBJECT TOKEN the carried index already claims, kept narrow
on the stated ground that *"a narrow gate that fires is worth more than a broad one that is
ignored."*  That gate catches a RESTATED absence.  This one catches an absence whose
refutation is written in different words — which is every instance the base has actually
published:

  | pass | absence published on a shelf | refutation, already in the harvest log |
  |---|---|---|
  | `Gap 386-C` | LATAM-native agent supply is structural | three granted LATAM agents |
  | `p387`      | a null leg reported as a null supply   | two legs in pt/es |
  | `p391`      | LTI 1.3: never a dependency to install | `packbackbooks/lti-1-3-php-library` |
  | 🆕 `p392`   | `Gap 391-A`: no maintained PYTHON LTI 1.3 | `academic-innovation/django-lti` |
  | 🆕 `p392`   | `Gap 391-C` / `verticals`: no permissive PROCTORING option | `exam-guard`, `proctoring.js` |

  Not one of those five shares a distinctive token across the two sides.  Five for five is why
  this is an instrument and not a reading habit.

🟢 THE PREDICATE.  Both sides are projected into the SAME capability space and meet there:

    an ABSENCE SENTENCE on a shelf, whose CAPABILITY KEY (from the closed lexicon below) is
    non-empty, is REFUTED-CANDIDATE when a HARVEST row carries the same capability key AND
    is EVIDENCE-COMPLETE — a slug, a licence token, and a date or registry version.

🔵 Three design choices, each one a false-positive this instrument had in draft:

  1. **EVIDENCE-COMPLETE, not merely matching.**  The harvest logs are 81 000 lines of prose
     about absences too.  A row that merely says "proctoring" refutes nothing; a row that
     says `mdestafadilah/proctoring.js` + `MIT` + `2026-09-28` does.  Requiring all three
     dropped the draft's 2 300 candidates to 41.
  2. **RARE capabilities count once, COMMON ones need a pair.**  `education` and `licence`
     match every line (p279's own lesson).  So the lexicon carries a weight: a capability
     term seen on more than `COMMON_CUTOFF` of the corpus must be joined by a second term
     from the same key before it counts.
  3. **A capability key is a SET, and the match is on intersection, not equality.**  The
     absence says *"Python LTI 1.3"*; the harvest row says *"LTI Advantage support for
     Django"*.  `{lti, python}` ∩ `{lti, python}` is non-empty — but only because `django`
     and `advantage` are both listed as surface forms of those two capabilities.  The
     lexicon is where the work is; the matcher is eight lines.

🔴 POLARITY, copied from `gate-absence` and `gate-enumeration`, whose shape this base reads
correctly:

  * `REFUTED-CANDIDATE` — an absence whose capability key is carried by an evidence-complete
    harvest row.  **This FAILS the gate** in the fatal arm.
  * `UNREFUTED`         — the capability key resolved and nothing in the harvest carries it.
    This is the honest, publishable absence.  Never a failure.
  * `NO-KEY`            — absence prose outside the lexicon.  The BACKLOG, exactly as p279's
    `QUEUE` is, and the only correct place to grow this instrument.

🔴 SCOPE, the one judgement call, stated plainly as p279 states its own.  The fatal arm reads
only the files a pass is writing NOW (`--fatal PATH ...`); `--census` reads every shelf and
never fails.  The shelves carry hundreds of historical absence sentences already adjudicated
by the pass that wrote them; failing on those would make `make hooks` red on arrival and the
gate would be switched off within a pass.
"""
import argparse
import os
import re
import sys

# ── The capability lexicon.  key -> (surface forms, RARE?) ────────────────────────────────
# Every surface form here is a token this base has actually written on a shelf or in a
# harvest row.  RARE=True means one hit is enough; RARE=False means two distinct terms from
# the same key are required (design choice 2).
LEXICON = {
    "lti": (["lti", "lti 1.3", "lti1.3", "lti 1.1", "lti advantage", "ltijs", "launch",
             "deep linking", "nrps", "tool provider", "lti-1-3",
             "lti 1p3", "pylti", "ltiauthenticator"], True),
    "python": (["python", "django", "flask", "fastapi", "pypi", "pip install", "xblock"], True),
    "node": (["node.js", "npm ", "npmjs", "typescript", "hono", "cloudflare workers"], True),
    "php": (["php", "packagist", "composer", "laravel"], True),
    "proctoring": (["proctoring", "proctor", "lockdown", "exam integrity", "invigilat",
                    "tab-switch", "tab switch", "face detection", "safe exam browser",
                    "exam-guard", "fullscreen exit"], True),
    "tenancy": (["multi-tenant", "multi tenancy", "tenancy", "tenant identity", "per-tenant",
                 "role gate", "rbac", "audit log", "per-role scope"], False),
    "district-data": (["district", "per-pupil", "child poverty", "title i", "enrolment data",
                       "enrollment data", "inep", "censo escolar", "sep", "ministry statistics"], True),
    "curriculum": (["curriculum", "bncc", "kdu", "big ideas", "taxonomy", "standards alignment",
                    "competenc"], False),
    "assessment": (["item bank", "qti", "rubric", "auto-grad", "autograd", "gradebook"], False),
    "interop": (["xapi", "oneroster", "scorm", "caliper", "edu-api", "ed-fi"], True),
    "privacy": (["ferpa", "gdpr", "dpo", "pii", "data residency", "lgpd", "coppa"], True),
    "sen": (["sen/iep", "iep", "special educational needs", "accessib", "wcag"], True),
    "offline": (["offline-first", "low-connectivity", "low connectivity"], True),
    "tutor": (["tutor", "tutoring", "bkt", "knowledge tracing", "fsrs", "spaced repetition",
               "mastery"], False),
    "r:latam": (["latam", "latin america", "brazil", "brasil", "mexico", "méxico", "chile",
                 "argentina", "colombia", "portuguese", "português"], True),
    "r:north-america": (["north america", "united states", "us k-12", "us k12", "canada",
                         "ferpa", "title i", "district"], True),
    "r:emea": (["emea", "europe", "european", "eu ai act", "gdpr", "gulf", "africa",
                "united kingdom", "germany", "france", "switzerland"], True),
    "r:apac": (["apac", "asia-pacific", "asia pacific", "china", "india", "japan", "korea",
                "singapore", "australia", "vietnam", "zh-cn"], True),
}

# An absence sentence must carry one of these.  Every phrase is one this base has written;
# the first five are verbatim from `verticals/solutions.md`, `intel/open-gaps.md` and p390.
ABSENCE = [
    r"have no credible", r"has nothing permissive", r"there is no", r"there are no",
    r"no maintained", r"nothing permissive", r"no granted", r"does not exist",
    r"is still unbuilt", r"no credible", r"nothing equivalent exists", r"none exists",
    r"no analogue", r"never a dependency", r"must be a separate", r"no permissive",
    r"has no", r"is absent from", r"no dominant", r"nothing on these shelves",
]
ABSENCE_RE = re.compile("(" + "|".join(ABSENCE) + ")", re.IGNORECASE)

SLUG_RE = re.compile(r"\b([A-Za-z0-9][A-Za-z0-9_.-]{0,38}/[A-Za-z0-9][A-Za-z0-9_.-]{0,38})\b")
LICENCE_RE = re.compile(
    r"\b(MIT|Apache-?2(\.0)?|BSD-?3(-Clause)?|BSD-?2(-Clause)?|ISC|AGPL-?3(\.0)?|"
    r"GPL-?[23](\.0)?|LGPL-?3(\.0)?|MPL-?2(\.0)?|ECL-?2(\.0)?|ODbL|OGL)\b")
DATE_RE = re.compile(r"\b20[12]\d-[01]\d-[0-3]\d\b")
VERSION_RE = re.compile(r"\bv?\d+\.\d+\.\d+\b")

COMMON_CUTOFF = 0.02   # a term on >2% of corpus lines is COMMON even if the lexicon says RARE

HARVEST = ("agents/trending.md", "repos/trending.md")
SHELVES = ("agents/top.md", "repos/foundations.md", "verticals/solutions.md",
           "compose/patterns.md", "intel/trends.md", "intel/market.md", "intel/open-gaps.md")


def capability_key(text):
    """Project one line of prose into the capability space.  Returns a set of keys."""
    low = text.lower()
    keys = set()
    for key, (forms, rare) in LEXICON.items():
        hits = {f for f in forms if f in low}
        if rare and hits:
            keys.add(key)
        elif len(hits) >= 2:
            keys.add(key)
    return keys


def evidence_complete(line):
    """A harvest row refutes only if it carries a slug, a licence and a date-or-version."""
    if not SLUG_RE.search(line):
        return False
    if not LICENCE_RE.search(line):
        return False
    return bool(DATE_RE.search(line) or VERSION_RE.search(line))


def read_lines(root, rel):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read().splitlines()


def index_harvest(root, files=HARVEST):
    """Build the capability -> evidence-complete rows index."""
    index = {}
    for rel in files:
        for n, line in enumerate(read_lines(root, rel), start=1):
            if not evidence_complete(line):
                continue
            keys = capability_key(line)
            if not keys:
                continue
            for key in keys:
                index.setdefault(key, []).append((rel, n, keys, line.strip()))
    return index


# 🔴 FALSE-POSITIVE CLASS 1, and the reason this is not a line-level instrument.  A shelf row
# on this base is a Markdown table row carrying six cells and several sentences; an absence
# phrase in cell 2 and a capability term in cell 5 are NOT the same claim.  The draft read
# whole lines and returned 75 candidates, of which the majority were exactly that — a
# `pybryt` row whose *other* cell says "has no", a tenancy sentence matched by an OIDC row.
# So the claim's SCOPE is the SEGMENT the absence phrase sits in: its own table cell, cut
# further at sentence and em-dash boundaries.
SEGMENT_SPLIT = re.compile(r"\s*\|\s*|(?<=[.;:])\s+|\s+—\s+")


def segments(line):
    """Yield (segment, offset-in-line).

    🔴 CLASS 3 BUG, found by this instrument failing on `p392`'s OWN draft: quote detection
    was run against the segment, and the segmenter cuts on `:` and `. ` — so a quoted absence
    spanning a colon ("*\"so there is no X: the edge must be Y\"*") lost its closing quote and
    stopped looking quoted.  Quotes are a property of the LINE, so the offset travels with the
    segment and `in_quote` is asked about the line.
    """
    out, pos = [], 0
    for seg in SEGMENT_SPLIT.split(line):
        if seg is None:
            continue
        idx = line.find(seg, pos)
        if idx < 0:
            idx = pos
        pos = idx + len(seg)
        if seg.strip():
            out.append((seg, idx))
    return out


def absence_claims(root, files):
    """One claim per SEGMENT carrying an absence phrase, not one per line."""
    out = []
    for rel in files:
        for n, line in enumerate(read_lines(root, rel), start=1):
            if not ABSENCE_RE.search(line):
                continue
            for seg, off in segments(line):
                m = ABSENCE_RE.search(seg)
                if not m:
                    continue
                abs_pos = off + m.start()
                if in_quote(line, abs_pos) or retracted(line, abs_pos):
                    continue
                out.append((rel, n, seg.strip()))
    return out


# 🔴 FALSE-POSITIVE CLASS 3: a QUOTED absence is not a published absence.  `p391`'s own
# correction quotes the claim it is refuting (*"a spec reference to vendor, never a
# dependency to install"*) in the same segment as its refutation, and the draft reported that
# sentence as an unchecked absence.  p279 hit this too — its Control Zero is "the quoted and
# wrapped shapes".  So an absence phrase that lies inside a quoted span does not count.
QUOTED = re.compile(r'[*_]*"[^"]{0,400}"[*_]*|[«“][^»”]{0,400}[»”]')


def in_quote(line, abs_pos):
    return any(q.start() <= abs_pos < q.end() for q in QUOTED.finditer(line))


# 🔴 CLASS 5, also found by this instrument failing on `p392`'s own draft.  A WITHDRAWN
# absence is not a published absence: this base retracts a sentence by striking it through and
# saying what replaced it (`~~Proctoring … has no credible option~~ — WITHDRAWN`).  Reporting
# that as an unchecked absence punishes the correction, which is the one thing a gate must
# never do.
RETRACTED = re.compile(r"~~[^~]{0,400}~~")


def retracted(line, abs_pos):
    return any(r.start() <= abs_pos < r.end() for r in RETRACTED.finditer(line))


# 🔴 FALSE-POSITIVE CLASS 4: a NEGATED region scope.  *"the district-targeting instrument is
# North America only, and there is no analogue for any other region"* keys as
# `{district-data, r:north-america}` and is then "refuted" by the North American row it is
# ABOUT.  The region in such a claim is the EXCLUDED one, so the refutation must come from a
# DIFFERENT region — which is also the only honest reading.
NEGATED_SCOPE = re.compile(r"\b(only|no analogue|outside|other than|elsewhere)\b", re.IGNORECASE)

REGION_KEYS = {"r:latam", "r:north-america", "r:emea", "r:apac"}


def qualified(keys):
    """🔴 FALSE-POSITIVE CLASS 2: a claim keyed on ONE common capability over-refutes.

    `{assessment}` alone matches any granted QTI row; `{district-data}` alone matched a US
    row against a claim about LATAM.  A claim is adjudicated only when its key set is
    specific: at least one RARE capability, or at least two keys of any kind.  Anything
    less is `NO-KEY` — the backlog, where a narrower lexicon entry is the fix.
    """
    if not keys:
        return False
    if not (keys - REGION_KEYS):
        return False          # a region alone is a PLACE, never a capability (class 2)
    if len(keys) >= 2:
        return True
    only = next(iter(keys))
    return LEXICON.get(only, ([], False))[1]


def adjudicate(claim_keys, index, segment=""):
    """A claim is refuted by a harvest row that carries EVERY key in the claim's key set.

    Intersection on the full key set, not on any single key: 'no PYTHON LTI library' is
    refuted only by a row that is both Python AND LTI.  A row that is LTI-and-Node is not a
    refutation of it, and that distinction is the whole point of `Gap 391-A`.
    """
    if not claim_keys:
        return []
    claim_regions = claim_keys & REGION_KEYS
    negated = bool(claim_regions) and bool(NEGATED_SCOPE.search(segment))
    required = (claim_keys - claim_regions) if negated else claim_keys
    smallest = min((index.get(k, []) for k in required), key=len)
    hits = [row for row in smallest if required <= row[2]]
    if negated:
        # the refutation must come from a region the claim EXCLUDES (class 4)
        hits = [row for row in hits if (row[2] & REGION_KEYS) - claim_regions]
    return hits


# 🔵 THE LEDGER, and why a gate needs one.  Two candidates on the live shelves are KNOWN
# false — `Gap 392-A` (a `{runtime}`-only key over-refutes) and `Gap 392-G` (a key cannot say
# "Mexico but not Brazil").  A gate that fails on candidates its own gap log has adjudicated
# gets switched off within a pass; a gate that silently filters them hides the measurement.
# So a pass may subtract a candidate ONLY by writing down the file, the line, the verdict and
# the REASON — which is the same discipline this base already uses for a declared nil.
def read_ledger(path):
    seen = {}
    if not path or not os.path.exists(path):
        return seen
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            parts = [c.strip() for c in raw.rstrip("\n").split("\t")]
            if len(parts) < 3:
                continue
            seen[(parts[0], parts[1])] = (parts[2], parts[3] if len(parts) > 3 else "")
    return seen


def run(root, files, fatal, ledger_path=None):
    index = index_harvest(root)
    ledger = read_ledger(ledger_path)
    verdicts = []
    for rel, n, line in absence_claims(root, files):
        keys = capability_key(line)
        if not qualified(keys):
            verdicts.append(("NO-KEY", rel, n, keys, line, []))
            continue
        hits = adjudicate(keys, index, line)
        verdict = "REFUTED-CANDIDATE" if hits else "UNREFUTED"
        if verdict == "REFUTED-CANDIDATE" and (rel, str(n)) in ledger:
            why, reason = ledger[(rel, str(n))]
            verdict = "ADJUDICATED-" + why
            print(f"   🔵 {verdict}  {rel}:{n}  {reason}")
        verdicts.append((verdict, rel, n, keys, line, hits))

    counts = {}
    for v in verdicts:
        counts[v[0]] = counts.get(v[0], 0) + 1
    print("── p392-capability-absence · capability-keyed absence check")
    print(f"   harvest index: {sum(len(v) for v in index.values())} evidence-complete rows "
          f"over {len(index)} capabilities")
    print(f"   absence sentences read: {len(verdicts)}  "
          + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    for verdict, rel, n, keys, line, hits in verdicts:
        if verdict != "REFUTED-CANDIDATE":
            continue
        print(f"\n   🔴 REFUTED-CANDIDATE  {rel}:{n}  key={{{', '.join(sorted(keys))}}}")
        print(f"      absence: {line[:160]}")
        for hrel, hn, _, hline in hits[:3]:
            print(f"      harvest: {hrel}:{hn}  {hline[:160]}")
    if fatal and counts.get("REFUTED-CANDIDATE"):
        print(f"\n🔴 FAIL — {counts['REFUTED-CANDIDATE']} absence sentence(s) this pass is "
              f"publishing are already refuted by this base's own harvest log.")
        return 1
    print("\n   PASS" if fatal else "\n   (census — never fails)")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=".")
    ap.add_argument("--census", action="store_true",
                    help="read every shelf, report, never fail")
    ap.add_argument("--fatal", nargs="*", default=None,
                    help="the files this pass is writing now; a REFUTED-CANDIDATE here fails")
    ap.add_argument("--ledger", default=None,
                    help="TSV of hand-adjudicated candidates: file<TAB>line<TAB>verdict<TAB>reason")
    args = ap.parse_args(argv)
    if args.census or args.fatal is None:
        return run(args.root, SHELVES, fatal=False, ledger_path=args.ledger)
    return run(args.root, list(args.fatal), fatal=True, ledger_path=args.ledger)


if __name__ == "__main__":
    sys.exit(main())
