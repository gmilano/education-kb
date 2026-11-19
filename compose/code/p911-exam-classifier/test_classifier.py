#!/usr/bin/env python3
"""p911 — controls for the national-exam education classifier.

Every case below is a MEASURED row from `evidence/p911-exam-rows.2026-11-19-p911.tsv`, not an
invented fixture.  The four `v1-false-positive` cases are the rows that made v1's published count
wrong, and they are kept as controls so no later pass can re-introduce the bare `learn`/`exam`/
`tutor`/`grade` keyword and still see a green suite.

Run: python3 -I test_classifier.py        (no network)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "ingest"))
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "p911chan",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..",
                 "ingest", "p911-exam-channel.py"))
chan = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chan)

# name, description, topics, query, bare_acronym, expect_v2, label
CASES = [
    # 🔴 the four classes that made v1 wrong.  All must be NOT-EDU under v2.
    ("jeelizFaceFilter", "Lightweight WebGL & JavaScript library for real-time multiple face tracking",
     ["webgl", "deep-learning", "face-detection"], "JEE", "JEE", False, "v1-false-positive: learn <- deep-learning"),
    ("WonderfulMatrices", "Wonderful Matrices to Build Small Language Models",
     ["machine-learning", "transformers"], "CAPS", "CAPS", False, "v1-false-positive: learn <- machine-learning"),
    ("awesome-go-orms", "A curated list with examples, benchmarks and tutorials",
     ["golang", "orm"], "matric", "matric", False, "v1-false-positive: exam <- example, tutor <- tutorial"),
    ("torch-optim", "Gradient accumulation and upgrade helpers for optimizers",
     ["pytorch"], "CBSE", "CBSE", False, "v1-false-positive: grade <- gradient/upgrade"),
    # 🟢 real education supply this channel found.  All must stay EDU.
    ("NAIJASCHOLAR", "Free, open-source exam prep for Nigerian students: JAMB, WAEC past questions",
     [], "WAEC exam", "WAEC", True, "real: Nigeria exam-prep"),
    ("ICFES-Exam-Engine", "App especializada en la generación de pruebas Saber-Icfes",
     [], "ICFES Saber", "ICFES", True, "real: Colombia item generation, Spanish"),
    ("RAG-Enhanced-NCERT-Tutor", "AI-powered tutor for NCERT textbook chapters",
     ["rag"], "NCERT", "NCERT", True, "real: India NCERT tutor"),
    ("KCSE-predictor", "Predicts exam topics by analyzing 20+ years of KCSE past papers",
     [], "KCSE exam", "KCSE", True, "real: Kenya past-paper analysis"),
    ("nias2", "National Schools Interoperability Programme validation and postprocessing",
     ["sif", "xml"], "NAPLAN", "NAPLAN", True, "real: p910's institutional row, the one a co-term filter removes"),
    # 🔵 the two-tier boundary, stated as a control rather than left implicit.
    ("quiz-cli", "A terminal quiz tool", [], "PAES", "PAES", True, "STRONG alone decides"),
    ("topic-test", "Test a topic", [], "PAES", "PAES", True, "two WEAK witnesses decide"),
    ("test-runner", "A fast test runner", [], "PAES", "PAES", False, "one WEAK witness is NOT a finding"),
    # 🔴 the term may never be its own evidence (p910's rule, re-asserted as a control).
    ("cbse-helper", "CBSE CBSE CBSE", [], "CBSE", "CBSE", False, "the acronym alone is not education context"),
    # 🔴 v2's two MEASURED false negatives, found by hand-adjudicating the 45 rows it removed.
    ("random-matrices-", "random matrices for teaching and exams", [], "matric exam", "matric",
     True, "v2-false-negative: the CO-TERM's word is evidence, not a self-match"),
    ("jee_mains_pyqs_data_base", "Tool to access and manage 14k+ jee main pyqs with semantic clustering",
     ["data-analysis"], "JEE mains", "JEE", True, "v2-false-negative: `pyq` is India's own word for a past paper"),
    ("Knec-John", "For KCSE 2025 exam material", [], "KCSE exam", "KCSE",
     True, "v2-false-negative: `KNEC` is Kenya's examinations council"),
    ("ALL-PYQ-Papers", "I am uploading all the State board papers", ["cbse", "jee-mains"], "JEE", "JEE",
     True, "vernacular + topics: board papers"),
    # 🔵 and the rule the fix must NOT break: the ACRONYM still may not be its own evidence.
    ("waec-stuff", "WAEC WAEC WAEC", [], "WAEC exam", "WAEC",
     False, "striking only the acronym must still strike the acronym"),
    # 🔴 v3's measured false-positive family: education CONTEXT is not education SUPPLY.
    ("ror-capstone-lifestyle", "RoR Capstone Project required at the end of Rails module in Microverse curriculum",
     [], "CAPS", "CAPS", False, "v3-false-positive: capstone + 'Microverse curriculum'"),
    ("MV-Capstone-1-Module-1", "This is the capstone project included in Microverse curriculum",
     [], "CAPS", "CAPS", False, "v3-false-positive: bootcamp portfolio piece"),
    # 🔵 and a real curriculum row must survive the guard.
    ("cbse-syllabus-tool", "Parses the CBSE curriculum into a question bank for teachers",
     [], "CBSE", "CBSE", True, "a real curriculum row is not caught by the capstone guard"),
]


def main(argv):
    if argv:
        sys.stderr.write("🔴 test_classifier.py takes no arguments.\n")
        return 2
    fails = []
    for name, desc, topics, q, bare, expect, label in CASES:
        ok, ev, tier = chan.is_edu_v2(name, desc, topics, q, bare)
        if ok != expect:
            fails.append(f"   🔴 {label}\n      {name!r} expected {expect}, got {ok} (tier={tier}, ev={ev})")
    # the v1 cases must additionally be shown to have FIRED under v1 — otherwise these
    # controls would pass vacuously and prove nothing about the defect they document.
    vacuous = []
    for name, desc, topics, q, bare, expect, label in CASES:
        if label.startswith("v1-false-positive"):
            if not chan.is_edu_v1(name, desc, topics, q, bare):
                vacuous.append(f"   🔴 {label}: v1 did NOT fire, so this control proves nothing")
    print(f"── p911-exam-classifier ({len(CASES)} field cases: 4 of v1's measured false "
          f"positives, 4 of v2's measured false negatives and 2 of v3's, all non-vacuous)")
    for v in vacuous:
        print(v)
    for f in fails:
        print(f)
    if fails or vacuous:
        print(f"🔴 FAIL — {len(fails)} wrong verdicts, {len(vacuous)} vacuous controls")
        return 1
    print(f"   PASS — {len(CASES)}/{len(CASES)}, and all 4 v1 controls fire under v1")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
