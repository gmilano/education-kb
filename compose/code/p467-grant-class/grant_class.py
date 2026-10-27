#!/usr/bin/env python3
"""p467 -- the GRANT-CLASS axis, closing `Gap 466-A` and `Gap 466-C` with one
reader.

`Gap 466-A` (from `p466`): three carried rows serve a root licence payload and
would pass any "has-a-LICENSE" screen -- `CC-BY-SA-4.0` (content copyleft, not a
software licence), `Elastic-2.0` (source-available, forbids hosted delivery) and
`CC-BY-NC-4.0` (NonCommercial, barred from every paid engagement). Its
prescribed closure: a `grant_class` axis read from the payload's FIRST NON-BLANK
LINE, with an explicit `UNSELLABLE` value for `*-NC`, `Elastic-*`, `BUSL-*` and
`SSPL`, required on every sell-shelf row before publication.

`Gap 466-C`: payload SIZE was used on these shelves as if it screened licence
family and it does not (AGPL-3.0 shows 7 live byte values spanning 1 116 B).
Its prescribed closure: replace the size screen with a first-non-blank-line
match against the SPDX title strings, keeping size and digest as PROVENANCE
ONLY.

Both prescriptions name the same anchor, so they are one instrument.

### The prescription is UNDER-SPECIFIED, and this file records where

A strictly one-line reader CANNOT grade Apache-2.0's version: the payload's
first non-blank line is "Apache License" and the version lives on the SECOND
non-blank line ("Version 2.0, January 2004"). Measured first-hand on
`HKUDS/DeepTutor` (11 408 B, sha256-12 cd2f54e1e506). Same shape for the GNU
family, whose version sits on its own line under the title.

So the axis is read in two layers, and which layer fired is RECORDED per row:

  * `family`      -- from the first non-blank line alone (the gap's anchor).
  * `version`     -- from the first 4 non-blank lines (the title BLOCK), which
                     is `p454`'s anchor and the only region a preamble cannot
                     reach.

A row whose family needs more than the first line is published `line1=0`, never
silently promoted. This is a deviation from the gap's literal text and is
declared rather than hidden.

### What is NOT delegated to size

Nothing. `bytes` and `sha256_12` are carried as provenance so a later pass can
prove it read the same payload, and no verdict in this file branches on either.
That is the whole of `Gap 466-C`'s closure.

### The UNSELLABLE class, and why it is not "non-OSI"

`UNSELLABLE` is a DELIVERY verdict, not a licence-approval verdict: it marks a
grant under which Globant cannot ship a paid client engagement. NonCommercial
bars payment outright; `Elastic-2.0`, `BUSL-1.1` and `SSPL` bar providing the
software to third parties as a hosted or managed service, which is the delivery
model for every platform tier on these shelves. A bespoke payload that refuses
permission lands here too, by title.

### v2 -- six defects, all found by READING the payloads this instrument graded

The first run of this file over the 103-address population published six wrong
verdicts. Every one was caught by reading the payload behind the verdict, never
by the verdict itself, and every one is recorded here rather than quietly fixed:

1. 🔴 **The MIT grant SENTENCE is not an MIT grant.** `CaviraOSS/PageLM`
   (2 049 ★) serves "PageLM Community License" (8 563 B, `c834209c5f33`) whose
   FIRST grant sentence is MIT's verbatim -- "Permission is hereby granted, free
   of charge, to any person obtaining a copy..." -- and then restricts that same
   sentence to "personal, educational, or non-commercial research purposes",
   prohibits redistribution outright, and requires a REVENUE-SHARING agreement
   before any commercial use, "in whole or in part". v1 graded it `MIT /
   PERMISSIVE` off the body form. So does this base's own `family_title.py`,
   whose `PERMISSIVE_GRANT` arm suppresses its bespoke check for exactly this
   reason. 🔵 This base had already measured the payload correctly at `pass255`
   /`pass257` and a later pass regressed it to `MIT`; the digest read first-hand
   this pass is byte-identical to that record. `Gap 466-A` said a present grant
   is not a permissive grant; this class says a permissive grant FORM is not a
   permissive grant. Remedy: a RESTRICTION OVERRIDE that runs after the body
   layer and outranks it.
2. 🔴 **A cross-repo pointer graded `UNSELLABLE`.** `codeforlife-education/aimmo`
   (117 ★) serves a 115 B `LICENSE.md` reading "Find our license
   [here](.../ocadotechnology/codeforlife-workspace/blob/main/LICENSE.md)". v1
   read a bespoke title ("# License") with no grant and condemned it. p454's
   reader has a pointer rule but it resolves IN-REPO paths only, and this target
   is ANOTHER REPOSITORY. Followed first-hand: AGPL-3.0, 32 920 B,
   `420e5ccb5e59`. Remedy: `POINTER_CROSS_REPO`, resolved, never condemned.
3. 🔴 **CERN-OHL graded `UNSELLABLE`.** `Wakoma/nimble` (110 ★) serves "CERN Open
   Hardware Licence Version 2 - Strongly Reciprocal" (13 419 B, `d6475a84171f`).
   It is a reciprocal FREE licence, not a refusal -- commercial use is permitted
   under reciprocity. Remedy: explicit CERN-OHL-P/W/S titles.
4. 🔴 **A bare Creative Commons title read `UNSTATED`.** `scollovati/awesome-lti`
   serves a payload whose first non-blank line is "Attribution-ShareAlike 4.0
   International" with the words "Creative Commons" NOWHERE on it. Two live
   title forms for one family; v1 knew one. Remedy: both forms.
5. 🟡 **`CC-BY-NC-ND` collapsed to `CC-BY-NC`.** `dvbs2000/visible-ai` is
   NonCommercial AND NoDerivatives, declared bilingually. Same class, wrong
   family -- and ND bars the adaptation an engagement would perform.
6. 🟢 **A per-asset grant surface has no verdict at all.**
   `learning-commons-org/knowledge-graph` (164 ★) states code MIT and datasets
   "not all licensed the same way", labelled Open / Open+Gated / Gated, with
   "**Open + Gated** and **Gated** content NOT covered by CC BY 4.0, CC0, or any
   other open license". Its sibling `evaluators` (87 ★) is MIT code + CC BY 4.0
   content + a CC BY-NC-SA 4.0 corpus inside one payload. The grant is a property
   of each ASSET, not of the repository. Remedy: `COMPOSITE_PER_ASSET`, which is
   never sellable on its own -- it means "clear per asset before use".

`CONTENT_NOT_SOFTWARE` is deliberately separate and is NOT unsellable: CC-BY and
ODbL content can ship with attribution, and CC-BY-SA ships with a propagating
ShareAlike obligation. Collapsing it into `UNSELLABLE` would have condemned the
914-star teacher-skills library that `p466` correctly graded as usable-as-content
-- a false negative in the direction that costs real supply.
"""
import re

# SPDX title strings, matched against the FIRST NON-BLANK LINE. Order matters:
# AGPL before GPL ("Affero General Public" contains "General Public"), and the
# NonCommercial CC variants before plain CC-BY.
TITLE_RULES = [
    # (family, grant_class, first-non-blank-line pattern)
    # Defect 4: TWO live title forms per CC family -- with and without the
    # words "Creative Commons". `(?:creative commons )?` carries both.
    # Order: the clause-bearing variants before the plainer ones.
    ("CC-BY-NC-ND",   "UNSELLABLE",           r"^#*\s*(?:creative commons )?attribution[- ]non[- ]?commercial[- ]no ?deriv"),
    ("CC-BY-NC-SA",   "UNSELLABLE",           r"^#*\s*(?:creative commons )?attribution[- ]non[- ]?commercial[- ]sharealike"),
    ("CC-BY-NC",      "UNSELLABLE",           r"^#*\s*(?:creative commons )?attribution[- ]non[- ]?commercial"),
    ("CC-BY-SA",      "CONTENT_NOT_SOFTWARE", r"^#*\s*(?:creative commons )?attribution[- ]sharealike"),
    ("CC-BY-ND",      "CONTENT_NOT_SOFTWARE", r"^#*\s*(?:creative commons )?attribution[- ]no ?deriv"),
    ("CC-BY",         "CONTENT_NOT_SOFTWARE", r"^#*\s*(?:creative commons )?attribution(?![- ]non)[- ]?[0-9]?"),
    # Defect 3: CERN-OHL is a FREE reciprocal hardware licence, not a refusal.
    ("CERN-OHL-P",    "PERMISSIVE",           r"cern open hardware licence.*permissive"),
    ("CERN-OHL-W",    "WEAK_COPYLEFT",        r"cern open hardware licence.*weakly reciprocal"),
    ("CERN-OHL-S",    "STRONG_COPYLEFT",      r"cern open hardware licence.*strongly reciprocal"),
    ("CERN-OHL",      "WEAK_COPYLEFT",        r"cern open hardware licence"),
    ("CC0-1.0",       "PUBLIC_DOMAIN",        r"creative commons (legal code|cc0)|cc0 1\.0 universal"),
    ("ODbL",          "CONTENT_NOT_SOFTWARE", r"open data commons|odc[- ]by|\bodbl\b"),
    ("Elastic-2.0",   "UNSELLABLE",           r"elastic license"),
    ("BUSL-1.1",      "UNSELLABLE",           r"business source license"),
    ("SSPL",          "UNSELLABLE",           r"server side public license"),
    ("PolyForm-NC",   "UNSELLABLE",           r"polyform noncommercial"),
    ("CommonsClause", "UNSELLABLE",           r"commons clause"),
    ("AGPL-3.0",      "NETWORK_COPYLEFT",     r"gnu affero general public license"),
    ("LGPL",          "WEAK_COPYLEFT",        r"gnu lesser general public license"),
    ("GPL",           "STRONG_COPYLEFT",      r"gnu general public license"),
    ("MPL-2.0",       "WEAK_COPYLEFT",        r"mozilla public license"),
    ("EPL",           "WEAK_COPYLEFT",        r"eclipse public license"),
    ("EUPL",          "WEAK_COPYLEFT",        r"european union public licence"),
    ("MIT",           "PERMISSIVE",           r"^#*\s*(the )?mit licen[cs]e\b"),
    ("Apache-2.0",    "PERMISSIVE",           r"^#*\s*apache licen[cs]e"),
    ("ISC",           "PERMISSIVE",           r"^#*\s*isc licen[cs]e"),
    ("BSD",           "PERMISSIVE",           r"^#*\s*bsd[ -][23][- ]clause"),
    ("Unlicense",     "PUBLIC_DOMAIN",        r"^#*\s*(this is free and unencumbered|the unlicense)"),
    ("WTFPL",         "PERMISSIVE",           r"do what the fuck you want to public license"),
    ("Zlib",          "PERMISSIVE",           r"^#*\s*zlib licen[cs]e"),
]

# BODY grant forms, used ONLY when the first non-blank line names no family.
# These are the payloads that open on a bare copyright line, which is the
# commonest MIT shape in the wild. `line1` is recorded 0 for every one of them.
BODY_RULES = [
    ("MIT",          "PERMISSIVE",  r"permission is hereby granted, free of charge"),
    ("BSD",          "PERMISSIVE",  r"redistribution and use in source and binary forms"),
    ("ISC",          "PERMISSIVE",  r"permission to use, copy, modify, and/or distribute"),
    ("Apache-2.0",   "PERMISSIVE",  r"licensed under the apache license, version 2\.0"),
    ("AGPL-3.0",     "NETWORK_COPYLEFT",  r"gnu affero general public license"),
    ("LGPL",         "WEAK_COPYLEFT",     r"gnu lesser general public license"),
    ("GPL",          "STRONG_COPYLEFT",   r"gnu general public license"),
    ("CC-BY-NC",     "UNSELLABLE",        r"attribution[- ]non[- ]?commercial"),
    ("Unlicense",    "PUBLIC_DOMAIN",     r"free and unencumbered software released into the public domain"),
]

# A payload whose title calls itself a licence/terms/policy but matches no SPDX
# title and affirms no grant is a bespoke instrument BY CONSTRUCTION. p454
# established that a refusal vocabulary cannot be enumerated, so this is a
# title test, not a refusal test.
BESPOKE_TITLE = re.compile(r"licen[cs]e|policy|terms|agreement|copyright", re.I)
ANY_GRANT = re.compile(
    r"permission is hereby granted|redistribution and use|permission to use|"
    r"apache licen[cs]e|general public licen[cs]e|mozilla public licen[cs]e|"
    r"creative commons|public domain|eclipse public licen[cs]e|is licensed under",
    re.I)
REFUSES = re.compile(
    r"not open source|source available|no permission is granted|all rights reserved\.?\s*$|"
    r"non[- ]?commercial|not free to reuse|viewing and reference purposes only", re.I)

# Defect 1 -- THE RESTRICTION OVERRIDE. A scope restriction inside the grant
# itself, which the MIT/BSD body forms cannot carry and a bespoke licence
# reciting them does. This runs AFTER the body layer and OUTRANKS it, because
# the body layer's whole job is to recognise a grant form, and a grant form is
# exactly what this class wears.
RESTRICTION = re.compile(
    r"non[- ]?commercial (?:research |use|purposes)|"
    r"for (?:personal|educational)[^.]{0,60}non[- ]?commercial|"
    r"revenue[- ]shar(?:e|ing)|"
    r"redistribution of the software[^.]{0,80}(?:is )?(?:strictly )?prohibited|"
    r"may not be (?:sold|sublicensed)|"
    r"not be used for commercial|requires? a (?:separate )?commercial licen[cs]e",
    re.I)
# A title that is NOT an SPDX family name. Any payload whose own title names a
# product or organisation is bespoke, whatever grant form it recites.
SPDX_TITLE_ANY = re.compile(
    r"^#*\s*(?:the )?(?:mit|isc|zlib|apache|bsd|mozilla|gnu|eclipse|european union|"
    r"creative commons|attribution|cc0|unlicense|elastic|business source|"
    r"server side|polyform|commons clause|cern open hardware|do what the)", re.I)

# Defect 2 -- a pointer, in-repo OR cross-repo. A pointer is the ABSENCE of a
# grant at this path, never the refusal of one.
POINTER_MAX_BYTES = 600
POINTER_IN_REPO = re.compile(
    r"(?:licen[cs]e|terms)[^\n]{0,80}?(?:in|at|under|see)\s*\[?`?"
    r"([A-Za-z0-9._/-]+\.(?:md|txt|rst|html))`?", re.I)
POINTER_CROSS_REPO = re.compile(
    r"https?://(?:github|gitlab)\.com/([A-Za-z0-9._-]+/[A-Za-z0-9._-]+)/"
    r"(?:blob|raw|-/blob)/([A-Za-z0-9._/-]+)", re.I)

# Defect 6 -- a per-asset grant surface: one payload, different grants for code
# and for each data asset, some of them gated or NonCommercial.
PER_ASSET = re.compile(
    r"not all licensed the same way|each dataset[^.]{0,60}(?:labeled|labelled)|"
    r"(?:code|software) is licensed under[^.]{0,80}\n[^\n]{0,200}"
    r"(?:data|content|corpus)[^.]{0,80}(?:licensed|provided)|"
    r"are not covered by cc ?by|per[- ]dataset licen",
    re.I)
# The second per-asset shape, and the more dangerous one: a single payload that
# names a permissive grant for the CODE and a different grant for a bundled
# CONTENT or CORPUS asset. `learning-commons-org/evaluators` is MIT code + CC BY
# 4.0 content + an "Annotated CLEAR Corpus" under CC BY-NC-SA 4.0 -- so a repo
# that reads MIT ships a NonCommercial corpus. The NC sub-asset is recorded,
# because it is the half that bars a paid engagement.
ASSET_SCOPE = re.compile(
    r"\b(code|software|library)\b[^.\n]{0,40}licensed under[^.\n]{0,60}"
    r"\b(mit|apache|bsd|isc)\b", re.I)
ASSET_CONTENT = re.compile(
    r"\b(content|corpus|dataset|data|annotations?)\b[^.\n]{0,60}"
    r"(?:licensed under|provided (?:by[^.\n]{0,40})?under|is under)[^.\n]{0,60}"
    r"(cc[ -]?by[a-z0-9.\- ]*|creative commons[a-z0-9.\- ]*)", re.I)
NC_TOKEN = re.compile(r"non[- ]?commercial|\bnc\b[- ]?(?:sa|nd)?\b", re.I)


def pointer(text):
    """-> ('IN_REPO'|'CROSS_REPO', target) or (None, '') for a short payload
    whose whole content says the licence lives elsewhere."""
    if text is None or len(text.encode()) > POINTER_MAX_BYTES:
        return None, ""
    m = POINTER_CROSS_REPO.search(text)
    if m:
        return "CROSS_REPO", f"{m.group(1)}@{m.group(2)}"
    m = POINTER_IN_REPO.search(text)
    if m:
        return "IN_REPO", m.group(1).lstrip("./")
    return None, ""


VERSION_RE = re.compile(r"\bversion\s+([0-9]+(?:\.[0-9]+)?)|\bv([0-9]+\.[0-9]+)\b", re.I)
GNU_VER_RE = re.compile(r"version\s+([123](?:\.[0-9])?)", re.I)
# The or-later election, which lives outside the title block (p455).
OR_LATER_RE = re.compile(r"either version [123].{0,80}?any later version", re.I | re.S)


def nonblank(text, n):
    return [l.strip() for l in text.splitlines() if l.strip()][:n]


def first_line(text):
    nb = nonblank(text, 1)
    return nb[0] if nb else ""


def title_block(text, n=4):
    return "\n".join(nonblank(text, n))


def grade(text):
    """-> dict(family, grant_class, version, line1, basis)

    `line1` is 1 when the family came from the first non-blank line alone --
    the anchor `Gap 466-A` prescribes -- and 0 when a later layer was needed.
    No field is derived from payload size.
    """
    if text is None:
        return dict(family="NO-ROOT-GRANT", grant_class="NO_GRANT",
                    version="", line1=0, basis="no payload at any root path")

    l1 = first_line(text)
    l1l = l1.lower()
    block = title_block(text)
    body = "\n".join(nonblank(text, 60))

    # (0) A pointer is the absence of a grant HERE, not a refusal. Checked
    #     before everything: a 115 B pointer has no licence text to grade.
    kind, tgt = pointer(text)
    if kind and not re.search(r"permission is hereby granted|redistribution and use", body, re.I):
        return dict(family=f"POINTER_{kind} ({tgt})", grant_class=f"POINTER_{kind}",
                    version="", line1=0, basis="short payload names the grant elsewhere")

    # (0b) A per-asset grant surface: the repository is not the unit of grant.
    if PER_ASSET.search(body):
        return dict(family="COMPOSITE_PER_ASSET", grant_class="COMPOSITE_PER_ASSET",
                    version="", line1=0,
                    basis="payload grants code and each data asset separately")
    mcode = ASSET_SCOPE.search(body)
    content_clauses = ASSET_CONTENT.findall(body)
    mcontent = ASSET_CONTENT.search(body)
    if mcode and mcontent:
        # EVERY content clause is checked, not the first: `evaluators` grants CC
        # BY 4.0 to its content two sentences before it grants CC BY-NC-SA 4.0
        # to its bundled corpus, and the NC half is the one that bars payment.
        nc = any(NC_TOKEN.search(" ".join(t)) for t in content_clauses)
        return dict(family=f"COMPOSITE_PER_ASSET ({mcode.group(2).upper()} code"
                           f" + {'NonCommercial' if nc else 'CC'} content)",
                    grant_class="COMPOSITE_PER_ASSET", version="", line1=0,
                    basis=("permissive code grant plus a NonCommercial content asset"
                           if nc else "permissive code grant plus a CC content asset"))

    # (1) The gap's anchor: SPDX title on the first non-blank line.
    for fam, cls, pat in TITLE_RULES:
        if re.search(pat, l1l):
            return dict(family=fam, grant_class=cls,
                        version=_version(fam, block, text), line1=1,
                        basis="first non-blank line")

    # (2) A bespoke instrument that names itself and affirms nothing. Checked
    #     BEFORE the body layer: this is the only class whose mis-grade invites
    #     a promotion onto a sell shelf.
    if BESPOKE_TITLE.search(l1) and not ANY_GRANT.search(body):
        return dict(family=f"NOT-OSI ({l1[:58]})", grant_class="UNSELLABLE",
                    version="", line1=1,
                    basis="bespoke title, no affirmative grant in head")

    # (3) The body layer, for payloads opening on a bare copyright line --
    #     SUBJECT TO the restriction override (defect 1). A bespoke title that
    #     recites MIT and then restricts scope is NOT MIT.
    for fam, cls, pat in BODY_RULES:
        if re.search(pat, body, re.I):
            if cls == "PERMISSIVE" and not SPDX_TITLE_ANY.search(l1) and RESTRICTION.search(body):
                return dict(family=f"NOT-OSI ({l1[:58]})", grant_class="UNSELLABLE",
                            version="", line1=0,
                            basis="bespoke title recites a permissive grant form "
                                  "then restricts its scope")
            return dict(family=fam, grant_class=cls,
                        version=_version(fam, block, text), line1=0,
                        basis="body grant form, title names no family")

    # (3b) An EXPLICITLY UNDECIDED reservation. Read first-hand on
    #      `jmattheij/pianojacq` (GitLab, 32 ★, 724 B, `ce0fedea93e4`): "I
    #      haven't decided on whether to release this as open source or not so
    #      for now this software is (C) ... All rights reserved." That is not
    #      `UNSTATED` (nothing matched) and not `NO_GRANT` (no payload): it is a
    #      served payload that withholds permission AND signals the decision is
    #      open. The distinction is operational -- the action is to ASK THE
    #      AUTHOR, which is worth doing for neither of the other two classes.
    if re.search(r"(?:have ?n.?t|not) (?:yet )?decided[^.]{0,80}(?:open source|licen[cs]e)|"
                 r"licen[cs]e (?:is )?(?:still )?(?:to be|tbd|undecided|coming)", body, re.I):
        return dict(family="RESERVED_UNDECIDED", grant_class="RESERVED_UNDECIDED",
                    version="", line1=0,
                    basis="payload reserves all rights and states the licence is undecided")

    # (4) A refusal reached only here is still a refusal.
    if REFUSES.search(body):
        return dict(family=f"NOT-OSI ({l1[:58]})", grant_class="UNSELLABLE",
                    version="", line1=0, basis="refusal in head, no grant")

    return dict(family="UNSTATED", grant_class="UNSTATED", version="",
                line1=0, basis="payload served, no title or grant form matched")


def _version(fam, block, text):
    """Version from the TITLE BLOCK, never from the first line alone.

    Apache-2.0 puts "Version 2.0" on its SECOND non-blank line and the GNU
    family puts its version on its own line under the title, so a one-line
    reader cannot grade either. Recorded, not guessed.
    """
    if fam in ("GPL", "LGPL", "AGPL-3.0"):
        m = GNU_VER_RE.search(block)
        v = m.group(1) if m else ""
        if v and fam != "AGPL-3.0":
            v = f"{v}.0" if "." not in v else v
            return v + ("-or-later" if OR_LATER_RE.search(text) else "-only")
        return "3.0" if fam == "AGPL-3.0" else (v or "UNSTATED")
    m = VERSION_RE.search(block)
    if m:
        return m.group(1) or m.group(2)
    if fam.startswith("CC"):
        for v in ("4.0", "3.0", "2.0", "1.0"):
            if v in block:
                return v
    return ""


SELLABLE = {"PERMISSIVE", "PUBLIC_DOMAIN"}
# A pointer and a per-asset surface are UNRESOLVED, not sellable and not
# refused: a pointer must be followed, a per-asset surface cleared per asset.
UNRESOLVED = {"POINTER_IN_REPO", "POINTER_CROSS_REPO", "COMPOSITE_PER_ASSET",
              "UNSTATED", "RESERVED_UNDECIDED"}
BUILD_ON_WITH_CARE = {"WEAK_COPYLEFT", "STRONG_COPYLEFT", "NETWORK_COPYLEFT"}


def sellable(cls):
    """The one-bit answer a sell-shelf row needs. UNSTATED is NOT sellable."""
    return cls in SELLABLE
