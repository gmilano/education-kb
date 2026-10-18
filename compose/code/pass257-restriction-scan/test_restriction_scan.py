"""Controls for `pass257-restriction-scan`.

Every fixture is a REAL payload read first-hand from `raw.githubusercontent.com` at
`p257` on an `ls-remote`-resolved ref, not text this base wrote for itself — which
is the gap `p255` named when `p252`'s hardening had only ever been tested against
its own fixtures.

Run from this directory (`p355-cwd-portability`: `python3 -I` strips the script's
directory from `sys.path`, so the suite only imports from its own cwd).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import restriction_scan as rs  # noqa: E402

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures-p257")

PASS = 0
FAIL = 0


def check(name, got, want):
    global PASS, FAIL
    if got == want:
        PASS += 1
    else:
        FAIL += 1
        print(f"FAIL {name}\n     got  {got!r}\n     want {want!r}")


def truthy(name, got):
    global PASS, FAIL
    if got:
        PASS += 1
    else:
        FAIL += 1
        print(f"FAIL {name}: expected truthy, got {got!r}")


def load(fname):
    with open(os.path.join(FIX, fname), encoding="utf-8", errors="replace") as fh:
        return fh.read()


USC = load("usc-academic-1812.txt")
APACHE = load("apache-2.0-11356.txt")
GPL = load("gpl-3.0-35146.txt")
MIT = load("mit-1091.txt")
NOTFOUND = load("notfound-14.txt")

# ── 1. The USC academic licence: restricted, and SAID to be restricted ───────────
usc = rs.scan(USC)
check("usc.verdict", usc["verdict"], rs.VERDICT_RESTRICTED)
check("usc.family", usc["family"], None)
check("usc.bytes", usc["bytes"], 1812)
check("usc.usable", rs.is_usable_permissive(USC), False)
# 🔴 The whole point: the EVIDENCE is non-empty.  `p1054` reports `[]` here.
truthy("usc.hits non-empty", len(usc["hits"]) > 0)
for token in ("non-profit", "commercial use", "research purposes",
              "all rights reserved", "without a written agreement"):
    truthy(f"usc.hits carries {token!r}", token in usc["hits"])

# ── 2. Verbatim Apache-2.0: permissive, and not confused with the above ─────────
ap = rs.scan(APACHE)
check("apache.verdict", ap["verdict"], rs.VERDICT_PERMISSIVE)
check("apache.family", ap["family"], "Apache-2.0")
check("apache.bytes", ap["bytes"], 11356)
check("apache.hits", ap["hits"], ())
check("apache.usable", rs.is_usable_permissive(APACHE), True)

# ── 3. Verbatim GPL-3.0: the benign-hit trap, measured ──────────────────────────
gpl = rs.scan(GPL)
check("gpl.family", gpl["family"], "GPL")
check("gpl.verdict", gpl["verdict"], rs.VERDICT_COPYLEFT)
# The token IS present and IS reported — it is simply not EFFECTIVE for this family.
check("gpl.hits", gpl["hits"], ("noncommercial",))
check("gpl.benign_hits", gpl["benign_hits"], ("noncommercial",))
check("gpl.effective_hits", gpl["effective_hits"], ())
check("gpl.usable", rs.is_usable_permissive(GPL), False)

# ── 4. Verbatim MIT: agrees with p1054 by construction ──────────────────────────
mit = rs.scan(MIT)
check("mit.family", mit["family"], "MIT")
check("mit.verdict", mit["verdict"], rs.VERDICT_PERMISSIVE)
check("mit.usable", rs.is_usable_permissive(MIT), True)

# ── 5. The 404 body is never a grant ────────────────────────────────────────────
nf = rs.scan(NOTFOUND)
check("notfound.bytes", nf["bytes"], 14)
check("notfound.family", nf["family"], None)
check("notfound.verdict", nf["verdict"], rs.VERDICT_UNCLASSIFIED)
check("notfound.usable", rs.is_usable_permissive(NOTFOUND), False)

# ── 6. THE REGRESSION CONTROL — these six assertions FAIL against p1054 ─────────
# They are the measurement that justifies this instrument existing, kept as code so
# a later pass cannot re-derive the defect by hand.  `p1054` is imported if it is
# reachable; if it is not, the controls are declared SKIPPED rather than passed.
P1054 = os.path.join(os.path.dirname(FIX), "..", "p1054-mit-plus-clause")
_p1054_ok = False
if os.path.isdir(P1054):
    sys.path.insert(0, os.path.abspath(P1054))
    try:
        import mit_plus  # noqa: E402

        _p1054_ok = True
    except Exception as exc:  # pragma: no cover - reported, never swallowed
        print(f"NOTE p1054 unimportable ({exc!r}); its controls are SKIPPED, not passed")
else:
    # 🔴 Said out loud, because the alternative is a count that shrinks silently.
    # The mutation run that proved this suite's failure capability executed from a
    # scratch copy where `p1054` was not on the expected relative path, and the
    # control count simply dropped 57 -> 49 with nothing printed.  A skip that does
    # not announce itself is indistinguishable from coverage, which is the exact
    # defect class this base keeps re-finding.
    print(
        f"NOTE p1054 not found at {P1054!r}; "
        "8 cross-instrument controls are SKIPPED, not passed"
    )

if _p1054_ok:
    # p1054 collapses all three distinct payloads onto one verdict with no evidence.
    for nm, body in (("usc", USC), ("apache", APACHE), ("gpl", GPL)):
        old = mit_plus.classify(body)
        check(f"p1054 collapses {nm} to NOT-MIT-BODY", old["verdict"], "NOT-MIT-BODY")
        check(f"p1054 reports no evidence for {nm}", list(old["hits"]), [])
    # 🟢 And this instrument separates them: three payloads, three verdicts.
    verdicts = {rs.scan(b)["verdict"] for b in (USC, APACHE, GPL)}
    check("p257 separates the three payloads", len(verdicts), 3)
    # The vocabulary must never drift BELOW p1054's.
    truthy(
        "vocabulary is a superset of p1054's",
        set(mit_plus.RESTRICTION_TERMS).issubset(set(rs.RESTRICTION_TERMS)),
    )

# ── 7. An MIT body with a non-commercial rider (the PageLM shape, p255) ─────────
# Not published as permissive, and it reaches a verdict that names a human.
pagelm_shape = MIT.replace(
    "to deal",
    "for personal, educational, or non-commercial research purposes, to deal",
)
pl = rs.scan(pagelm_shape)
check("pagelm_shape.family", pl["family"], "MIT")
check("pagelm_shape.verdict", pl["verdict"], rs.VERDICT_FAMILY_PLUS)
check("pagelm_shape.usable", rs.is_usable_permissive(pagelm_shape), False)
truthy("pagelm_shape hits non-commercial", "non-commercial" in pl["hits"])

# ── 8. THE TITLE-ANCHOR REGRESSION, pinned ──────────────────────────────────────
# 🔴 This instrument's FIRST draft matched family anchors body-wide and graded the
# real GPL-3.0 fixture as AGPL, because GPL-3.0 §13 is titled "Use with the GNU
# Affero General Public License".  The next controls fail against that draft.
truthy(
    "the GPL fixture really does quote the Affero GPL (the trap is real)",
    "gnu affero general public license" in GPL.lower(),
)
check("GPL fixture is not graded AGPL", rs.family_of(GPL), "GPL")
# And the converse: a real AGPL payload still grades AGPL, by its own title line.
agpl = (
    "                    GNU AFFERO GENERAL PUBLIC LICENSE\n"
    "                       Version 3, 19 November 2007\n\n"
    "...incorporated under version 3 of the GNU General Public License...\n"
)
check("agpl grades by its title line", rs.family_of(agpl), "AGPL")
# A licence NAME appearing only deep in the body does not name the family.
deep = "Copyright (c) 2026 Someone\n\n" + ("filler\n" * 40) + "Apache License\n"
check("a deep mention is not a title", rs.family_of(deep), None)
# A BSD grant opening on a bare copyright line is still reached, via stage two.
bsd = (
    "Copyright (c) 2026 Example Institution\nAll rights reserved.\n\n"
    "Redistribution and use in source and binary forms, with or without\n"
    "modification, are permitted provided that the following conditions are met:\n"
)
check("bsd reached by operative clause", rs.family_of(bsd), "BSD")
# 🔴 ...and that payload carries `all rights reserved`, which is in the vocabulary.
# A real BSD grant says that phrase benignly, so the verdict must name a human
# rather than either publishing it as permissive or burying the hit.
bsd_scan = rs.scan(bsd)
truthy("bsd hit is reported", "all rights reserved" in bsd_scan["hits"])
check("bsd verdict names a human", bsd_scan["verdict"], rs.VERDICT_FAMILY_PLUS)
check("bsd is not auto-published as permissive", rs.is_usable_permissive(bsd), False)

# ── 8b. `p287` / `T-p286b` — THE VOCABULARY IS NO LONGER ENGLISH-ONLY ───────────
# Both payloads below are REAL, read first-hand from `raw.githubusercontent.com` on
# `ls-remote`-resolved refs at `p287`, and both graded
# `UNCLASSIFIED:no-family-no-restriction` WITH ZERO HITS before this change.  These
# are the controls that fail against `p257`..`p286`.
RAPKUMER = load("rapkumer-id-3140.txt")
GAOKAO = load("opengaokao-zh-15992.txt")

rk = rs.scan(RAPKUMER)
check("rapkumer.bytes", rk["bytes"], 3140)
check("rapkumer.language", rk["language"], "id")
check("rapkumer.verdict", rk["verdict"], rs.VERDICT_RESTRICTED)
check("rapkumer.usable", rs.is_usable_permissive(RAPKUMER), False)
truthy("rapkumer hits its section-3 title",
       "larangan penggunaan komersial" in rk["hits"])
truthy("rapkumer hits non-empty (p257..p286 reported ())", len(rk["hits"]) > 0)
# 🔴 The trap this payload sets, and the reason the MIT body anchor had to be
# measured before it was added: `rapkumer` §6 sub-licences Feather Icons under MIT.
# A permissive-looking carve-out inside a total commercial prohibition must NOT make
# the payload MIT, or `p287`'s OTHER fix would publish it as usable.
check("rapkumer is not graded MIT by its own MIT carve-out", rk["family"], None)

gk = rs.scan(GAOKAO)
check("gaokao.bytes", gk["bytes"], 15992)
check("gaokao.language", gk["language"], "zh")
check("gaokao.verdict", gk["verdict"], rs.VERDICT_RESTRICTED)
check("gaokao.usable", rs.is_usable_permissive(GAOKAO), False)
truthy("gaokao hits its first clause", "禁止商业使用" in gk["hits"])

# 🔵 THE PORT IS MEASURED IN BOTH DIRECTIONS, not trusted to agree (`p637`).
# Every non-English phrase `lib/license_family.sh::commercial_use_ok` matches must be
# reachable from this instrument's vocabulary too, or the two predicates disagree on
# a payload and the shelf gate and the Python gate publish different verdicts.
SHELL_LIB = os.path.join(os.path.dirname(FIX), "..", "lib", "license_family.sh")
if os.path.isfile(SHELL_LIB):
    with open(SHELL_LIB, encoding="utf-8", errors="replace") as fh:
        shell_src = fh.read()
    _ours = set(rs.RESTRICTION_TERMS)
    _missing = [
        ph for ph in (
            "uso no comercial", "fines no comerciales", "prohibido el uso comercial",
            "uso não comercial", "fins não comerciais", "proibido o uso comercial",
            "usage non commercial", "fins non commerciales",
            "nicht-kommerziell", "keine kommerzielle nutzung",
            "uso non commerciale",
            "禁止商业使用", "禁止商用", "非商业使用", "不得用于商业",
            "商用利用禁止", "非営利", "비상업적",
        )
        if ph not in _ours
    ]
    check("every shell restriction phrase is in this vocabulary too", _missing, [])
    # ...and the phrases really are in the shell lib, so the list above is a PORT
    # and not a wish list this suite invented.
    for ph in ("禁止商业使用", "uso no comercial", "nicht-kommerziell"):
        truthy(f"shell lib really carries {ph!r}", ph in shell_src)
    # 🟢 `p287` adds the `id` arm to BOTH, so the shell lib must carry it as well.
    truthy("shell lib gained the Indonesian arm at p287",
           "larangan penggunaan komersial" in shell_src)
else:
    print(f"NOTE shell lib not found at {SHELL_LIB!r}; 5 port controls are SKIPPED, not passed")

# ── 8c. A NEGATIVE CONTROL PER LANGUAGE ARM ─────────────────────────────────────
# 🔴 Required, and not optional: every arm matches a PHRASE precisely because the
# bare word is permissive-neutral.  Each body below PERMITS commercial use, in the
# arm's own language, using the arm's own vocabulary word.  An arm that fires here
# is an arm that would condemn every permissive licence written in that language.
PERMITS = {
    "id": "Penggunaan komersial diizinkan tanpa batasan apa pun.",
    "es": "Se permite el uso comercial de este software sin restricciones.",
    "pt": "É permitido o uso comercial deste software sem restrições.",
    "fr": "L'usage commercial de ce logiciel est autorisé sans restriction.",
    "de": "Die kommerzielle Nutzung dieser Software ist ausdrücklich erlaubt.",
    "it": "L'uso commerciale di questo software è consentito senza restrizioni.",
    "zh": "允许商业使用本软件，无需额外授权。",
    "ja": "商用利用は許可されています。",
    "ko": "상업적 이용이 허용됩니다.",
    "vi": "Cho phép sử dụng cho mục đích thương mại.",
}
for lang, body in PERMITS.items():
    arm = rs.RESTRICTION_TERMS_BY_LANGUAGE[lang]
    fired = [t for t in arm if t in body.lower()]
    check(f"negative control: the {lang!r} arm does not fire on a PERMITTING body",
          fired, [])
# ...and the positive half, so the arms are not merely silent.
POSITIVE = {
    "id": "Pasal 3: LARANGAN PENGGUNAAN KOMERSIAL dalam bentuk apa pun.",
    "es": "Se autoriza únicamente el uso no comercial de esta obra.",
    "pt": "Autoriza-se apenas o uso não comercial desta obra.",
    "fr": "Seul l'usage non commercial de ce logiciel est autorisé.",
    "de": "Nur die nicht kommerzielle Nutzung ist gestattet.",
    "it": "È consentito soltanto l'uso non commerciale di questa opera.",
    "zh": "禁止商业使用本软件。",
    "ja": "商用利用禁止とします。",
    "ko": "비상업적 용도로만 사용할 수 있습니다.",
    "vi": "Chỉ cho phép sử dụng phi thương mại.",
}
for lang, body in POSITIVE.items():
    arm = rs.RESTRICTION_TERMS_BY_LANGUAGE[lang]
    fired = [t for t in arm if t in body.lower()]
    truthy(f"positive control: the {lang!r} arm fires on a RESTRICTING body",
           len(fired) > 0)
    # And the whole scan reaches a restricted verdict, not merely the arm.
    truthy(f"{lang!r} restricting body is never usable",
           rs.is_usable_permissive(body) is False)
# The English arm's negative control is a REAL payload, and it is already loaded:
# verbatim Apache-2.0 carries none of the English vocabulary.
check("negative control: the English arm does not fire on verbatim Apache-2.0",
      rs.scan(APACHE)["hits"], ())

# ── 8d. `UNREADABLE-BODY` — "nothing found" vs "nothing looked for" ─────────────
# 🔴 SYNTHETIC, and said so out loud: this base holds no payload in an UNCOVERED
# language yet, so the reachability control for the new verdict is written text and
# not a fixture.  Registered as a backlog item rather than dressed up — every other
# fixture in this directory is real, and the difference must stay visible.
# 🔵 Thai is the right language to write it in rather than an arbitrary one: O-NET is
# a national exam with a real education-software market, Thai has NO arm in this
# vocabulary, and a Thai licence prohibiting commercial use would — before this
# verdict existed — have been published as carrying no restriction at all.
THAI_BODY = (
    "สัญญาอนุญาตการใช้งานซอฟต์แวร์นี้ ผู้ใช้ต้องยอมรับเงื่อนไขทั้งหมดก่อนการใช้งาน "
    "ห้ามนำซอฟต์แวร์นี้ไปใช้ในเชิงพาณิชย์โดยไม่ได้รับอนุญาตเป็นลายลักษณ์อักษร "
    "การทำซ้ำ ดัดแปลง หรือเผยแพร่ต่อสาธารณะต้องได้รับความยินยอมจากผู้ถือลิขสิทธิ์ "
    "ผู้ถือลิขสิทธิ์ขอสงวนสิทธิ์ทั้งหมดที่ไม่ได้ระบุไว้อย่างชัดเจนในเอกสารนี้ "
    "เอกสารนี้จัดทำขึ้นเพื่อการศึกษาและการวิจัยภายในสถาบันเท่านั้น"
)
th = rs.scan(THAI_BODY)
truthy("the Thai control clears the byte floor",
       th["bytes"] >= rs.UNREADABLE_MIN_BYTES)
check("thai.family", th["family"], None)
check("thai.language", th["language"], None)
check("thai.vocabulary_covers_language", th["vocabulary_covers_language"], False)
# 🟢 The verdict that is the point of the whole change.
check("thai.verdict is UNREADABLE-BODY, not UNCLASSIFIED",
      th["verdict"], rs.VERDICT_UNREADABLE)
check("thai.usable", rs.is_usable_permissive(THAI_BODY), False)
# A covered language with nothing to find is still a MEASUREMENT, not an admission.
check("verbatim Apache-2.0 is not called unreadable",
      rs.scan(APACHE)["verdict"], rs.VERDICT_PERMISSIVE)
check("the English vocabulary covers the Apache body",
      rs.scan(APACHE)["vocabulary_covers_language"], True)
# 🔵 And BELOW the floor the verdict is deliberately NOT claimed: a 14-byte `404`
# body has too little text for the marker test to mean anything, and shouting
# "cannot read" at it would bury the case the verdict exists for.
check("the 404 body stays UNCLASSIFIED, below the floor",
      rs.scan(NOTFOUND)["verdict"], rs.VERDICT_UNCLASSIFIED)
truthy("the 404 body is indeed below the floor",
       rs.scan(NOTFOUND)["bytes"] < rs.UNREADABLE_MIN_BYTES)
truthy("UNREADABLE-BODY is not in the usable arm",
       rs.VERDICT_UNREADABLE not in rs.USABLE_VERDICTS)

# ── 8e. `p287` — AN MIT BODY WITH NO TITLE LINE ─────────────────────────────────
# REAL payload: `Priyamakeshwari/TeachGPT` `LICENSE.md`, 1 057 B on `main`, read
# first-hand at `p287`.  A verbatim MIT body that simply omits its own title, so the
# title stage sees nothing and stage two had anchors for BSD and ISC but not MIT.
# 🟡 The direction was conservative — never published as permissive — so it cost no
# wrong claim; it cost a real usable grant read as unclassifiable.
MIT_UNTITLED = load("mit-untitled-1057.txt")
mu = rs.scan(MIT_UNTITLED)
check("mit_untitled.bytes", mu["bytes"], 1057)
truthy("the payload really has no title line",
       "mit license" not in "\n".join(MIT_UNTITLED.lower().splitlines()[:4]))
truthy("...and really does recite MIT's operative clause",
       "permission is hereby granted, free of charge" in MIT_UNTITLED.lower())
check("mit_untitled grades MIT via the operative clause", mu["family"], "MIT")
check("mit_untitled.verdict", mu["verdict"], rs.VERDICT_PERMISSIVE)
check("mit_untitled.usable", rs.is_usable_permissive(MIT_UNTITLED), True)
# 🔴 The anchor must not reach past its own clause.  Measured on every fixture
# before it was added; pinned here so a later pass cannot widen it by accident.
for nm, body in (("apache", APACHE), ("gpl", GPL), ("usc", USC),
                 ("rapkumer", RAPKUMER), ("gaokao", GAOKAO)):
    truthy(f"{nm} does not recite MIT's operative clause",
           "permission is hereby granted, free of charge" not in body.lower())
truthy("so the MIT anchor cannot turn any of them MIT",
       {rs.family_of(b) for b in (APACHE, GPL, USC, RAPKUMER, GAOKAO)}
       == {"Apache-2.0", "GPL", None})

# ── 9. Every verdict in ALL_VERDICTS is reachable, and the usable arm is closed ──
reached = {
    rs.scan(USC)["verdict"],
    rs.scan(APACHE)["verdict"],
    rs.scan(GPL)["verdict"],
    rs.scan(NOTFOUND)["verdict"],
    rs.scan(pagelm_shape)["verdict"],
    rs.scan(THAI_BODY)["verdict"],
}
check("all verdicts reachable", sorted(reached), sorted(rs.ALL_VERDICTS))
truthy("usable arm is closed", rs.USABLE_VERDICTS == frozenset({rs.VERDICT_PERMISSIVE}))
for v in rs.ALL_VERDICTS:
    if v != rs.VERDICT_PERMISSIVE:
        truthy(f"{v} is not usable", v not in rs.USABLE_VERDICTS)

# ── 10. Bytes are counted as UTF-8, not as characters (the ©️ in the USC header) ─
truthy("usc header is non-ascii", any(ord(c) > 127 for c in USC))
check("usc utf8 byte count", usc["bytes"], len(USC.encode("utf-8")))
truthy("usc bytes exceed char count", usc["bytes"] > len(USC))

print(f"{PASS}/{PASS + FAIL} controls pass")
sys.exit(1 if FAIL else 0)
