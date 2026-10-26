#!/usr/bin/env python3
"""Controls for the rebuilt family reader. Every assertion is a payload read
first-hand at HEAD this pass, or a value an earlier pass published.

Run in BOTH directions, because each of this pass's two reader defects was a
verdict firing where it should not AND failing to fire where it should."""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def load(n, p):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s)
    sv = sys.argv; sys.argv = [sv[0]]; s.loader.exec_module(m); sys.argv = sv; return m

new = load("f", os.path.join(HERE, "family_title.py"))
old = load("v", os.path.abspath(os.path.join(HERE, "..", "p453-vocabulary-ledger", "verify.py")))

F = []
def check(n, got, want):
    ok = (got == want) if not callable(want) else want(got)
    print(f"  {'OK  ' if ok else 'FAIL'} {n:54s} got={got!r}")
    if not ok:
        F.append(n); print(f"       want={want!r}")

def body(slug, path="LICENSE"):
    b, c, s = old.fetch(f"https://raw.githubusercontent.com/{slug}/HEAD/{path}")
    assert c == "200", f"{slug}/{path} -> HTTP {c}"
    return b

print("=== defect 1: GPLv2 must NOT grade LGPL, GPLv3 must NOT either ===")
check("oat-sa/tao-core (GPL-2.0 payload)", new.family(body("oat-sa/tao-core")), "GPL")
check("  ...and the old reader got it wrong", old.family(body("oat-sa/tao-core")), "LGPL")
# A real LGPL payload must STILL grade LGPL -- the fix must not over-correct.
check("caliper-php-public (LGPL-3.0 payload)",
      new.family(body("tl-its-umich-edu/caliper-php-public")), "LGPL")
# A real AGPL payload must still grade AGPL (p453 published this one).
check("nodetool-ai/nodetool (AGPL-3.0 payload)",
      new.family(body("nodetool-ai/nodetool", "LICENSE.txt")), "AGPL-3.0")

print("\n=== defect 2: a composite is DISTINCT FAMILIES, not a heading count ===")
check("bncc-pacotes -> composite naming BOTH halves",
      new.family(body("bncc-dev/bncc-pacotes")),
      lambda g: g.startswith("COMPOSITE") and "MIT" in g and "CC-BY" in g)
check("  ...old reader kept only the CC half",
      old.family(body("bncc-dev/bncc-pacotes")), "CC-BY-4.0")
check("aksara is NOT a composite (15 numbered sections, one licence)",
      new.family(body("nakafaai/aksara")), lambda g: not g.startswith("COMPOSITE"))

print("\n=== the class both defects hid: a payload that is not a licence ===")
check("aksara -> NOT-OSI, named", new.family(body("nakafaai/aksara")),
      lambda g: g.startswith("NOT-OSI") and "Nakafa Source Available" in g)
check("  ...both earlier readers said UNREAD", old.family(body("nakafaai/aksara")), "UNREAD")
check("nakafa.com -> same grant, same verdict",
      new.family(body("nakafaai/nakafa.com")), lambda g: g.startswith("NOT-OSI"))
check("Nakafa CONTENT_LICENSE -> NOT-OSI too",
      new.family(body("nakafaai/aksara", "CONTENT_LICENSE.md")),
      lambda g: g.startswith("NOT-OSI"))

print("\n=== over-correction controls: permissive payloads must be UNCHANGED ===")
for slug, path, want in [("food-x-technologies/escolar", "LICENSE", "MIT"),
                         ("bolewood/collegedata-fyi", "LICENSE", "MIT"),
                         ("scaler-opensource/exam-guard", "LICENSE", "Apache-2.0")]:
    b = body(slug, path)
    check(f"{slug} unchanged", (new.family(b), old.family(b)), (want, want))

print()
if F:
    print(f"RED: {len(F)} control(s) failed: {F}"); sys.exit(1)
print("GREEN: all controls pass, both directions")

print("\n=== defect 3 (this pass's own): 'all rights reserved' is MIT boilerplate ===")
# node-extsprintf opens "All rights reserved." and then GRANTS MIT. The first
# cut of the NOT-OSI class condemned it on that line alone.
check("node-extsprintf is MIT, not NOT-OSI",
      new.family(body("davepacheco/node-extsprintf")), "MIT (body form, no title)")
# dofek opens the same way and then REFUSES permission. It must still be caught,
# so the fix must not be a blanket retreat.
check("dofek REFUSES permission -> NOT-OSI",
      new.family(body("asherlc/dofek")), lambda g: g.startswith("NOT-OSI"))
check("  ...and the old reader missed it", old.family(body("asherlc/dofek")), "UNREAD")

print()
if F:
    print(f"RED: {len(F)} control(s) failed: {F}"); sys.exit(1)
print("GREEN: all controls pass, both directions (incl. defect 3)")

print("\n=== defect 4 (this pass's own): a pointer is not a refusal ===")
check("ckeditor5 root LICENSE.md -> POINTER_IN_REPO",
      new.family(body("ckeditor/ckeditor5", "LICENSE.md")),
      lambda g: g.startswith("POINTER_IN_REPO") and "packages/ckeditor5/LICENSE.md" in g)
check("  ...and the repo really does serve a GPL payload",
      new.family(body("ckeditor/ckeditor5", "COPYING.GPL")), "GPL")
# The pointer class must NOT swallow a real licence that happens to say "see".
check("GPLv2 payload is not a pointer",
      new.family(body("oat-sa/tao-core")), "GPL")
check("aksara (11 997 B) is too long to be a pointer",
      new.family(body("nakafaai/aksara")), lambda g: g.startswith("NOT-OSI"))
check("dofek still NOT-OSI (names a per-directory override, is not a pointer)",
      new.family(body("asherlc/dofek")), lambda g: g.startswith("NOT-OSI"))

print("\n=== Gap 453-E (d) reproduced live: a 404 body is 14 bytes ===")
_b, _c, _s = old.fetch("https://raw.githubusercontent.com/ckeditor/ckeditor5/HEAD/LICENSE")
check("404 body size", (_c, _s), ("404", 14))
check("  ...and it is a body a byte-reader would have believed",
      _b.strip(), "404: Not Found")

print()
if F:
    print(f"RED: {len(F)} control(s) failed: {F}"); sys.exit(1)
print("GREEN: all controls pass, both directions (incl. defects 3 and 4)")
