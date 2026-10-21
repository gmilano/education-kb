#!/usr/bin/env python3
"""`p351-address-shape` — `ACTION ZZ-an`: the harvested address denominator, de-inflated.

p350 sampled the 17 addresses its identity run recorded as `UNANSWERED` and found that
**8 of them were never addresses at all** — GitHub navigation paths harvested as
`owner/repo` (`topics/ai-tutor`, `orgs/moodle`, `repos/moodle`, `trending/python`), two
planted negative controls, and a README placeholder (`your-username/safetutors`).  It
registered `ACTION ZZ-an` on the consequence: **every identity instrument on these
shelves quotes its coverage against a denominator that counts non-addresses as
addresses.**

ZZ-an prescribed the fix as *"an `owner/repo` shape filter that rejects `topics/`,
`orgs/`, `repos/`, `trending/` and placeholder owners"*.

🔴 **That prescription is INSUFFICIENT, measured.** The shelves carry **33**
non-addresses; ZZ-an's four named namespaces plus a placeholder-owner list reject **28**
of them and miss **five**, in three classes:

    search/repositories                    a FIFTH namespace ZZ-an did not name.  This
                                           is the generic defect of a blacklist: it is
                                           complete only against the examples that
                                           prompted it.
    .../archive  .../blob  .../releases    an ELLIDED owner.  Prose that writes a URL
                                           as `github.com/.../blob/main/LICENSE` leaves
                                           a shape the harvester reads as an address
                                           whose owner is literally "...".
    git_user_id/git_repo_id                a CODEGEN TEMPLATE VARIABLE.  It is the
                                           swagger/openapi-generator placeholder, and it
                                           is not a placeholder WORD — no list of
                                           `your-`/`my-`/`example-` prefixes reaches it.

🟢 **So this filter leads with GitHub's own naming rule rather than a blacklist.** An
owner is 1–39 characters of alphanumerics and interior single hyphens; a repository name
is 1–100 characters of alphanumerics, `.`, `-` and `_`.  `...` fails the owner rule on
the dot, `git_user_id` fails it on the underscore, and an empty component fails it on
length — none of which needs to be enumerated in advance, which is the whole point.

🟡 **But the shape rule alone is NOT sufficient either, and saying so is the honest half
of this instrument.** `topics/education` is a perfectly legal `owner/repo` shape; it is
not a repository because `topics` is a namespace on github.com.  Of the 33, the shape
rule reaches 6 and the namespace/placeholder lists reach the other 27.  **Both arms are
load-bearing** — the shape rule because it needs no foresight, the lists because
legality is not repository-hood.

🔵 **What this instrument does NOT claim.** A legal shape is not a live repository, and
this module makes no network call.  It separates *cannot be an address* from *may be an
address*; whether an address answers is `p293-slug-existence-oracle`'s question and
whether two addresses are one repository is `p349-name-collision`'s.  A pass that reads
a corrected denominator here as a coverage figure has overclaimed exactly the way ZZ-an
was registered to stop.

    address_shape.py census <shelf files...>   -> denominators, TSV
    address_shape.py reject <shelf files...>   -> every rejected shape with its class
"""
import collections
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "p348-fold-identity"))
from fold_identity import slugs_in  # noqa: E402  the harvester is p348's, not rewritten

# GitHub's own rules, as shapes rather than as a blacklist.
#   owner: 1-39 chars, alphanumeric or single interior hyphen.
#   name:  1-100 chars, alphanumeric or `.` `-` `_`.
# Folded (lower-cased) input is assumed, which is p348's convention.
OWNER_SHAPE = re.compile(r"^[a-z0-9](?:[a-z0-9]|-(?=[a-z0-9])){0,38}$")
NAME_SHAPE = re.compile(r"^[a-z0-9._-]{1,100}$")

# Legal shapes that are nonetheless not repositories: GitHub's own first-segment
# namespaces.  A path under one of these is a page on github.com, not a repo.
NAV_NAMESPACES = frozenset("""
topics orgs repos trending search collections sponsors users features about pricing
settings notifications explore marketplace apps login join new stars watching issues
pulls dashboard codespaces enterprise security sitemap contact site organizations
""".split())

# Legal shapes that are nonetheless not repositories: a human placeholder.  Kept
# deliberately short — the template-variable class above is why this list is not the
# instrument, and a long list of guessed prefixes would hide that.
PLACEHOLDER_WORD = re.compile(
    r"^(?:your|my|some|example|sample|placeholder|owner|organization|org|user|username|"
    r"company|someone|test|foo|bar|baz|xxx|tbd|todo|changeme)"
    r"(?:[-_]?(?:username|user|name|org|repo|account))?$")

# A name that is reserved or degenerate rather than a repository.
NAME_RESERVED = frozenset({".", ".."})


def classify(folded):
    """`owner/repo` (folded) -> None if it may be an address, else its rejection class.

    The classes are ordered most-specific-first, so a shape that fails several reasons
    is reported under the one a reader can act on.
    """
    owner, sep, name = folded.partition("/")
    if not sep:
        return "NO-SEPARATOR"
    if not owner:
        return "EMPTY-OWNER"
    if not name:
        return "EMPTY-NAME"
    if not OWNER_SHAPE.match(owner):
        # The two classes ZZ-an's prescription could not see, named apart so a
        # successor can tell an ellided URL from a codegen template.
        if "." in owner:
            return "OWNER-ELLIDED"
        if "_" in owner:
            return "OWNER-TEMPLATE-VAR"
        return "OWNER-ILLEGAL"
    if not NAME_SHAPE.match(name) or name in NAME_RESERVED:
        return "NAME-ILLEGAL"
    if owner in NAV_NAMESPACES:
        return "NAV-NAMESPACE"
    if PLACEHOLDER_WORD.match(owner):
        return "PLACEHOLDER-OWNER"
    if PLACEHOLDER_WORD.match(name):
        return "PLACEHOLDER-NAME"
    return None


def harvest(paths):
    """folded address -> {as published}, over whole files (history included)."""
    idx = collections.defaultdict(set)
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            for s in slugs_in(fh.read()):
                idx[s.lower()].add(s)
    return idx


def partition(idx):
    """(addresses, rejected) where rejected is folded -> class."""
    rejected = {}
    for folded in idx:
        cls = classify(folded)
        if cls:
            rejected[folded] = cls
    addresses = {a for a in idx if a not in rejected}
    return addresses, rejected


def main(argv):
    mode = "census"
    if argv and argv[0] in ("census", "reject"):
        mode, argv = argv[0], argv[1:]
    # P541: a measurement over the files it is GIVEN must refuse an empty argument list.
    if not argv:
        sys.stderr.write("p351-address-shape: no shelf files given — refusing to "
                         "publish a denominator over nothing\n")
        return 2
    idx = harvest(argv)
    addresses, rejected = partition(idx)
    if mode == "reject":
        print("folded\tclass\tas_published")
        for folded in sorted(rejected):
            print(f"{folded}\t{rejected[folded]}\t{'; '.join(sorted(idx[folded]))}")
        return 0
    byclass = collections.Counter(rejected.values())
    print("cifra\tvalor")
    print(f"harvested_folded\t{len(idx)}")
    print(f"rejected_non_addresses\t{len(rejected)}")
    print(f"addresses_corrected\t{len(addresses)}")
    pct = 100.0 * len(rejected) / len(idx) if idx else 0.0
    print(f"inflation\t{pct:.2f}%")
    for cls, n in sorted(byclass.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"class:{cls}\t{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
