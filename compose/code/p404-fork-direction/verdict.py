"""Grade a same-name repository pair by its FULL history, not by its ref set.

p402's `refset.sh` compares ref sets. That answers "are these one repository or
two" and provably cannot answer "who copied whom": a squash-republish shares
ZERO refs with its origin, so a ref-set test grades it exactly like two
unrelated repositories that happen to share a name.

Full history separates the three mechanisms that all present as
"same plugin name, different HEADs":

  INDEPENDENT   0 shared commits AND 0 shared trees  -> two implementations
  CONTENT-COPY  0 shared commits AND >0 shared trees -> republished content,
                                                        fresh history
  SUPERSET      every commit of one side is in the other, and that side's HEAD
                is an ancestor of the other's -> continuation / hand-off
  DIVERGED-FORK shared commits, neither HEAD an ancestor of the other

The function is pure so the grading rule is testable without network.
"""


def grade(shared_commits, shared_trees, a_contains_b_head, b_contains_a_head,
          root_tree_owner=None):
    """Grade a pair from measured counts.

    `a_contains_b_head` is True when B's HEAD is an ancestor of A's HEAD.
    `root_tree_owner` names the side whose ROOT commit carries a shared tree,
    which is the direction signal for a CONTENT-COPY: a root commit holding
    content that already existed in the other repository is the copy.
    """
    if shared_commits < 0 or shared_trees < 0:
        raise ValueError("counts cannot be negative")
    if a_contains_b_head and b_contains_a_head and shared_commits == 0:
        raise ValueError("mutual ancestry with no shared commits is impossible")

    if shared_commits == 0:
        if shared_trees == 0:
            return ("INDEPENDENT", None)
        if root_tree_owner is None:
            return ("CONTENT-COPY", None)        # copy proved, direction not
        return ("CONTENT-COPY", root_tree_owner)  # root-tree side is the copy

    if a_contains_b_head and not b_contains_a_head:
        return ("SUPERSET", "a")   # A continues B
    if b_contains_a_head and not a_contains_b_head:
        return ("SUPERSET", "b")   # B continues A
    if a_contains_b_head and b_contains_a_head:
        return ("SAME-HEAD", None)
    return ("DIVERGED-FORK", None)
