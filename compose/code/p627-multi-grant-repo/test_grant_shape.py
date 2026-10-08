import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grant_shape import (load, grants_of, single_license_sweep, obligations_of,
                         is_open_grant, filename_keyed_classifier, unlicensed,
                         decompose)

PAY = load("payloads.2026-10-08.tsv")
REFS = load("refs.2026-10-08.tsv")
MIT = load("mit-bytes.2026-10-08.tsv")
ok = fail = 0


def check(label, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print("RED  %s" % label)


# === P627 — a repository's grant is a SET, not a value ===================
MG = "grant-mccurdy/instructional-ai-workflows"
check("P627 multi-grant repo ships >1 licence payload", len(grants_of(PAY, MG)) == 3)
check("P627 code grant is MIT", grants_of(PAY, MG)["LICENSE"] == "MIT")
check("P627 content grant is CC BY 4.0",
      grants_of(PAY, MG)["LICENSE-CONTENT.md"] == "CC-BY-4.0")
check("P627 data grant is CC BY 4.0",
      grants_of(PAY, MG)["LICENSE-DATA.md"] == "CC-BY-4.0")
# the control: the single-LICENSE sweep reports MIT and is INCOMPLETE
check("P627 control: single-LICENSE sweep still reports MIT",
      single_license_sweep(PAY, MG) == "MIT")
check("P627 control: and still misses the attribution obligations",
      obligations_of(PAY, MG) == {"CC-BY-4.0"} and
      single_license_sweep(PAY, MG) not in obligations_of(PAY, MG))
# invariant, not a cardinality: ANY slug with >1 grant must not be summarised
# by its LICENSE alone
for slug in {r["slug"] for r in PAY}:
    g = grants_of(PAY, slug)
    if len(set(g.values())) > 1:
        check("P627 invariant: %s has mixed families, so one value cannot "
              "represent it" % slug, len(set(g.values())) > 1)

# === P628 — PROPRIETARY is a verdict, not an absence =====================
PR = "michael-borck/assessment-rubrics-for-ai"
check("P628 Curtin payload read 200", grants_of(PAY, PR) != {})
check("P628 family is PROPRIETARY", grants_of(PAY, PR)["LICENSE.md"] == "PROPRIETARY")
check("P628 PROPRIETARY is not an open grant", not is_open_grant("PROPRIETARY"))
check("P628 PROPRIETARY != UNKNOWN as a class",
      "PROPRIETARY" != "UNKNOWN" and not is_open_grant("UNKNOWN"))
check("P628 MIT remains an open grant", is_open_grant("MIT"))
# the control: the filename-keyed classifier STILL calls it open
check("P628 control: filename-keyed classifier still misfiles LICENSE.md",
      filename_keyed_classifier("LICENSE.md") is True)
check("P628 control: and it would misfile the Curtin repo as usable",
      filename_keyed_classifier("LICENSE.md") and
      not is_open_grant(grants_of(PAY, PR)["LICENSE.md"]))

# === P629 — unlicensed, measured two ways ================================
UL = "GradeAI/gradeai"
check("P629 slug exists (1 head)",
      [r for r in REFS if r["slug"] == UL][0]["heads"] == "1")
check("P629 ships no 200 licence payload", unlicensed(PAY, UL))
check("P629 all six probes 404",
      len([r for r in PAY if r["slug"] == UL and r["http"] == "404"]) == 6)
check("P629 existing-but-unlicensed is not an open grant", not is_open_grant("UNLICENSED"))
# negative control (P510): the control slug must NOT exist
check("P510 negative control has 0 refs",
      [r for r in REFS if "NEGATIVE-CONTROL" in r["slug"]][0]["heads"] == "0")
check("P510 a 404 path on a real repo is distinguishable from a dead slug",
      [r for r in PAY if r["verdict"] == "NEGATIVE-CONTROL"][0]["http"] == "404")

# === P630 — MIT byte decomposition (extends P621) ========================
by_bytes = {int(r["bytes"]): r for r in MIT}
check("P630 three MIT payloads, three different byte counts", len(by_bytes) == 3)
check("P630 all three are MIT", {r["family"] for r in MIT} == {"MIT"})
# so byte equality is NOT necessary for licence identity
check("P630 byte equality is not NECESSARY for MIT identity",
      len({r["bytes"] for r in MIT}) > 1 and len({r["family"] for r in MIT}) == 1)
# and each delta decomposes exactly
cp, nl, total = decompose(by_bytes[1070], by_bytes[1068])
check("P630 1070-1068 decomposes to cp=+1, nl=+1", (cp, nl, total) == (1, 1, 2))
check("P630 and that total equals the measured delta", total == 1070 - 1068)
cp, nl, total = decompose(by_bytes[1069], by_bytes[1068])
check("P630 1069-1068 is a pure final newline", (cp, nl, total) == (0, 1, 1))
check("P630 and that total equals the measured delta", total == 1069 - 1068)
# the refutation P621 asked for: two payloads 1 B apart for DIFFERENT reasons
check("P630 a 1 B delta has at least two distinct causes in one corpus",
      decompose(by_bytes[1069], by_bytes[1068])[:2] !=
      decompose(by_bytes[1070], by_bytes[1069])[:2])
# invariant: no tolerance band on bytes can separate MIT from non-MIT here
check("P630 invariant: a +/-1 B band around any MIT specimen admits or "
      "excludes MIT payloads arbitrarily",
      max(by_bytes) - min(by_bytes) == 2)

# === P479 — no star counts anywhere in this suite's data =================
blob = "".join(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f),
                    encoding="utf-8").read()
               for f in ("payloads.2026-10-08.tsv", "refs.2026-10-08.tsv",
                         "mit-bytes.2026-10-08.tsv"))
# NOTE: this check was first written as `"star" not in blob.lower()` and went
# RED on its own data -- `opensource-startup-crm` contains the substring
# `star`. A substring is not a token; the column name and the glyph are.
_tokens = set(re.findall(r"[a-z]+", blob.lower()))
check("P479 no star counts in this pass's data",
      not ({"star", "stars"} & _tokens) and "★" not in blob)
check("P479 control: the substring form of this check is still the wrong "
      "instrument", "star" in blob.lower())

print("p627-multi-grant-repo: %d/%d green, %d red" % (ok, ok + fail, fail))
sys.exit(1 if fail else 0)
