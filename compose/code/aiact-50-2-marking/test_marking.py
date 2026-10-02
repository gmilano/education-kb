#!/usr/bin/env python3
"""Pass 46, action 1 (gap 95). The three assertions the action names, plus the
vocabulary-drift and SCORM-conformance checks.

Run:  python3 test_marking.py
      python3 test_marking.py --with-xmllint   (also validates a real manifest)
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import marking as M

HERE = os.path.dirname(os.path.abspath(__file__))
checks: list[tuple[bool, str, str]] = []


def check(ok, label, detail=""):
    checks.append((bool(ok), label, detail))
    print("  %-4s %s%s" % ("ok" if ok else "FAIL", label, ("  -- " + detail) if detail else ""))


# A turn that mixes all three authorship kinds -- the realistic case, and the one
# a turn-level boolean cannot describe.
SEGMENTS = [
    ("La fotosintesis convierte luz en energia quimica. ", "direct_source"),
    ("Entonces, en tu experimento la planta tapada crecio menos porque le faltaba luz. ", "mentor_inference"),
    ("Dijiste que la regaste todos los dias. ", "learner_observation"),
]


def main():
    print("-- vocabulary: no drift from the upstream policy file --")
    policy = open(os.path.join(HERE, "fixtures-provenance-policy.md"), encoding="utf-8").read()
    found = re.findall(r"^-\s+`([a-z_]+)`:", policy, re.M)
    check(len(found) == 9, "the policy file lists exactly 9 values", "found %d" % len(found))
    check(tuple(found) == M.VOCABULARY,
          "marking.py's vocabulary matches it value for value and in order",
          "drift would mean a label silently falling through to the fail-closed default")
    check(sum(M.PROVENANCE_SYNTHETIC.values()) == 5,
          "FIVE values map to synthetic, not the four pass 45 counted",
          "the fifth is `unsupported`, marked True deliberately -- see marking.py")

    print("\n-- assertion 1: a span quoted verbatim from a source is NOT marked --")
    spans = M.spans_from_segments(SEGMENTS)
    quoted = spans[0]
    check(quoted["provenance"] == "direct_source" and quoted["synthetic"] is False,
          "direct_source span carries synthetic=False",
          "marking a teacher's own sentence as AI-written is wrong data, not caution")
    check(all(not s["synthetic"] for s in spans if s["provenance"] in
              ("direct_source", "learner_observation", "learner_hypothesis", "real_world_evidence")),
          "no human-authored category is marked synthetic")

    print("\n-- assertion 2: a mentor_inference span IS marked --")
    inferred = spans[1]
    check(inferred["synthetic"] is True, "mentor_inference span carries synthetic=True",
          '"runtime interpretation not stated by the teacher" is the model\'s own words')
    check(inferred["provenance"] == "mentor_inference",
          "and the ORIGINAL label is kept beside the boolean",
          "the boolean answers the regulator, the label answers the teacher")

    payload = M.build_marked_provenance(spans=spans, scene="tutor_chat", workflow="socratic")
    check(payload["generated"] is True, "the turn reports generated=True because one span is synthetic")
    check(payload["synthetic_span_count"] == 1 and payload["span_count"] == 3,
          "1 of 3 spans synthetic, counted not assumed",
          "%d chars of %d" % (payload["synthetic_char_count"],
                              sum(len(t) for t, _ in SEGMENTS)))

    # The stricter-than-upstream case: OpenTutor's agent path hard-codes
    # generated=True, so it cannot represent this turn at all.
    only_quotes = M.build_marked_provenance(
        spans=M.spans_from_segments([(t, p) for t, p in SEGMENTS if p != "mentor_inference"]))
    check(only_quotes["generated"] is False,
          "a turn that only quotes and relays reports generated=False",
          "measured span by span; OpenTutor's turn path would report True here")

    print("\n-- assertion 3: the mark survives dumps -> loads of the DETACHED artifact --")
    artifact = M.detach_artifact(payload)
    check("spans" in artifact and "text" in artifact,
          "the detached artifact carries text and spans, no envelope")
    revived = M.round_trip(artifact)
    check(revived == artifact, "byte-for-byte identical after json.dumps -> json.loads")
    check(revived["generated"] is True, "the turn-level mark survives detachment")
    check(M.synthetic_ranges(revived) == M.synthetic_ranges(artifact),
          "the synthetic RANGES survive, so the marking is still per-span after transport",
          str(M.synthetic_ranges(revived)))

    # The offsets have to index the delivered text, or a consumer cannot show the
    # reader WHICH words were generated.
    text = revived["text"]
    a, b = M.synthetic_ranges(revived)[0]
    check(text[a:b] == SEGMENTS[1][0],
          "the surviving offsets select exactly the generated sentence",
          repr(text[a:b][:46] + "...")) 
    check(text == "".join(t for t, _ in SEGMENTS),
          "and the reassembled text is the delivered text, unchanged")

    print("\n-- fail-closed behaviour --")
    unknown = M.mark_span(text="x", provenance="some_future_label")
    check(unknown["synthetic"] is True, "an unrecognised label is marked synthetic")
    check(M.UNKNOWN_LABEL in unknown.get("flags", []),
          "and is flagged, so it is visible rather than merely safe")
    for bad in (None, "", 7):
        try:
            M.is_synthetic(bad)
            check(False, "rejects %r" % (bad,))
        except M.ProvenanceError:
            check(True, "rejects %r with ProvenanceError" % (bad,))

    print("\n-- the SCORM injection point (gap 97, measured in action 3) --")
    frag = M.manifest_metadata_fragment(artifact)
    check('xmlns:m="urn:globant:aiact:50-2"' in frag,
          "the marker declares its OWN namespace",
          "a default-namespace element fails xsd validation -- measured, see README")
    check('value="true"' in frag and '<m:span start=' in frag,
          "the fragment carries the boolean and the span ranges")

    if "--with-xmllint" in sys.argv:
        ok, detail = validate_manifest(frag)
        check(ok, "a manifest carrying the marker validates against imscp_v1p1.xsd", detail)
    else:
        print("  skip  xmllint conformance (pass --with-xmllint and set SCORM_SCHEMAS)")

    failed = [c for c in checks if not c[0]]
    print("\n%d/%d checks passed" % (len(checks) - len(failed), len(checks)))
    if failed:
        sys.exit(1)
    print("""
ACTION 1 VERIFIED (gap 95). The transversal Article 50(2) marking component exists:
lineage-skill's 9 labels -> a boolean plus the original label, carried in
OpenTutor's payload shape extended to the SPAN, and surviving detachment from the
envelope. The signature seam (MarkLLM / SynthID, P33) is declared and NOT filled.""")


def validate_manifest(fragment):
    schemas = os.environ.get("SCORM_SCHEMAS")
    if not schemas or not os.path.isdir(schemas):
        return False, "set SCORM_SCHEMAS to a dir holding scorm-mcp-server/schemas/*.xsd"
    import shutil
    import tempfile
    if not shutil.which("xmllint"):
        return False, "xmllint not on PATH"
    manifest = """<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="M1" version="1.0"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_v1p3"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd http://www.adlnet.org/xsd/adlcp_v1p3 adlcp_v1p3.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>2004 4th Edition</schemaversion>
    %s
  </metadata>
  <organizations default="ORG-1">
    <organization identifier="ORG-1">
      <title>T</title>
      <item identifier="ITEM-1" identifierref="RES-1" isvisible="true"><title>T</title></item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES-1" type="webcontent" adlcp:scormType="sco" href="index.html">
      <file href="index.html"/>
    </resource>
  </resources>
</manifest>
""" % fragment
    with tempfile.TemporaryDirectory() as d:
        for n in os.listdir(schemas):
            if n.endswith(".xsd"):
                shutil.copy(os.path.join(schemas, n), d)
        p = os.path.join(d, "imsmanifest.xml")
        open(p, "w", encoding="utf-8").write(manifest)
        r = subprocess.run(["xmllint", "--noout", "--schema",
                            os.path.join(d, "imscp_v1p1.xsd"), p],
                           capture_output=True, text=True)
        return r.returncode == 0, (r.stderr.strip().splitlines() or ["validates"])[-1]


if __name__ == "__main__":
    main()
