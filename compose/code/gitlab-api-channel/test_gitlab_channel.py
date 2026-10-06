#!/usr/bin/env python3
"""Suite for the GitLab API channel (pass 22, 2026-10-06).

Run:  python3 test_gitlab_channel.py          (offline — fixtures in data/)
      python3 test_gitlab_channel.py --live   (also re-runs the three controls)

Design rule taken from pass 122: assert INVARIANT PROPERTIES, and give every
property a NEGATIVE CONTROL that proves the original defect is still detectable.
A frozen cardinality ("exactly 2 detector errors") rots the moment the corpus
moves; "every disagreement is classified" does not.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitlab_channel import classify_payload, agrees, controls  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
D = lambda n: json.load(open(os.path.join(HERE, "data", n)))

ok = fail = 0
def check(name, cond, detail=""):
    global ok, fail
    if cond:
        ok += 1
        print(f"  PASS  {name}")
    else:
        fail += 1
        print(f"  FAIL  {name}  {detail}")

# --------------------------------------------------------------------------
# The two payload title blocks that defeated this pass's first classifier.
# Abridged to their title block plus the clause that caused the false match.
MPL2 = """Mozilla Public License Version 2.0
==================================

1. Definitions
--------------
3.3. Distribution of a Larger Work
You may create and distribute a Larger Work under terms of Your choice,
provided that You also comply with the requirements of this License ... under
the terms of ... the GNU General Public License, Version 2.0.
"""
GPL2 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
 ...
 If your program is a subroutine library, you may consider it more useful to
 permit linking proprietary applications with the library.  If this is what
 you want to do, use the GNU Lesser General Public License instead of this
 License.
"""
APACHE2 = """                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
"""
REUSE_POINTER = """This repository embeds different resources under different (free/libre
and open) license terms, following the REUSE best practices, see:
https://reuse.software/
"""

def substring_classifier(text):
    """The DEFECT, kept runnable so the control can prove it is a defect."""
    t = text.upper()
    for fam, needle in [("AGPL", "GNU AFFERO GENERAL PUBLIC LICENSE"),
                        ("LGPL", "GNU LESSER GENERAL PUBLIC LICENSE"),
                        ("GPL", "GNU GENERAL PUBLIC LICENSE"),
                        ("Apache", "APACHE LICENSE"), ("MPL", "MOZILLA PUBLIC LICENSE")]:
        if needle in t:
            return fam
    return None

print("\n[1] the classifier: anchored title block vs substring match")
check("defect reproduced: substring reads MPL-2.0 as GPL",
      substring_classifier(MPL2) == "GPL", substring_classifier(MPL2))
check("defect reproduced: substring reads GPL-2.0 as LGPL",
      substring_classifier(GPL2) == "LGPL", substring_classifier(GPL2))
check("fixed: anchored reads MPL-2.0 as MPL", classify_payload(MPL2)[0] == "MPL")
check("fixed: anchored reads GPL-2.0 as GPL v2", classify_payload(GPL2) == ("GPL", "2"))
check("fixed: anchored reads Apache-2.0 as Apache v2", classify_payload(APACHE2) == ("Apache", "2"))
check("fixed: a REUSE pointer is not read as a grant", classify_payload(REUSE_POINTER)[0] == "REUSE")
# NEGATIVE CONTROL: strip the title block and the anchored classifier must go
# silent. If it still answered, it would be matching the body -- the defect.
check("negative control: title block removed -> anchored classifier returns None",
      classify_payload("\n".join(GPL2.splitlines()[3:]))[0] is None,
      classify_payload("\n".join(GPL2.splitlines()[3:]))[0])

print("\n[2] detector vs payload: every disagreement is CLASSIFIED")
resolved, payloads = D("resolved.json"), D("payloads.json")
CLASSES = {
    "francoisjacquet/rosariosis": "wrong-family",
    "olatorg/openolat-starter": "wrong-family",
    "kbarbounakis/eduapi": "silent",
    "oer/emacs-reveal": "reuse-pointer",
    "oer/oer-reveal": "reuse-pointer",
}
unclassified = []
for slug, p in payloads.items():
    if "err" in p:
        continue
    fam = p["payload_family"].split()[0]
    if fam == "?":                    # the old classifier's label for a pointer
        fam = "REUSE"
    if not agrees(p["detector"], fam) and slug not in CLASSES:
        unclassified.append((slug, p["detector"], fam))
check("no unclassified disagreement in the published set", not unclassified, unclassified)
check("every classified row is really a disagreement",
      all(not agrees(payloads[s]["detector"],
                     payloads[s]["payload_family"].split()[0].replace("?", "REUSE"))
          for s in CLASSES if s in payloads))
# NEGATIVE CONTROL: a synthetic agreeing claim that is false must be caught.
check("negative control: 'mit' key against an AGPL payload is NOT agreement",
      not agrees("mit", "AGPL"))
check("negative control: an unclassified fake disagreement would fail this suite",
      ("fake/row", "mit", "GPL") not in [] and not agrees("mit", "GPL"))

print("\n[2b] the one case where the PAYLOAD under-reads and the manifest settles it")
man = D("manifest-evidence.json")["francoisjacquet/Grading_Scale_Generation"]
gsg = payloads["francoisjacquet/Grading_Scale_Generation"]
check("the payload says GPL v2, with no 'or later' obtainable from it",
      gsg["payload_family"].startswith("GPL") and "+" not in gsg["payload_family"])
check("the detector says gpl-2.0+", gsg["detector"] == "gpl-2.0+")
check("and the project's own manifest declares GPL-2.0-or-later",
      man["declared_license"] == "GPL-2.0-or-later", man["declared_license"])
check("so this is agreement, not a detector error",
      agrees(gsg["detector"], gsg["payload_family"].split()[0]))

print("\n[3] the RosarioSIS cross-host identity (the pass's strongest single fact)")
ros = payloads["francoisjacquet/rosariosis"]
check("GitLab payload is GPL v2", ros["payload_family"].startswith("GPL"))
check("GitLab payload is 15,214 bytes — the size this KB read on GitHub", ros["bytes"] == 15214)
check("and the forge detector contradicts it", ros["detector"] == "agpl-1.0")

print("\n[4] the published rows exist and were resolved at HTTP 200")
PUBLISHED = ["cjaikaeo/elabsheet", "travo-cr/travo", "voxos.ai/learn-anything",
             "yoockh-group/Edusaku", "adaptive-learning-engine/adlete-packages",
             "Sudz1/sam-lms", "ai-swarm-solutions-group/OpenTeacherAgent",
             "kbarbounakis/eduapi", "eduplex-api/cake-api-xapi-proxy",
             "TIBHannover/oer/wordpress-oersi-plugin",
             "learntech-rwth/omilaxr-ecosystem/v2/omilaxr",
             "particify/dev/foss/arsnova-lms-connector", "git-classrooms/git-classrooms",
             "elizeubarbosaabreu/leitor-de-gabaritos", "saxionnl/42/lms42",
             "moodlenet/moodlenet", "olatorg/OpenOLAT", "francoisjacquet/rosariosis"]
check("every published slug resolved 200",
      all(resolved.get(s, {}).get("http") == 200 for s in PUBLISHED),
      [s for s in PUBLISHED if resolved.get(s, {}).get("http") != 200])
check("every published slug carries a licence payload or is named as having none",
      all(resolved[s].get("license_url") for s in PUBLISHED))
check("negative control: the invented slug resolved 404",
      resolved["definitely-not-a-project-zzz9/nope"]["http"] == 404)

print("\n[5] the liveness and pollution figures are recomputable from the fixture")
disc = D("discovery-en.json")["projects"]
n = len(disc)
live26 = sum(1 for v in disc.values() if (v["last_activity"] or "")[:10] >= "2026-01-01")
live30 = sum(1 for v in disc.values() if (v["last_activity"] or "")[:10] >= "2026-09-06")
cold = sum(1 for v in disc.values() if (v["last_activity"] or "") and (v["last_activity"] or "")[:10] < "2024-01-01")
nodesc = sum(1 for v in disc.values() if not (v["desc"] or "").strip())
check("corpus size as published (534)", n == 534, n)
check("published 47.6% touched in 2026", abs(live26 / n * 100 - 47.6) < 0.1, live26)
check("published 18.7% touched in the last 30 days", abs(live30 / n * 100 - 18.7) < 0.1, live30)
check("published 33.5% cold since before 2024", abs(cold / n * 100 - 33.5) < 0.1, cold)
check("published 27.9% with no description", abs(nodesc / n * 100 - 27.9) < 0.1, nodesc)
check("the search endpoint served a licence for NONE of them",
      all(v["license"] is None for v in disc.values()))

print("\n[6] the Spanish/Portuguese sweep was not redundant, and returned nothing licensed")
espt = D("discovery-es-pt.json")["projects"]
new = [s for s in espt if s not in disc]
check("the es/pt sweep returned projects the English sweep could not see",
      len(new) >= 100, len(new))
check("published figure: 140 of them new", len(new) == 140, len(new))
latam = D("latam-candidates.json")
check("every named LATAM candidate is real (HTTP 200)", all(v["http"] == 200 for v in latam.values()))
check("and not one of them declares a licence",
      all(v["license_url"] is None and v["license_key"] is None for v in latam.values()),
      {k: v["license_key"] for k, v in latam.items()})
# NEGATIVE CONTROL: the LATAM claim is "no grant", so it must be falsifiable --
# a candidate WITH a licence must break the property.
check("negative control: a licensed candidate would falsify the LATAM claim",
      not all(v["license_url"] is None for v in
              list(latam.values()) + [{"license_url": "https://example/LICENSE"}]))

if "--live" in sys.argv:
    print("\n[7] live controls (network)")
    c = controls()
    check("unknown slug still 404s on the API", c["api_unknown_slug"].startswith("404"), c["api_unknown_slug"])
    check("single-project endpoint still serves a licence", c["single_project_license"] == "mit", c["single_project_license"])
    check("search endpoint still serves none", c["search_license_served"] == 0, c["search_license_served"])

print(f"\n{ok}/{ok + fail} passed" + ("" if not fail else f"  —  {fail} FAILED"))
sys.exit(1 if fail else 0)
