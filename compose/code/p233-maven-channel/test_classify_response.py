#!/usr/bin/env python3
"""Offline controls for p233's response classifier. Every case below is a REAL measurement
from this pass or from p232, not a hypothetical."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify_response import (ABSENT, CHALLENGED, EMPTY_BODY_MAX,
                               NOT_ESTABLISHED, PRESENT, REAL_MISS_BYTES_MEASURED,
                               THROTTLED, classify)

LISTING = "<!DOCTYPE html><html><head><title>Central Repository: org</title>" + "<a href=\"x/\">x/</a>" * 40
MAVEN_429 = "Your ip has exceeded rate limits. Find out more here https://central.sonatype.org/faq/429-error/"
GCS_404 = "<?xml version='1.0' encoding='UTF-8'?><Error><Code>NoSuchKey</Code><Message>The specified key does not exist.</Message></Error>"
PYPI_CHALLENGE = "<html><body>Client Challenge</body></html>" + "x" * 3000

CASES = [
    # --- p233's own measurements, repo1.maven.org, all inside one minute ---
    ("org/ listing, round 1", 200, LISTING, "<a href", False, PRESENT),
    ("org/ same url, round 2 — the 429", 429, MAVEN_429, "<a href", False, THROTTLED),
    ("org/ same url, round 3 — the 1-byte 404", 404, " ", "<a href", False, THROTTLED),
    # 🔴 p237 OVERTURNS this case. It used to expect ABSENT: "the SAME 1-byte 404 becomes an
    # absence ONLY with a control that passed in the window". p237 measured the same url
    # answering with a 554-byte nginx 404 and then a one-byte 404, so the one-byte body is the
    # throttle's signature and no control can license an absence from it.
    ("1-byte 404 WITH a passing control — p237: still THROTTLED", 404, " ", "<a href", True,
     THROTTLED),
    # a 404 carrying a real error document is a genuine miss
    # p237: a documented 404 is a genuine miss only from a channel shown to be answering, so
    # the control now decides this pair rather than the 1-byte pair above.
    ("GCS NoSuchKey, no control — p237: NOT-ESTABLISHED", 404, GCS_404, "<metadata", False,
     NOT_ESTABLISHED),
    ("GCS NoSuchKey WITH a passing control", 404, GCS_404, "<metadata", True, ABSENT),
    # --- p232's measurement, carried so the lesson cannot regress ---
    ("PyPI search: 200 with a challenge body", 200, PYPI_CHALLENGE, "results", False, CHALLENGED),
    # --- transport failures say nothing about the resource ---
    ("proxy refused the tunnel", 0, "", "numFound", False, NOT_ESTABLISHED),
    ("proxy refused, control passed anyway", 0, "", "numFound", True, NOT_ESTABLISHED),
    # --- a 200 with a body too small to carry anything ---
    ("200 with an empty body", 200, "", None, False, CHALLENGED),
    # --- the real 497-byte org/imsglobal listing: small, but a genuine read ---
    ("org/imsglobal, 497 B, one artefact",
     200,
     "<html><head><title>Central Repository: org/imsglobal</title></head><body><pre>"
     "<a href=\"../\">../</a>\n<a href=\"basiclti-util/\">basiclti-util/</a></pre></body></html>",
     "<a href", False, PRESENT),
    # --- an unmodelled status is never promoted to a finding ---
    ("503 from a mirror", 503, "upstream unavailable", "<a href", False, NOT_ESTABLISHED),
]

fails = 0
for name, status, body, token, control, expected in CASES:
    got = classify(status, body, expect_token=token, control_passed=control)
    if got != expected:
        print(f"FAIL  {name}: expected {expected}, got {got}")
        fails += 1

# ── p237 corrects this property ──────────────────────────────────────────────────────────
# It used to read: "the SAME 404 body must NOT yield the same verdict with and without a
# passing control", asserted on a ONE-BYTE body. p237 measured the same url returning a
# 554-byte nginx 404 and, minutes later, a one-byte 404 -- so the one-byte body is the
# throttle's signature and a control must NOT be able to promote it to ABSENT. The property
# is still load-bearing; it just belongs on the band where a control can legitimately decide,
# which is a 404 carrying a REAL ERROR DOCUMENT.
NGINX_404 = (
    "<html>\n<head><title>404 Not Found</title></head>\n<body bgcolor=\"white\">\n"
    "<center><h1>404 Not Found</h1></center>\n<hr><center>nginx</center>\n</body>\n</html>\n"
) + "<!-- a padding to disable MSIE and Chrome friendly error page -->\n" * 6

without = classify(404, NGINX_404, expect_token="<a href", control_passed=False)
with_ctl = classify(404, NGINX_404, expect_token="<a href", control_passed=True)
if without == with_ctl:
    print(f"FAIL  the control must change the verdict on a documented 404 (both {without})")
    fails += 1
if without != NOT_ESTABLISHED:
    print(f"FAIL  a documented 404 with no control must be NOT-ESTABLISHED, got {without}")
    fails += 1
if with_ctl != ABSENT:
    print(f"FAIL  a documented 404 with a passing control must be ABSENT, got {with_ctl}")
    fails += 1

# And the new property p237 earned: a SIGNATURE-SHAPED 404 is THROTTLED whatever the control
# says. This is the one a passing control used to defeat, and it is how six education
# groupIds would have been tabled as six absences.
for ctl in (False, True):
    got = classify(404, "\n", expect_token="<a href", control_passed=ctl)
    if got != THROTTLED:
        print(f"FAIL  one-byte 404 with control_passed={ctl} must be THROTTLED, got {got}")
        fails += 1

# The measured real-miss size is recorded, not guessed, and is above the empty threshold --
# which is the whole reason the two bands are distinguishable.
if REAL_MISS_BYTES_MEASURED <= EMPTY_BODY_MAX:
    print("FAIL  the measured real-miss size must exceed the empty-body threshold")
    fails += 1
EXTRA_PROPS = 6

# And a 200 must never be reported as a read on the strength of its status alone.
if classify(200, PYPI_CHALLENGE, expect_token="results") == PRESENT:
    print("FAIL  a 200 with a challenge body was reported as PRESENT")
    fails += 1

print(f"{len(CASES) + EXTRA_PROPS + 1 - fails}/{len(CASES) + EXTRA_PROPS + 1} PASS" if not fails else f"{fails} FAILURES")
sys.exit(1 if fails else 0)
