#!/usr/bin/env python3
"""`p400-candidate-membership` — `ACTION p400-C`: the ACCEPTANCE test, which no instrument owned.

🔴 **The defect, in the words of the passes that committed it.**  `p398` and `p399` each closed
on *"every one already carried on these shelves, **each checked by grep** rather than by
memory"* — and a grep for a bare repository NAME is a SUBSTRING match over the shelf text.
🔴 **It therefore answers "already shelved" for an address this base has never carried**, and the
address is dropped before any licence read, any census, any gate.  Every census instrument on
this tree asks *"which addresses does the shelf hold?"*; **this asks the opposite question** —
*"is THIS candidate on the shelf?"* — and the opposite question had no instrument.

🟢 **The specimen is live, not constructed.**  `p400`'s supply leg returned
`andres-tovar-purdue/ai-grader`.  A bare `grep ai-grader` over the tree returns hits, every one
of them from [`moocupv/lti-ai-grader`](https://github.com/moocupv/lti-ai-grader) — a **different
repository, a different owner and a different name**, whose name merely CONTAINS the candidate's.
🔴 Read as a membership verdict that is a false *"already shelved"*, and `p400`'s own first check
produced exactly that before this module existed.

🔵 **The nearest owner, named so this is not re-sold as new.**  `p332-delivery-audit` already
finds this SHAPE — its `PREFIX PAIRS` arm reports `eecs-autograder/autograder` against
`eecs-autograder/autograder.io`.  🔴 **But p332 looks INSIDE the harvested corpus**, pairing
slugs the shelves already hold.  An incoming candidate is not in the corpus yet, which is
precisely why the shape survived there and was never caught here.  Same family as `T80`: a
defect that moves one layer out and finds no instrument waiting.

🟢 **BOTH channels, because the symmetric error is already owned and must not be re-committed.**
`p374`/`p375` established that a bare backticked `owner/repo` is invisible to the `github.com/`
harvester.  An exact-address membership test keyed on URLs alone would therefore answer
**UNSHELVED** for `dymchenkko/claude-study-agent` and `i-ninte/grad-agent` — both fully carried
on `agents/trending.md`, **with their grants read**, and neither written as a link.
🟢 So this module takes its address set from `p375.union_harvest`, which is channel U ∪ channel
B with both shape filters applied, and **those two addresses are pinned as controls** so no
successor can narrow this back to one channel.

🔵 **What this module does NOT claim.**  `UNSHELVED` is not *"new to the world"* and not
*"worth promoting"* — `p400`'s own specimen is `UNSHELVED`, unlicensed and stayed off every
build-on tier.  A membership verdict is an input to a licence read, never a substitute for one.

    membership.py classify <candidate...>     -> one verdict per candidate, TSV
    membership.py audit <file>                -> one candidate per line, TSV with a summary
"""
import importlib.util
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(relpath, name):
    path = os.path.join(_HERE, os.pardir, relpath)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _p375():
    return _load(os.path.join("p375-census-union", "census_union.py"), "p400_p375")


def _p367():
    return _load(os.path.join("p367-bare-slug-channel", "bare_slug_channel.py"), "p400_p367")


def _p351():
    return _load(os.path.join("p351-address-shape", "address_shape.py"), "p400_p351")


# 🟢 The shelf list is IMPORTED from `p235`'s committed index, never restated here — `p286`'s
# ratchet, and `p371`'s own remedy for this exact temptation.
def shelf_paths(root="."):
    p235_dir = os.path.join(_HERE, os.pardir, "p235-carried-index")
    sys.path.insert(0, p235_dir)
    try:
        from carried_index import SHELVES  # noqa: E402
    finally:
        sys.path.pop(0)
    return [os.path.join(root, s) for s in SHELVES
            if os.path.exists(os.path.join(root, s))]


# The verdicts.  `NAME-SUBSTRING-ONLY` is the one that exists because of the defect: a bare-name
# grep says "shelved" and the exact-address channels say nothing.
SHELVED_EXACT = "SHELVED-EXACT"
NAME_OTHER_OWNER = "NAME-OTHER-OWNER"
NAME_SUBSTRING_ONLY = "NAME-SUBSTRING-ONLY"
UNSHELVED = "UNSHELVED"
NOT_AN_ADDRESS = "NOT-AN-ADDRESS"


class Shelf:
    """The shelf's addresses over BOTH channels, plus the raw text a bare grep would search."""

    def __init__(self, paths):
        p375 = _p375()
        self.addresses, self.rejected, _harvested, _b = p375.union_harvest(paths)
        self.names = {}
        for a in self.addresses:
            owner, _, name = a.partition("/")
            self.names.setdefault(name, set()).add(owner)
        chunks = []
        for p in paths:
            with open(p, encoding="utf-8", errors="replace") as fh:
                chunks.append(fh.read().lower())
        self.text = "\n".join(chunks)

    def classify(self, candidate):
        """A candidate `owner/name` -> (verdict, evidence).

        Shape is asked FIRST, for `p375`'s reason: a string that cannot be an address is a
        false positive whatever any channel says about it.
        """
        p367, p351 = _p367(), _p351()
        folded = p367.fold(candidate)
        if not folded or "/" not in folded:
            return NOT_AN_ADDRESS, "no owner/name shape"
        if p351.classify(folded) is not None:
            return NOT_AN_ADDRESS, p351.classify(folded)
        shape = _p375().name_reject(folded)
        if shape:
            return NOT_AN_ADDRESS, shape
        if folded in self.addresses:
            return SHELVED_EXACT, folded
        _owner, _, name = folded.partition("/")
        others = sorted(self.names.get(name, ()))
        if others:
            return NAME_OTHER_OWNER, ",".join(o + "/" + name for o in others)
        # 🔴 The defect's own class: the text says yes and every address channel says no.
        if name in self.text:
            return NAME_SUBSTRING_ONLY, _containing(self.names, name)
        return UNSHELVED, "-"


def _containing(names, name):
    """Which shelved NAMES contain this candidate's name as a substring — the grep's hits."""
    hits = sorted(n for n in names if name in n and n != name)
    return ",".join(hits[:6]) if hits else "prose-only"


def main(argv):
    mode = "classify"
    if argv and argv[0] in ("classify", "audit"):
        mode, argv = argv[0], argv[1:]
    # P541: an instrument that takes its population by argument refuses an empty one.
    if not argv:
        sys.stderr.write("p400-candidate-membership: no candidate given — refusing to "
                         "publish a membership verdict over nothing\n")
        return 2

    explicit = []
    if mode == "audit":
        with open(argv[0], encoding="utf-8") as fh:
            cands = [l.strip() for l in fh if l.strip() and not l.startswith("#")]
        rest = argv[1:]
        # 🟢 An explicit shelf list beats a root, so a caller can grade against a FIXTURE
        # population.  `p400`'s own suite needs this: a control whose population is the live
        # tree is falsified by the pass that writes to it.
        explicit = [p for p in rest if os.path.isfile(p)]
        root = next((p for p in rest if os.path.isdir(p)), ".")
    else:
        cands, root = argv, "."

    shelf = Shelf(explicit or shelf_paths(root))
    print("candidate\tverdict\tevidence")
    counts = {}
    for c in cands:
        verdict, ev = shelf.classify(c)
        counts[verdict] = counts.get(verdict, 0) + 1
        print(f"{c}\t{verdict}\t{ev}")
    if mode == "audit":
        print("#")
        for v in sorted(counts):
            print(f"# {v}\t{counts[v]}")
        print(f"# shelf addresses (channel U union B)\t{len(shelf.addresses)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
