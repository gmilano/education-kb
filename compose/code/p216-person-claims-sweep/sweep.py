#!/usr/bin/env python3
"""ACTION QK — sweep the shelves for PERSON-level inferences resting on an absence reading.

T215-7: this KB published "this author ships unlicensed education connectors as a pattern"
about a named individual, derived from two root-only ABSENT readings. Both repositories
declare MIT in their manifests. The claim was withdrawn in place at p215.

QK asks whether that was the only one. Limb 1: 1+ further claim about a named person, org or
author's PRACTICE rests on an absence-at-one-channel -> the KB needs a standing rule separating
what a CHANNEL RETURNED from what a PERSON DOES. Limb 2: 0 -> it was the only one.

Method: for every line on the four client-facing shelves (plus open-gaps and the README), ask
two independent questions and report the conjunction:

  (a) does the line attribute a PRACTICE, HABIT or CHARACTER to an actor
      (author / maintainer / org / "as a pattern" / "ships" / "never" / "siempre") ?
  (b) does the same line, or either neighbour, carry an ABSENCE marker
      (ABSENT / "no licence" / "sin licencia" / NOASSERTION / 404 / "unlicensed") ?

Deliberately high-recall and reported verbatim: a sweep for claims about people must not be
the one that quietly drops candidates. Every hit is adjudicated by hand in the pass notes.
"""

import re
import sys

SHELVES = [
    "agents/top.md",
    "agents/trending.md",
    "repos/foundations.md",
    "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md",
    "intel/trends.md",
    "compose/patterns.md",
    "intel/open-gaps.md",
    "README.md",
]

# (a) practice/character attributed to an actor
ACTOR = re.compile(
    r"\b("
    r"this (?:author|maintainer|developer|org|organisation|organization|team|vendor)"
    r"|the (?:author|maintainer)'s"
    r"|el (?:autor|mantenedor)"
    r"|este (?:autor|mantenedor)"
    r"|as a pattern|como patr[oó]n"
    r"|ships? (?:unlicensed|no licence|no license)"
    r"|publica sin licencia"
    r"|habitually|systematically|consistently (?:fails|omits)"
    r"|no (?:suele|acostumbra)"
    r")\b",
    re.IGNORECASE,
)

# (b) absence-at-one-channel marker
ABSENCE = re.compile(
    r"(\bABSENT\b|\bNOASSERTION\b|\bunlicensed\b|\bungranted\b"
    r"|no licence|no license|sin licencia|no grant|ning[uú]n manifiesto"
    r"|\b404\b|all `?404`?|no licence field|no license field)",
    re.IGNORECASE,
)


def main():
    hits = []
    for path in SHELVES:
        try:
            with open(path, encoding="utf-8") as fh:
                lines = fh.read().splitlines()
        except FileNotFoundError:
            sys.stderr.write(f"missing: {path}\n")
            continue
        for i, line in enumerate(lines):
            if not ACTOR.search(line):
                continue
            window = "\n".join(lines[max(0, i - 1): i + 2])
            if ABSENCE.search(window):
                hits.append((path, i + 1, ACTOR.search(line).group(0), line.strip()))

    print(f"# p216 ACTION QK — actor-practice claims co-located with an absence marker")
    print(f"# shelves swept: {len(SHELVES)}   hits: {len(hits)}")
    print("file\tline\ttrigger\ttext")
    for path, no, trig, text in hits:
        print(f"{path}\t{no}\t{trig}\t{text[:400]}")

    # Control: how often each side fires alone, so the conjunction's size is interpretable.
    actor_only = absence_only = 0
    for path in SHELVES:
        try:
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    a, b = bool(ACTOR.search(line)), bool(ABSENCE.search(line))
                    actor_only += a and not b
                    absence_only += b and not a
        except FileNotFoundError:
            pass
    print(f"\n# control: actor-claim lines with no absence on the line: {actor_only}")
    print(f"# control: absence lines with no actor claim:             {absence_only}")


if __name__ == "__main__":
    main()
