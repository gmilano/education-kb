"""Controls for family_lang.py. Real controls read the payloads measured in p474;
synthetic controls are LABELLED synthetic -- no payload for them was found this pass.
"""
import os, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from family_lang import grade

P = sys.argv[1] if len(sys.argv) > 1 else "payloads"

# (payload file, expected family, version, or_later, scope)
REAL = [
 ("portabilis__pre-matricula-digital__LICENSE", "AGPL", "3", True,  "WHOLE_WORK"),
 ("ipti__br.tag__LICENSE",                       "GPL",  "2", True,  "WHOLE_WORK"),
 ("prefeiturasp__SME-PratoAberto-Edu__LICENSE",  "GPL",  "3", True,  "WHOLE_WORK"),
 ("datauy__ElijoEstudiar__LICENSE",              "GPL",  "3", True,  "WHOLE_WORK"),
 ("sakaiproject__sakai__LICENSE",                "ECL",  "2.0", False, "WHOLE_WORK"),
 ("Apereo-Learning-Analytics-Initiative__OpenLRW__LICENSE","ECL","2.0",False,"WHOLE_WORK"),
 ("chenhz01__scireason-forge__LICENSE",          "APACHE","2.0",False,"WHOLE_WORK"),
 ("Benjamin-KY__open-harness-atlas__LICENSE",    "APACHE","2.0",False,"WHOLE_WORK"),
 ("gpassero__uol-redacoes-xml__LICENSE",         "APACHE","2.0",False,"WHOLE_WORK"),
 ("PolyOS-Team__Atolye.Platform__LICENSE",       "MIT",  None, False, "WHOLE_WORK"),
 ("bncc-dev__bncc-dados__LICENSE",               "MIT",  None, False, "WHOLE_WORK"),
 ("Handshake-AI-Research__studentbench__LICENSE","MIT",  None, False, "WHOLE_WORK"),
 ("kaushikatla-cell__EduSafeBench__LICENSE",     "MIT",  None, False, "WHOLE_WORK"),
 ("RandMelville__slm-writing-feedback-tutor-ptbr__LICENSE","MIT",None,False,"WHOLE_WORK"),
 ("Simon-zj1__eyedot__LICENSE",                  "MIT",  None, False, "WHOLE_WORK"),
 ("agn3si__ResultadosUNAM---data__LICENSE",      "MIT",  None, False, "WHOLE_WORK"),
 ("cortega26__chile-hub__LICENSE",               "MIT",  None, False, "WHOLE_WORK"),
 ("pguso__agents-from-scratch__LICENSE",         "MIT",  None, False, "WHOLE_WORK"),
 ("huseyingulsin__Acik-Kaynak-Bilgisayar-Bilimleri__LICENSE.md","MIT",None,False,"WHOLE_WORK"),
 ("Turkish-AI-Community__hsd-agu-egitim__LICENSE","MIT", None, False, "WHOLE_WORK"),
 # the three split-scope payloads: NO family in the title block, and that is correct
 ("bncc-dev__bncc-benchmark__LICENSE",           None,  None, False, "SPLIT_SCOPE"),
 ("bncc-dev__bncc-pacotes__LICENSE",             None,  None, False, "SPLIT_SCOPE"),
 ("richer-richard__arquimedes__LICENSE",         None,  None, False, "SPLIT_SCOPE"),
]

SYNTHETIC = [
 ("es-AGPL3-or-later", "LICENCIA PUBLICA GENERAL AFFERO DE GNU\nVersion 3, 19 de noviembre de 2007\n"
   "...bajo los terminos de la Licencia, o (a su eleccion) cualquier version posterior.",
   "AGPL", "3", True, "WHOLE_WORK"),
 ("es-GPL2-only", "LICENCIA PUBLICA GENERAL DE GNU\nVersion 2, junio de 1991\n(sin eleccion)",
   "GPL", "2", False, "WHOLE_WORK"),
 ("pt-LGPL21", "LICENCA PUBLICA GERAL MENOR DO GNU\nVersao 2.1, fevereiro de 1999",
   "LGPL", "2.1", False, "WHOLE_WORK"),
 ("en-negative-prose-only", "This project is free software. See the website for terms.",
   None, None, False, "WHOLE_WORK"),
]

passed = failed = 0
print(f"{'control':62} {'family':7} {'ver':5} {'orl':5} {'scope':12} result")
print("-" * 104)
for fn, ef, ev, eo, es in REAL:
    path = os.path.join(P, fn)
    if not os.path.exists(path):
        print(f"{fn[:62]:62} {'-':7} {'-':5} {'-':5} {'-':12} MISSING-PAYLOAD"); failed += 1; continue
    body = open(path, encoding="utf-8", errors="replace").read()
    g = grade(body)
    ok = (g["family"] == ef and g["version"] == ev and g["or_later"] == eo and g["scope"] == es)
    passed += ok; failed += (not ok)
    print(f"{fn[:62]:62} {str(g['family']):7} {str(g['version']):5} {str(g['or_later']):5} "
          f"{g['scope']:12} {'PASS' if ok else 'FAIL exp=' + str((ef,ev,eo,es))}")
print("-" * 104)
for name, body, ef, ev, eo, es in SYNTHETIC:
    g = grade(body)
    ok = (g["family"] == ef and g["version"] == ev and g["or_later"] == eo and g["scope"] == es)
    passed += ok; failed += (not ok)
    print(f"{('[synthetic] ' + name)[:62]:62} {str(g['family']):7} {str(g['version']):5} "
          f"{str(g['or_later']):5} {g['scope']:12} {'PASS' if ok else 'FAIL exp=' + str((ef,ev,eo,es))}")
print("-" * 104)
print(f"{passed}/{passed + failed} controls pass   ({len(REAL)} real payloads, {len(SYNTHETIC)} synthetic)")
sys.exit(1 if failed else 0)
