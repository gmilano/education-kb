"""FABRICATED NEGATIVE CONTROL - the gate MUST stay silent on this file.

It names a dated evidence path three times, in a docstring, in a comment and in
a READ. Citing yesterday's evidence is the correct behaviour, and a gate that
cannot tell a mention from a write would flag every honest instrument in this
repository.

See evidence/score.2026-10-11.tsv for the figure this script re-checks.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

# The anchor is score.2026-10-11.tsv, committed at pass 120.
anchor = HERE / "score.2026-10-11.tsv"
if anchor.exists():
    rows = anchor.read_text(encoding="utf-8").splitlines()
    print("anchor rows\t%d" % len(rows))

# A write to an UNDATED path is also not this gate's business.
(HERE / "summary.tsv").write_text("ok\n", encoding="utf-8")
