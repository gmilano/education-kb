#!/usr/bin/env python3
"""p882 — `881-G3`: a shelf table's structural key is its COLUMN SET, not its header STRING.

## The defect this closes

`ingest/derive-counts.py` located a shelf table by testing its header row for membership of a
list of **exact literal strings** (`if header in sigset`). Several of those literals embed a
date:

    | Repo | Licence (byte-read `2026-11-16`) | ★ | Pushed | Region | Why it is here |

so the gate reddened on a *correct* shelf the next time any shelf re-dated a header — which is
a check on presentation wearing the costume of a structural check. `881-G3` measured the
consequence: *"none of the 21 declared column-header signatures was found; no table can be
located"* on `agents/top.md`, `repos/foundations.md` and `verticals/solutions.md`, three
shelves that all plainly contain tables.

🔴 **And it is a defect CLASS, not an instance.** The literal list was widened by `p543`,
`p568`, `p718`, `p811`, `p813`, `p853`, `p858`, `p865`, `p866`, `p867`, `p869` and `p870` —
twelve passes, each adding the one spelling its own rewrite had just invented. `p811`'s note
records the same thing from the other side: the declared literals were *"wrong on their face
('Licence' where both files write 'License')"*. A list of literals cannot stop being wrong,
because the thing it pins is the thing the shelves are free to reword.

## The key

🟢 Three reductions, each one a presentation variance this base has actually been bitten by:

1. **Dates, pass-ids, backticks and emphasis are stripped.** `` Licence (byte-read `2026-11-16`) ``
   and `Licence (byte-read)` are the same column. This is `881-G3`'s explicit demand, and its
   acceptance test — *"a fixture pair that differs only in the embedded date must grade
   identically"* — is `test_header_sig.py`'s `C1`/`C2`.
2. **`licence`/`license` are folded**, with case and punctuation. `p811` recorded this exact
   spelling split as a cause of RED.
3. **The final column is dropped, and the rest compared AS A SET.** The last column of every
   shelf table on this base is free prose — *"Why it is a foundation"*, *"Role in an
   engagement"*, *"What it actually does, and the posture"* — and it is where essentially all
   of the declared literals differ from each other. The leading columns are the contract; the
   last one is the sentence. Order is not meaning for a column set, so a shelf that moves
   `★` ahead of `Pushed` is the same table.

🔴 **What is deliberately NOT folded:** `Licence, as measured` / `Licence (byte-read)` /
`Licence, re-read` stay distinct from one another, because they name different *provenance*
for the cell and this base grades provenance. Only presentation is normalised. A normaliser
that collapsed those would make the gate agree with anything.

🔵 **Why this cannot go blind the way its twelve predecessors did:** a header whose column set
is not declared is still an UNCOUNTED-TABLE RED naming the line (`p813`'s ratchet, kept). The
fix removes the *date* tripwire, not the requirement to declare a new shape.
"""
import re

__all__ = ["norm_cell", "sig_key", "has_date", "SIG_DOC"]

SIG_DOC = "normalised column set (dates/ids/backticks/emphasis stripped, final prose column dropped)"

# ISO dates (`2026-11-16`), the shape that is actually embedded in this base's headers.
_DATE = re.compile(r"\b(?:19|20)\d{2}-\d{2}-\d{2}\b")
# Pass ids — `p879`, `p878`. A header that names the pass that wrote it is dated by another
# means, and `agents/top.md` publishes `| Repo | ★ `p879` | `p878` | Δ | ... |`.
_PASSID = re.compile(r"\bp\d{2,4}\b")
# Everything kept: letters, digits, the star, the middot and the slash this base's
# compound columns use (`★ / forks`, `Default ref · pushed`) and the HYPHEN. The hyphen
# is kept deliberately: dates are already gone by this point, and `byte-read` / `re-read`
# are the provenance distinction this normaliser must NOT erase (see `C9`).
# A markdown separator row (`|---|---:|`). 🔴 Found by this module's own suite (`C12`) the
# moment the hyphen was added to `_KEEP`: without this, `|---|---|` normalises to the
# non-empty key `{"---"}` and a separator row becomes keyable. `_tables()` never hands one to
# `sig_key`, so it was a latent defect in the FUNCTION rather than a live one in the gate --
# which is the only reason the control exists.
_SEP_CELL = re.compile(r"^[\s:-]*$")

_KEEP = re.compile(r"[^a-z0-9/·★ -]")
_WS = re.compile(r"\s+")


def has_date(text):
    """True if an ISO date or a pass-id survives in `text`.

    🔴 `881-G3`: *"If the fix leaves any date inside a signature, it is not fixed."* This is
    that clause as a callable, so the suite can assert it over every declared signature
    rather than over a sample.
    """
    return bool(_DATE.search(text) or _PASSID.search(text))


def norm_cell(cell):
    """One column header -> its comparable form."""
    c = cell.replace("`", "").replace("*", "").replace("_", " ")
    c = _DATE.sub(" ", c)
    c = _PASSID.sub(" ", c.lower())
    # 🟢 p811's spelling split: these shelves write both. Fold to one BEFORE the keep-filter,
    # so the fold is on the word and not on whatever punctuation surrounds it.
    c = re.sub(r"\blicence\b", "license", c)
    c = _KEEP.sub(" ", c)
    return _WS.sub(" ", c).strip()


def sig_key(header):
    """A header row -> frozenset of its normalised LEADING column names.

    Returns an empty frozenset for anything that is not a table header with at least two
    columns, so a caller can treat falsity as "not a keyable header" without a second test.
    """
    if not header or not header.strip().startswith("|"):
        return frozenset()
    cells = header.strip().strip("|").split("|")
    if len(cells) < 2:
        return frozenset()
    if all(_SEP_CELL.match(c) for c in cells):
        return frozenset()
    lead = [norm_cell(c) for c in cells[:-1]]
    return frozenset(c for c in lead if c)
