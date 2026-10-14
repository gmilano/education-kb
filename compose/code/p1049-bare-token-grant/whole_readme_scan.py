#!/usr/bin/env python3
"""P1049 limb 2 — the WHOLE-README identifier scan.

Limb 1 (bare_token_grant.py) only reads what sits under a licence HEADING.
Its own positive control defeated it: `xiaolai/the-craft-of-selfteaching`
states its grant in a Chinese sentence with no heading anywhere
("本书的版权协议为 CC-BY-NC-ND license"), and limb 1 returned NO_HEADING.

Limb 2 drops the heading requirement and scans every line of the README for a
licence identifier, then prints the line so a human reads it.  It is a SCREEN,
not a verdict: p185 measured limb 1's false positives at 3 in 14, all three
from a token that belonged to something else (a dependency inventory, a
submission policy, a badge).  The line is the evidence; the token is only the
cue to read it.

Token list widened against the four forms p185 measured and limb 1 missed:
  * "Apache License, Version 2.0"   (incorporation by reference — adlnet)
  * unversioned "GPL"               (atutor)
  * a creativecommons.org/licenses/ URL (xiaolai, and every CC row)
  * CJK licence vocabulary          (版权协议 / 许可 / 授权)
"""
import re, sys, urllib.request, urllib.error

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"
PATHS = ["README.md", "README.MD", "readme.md", "README.rst", "README.txt",
         "README_EN.md", "README-en.md", "README.zh-CN.md", "README_zh.md"]

IDENT = re.compile(
    r"(AGPL[- ]?3(\.0)?|AGPLv3|Affero General Public License"
    r"|Apache License,? Version 2\.0|Apache[- ]?2(\.0)?|Apache License"
    r"|LGPL[- ]?[23](\.[01])?|GPL[- ]?[23](\.0)?|GPLv[23]|General Public License|\bGPL\b"
    r"|BSD[- ]?[23][- ]Clause|\bBSD\b|MPL[- ]?2\.0|Mozilla Public License"
    r"|creativecommons\.org/licenses|CC[- ]?BY(?:[- ]?(?:NC|ND|SA)){0,3}"
    r"|\bCC0\b|\bUnlicense\b|\bWTFPL\b|\bISC\b|\bEPL[- ]?2\.0\b|\bMIT\b"
    r"|版权协议|许可协议|开源协议|授权条款|ライセンス)", re.I)

# Lines that merely talk ABOUT licensing without granting anything.
NOISE = re.compile(r"shields\.io|badgen\.net|img\.shields|^\s*[-*]\s|licen[cs]e of|"
                   r"are licensed under their own|third[- ]party|dependenc", re.I)


def fetch(slug):
    for path in PATHS:
        try:
            with urllib.request.urlopen(RAW.format(slug=slug, path=path), timeout=30) as r:
                if r.status == 200:
                    return path, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError:
            continue
        except Exception:
            continue
    return None, None


if __name__ == "__main__":
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    print("slug\treadme\thits\tnoise_only\tfirst_line")
    for s in slugs:
        path, txt = fetch(s)
        if txt is None:
            print(f"{s}\t-\t0\t-\tNO_README")
            continue
        hits, noisy = [], 0
        for line in txt.split("\n"):
            if IDENT.search(line):
                if NOISE.search(line):
                    noisy += 1
                else:
                    hits.append(re.sub(r"\s+", " ", line).strip())
        first = hits[0][:200] if hits else ("(only noise lines)" if noisy else "-")
        print(f"{s}\t{path}\t{len(hits)}\t{noisy}\t{first}", flush=True)
