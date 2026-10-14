#!/usr/bin/env python3
"""p191 — extract the rows this KB publishes WITH a licence, from the pages themselves.

Why this exists
---------------
`ACTION NK` asks for the FULL `P1057` sweep over *all* published licence rows. p190 ran
`156` variants over only the `17` grant-absent ones and `limit=16` over the rest — and
`limit=16` cannot reach `.md` (`Gap 434`). To sweep at full depth the sweep first needs the
POPULATION, and the population lives in the published pages, not in a side file.

The contract
------------
A row is `(slug, published_id)` where the slug is a `github.com/<owner>/<repo>` address and
the id is an SPDX-shaped token found in the SAME markdown table row. 🔴 Deliberately NOT a
licence classifier and NOT a prose reader: a licence named in a sentence is not a published
row, because this KB's own pages distinguish the two and `Gap 442` was a prose reader
promoted by accident.

Owner/repo are kept in the case the page spells them. `raw.githubusercontent.com` treats the
OWNER segment as case-insensitive (p190) but the PATH as case-sensitive, which is the whole
reason this sweep exists.
"""
from __future__ import annotations

import re

PAGES = (
    "README.md",
    "agents/top.md",
    "agents/trending.md",
    "repos/foundations.md",
    "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md",
    "intel/trends.md",
    "compose/patterns.md",
)

SLUG = re.compile(r"github\.com/([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)/([A-Za-z0-9][A-Za-z0-9._-]*?)(?=[)\s`,;]|/|$)")

# SPDX-shaped ids this KB publishes. 🔴 **This tuple is the single source of truth for the
# vocabulary, and it exists in this shape because the first build did not have one.** It
# lacked `ECL-2.0` — the Educational Community License, which is the licence of
# `sakaiproject/sakai` AND `opencast/opencast`, two of the largest platforms on this shelf.
# Both rows publish `ECL-2.0` correctly and both EXPLAIN it in the same cell *("OSI-approved
# `Apache-2.0` derivative for universities")*, so the extractor could not see the id the row
# published and did see the id the row merely NAMED. 🔴 Two platform rows were reported as
# contradicted, and the KB was right on both.
# 🟢 `column_full_depth` asserts at import that its family map covers every id here, so the
# two vocabularies cannot drift apart again silently.
IDS = (
    "AGPL-3.0-only", "AGPL-3.0", "GPL-3.0-only", "GPL-3.0", "GPL-2.0",
    "LGPL-3.0", "LGPL-2.1",
    "Apache-2.0", "MIT", "BSD-3-Clause", "BSD-2-Clause", "MPL-2.0",
    "EPL-2.0", "EPL-1.0", "ISC", "Unlicense",
    "CC0-1.0", "CC-BY-NC-SA-4.0", "CC-BY-SA-4.0", "CC-BY-NC-4.0", "CC-BY-4.0",
    # Education's own licences, and the ones this shelf actually meets in EMEA and APAC.
    "ECL-2.0", "EUPL-1.2", "EUPL-1.1", "MulanPSL-2.0",
)
ID_RX = re.compile("|".join(re.escape(i) for i in sorted(IDS, key=len, reverse=True)))

_TRAIL = re.compile(r"\.git$|[.,;:]$")


def clean_repo(repo: str) -> str:
    return _TRAIL.sub("", repo)


def row_pairs(line: str) -> list[tuple[str, str]]:
    """(slug, id) pairs for ONE line. Empty when the line has no slug or no id."""
    ids = ID_RX.findall(line)
    if not ids:
        return []
    out: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for owner, repo in SLUG.findall(line):
        slug = f"{owner}/{clean_repo(repo)}"
        for lic in ids:
            if (slug, lic) not in seen:
                seen.add((slug, lic))
                out.append((slug, lic))
    return out


def collect(texts: dict[str, str]) -> dict[str, dict]:
    """slug -> {"ids", "pages", "confident"}. Table rows only.

    🔴 **`confident` exists because the first build of this module manufactured three
    false accusations in six.** A published table row may name SEVERAL repositories and
    SEVERAL licences — `verticals/solutions.md`'s Q-Acadêmico row names four repos and two
    ids — and pairing them as a cross-product attributed `Apache-2.0` to
    `AlexandreL0pes/q-scraper`, whose own grant is MIT. Read, the row never said that.

    🟢 So an id is attributed to a slug only from a line carrying EXACTLY ONE slug. A slug
    seen only on multi-slug lines keeps its ids and is marked `confident=False`, and the
    comparison downstream must report it `PAIRING-AMBIGUOUS` rather than contradicted.
    🔵 This is `P1058`'s rule — *a cheap proxy for a precise thing must be tested against
    the case that distinguishes them* — applied to the POPULATION rather than to a path.
    """
    acc: dict[str, dict] = {}
    for page, text in texts.items():
        for line in text.splitlines():
            if not line.lstrip().startswith("|"):
                continue
            pairs = row_pairs(line)
            if not pairs:
                continue
            n_slugs = len({s for s, _ in pairs})
            for slug, lic in pairs:
                e = acc.setdefault(slug, {"ids": set(), "pages": set(),
                                          "sole": set()})
                e["pages"].add(page)
                if n_slugs == 1:
                    e["sole"].add(lic)
                else:
                    e["ids"].add(lic)
    out: dict[str, dict] = {}
    for slug, v in sorted(acc.items(), key=lambda kv: kv[0].lower()):
        confident = bool(v["sole"])
        out[slug] = {
            "ids": sorted(v["sole"]) if confident else sorted(v["ids"]),
            "pages": sorted(v["pages"]),
            "confident": confident,
        }
    return out


def read_pages(root: str) -> dict[str, str]:
    import os

    out: dict[str, str] = {}
    for p in PAGES:
        fp = os.path.join(root, p)
        if os.path.exists(fp):
            with open(fp, encoding="utf-8") as fh:
                out[p] = fh.read()
    return out


if __name__ == "__main__":
    import os
    import sys

    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    rows = collect(read_pages(root))
    for slug, v in rows.items():
        print(f"{slug}\t{','.join(v['ids'])}\t"
              f"{'SOLE' if v['confident'] else 'MULTI'}\t{len(v['pages'])}")
    print(f"# {len(rows)} rows", file=sys.stderr)
