"""Grade a WHOLE name-collision group's lineage from full histories.

`p404`'s `forkdir.sh` grades ONE pair and clones two repositories to do it.  A group
of N addresses has C(N,2) pairs, so the pairwise instrument costs O(N^2) clones --
190 for `canvas-mcp`'s 20 -- which is why `intel/open-gaps.md` item 3's LINEAGE half
stayed open after `p402` answered its identity half on the ref-set channel.

The fix is not a faster clone.  It is that the facts a pair needs are properties of
ONE repository: its commit SHA set, its tree SHA set, its root commits and its HEAD.
Measure those once per address -- O(N) clones -- and every pair is a set operation on
cached data.  20 clones, 190 verdicts.

The grading rule is NOT reimplemented here.  `p404`'s `verdict.grade` is imported, so
this instrument cannot drift from the pair instrument whose 11 controls already pin it;
a group result and a pair result on the same two addresses are the same function call.

What a group adds over a pair, and why it needed its own instrument:

  * `UNRELATED` is a group-level verdict.  A pair of addresses sharing nothing is one
    measurement; N addresses sharing nothing pairwise is the finding `open-gaps` item 3
    asks for -- "many projects, not a few forked many times" -- and it can only be
    stated once every pair has been asked.
  * A lineage is TRANSITIVE and a pair test cannot see it.  If a~b and b~c, the three
    are one family even when a and c share nothing at HEAD.  Connected components over
    the related-pair graph are therefore the unit a shelf should cite, not the pair.
"""

import itertools
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                os.pardir, "p404-fork-direction"))
from verdict import grade  # noqa: E402  -- p404's rule, imported, never reimplemented

# A pair is RELATED when it shares any commit or any tree.  Both halves matter: a
# squash-republish shares zero commits, which is the whole reason `p404` exists.
RELATED = ("CONTENT-COPY", "SUPERSET", "DIVERGED-FORK", "SAME-HEAD")


class Address:
    """The per-repository facts every pair verdict in the group is computed from."""

    def __init__(self, slug, commits, trees, head, roots, root_trees, ancestors):
        self.slug = slug
        self.commits = frozenset(commits)
        self.trees = frozenset(trees)
        self.head = head
        self.roots = frozenset(roots)
        self.root_trees = frozenset(root_trees)
        # Commits reachable from HEAD.  Ancestry is asked against THIS set and never
        # against `commits` (which is `rev-list --all`): a commit on an unmerged branch
        # is in the repository and is NOT an ancestor of HEAD, and conflating the two
        # reports a fork as a superset.
        self.ancestors = frozenset(ancestors)


def pair(a, b):
    """Two Addresses -> (shared_commits, shared_trees, a>=b_head, b>=a_head, verdict, dir)."""
    shared_commits = len(a.commits & b.commits)
    shared_trees = len(a.trees & b.trees)
    a_has_b = b.head in a.ancestors
    b_has_a = a.head in b.ancestors
    owner = None
    if shared_commits == 0 and shared_trees > 0:
        # Direction for a content copy: the side whose ROOT tree is the shared one is
        # the copy, because a root commit cannot hold content that did not exist yet.
        shared = a.trees & b.trees
        a_root_shared = bool(a.root_trees & shared)
        b_root_shared = bool(b.root_trees & shared)
        if a_root_shared != b_root_shared:          # exactly one side: unambiguous
            owner = "a" if a_root_shared else "b"
    verdict, direction = grade(shared_commits, shared_trees, a_has_b, b_has_a,
                               root_tree_owner=owner)
    return shared_commits, shared_trees, a_has_b, b_has_a, verdict, direction


def components(slugs, related_pairs):
    """Connected components over the related-pair graph, as sorted lists.

    Lineage is transitive; a pair test is not.  Two addresses with nothing in common
    still belong to one family when a third relates them, so a shelf that cites the
    PAIR understates the family.
    """
    parent = {s: s for s in slugs}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in related_pairs:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    groups = {}
    for s in slugs:
        groups.setdefault(find(s), []).append(s)
    return sorted((sorted(v) for v in groups.values()), key=lambda v: (-len(v), v[0]))


def grade_group(addresses):
    """[Address] -> (rows, components, summary).

    `rows` is every pair, graded.  `summary` counts the verdicts, so "20 addresses,
    0 related pairs" is stated with its denominator rather than asserted.
    """
    rows, related = [], []
    for a, b in itertools.combinations(addresses, 2):
        sc, st, ab, ba, verdict, direction = pair(a, b)
        rows.append((a.slug, b.slug, len(a.commits), len(b.commits), sc, st, ab, ba,
                     verdict, direction))
        if verdict in RELATED:
            related.append((a.slug, b.slug))
    slugs = [a.slug for a in addresses]
    summary = {}
    for r in rows:
        summary[r[8]] = summary.get(r[8], 0) + 1
    return rows, components(slugs, related), summary
