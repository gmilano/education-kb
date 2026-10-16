#!/usr/bin/env python3
"""Offline controls for p233's response classifier. Every case below is a REAL measurement
from this pass or from p232, not a hypothetical."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from classify_response import (ABSENT, CHALLENGED, NOT_ESTABLISHED, PRESENT,
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
    # the SAME 1-byte 404 becomes an absence ONLY with a control that passed in the window
    ("1-byte 404 WITH a passing control", 404, " ", "<a href", True, ABSENT),
    # a 404 carrying a real error document is a genuine miss
    ("GCS NoSuchKey", 404, GCS_404, "<metadata", False, ABSENT),
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

# The load-bearing property, asserted directly: the SAME 404 body must NOT yield the same
# verdict with and without a passing control. If this ever holds, the classifier has lost the
# distinction the whole pass was about.
without = classify(404, " ", expect_token="<a href", control_passed=False)
with_ctl = classify(404, " ", expect_token="<a href", control_passed=True)
if without == with_ctl:
    print(f"FAIL  the control must change the verdict on an empty 404 (both {without})")
    fails += 1

# And a 200 must never be reported as a read on the strength of its status alone.
if classify(200, PYPI_CHALLENGE, expect_token="results") == PRESENT:
    print("FAIL  a 200 with a challenge body was reported as PRESENT")
    fails += 1

print(f"{len(CASES) + 2 - fails}/{len(CASES) + 2} PASS" if not fails else f"{fails} FAILURES")
sys.exit(1 if fails else 0)
