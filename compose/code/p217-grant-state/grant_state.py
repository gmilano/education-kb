"""p217 - P217-A: report a grant STATE, never let a prose channel write the licence field.

Measured problem (p217, over the 67 ungranted rows):
  - a scanner trusting README prose records MIT for 4 repositories whose LICENSE file
    does not exist (180, 179, 76 and 36 files in tree; 0 licence-shaped paths);
  - it records MIT for a repo whose README says "MIT - demo use only";
  - it records CC BY 4.0 for a benchmark whose own prose says CC BY-SA 4.0;
  - and a scanner reading only FILES records nothing for 2 repositories that have
    affirmatively REFUSED a grant, so it re-queues them forever.

The return value is a (state, licence, channel) triple. The licence slot is None unless
a BLOB was read. That is the rule this module exists to enforce.

States, and the instruction each carries to a studio:
  GRANTED          -> build
  CLAIMED-IN-PROSE -> a lead; ask
  CLAIMED-DANGLING -> a lead with a named defect; one commit fixes it
  GRANT-REFUSED    -> do not touch. Answered. Never queue again.
  NON-PUBLIC       -> nothing left to probe
  UNKNOWN          -> probe
"""

# Ordered: the refusal test runs BEFORE any permissive token. AI-LMS-TMS's README
# contains "License" as a heading and "All rights reserved" as the body; heading-first
# ordering gets it backwards - the same bug P216-A fixed for ECL-2.0.
REFUSAL = (
    "all rights reserved",
    "proprietary software",
    "not licensed for redistribution",
    "todos los derechos reservados",          # T217-2: the shelves are bilingual
    "software propietario",
    "保留所有权利",   # P421: and so is the upstream corpus
)

LICENCE_NAMES = (
    "mit", "apache", "bsd", "gpl", "lgpl", "agpl", "mpl", "isc",
    "creative commons", "cc by", "ecl", "educational community license",
)


def grant_state(slug):
    blob = read_licence_blob(slug)            # p215 channel: full ls-tree, 0 blob transfer
    if blob:
        return ("GRANTED", classify_p216(blob), "blob")   # p216's ECL-aware title-window

    readme = fetch_readme(slug)               # 6 filename forms; None if the repo is gone
    if readme is None:
        return ("NON-PUBLIC", None, None)     # confirm with `git ls-remote --symref`

    win = licence_section(readme)             # the SECTION BODY, never the heading alone
    if not win:
        return ("UNKNOWN", None, "readme")

    low = win.lower()
    if any(t in low for t in REFUSAL):
        return ("GRANT-REFUSED", None, "readme")

    if is_domain_noun(slug, win):             # spdx/license-list-data: licence as DATA (T215-4)
        return ("UNKNOWN", None, "readme")

    if any(n in low for n in LICENCE_NAMES):
        if not points_at_existing_file(slug, win):
            return ("CLAIMED-DANGLING", None, "readme")
        return ("CLAIMED-IN-PROSE", None, "readme")

    return ("UNKNOWN", None, "readme")


def licence_section(readme):
    """Return the BODY under the first licence-shaped heading, not the heading itself.

    9 of p217's 19 hits matched only `## License`; the grant sat 1-3 lines below, and in
    two of those cases the body was a refusal.
    """
    lines = readme.splitlines()
    for i, line in enumerate(lines):
        s = line.strip().lower()
        if s.startswith("#") and "licen" in s:
            return "\n".join(lines[i:i + 12])
    # a statement can also appear with no heading at all (haanhtuandev/vgu-mcp)
    for i, line in enumerate(lines):
        low = line.lower()
        if "licensed under" in low or "license -" in low or "license." in low:
            return "\n".join(lines[i:i + 4])
    return None


def points_at_existing_file(slug, win):
    """True only if the prose names a file that is actually in the tree.

    The tree is already in hand from read_licence_blob()'s ls-tree call, so this is a
    set-membership test, not a fetch - which is what makes CLAIMED-DANGLING cheap.
    """
    if "license" not in win.lower():
        return True                            # no pointer claimed; not a dangling case
    return bool(licence_shaped_paths(slug))


def is_domain_noun(slug, win):
    """Reject repositories ABOUT licences. Second instance of the T215-4 class."""
    name = slug.split("/")[-1].lower()
    return "license" in name or "licence" in name
