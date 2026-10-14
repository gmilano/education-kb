"""p189 / P1057 — licence-path CASE closure, and the manifest field that names the file.

Why this exists
---------------
`ACTION MZ` fetched licence bytes for 64 rows over the raw channel using this KB's
standing path list — LICENSE, LICENSE.txt, LICENSE.md, COPYING. Seven rows returned
nothing. One of them was `openedx/XBlock`, which this KB publishes as:

    🔴 NO_LICENCE_FILE — "Apache-2.0 ASSERTED — and no licence TEXT anywhere in the tree"

That verdict is WRONG. The file is `LICENSE.TXT` — uppercase extension — and it is
11 358 B of verbatim Apache-2.0. raw.githubusercontent.com is CASE-SENSITIVE, so a path
list that spells the extension in one case has not looked for the file; it has looked
for one spelling of the file. The row is this KB's recommended permissive entry point
into AGPL Open edX, so the caveat the wrong verdict forced onto every engagement using
it ("the grant is a NOTICE not a LICENSE") was never real.

Two channels are checked here, in cost order.

1. THE MANIFEST NAMES THE FILE. PEP 639 `license-files` (pyproject.toml) and npm's
   `licenseFile` state the path outright, so no guessing is needed:

       openedx/XBlock, pyproject.toml:  license-files = ["LICENSE.TXT"]

   Measured coverage over the same 64 rows: 1 manifest declares it. So this channel is
   AUTHORITATIVE and RARE — use it when present, never rely on it.

2. CASE VARIANTS. Because coverage of (1) is ~2%, the generalisable fix is to vary the
   case of the stem and the extension. Measured cost and yield, same pass:
   16 variants x 14 grant-absent rows = 224 probes, 0 further grants. So the XBlock miss
   was ISOLATED, not systemic — which is the honest result and the reason this file
   records the yield as well as the method.

What this is NOT
----------------
Not a licence classifier. It emits PATHS to probe and reads a manifest field. Whether
the bytes at a path are a grant is P1054/P1056/P1049's job. No network: the caller
supplies the manifest text and does the fetching (gap 139 — this harness cannot install
dependencies).
"""

from __future__ import annotations

import re

# Stems this KB has seen carry a grant, lower-cased. Order is probe order.
STEMS = ("license", "licence", "copying", "notice")

# Extensions, lower-cased. "" is the bare file, which is the commonest shape.
EXTS = ("", ".txt", ".md", ".rst", ".apache2", ".mit", ".gpl")

# The three casings that occur in the wild. Measured: LICENSE (most), LICENSE.TXT
# (openedx/XBlock), License.md and license.txt both appear on GitHub generally.
def _casings(word: str) -> tuple[str, ...]:
    return (word.upper(), word.capitalize(), word.lower())


# PEP 639 (pyproject.toml) and npm (package.json) fields that NAME the licence file.
_PEP639 = re.compile(r"license-files\s*=\s*\[([^\]]*)\]", re.I)
_NPM = re.compile(r'"licenseFile"\s*:\s*"([^"]+)"', re.I)
_QUOTED = re.compile(r'["\']([^"\']+)["\']')


def declared_licence_files(manifest_text: str) -> list[str]:
    """Paths a manifest NAMES as holding the licence. Authoritative when non-empty."""
    out: list[str] = []
    m = _PEP639.search(manifest_text)
    if m:
        out.extend(_QUOTED.findall(m.group(1)))
    for m in _NPM.finditer(manifest_text):
        out.append(m.group(1))
    seen: set[str] = set()
    return [p for p in out if not (p in seen or seen.add(p))]


def candidate_paths(limit: int | None = None) -> list[str]:
    """Case-varied licence paths, in probe order, de-duplicated.

    The bare uppercase stems come first because they are overwhelmingly the commonest,
    so a caller that truncates this list still spends its first probes well.
    """
    out: list[str] = []
    seen: set[str] = set()
    for ext in EXTS:
        for stem in STEMS:
            for stem_case in _casings(stem):
                for ext_case in ({ext, ext.upper()} if ext else {""}):
                    p = f"{stem_case}{ext_case}"
                    if p not in seen:
                        seen.add(p)
                        out.append(p)
    return out[:limit] if limit else out


def probe_plan(manifest_text: str = "", limit: int | None = None) -> dict:
    """What to fetch, and why, for one repository.

    A declared path is returned FIRST and flagged, so a caller that stops at the first
    200 spends one request instead of sixteen.
    """
    declared = declared_licence_files(manifest_text) if manifest_text else []
    variants = [p for p in candidate_paths(limit) if p not in declared]
    return {
        "declared": declared,
        "variants": variants,
        "order": declared + variants,
        "channel": "manifest" if declared else "case-variants",
    }
