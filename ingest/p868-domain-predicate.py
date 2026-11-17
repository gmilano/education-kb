#!/usr/bin/env python3
"""p868 — discharge of `867-G1`: the DOMAIN decision, taken by a command instead of by eye.

WHY THIS EXISTS.  This base has now moved hand-grading downstream three times and each
move was registered as a gap by the pass that made it:

    `865-G4`  removed hand-grading from the three-way SPLIT  -> `ingest/p866-triage.py`
    `866-G1`  removed it from the CHOICE of which UNGRADED address to file
              -> `ingest/p867-promotion-rank.py`
    `867-G1`  found it one step further UPSTREAM: `p867` collected `285`
              organisation-owned candidates and selected `30` of them AS
              EDUCATION-DOMAIN BY READING THEIR DESCRIPTIONS, before either
              instrument ran.

So the ranker was being fed a hand-picked bucket and its hit rate was measuring the
ranker against the hand that had already chosen.  This is the missing gate: a mechanical
DOMAIN predicate over `description` + `topics`, scored in `ingest/config.json`'s own
declared terms rather than a fresh vocabulary invented here.

WHAT IT IS.  A weighted keyword/topic score, three bands, and nothing else:

    TOPIC hit      weight 3   -- an author who tags `topic:edtech` has DECLARED the domain
    STRONG term    weight 2   -- a word that is education and almost nothing else
    WEAK term      weight 1   -- a word that is education IN CONTEXT and noise outside it
    NEGATIVE term  weight -3  -- the homograph trap this corpus keeps walking into

`KEEP` at score >= 3, `MARGINAL` at 1-2, `DROP` at <= 0.

🔴 WHY THE NEGATIVE LIST EXISTS, measured and not guessed.  `p867` published the reason:
its `curriculum OR syllabus generator` vein alone reported `20,340` totals and imported
`OpenAPITools/openapi-generator`, `OrcaSlicer/OrcaSlicer`, `grpc-ecosystem/grpc-gateway`
and `appwrite/sdk-generator` — four pieces of general-purpose tooling that matched on a
word.  A predicate with no negative arm reproduces exactly that, and this base's `T-series`
already records the homograph class (`p862-homograph-control.sh`).

WHAT IT IS NOT.  It is not a quality or licence judgement — `p867-promotion-rank.py` holds
those gates and runs after this one.  It does not read a README (that is a clone, and the
sweep is metadata).  And it is NOT claimed to be better than the hand: `--against` publishes
its RECALL against a pass's hand selection and the addresses it ADDS, whichever way they fall.

Usage:
    python3 -I ingest/p868-domain-predicate.py --sweep sweep.tsv --org-only
    python3 -I ingest/p868-domain-predicate.py --sweep s.tsv --org-only \
        --against evidence/handpicked.txt --tsv evidence/domain-predicate.<date>-p868.tsv
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# --- the vocabulary, derived from ingest/config.json rather than invented here -----------
# config.json declares `topics`, `agentKeywords`, `repoKeywords`, `verticalKeywords` and a
# `keywords` map.  The three bands below are those terms, sorted by how much of the
# education domain each one carries ALONE.  Every term is a config.json term or a platform
# name config.json already names; nothing is added for convenience.
CONFIG_TOPICS = ["edtech", "learning-management", "educational-ai", "tutoring", "e-learning"]

STRONG = [
    # a word that is education and almost nothing else
    "edtech", "e-learning", "elearning", "lms", "moodle", "open edx", "openedx", "xblock",
    "canvas lms", "chamilo", "ilias", "sakai", "blackboard", "scorm", "lti", "oneroster",
    "student", "teacher", "classroom", "pupil", "learner", "tutor", "tutoring", "coursework",
    "curriculum", "syllabus", "pedagog", "didactic", "university", "school", "k-12", "k12",
    "mooc", "educator", "gradebook", "quiz", "exam", "homework", "lecture", "flashcard",
    "learning management", "learning analytics", "educational",
]
WEAK = [
    # education IN CONTEXT; noise on its own, which is why it scores 1
    "education", "learning", "course", "grading", "grade", "assessment", "assignment",
    "study", "teach", "training", "academic", "enrol", "enroll", "transcript", "credential",
    "curricula", "instruction", "knowledge", "literacy", "skill",
]
NEGATIVE = [
    # 🔴 p867's four measured imports and their families: tooling that matched on a word
    "openapi", "swagger", "sdk generator", "code generator", "slicer", "3d print",
    "grpc", "gateway", "boilerplate", "scaffold", "terraform", "kubernetes operator",
    "crypto", "blockchain wallet", "trading", "resume builder", "cv generator",
    "static site generator", "theme for", "wordpress theme", "dotfiles", "awesome list",
]
KEEP_AT = 3
MARGINAL_AT = 1

TOPIC_WEIGHT = 3
STRONG_WEIGHT = 2
WEAK_WEIGHT = 1
NEGATIVE_WEIGHT = -3


def _wordish(term):
    """Match a term on word boundaries where it is a word, as a substring where it is a stem.

    `T174`/`852-G3` is this base's standing finding that a presence check keyed on
    substrings OVER-reports and one keyed on whole URLs UNDER-reports.  The same applies
    here: `pedagog` must match `pedagogical`, and `lms` must NOT match `films`.
    """
    if term.endswith(("g", "l")) and term in ("pedagog", "enrol"):
        return re.compile(re.escape(term), re.I)
    if " " in term or "-" in term:
        return re.compile(re.escape(term), re.I)
    return re.compile(r"\b%s\w{0,3}\b" % re.escape(term), re.I)


STRONG_RE = [(t, _wordish(t)) for t in STRONG]
WEAK_RE = [(t, _wordish(t)) for t in WEAK]
NEGATIVE_RE = [(t, _wordish(t)) for t in NEGATIVE]


def score(description, topics, address=""):
    """Return (score, band, reasons).  Deterministic; no network, no README."""
    text = " ".join([description or "", address.replace("/", " ").replace("-", " ")])
    tops = [t.strip().lower() for t in (topics or "").split(",") if t.strip()]
    pts = 0
    why = []
    for t in tops:
        if t in CONFIG_TOPICS or any(c in t for c in ("edtech", "education", "learning", "school",
                                                     "student", "teach", "course", "tutor")):
            pts += TOPIC_WEIGHT
            why.append("topic:%s+%d" % (t, TOPIC_WEIGHT))
    for term, rx in STRONG_RE:
        if rx.search(text):
            pts += STRONG_WEIGHT
            why.append("%s+%d" % (term, STRONG_WEIGHT))
    for term, rx in WEAK_RE:
        if rx.search(text):
            pts += WEAK_WEIGHT
            why.append("%s+%d" % (term, WEAK_WEIGHT))
    for term, rx in NEGATIVE_RE:
        if rx.search(text):
            pts += NEGATIVE_WEIGHT
            why.append("%s%d" % (term, NEGATIVE_WEIGHT))
    band = "KEEP" if pts >= KEEP_AT else "MARGINAL" if pts >= MARGINAL_AT else "DROP"
    return pts, band, ";".join(why) or "-"


def normalise(raw):
    s = raw.strip().strip("`,|").rstrip("/")
    for pre in ("https://github.com/", "http://github.com/", "github.com/"):
        if s.lower().startswith(pre):
            s = s[len(pre):]
            break
    if s.endswith(".git"):
        s = s[:-4]
    parts = [p for p in s.split("/") if p]
    return "/".join(parts[:2]) if len(parts) >= 2 else ""


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--sweep", required=True,
                    help="TSV from p868-org-sweep.sh: vein,address,owner_type,stars,forks,"
                         "licence,pushed,archived,default_branch,description,topics")
    ap.add_argument("--org-only", action="store_true",
                    help="keep only owner_type == Organization (p867's one changed parameter)")
    ap.add_argument("--against", help="file of hand-selected addresses, one per line")
    ap.add_argument("--tsv", help="write the per-address record here")
    a = ap.parse_args(argv)

    rows, seen = [], set()
    with open(a.sweep, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        idx = {name: i for i, name in enumerate(head)}
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < len(head):
                f += ["-"] * (len(head) - len(f))
            addr = f[idx["address"]]
            if a.org_only and f[idx["owner_type"]] != "Organization":
                continue
            if addr in seen:
                continue
            seen.add(addr)
            pts, band, why = score(f[idx["description"]], f[idx["topics"]], addr)
            rows.append((addr, f[idx["vein"]], pts, band, f[idx["stars"]], f[idx["licence"]],
                         f[idx["pushed"]], f[idx["description"]][:160], why))

    rows.sort(key=lambda r: (-r[2], -int(r[4]) if r[4].isdigit() else 0))
    counts = {}
    for r in rows:
        counts[r[3]] = counts.get(r[3], 0) + 1

    print("population: %d distinct%s" % (len(rows), " (Organization only)" if a.org_only else ""))
    for b in ("KEEP", "MARGINAL", "DROP"):
        print("  %-9s %4d" % (b, counts.get(b, 0)))

    if a.against:
        hand = {normalise(l) for l in open(a.against, encoding="utf-8") if normalise(l)}
        by_addr = {r[0]: r for r in rows}
        kept = {h for h in hand if h in by_addr and by_addr[h][3] == "KEEP"}
        marginal = {h for h in hand if h in by_addr and by_addr[h][3] == "MARGINAL"}
        dropped = {h for h in hand if h in by_addr and by_addr[h][3] == "DROP"}
        absent = hand - set(by_addr)
        adds = [r for r in rows if r[3] == "KEEP" and r[0] not in hand]
        print("\nagainst %s: %d hand-selected addresses" % (a.against, len(hand)))
        print("  KEEP      %d  (recall over the addresses this sweep re-found)" % len(kept))
        print("  MARGINAL  %d" % len(marginal))
        print("  DROP      %d  <- the predicate disagrees with the hand here" % len(dropped))
        print("  not in this sweep %d  (vein bodies differ; declared, not hidden)" % len(absent))
        for h in sorted(dropped):
            print("    DROP %-52s score=%d  %s" % (h, by_addr[h][2], by_addr[h][8][:70]))
        for h in sorted(absent):
            print("    ABSENT %s" % h)
        print("  ADDS %d addresses the hand did not select" % len(adds))
        for r in adds[:25]:
            print("    +%-52s score=%2d  %s" % (r[0], r[2], r[7][:64]))

    if a.tsv:
        with open(a.tsv, "w", encoding="utf-8") as out:
            out.write("address\tvein\tscore\tband\tstars\tlicence\tpushed\tdescription\treasons\n")
            for r in rows:
                out.write("\t".join(str(x) for x in r) + "\n")
        print("\nwrote %s" % a.tsv)
    return 0


if __name__ == "__main__":
    sys.exit(main())
