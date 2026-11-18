#!/usr/bin/env python3
"""Controls for origin_strip.py (p899). Run: python3 -I test_origin_strip.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from origin_strip import strip, score, verdict, analyse, THRESHOLD, spread, positions

FX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")
P, F = 0, []
def ck(name, cond, detail=""):
    global P
    if cond: P += 1
    else: F.append(f"{name}: {detail}")

# ---- 1. THE NAMED KNOWN-GOOD NEGATIVE FIXTURE (898-G1's whole point) ----------------
aula = open(os.path.join(FX, "aula-README.NEGATIVE-FIXTURE.md"), encoding="utf-8").read()
a = analyse(aula)

# p898 recorded aula at ES=64/PT=83 raw -> PT*=0/ES*=1 stripped, and concluded that STRIPPING
# was the fix. Decomposed here as a 2x2, that conclusion is wrong. A p898-style NON-exclusive
# marker list (shared Romance function words: de/la/el/no/con/um/os...) scores:
#
#                              PT    ES
#   legacy markers / raw       464   653
#   legacy markers / stripped  287   362     <- stripping alone: -38%, STILL places aula as LATAM
#   exclusive markers / raw      0     2     <- exclusivity alone: -99.7%
#   exclusive markers / stripped 0     2
#
# So stripping is the WEAKER lever and 898-G1's acceptance test could have been passed in full
# by an instrument that still published the false LATAM row. Both fixes ship; this control
# pins the decomposition so the finding cannot be silently lost.
LEGACY_PT = ["ã","õ","ç","ção","você","não","de","da","do","em","com","os","as","um","uma","para","por","no","na"]
LEGACY_ES = ["ñ","¿","¡","ción","qué","más","de","la","el","los","las","un","una","para","por","con","no","en"]
def _legacy(t):
    low = t.lower()
    return sum(low.count(m) for m in LEGACY_PT), sum(low.count(m) for m in LEGACY_ES)
_lr_pt, _lr_es = _legacy(aula)
_ls_pt, _ls_es = _legacy(strip(aula))
ck("aula-legacy-raw-would-place", _lr_es >= 100 and _lr_pt >= 100,
   f"legacy/raw PT={_lr_pt} ES={_lr_es} — fixture must still demonstrate the trap")
ck("aula-stripping-ALONE-insufficient", _ls_es >= THRESHOLD,
   f"legacy/stripped ES={_ls_es} — if this ever drops below threshold the decomposition changed")
ck("aula-exclusivity-is-the-lever", a["raw"]["ES"] < THRESHOLD and a["raw"]["PT"] < THRESHOLD,
   f"exclusive/raw PT={a['raw']['PT']} ES={a['raw']['ES']}")
ck("aula-stripped-PT-noise", a["stripped"]["PT"] < THRESHOLD, f"PT*={a['stripped']['PT']}")
ck("aula-stripped-ES-noise", a["stripped"]["ES"] < THRESHOLD, f"ES*={a['stripped']['ES']}")
ck("aula-verdict-not-latam", "PT" not in a["verdict"] and "ES" not in a["verdict"],
   f"verdict={a['verdict']} — publishing this as LATAM is the exact defect 898-G1 names")

# ---- 2. POSITIVE FIXTURES: a real PT repo and a real CJK repo must SURVIVE stripping --
pt = analyse(open(os.path.join(FX, "menthor-README.PT-POSITIVE-FIXTURE.md"), encoding="utf-8").read())
ck("menthor-PT-survives", pt["stripped"]["PT"] >= THRESHOLD, f"PT*={pt['stripped']['PT']}")
ck("menthor-verdict-PT", pt["verdict"].startswith("PT"), f"verdict={pt['verdict']}")
cj = analyse(open(os.path.join(FX, "studymate-README.CJK-POSITIVE-FIXTURE.md"), encoding="utf-8").read())
ck("studymate-CJK-survives", cj["stripped"]["CJK"] >= THRESHOLD, f"CJK*={cj['stripped']['CJK']}")
ck("studymate-verdict-CJK", cj["verdict"].startswith("CJK"), f"verdict={cj['verdict']}")

# ---- 3. THE STRIPPER ITSELF ---------------------------------------------------------
ck("strip-fence",  "ção" not in strip("hi\n```\nfunção educação\n```\nbye"))
ck("strip-inline", "ñ" not in strip("see `señor` here"))
ck("strip-url",    score(strip("visit https://educação.com.br/ação now"))["PT"] == 0,
   str(score(strip("visit https://educação.com.br/ação now"))))
ck("strip-dotcom", score(strip("mail me at foo.com"))["PT"] == 0)
ck("strip-mdlink", "ção" not in strip("[educação](http://x.com)"))
ck("strip-img",    "ñ" not in strip("![añejo](http://x.com/a.png)"))
ck("strip-html",   "ç" not in strip("<img alt='açaí'>"))
ck("keeps-prose",  score(strip("A educação não é só conteúdo, você precisa de ensino."))["PT"] >= 5,
   str(score(strip("A educação não é só conteúdo, você precisa de ensino."))))

# ---- 4. NO SHARED-ROMANCE MARKERS (what produced p898's 147 false hits) --------------
from origin_strip import PT_EXCL, ES_EXCL
for shared in ("la", "de", "no", "con", "el", "um", "os", "as", "com"):
    ck(f"no-shared-{shared}", shared not in PT_EXCL and shared not in ES_EXCL,
       f"'{shared}' is not exclusive to PT/ES and will fire on English prose")

# ---- 5. ENGLISH MUST NOT PLACE (asymmetry guard) ------------------------------------
eng = "An open source learning platform for students and teachers. Build lesson plans fast."
ck("english-unknown", verdict(score(strip(eng))) == "ENGLISH-OR-UNKNOWN",
   verdict(score(strip(eng))))
ck("empty-unknown", verdict(score(strip(""))) == "ENGLISH-OR-UNKNOWN")

# ---- 6. KANA DISCRIMINATES JAPANESE FROM CHINESE ------------------------------------
ck("kana-beats-cjk", verdict({"PT":0,"ES":0,"CJK":40,"KANA":12,"HANGUL":0,"DEVANAGARI":0,
                              "ARABIC":0,"CYRILLIC":0,"THAI":0}).startswith("KANA"))
ck("cjk-alone-is-cjk", verdict({"PT":0,"ES":0,"CJK":40,"KANA":0,"HANGUL":0,"DEVANAGARI":0,
                                "ARABIC":0,"CYRILLIC":0,"THAI":0}).startswith("CJK"))

# ---- 7. THRESHOLD GUARD: one stray accent must never place a repo -------------------
ck("one-accent-noise", verdict(score("the author is José"))== "ENGLISH-OR-UNKNOWN",
   verdict(score("the author is José")))

# ---- 8. LANGUAGE LISTS ARE NOT ORIGIN (p899 finding) -------------------------------
switcher = "# book-to-skill\n\nEnglish · Русский · 简体中文\n\n" + ("Turn any technical book into a skill. " * 200)
v = analyse(switcher)["verdict"]
ck("switcher-not-placed", v.startswith("LANGUAGE-LIST") or v == "ENGLISH-OR-UNKNOWN",
   f"verdict={v} — a language switcher must never place a repo by origin")
langlist = "# rumi\n\nSupported: हिन्दी Hindi · বাংলা Bengali · मराठी Marathi\n\n" + ("WhatsApp teaching assistant for classrooms. " * 200)
v2 = analyse(langlist)["verdict"]
ck("langlist-not-placed", v2.startswith("LANGUAGE-LIST") or v2 == "ENGLISH-OR-UNKNOWN",
   f"verdict={v2} — a supported-languages list is a target market, not an origin")
# dispersed prose in the SAME script must still place
prose = ("शिक्षा और सीखने के लिए एक मुक्त मंच। " * 60)
ck("dispersed-prose-places", analyse(prose)["verdict"].startswith("DEVANAGARI"),
   f"verdict={analyse(prose)['verdict']}")
ck("spread-zero-single-span", spread("aaa\u0939\u0939\u0939" + "b"*500, "DEVANAGARI") < 0.10)

print(f"{P}/{P+len(F)} controls PASS")
for f in F: print("  FAIL", f)
sys.exit(1 if F else 0)
