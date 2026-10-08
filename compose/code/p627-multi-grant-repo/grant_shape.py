"""P627-P630 — the shape of a repository's grant.

Four properties this pass measured, expressed as invariants rather than as
frozen corpus cardinalities (P399): each holds for any corpus, so none
expires when the next pass adds a row.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    with open(os.path.join(HERE, name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


# ---------------------------------------------------------------- P627
def grants_of(rows, slug):
    """Every 200-status licence payload a slug ships. A repo's grant is a SET."""
    return {r["path"]: r["family"] for r in rows
            if r["slug"] == slug and r["http"] == "200"}


def single_license_sweep(rows, slug):
    """What a sweep that reads only `LICENSE` would report. Under-reports a
    multi-grant repo -- this is the defect P627 names, kept as the control."""
    g = grants_of(rows, slug)
    return g.get("LICENSE")


def obligations_of(rows, slug):
    """Families that impose an attribution obligation beyond the code grant."""
    return {fam for path, fam in grants_of(rows, slug).items()
            if fam.startswith("CC-BY")}


# ---------------------------------------------------------------- P628
def is_open_grant(family):
    """PROPRIETARY is a verdict, not an absence. It must not collapse into
    UNKNOWN: UNKNOWN means 'not read', PROPRIETARY means 'read, and it
    refuses'. Conflating them turns a refusal into a retry."""
    return family not in ("PROPRIETARY", "UNLICENSED", "UNKNOWN", "")


def filename_keyed_classifier(path):
    """The defective classifier P628 refutes: it concludes 'open' from the
    presence of a licence-shaped FILENAME. Kept so the defect stays detectable."""
    base = os.path.basename(path).lower()
    return base.startswith("licen") or base.startswith("copying")


# ---------------------------------------------------------------- P629
def unlicensed(rows, slug):
    """A slug that exists but ships no 200 licence payload. Measured two ways:
    a full tree enumeration AND the six-filename probe (P624)."""
    return grants_of(rows, slug) == {}


# ---------------------------------------------------------------- P630
def decompose(a, b):
    """Byte delta between two MIT payloads, decomposed into its only two
    axes: copyright-line length and the final newline. Extends P621."""
    cp = int(a["cp_len"]) - int(b["cp_len"])
    nl = (1 if a["final_newline"] == "yes" else 0) - \
         (1 if b["final_newline"] == "yes" else 0)
    return cp, nl, cp + nl
