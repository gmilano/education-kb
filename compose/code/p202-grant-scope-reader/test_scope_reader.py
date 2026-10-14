#!/usr/bin/env python3
"""p202 — suite for the scope reader. OFFLINE.

The loaded case is `ACTION OR`'s falsifier: pupilfirst and leemons build their
notice from the SAME template, and the suite fails if the reader cannot tell
them apart. Read the fixtures' PROVENANCE.tsv before trusting a byte figure
from them -- only leemons.LICENSE.md is a complete file.
"""
import sys
sys.path.insert(0, ".")
from scope_reader import (classify, fallback_grant, has_split_scope_preamble,
                          scopes, content_family, non_osi_family)

checks = 0
fails = 0


def ck(cond, name):
    global checks, fails
    checks += 1
    print(("ok   " if cond else "FAIL ") + name)
    if not cond:
        fails += 1


leemons = open("fixtures/leemons.LICENSE.md").read()
pupil = open("fixtures/pupilfirst.LICENSE.head").read()
hst = open("fixtures/human-skill-tree.LICENSE.scope").read()

# --- THE LOADED CASE: same template, opposite grants ---
ck(has_split_scope_preamble(leemons), "leemons announces split scope")
ck(has_split_scope_preamble(pupil), "pupilfirst announces split scope")
ck(fallback_grant(leemons) == "Fair code License",
   "leemons fallback == 'Fair code License' (got %r)" % fallback_grant(leemons))
ck(fallback_grant(pupil) == "MIT",
   "pupilfirst fallback == 'MIT' (got %r)" % fallback_grant(pupil))
ck(fallback_grant(leemons) != fallback_grant(pupil),
   "ACTION OR FALSIFIER: the shared template does NOT defeat the reader")
ck(non_osi_family(fallback_grant(leemons)) == "FAIRCODE",
   "leemons fallback is named non-OSI")
ck(non_osi_family(fallback_grant(pupil)) is None,
   "pupilfirst fallback is not flagged non-OSI")

# --- the code/content split, which a repo-level column hides ---
cp = classify(pupil)
ck(cp["code_content_split"] is True,
   "pupilfirst: content scope under CC + code fallback under MIT == split")
ck(("docs/", "CC-BY-SA") in cp["scopes"],
   "pupilfirst docs/ reads as CC-BY-SA (got %r)" % (cp["scopes"],))
ck(any(g == "UPSTREAM-OWN" for _, g in cp["scopes"]),
   "a third-party bullet is read as UPSTREAM-OWN, not as a grant")

cl = classify(leemons)
ck(cl["code_content_split"] is False,
   "leemons has no CC content scope, so no code/content split")

# --- human-skill-tree: a path that is MORE permissive than the repo ---
sh = dict((s, g) for s, g in scopes(hst))
ck("skills/" in sh, "skills/ is read as a scope (got %r)" % (sh,))
ck(sh.get("skills/") == "AGPL-3.0-OR-MIT",
   "P202 REGRESSION: skills/ keeps BOTH limbs of the dual grant (got %r)"
   % sh.get("skills/"))
ck(sh.get("app/") == "AGPL-3.0",
   "app/ is AGPL-3.0 only -- the dual grant does NOT leak to it (got %r)"
   % sh.get("app/"))
ck("MIT" in (sh.get("skills/") or ""),
   "the shippable limb is visible on skills/, which is what decides a deliverable")

# --- content families, named not guessed ---
ck(content_family("Creative Commons CC BY-SA 4.0") == "CC-BY-SA", "CC-BY-SA named")
ck(content_family("CC BY-NC-ND 4.0") == "CC-BY-NC", "NonCommercial named first")
ck(content_family("MIT") is None, "MIT is not a content licence")
ck(content_family("Apache-2.0") is None, "Apache-2.0 is not a content licence")

# --- silence is never a grant ---
ck(fallback_grant("this project is open source") is None,
   "no fallback clause -> None, not a guess")
ck(classify("")["fallback"] is None, "empty notice -> no fallback")
ck(has_split_scope_preamble("MIT License\n\nCopyright (c) 2026") is False,
   "a plain MIT notice does not announce split scope")

# --- the regression that matters for P237: this module does NOT name families ---
ck(not hasattr(sys.modules["scope_reader"], "family_of"),
   "scope_reader does not reimplement family_of (that is lib/license_family.sh)")

print()
print("%d/%d" % (checks - fails, checks))
sys.exit(1 if fails else 0)
