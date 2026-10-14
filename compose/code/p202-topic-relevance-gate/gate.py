#!/usr/bin/env python3
"""p202 — the relevance gate ACTION OO asked for, and the measurement that
decides how it may be used.

Gate a `topic:` page row by its DESCRIPTION alone, which is what the topic-page
channel gives (stars + description, no per-repo topic list). The gate answers
one question: does this description name education?

The counter-intuitive part, and the reason this is an instrument and not a
reminder: **bare "learning" is NOISE in an education KB.** It is the single most
common token in both education and machine learning, and on `topic:adaptive-
learning` the ML sense outnumbers the education sense. So "learning" is only ever
read inside a bounded phrase ("e-learning", "learning record", "adaptive
learning"), never alone -- and "machine/active/online/reinforcement learning"
are never education terms.

Offline. No network. No licence classification here: that is license_family.sh.
"""
import re

# Education vocabulary. Prefix-matched at a left word boundary, so "scorm" hits
# "SCORM1.2" and "educa" hits "education", "educational", "educacionais",
# "educativo". Bare "learn"/"learning" is deliberately ABSENT.
EDU_PREFIXES = [
    "educa", "teacher", "teaching", "student", "learner", "pedagog",
    "curricul", "course", "lecture", "lesson", "syllabus", "classroom",
    "school", "universit", "faculty", "instructor", "exam", "quiz",
    "assessment", "grading", "grade", "tutor", "proctor", "invigilat",
    "textbook", "homework", "academic", "enrol", "enroll", "study",
    "studying", "mooc", "scorm", "xapi", "moodle", "cmi5", "k-12", "k12",
    "edtech", "e-learning", "elearning",
]
# Terms that appear as the tail of a hyphen compound in which they mean nothing
# educational: "production-grade", "enterprise-grade", "military-grade". These
# need a left boundary that also excludes a hyphen. Measured defect, not a
# hypothetical: "Production-grade AI Mock Interview Platform" was the one noise
# row this gate admitted before the fix.
HYPHEN_COMPOUND_PRONE = ["grade", "grading"]
# Terms whose prefix is swallowed by a common unrelated word. "exam" inside
# "example" is the expensive one: "usage example" appears in a large share of
# all repo descriptions, so without this guard the gate reads half of GitHub as
# education. Measured defect, found by this suite.
RIGHT_GUARD = {"exam": r"(?!ple)"}
# Multi-word terms, whitespace- or hyphen-separated.
EDU_PHRASES = [
    "learning management", "learning record", "learning analytics",
    "learning resource", "learning objective", "learning technolog",
    "adaptive learning", "distance learning", "blended learning",
    "knowledge tracing", "instructional design", "learning tools",
    "tin can", "open educational",
]
# Standards acronyms that must match as whole tokens -- "LTI" inside "PyLTI1p3"
# is not a claim about education, and "LRS" inside a word is not either.
EDU_ACRONYMS = ["lti", "lrs", "lms", "oer", "h5p", "edx", "ims"]

_SEP = r"[\s\-_/]+"


def _norm(text):
    return (text or "").lower()


def matched_terms(description):
    """Every education term the description names. Order is stable."""
    d = _norm(description)
    hits = []
    for p in EDU_PREFIXES:
        left = r"(?<![a-z0-9-])" if p in HYPHEN_COMPOUND_PRONE else r"(?<![a-z0-9])"
        if re.search(left + re.escape(p) + RIGHT_GUARD.get(p, ""), d):
            hits.append(p)
    for ph in EDU_PHRASES:
        pat = _SEP.join(re.escape(w) for w in ph.split())
        if re.search(r"(?<![a-z0-9])" + pat, d):
            hits.append(ph)
    for a in EDU_ACRONYMS:
        if re.search(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", d):
            hits.append(a)
    return hits


def is_education(description):
    return bool(matched_terms(description))


def verdict(description):
    """KEEP / REVIEW. There is deliberately no REJECT: see the measurement.

    A description that names no education term is NOT evidence that the repo is
    off-topic -- an OER repo names its subject ("Programming with R"), not its
    pedagogy, and an empty description names nothing at all. So a non-match is
    an UNDECIDED row for a human or a second channel, never a rejection.
    """
    return "KEEP" if is_education(description) else "REVIEW"
