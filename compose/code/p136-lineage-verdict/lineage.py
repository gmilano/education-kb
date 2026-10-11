"""p136-lineage-verdict -- a four-way lineage verdict for repositories that share a README.

p135 established that byte-identity of a non-licence payload (the README) is a far
stronger mirror signal than the shared `pushed_at` timestamps p134 used, and wrote
that README identity "is a verdict". ACTION BU asked for that detector to be run
across the whole corpus. Running it returned 25 cross-owner clusters -- and 12 of
them are ONE repository served under TWO slugs, because GitHub keeps serving a
renamed owner or repository name. README identity is therefore a CANDIDATE, not a
verdict: it cannot distinguish a rename from a copy.

This instrument adds the two cheap git-level measurements that separate them:

    ref-set identity   `git ls-remote --heads --tags` -> sha256 of the sorted sha list
    root tree identity `git rev-parse HEAD^{tree}` (needs a shallow clone)

and reports one of five verdicts:

    ALIAS                      identical ref sets -- the same repository under two
                               names (owner renamed, repo renamed, or transferred)
    FORK_AT_TIP                same HEAD commit, different ref sets -- a live fork
                               that has not diverged yet
    DIVERGED_FORK              different HEAD, SHARED commit ancestry
    ATTRIBUTION_STRIPPED_COPY  identical root TREE, NO shared commit sha -- the file
                               content is identical and the history was replayed
                               under a different identity. This is what the four
                               `api_enem_microdados` repositories are (ACTION BW),
                               and it is invisible to every signal p134 and p135 used
    SQUASHED_COPY              different tree, NO shared commit sha, and one side is a
                               SINGLE commit against the other's many -- the files were
                               re-uploaded without the history. The one measured here
                               (`0awei0/kt`) also dropped the upstream LICENSE file,
                               which is why `licence_dropped()` exists
    INDEPENDENT                neither tree nor commits in common -- the shared README
                               is a coincidence or a copied document, not a copied tree
    UNRESOLVED                 the pair differs at ref level and the measurements that
                               would separate a fork from a copy (root tree sha, commit
                               shas) were NOT taken. Reported rather than guessed: the
                               defect this instrument exists to prevent is a verdict
                               published from a measurement nobody ran

The point of the taxonomy is that only two of the five are a supply-inflation
problem for a shelf (FORK_AT_TIP, DIVERGED_FORK), one is a KB data defect
(ALIAS -- two rows, one repository), and one is an attribution problem in the
upstream project's licence terms (ATTRIBUTION_STRIPPED_COPY).

No pytest in this environment: `python3 -I test_lineage.py` runs the suite.
"""

ALIAS = "ALIAS"
FORK_AT_TIP = "FORK_AT_TIP"
DIVERGED_FORK = "DIVERGED_FORK"
STRIPPED = "ATTRIBUTION_STRIPPED_COPY"
SQUASHED_COPY = "SQUASHED_COPY"
INDEPENDENT = "INDEPENDENT"
UNRESOLVED = "UNRESOLVED"


class Repo:
    """A measured repository. Every field is something a shallow clone or an
    ls-remote supplies; nothing here is inferred from metadata or a description."""

    def __init__(self, slug, readme_sha=None, refset_sha=None, head=None,
                 tree_sha=None, commit_shas=(), authors=(), commit_count=None,
                 files=()):
        self.slug = slug
        self.readme_sha = readme_sha
        self.refset_sha = refset_sha
        self.head = head
        self.tree_sha = tree_sha
        self.commit_shas = tuple(commit_shas)
        self.authors = tuple(authors)
        self.commit_count = commit_count
        self.files = tuple(files)

    @property
    def owner(self):
        return self.slug.split("/", 1)[0]

    @property
    def name(self):
        return self.slug.split("/", 1)[1] if "/" in self.slug else ""


def same_slug(a, b):
    """True when two slugs differ only in case. GitHub slugs are
    case-insensitive, so these are the same repository and a cluster of them is a
    defect in whoever wrote the rows, not a finding about the sector."""
    return a.slug.lower() == b.slug.lower()


def verdict(a, b):
    """Lineage verdict for a pair that already shares a README sha.

    Order matters: ref-set identity is checked before HEAD identity because two
    slugs for one repository necessarily share HEAD too, and calling that a fork
    is the error this instrument exists to prevent.
    """
    if a.readme_sha is None or b.readme_sha is None or a.readme_sha != b.readme_sha:
        raise ValueError("verdict() is only defined for repositories that share a README sha")
    if a.refset_sha and b.refset_sha and a.refset_sha == b.refset_sha:
        return ALIAS
    if a.head and b.head and a.head == b.head:
        return FORK_AT_TIP
    shared = set(a.commit_shas) & set(b.commit_shas)
    if shared:
        return DIVERGED_FORK
    if a.tree_sha and b.tree_sha and a.tree_sha == b.tree_sha:
        return STRIPPED
    counts = sorted(c for c in (a.commit_count, b.commit_count) if c is not None)
    if len(counts) == 2 and counts[0] == 1 and counts[1] > 1:
        return SQUASHED_COPY
    if (a.tree_sha and b.tree_sha) or (a.commit_shas and b.commit_shas):
        return INDEPENDENT
    return UNRESOLVED


def cluster_verdict(repos):
    """Verdict for a whole README-identity cluster.

    Case-variant slugs are collapsed first: a cluster of `Elgg/Elgg` and
    `elgg/elgg` has nothing in it. Returns (verdict, distinct_slugs) with
    verdict None when fewer than two distinct repositories remain.
    """
    distinct = []
    for r in repos:
        if not any(same_slug(r, d) for d in distinct):
            distinct.append(r)
    if len(distinct) < 2:
        return None, distinct
    verdicts = set()
    for i in range(len(distinct)):
        for j in range(i + 1, len(distinct)):
            verdicts.add(verdict(distinct[i], distinct[j]))
    # The strongest claim a cluster supports is its weakest pairwise verdict:
    # one INDEPENDENT pair means the cluster is not a single lineage.
    for v in (UNRESOLVED, INDEPENDENT, SQUASHED_COPY, STRIPPED, DIVERGED_FORK,
              FORK_AT_TIP, ALIAS):
        if v in verdicts:
            return v, distinct
    return None, distinct


def attribution_rewritten(repos):
    """For an ATTRIBUTION_STRIPPED_COPY cluster, the author identities that
    replaced the original. Returns {slug: authors} for every member whose author
    set differs from the earliest-created member's.

    This is the measurement that makes `clone` the wrong word: the trees are
    identical, so nothing was changed except who the commits say wrote them.
    """
    if not repos:
        return {}
    base = repos[0]
    out = {}
    for r in repos[1:]:
        if set(r.authors) != set(base.authors):
            out[r.slug] = r.authors
    return out


LICENCE_FILENAMES = ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md",
                     "COPYING", "COPYING.LESSER", "LICENSE-MIT", "license")


def _has_licence(files):
    names = {f.split("/")[-1] for f in files}
    return any(n in names for n in LICENCE_FILENAMES)


def licence_dropped(upstream, copy):
    """True when the upstream ships a licence file and the copy does not.

    This is the measurement that makes the taxonomy matter to a shelf rather than
    to a curiosity cabinet: a copy that drops the grant file reads as
    unlicensed-by-omission to any probe that looks at filenames, while the
    repository it was taken from is permissively licensed. A licence verdict
    therefore belongs to a LINEAGE, not to a slug -- which is the same error, in
    the opposite direction, as reading `pipwerks/scorm-api-wrapper`'s missing
    LICENSE file as a missing grant when the grant is in its package manifest and
    its source header.
    """
    if not upstream.files or not copy.files:
        return None  # not measured; say so rather than return False
    return _has_licence(upstream.files) and not _has_licence(copy.files)
