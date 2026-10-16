"""Controls for `p253-captured-body-census` (`ACTION XY`).

Signals failure with an explicit non-zero exit and a count of the checks it ran, so it
cannot pass while asserting nothing — `p251`'s five `unittest.main()` controls and
`p252`'s `71` ungated suites are the reason this file does not use `unittest.main()`.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import captured_body as cb  # noqa: E402

FAILED = []
RAN = 0


def chk(name, got, want):
    global RAN
    RAN += 1
    if got != want:
        FAILED.append("  FAIL %s\n       got  %r\n       want %r" % (name, got, want))
    else:
        print("  OK   %s" % name)


# ── the shapes, one at a time ────────────────────────────────────────────────────────────
chk("a status capture is not a body",
    cb.capture_shape("curl -s -o /dev/null -w '%{http_code}' \"$u\""), "STATUS")
chk("a HEAD request is not a body",
    cb.capture_shape("curl -sI \"$u\""), "STATUS")
chk("a measuring pipe inside the substitution holds a NUMBER",
    cb.capture_shape("curl -s \"$u\" | wc -c | tr -d ' '"), "MEASURED")
chk("a sha256 pipe inside the substitution holds a NUMBER",
    cb.capture_shape("curl -sS \"$u\" | sha256sum | cut -c1-16"), "MEASURED")
chk("a bare fetch holds the BODY",
    cb.capture_shape("curl -sS --max-time 25 \"$u\""), "BODY")
chk("cat of a payload holds the BODY too — P834 is not curl-specific",
    cb.capture_shape("cat \"$1\""), "BODY")
chk("an output file means the body never entered the capture",
    cb.capture_shape("curl -s -o \"$dest\" -w '%{http_code}' \"$u\""), "STATUS")
chk("no producer at all is OTHER",
    cb.capture_shape("date +%Y-%m-%d"), "OTHER")

# 🔴 The false NEGATIVE this instrument shipped on its second run: `2>/dev/null` read as an
# output file, which made `lib/payload_measure.sh` vanish from the census entirely.
chk("stderr redirection is NOT an output file (the measured false negative)",
    cb.capture_shape("cat \"$1\" 2>/dev/null"), "BODY")
chk("stdout to /dev/null IS a discarded body",
    cb.capture_shape("curl -s \"$u\" > /dev/null"), "STATUS")

# ── comments are not code ───────────────────────────────────────────────────────────────
# 🔴 The first run's false POSITIVE: `p117-second-channel/licence.sh` graded CAPTURED on a
# comment that quotes the defect in order to warn against it.
WARNING_ONLY = '''#!/usr/bin/env bash
#     body=$(curl -sS -f "$RAW/$slug/$br/$p")   # <- the trailing newline run dies HERE
#     …  "$(printf '%s' "$body" | wc -c)"       # <- and the count is low by that much
f=$(wc -c < "$dest" | tr -d ' ')
printf '%s\\n' "$f"
'''
chk("a comment quoting the defect is not the defect",
    cb.classify_text(WARNING_ONLY)["verdict"], "CLEAN")
chk("a `#` inside a quoted string is not a comment",
    cb.strip_comments('x="a#b"\n').strip(), 'x="a#b"')

# ── co-occurrence is not consumption ────────────────────────────────────────────────────
# 🔴 The third measured false positive: the hash and the size come from the FILE, and the
# capture goes only to a newline-INSENSITIVE classifier, all on one line.
FILE_MEASURED = '''#!/usr/bin/env bash
payload=$(cat "$f")
printf '%s\\t%s\\t%s\\n' "$(sha256sum "$f"|cut -c1-12)" "$(stat -c%s "$f")" "$(family_of "$payload")"
'''
chk("a file-measured line that merely MENTIONS the capture is BODY-ONLY",
    cb.classify_text(FILE_MEASURED)["verdict"], "BODY-ONLY")

DEFECT = '''#!/usr/bin/env bash
body=$(curl -sS "$u")
bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
printf '%s\\n' "$bytes"
'''
chk("the canonical P834 shape is CAPTURED-LIVE",
    cb.classify_text(DEFECT)["verdict"], "CAPTURED-LIVE")

HERESTRING = '''#!/usr/bin/env bash
body=$(curl -sS "$u")
h=$(sha256sum <<< "$body")
'''
chk("the here-string shape is CAPTURED-LIVE too",
    cb.classify_text(HERESTRING)["verdict"], "CAPTURED-LIVE")

DECLARED = '''#!/usr/bin/env bash
size_of_capture_BROKEN() {
  local b; b=$(cat "$1" 2>/dev/null)
  printf '%s' "$b" | wc -c | tr -d ' '
}
'''
chk("a defect preserved under a BROKEN-named function is a CONTROL, not a live site",
    cb.classify_text(DECLARED)["verdict"], "CAPTURED-CONTROL")

SUBJECT = '''#!/usr/bin/env bash
full=$(wc -c < "$tmp" | tr -d ' ')
body="$(cat "$tmp")"
strip=$(printf '%s' "$body" | wc -c | tr -d ' ')
printf '%s\\t%s\\n' "$full" "$strip"
'''
chk("measuring the SAME payload by BOTH channels is the SUBJECT, not a defect",
    cb.classify_text(SUBJECT)["verdict"], "CAPTURED-SUBJECT")

# ── the mandated falsifier, on the real file ─────────────────────────────────────────────
# `ACTION XY` limb 1, verbatim: *"Falsified if the rule flags
# p176-grant-path-vocabulary/probe_spellings.sh, which pipes and is sound."*
P176 = os.path.join(cb.CODE_ROOT, "p176-grant-path-vocabulary", "probe_spellings.sh")
chk("ACTION XY's own falsifier: p176/probe_spellings.sh exists to be graded",
    os.path.exists(P176), True)
if os.path.exists(P176):
    chk("ACTION XY's own falsifier: p176/probe_spellings.sh is PIPED, never CAPTURED",
        cb.classify_file(P176)["verdict"], "PIPED")

# ── the real shelf, graded ──────────────────────────────────────────────────────────────
ROWS = cb.census()
chk("the census reaches the whole .sh population", len(ROWS) >= 300, True)
LIVE = sorted(p for p, r in ROWS.items() if r["verdict"] == "CAPTURED-LIVE")
# 🟢 All five were read by hand, then FIXED in this same pass: each now fetches to a file
# and sizes the file, keeping the capture for the newline-insensitive classifier only.  So
# the live population is `0` and this control is what keeps it there — a sixth site, or a
# regression in one of the five, fails the gate by name.
chk("no instrument measures a payload through a captured body", LIVE, [])
chk("the five sites p253 fixed are now BODY-ONLY, not CAPTURED",
    [ROWS.get(p, {}).get("verdict", "MISSING") for p in (
        "p117-second-channel/title.sh",
        "p122-prose-licence-census/scan_licences.sh",
        "p326-titleholder-book-license/sweep_titleholder.sh",
        "p784-licence-scope-map/probe.sh",
    )], ["BODY-ONLY"] * 4)
# `p326/controls.sh` asks "why three different byte counts for the same family", so it now
# prints BOTH channels labelled — which is the SUBJECT grade, not a defect.
chk("p326/controls.sh now measures both channels explicitly",
    ROWS.get("p326-titleholder-book-license/controls.sh", {}).get("verdict", "MISSING"),
    "CAPTURED-SUBJECT")
chk("lib/payload_measure.sh is graded as the declared control it is",
    ROWS.get("lib/payload_measure.sh", {}).get("verdict", "MISSING"), "CAPTURED-CONTROL")
chk("the class's own instruments are SUBJECT, not defects",
    sorted(p for p, r in ROWS.items() if r["verdict"] == "CAPTURED-SUBJECT"), [
        "p178-byte-channel-census/test_check_channel.sh",
        "p178-byte-channel-census/two_channels.sh",
        "p179-capture-shape/test_capture_shape.sh",
        "p179-capture-shape/trailing_census.sh",
        "p326-titleholder-book-license/controls.sh",
    ])
chk("probe_payload.sh carries the pass-74 fix and stays clean",
    ROWS.get("lib/probe_payload.sh", {}).get("verdict", "MISSING"), "CLEAN")

# ── the pins ────────────────────────────────────────────────────────────────────────────
PINS = cb.read_pins()
chk("sites.tsv exists — a missing pin file is a FAILURE, never a clean census", PINS is not None, True)
if PINS is not None:
    chk("--verify agrees with the live census", cb.verify(PINS, ROWS), [])
    chk("an absent pin file does not read as clean",
        cb.verify(None, ROWS)[0].startswith("UNPINNED"), True)
    fake = dict(PINS)
    fake["p117-second-channel/title.sh"] = {"path": "p117-second-channel/title.sh",
                                            "verdict": "CAPTURED-LIVE"}
    chk("a verdict silently downgraded in the pins is caught",
        any(b.startswith("CHANGED") for b in cb.verify(fake, ROWS)), True)
    dropped = {k: v for k, v in PINS.items() if k != "p784-licence-scope-map/probe.sh"}
    chk("a live site missing from the pins is caught",
        any(b.startswith("NEW") for b in cb.verify(dropped, ROWS)), True)

print()
if FAILED:
    print("\n".join(FAILED))
    print("test_captured_body.py: %d/%d checks passed, %d FAILED" % (RAN - len(FAILED), RAN, len(FAILED)))
    sys.exit(1)
print("test_captured_body.py: %d/%d checks passed" % (RAN, RAN))
sys.exit(0)
