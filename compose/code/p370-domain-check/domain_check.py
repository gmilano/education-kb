#!/usr/bin/env python3
"""`p370-domain-check` — `Gap 475` / `ACTION ZZ-cb`: the SLUG is not the DOMAIN.

`p367` declared this gap and priced it as the cheapest one on the base:

    "An education-sounding slug is not an education repository, and nothing on this
     base checks the domain before shelving." — measured, a 40% trap rate on the
     permissive subset of p367's net-new class.

🔴 The two specimens `p367` named are the whole argument: `google/caliper` is a Java
microbenchmark harness, not 1EdTech's Caliper Analytics; `python-adaptive/adaptive` is
numerical function sampling, not adaptive learning. `p370` adds the sharpest pair yet:
`pawelkn/xapi-rs` and `peterszombati/xapi-node` are clients for **xStation5, a forex
broker's trading API** — in education `xAPI` is the Experience API, and a name match
between the two has nothing behind it. `cern-qti/quask` is CERN's **Quantum Technology
Initiative**, not IMS QTI.

🟢 THE RULE: the domain verdict is read from the README PAYLOAD, with the root-tree
ENUMERATION as the fallback channel, and NEVER from the slug. The slug is used for
exactly one thing — to decide whether a negative verdict is an ordinary miss or a TRAP
(a slug that *promises* education and a payload that does not deliver it).

Verdicts:
    EDUCATION        >= 1 STRONG anchor, or >= 2 distinct weak anchors with a slug promise
    WEAK             weak anchors only and no slug promise — a human adjudicates
    SLUG-TRAP        the SLUG carries an education token, the payload does not clear the bar
    NOT-EDUCATION    neither the slug nor the payload is in the domain
    NO-EVIDENCE      no readme payload and no informative tree; no verdict is available

🔴 FOUR DEFECTS IN THIS INSTRUMENT'S OWN FIRST DRAFT, each found by hand-adjudicating
its 15 `SLUG-TRAP` verdicts on `p370`'s 63-slug population, and each fixed here:

  D1  a single STRONG anchor was not sufficient — the first draft demanded two anchors
      of ANY kind, so `bycs-lp/moodle-ci-workflows` ("reusable workflows for the Moodle
      plugins of bycs-lp") was called a trap on the word `moodle`. If a term needs
      corroboration it is not strong; the two-anchor rule now applies only to the
      weak-only path.
  D2  a word boundary hides a strong token inside a COMPOUND NAME —
      `surlabs/aichatformoodle`, whose entire README is the single line
      `# AIChatForMoodle`, matched nothing, because `moodle` there is preceded by a
      letter. The unambiguous product names are now matched as substrings; the
      ambiguous ones (`lms`, `qti`, `canvas`, `banner`, `k12`) stay word-bounded,
      because that is what stops `qtimigrationtool`-style accidents.
  D3  no morphology — `quiz` missed `quizzes` and `grade` missed `graded`, so
      `quizlar/mcp-server` ("auto-graded quizzes", FSRS flashcards) scored one anchor.
      ASCII terms now tolerate a trailing `s|es|d|ed|ing` (a stem ending in `e` takes
      the bare `d`: `grade` -> `graded`), and the vocabulary gained the
      terms the adjudication showed were missing (`flashcard`, `competency`,
      `school district`, `spaced repetition`).
      🟡 The inflection rule does NOT cover English consonant doubling: `quiz` +
      `zes` is not `quiz` + `es`, so `quizzes` is carried as its own vocabulary entry
      rather than pretended to be derived. A rule that claimed to cover it would be
      wrong about `bus`/`buses` in the other direction, and this instrument does not
      need a stemmer to answer a yes/no domain question.
  D4  the lexicon was English-plus-Iberian, so a NATIONAL instrument in any other
      language reads as out-of-domain. `3121n/nor-data-udir-mcp` wraps the Norwegian
      Directorate for Education's **national school register** and its README is in
      Norwegian (`skoler`, `barnehager`) — the instrument called it a trap. 🔵 This is
      `Gap 476`/`ACTION ZZ-cc` arriving from the other direction: the same monolingual
      assumption that made the EMEA and APAC region legs return analyst prose also
      made the domain filter blind to the national instruments those legs exist to
      find. School-and-pupil terms for the languages of this base's four regions are
      now in `STRONG`.

🟡 HONESTY ABOUT THE FIX, stated because the number is otherwise misleading: all four
defects were derived from THIS pass's 63-slug sample, so the post-fix precision is an
IN-SAMPLE figure. It is published as such, and the out-of-sample run is this
instrument's next obligation, not a result it already has.

No network (`gap 139`): the caller supplies README text and tree names.
"""
import re

#: Unambiguous product and standard names: matched as SUBSTRINGS (defect D2).
STRONG_SUBSTRING = (
    "moodle", "openedx", "open edx", "brightspace", "schoology", "powerschool",
    "oneroster", "scorm", "ellucian", "chamilo", "blackboard", "edx-platform",
    "learnworlds", "gradebook", "edufi", "edtech", "mooc",
    # 🔴 D5 (p371, OUT OF SAMPLE): two foundations whose entire output is education
    # software, and whose repositories therefore carry no other education token.
    # `Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy` was called a TRAP on a
    # README that says only *"a framework for displaying visualizations called cards"* —
    # Apereo is Sakai's and uPortal's foundation. `Kennisnet/phpEdurepSearch` likewise:
    # Kennisnet is the DUTCH NATIONAL EDUCATION ICT FOUNDATION and Edurep is its
    # learning-resource repository.
    "apereo", "kennisnet", "edurep", "nllom", "learnr",
)

#: Domain terms that need a word boundary — `lms` must not match `films`, `qti` must
#: not match a tool name, `canvas` and `banner` have famous non-education meanings.
STRONG_WORD = (
    "lms", "qti", "k-12", "k12", "sis", "lti", "xapi statement", "experience api",
    "canvas lms", "blackboard learn", "banner student", "learning management",
    "student information system", "learning record store", "caliper analytics",
    "ims global", "1edtech", "ed-fi", "edfi", "sis integration",
    "learning analytics", "knowledge tracing", "intelligent tutoring",
    "adaptive learning", "spaced repetition", "flashcard", "competency",
    "competencies", "school district", "course catalog", "course catalogue",
    "syllabus", "lesson plan", "curriculum", "curricular", "bncc", "cbse", "ncert",
    "pupil", "registrar", "coursework", "formative assessment", "summative assessment",
    "essay scoring", "rubric", "teacher", "classroom", "gradebook", "transcript",
    "higher education", "primary school", "secondary school", "kindergarten",
    # D4 — the national-language school-and-pupil terms of this base's four regions
    "skole", "skoler", "barnehage", "barnehager", "skola", "skolverket", "elev",
    "schule", "schüler", "lehrer", "lehrplan", "école", "élève", "enseignant",
    "scuola", "studente", "insegnante", "school", "leerling", "escola", "escuela",
    "colegio", "universidad", "universidade", "aluno", "alumno", "docente",
    "profesor", "professor", "学生", "学校", "教育", "授業", "학생", "학교",
    "छात्र", "विद्यालय", "शिक्षा", "طالب", "مدرسة", "öğrenci", "okul",
    "siswa", "sekolah", "học sinh", "trường học", "นักเรียน", "โรงเรียน",
    # ───────────────────────────────────────────────────────────────────────────────
    # 🔴 D5 (p371): THE CREDENTIALING, OER AND CURRICULUM-STANDARDS LAYER WAS ABSENT.
    # `p370`'s in-sample recall was 92.6 %; `p371` ran this instrument out of sample on
    # 1 859 addresses and hand-adjudicated a seeded sample of 40. **All 8 errors fell in
    # two classes and neither was tutoring.** Every term below was then read out of the
    # payload that the instrument had misjudged, never guessed:
    #
    #   opensalt/OB3DefinitionWidget        NOT-EDUCATION → "open badge", "achievement"
    #   impierce/credential-converter       NOT-EDUCATION → "openbadges", "europass"
    #   digitalcredentials/verifier-plus    WEAK          → "verifiable credential"
    #   sci-oer/automated-builder           NOT-EDUCATION → "oer"
    #   jp-cos/jp-cos.github.io             WEAK          → "course of study", "mext",
    #                                                       "ministry of education",
    #                                                       "学習指導要領"
    #   showlab/Code2Video                  WEAK          → "educational video"
    #   OpenIntroStat/ims-tutorials         SLUG-TRAP     → "learnr"
    #   sumeedu/bancodeitinerarios          SLUG-TRAP     → "itinerários formativos",
    #                                                       "instituições de ensino"
    #   rohit-dev45/programming-tutor-agent SLUG-TRAP     → "tutor agent"
    #
    # 🟡 Deliberately NOT added, because each is ambiguous outside education and would
    # buy recall with precision: bare "elm" (a programming language), bare "clr" (the
    # .NET runtime), bare "lesson" ("lessons learned" is everywhere) and bare "lom".
    "open badge", "open badges", "openbadges", "verifiable credential",
    "verifiable credentials", "micro-credential", "microcredential",
    "digital credential", "comprehensive learner record", "learner record",
    "europass", "european learner model", "open educational resource",
    "open educational resources", "oer", "learning object metadata",
    "course of study", "学習指導要領", "mext", "ministry of education",
    "ministerio de educación", "ministério da educação", "educational video",
    "courseware", "course material", "course materials",
    "itinerário formativo", "itinerários formativos", "itinerarios formativos",
    "instituições de ensino", "instituciones educativas", "materiais educacionais",
    "secretarias educacionais", "secretaria de educação",
    "ai tutor", "tutor agent", "programming tutor", "math tutor", "tutoring system",
    "study assistant", "homework",
)

#: Terms consistent with education but common elsewhere. Two are needed, and only
#: with a slug promise, because on their own they describe half of GitHub.
WEAKISH = (
    "student", "course", "learner", "learning", "education", "educational", "school",
    "university", "college", "assignment", "quiz", "quizzes", "exam", "grade", "grading",
    "tutor", "tutoring", "enrol", "enroll", "academic", "campus", "faculty",
    "curso", "escolar", "educa", "ensino", "aprendiz", "aprendizaje",
)

#: Slug tokens that PROMISE the domain. A negative verdict on one of these is a TRAP.
SLUG_TOKENS = (
    "edu", "school", "student", "teacher", "course", "learn", "tutor", "lms",
    "moodle", "canvas", "blackboard", "brightspace", "d2l", "sakai", "lti", "scorm",
    "xapi", "oneroster", "qti", "caliper", "adaptive", "banner", "powerschool",
    "schoology", "classroom", "quiz", "grade", "exam", "academic", "khanacademy",
    "ncert", "cbse", "bncc", "udir", "skolverket", "escolar", "aluno", "alumno",
    "pedago", "campus", "curricul", "academy",
    # D5 (p371): the classes the out-of-sample run showed were missing
    "oer", "credential", "badge", "itinerario", "itinerário", "ensino", "apereo",
)

#: >= this many distinct weak anchors, on the weak-only path (defect D1).
MIN_WEAK_ANCHORS = 2

#: tolerated inflections on an ASCII term (defect D3)
_INFLECT = r"(?:s|es|d|ed|ing)?"


def _word_hits(text, terms):
    low = (text or "").lower()
    hits = []
    for t in terms:
        if t.isascii():
            pat = r"(?<![a-z0-9])" + re.escape(t) + _INFLECT + r"(?![a-z0-9])"
            if re.search(pat, low):
                hits.append(t)
        elif t in low:
            hits.append(t)
    return hits


def _substring_hits(text, terms):
    low = (text or "").lower()
    return [t for t in terms if t in low]


def slug_promises_education(slug):
    low = (slug or "").lower()
    return [t for t in SLUG_TOKENS if t in low]


def check(slug, readme_payload, tree_names=()):
    """-> {"verdict", "strong", "weak", "slug_tokens", "channel"}

    `tree_names` is the root-tree enumeration, used when there is no readme payload. It is a
    real channel, not a courtesy: `ayrtonmoura1/conectabncc` ships no README at all and
    its file names are `competencias_bncc.json`, `bncc_progressao_pre_requisitos.json`,
    `relacoes_bncc_final.json` — Brazil's national curriculum, stated by the tree.
    """
    promised = slug_promises_education(slug)
    tree_text = "\n".join(tree_names or ())
    # 🟡 The channel labels are `readme-payload` and `tree-enumeration`, not the bare
    # tokens, because `gate-ladder-case`'s path census reads a bare `readme` in code as a
    # path SPELLING and cannot tell a label from a path (its own `C21` draws the same line
    # for a method attribute). `p367` hit this on entry too. Labelling the channel for what
    # it is costs nothing and keeps the ratchet meaningful.
    channel = "readme-payload" if readme_payload else (
        "tree-enumeration" if tree_text else "none")
    body = readme_payload if readme_payload else tree_text
    if not body:
        return {"verdict": "NO-EVIDENCE", "strong": [], "weak": [],
                "slug_tokens": promised, "channel": "none"}

    strong = sorted(set(_substring_hits(body, STRONG_SUBSTRING)
                        + _word_hits(body, STRONG_WORD)))
    weak = sorted(set(_word_hits(body, WEAKISH)))

    if strong:
        verdict = "EDUCATION"
    elif len(weak) >= MIN_WEAK_ANCHORS and promised:
        verdict = "EDUCATION"
    elif promised:
        verdict = "SLUG-TRAP"
    elif len(weak) >= MIN_WEAK_ANCHORS:
        verdict = "WEAK"
    else:
        verdict = "NOT-EDUCATION"
    return {"verdict": verdict, "strong": strong, "weak": weak,
            "slug_tokens": promised, "channel": channel}


SHELVEABLE = ("EDUCATION",)


def may_shelve(verdict):
    """🔴 Only an EDUCATION verdict may be shelved as an industry row. A `WEAK`,
    `SLUG-TRAP`, `NOT-EDUCATION` or `NO-EVIDENCE` verdict needs a human to say, in
    writing, why the row belongs — which is the whole point of `Gap 475`."""
    return verdict in SHELVEABLE
