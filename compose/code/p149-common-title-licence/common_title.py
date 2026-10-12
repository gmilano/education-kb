"""p149-common-title-licence -- `ACTION FC`: a licence named in words, not in an SPDX token.

`T72` came out of `Fedena`: 2026 comparison tables call it the only Apache-licensed SIS, and
the repository ships **no licence body of its own**. 🔵 **The general shape behind it** is that
this shelf's matcher recognises `Apache-2.0` and not *"Apache License 2.0"* -- a hyphen and a
token order, where humans write a title.

> 🟡 **`ACTION FC`** -- add the **common-title forms** (`Apache License 2.0`, `MIT License`,
> `GPLv2`, `GPL v3`, `BSD 3-Clause`) that name a licence without the token the current
> patterns require. Re-run over all **57** subjects.
> 🔴 *Refuted if no row changes class* -- which would make `T72` a Fedena-specific artefact
> outside this shelf's population, and the census complete at 8 of 57 strict-unlicensed.

## 🔴 What the published matcher can and cannot read

`p147-licence-language`'s `SPDX` pattern requires the punctuation:

| written as | `SPDX` reads it? | why |
|---|---|---|
| `Apache-2.0` | 🟢 yes | the token |
| **`Apache License 2.0`** | 🔴 **no** | no hyphen; `Apache` alone is not in the pattern |
| `MIT` / **`MIT License`** | 🟢 yes | 🔵 `\bMIT\b` matches inside the title by luck |
| **`GPLv2`**, **`GPL v3`** | 🔴 **no** | the pattern wants `GPL-2.0` |
| **`BSD 3-Clause`** | 🔴 **no** | the pattern wants `BSD-3-Clause`, with the first hyphen |
| **`MPL 2.0`** | 🔴 **no** | wants `MPL-2.0` |

🟢 **So `MIT` was never at risk and the other four were** -- which is why a Fedena-shaped row
can read `UNIDENTIFIED` while its README names a licence in plain words.

    python3 common_title.py <clone-dir>... [--published <tsv>]
    python3 test_common_title.py       # 27 tests, authored fixtures, offline
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, os.pardir, "p147-licence-language"))

import licence_language as ll  # noqa: E402  the published matcher, driven unmodified

# 🆕 Title forms, each mapped to the SPDX id it denotes. 🔵 Ordered: the longer and more
# specific forms are tried first, so *"GNU Affero General Public License v3"* is not read as
# a bare GPL and *"Apache License, Version 2.0"* is not read as *"Apache 2"*.
COMMON_TITLE = [
    (re.compile(r"(?i)\bApache\s+Licen[cs]e,?\s*(?:Version\s*)?2(?:\.0)?\b"), "Apache-2.0"),
    (re.compile(r"(?i)\bApache\s*2(?:\.0)?\s+Licen[cs]e\b"), "Apache-2.0"),
    (re.compile(r"(?i)\bApache[-\s]+2\.0\b"), "Apache-2.0"),
    (re.compile(r"(?i)\bGNU\s+Affero\s+General\s+Public\s+Licen[cs]e(?:\s*v?3(?:\.0)?)?\b"),
     "AGPL-3.0"),
    (re.compile(r"(?i)\bAGPL\s*v?\.?\s*3(?:\.0)?\b"), "AGPL-3.0"),
    (re.compile(r"(?i)\bGNU\s+Lesser\s+General\s+Public\s+Licen[cs]e(?:\s*v?([23])(?:\.[01])?)?\b"),
     "LGPL"),
    (re.compile(r"(?i)\bLGPL\s*v?\.?\s*([23])(?:\.[01])?\b"), "LGPL"),
    (re.compile(r"(?i)\bGNU\s+General\s+Public\s+Licen[cs]e,?\s*(?:Version\s*)?v?([23])(?:\.0)?\b"),
     "GPL"),
    (re.compile(r"(?i)\bGPL\s*v?\.?\s*([23])(?:\.0)?\b"), "GPL"),
    (re.compile(r"(?i)\bMozilla\s+Public\s+Licen[cs]e,?\s*(?:Version\s*)?2(?:\.0)?\b"),
     "MPL-2.0"),
    (re.compile(r"(?i)\bMPL\s*v?\.?\s*2(?:\.0)?\b"), "MPL-2.0"),
    (re.compile(r"(?i)\b([23])[-\s]+Clause\s+BSD\b"), "BSD"),
    (re.compile(r"(?i)\bBSD\s+([23])[-\s]*Clause\b"), "BSD"),
    (re.compile(r"(?i)\bCreative\s+Commons\s+Zero\b|\bCC0\b"), "CC0-1.0"),
    (re.compile(r"(?i)\bThe\s+Unlicen[cs]e\b"), "Unlicense"),
    (re.compile(r"(?i)\bISC\s+Licen[cs]e\b"), "ISC"),
    (re.compile(r"(?i)\bMIT\s+Licen[cs]e\b"), "MIT"),
    (re.compile(r"(?i)\bEducational\s+Community\s+Licen[cs]e(?:,?\s*Version\s*2(?:\.0)?)?\b"),
     "ECL-2.0"),
]


def title_licence(text):
    """The SPDX id a common-title form names, or None.

    🟢 The earliest match in the text wins, so a README whose own licence heading precedes a
    dependency's notice is read on its own heading. 🔵 Ties at the same offset go to the more
    specific pattern, which is why `COMMON_TITLE` is ordered.
    """
    best = None
    for rx, spdx in COMMON_TITLE:
        m = rx.search(text)
        if m and (best is None or m.start() < best[0]):
            best = (m.start(), spdx)
    return best[1] if best else None


def identify_ext(text):
    """`ll.identify`, falling back to a common-title form before giving up."""
    got = ll.identify(text)
    if got != "UNIDENTIFIED":
        return got
    return title_licence(text) or "UNIDENTIFIED"


def payload_root(root):
    """The directory a census should read.

    🔴 `npm pack` extracts its tarball into a single `package/` directory, so pointing a
    census at the extraction directory reads an empty root. 🔴 **The first run of this module
    did exactly that** and reported 7 of the 8 npm rows as `NONE/-` against `p145`'s published
    `PKG_ONLY/MIT` -- 🔵 **a defect in the harness, in the direction of understating the
    shelf's licence coverage**, caught by the reproduction control and not in review.
    🟢 `p147-npm-region`'s published `where` values (`package/README.md`) say the same thing.
    """
    if not os.path.isdir(root):
        return root
    entries = [e for e in os.listdir(root) if not e.startswith(".")]
    if entries == ["package"] and os.path.isdir(os.path.join(root, "package")):
        return os.path.join(root, "package")
    return root


def census_ext(root, subject):
    """`ll.census` under the published README rule, with titles read where SPDX failed.

    🔵 Only the *identification* changes. The grant ladder -- `FILE` > `README_ONLY` >
    `PKG_ONLY` > `NONE` -- is the published one, untouched, so this cannot move a row between
    grant classes for any reason other than a licence becoming identifiable.
    """
    base = ll.census(root, subject, ll.EXTENDED_README, allow_informal=True)
    if base["licence"] != "UNIDENTIFIED":
        return base
    out = dict(base)
    if base["grant"] == "FILE":
        body = ll.read(os.path.join(root, base["evidence"]))
        found = title_licence(body)
    else:
        found = None
        for b in (sorted(os.listdir(root)) if os.path.isdir(root) else []):
            if b.lower().startswith("readme"):
                found = title_licence(ll.read(os.path.join(root, b)))
                if found:
                    break
    if found:
        out["licence"] = found
        out["evidence"] = base["evidence"] + "+title"
    return out


COLS = ["subject", "base_grant", "base_licence", "ext_grant", "ext_licence", "evidence",
        "changed"]


def main(argv):
    roots = [a for a in argv[1:] if not a.startswith("--")]
    if not roots:
        print(__doc__)
        return 2
    rows, changed = [], []
    for root in roots:
        root = root.rstrip("/")
        subj = os.path.basename(root)
        root = payload_root(root)
        b = ll.census(root, subj, ll.EXTENDED_README, allow_informal=True)
        e = census_ext(root, subj)
        diff = (b["grant"], b["licence"]) != (e["grant"], e["licence"])
        if diff:
            changed.append((subj, b, e))
        rows.append(dict(subject=subj, base_grant=b["grant"], base_licence=b["licence"],
                         ext_grant=e["grant"], ext_licence=e["licence"],
                         evidence=e["evidence"], changed="CHANGED" if diff else "-"))
    def tally(key):
        out = {}
        for r in rows:
            out[r[key]] = out.get(r[key], 0) + 1
        return out
    print("# population: %d" % len(rows))
    print("# base grants: %s" % sorted(tally("base_grant").items()))
    print("# ext  grants: %s" % sorted(tally("ext_grant").items()))
    base_unid = sum(1 for r in rows if r["base_licence"] == "UNIDENTIFIED")
    ext_unid = sum(1 for r in rows if r["ext_licence"] == "UNIDENTIFIED")
    print("# UNIDENTIFIED: base %d -> ext %d" % (base_unid, ext_unid))
    for s, b, e in changed:
        print("#   CHANGED %-46s %s/%s -> %s/%s"
              % (s, b["grant"], b["licence"], e["grant"], e["licence"]))
    print("#")
    print("# ACTION FC falsifier -- rows changing class: %d -> %s"
          % (len(changed), "NOT REFUTED" if changed else "REFUTED"))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
