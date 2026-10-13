"""POSITIVE CONTROL - frozen from a real shape in this repository.

Binds a dated path to a variable and then writes it. The gate MUST flag this,
because the commonest real offender never writes the literal inline.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
out = HERE / "score.2026-10-11.tsv"
out.write_text("claim\tscore\n", encoding="utf-8")

phantom = HERE / "phantom-claims.2026-10-11.tsv"
with open(phantom, "w", encoding="utf-8") as handle:
    handle.write("claim\n")
