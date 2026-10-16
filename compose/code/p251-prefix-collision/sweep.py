"""`ACTION XN`'s runner: the prefix-collision sweep over the shelves.

    python3 sweep.py <shelf.md> [...]      # TSV on stdout, counts on stderr
"""
import os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prefix_collision import collisions

print("\t".join(["shelf", "short", "long", "class", "continuation", "verdict",
                 "bare_lines", "short_published_as_url"]))
counts = collections.Counter()
for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    for r in collisions(text):
        counts[r["verdict"]] += 1
        print("\t".join([path, r["short"], r["long"], r["class"], r["continuation"],
                         r["verdict"], ",".join(map(str, r["bare_lines"][:8])) or "-",
                         "yes" if r["short_published_as_url"] else "no"]))
print("## " + "  ".join("%s=%d" % kv for kv in sorted(counts.items())), file=sys.stderr)
