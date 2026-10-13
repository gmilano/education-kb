#!/usr/bin/env bash
# `ACTION KW` — p179.  Build a REAL corpus for `dolos`, with a ground truth this KB controls.
#
# `ACTION KQ` (p177) verified `dodona-edu/dolos` past its licence and measured its language
# coverage and its false-positive behaviour ON ITS OWN CONTROLS.  `ACTION KW` was then
# pre-registered twice (p177, p178) and attempted neither time, with one question left:
#
#   limb 1 — template exclusion (`-i`) materially changes the pair ranking → the `-i` step in
#            Pattern `1` is LOAD-BEARING and a client must be told to supply the template.
#   limb 2 — it does not → the step is CARGO CULT and the pattern should drop it.
#
# THE CORPUS.  Real code, not fixtures, and deliberately the code this same pass read for
# `ACTION KX`: the `13` Python modules and test files of `Li-Evan/Bloom`'s FastAPI backend
# (`4 009` lines tracked, `MIT`, `HEAD b3918981bb34`).  Using the pass's own subject means the
# corpus is auditable from this repository's other evidence rather than being a private fixture.
#
# THE GROUND TRUTH, which is what a corpus of real code otherwise lacks:
#
#   KNOWN POSITIVE 1  `p_rename.py`  — `recommendations.py` with every identifier mechanically
#                     renamed.  This is the transform a student actually performs; a detector
#                     that misses it is useless in an education engagement.
#   KNOWN POSITIVE 2  `p_rename_reorder.py` — the same, with the top-level definitions emitted in
#                     reverse order.  Harder, and the standard next step.
#   KNOWN NEGATIVES   every other pair among the `13` real files.  They share a framework, an
#                     ORM, a test style and an author, so they are the HONEST false-positive
#                     test: structurally similar code that is not copied.
#
# THE TEMPLATE for the `-i` limb is built from the lines the real files actually share, not from
# an invented header — otherwise the limb would be measuring a fixture again.
#
# Usage: bash build_corpus.sh <bloom_backend_dir> <out_dir>
set -u
src="${1:-}"; out="${2:-}"
[ -d "$src" ] || { echo "p179/KW: REFUSED — '$src' is not a directory" >&2; exit 2; }
[ -n "$out" ] || { echo "p179/KW: REFUSED — no output directory given" >&2; exit 2; }
rm -rf "$out"; mkdir -p "$out/corpus"

cp "$src"/app/*.py "$out/corpus/" 2>/dev/null
cp "$src"/tests/unit/*.py "$src"/tests/integration/*.py "$out/corpus/" 2>/dev/null
rm -f "$out/corpus/__init__.py"
real=$(ls "$out/corpus" | wc -l | tr -d ' ')
[ "$real" -ge 8 ] || { echo "p179/KW: REFUSED — only $real real files; that is not a corpus" >&2; exit 2; }

# ── KNOWN POSITIVE 1: mechanical identifier rename, the transform students actually use ───────
base="$out/corpus/recommendations.py"
[ -f "$base" ] || { echo "p179/KW: REFUSED — recommendations.py absent, no ground truth" >&2; exit 2; }
sed -E \
  -e 's/\brecommendation\b/suggestion/g' -e 's/\brecommendations\b/suggestions/g' \
  -e 's/\bLearningRecommendation\b/StudyHint/g' -e 's/\blesson\b/unit/g' \
  -e 's/\blessons\b/units/g' -e 's/\bcourse\b/subject/g' -e 's/\bcourses\b/subjects/g' \
  -e 's/\bdb\b/sess/g' -e 's/\bresult\b/outcome/g' -e 's/\bitems\b/entries/g' \
  "$base" > "$out/corpus/p_rename.py"

# ── KNOWN POSITIVE 2: the same, with top-level blocks reversed ─────────────────────────────────
python3 -I - "$out/corpus/p_rename.py" "$out/corpus/p_rename_reorder.py" <<'PY'
import sys, re
src, dst = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
# Split at top-level `def`/`class` boundaries and emit the blocks in reverse order.  The imports
# stay on top so the file is still valid Python, which matters: dolos parses it.
parts = re.split(r"(?m)^(?=(?:def |class |@))", text)
head, blocks = parts[0], parts[1:]
open(dst, "w", encoding="utf-8").write(head + "".join(reversed(blocks)))
PY

# ── THE TEMPLATE, built from what the real files SHARE ─────────────────────────────────────────
# Any import or `from` line that appears in at least 3 of the real modules counts as boilerplate
# the course would have handed out.
awk 'FNR==1 {n++} /^(import |from )/ {print}' "$out/corpus"/*.py \
  | sort | uniq -c | awk '$1 >= 3 {$1=""; sub(/^ /,""); print}' > "$out/template.py"
tl=$(wc -l < "$out/template.py" | tr -d ' ')

printf 'p179/KW corpus: %s real files, 2 known positives, template of %s shared lines\n' "$real" "$tl"
printf 'corpus=%s\ntemplate=%s\n' "$out/corpus" "$out/template.py"
