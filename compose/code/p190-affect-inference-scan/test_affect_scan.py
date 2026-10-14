"""P1058 tests. Every fixture is verbatim from the p190 corpus or from the two
defects that corpus exposed. Run: python3 -I test_affect_scan.py"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])

from affect_scan import is_vendored, scan_file, scan_text, verdict

T = 0
def ok(cond, name):
    global T
    T += 1
    if not cond:
        print(f"FAIL {T}: {name}"); sys.exit(1)

# --- the defect that nearly produced a false accusation -----------------------
# caniuse-lite/data/features/deviceorientation.js, verbatim shape.
DEVICE_MOTION = "deviceMotionEvent,deviceMotionEventRotationRate,deviceMotionEventAcceleration"
ok(scan_text(DEVICE_MOTION)["a"] == [],
   "a \\b-anchored 'emotion' must NOT fire inside deviceMotionEvent")

# The unanchored pattern the first draft used. Kept as a guard so the anchor is
# never dropped: if this ever stops matching, the fixture has changed, not the fix.
import re
ok(re.search(r"emotion[a-z_]*", DEVICE_MOTION, re.I) is not None,
   "the UNANCHORED pattern does fire here -- this is why the anchor exists")

# mime-db/db.json carries application/emotionml+xml. The token IS a real word here,
# so the anchor cannot save it; the vendored-path rule must.
ok(is_vendored("frontend/node_modules/mime-db/db.json"), "node_modules is vendored")
ok(scan_file("frontend/node_modules/mime-db/db.json",
             '"application/emotionml+xml": {}')["skipped"] is True,
   "a vendored file is skipped, not scanned")
ok(scan_text('"application/emotionml+xml"')["a"] == ["emotionml"],
   "and the same bytes DO hit when they are not vendored -- so the skip is load-bearing")

ok(is_vendored("a/vendor/b.php") and is_vendored("x/.venv/y.py")
   and is_vendored("lib/site-packages/z.py") and is_vendored("app/dist/bundle.js"),
   "other vendored tree names")
ok(not is_vendored("client/src/student/worker/detection.worker.ts"),
   "real source is not vendored")
ok(not is_vendored("src/vendored_notes.py"),
   "a path SEGMENT must match -- a filename containing 'vendor' is source")

# --- shaheeranser/exam-proctor: the real options block, verbatim --------------
EXAM_PROCTOR = """
        faceLandmarker = await FaceLandmarker.createFromOptions(filesetResolver, {
          baseOptions: { modelAssetPath: '.../face_landmarker.task', delegate: 'GPU' },
          runningMode: 'VIDEO', numFaces: 1,
          outputFacialTransformationMatrixes: true,
        });
        const { yaw, pitch } = yawPitchFromMatrix(matrix.data);
        detections.push({ label: 'head_pose', confidence: 1.0 });
        const irisDev = computeIrisDeviation(landmarks);
"""
h = scan_file("client/src/student/worker/detection.worker.ts", EXAM_PROCTOR)
v = verdict([h])
ok(v["verdict"] == "CLASS_B_ONLY", "exam-proctor is CLASS B only -- no affect token")
ok("facelandmarker" in v["class_b"] and "head_pose" in v["class_b"],
   "head pose and the landmarker are CLASS B")
ok(v["class_a"] == [], "and nothing in CLASS A")

# One line flips it from an Annex III duty into an Article 5 PROHIBITION.
FLIPPED = EXAM_PROCTOR.replace("outputFacialTransformationMatrixes: true,",
                               "outputFacialTransformationMatrixes: true,\n"
                               "          outputFaceBlendshapes: true,")
v2 = verdict([scan_file("client/src/x.ts", FLIPPED)])
ok(v2["verdict"] == "CLASS_A_PRESENT",
   "outputFaceBlendshapes:true must be CLASS A -- the one-line crossing")
ok("outputfaceblendshapes" in v2["class_a"], "and it is named in the verdict")

# --- singhrajvardhan/SecureExam-Platform: face_detected as a boolean ----------
SECURE_EXAM = ("if(in_array($data['activity_type'], ['tab_switch','no_face_detected',"
               "'multiple_faces','copy_attempt','paste_attempt'])) {"
               " SUM(CASE WHEN face_detected = 1 THEN 1 ELSE 0 END)")
v3 = verdict([scan_file("api/track_activity.php", SECURE_EXAM)])
ok(v3["verdict"] == "CLASS_B_ONLY", "a face-presence counter is CLASS B, not CLASS A")

# --- VIJAYAPANDIANT/online-examination-system: the browser lock ---------------
EXAM_JAIL = """
  document.addEventListener("visibilitychange", handleVisibilityChange);
  document.addEventListener("fullscreenchange", handleFullscreenChange);
  window.addEventListener("contextmenu", handleContextMenu);
"""
v4 = verdict([scan_file("frontend/src/components/ExamJail.jsx", EXAM_JAIL),
              scan_file("frontend/node_modules/caniuse-lite/x.js", DEVICE_MOTION)])
ok(v4["verdict"] == "NO_BIOMETRIC_SIGNAL",
   "a browser lock has NO biometric signal -- it is not in 5(1)(f) scope at all")
ok(v4["vendored_files_skipped"] == 1, "and the vendored file was skipped, not counted")

# --- the separation itself ----------------------------------------------------
ok(verdict([scan_file("s.py", "engagement_score = model(frame)")])["verdict"]
   == "CLASS_A_PRESENT", "an engagement score is affect inference")
ok(verdict([scan_file("s.py", "sentiment = classify(text)")])["verdict"]
   == "CLASS_A_PRESENT", "sentiment is CLASS A")
ok(verdict([scan_file("s.py", "x = 1")])["verdict"] == "NO_BIOMETRIC_SIGNAL",
   "silence is silence")

print(f"PASS {T}/{T} — P1058")
