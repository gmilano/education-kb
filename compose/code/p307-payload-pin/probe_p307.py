#!/usr/bin/env python3
"""p307 — payload-pin the backlog, and retire the filename ladder.

`ACTION p306-R` ranked three instrument items (1 pin the backlog by bytes,
2 make the verdict three-valued, 3 add lower-case `license.txt` to the
ladder).  Items 1 and 2 are implemented here as ordered.  🔴 **Item 3 is
implemented by DELETING the thing it asked to extend.**

Why: built exactly to item 3's spec — `LICENSE`, `LICENSE.txt`, `license.txt`
and eleven more — this prober's first version returned `NO-PAYLOAD` for
[`openedx/XBlock`](https://github.com/openedx/XBlock), whose README names
Apache-2.0 and links a file that 404s.  Two independent channels (`raw`
and `github.com/blob`) agreed on the absence.  **Both were wrong.**  The
payload is at `LICENSE.TXT` — upper-case extension, a case the ladder did
not hold and the README's own link does not use.

A ladder cannot be completed, because the case axis has no bound.  So the
enumeration channel replaces it:

    git clone --depth 1 --filter=blob:none   ->  git ls-tree HEAD

which READS the root filenames instead of guessing them, then pulls the one
blob it needs.  🟢 `p305`'s `ls-remote` lesson one level further: do not
guess the branch, and do not guess the filename either.

(The clone channel itself was carried as REFUSED by this base for two
passes.  It is not.  Re-tested at `p307`, `rc=0`, ~2.4 s, ~1.5 MB blobless.)

Three-valued verdict, per `ACTION p306-R` item 2:
    GRANT    a permission clause is present
    POINTER  no clause, but an http(s) URL to a licence text
    RESERVED no clause and no URL

Clause matching runs over WHITESPACE-NORMALISED text.  The first version
matched raw bytes and misread `tsugiproject/tsugi` as a POINTER because
Apache-2.0's "hereby" and "grants to You a perpetual" fell on opposite sides
of a line break.  A rule defeated by line-wrapping is the same class of
defect as `p304`'s length rule and `p305`'s clause rule — caught here before
publication, which is the control `ACTION p305-R` item 1 asked for.

Two hashes are emitted.  `sha12` is byte-identity.  `nsha12` is computed
over CRLF-normalised, end-stripped text and is LICENCE-identity: the two
11 357 B Apache payloads `p306` recorded as "distinct" differ by one leading
newline and one trailing newline and are the same licence.
"""
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile

LIC_NAME = re.compile(r"^(licen[cs]e|copying|unlicen[cs]e|copyright)", re.I)

GRANT_CLAUSES = [
    ("MIT/ISC", r"Permission is hereby granted, free of charge"),
    ("ISC-form", r"Permission to use, copy, modify, and(?:/or)? distribute"),
    ("Apache/MPL", r"grants? to You a perpetual"),
    ("MPL", r"hereby granted a world-wide, royalty-free, non-exclusive"),
    ("BSD", r"Redistribution and use in source and binary forms"),
    ("GPL-family", r"GNU (?:Affero |Lesser )?General Public License"),
    ("CC", r"Creative Commons Corporation"),
    ("CC0", r"has waived all copyright and related or neighboring rights"),
    ("Unlicense", r"free and unencumbered software released into the public domain"),
    ("EPL", r"Eclipse Public License"),
]

# Two groups, and the split is load-bearing.
#
# TITLE_FAMILY is matched against the HEAD of the payload only, because these
# licences name themselves on line one and their BODIES name each other:
# GPL-2.0 says "use the GNU Lesser General Public License instead of this
# License", so a body-wide match grades every GPL-2.0 as LGPL.
#
# 🔴 And the version in the title is not decoration.  AGPL-3.0's title
# contains GPL-3.0's.  This base carried `brownplt/LTLTutor` (35 148 B) and
# `IgorFonck/logicits` (35 149 B) as AGPL-3.0 for two passes on the strength
# of a byte LENGTH SERIES; both titles read "GNU GENERAL PUBLIC LICENSE
# Version 3".  They are GPL-3.0.  The 33 893 / 34 520 payloads are the AGPL.
#
# BODY_FAMILY is matched against the WHOLE text, because BSD-3-Clause's only
# discriminator ("Neither the name of") sits ~900 bytes in, behind the
# sentence it shares with BSD-2-Clause.
TITLE_FAMILY = [
    ("CC0-1.0", r"CC0 1\.0|Creative Commons Zero"),
    ("CC-BY-SA-4.0", r"Attribution-ShareAlike 4\.0"),
    ("CC-BY-4.0", r"Attribution 4\.0 International"),
    ("AGPL-3.0", r"GNU AFFERO GENERAL PUBLIC LICENSE,? Version 3"),
    ("LGPL-3.0", r"GNU LESSER GENERAL PUBLIC LICENSE,? Version 3"),
    ("LGPL-2.1", r"GNU LESSER GENERAL PUBLIC LICENSE,? Version 2"),
    ("GPL-3.0", r"GNU GENERAL PUBLIC LICENSE,? Version 3"),
    ("GPL-2.0", r"GNU GENERAL PUBLIC LICENSE,? Version 2"),
    ("Apache-2.0", r"Apache License,? Version 2\.0"),
    ("MPL-2.0", r"Mozilla Public License,? Version 2\.0"),
    ("EPL-2.0", r"Eclipse Public License - v 2\.0"),
]
BODY_FAMILY = [
    ("BSD-3-Clause", r"Neither the name of"),
    ("BSD-2-Clause", r"Redistribution and use in source and binary forms"),
    ("ISC", r"Permission to use, copy, modify, and(?:/or)? distribute"),
    ("Unlicense", r"free and unencumbered software"),
    ("MIT", r"Permission is hereby granted, free of charge"),
]

URL_RE = re.compile(r"https?://[^\s)>\"']+")
RESERVED_RE = re.compile(r"all rights reserved", re.I)


def norm_text(body: bytes) -> str:
    return body.decode("utf-8", "replace").replace("\r\n", "\n").strip()


def flat(text: str) -> str:
    """Whitespace-flattened: a clause that line-wraps still matches."""
    return re.sub(r"\s+", " ", text)


def classify_payload(body: bytes):
    """-> (verdict, family, note).  Pure; no network."""
    t = flat(norm_text(body))
    clause = next((n for n, p in GRANT_CLAUSES if re.search(p, t, re.I)), None)
    if clause:
        # The TITLE decides the family, not the body.  GPL-2.0's own text
        # recommends the Lesser licence twice ("use the GNU Lesser General
        # Public License instead"), so a body-wide match grades every GPL-2.0
        # payload as LGPL — which is how `oat-sa/tao-core` and
        # `oat-sa/package-tao` were briefly graded against a shelf that had
        # them right.  Head first, whole text only as a fallback (BSD-3's
        # discriminating clause is ~900 bytes in).
        family = (next((f for f, p in TITLE_FAMILY
                        if re.search(p, t[:300], re.I)), None)
                  or next((f for f, p in BODY_FAMILY
                           if re.search(p, t, re.I)), "UNKNOWN"))
        return "GRANT", family, f"clause={clause}"
    url = URL_RE.search(t)
    if url:
        return "POINTER", "—", f"url={url.group(0)[:70]}"
    if RESERVED_RE.search(t):
        return "RESERVED", "—", "explicit 'all rights reserved'"
    return "RESERVED", "—", "no grant clause, no URL"


def nsha12(body: bytes) -> str:
    return hashlib.sha256(norm_text(body).encode()).hexdigest()[:12]


def run(args, cwd=None, timeout=180):
    return subprocess.run(args, cwd=cwd, capture_output=True, timeout=timeout)


def probe(slug: str):
    blank = dict(slug=slug, branch="—", found="—", file="—", bytes="—",
                 sha12="—", nsha12="—", verdict="—", family="—", note="")
    tmp = tempfile.mkdtemp(prefix="p307-")
    try:
        c = run(["git", "clone", "-q", "--depth", "1", "--filter=blob:none",
                 f"https://github.com/{slug}", tmp + "/r"], timeout=240)
        if c.returncode != 0:
            err = c.stderr.decode("utf-8", "replace").strip().splitlines()
            return {**blank, "verdict": "NO-SLUG",
                    "note": "clone: " + (err[-1][:90] if err else "failed")}
        repo = tmp + "/r"
        br = run(["git", "-C", repo, "rev-parse", "--abbrev-ref", "HEAD"]
                 ).stdout.decode().strip()
        # `--name-only` was the first version's second defect.  The root of
        # `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` holds a DIRECTORY called `Licenses`
        # (six PDFs); `git show HEAD:Licenses` prints a tree listing, the
        # listing contains the words "GNU Lesser General Public License", and
        # the classifier read a directory index as an LGPL grant.  Blobs only.
        entries = run(["git", "-C", repo, "ls-tree", "HEAD"]
                      ).stdout.decode("utf-8", "replace").split("\n")
        names, blobs = [], []
        for e in entries:
            if not e.strip():
                continue
            meta, _, name = e.partition("\t")
            names.append(name)
            if meta.split()[1] == "blob":
                blobs.append(name)
        cands = [n for n in blobs if LIC_NAME.match(n)]
        if not cands:
            return {**blank, "branch": br, "verdict": "NO-PAYLOAD",
                    "note": f"root tree enumerated ({len(names)} entries), "
                            f"no licence-named blob"}
        # Prefer a plain LICENCE/LICENSE/COPYING over COPYRIGHT or -MIT variants.
        cands.sort(key=lambda n: (not re.match(r"^licen[cs]e", n, re.I), len(n)))
        pick = cands[0]
        body = run(["git", "-C", repo, "show", f"HEAD:{pick}"], timeout=120).stdout
        verdict, family, note = classify_payload(body)
        if len(cands) > 1:
            note += f" ⚠ {len(cands)} licence blobs at root; this is the pick"
        return dict(slug=slug, branch=br, found="+".join(cands), file=pick,
                    bytes=len(body),
                    sha12=hashlib.sha256(body).hexdigest()[:12],
                    nsha12=nsha12(body), verdict=verdict, family=family,
                    note=note)
    except subprocess.TimeoutExpired:
        return {**blank, "verdict": "TIMEOUT", "note": "clone or show timed out"}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


COLS = ["slug", "branch", "found", "file", "bytes", "sha12", "nsha12",
        "verdict", "family", "note"]

if __name__ == "__main__":
    print("\t".join(COLS))
    for s in (a.strip() for a in sys.stdin if a.strip()):
        r = probe(s)
        print("\t".join(str(r[c]) for c in COLS), flush=True)
