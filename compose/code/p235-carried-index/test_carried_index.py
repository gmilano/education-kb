#!/usr/bin/env python3
"""p235 — offline controls for the carried index. No network, no shelves required:
every case is built from fixtures in a temp dir, so this runs in a hook and in a
sandbox without egress."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import carried_index as ci  # noqa: E402

FAILED = []


def check(name, got, want):
    if got != want:
        FAILED.append(f"{name}: got {got!r}, want {want!r}")


def shelf_dir(files):
    d = tempfile.mkdtemp()
    for rel, body in files.items():
        path = os.path.join(d, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(body)
    return d


# ── fold(): ACTION UH's predicate
check("fold lowers", ci.fold("OpenOLAT/OpenOLAT"), "openolat/openolat")
check("fold strips trailing period", ci.fold("a/b."), "a/b")
check("fold strips trailing comma", ci.fold("a/b,"), "a/b")
check("fold strips trailing paren", ci.fold("a/b)"), "a/b")
check("fold is idempotent", ci.fold(ci.fold("A/B.")), "a/b")

# ── the collision p234 actually tripped over
d = shelf_dir({"README.md": "see https://github.com/OpenOLAT/OpenOLAT and "
                            "https://github.com/openolat/OpenOLAT today"})
idx = ci.harvest(d)
check("case variants collapse to one row", len(idx), 1)
check("collision is reported", list(ci.collisions(idx)), ["openolat/openolat"])
check("both spellings retained", len(ci.collisions(idx)["openolat/openolat"]), 2)
check("carried() is case-blind", ci.carried("OPENOLAT/OPENOLAT", idx), True)
check("carried() rejects a non-row", ci.carried("acme/nope", idx), False)

# ── a single spelling is not a collision
d = shelf_dir({"README.md": "https://github.com/a/b https://github.com/a/b"})
idx = ci.harvest(d)
check("one spelling twice is not a collision", ci.collisions(idx), {})
check("but it is carried", ci.carried("a/b", idx), True)

# ── shelves only: evidence/ and archive/ are NOT the shelves
d = shelf_dir({
    "README.md": "nothing here",
    "evidence/x.tsv": "https://github.com/ghost/row",
    "archive/old/agents-top.md": "https://github.com/archived/row",
})
idx = ci.harvest(d)
check("evidence is not a shelf", ci.carried("ghost/row", idx), False)
check("archive is not a shelf", ci.carried("archived/row", idx), False)

# ── a missing shelf must not be fatal (partial checkout)
d = shelf_dir({"README.md": "https://github.com/only/one"})
check("missing shelves are skipped", len(ci.harvest(d)), 1)

# ── claims(): the predicate that would have stopped the nine-pass LMS error
#    and this pass's LATAM-zero error
d = shelf_dir({
    "README.md": "LATAM: 0 open-source education repositories",
    "verticals/solutions.md": "portabilis/i-educar is the largest in Brazil",
    "intel/market.md": "i-educar again",
})
hits = ci.claims("i-educar", d)
check("claims finds the token on 2 shelves", sorted(hits), ["intel/market.md",
                                                           "verticals/solutions.md"])
check("claims counts occurrences", hits["intel/market.md"], 1)
check("claims is case-insensitive", "verticals/solutions.md" in ci.claims("I-EDUCAR", d), True)
check("claims is empty for a real absence", ci.claims("zzz-no-such-token", d), {})

# ── the URL shapes the shelves actually use
d = shelf_dir({"README.md": (
    "[`a/b`](https://github.com/a/b) | plain https://github.com/c/d, "
    "trailing https://github.com/e/f. and a dot-name https://github.com/g/h.js")})
idx = ci.harvest(d)
check("markdown link form", ci.carried("a/b", idx), True)
check("bare form with comma", ci.carried("c/d", idx), True)
check("bare form with period", ci.carried("e/f", idx), True)
check("dotted repo name survives", ci.carried("g/h.js", idx), True)

if FAILED:
    print(f"FAIL ({len(FAILED)})")
    for line in FAILED:
        print("  " + line)
    sys.exit(1)
print("PASS — 23 controls")
