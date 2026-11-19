#!/usr/bin/env python3
"""p911 -- the national-examination channel, run BOTH ways, as p910-G1 registered it.

p910 measured this channel on 14 APAC/EMEA terms and found the bare acronym tier is 63%
homonym noise, which one co-term takes to 4%.  It then measured the co-term's RECALL COST:
`NAPLAN assessment` returned 3 repositories and 0 education rows, while the one real
institutional artefact in the Australian leg (`nsip/nias2`, Apache-2.0, the National Schools
Interoperability Programme) appears ONLY on the bare term.  The gate it registered:

    the national-exam channel must be run BOTH ways -- bare for recall, co-termed for
    precision -- and the bare run must be read rather than filtered, because the thing a
    filter removes is exactly the institutional tier a studio wants.

p910 ran the instrument ad hoc and committed no script, so `p907`-`p909`'s "named but
untried" failure could repeat.  This file is the instrument.  It discharges `906-G2`'s
remaining markets: India, Nigeria, Kenya, South Africa, Chile, Germany (named by p910) plus
Mexico (`p904`'s largest supply-side hole, `EXANI` never re-run).

Two properties this script has and p910's ad-hoc run could not prove it had:

  * It REFUSES EMPTY INPUT (`main([]) -> 2`).  `Gap 243`/`Gap 245` recorded 23 instruments in
    this tree that reported success over nothing; `p383` printed `total 0` and exited `0`.
    An instrument that can report a 0% collision rate over 0 queries is worse than no
    instrument, because the number looks like a measurement.
  * `default_branch` is taken from the search channel per repository and never guessed.
    `p906` regressed the `884-G2` fix by hardcoding `{main, master}`; two of p910's 28 grant
    reads were on `master` and would have been invisible again.

Channels: `gh api search/repositories` only.  No byte-read happens here -- promotion rows are
byte-read by `ingest/p880-licence-byteread.sh`, which classifies licence families
CUMULATIVELY.  `spdx_id` from this script SCREENS; it never decides (`906-G1`).

Usage: p911-exam-channel.py ROWS.tsv SUMMARY.tsv
"""
import json
import subprocess
import sys
import time

# (market, region, bare term, co-termed term).  `region` is the CLOSED vocabulary the
# compiler reads: North America | EMEA | APAC | LATAM | Global.  Country goes in `market`.
TERMS = [
    ("India",        "APAC",  "CBSE",      "CBSE syllabus"),
    ("India",        "APAC",  "NCERT",     "NCERT textbook"),
    ("India",        "APAC",  "JEE",       "JEE mains"),
    ("India",        "APAC",  "NEET",      "NEET exam"),
    ("Nigeria",      "EMEA",  "WAEC",      "WAEC exam"),
    ("Nigeria",      "EMEA",  "JAMB",      "JAMB cbt"),
    ("Kenya",        "EMEA",  "KCSE",      "KCSE exam"),
    ("South Africa", "EMEA",  "matric",    "matric exam"),
    ("South Africa", "EMEA",  "CAPS",      "CAPS curriculum"),
    ("Germany",      "EMEA",  "Abitur",    "Abitur Mathematik"),
    ("Chile",        "LATAM", "PAES",      "PAES prueba"),
    ("Mexico",       "LATAM", "EXANI",     "EXANI examen"),
    ("Mexico",       "LATAM", "COMIPEMS",  "COMIPEMS examen"),
    ("Colombia",     "LATAM", "ICFES",     "ICFES Saber"),
]

# Education context is judged on name + description + topics.  The exam acronym itself is
# EXCLUDED from the evidence (p910's rule): a row that matches only the acronym matches
# trivially, and the measurement is how many rows carry education context BESIDES the
# acronym that found them.
#
# 🔴 v1 of this classifier (the one p910 ran, and the first cut of this file) was WRONG, and the
# defect is published rather than quietly fixed: `jeeliz/jeelizFaceFilter` -- a WebGL face-tracking
# library, 2,957 stars -- classified as education supply because `learn` matches `deep-learning`
# in its GitHub topics.  58 of v1's 263 education verdicts (22%), over 56 distinct repositories,
# rest ONLY on keywords with a
# software-domain homonym: `learn` <- machine/deep/reinforcement learning, `exam` <- example,
# `tutor` <- tutorial, `grade` <- gradient/upgrade/gradle.  An education KB that published v1's
# count would have shelved a face-tracking library as Indian exam-prep supply -- p910's own
# Minecraft-NBT failure mode, arriving through the CLASSIFIER instead of the query.
#
# v2 does two things v1 did not:
#   1. STRIPS known software-domain phrases from the haystack before matching, so the homonym
#      cannot supply the evidence.
#   2. Grades on TWO TIERS.  A STRONG term (a word that is not plausibly about software) decides
#      alone; a WEAK term needs a second witness.  One ambiguous word is not a finding.
# Both classifiers run on every row and both verdicts are written out, because the DELTA between
# them is this pass's measurement of how much a published collision rate depends on its classifier.

# v1's flat keyword list, kept verbatim so the delta between the two classifiers is
# reproducible from this file alone and not merely asserted in prose.
EDU_V1 = [
    "exam", "school", "student", "study", "studie", "learn", "teach", "tutor", "curricul",
    "syllabus", "textbook", "quiz", "question", "past paper", "pastpaper", "revision",
    "education", "educa", "mock test", "test prep", "testprep", "prep", "course", "lesson",
    "classroom", "grade", "grading", "academy", "academic", "flashcard", "marking",
    "assessment", "aprendiz", "ensino", "escola", "escuela", "colegio", "docente", "prueba",
    "examen", "prova", "vestibular", "simulado", "tarea", "schule", "lernen", "unterricht",
    "aufgaben", "pupil", "homework", "coaching", "university admission", "entrance",
    "scholar", "cbt", "olympiad", "worksheet", "mcq", "ncert", "tuition",
]

# Collisions p910 catalogued plus the ones these markets predict.  Recorded, not filtered:
# the counter exists so the SHAPE of the noise is publishable, not just its rate.
NOISE = {
    "JEE": ["java", "jakarta", "ejb", "j2ee", "servlet", "glassfish", "wildfly", "maven"],
    "CAPS": ["capslock", "caps lock", "uppercase", "capability", "capabilities", "capsule",
             "capture", "bottlecap"],
    "matric": ["matrix", "matrices", "matrik", "linear algebra"],
    "NEET": ["anime", "weeb", "hikikomori", "shitpost"],
    "PAES": ["paessler", "package", "paes cipher", "block cipher"],
}

# Phrases removed before matching.  Each one is a measured false positive, not a precaution.
HOMONYM_PHRASES = [
    "machine learning", "deep learning", "reinforcement learning", "transfer learning",
    "federated learning", "supervised learning", "unsupervised learning", "self-supervised",
    "contrastive learning", "representation learning", "in-context learning", "few-shot learning",
    "zero-shot learning", "meta-learning", "active learning", "online learning", "q-learning",
    "curriculum learning", "learning rate", "learning algorithm", "learning model",
    "scikit-learn", "learn more", "deep-learning", "machine-learning", "ml/dl",
    "example", "examples", "examine", "examining", "for exam ple",
    "tutorial", "tutorials",
    "gradient", "gradients", "upgrade", "upgrades", "degrade", "gradle", "gradio",
    "preprocess", "preprocessing", "prepare", "prepared", "preparing", "prepend",
    "concourse", "classify", "classifier", "classification",
    # 🔴 Third measured false-positive family, found in the PERMISSIVE shelf candidates: the bare
    # `CAPS` leg returns `capstone`, and a bootcamp's "Microverse curriculum" then supplies the
    # STRONG term `curricul`.  11 of the 54 permissive education rows v1 accepts are
    # Microverse portfolio projects.  They have education CONTEXT and are not education SUPPLY —
    # a studio cannot build on someone's HTML-module portfolio piece — so the distinction is
    # enforced here rather than left to a reader.
    # Longest first: the list is applied in order, and stripping `microverse` alone would leave
    # `curriculum` behind to supply the STRONG term on its own.
    "microverse curriculum", "bootcamp curriculum", "microverse main technical curriculum",
    "capstone project", "capstone", "microverse", "bootcamp", "portfolio project",
]

# STRONG: not plausibly about software.  One is enough.
STRONG = [
    "student", "school", "escuela", "escola", "colegio", "schule", "schüler", "pupil",
    "education", "educa", "educativ", "bildung", "syllabus", "textbook", "curricul",
    "classroom", "lehrplan", "teacher", "docente", "profesor", "lehrer", "tuition",
    "past paper", "pastpaper", "question bank", "questionbank", "quiz", "flashcard",
    "exam prep", "test prep", "testprep", "exam paper", "examination", "examen", "exame",
    "prueba", "prova", "vestibular", "simulado", "olympiad", "mock test", "mock exam",
    "revision", "homework", "aufgaben", "unterricht", "lernen", "aprendizaje", "ensino",
    "coaching", "scholarship", "university admission", "entrance exam", "worksheet",
    "mcq", "multiple choice", "cbt", "grading", "marking scheme", "rubric", "tutoring",
    "lesson", "academy", "academic",
    # 🔴 Vernacular tier, added after hand-adjudicating the 45 rows v2 removed.  A classifier
    # built from English education vocabulary UNDER-READS this supply, because each market has
    # its own word for a past paper: India writes `pyq` (previous year question), the CBSE board
    # exam is `AISSCE`, Kenya's board is `KNEC`, Nigeria's sibling board is `NECO`.  This is
    # `T20`'s lesson ("vernacular agents are not translations of English ones") arriving in the
    # CLASSIFIER.  None of these is a queried term, so none is a trivial self-match.
    "pyq", "aissce", "knec", "neco", "upsc", "board exam", "past question",
    "question paper", "grade12", "grade 12", "saber 11", "saber11", "bachillerato",
    "secundaria", "primaria", "simulacro", "repaso", "preparacion", "preparación",
    "anki", "deck", "study app", "e-exam", "oberstufe", "klausur", "gymnasium",
]
# WEAK: ambiguous in a software corpus.  Needs a second witness (STRONG or another WEAK).
WEAK = [
    "exam", "learn", "study", "studies", "teach", "tutor", "course", "grade", "prep",
    "question", "assessment", "test", "subject", "chapter", "topic", "practice", "tarea",
]


def _hay(name, desc, topics, term, bare=None):
    """p910's rule is that the queried term may not be its own evidence.  🔴 That rule was
    written for BARE ACRONYMS and is WRONG when applied to a co-term: on `WAEC exam` it strips
    the word `exam`, which is the strongest education signal the row has.  Measured cost of
    getting this wrong: `macbuse/random-matrices-` ("random matrices for teaching and exams")
    graded NOT-EDU on the `matric exam` leg because `exam` had been removed from its own
    description.  So only the ACRONYM is struck out; the co-term's added word is evidence like
    any other, since it was not what made the row trivially match."""
    hay = f"{name} {desc or ''} {' '.join(topics or [])}".lower()
    for tok in (bare or term).lower().split():
        hay = hay.replace(tok, " ")
    return hay


def is_edu_v1(name, desc, topics, term, bare=None):
    """The classifier p910 ran.  Kept so the delta is reproducible, NOT because it is right."""
    hay = _hay(name, desc, topics, term, bare)
    return [k for k in EDU_V1 if k in hay]


def is_edu_v2(name, desc, topics, term, bare=None):
    """Homonym-guarded, two-tier, acronym-only striking.  Returns (verdict, evidence, tier)."""
    hay = _hay(name, desc, topics, term, bare)
    for ph in HOMONYM_PHRASES:                # the homonym may not supply the evidence
        hay = hay.replace(ph, " ")
    strong = [k for k in STRONG if k in hay]
    weak = [k for k in WEAK if k in hay]
    if strong:
        return True, strong + weak, "STRONG"
    if len(weak) >= 2:
        return True, weak, "WEAK-PAIR"
    return False, weak, "WEAK-SINGLE" if weak else "NONE"


def api(q, per_page=25):
    """One search leg.  Returns (total_count, items).  A failure is returned as such -- it is
    never silently coerced to an empty result, because `0 hits` and `the query failed` are
    different facts and `Gap 253` is this tree's record of what conflating them costs."""
    cmd = ["gh", "api", "-X", "GET", "search/repositories", "-f", f"q={q}",
           "-f", "sort=stars", "-f", "order=desc", "-f", f"per_page={per_page}"]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if p.returncode != 0:
        return None, f"QUERY-FAILED rc={p.returncode} {p.stderr.strip()[:160]}"
    d = json.loads(p.stdout)
    return d.get("total_count"), d.get("items", [])


def is_edu(name, desc, topics, term):
    """Education context on name + description + topics, with the term's own tokens removed."""
    hay = f"{name} {desc or ''} {' '.join(topics or [])}".lower()
    for tok in term.lower().split():
        hay = hay.replace(tok, " ")
    return [k for k in EDU if k in hay]


def noise_hits(name, desc, bare):
    hay = f"{name} {desc or ''}".lower()
    return [k for k in NOISE.get(bare, []) if k in hay]


def main(argv):
    if len(argv) != 2:
        sys.stderr.write(
            "🔴 p911-exam-channel refuses to run without both output paths.\n"
            "   usage: p911-exam-channel.py ROWS.tsv SUMMARY.tsv\n"
            "   (p541/Gap 245: an instrument that exits 0 over no input publishes a\n"
            "    collision rate computed from nothing.)\n")
        return 2
    rows_path, summary_path = argv
    rows, summary, seen = [], [], {}

    for market, region, bare, coterm in TERMS:
        for kind, q in (("bare", bare), ("coterm", coterm)):
            total, items = api(q)
            time.sleep(2)
            if total is None:
                summary.append([market, region, bare, kind, q, "QUERY-FAILED", "", "", "",
                                "", "", str(items)])
                continue
            edu = edu_v1 = 0
            for it in items:
                name = it["full_name"]
                desc = it.get("description") or ""
                topics = it.get("topics") or []
                v1 = is_edu_v1(it["name"], desc, topics, q, bare)
                ok, hits, tier = is_edu_v2(it["name"], desc, topics, q, bare)
                noise = noise_hits(it["name"], desc, bare)
                if v1:
                    edu_v1 += 1
                if ok:
                    edu += 1
                lic = (it.get("license") or {}).get("spdx_id") or "NULL"
                rows.append([
                    market, region, bare, kind, q, name,
                    str(it.get("stargazers_count", 0)), lic,
                    it.get("default_branch") or "", (it.get("pushed_at") or "")[:10],
                    "EDU" if ok else "NOT-EDU", tier,
                    "EDU" if v1 else "NOT-EDU",
                    ",".join(hits[:5]), ",".join(v1[:5]), ",".join(noise[:3]),
                    ";".join(topics[:6]),
                    desc.replace("\t", " ").replace("\n", " ")[:160],
                ])
                if ok:
                    r = seen.setdefault(name, {"stars": it.get("stargazers_count", 0),
                                               "spdx": lic, "branch": it.get("default_branch"),
                                               "pushed": (it.get("pushed_at") or "")[:10],
                                               "markets": set(), "region": region})
                    r["markets"].add(market)
            n = len(items)
            summary.append([market, region, bare, kind, q, str(total), str(n), str(edu),
                            f"{(n - edu) / n * 100:.0f}%" if n else "n/a", str(edu_v1),
                            f"{(n - edu_v1) / n * 100:.0f}%" if n else "n/a", ""])

    with open(rows_path, "w") as f:
        f.write("market\tregion\tbare_term\tkind\tquery\trepo\tstars\tspdx_screen\t"
                "default_branch\tpushed\tverdict_v2\ttier\tverdict_v1\tevidence_v2\t"
                "evidence_v1\tnoise_evidence\ttopics\tdescription\n")
        for r in rows:
            f.write("\t".join(r) + "\n")

    with open(summary_path, "w") as f:
        f.write("market\tregion\tbare_term\tkind\tquery\tnominal_hits\tsampled\t"
                "education_context\tcollision\teducation_context_v1\tcollision_v1\tnote\n")
        for s in summary:
            f.write("\t".join(s) + "\n")

    print(f"🟢 p911 exam channel: {len(summary)} legs, {len(rows)} sampled rows, "
          f"{len(seen)} distinct education-context repositories.")
    print(f"   rows    -> {rows_path}")
    print(f"   summary -> {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
