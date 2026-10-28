#!/usr/bin/env python3
"""p515 — the probe that would have caught p514's error.

A UNIVERSAL CLAIM about a licence class ("every LMS on these shelves is copyleft")
is not checkable by gate-shelf-consistency, which compares licence CELLS for one
slug across shelves. p514 shipped such a claim while two live rows contradicted it.

This probe does the one thing that catches that class: it collects universal
licence claims from the live shelves, collects the permissive rows those claims
quantify over, and prints both so a claim can never be read without its
counterexamples in view.

Limits, stated because an unstated limit is how p514 happened:
  * It finds claims by PHRASE, so a claim worded a new way is missed.
  * It EXCUSES a line that quotes a claim, corrects it, or scopes it ("this
    window", "they front"), so the exit code means "an unqualified universal
    claim is live", not merely "the words appear somewhere".
  * It does not decide truth. It puts a claim next to the rows it quantifies
    over and leaves the verdict to a reader.
  * It reads the shelves as text. It does not fetch anything.

Usage: python3 -I class_claim.py [KB_ROOT]
Exit 1 if any universal claim coexists with a contradicting permissive row.
"""
import os, re, sys

SHELVES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "compose/patterns.md",
           "intel/market.md", "intel/trends.md"]

# universal quantifiers over a licence class
CLAIM = re.compile(
    r"(every|all|each|no)\s+(\w+\s+){0,3}?(LMS|platform|repo|repository|row|shelf|option)s?"
    r"[^.\n]{0,80}?(is|are|ships?|carr(?:y|ies)|remains?)\s+"
    r"[^.\n]{0,40}?(copyleft|GPL|AGPL|permissive|MIT|Apache)", re.I)

# a permissive grant cell: slug plus MIT/Apache in the same table row
PERMISSIVE_ROW = re.compile(
    r"\|[^|\n]*\[`?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)`?\]\([^)]*github\.com[^)]*\)"
    r"[^\n]*?\*\*(MIT|Apache-2\.0|BSD-[23]-Clause)\*\*", re.I)

LMSISH = re.compile(r"\b(LMS|learning platform|learning management)\b", re.I)


def scan(root):
    claims, permissive = [], {}
    for rel in SHELVES:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            continue
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            if CLAIM.search(line):
                claims.append((rel, n, line.strip()))
            m = PERMISSIVE_ROW.search(line)
            if m and LMSISH.search(line):
                permissive.setdefault(m.group(1), (rel, n, m.group(2)))
    return claims, permissive


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    claims, permissive = scan(root)

    print("── p515-class-claim: universal licence claims vs permissive LMS rows")
    print("   permissive LMS/platform rows found: %d" % len(permissive))
    for slug, (rel, n, lic) in sorted(permissive.items()):
        print("     🟢 %-34s %-12s %s:%d" % (slug, lic, rel, n))

    # A claim line is EXCUSED when it is a quotation of a claim under correction,
    # when it carries its own correction, or when it is explicitly scoped.
    EXCUSE = re.compile(
        r"^>|\bfalse\b|\brefut|\bwithdraw|\bcorrect(ed|ion)\b|\bis wrong\b|"
        r"\bthis window\b|\bthey front\b|\bfirst-hand\b|\bclaimed\b", re.I)

    copyleft_universals = [c for c in claims
                           if re.search(r"copyleft|GPL|AGPL", c[2], re.I)
                           and re.search(r"every|all\b", c[2], re.I)
                           and LMSISH.search(c[2])
                           and not EXCUSE.search(c[2].lstrip())]

    print("   universal licence claims found: %d (of which 'every/all ... copyleft' over an LMS class: %d)"
          % (len(claims), len(copyleft_universals)))

    if copyleft_universals and permissive:
        print("   🔴 A universal copyleft claim coexists with %d permissive row(s). Each claim below"
              % len(permissive))
        print("      must either carry a qualifier or be withdrawn:")
        for rel, n, line in copyleft_universals:
            print("      🔴 %s:%d" % (rel, n))
            print("         %s" % line[:200])
        return 1

    print("   🟢 PASS — no unqualified universal copyleft claim over a class that has permissive rows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
