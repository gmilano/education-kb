#!/usr/bin/env python3
"""p454 controls. Every one asserts a value an EARLIER pass already published,
so a defect in this pass's instrument fails against prior evidence rather than
against this pass's own output (Gap 453-E's stated remedy: three of its four
defects were caught only that way).

Run BOTH directions: a verdict class that cannot fire reads as "no project ever
did this" (Gap 452 defect (e), which reappeared verbatim in p453).
"""
import importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("vs", os.path.join(HERE, "value_sweep.py"))
vs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vs)

FAILED = []

def check(name, got, want):
    ok = got == want
    print(f"  {'OK  ' if ok else 'FAIL'} {name:58s} got={got!r:38s} want={want!r}")
    if not ok:
        FAILED.append(name)

print("=== canon() -- asserted against values p453 PUBLISHED ===")
# p453's declared-vs-payload.tsv carries these declared strings verbatim.
check("canon('MIT')", vs.canon("MIT"), "MIT")
check("canon('MIT License')", vs.canon("MIT License"), "MIT")
check("canon('Apache License 2.0')", vs.canon("Apache License 2.0"), "APACHE-2.0")
check("canon('Apache-2.0')", vs.canon("Apache-2.0"), "APACHE-2.0")
check("canon('BSD-3-Clause')", vs.canon("BSD-3-Clause"), "BSD-3-CLAUSE")
check("canon('GNU Affero General Public License v3')",
      vs.canon("GNU Affero General Public License v3"), "AGPL-3.0")
check("canon('GNU Lesser General Public License v3 (LGPLv3)')",
      vs.canon("GNU Lesser General Public License v3 (LGPLv3)"), "LGPL")
check("canon('GNU General Public License v3 or later (GPLv3+)')",
      vs.canon("GNU General Public License v3 or later (GPLv3+)"), "GPL")
check("canon('GPL-2.0-only')", vs.canon("GPL-2.0-only"), "GPL")
check("canon('LGPL-3.0')", vs.canon("LGPL-3.0"), "LGPL")
check("canon('MPL-2.0')", vs.canon("MPL-2.0"), "MPL-2.0")
check("canon('ISC')", vs.canon("ISC"), "ISC")
# Gap 451-C's live instance, byte-identical across two registries.
check("canon('SEE LICENSE IN LICENSE')",
      vs.canon("SEE LICENSE IN LICENSE"), "POINTER-OUT-OF-REGISTRY")
check("canon('proprietary')", vs.canon("proprietary"), "PROPRIETARY")
check("canon('') -- registry silent", vs.canon(""), "")
# NEGATIVE direction: an AGPL string must NOT collapse onto GPL, or p453's one
# load-bearing DISAGREE (MIT declared over AGPL served) becomes invisible.
check("canon('AGPL-3.0') != canon('GPL-2.0-only')",
      vs.canon("AGPL-3.0") != vs.canon("GPL-2.0-only"), True)
check("canon('LGPL-3.0') != canon('GPL-2.0-only')",
      vs.canon("LGPL-3.0") != vs.canon("GPL-2.0-only"), True)

print("\n=== family() -- title-anchored, asserted against p453's published payloads ===")
# nodetool-ai/nodetool: p453 published AGPL-3.0, LICENSE.txt 34522 B 4df3c306ddda.
p, f, n, s, _ = vs.payload_of("github.com/nodetool-ai/nodetool")
check("nodetool payload family", f, "AGPL-3.0")
check("nodetool payload bytes", n, 34522)
check("nodetool payload sha256_12", s, "4df3c306ddda")
# food-x-technologies/escolar: p453 published MIT, 1075 B 3b443e863252.
p, f, n, s, _ = vs.payload_of("github.com/food-x-technologies/escolar")
check("escolar payload family", f, "MIT")
check("escolar payload bytes", n, 1075)
check("escolar payload sha256_12", s, "3b443e863252")
# bolewood/collegedata-fyi: p453 published MIT 1115 B a3a16c648652.
p, f, n, s, _ = vs.payload_of("github.com/bolewood/collegedata-fyi")
check("collegedata-fyi payload bytes", n, 1115)
check("collegedata-fyi payload sha256_12", s, "a3a16c648652")

print("\n=== negative controls -- a verdict that cannot fire is not a verdict ===")
# A fabricated address must be NO_PAYLOAD, not a phantom grant (Gap 453-E (d)).
p, f, n, s, _ = vs.payload_of("github.com/nope-xyz-123-p454/nope-xyz-123-p454")
check("fabricated slug -> NO_PAYLOAD", f, "NO_PAYLOAD")
check("fabricated slug -> 0 bytes", n, 0)
# An unsupported forge must be named, not silently graded absent.
p, f, n, s, _ = vs.payload_of("codeberg.org/does-not/matter")
check("unsupported forge -> FORGE_UNSUPPORTED", f, "FORGE_UNSUPPORTED")
# A gitlab address must reach gitlab's raw endpoint, NOT raw.githubusercontent.
p, f, n, s, _ = vs.payload_of("gitlab.com/travo-cr/travo")
check("gitlab forge reader reaches a payload", f != "NO_PAYLOAD", True)
# DISAGREE must be reachable: construct one by hand from the grader's own logic.
row = ["npm", "ctl-pkg", "AGREE", "", "", "MIT", "1.0.0", "github.com/nodetool-ai/nodetool"]
check("DISAGREE class is reachable", vs.grade(row)[9], "DISAGREE")
row = ["npm", "ctl-pkg", "AGREE", "", "", "AGPL-3.0", "1.0.0", "github.com/nodetool-ai/nodetool"]
check("AGREE class is reachable", vs.grade(row)[9], "AGREE")
row = ["npm", "ctl-pkg", "AGREE", "", "", "SEE LICENSE IN LICENSE", "1.0.0",
       "github.com/food-x-technologies/escolar"]
check("POINTER class is reachable", vs.grade(row)[9], "POINTER")
row = ["npm", "ctl-pkg", "AGREE", "", "", "MIT", "1.0.0",
       "github.com/nope-xyz-123-p454/nope-xyz-123-p454"]
check("MANIFEST_ONLY class is reachable", vs.grade(row)[9], "MANIFEST_ONLY")
row = ["npm", "ctl-pkg", "ABSENT", "", "", "MIT", "1.0.0", ""]
check("NO_ADDRESS class is reachable", vs.grade(row)[9], "NO_ADDRESS")

print()
if FAILED:
    print(f"RED: {len(FAILED)} control(s) failed: {FAILED}")
    sys.exit(1)
print("GREEN: all controls pass, both directions")
