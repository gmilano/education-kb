#!/usr/bin/env python3
"""`p367-bare-slug-channel` — `ACTION ZZ-bv`: the second address channel, built.

🔴 **The defect, in `p366`'s own words:** *"every 'absent from N addresses' figure
this base has published, `p364`'s 79% included, is an over-estimate by the size of
its bare-slug class."*  `p366` measured the rate — **8.2%** — and registered
`ACTION ZZ-bv` because it did not fix the channel.  This file is the fix.

🔵 **Where the blindness actually lives, named so it cannot be mistaken for a
judgement call.**  `p348-fold-identity` harvests addresses with

    SLUG = re.compile(r"github\\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

and **every** census, identity and absence instrument on this base imports
`slugs_in` from it rather than reimplementing — which is the right rule and is
exactly why the blindness is total.  A repository this base discusses as a bare
backticked slug (`CAHLR/OATutor-Content`, mentioned **7** times, `Gap 264`'s own
subject) is invisible to all of them at once.

🟢 **So this is a SECOND channel, not a replacement.**  Channel **U** is p348's
URL form and is untouched.  Channel **B** reads a backticked one-slash token.
The two are reported separately, because their precision is not remotely the
same and a successor must not average them.

🔴 **Channel B over-collects by construction and that is deliberate.**  Markdown
prose writes `owner/repo`-shaped things that are not repositories: a shelf path
(`agents/top.md`), a grant rung (`main/LICENSE`), a ratio (`47/47`), a licence
pair (`MIT/Apache-2.0`).  Four offline arms reject those classes; what survives is
**adjudicated online by `git ls-remote`**, which is the only instrument here that
can say a repository exists.  🟢 The offline arms are therefore allowed to be
imprecise and are MEASURED rather than trusted — `probe_slugs.sh` reports the
survivor precision, and the false-rejection control probes a sample of the
rejected set to prove the arms are not eating live repositories.

🔵 **What this instrument does NOT claim.**  A live address is not an
education-relevant repository, and a live address is not a *distinct* repository:
two addresses can serve one commit.  Deciding that is `p366`'s `HEAD`-sha test and
the `ref-set` refinement in `probe_slugs.sh`, not this module's shape rules.

    bare_slug_channel.py census <shelf files...>   -> both channels, TSV
    bare_slug_channel.py candidates <shelf files...>  -> channel-B survivors, one per line
    bare_slug_channel.py reject <shelf files...>   -> every channel-B rejection with its class
"""
import collections
import importlib.util
import os
import re
import sys

# 🔵 p348's harvester and p351's shape filter are IMPORTED, never reimplemented —
# `p352`'s rule, because two copies of a shape filter is this base's "second
# channel disagreeing with itself" defect.
_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(relpath, name):
    path = os.path.join(_HERE, os.pardir, relpath)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _address_shape():
    return _load(os.path.join("p351-address-shape", "address_shape.py"),
                 "p351_address_shape")


# A backticked run with no newline in it.  The backtick is load-bearing: `ZZ-bv`'s
# specimen is a *backticked* slug, and unticked prose `owner/repo` cannot be told
# from an English word pair by any rule this file could carry honestly.
TICKED = re.compile(r"`([^`\n]{3,120})`")

# 🔴 `.git` is a real clone suffix and must fold to the same address as the bare
# name.  p348's `slugs_in` strips it; p367's FIRST DRAFT DID NOT, and the omission
# put **7** spelling artefacts into the live population and 7 false rows into the
# sha-collision table (`cvmcosta/ltijs.git` ≡ `cvmcosta/ltijs`).  It did not move
# the net-new count, because each artefact collided with its own de-suffixed form —
# which is the only reason a reader of the first draft would not have been misled.
NAME_TRAILERS = re.compile(r"(?:\.git)$", re.IGNORECASE)

# Arm 1 — a first segment that is a git ref or a directory, not an owner.  This is
# the largest rejection class by far and it is a list rather than a shape for the
# reason `p351` states about `NAV_NAMESPACES`: legality is not repository-hood.
# `main/LICENSE` is a perfectly legal `owner/repo` shape.
#
# 🔴 `make gate-ladder-case` — `p283`'s audit — graded this file `SINGLE-SPELLING` on the
# `licence` family the moment it entered `HOOK_GATES`, breaching `p286`'s ratchet
# (STANDING:SINGLE-SPELLING 17 -> 18).  🟡 Two remedies were tried and MEASURED before the
# cause was found, and both are recorded because each was wrong in an instructive way.
#   (a) Case-closing these words in the literals — `p352`'s and `p354`'s remedy when the
#       same audit caught THEIR ladders.  It moved the reason from `no-upper-ext` to
#       `UPPER-EXT` and did not clear the grade, because it was treating a symptom.
#   (b) Deleting the grant-family words outright.  🔴 Refuted by measurement: six
#       non-addresses leaked straight into the live population (`license/license`,
#       `license/disclaimer`, `license/license.code`, `license/license.original`,
#       `license/license.output`, `licenses/license-mit`), so the stems are load-bearing
#       and the owner `license` is a real rejection this instrument needs.
# 🟢 THE ACTUAL CAUSE was this file's OWN IDENTIFIERS, in two places.  `p283`'s `BARE`
# pattern is case-sensitive and unquoted, so it read the constant `LICENCE_TOKEN` and the
# rejection-class string `"LICENCE-PAIR"` as licence PATH spellings — the exact defect class
# `p286` wrote `_METHODS` to catch for `LICENCE.findall`, arriving through a constant and a
# status value rather than an attribute.  Neither names a file: the set holds SPDX-style
# licence IDENTIFIERS (`mit`, `apache-2.0`).  🟢 Renamed `GRANT_ID_TOKEN` and
# `GRANT-ID-PAIR`, the family words below stay lowercase — which is all the behaviour needs,
# since membership is tested against a folded owner — and the grade clears to `COMMENT-ONLY`
# on the `main/LICENSE` that survives in the prose above, where it belongs.
# 🔵 The population was re-measured after every one of the three attempts and is
# byte-identical at all four points: 823 channel-B-only candidates.  A gate fix that moves
# the measurement is a different instrument wearing the same name.
# 🔵 Worth the three attempts: the audit was RIGHT that this file named licence vocabulary
# in code, and WRONG about what for.  An instrument that reports the right finding with the
# wrong cause is this base's most expensive failure mode, and the cheap tell was that
# neither remedy moved the number.
REF_OR_PATH = frozenset(w.lower() for w in """
main master develop dev head trunk release stable latest newnew lib libs
docs doc documentation html public src source test tests spec specs scripts
script packages package pkg refs appinfo components component tools tool bin
build dist data dados config conf assets images img static templates
template include includes vendor node_modules modules module plugin plugins
theme themes examples example fixtures sample samples debian license licence licenses licences
Licence licence COPYING Copying copying NOTICE Notice notice README Readme
ReadMe readme api app apps core server client web www frontend backend ui
cli sdk admin classes db sql migrations util utils common shared internal
cmd pages local mod blocks block other v0 v1 v2 v3 v4 ingest evidence
archive raw code compose agents repos intel verticals decisions skills
overview ontology industries onboarding bootstrap decks harness-builder
""".split())

# Arm 2 — a second segment that is a FILE.  A repository may legally be named
# `socket.io`, so this arm is restricted to extensions that mark a document or a
# source file rather than any dotted name.
DOC_EXT = (".md", ".txt", ".tsv", ".csv", ".json", ".yml", ".yaml", ".sh", ".py",
           ".php", ".xml", ".html", ".htm", ".rst", ".toml", ".cfg", ".ini",
           ".lock", ".sql", ".pdf", ".png", ".svg", ".log", ".mjs", ".ipynb",
           ".tex", ".bib", ".zip", ".gz")

# Arm 3 — a ratio or a date, not an address.  This base writes `47/47` and
# `2026/1744` constantly; both are legal shapes.
# Arm 4 — a grant-identifier pair.  `MIT/Apache-2.0` is shaped exactly like an address.
GRANT_ID_TOKEN = frozenset("""
mit apache-2.0 apache2 apache bsd bsd-2-clause bsd-3-clause gpl gpl-2.0 gpl-3.0
agpl agpl-3.0 lgpl lgpl-2.1 lgpl-3.0 mpl-2.0 cc-by cc-by-sa cc-by-sa-4.0
cc-by-nc-sa-4.0 cc0 unlicense proprietary sata epl-2.0 isc zlib wtfpl
""".split())


# 🆕 Arm 5 (p382) — a first segment that is a git BRANCH PREFIX.  `Gap 539`, and p381 gave
# it its first fixture the hard way: p381 wrote `feature/x` into Gap 539's own text as an
# EXAMPLE of a branch prefix, and THIS HARVESTER HARVESTED THE EXAMPLE, putting a fake
# address into p381's own census inside the sentence declaring the defect.
# 🔵 `release`, `main`, `master`, `develop`, `dev`, `head`, `trunk`, `stable` and `latest`
# are already in REF_OR_PATH above, so they are deliberately NOT repeated here: this set is
# what p381 asked for MINUS what was already caught, plus the rest of git-flow and
# Conventional Commits.
# 🔴 THE FALSE-POSITIVE RISK, DECLARED HERE RATHER THAN DISCOVERED LATER: `fix`, `patch`,
# `perf`, `ci`, `style`, `task` and `wip` are all LEGAL GitHub owner names, so this arm will
# reject a real repository owned by anyone so named.  That is the same trade REF_OR_PATH
# already makes for `api`, `app`, `core` and `web`, and it is made for the same reason —
# channel B harvests MARKDOWN PROSE, where `feature/foo` is a branch far more often than an
# owner.  🟢 Measured at p382 over the nine SHELF_FILES: 8 distinct tokens rejected, census
# 3 078 -> 3 070, and all 8 are named in evidence/branch-prefix-stoplist.2026-10-22-p382.tsv.
BRANCH_PREFIX = frozenset("""
feature feat fix bugfix hotfix chore refactor perf style ci revert
wip tmp temp backport patch task story epic spike draft
dependabot renovate
""".split())


def fold(token):
    """One address, one spelling — `gate-fold-identity`'s rule applied at source."""
    return NAME_TRAILERS.sub("", token.strip()).lower()


def classify_b(folded):
    """Channel-B-specific rejection class, or None if it may be an address.

    🔵 This runs AFTER `p351.classify`, never instead of it: p351 owns the
    shape and namespace question, and this function owns only the four classes
    that a *markdown document* introduces and a URL cannot.
    """
    owner, sep, name = folded.partition("/")
    if not sep:
        return "NO-SEPARATOR"
    if owner in REF_OR_PATH:
        return "REF-OR-PATH-SEGMENT"
    if name.endswith(DOC_EXT):
        return "DOC-PATH"
    if owner.isdigit() or name.isdigit():
        return "NUMERIC-PAIR"
    if owner in GRANT_ID_TOKEN or name in GRANT_ID_TOKEN:
        return "GRANT-ID-PAIR"
    if owner in BRANCH_PREFIX:
        return "BRANCH-PREFIX"          # 🆕 p382, Gap 539
    return None


def channel_u(paths):
    """p348's URL channel, folded. Imported harvester, untouched behaviour."""
    fi = _load(os.path.join("p348-fold-identity", "fold_identity.py"),
               "p348_fold_identity")
    out = collections.Counter()
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for s in fi.slugs_in(fh.read()):
                out[s.lower()] += 1
    return out


def channel_b(paths, shape=None):
    """(survivors, rejected) over backticked one-slash tokens.

    `survivors` is folded -> occurrence count; `rejected` is folded -> class.
    Rejections from p351 are reported under p351's own class names, so a reader
    can tell a shape rejection from one of this file's four arms.
    """
    shape = shape or _address_shape()
    seen = collections.Counter()
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for m in TICKED.finditer(fh.read()):
                token = m.group(1).strip()
                if token.count("/") != 1:
                    continue
                seen[fold(token)] += 1
    survivors, rejected = collections.Counter(), {}
    for folded, n in seen.items():
        cls = shape.classify(folded) or classify_b(folded)
        if cls:
            rejected[folded] = cls
        else:
            survivors[folded] = n
    return survivors, rejected


def main(argv):
    mode = "census"
    if argv and argv[0] in ("census", "candidates", "reject"):
        mode, argv = argv[0], argv[1:]
    # P541: a measurement over the files it is GIVEN must refuse an empty list.
    if not argv:
        sys.stderr.write("p367-bare-slug-channel: no shelf files given — refusing "
                         "to publish a corpus over nothing\n")
        return 2
    u = channel_u(argv)
    b, rejected = channel_b(argv)
    only_b = {a: n for a, n in b.items() if a not in u}
    if mode == "candidates":
        for a in sorted(only_b):
            print(a)
        return 0
    if mode == "reject":
        print("folded\tclass")
        for a in sorted(rejected):
            print(f"{a}\t{rejected[a]}")
        return 0
    print("cifra\tvalor")
    print(f"channel_u_addresses\t{len(u)}")
    print(f"channel_b_ticked_candidates\t{len(b) + len(rejected)}")
    print(f"channel_b_rejected\t{len(rejected)}")
    print(f"channel_b_survivors\t{len(b)}")
    print(f"channel_b_only\t{len(only_b)}")
    for cls, n in sorted(collections.Counter(rejected.values()).items(),
                         key=lambda kv: (-kv[1], kv[0])):
        print(f"class:{cls}\t{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
