"""AMBIGUOUS CONTROL - a literal dated write in a script that ALSO calls the
clock. The gate must see the write and classify it `clock`, not `hardcoded`:
the clock call may or may not reach this path, and over-reporting an offender
is the one error this gate must not make, because its output drives a repair.
"""

from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent

print("run at", date.today().isoformat())

out = HERE / "census-items.2026-10-05.tsv"
out.write_text("item\n", encoding="utf-8")
