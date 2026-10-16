#!/usr/bin/env python3
"""Controls for p240-grant-language.

The specimen is real and was read first-hand this pass: heronerar/OpenGaokao, LICENSE,
15 992 B on `main` at a75b65aaa494.  Its first clause is 禁止商业使用 and the shared
classifier answered ALLOWED on it before p240.

COVERAGE NOTE, which is the point of the suite: a language gate validated only on the
language that broke it scores 100% while useless.  So the negatives carry the weight --
a Latin-script payload must NEVER be flagged, a non-Latin payload that GRANTS commercial
use must still be reported as non-English (it is unread by the English match either way),
and a holder name in a foreign script must not drag an English grant over the threshold.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grant_language import (  # noqa: E402
    NON_LATIN_PCT, RESTRICTION_TOKENS, may_publish, restrictions_found,
    script_of, script_profile, verdict,
)

n = 0
fail = 0


def check(name, expected, actual):
    global n, fail
    n += 1
    if expected == actual:
        print("ok   %-58s %s" % (name, actual))
    else:
        print("FAIL %-58s expected=%r got=%r" % (name, expected, actual))
        fail += 1


MIT = """MIT License

Copyright (c) 2026 Someone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software."""

# The real specimen, trimmed to its operative clauses.  Not a synthetic fixture: these
# lines are a verbatim excerpt of the payload p240 read from raw.githubusercontent.com.
OPENGAOKAO = """# OpenGaokao Source-Available License 1.0

版本：1.0
简称：`OpenGaokao-SAL-1.0`

本许可证是“源码可见、商业受限”许可证，不是 OSI 认可的开源许可证。

1. 禁止商业使用；商业使用必须事先取得许可人单独签署的书面付费授权；
2. 禁止利用本软件或其受著作权保护的表达开发、运行或改进竞争性产品或服务；
3. 禁止在 GitHub 平台以外再分发原始软件；"""

# Non-Latin and PERMISSIVE.  Still reported non-English: the English token match did not
# read it either, and that is the fact the verdict records.
ZH_PERMISSIVE = """MIT 许可证

版权所有 (c) 2026

特此免费授予任何人获得本软件及相关文档文件副本的权利，可以不受限制地处置本软件，
包括但不限于使用、复制、修改、合并、出版发行、散布、再授权和销售本软件的副本。"""

# An ENGLISH grant whose copyright holder is written in Chinese.  Four CJK characters in
# 700 letters must not cross a 20% threshold -- this is the false-positive mode that a
# naive "contains non-ASCII" test would have.
EN_WITH_CJK_HOLDER = MIT.replace("Someone", "清华大学 (Tsinghua University)")

ES_NC = """Licencia de materiales

Estos materiales se ceden para uso no comercial en centros educativos."""

# --- script_of / script_profile -------------------------------------------------------
check("script_of: latin a", "LATIN", script_of("a"))
check("script_of: CJK", "CJK", script_of("商"))
check("script_of: hiragana", "HIRAGANA", script_of("の"))
check("script_of: hangul", "HANGUL", script_of("한"))
check("script_of: cyrillic", "CYRILLIC", script_of("д"))
check("script_of: digit is not a script", "OTHER", script_of("4"))
check("script_of: punctuation", "OTHER", script_of("-"))

letters, non_latin, pct, dom = script_profile(OPENGAOKAO)
check("profile: specimen is CJK-dominant", "CJK", dom)
check("profile: specimen is over threshold", True, pct >= NON_LATIN_PCT)
check("profile: MIT has no non-latin letters", 0, script_profile(MIT)[1])
check("profile: MIT pct is zero", 0.0, script_profile(MIT)[2])
check("profile: empty text does not divide by zero", 0.0, script_profile("")[2])
check("profile: counts LETTERS, not bytes",
      True, script_profile("商业 1234567890 -----")[2] == 100.0)

# --- restriction tokens ---------------------------------------------------------------
check("tokens: specimen fires zh", True,
      any(h.startswith("zh:") for h in restrictions_found(OPENGAOKAO)))
check("tokens: MIT fires nothing", [], restrictions_found(MIT))
check("tokens: es phrase fires", True,
      "es:uso no comercial" in restrictions_found(ES_NC))
check("tokens: the bare word comercial does NOT fire",
      [], restrictions_found("Se permite el uso comercial sin restriccion."))
check("tokens: the bare word commercial does NOT fire",
      [], restrictions_found("Commercial use is expressly permitted."))
check("tokens: zh permissive notice fires nothing", [], restrictions_found(ZH_PERMISSIVE))

# --- verdicts -------------------------------------------------------------------------
check("verdict: the specimen is RESTRICTED",
      "NON-ENGLISH-GRANT-RESTRICTED", verdict(OPENGAOKAO)[0])
check("verdict: MIT is latin-script", "LATIN-SCRIPT", verdict(MIT)[0])
check("verdict: es NC text is latin-script (the token match reads it)",
      "LATIN-SCRIPT", verdict(ES_NC)[0])
check("verdict: non-latin + no token is UNREAD, not CLEAR",
      "NON-ENGLISH-GRANT-UNREAD", verdict(ZH_PERMISSIVE)[0])
check("verdict: CJK holder name in an English grant stays latin-script",
      "LATIN-SCRIPT", verdict(EN_WITH_CJK_HOLDER)[0])
check("verdict: empty payload is latin-script, not a false alarm",
      "LATIN-SCRIPT", verdict("")[0])

# --- may_publish: the asymmetry the gate exists to enforce ----------------------------
check("may_publish: MIT yes", True, may_publish(MIT))
check("may_publish: the specimen no", False, may_publish(OPENGAOKAO))
check("may_publish: UNREAD is not publishable either", False, may_publish(ZH_PERMISSIVE))

# --- the vocabulary stays in step with lib/license_family.sh --------------------------
# P255: two lists that drift are three instruments with three answers.  Every token this
# module carries for a language the shell classifier also covers must be present there.
_LIB = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "lib", "license_family.sh")
if os.path.exists(_LIB):
    with open(_LIB, encoding="utf-8") as fh:
        lib_src = fh.read()
    missing = [t for lang in ("zh", "ja", "ko", "es", "pt", "fr", "de", "it")
               for t in RESTRICTION_TOKENS[lang] if t not in lib_src]
    check("vocabulary: every non-English token is also in lib/license_family.sh",
          [], missing)
else:
    check("vocabulary: lib present", True, False)

print("\n%d/%d" % (n - fail, n))
sys.exit(1 if fail else 0)
