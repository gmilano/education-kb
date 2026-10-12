"""p145-not-shipped-property -- `ACTION EA`: is the `NOT_SHIPPED` list a sound exclusion?

> 🟡 **`ACTION EA`** -- apply `T39` to the `NOT_SHIPPED` list properly. For each of the
> nine inert names, state the property-bearing test: could a tree with that name ever hold
> a shipped tool registration? Replace the blanket list with the two names `P144-H` proves
> are load-bearing plus an explicit rule.
> 🔴 *Refuted if any of the nine names can be shown to bear a registration in a real
> repository outside this shelf's 16 subjects* -- which would mean the list is a sound
> heuristic that this population simply does not exercise, and it should be kept whole.

🟢 **The falsifier names a population this KB already holds**: the 44-row census includes
28 repositories that are NOT among the 16 surface subjects. This probe runs the registration
scanner over every `NOT_SHIPPED`-named tree in all 44, so the falsifier is evaluated on
evidence rather than on the 16 rows that motivated the list.

The property is *"bears a shipped tool registration"*. A name is sound to exclude only if
no tree carrying it bears one.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "p145-surface-payload-repair"))
import surface_gate3 as g  # noqa: E402

NAMES = sorted(g.NOT_SHIPPED)
# 🔴 `P144-H` measured these two as the only names that change any row on this shelf.
LOAD_BEARING = {"legacy_reference", "scripts"}

COLS = ["repo", "tree_name", "rel_path", "literal", "dynamic", "gated", "bears_registration"]


def find_trees(root):
    """Every directory under `root` whose basename is in NOT_SHIPPED."""
    hits = []
    for base, dirs, _files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {".git", "node_modules", "__pycache__"}]
        for d in list(dirs):
            if d in g.NOT_SHIPPED:
                hits.append(os.path.join(base, d))
    return hits


def main(argv):
    rows = []
    for spec in argv:
        subject, root = spec.split("=", 1)
        for tree in find_trees(root):
            lit, dyn, gated, _l, _s, _sites = g.scan(tree)
            if lit or dyn or gated:
                rows.append(dict(zip(COLS, [
                    subject, os.path.basename(tree),
                    os.path.relpath(tree, root), lit, dyn, gated, "YES"])))
            else:
                rows.append(dict(zip(COLS, [
                    subject, os.path.basename(tree),
                    os.path.relpath(tree, root), 0, 0, 0, "no"])))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    print("", file=sys.stderr)
    bearing = {}
    seen = {}
    for r in rows:
        seen.setdefault(r["tree_name"], 0)
        seen[r["tree_name"]] += 1
        if r["bears_registration"] == "YES":
            bearing.setdefault(r["tree_name"], []).append(r["repo"])
    print("# %-18s %-8s %-8s %s" % ("name", "trees", "bearing", "verdict"),
          file=sys.stderr)
    for n in NAMES:
        b = bearing.get(n, [])
        tag = ("LOAD_BEARING" if n in LOAD_BEARING else
               ("🔴 BEARS -- EXCLUSION UNSOUND" if b else "inert here"))
        print("# %-18s %-8d %-8d %s" % (n, seen.get(n, 0), len(b), tag),
              file=sys.stderr)
        for repo in b:
            print("#     bears in: %s" % repo, file=sys.stderr)
    unsound = [n for n in bearing if n not in LOAD_BEARING]
    print("", file=sys.stderr)
    print("# names NOT in P144-H's load-bearing pair that nevertheless bear a "
          "registration: %d  %s" % (len(unsound), ", ".join(sorted(unsound)) or "-"),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
