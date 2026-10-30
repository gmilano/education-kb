#!/usr/bin/env python3
"""rule-revision.py -- the instrument Gap 549-B demanded (p551).

WHY THIS EXISTS
  p549 reproduced the canonical address rule over six commits and found that
  `repos/foundations.md` measures 175 at p543..p548 under the rule's CURRENT
  revision, while p546 and p547 correctly published 176 under the rule of their
  day -- because p548 later added `x` and `y` to PLACEHOLDER as its fix for
  547-I recurring.

  p549 wrote: "Both figures are right; neither is reproducible without its
  revision." A figure carrying only a rule NAME is therefore still pass
  arithmetic in the sense Gap 546-B named -- the name is stable while the rule
  underneath it moves, so two passes can publish different numbers, both
  honestly, both labelled identically, and no later pass can tell which rule
  produced which.

  546-B's fix was "the rule ships WITH the number, as runnable code". This is
  the missing half: the rule's REVISION ships with the number too.

WHAT IT GUARANTEES
  1. The revision is derived from the rule's actual decision inputs --
     NOT_A_REPO, PLACEHOLDER and the CANONICAL designation -- read out of
     address-count.py by import, never retyped here. Retyping them would create
     a second copy that drifts, which is the defect class this closes.
  2. Set ordering cannot affect the hash: members are sorted before hashing, so
     the same rule reformatted yields the same revision.
  3. The hash covers the CANONICAL name as well, so redesignating the canonical
     rule moves the revision even if the sets do not change.
  4. It prints the full stamp `<rule>@<sha12>` ready to paste beside a figure,
     and `--verify` re-derives a stamp recorded earlier and exits non-zero on
     disagreement, so a successor can CHECK a carried figure rather than trust it.

WHAT IT DOES NOT DO
  It does not version the extraction REGEXes (LINK_TEXT, PAIR) or the table-row
  detection. Those are also rule inputs, and a change to either would move the
  counts without moving this hash. They are excluded because they are code
  rather than data and cannot be hashed stably by import; closing that is a
  successor's job and is registered as Gap 551-B rather than left implied.

USAGE
    python3 ingest/rule-revision.py                 # print the current stamp
    python3 ingest/rule-revision.py --show          # stamp + the hashed inputs
    python3 ingest/rule-revision.py --verify STAMP  # exit 1 if STAMP is stale
"""
import hashlib
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent


def load_address_count():
    """Import address-count.py by path -- its name is not a valid identifier."""
    target = HERE / "address-count.py"
    if not target.exists():
        sys.exit(f"rule-revision: cannot find {target}")
    spec = importlib.util.spec_from_file_location("address_count", target)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def inputs(mod):
    """The rule's decision inputs, in a canonical, order-independent form."""
    return [
        ("CANONICAL", [mod.CANONICAL]),
        ("NOT_A_REPO", sorted(mod.NOT_A_REPO)),
        ("PLACEHOLDER", sorted(mod.PLACEHOLDER)),
    ]


def revision(mod):
    h = hashlib.sha256()
    for name, members in inputs(mod):
        h.update(name.encode())
        h.update(b"\x00")
        for m in members:
            h.update(m.encode())
            h.update(b"\x00")
        h.update(b"\x01")
    return h.hexdigest()[:12]


def main(argv):
    mod = load_address_count()
    rev = revision(mod)
    stamp = f"{mod.CANONICAL}@{rev}"

    if "--verify" in argv:
        i = argv.index("--verify")
        if i + 1 >= len(argv):
            sys.exit("rule-revision: --verify needs a stamp")
        given = argv[i + 1].strip()
        if given == stamp:
            print(f"OK\t{given}")
            return 0
        print(f"STALE\tgiven={given}\tcurrent={stamp}")
        print(
            "The rule moved since that figure was published. The figure is not "
            "wrong -- it is not reproducible under the current rule. Re-derive it."
        )
        return 1

    print(stamp)
    if "--show" in argv:
        for name, members in inputs(mod):
            print(f"  {name}\t{len(members)}\t{' '.join(members)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
