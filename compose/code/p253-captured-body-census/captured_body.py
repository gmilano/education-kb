"""`ACTION XY` (p252) — bound the population of instruments that measure a payload's
bytes or `sha256` through a CAPTURED BODY rather than through a file or a pipe.

Why this exists.  `P834` is this base's oldest live defect class: `body=$(cmd …)` strips
the entire run of trailing newlines, so `printf '%s' "$body" | wc -c` reads short and
`sha256sum` reads a hash that can never be reproduced from the payload.  `p178`
("Channel B (STRIPPING)") and `p179` ("capture shape") own the class; `lib/payload_measure.sh`
carries the fix.  Neither ever COUNTED the population, and `p252` walked into the defect on
its own first probe — three grant payloads one byte short, three unreproducible `sha256`s —
on a shelf that pins SHAs.  A class that is documented and uncounted is a class nobody can
close.

The discriminator, and it is the whole instrument.  `p252`'s `ACTION XY` limb 1 states it:
a pipe to `wc -c` / `sha256sum` is CORRECT and must not be swept up.  What makes a site
defective is not the `$(…)` — it is whether the payload BODY passes through a shell
VARIABLE on its way to the measurement.  So each command substitution is classified by what
its capture HOLDS:

    STATUS    the capture holds an HTTP status or a header  (`-w '%{http_code}'`, `-o /dev/null`, `-I`)
    MEASURED  the capture holds a NUMBER — the body was piped into a measuring command
              INSIDE the substitution, so the trailing-newline run was counted before any
              shell could strip it
    BODY      the capture holds the payload itself — a content producer with neither an
              output file nor a measuring pipe
    OTHER     no content producer inside the substitution

and a script is `CAPTURED` only when a `BODY`-holding variable is then READ by a byte or
hash measurement.  A `BODY` capture that is only grepped or classified is `BODY-ONLY`:
`family_of`/`holder_of` are newline-insensitive, so those verdicts stand — which is
`lib/payload_measure.sh`'s own stated scope, reused here rather than re-reasoned.

What this instrument does NOT claim.  It reads shell source lexically.  It cannot see a
body that reaches a measurement through a second variable, an array, or a function
argument.  Every verdict is therefore a LOWER bound on the defect and an UPPER bound on
cleanliness, and `--verify` pins the population so a later pass sees movement rather than
re-deriving it.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE_ROOT = os.path.dirname(HERE)
PINS = os.path.join(HERE, "sites.tsv")

# A content producer: a command whose stdout is the payload body.
PRODUCER = re.compile(r"(?:^|[|;&(]\s*|\s)(curl|wget|cat|_raw|raw_get|git\s+show|fetch_payload\w*)\b")

# Taken INSIDE a substitution, these consume the body and emit a number, so the capture
# holds a figure and not a body.  `P834` cannot reach a figure.
MEASURER = re.compile(r"\b(wc|sha256sum|sha1sum|md5sum|cksum|stat|grep\s+-c)\b")

# curl asked for metadata rather than a body.
# `-I` is routinely BUNDLED (`curl -sI`), so an unbundled-only pattern misses the HEAD
# request entirely and grades a metadata probe as a body capture.
STATUS = re.compile(r"-w\s*['\"]?%\{|-o\s*/dev/null|(?:^|\s)-[A-Za-z]*I(?:\s|$)|--head")

# A measurement READING a variable.  The `printf '%s' "$v" | wc -c` shape and the
# here-string shape are the two `p179` enumerated; `<<<` strips nothing itself but the
# variable already did.
MEASURE_READ = re.compile(r"\b(wc\s+-[cml]|sha256sum|sha1sum|md5sum|cksum)\b")

# A deliberately preserved defect, kept so a suite can assert the failing case.  Lexical,
# and named as such: the marker is the FUNCTION NAME, which is the only signal in the
# source that survives a refactor of the surrounding comment.
DECLARED_CONTROL = re.compile(r"\b\w*BROKEN\w*\b")


def strip_comments(text):
    """Blank every `#` comment, preserving length so positions stay valid.

    Found by inspecting this instrument's own first output: `p117-second-channel/licence.sh`
    graded `CAPTURED` on the strength of a four-line COMMENT quoting the defect in order to
    warn against it.  A census that reads a warning as the thing it warns about is worse
    than no census, because the false positive lands on exactly the instruments that paid
    most attention to the class.  `#` inside single or double quotes is not a comment.
    """
    out = list(text)
    i, n = 0, len(text)
    quote = None
    while i < n:
        c = text[i]
        if quote:
            if c == "\\" and quote == '"':
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in "'\"":
            quote = c
        elif c == "#":
            j = text.find("\n", i)
            j = n if j < 0 else j
            for k in range(i, j):
                out[k] = " "
            i = j
            continue
        i += 1
    return "".join(out)


def substitutions(text):
    """Yield (varname_or_None, inner_text) for each `$( … )`, non-nested.

    A nested `$( … )` is reported as its own site; the outer one keeps the inner text, so
    a measuring pipe in either position is seen.  Backticks are NOT handled — measured
    below and reported by `backtick_sites`.
    """
    out = []
    # `body="$(cat "$tmp")"` is the same assignment as `body=$(cat "$tmp")`, and an
    # unquoted-only pattern loses it — a FALSE NEGATIVE, the direction that cannot be
    # noticed downstream.  Measured on `p178-byte-channel-census/two_channels.sh`.
    for m in re.finditer(r"([A-Za-z_][A-Za-z0-9_]*)=[\"']?\$\(|(?<!\$)\$\(", text):
        start = m.end()
        depth = 1
        i = start
        while i < len(text) and depth:
            if text[i] == "(":
                depth += 1
            elif text[i] == ")":
                depth -= 1
            i += 1
        out.append((m.group(1), text[start : i - 1], m.start()))
    return out


def capture_shape(inner):
    """What a `$( inner )` capture HOLDS."""
    if not PRODUCER.search(inner):
        return "OTHER"
    if STATUS.search(inner):
        return "STATUS"
    if "|" in inner and MEASURER.search(inner.split("|", 1)[1]):
        return "MEASURED"
    # An OUTPUT FILE means the body never entered the capture.  `2>` and `&>` are not
    # output files, and reading them as one is a FALSE NEGATIVE — measured on
    # `lib/payload_measure.sh`, whose `b=$(cat "$1" 2>/dev/null)` graded `STATUS` and so
    # vanished from the census entirely.  A census that loses a site is worse than one that
    # over-reports, because nothing downstream can notice the absence.
    if re.search(r"-o\s+(?!/dev/null)\S|-O\b|(?<![0-9&])>\s*\S", inner):
        return "STATUS"
    return "BODY"


def enclosing_function(text, pos):
    """Name of the shell function containing `pos`, or None."""
    name = None
    for m in re.finditer(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(\)\s*\{", text, re.M):
        if m.start() > pos:
            break
        name = m.group(1)
    return name


def measured_vars(text, names):
    """Which of `names` are CONSUMED by a byte/hash measurement.

    Co-occurrence on a line is NOT consumption, and reading it as such is this
    instrument's third measured defect.  `p172-manifest-attribution/classify_bodies.sh`
    and `p173-apache11-family/sweep_family.sh` both print

        "$(sha256sum "$f" | cut -c1-12)"  "$(stat -c%s "$f")"  "$(family_of "$payload")"

    on ONE line: the hash and the size are taken from the FILE, and the capture goes only
    to `family_of`, which is newline-insensitive.  Both are sound, and a line-granularity
    rule called both defective.  So the variable must sit on the PRODUCING side of the pipe
    that feeds the measurer, or be its here-string — the two shapes `p179` enumerated.
    """
    hit = set()
    for n in names:
        v = r'[$]\{?' + re.escape(n) + r'\}?'
        pipe = r'(?:printf|echo|cat)\b[^|\n]*' + v + r'[^|\n]*\|[^\n]*?' + MEASURE_READ.pattern
        here = MEASURE_READ.pattern + r'[^\n]*<<<\s*"?' + v
        if re.search(pipe, text) or re.search(here, text):
            hit.add(n)
    return hit


def backtick_sites(text):
    """Legacy `` `cmd` `` captures of a producer — the same defect, a different spelling."""
    return [m.group(0) for m in re.finditer(r"`[^`]*`", text) if PRODUCER.search(m.group(0))]


# A FILED measurement reads from a FILE: `wc -c < path`.  `(?<!<)<(?!<)` is load-bearing —
# without it, `sha256sum <<< "$body"` matches on the third `<` and a here-string reads as a
# file redirect, which promoted the canonical defect shape to SUBJECT.
FILED_MEASURE = re.compile(
    r"\b(wc\s+-[cml]|sha256sum|sha1sum|md5sum|cksum)\b[^|\n]*(?<!<)<(?!<)\s*[\"']?\$?[A-Za-z_./{]"
)


def classify_text(raw):
    """Verdict plus the counts that justify it, for one shell script's source."""
    text = strip_comments(raw)
    subs = substitutions(text)
    shapes = {}
    body_vars = []
    for var, inner, _pos in subs:
        s = capture_shape(inner)
        shapes[s] = shapes.get(s, 0) + 1
        if s == "BODY" and var:
            body_vars.append(var)
    read = measured_vars(text, body_vars)
    ticks = backtick_sites(text)

    # Grading a CAPTURED site.  `p252`'s limb 1 warned against sweeping up sound sites; the
    # same care is owed to sites that hold the defect ON PURPOSE, because a census that
    # cannot tell a fixture from a live defect gets ignored on its second run.
    declared = False
    for var, inner, pos in subs:
        if var in read and capture_shape(inner) == "BODY":
            fn = enclosing_function(text, pos)
            if fn and DECLARED_CONTROL.search(fn):
                declared = True
    # SUBJECT: the script measures the SAME payload by BOTH channels, which is what an
    # instrument investigating `P834` must do.  Objective, not a judgement about intent.
    subject = bool(read) and bool(FILED_MEASURE.search(text))

    if read and declared:
        verdict = "CAPTURED-CONTROL"
    elif read and subject:
        verdict = "CAPTURED-SUBJECT"
    elif read:
        verdict = "CAPTURED-LIVE"
    elif body_vars:
        verdict = "BODY-ONLY"
    elif shapes.get("MEASURED"):
        verdict = "PIPED"
    elif shapes.get("STATUS"):
        verdict = "STATUS"
    else:
        verdict = "CLEAN"

    return {
        "verdict": verdict,
        "body": shapes.get("BODY", 0),
        "measured": shapes.get("MEASURED", 0),
        "status": shapes.get("STATUS", 0),
        "read": sorted(read),
        "backticks": len(ticks),
    }


def classify_file(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return classify_text(fh.read())


def walk(code_root=None):
    root = code_root or CODE_ROOT
    for dirpath, _dirs, files in os.walk(root):
        for f in sorted(files):
            if f.endswith(".sh"):
                p = os.path.join(dirpath, f)
                yield os.path.relpath(p, root), p


def census(code_root=None):
    rows = {}
    for rel, full in walk(code_root):
        r = classify_file(full)
        r["path"] = rel
        rows[rel] = r
    return rows


FIELDS = ("path", "verdict", "body", "measured", "status", "backticks")


def write_pins(rows, path=None):
    out = path or PINS
    keep = [r for r in rows.values() if r["verdict"] not in ("CLEAN", "STATUS")]
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\t".join(FIELDS) + "\n")
        for r in sorted(keep, key=lambda r: r["path"]):
            fh.write("\t".join(str(r[k]) for k in FIELDS) + "\n")
    return len(keep)


def read_pins(path=None):
    src = path or PINS
    if not os.path.exists(src):
        return None
    pins = {}
    with open(src, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if not line.strip():
                continue
            cells = line.rstrip("\n").split("\t")
            row = dict(zip(head, cells))
            pins[row["path"]] = row
    return pins


_UNSET = object()


def verify(pins=_UNSET, rows=_UNSET):
    """Non-zero on any NEW or CHANGED site.  A missing pin file is a FAILURE, never clean.

    `None` means *the pin file is absent* and is a distinct state from *not supplied*.
    The first draft used `None` for both, so the one control that asserts a missing pin
    file does not read as clean could not express the case at all — it silently re-read
    the real `sites.tsv` and returned `[]`.  That is `p252`'s own hazard, a new state
    falling through into the clean branch, in this instrument's verifier.
    """
    pins = read_pins() if pins is _UNSET else pins
    rows = census() if rows is _UNSET else rows
    if pins is None:
        return ["UNPINNED\tsites.tsv is absent — a missing pin file is not a clean census"]
    bad = []
    live = {p: r for p, r in rows.items() if r["verdict"] not in ("CLEAN", "STATUS")}
    for p, r in sorted(live.items()):
        if p not in pins:
            bad.append("NEW\t%s\t%s" % (p, r["verdict"]))
        elif pins[p]["verdict"] != r["verdict"]:
            bad.append("CHANGED\t%s\t%s -> %s" % (p, pins[p]["verdict"], r["verdict"]))
    for p in sorted(pins):
        if p not in live:
            bad.append("GONE\t%s\t%s" % (p, pins[p]["verdict"]))
    return bad


def main(argv):
    args = argv[1:]
    if "--pin" in args:
        rows = census()
        n = write_pins(rows)
        print("pinned %d sites" % n)
        return 0
    if "--verify" in args:
        bad = verify()
        for b in bad:
            print(b)
        if bad:
            print("FAIL: %d site(s) differ from sites.tsv" % len(bad))
            return 1
        print("OK: census matches sites.tsv")
        return 0
    rows = census()
    tally = {}
    for r in rows.values():
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    print("scripts\t%d" % len(rows))
    for k in sorted(tally):
        print("%s\t%d" % (k, tally[k]))
    for r in sorted(rows.values(), key=lambda r: r["path"]):
        if r["verdict"].startswith("CAPTURED"):
            print("%s\t%s\t%s" % (r["verdict"], r["path"], ",".join(r["read"])))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
