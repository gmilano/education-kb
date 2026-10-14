#!/usr/bin/env python3
"""p202 — suite for the relevance gate. OFFLINE.

The loaded cases are the NEGATIVES: the homonyms that a naive education
vocabulary keeps. Every one of them was measured on a real topic page this
pass, not invented.
"""
import sys
sys.path.insert(0, ".")
from gate import is_education, matched_terms, verdict

checks = 0
fails = 0


def ck(cond, name):
    global checks, fails
    checks += 1
    if cond:
        print("ok   %s" % name)
    else:
        fails += 1
        print("FAIL %s" % name)


# --- the measured homonyms: every one must NOT be read as education ---
NOISE = [
    ("xcp-ng/xcp", "Entry point for issues and wiki. Also contains some scripts and sources."),
    ("vatesfr/xo", "Merged with monorepo https://github.com/vatesfr/xen-orchestra"),
    ("peterszombati/xapi-node", "xStation5 Trading API for NodeJS/JS"),
    ("jrgenerative/fixed-wing-sim", "Matlab implementation to simulate the non-linear dynamics of a fixed-wing unmanned areal glider."),
    ("kmilo17pet/qlibs", "A collection of useful libraries for embedded systems : signal smoothing, PID control, Fuzzy Logic"),
    ("loowid/loowid", "Webconference solution based on webrtc"),
    ("edmozley/freeitsm", "A completely free ITSM tool"),
    ("python-adaptive/adaptive", "Adaptive: parallel active learning of mathematical functions"),
    ("max-baz/wluma", "Automatic brightness adjustment based on screen contents and ALS"),
    ("codelion/adaptive-classifier", "A flexible, adaptive classification system for dynamic text classification"),
    ("cdslaborg/paramonte", "ParaMonte: Parallel Monte Carlo and Machine Learning Library for Python, MATLAB, Fortran, C++, C."),
    ("Western-OC2-Lab/PWPAE", "Data stream analytics: Implement online learning methods to address concept drift and model drift"),
    ("AkihikoWatanabe/paper_notes", "Daily notes on AI papers"),
    ("Bin-Cao/Bgolearn", "Offical implement of Bgolearn"),
    ("mingyuyng/Dynamic_JSCC", "Codes for Deep Joint Source-Channel Coding for Wireless Image Transmission with Adaptive Rate Control"),
    ("alipsgh/tornado", "The Tornado framework, designed and implemented for adaptive online learning and data stream mining in Python."),
    ("Tibsfox/gsd-skill-creator", "Introduces a comprehensive agent-based framework for guided software development (GSD)"),
    ("Blunde1/agtboost", "Adaptive and automatic gradient boosting computations."),
    ("Totoketchup/Adaptive-MultiSpeaker-Separation", "Adaptive and Focusing Neural Layers for Multi-Speaker Separation Problem"),
    ("mmalekzadeh/dana", "DANA: Dimension-Adaptive Neural Architecture (UbiComp21)( ACM IMWUT)"),
    ("chyp3r/KACHOW-Teknofest-2026", "Teknofest 2026 Dogal Dil Ajanlari Yarismasi 1. Senaryo kapsaminda gelistirilen"),
    ("theunstopabble/InterviewMinds", "Production-grade AI Mock Interview Platform with 81 service modules."),
]
for repo, desc in NOISE:
    ck(not is_education(desc), "NOISE rejected: %s %s" % (repo, matched_terms(desc) or ""))

# --- the regression that the first version of this gate FAILED ---
ck(not is_education("Production-grade AI Mock Interview Platform"),
   "P202 REGRESSION: 'production-grade' is not a grade")
ck(not is_education("enterprise-grade retrieval pipeline"),
   "P202 REGRESSION: 'enterprise-grade' is not a grade")
ck(is_education("the teacher reviews each grade before release"),
   "a real standalone 'grade' still matches")
ck(is_education("automated grading of student submissions"),
   "'grading' still matches")

# --- bare 'learning' must never carry the gate on its own ---
ck(not is_education("parallel active learning of mathematical functions"),
   "bare 'active learning' is NOT education")
ck(not is_education("online learning for concept drift"),
   "bare 'online learning' is NOT education")
ck(not is_education("a machine learning library"),
   "'machine learning' is NOT education")
ck(is_education("adaptive learning workspace that runs locally"),
   "'adaptive learning' as a contiguous phrase IS education")
ck(is_education("the ultimate Learning Record Store"),
   "'learning record' IS education")
ck(is_education("an open-source learning analytics platform"),
   "'learning analytics' IS education")

# --- acronyms bind as whole tokens, so a substring is not a claim ---
ck(not is_education("PyLTI1p3 Django usage example"),
   "'LTI' inside PyLTI1p3 does not match (whole-token acronym)")
ck(is_education("LTI 1.3 Advantage Tool"), "standalone 'LTI' matches")
ck(is_education("A simple SCORM1.2 SCO run-time test environment"),
   "'SCORM1.2' matches (prefix term)")

# --- multilingual: the vocabulary must not be English-only ---
ck(is_education("recursos educacionais abertos sobre calculo numerico"),
   "Portuguese 'educacionais' matches")
ck(is_education("plataforma educativa para estudiantes"),
   "Spanish 'educativa'/'estudiantes' matches")

# --- the contract: there is no REJECT verdict ---
ck(verdict("Image Processing with Python") == "REVIEW",
   "a non-match is REVIEW, never REJECT")
ck(verdict("") == "REVIEW", "an empty description is REVIEW, not a rejection")
ck(verdict("A modern SCORM JavaScript runtime library.") == "KEEP",
   "scorm-again is KEPT (the row ACTION OO named as the limb-2 risk)")

# --- 'exam' must not be read out of 'example' ---
ck(not is_education("PyLTI1p3 Django usage example"),
   "P202 REGRESSION: 'exam' inside 'example' does not match")
ck(not is_education("a minimal usage example and some scripts"),
   "P202 REGRESSION: 'example' alone is not an exam")
ck(is_education("online examination system prototype"),
   "'examination' still matches")
ck(is_education("Exam bubble sheet scorer"), "standalone 'Exam' still matches")

print()
print("%d/%d" % (checks - fails, checks))
sys.exit(1 if fails else 0)
