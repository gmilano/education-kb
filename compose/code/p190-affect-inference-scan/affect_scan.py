"""p190 / P1058 — affect-inference screening for EU AI Act Article 5(1)(f).

Why this exists
---------------
Article 5(1)(f) PROHIBITS AI systems that infer emotions of a natural person in
education institutions. It has applied since 2025-02-02, it was NOT delayed by the
Omnibus, and the ceiling is EUR 35M or 7% of worldwide turnover. ACTION NH had to
answer, for each proctoring row this KB publishes: does it infer emotion?

The first draft of this screen reported SIXTEEN emotion hits in a repository that
has no camera at all. Both causes are encoded as tests below, because either one
alone produces a false accusation against a real repository:

  1. A case-insensitive SUBSTRING match for "emotion" fires inside
     "deviceMotionEvent" -> "devic-eMotionEvent". The DOM event name
     `deviceMotionEventRotationRate` contains `emotioneventrotationrate`.
  2. Vendored trees. `node_modules/mime-db/db.json` carries the MIME type
     `application/emotionml+xml`; `caniuse-lite` carries the DOM event names.
     Any JavaScript repository with a lockfile will "infer emotion".

p189 found a SUBSTRING standing in for a PATH (LICENSE vs LICENSE.TXT).
This is the same class one segment over: a SUBSTRING standing in for a TOKEN.

Two classes, kept apart on purpose
----------------------------------
CLASS A  emotion / affect INFERENCE          -> what 5(1)(f) prohibits
CLASS B  biometric capture, no affect claim  -> face, gaze, head pose.
         NOT prohibited by 5(1)(f). Still Annex III point 3 (monitoring and
         detecting prohibited behaviour during tests) and still GDPR Art. 9 when
         used to identify. A CLASS B hit is a DUTY, not a prohibition, and
         conflating them is how a clear row gets reported as a blocked one.

What this is NOT
----------------
Not a clearance. It reads TOKENS, not behaviour: a model whose affect score lands
in a neutrally-named variable passes. It also cannot see a model fetched from a CDN
at runtime, which is how both face models in the p190 corpus are loaded. Use it to
decide WHERE TO READ, then read.
"""

from __future__ import annotations

import re

# CLASS A. Every pattern is anchored with \b on the left: that anchor is the whole
# point of the file. ".*" is never used — a bare "emotion" substring is the defect.
CLASS_A = (
    r"\bemotion[a-z_]*",
    r"\baffect(?:ive|_)[a-z_]*",
    r"\bmood\b",
    r"\bsentiment[a-z_]*",
    r"\bvalence\b",
    r"\barousal\b",
    r"\bfacial[_ ]expression",
    r"\bblendshape[a-z_]*",          # MediaPipe's 52 expression coefficients
    r"\boutputFaceBlendshapes\b",
    r"\bdrowsi[a-z]*",
    r"\bengagement[_ ]?score\b",
    r"\battention[_ ]?score\b",
)

# CLASS B. Biometric capture without an affect claim.
CLASS_B = (
    r"\bface[_ ]?(?:detect|recogn|track|mesh|landmark)[a-z_]*",
    r"\bgaze\b",
    r"\bhead[_ ]?pose\b",
    r"\beye[_ ]?track[a-z_]*",
    r"\bgetUserMedia\b",
    r"\bmediaDevices\b",
    r"\bmediapipe\b",
    r"\bface-api\b",
    r"\bhaarcascade\b",
    r"\bFaceLandmarker\b",
)

# Dependency and build trees. A hit inside one of these is the ecosystem's text,
# not the project's code, and must never reach a verdict.
VENDORED = (
    "node_modules", "vendor", "site-packages", "dist-info", ".venv", "venv",
    "bower_components", "third_party", "thirdparty", "external",
    ".git", "__pycache__", "dist", "build", ".next", "target",
)

_A = tuple(re.compile(p, re.I) for p in CLASS_A)
_B = tuple(re.compile(p, re.I) for p in CLASS_B)


def is_vendored(path: str) -> bool:
    """True when `path` lies inside a dependency or build tree."""
    parts = re.split(r"[/\\]", path)
    return any(part in VENDORED for part in parts)


def scan_text(text: str) -> dict:
    """Token hits in one blob. Returns {"a": [...], "b": [...]}, lower-cased."""
    a = [m.group(0).lower() for rx in _A for m in rx.finditer(text)]
    b = [m.group(0).lower() for rx in _B for m in rx.finditer(text)]
    return {"a": a, "b": b}


def scan_file(path: str, text: str) -> dict:
    """Scan one file, skipping vendored paths entirely."""
    if is_vendored(path):
        return {"a": [], "b": [], "skipped": True, "path": path}
    hits = scan_text(text)
    hits.update(skipped=False, path=path)
    return hits


def verdict(file_hits) -> dict:
    """Roll per-file results into the only three statements this screen may make."""
    a, b, skipped = [], [], 0
    for h in file_hits:
        if h.get("skipped"):
            skipped += 1
            continue
        a.extend(h["a"])
        b.extend(h["b"])
    if a:
        v = "CLASS_A_PRESENT"          # candidate Art. 5(1)(f) exposure -> READ THE CODE
    elif b:
        v = "CLASS_B_ONLY"            # biometric capture, no affect token
    else:
        v = "NO_BIOMETRIC_SIGNAL"     # not in scope of 5(1)(f) on this evidence
    return {"verdict": v, "class_a": sorted(set(a)), "class_b": sorted(set(b)),
            "vendored_files_skipped": skipped}
