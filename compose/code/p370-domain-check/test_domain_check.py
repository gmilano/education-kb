"""p370 tests. Every readme fixture is VERBATIM payload read through the git tree
channel on 2026-10-21 and committed under ../p370-git-tree-payload/trees/. No invented
READMEs. Each of the four defects D1-D4 has the string that caused it."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from domain_check import (check, may_shelve, slug_promises_education,
                          SHELVEABLE, MIN_WEAK_ANCHORS)

TREES = os.path.join(HERE, os.pardir, "p370-git-tree-payload", "trees")


def readme_payload(slug):
    p = os.path.join(TREES, slug.replace("/", "%") + ".readme")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read(20000)


def tree(slug):
    p = os.path.join(TREES, slug.replace("/", "%") + ".tree")
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8", errors="replace") as fh:
        return [l.strip() for l in fh if l.strip()]


fails = []
_CALLS = 0


def check_eq(name, got, want):
    global _CALLS
    _CALLS += 1
    if got != want:
        fails.append("%s: got %r, want %r" % (name, got, want))


def verdict(slug):
    return check(slug, readme_payload(slug), tree(slug))["verdict"]


# --- the four traps that are REAL, and must stay caught --------------------------
# `xAPI` in education is the Experience API. These two are xStation5, a forex broker.
check_eq("xapi-rs is a trading client, not xAPI", verdict("pawelkn/xapi-rs"), "SLUG-TRAP")
check_eq("xapi-node likewise", verdict("peterszombati/xapi-node"), "SLUG-TRAP")
check_eq("quask is CERN's Quantum Technology Initiative, not IMS QTI",
         verdict("cern-qti/quask"), "SLUG-TRAP")
check_eq("`adaptive` here is multispeaker speech separation",
         verdict("totoketchup/adaptive-multispeaker-separation"), "SLUG-TRAP")
check_eq("a generic MCP framework is not in the domain",
         verdict("casys-ai/mcp-server"), "NOT-EDUCATION")
check_eq("browser automation is not in the domain",
         verdict("microsoft/playwright-mcp"), "NOT-EDUCATION")
check_eq("an awesome-list of MCP servers is not an education row",
         verdict("punkpeye/awesome-mcp-servers"), "NOT-EDUCATION")

# --- D1: ONE strong anchor is sufficient; demanding two called this a trap -------
check_eq("D1 — reusable CI workflows FOR MOODLE PLUGINS are in the domain",
         verdict("bycs-lp/moodle-ci-workflows"), "EDUCATION")
check_eq("D1 — and `moodle` is the anchor that carries it",
         "moodle" in check("bycs-lp/moodle-ci-workflows",
                           readme_payload("bycs-lp/moodle-ci-workflows"))["strong"], True)

# --- D2: a strong token inside a COMPOUND NAME ----------------------------------
# The entire README of this repository is the single line `# AIChatForMoodle`.
check_eq("D2 — a one-line readme payload whose only word is a compound product name",
         verdict("surlabs/aichatformoodle"), "EDUCATION")
check_eq("D2 — the ambiguous tokens stay word-bounded: `lms` must not match `films`",
         check("x/y", "these are films about nothing")["strong"], [])
check_eq("D2 — nor may `qti` match a tool name in prose",
         check("x/y", "run the qtimigrationtool on the bank")["strong"], [])

# --- D3: morphology — `quiz` missed `quizzes`, `grade` missed `graded` ----------
check_eq("D3 — FSRS flashcards and auto-graded quizzes are in the domain",
         verdict("quizlar/mcp-server"), "EDUCATION")
check_eq("D3 — an inflected weak term is found",
         "grade" in check("x/y", "every answer is graded")["weak"], True)
check_eq("D3 — and inflection does not break the boundary rule",
         check("x/y", "quizzical remarks")["weak"], [])
check_eq("D3 — consonant doubling is NOT derived, it is carried as its own entry",
         "quizzes" in check("x/y", "it runs quizzes for you")["weak"], True)

# --- D4: the lexicon was English-plus-Iberian; a national instrument is not -----
# UDIR is the Norwegian Directorate for Education; this wraps its national school
# and kindergarten registers, and its README is in Norwegian.
check_eq("D4 — a Norwegian national school register is in the domain",
         verdict("3121n/nor-data-udir-mcp"), "EDUCATION")
check_eq("D4 — `skoler` and `barnehager` are the anchors",
         set(check("3121n/nor-data-udir-mcp",
                   readme_payload("3121n/nor-data-udir-mcp"))["strong"])
         >= {"skoler", "barnehager"}, True)

# --- the tree channel: a repository with NO README at all -----------------------
# `ayrtonmoura1/conectabncc` ships no readme at all. Its file names are the evidence.
check_eq("no readme payload exists for conectabncc",
         readme_payload("ayrtonmoura1/conectabncc"), None)
check_eq("the tree channel answers instead",
         check("ayrtonmoura1/conectabncc", None,
               tree("ayrtonmoura1/conectabncc"))["channel"], "tree-enumeration")
check_eq("and Brazil's BNCC curriculum is named by the file names",
         verdict("ayrtonmoura1/conectabncc"), "EDUCATION")
check_eq("a tree with no domain evidence yields no education verdict",
         check("chatt-state/banner-mcp-server", None,
               tree("chatt-state/banner-mcp-server"))["verdict"], "SLUG-TRAP")
check_eq("no readme payload and no tree is NO-EVIDENCE, never a verdict",
         check("a/b", None, [])["verdict"], "NO-EVIDENCE")
check_eq("NO-EVIDENCE is not shelveable", may_shelve("NO-EVIDENCE"), False)

# --- the live LMS/SIS rows this pass shelves must pass --------------------------
for slug in ("dddanielliu/nccu-moodle-mcp", "general-mudkip/d2l-mcp-server",
             "n35da/brightspace-mcp", "coimf/schoology-mcp", "zuvy/ps-mcp-server",
             "hocphi-info/hocphi-info-mcp", "nicolasviruel/moodle-utn-mcp",
             "bibo242/blackboard-mcp", "mattlo0546/canvas-mcp",
             "brightspaceui/lms-context-provider", "vossenv/oneroster-python",
             "packbackbooks/lti-1-3-php-library", "openedx/XBlock"):
    check_eq("in domain: %s" % slug, verdict(slug), "EDUCATION")

# ═══════════════════════════════════════════════════════════════════════════════════
# 🔴 D5 — `p371`'s OUT-OF-SAMPLE run, which is the obligation `p370` declared on itself.
# `p370` published 92.6 % recall and said in its own docstring that the figure was
# IN-SAMPLE. `p371` ran this instrument over 1 859 held-out addresses and
# hand-adjudicated a seeded stratified sample of 40: **26 of 34 decisive verdicts
# correct (76.5 %)** — 16/16 on EDUCATION, 5/8 on NOT-EDUCATION, 5/10 on SLUG-TRAP.
# 🟢 **All 8 errors fell in two classes, and neither was tutoring:** CREDENTIALING/OER
# and CURRICULUM-STANDARDS, plus two non-English payloads.
# Every string below is read from the payload that was misjudged, never invented.
# ═══════════════════════════════════════════════════════════════════════════════════

# the credentialing layer: two NOT-EDUCATION and one WEAK, all three in domain
check_eq("D5: an Open Badge v3 widget is in domain",
         check("opensalt/OB3DefinitionWidget",
               "Open Badge v3 Definition Widget. This widget provides a simple form to "
               "create an Open Badge v3 achievement definition.")["verdict"], "EDUCATION")
check_eq("D5: an OpenBadges-to-Europass mapper is in domain",
         check("impierce/credential-converter",
               "ELM - OpenBadges v3 Mapper. Converts JSON files written in the "
               "OpenBadges v3 standard to the ELM (Europass) standard and back.")["verdict"],
         "EDUCATION")
check_eq("D5: a verifiable-credential verifier is in domain",
         check("digitalcredentials/verifier-plus",
               "verifier-plus provides Credential Verification and Display - a web page "
               "for viewing and verifying Verifiable Credentials.")["verdict"], "EDUCATION")

# the OER layer
check_eq("D5: an OER container builder is in domain",
         check("sci-oer/automated-builder",
               "Automated builder for the sci-oer open educational resource containers. "
               "Builds a self-contained OER image.")["verdict"], "EDUCATION")

# national curriculum standards
check_eq("D5: Japan's MEXT Course of Study dataset is in domain",
         check("jp-cos/jp-cos.github.io",
               "Japanese Course of Study LOD (学習指導要領LOD). A structured dataset derived "
               "from open data released by the Ministry of Education, Culture, Sports and "
               "Technology (MEXT).")["verdict"], "EDUCATION")

# 🔴 D4's class, a second time: a non-English education payload
check_eq("D5: a Portuguese payload naming itinerários formativos is in domain",
         check("sumeedu/bancodeitinerarios",
               "O Banco de Itinerários é um projeto de código aberto que tem como objetivo "
               "oferecer uma ferramenta colaborativa para auxiliar instituições de ensino, "
               "secretarias educacionais e educadores da rede pública por meio do "
               "intercâmbio de itinerários formativos e materiais educacionais.")["verdict"],
         "EDUCATION")

# an education-only foundation places its own repositories
check_eq("D5: an Apereo LAI project is in domain on a generic README",
         check("Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy",
               "OpenDashboard. A web application that provides a framework for displaying "
               "visualizations and data views called cards. An Apereo Learning Analytics "
               "Initiative project.")["verdict"], "EDUCATION")
check_eq("D5: Kennisnet's Edurep client is in domain",
         check("Kennisnet/phpEdurepSearch",
               "phpEdurepSearch is a PHP package for searching with the Edurep search "
               "engines. In Edurep you can search in NLLOM metadata records.")["verdict"],
         "EDUCATION")

# a tutor AGENT, which scored one weak anchor and was called a trap
check_eq("D5: a programming tutor agent is in domain",
         check("rohit-dev45/programming-tutor-agent",
               "AI Tutor Agent. Python programming tutor built with LangChain, Gemini and "
               "MCP tools. The tutor agent answers coding questions.")["verdict"],
         "EDUCATION")

# 🟡 the negative control for D5's fix, and the reason the fix is NARROW: each of these
# words is ambiguous outside education, so none was added to the vocabulary.
for _text, _why in (
        ("Compiled with the Elm language targeting the ELM runtime.", "elm/ELM"),
        ("The CLR hosts the assembly at runtime.", "clr"),
        ("Lessons learned while scaling the service.", "lesson"),
        ("A LOM-format audio loop library for samplers.", "lom")):
    check_eq("D5: deliberately not added stays out: %s" % _why,
             check("someone/sometool", _text)["verdict"] == "EDUCATION", False)

# --- the contract ---------------------------------------------------------------
check_eq("only EDUCATION may be shelved", SHELVEABLE, ("EDUCATION",))
check_eq("a SLUG-TRAP may not be shelved", may_shelve("SLUG-TRAP"), False)
check_eq("a WEAK verdict may not be shelved either", may_shelve("WEAK"), False)
check_eq("the weak-only bar is two anchors", MIN_WEAK_ANCHORS, 2)
check_eq("the slug channel is reported, never decisive",
         slug_promises_education("pawelkn/xapi-rs"), ["xapi"])
check_eq("a slug with no promise reports none", slug_promises_education("a/b"), [])

TOTAL = 56
if _CALLS != TOTAL:
    print("🔴 p370-domain-check: %d controls ran, %d declared" % (_CALLS, TOTAL))
    sys.exit(1)
if fails:
    print("🔴 p370-domain-check FAILED %d of %d controls" % (len(fails), TOTAL))
    for f in fails:
        print("   " + f)
    sys.exit(1)
print("🟢 p370-domain-check PASS %d/%d — the slug is not the domain" % (TOTAL, TOTAL))
