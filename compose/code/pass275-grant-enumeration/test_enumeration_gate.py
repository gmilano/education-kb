#!/usr/bin/env python3
"""p275 — tests for the enumeration gate.

Runs from THIS directory (p229/p355-cwd-portability: `python3 -I` strips the script's
directory from sys.path, so a suite that imports its subject must be invoked from beside
it — every Makefile recipe on this base `cd`s in first).
"""
import sys

from enumeration_gate import (ABSENT_KEY, NEGATIVE, RETRACTION, attribute,
                               candidate_grants, states_a_grant)

FAILED = []


def check(name, got, want):
    if got != want:
        FAILED.append(f"{name}: got {got!r}, want {want!r}")


# --- candidate_grants: a licence-like path is not automatically a grant ----------------
check("root LICENSE is a grant",
      candidate_grants(["LICENSE"]), ["LICENSE"])
check("the openSIS grant the 19-path ladder never tried",
      candidate_grants(["docs/License.txt", "docs/LICENSE.rtf"]),
      ["docs/License.txt", "docs/LICENSE.rtf"])
check("NONE_IN_TREE yields nothing",
      candidate_grants(["NONE_IN_TREE"]), [])
check("vendored dependency licences are NOT the repo's grant",
      candidate_grants(["custompackages/brozot/laravel-fcm/LICENSE",
                        "libraries/htmlpurifier/LICENSE",
                        "assets/js/plugins/editors/ckeditor/LICENSE.md"]), [])
check("kolibri-design-system's 7 hits are Vue ICONS, not grants",
      candidate_grants(["lib/KIcon/precompiled-icons/mdi/license.vue",
                        "lib/KIcon/precompiled-icons/material-icons/copyright/baseline.vue"]), [])
check("a Java class named LicenseService is not a grant",
      candidate_grants(["src/main/java/de/tum/cit/aet/artemis/"
                        "programming/service/LicenseService.java"]), [])
check("a root LICENSE is still found alongside vendored noise",
      candidate_grants(["LICENSE", "vendor/foo/LICENSE"]), ["LICENSE"])

# --- attribute: one line, two subjects -------------------------------------------------
LEDGER = ["ls1intum/Athena", "ls1intum/Artemis", "os4ed/openSIS-Classic"]

artemis_row = ("| [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | 819 | "
               "ships Iris, Pyris and [`ls1intum/Athena`](https://github.com/ls1intum/Athena), "
               "**licence UNVERIFIED — no payload**) |")
check("an MIT row does not refute itself via a phrase about another slug",
      attribute(artemis_row, LEDGER), ["ls1intum/Athena"])

prose_row = ("| **Artemis** | [ls1intum/Artemis](https://github.com/ls1intum/Artemis) | MIT | "
             "**Iris** (MIT), **Athena** (feedback suggestion, **licence UNVERIFIED**) |")
check("a PROSE subject is attributed, not the row's only hyperlink",
      attribute(prose_row, LEDGER), ["ls1intum/Athena"])

osis_row = ("| [os4ed/openSIS-Classic](https://github.com/os4ed/openSIS-Classic) | GPL-2.0 SIS | "
            "Resolves, but **no licence payload served** on any path tried. |")
check("the true positive is still reported",
      attribute(osis_row, LEDGER), ["os4ed/openSIS-Classic"])
check("a line with no project named yields nothing",
      attribute("no licence payload anywhere", []), [])

# --- the regexes themselves ------------------------------------------------------------
check("British spelling is caught (p267's lesson)",
      bool(NEGATIVE.search("no licence payload")), True)
check("American spelling is caught",
      bool(NEGATIVE.search("no license payload")), True)
check("a retraction is recognised as narration, not a live claim",
      bool(RETRACTION.search("🔴 RETRACTED. 12 of 14 manifests declare MIT")), True)
check("an ordinary negative verdict is NOT read as a retraction",
      bool(RETRACTION.search("no licence payload served on any path tried")), False)

check("an append-only cell annotated with a dated supersede marker is narration",
      bool(RETRACTION.search(
          "no licence payload served on any path tried. "
          "— 🔴 SUPERSEDED 2026-10-17 (p275): the grant is at docs/License.txt")), True)
check("'superseded' does not leak into the negative vocabulary",
      bool(NEGATIVE.search("SUPERSEDED 2026-10-17")), False)

check("a POSSESSIVE mention is a modifier, not the subject",
      attribute("| Athena | [ls1intum/Athena](https://github.com/ls1intum/Athena) | MIT | "
                "**Artemis's feedback-suggestion engine** ... retracts "
                "'treat as all-rights-reserved' |", LEDGER), ["ls1intum/Athena"])
check("a non-possessive mention is still a candidate subject",
      attribute("**Artemis** ships it, licence UNVERIFIED", LEDGER), ["ls1intum/Artemis"])
check("the retraction STEM matches 'retracts', not just 'RETRACTED'",
      bool(RETRACTION.search("it retracts this base's earlier verdict")), True)

check("a DEAD slug does not own a claim about the real repo of the same basename",
      attribute("| **GegoK12** | 🔴 NOT ESTABLISHED. No licence payload on 15 "
                "path/ref combinations. |", ["Gego-K12/gegok12"]), ["Gego-K12/gegok12"])

# --- states_a_grant: a line that publishes the grant is correcting, not claiming --------
check("quoting an old refusal WHILE publishing the grant is a correction",
      states_a_grant('| openSIS-Classic | "no licence payload served on any path tried" '
                     '| docs/License.txt — verbatim GPL-2.0, 200, 17 286 B |'), True)
check("a bare negative verdict naming NO grant is still a live claim",
      states_a_grant("Resolves, but no licence payload was served on any path tried."), False)
check("an SPDX token alone does not silence a row",
      states_a_grant("Commonly cited as GPL-2.0; no payload on any path tried."), False)
check("a manifest-declared grant counts as evidence",
      states_a_grant('treat as all-rights-reserved — but 12 of 14 manifests declare MIT'), True)

check("a VENDOR's marketing prose naming a licence is NOT grant evidence",
      states_a_grant('*"free core is free forever under the MIT licence; 26 of 38 modules '
                     'free"* — a vendor listing | NOT ESTABLISHED. No licence payload on '
                     '15 path/ref combinations.'), False)
check("the bare FILENAME in caps still counts",
      states_a_grant("MIT at LICENSE, read this pass"), True)

# --- C3: the POSITIVE control, borrowed from P275's own doctrine ----------------------
# `sweep_tree.sh` (pase 93): "un instrumento que no reproduce un positivo conocido no
# sostiene una ausencia."  These are the two grants p275 read FIRST-HAND at payload, so
# the predicate must find both -- otherwise none of its VERIFIED-ABSENT rows mean anything.
check("C3 positive control: the known root grant is found",
      candidate_grants(["LICENSE", "custompackages/brozot/laravel-fcm/LICENSE"]), ["LICENSE"])
check("C3 positive control: the known docs/ grant is found",
      candidate_grants(["docs/License.txt", "assets/js/plugins/editors/ckeditor/LICENSE.md"]),
      ["docs/License.txt"])
check("C3 negative arm: an enumerated empty tree yields no grant",
      candidate_grants([]), [])

# ======================================================================================
# p276 — controls for the four defects found by WORKING p275's own backlog.
# Every one of these is a measured instance, not a hypothetical: 30 queue rows enumerated
# in two channels, ledger `evidence/tree-enumeration.2026-10-17-p276.tsv`.
# ======================================================================================

# --- D5: bare-name attribution had no specificity test --------------------------------
# Enumerating `frappe/lms` attributed FOURTEEN lines across FIVE shelves to it; THIRTEEN
# were about other projects.  `\b` does not stop at a hyphen and re.I made a noun a name.
LMS = ["frappe/lms"]
# NB: the phrase must be one NEGATIVE actually matches -- "no licence statement" is not in
# that vocabulary, so the real shelf line's own wording is used here.
check("D5: a hyphen-suffixed name is NOT a mention of the short basename",
      attribute("[DMontgomery40/mcp-canvas-lms](https://github.com/DMontgomery40/mcp-canvas-lms) "
                "| **NONE** — no licence statement in README | **Do not use.** "
                "No licence = all rights reserved.", LMS),
      ["DMontgomery40/mcp-canvas-lms"])
check("D5: a common noun in prose is not a repository name",
      attribute("the LMS-side MCP servers, and a re-probe of every 'no licence payload' row", LMS),
      [])
check("D5: an uppercase acronym inside another slug is not a mention",
      attribute("[`alfredang/AI-LMS-TMS`](https://github.com/alfredang/AI-LMS-TMS) "
                "| proprietary software … All rights reserved", LMS),
      ["alfredang/AI-LMS-TMS"])
check("D5: the real row still attributes correctly by slug",
      attribute("[`frappe/lms`](https://github.com/frappe/lms) are LIVE-NOGRANT — no payload", LMS),
      ["frappe/lms"])
# ...and p275's own Athena case, which the bare-name fallback exists for, must still work.
check("D5 regression: p275's bare-name case in bold prose still attributes",
      attribute("Artemis's feedback-suggestion engine **Athena** — treat as all-rights-reserved",
                ["ls1intum/Athena", "ls1intum/Artemis"]),
      ["ls1intum/Athena"])

# --- D2: candidate_grants had no SCOPE test -------------------------------------------
check("D2: ReaDirect-V2's asset attributions are not the repo's code grant",
      candidate_grants(["assets/icons/source/achievements/License.txt",
                        "apps/web/public/assets/game/licenses/ninja-adventure-cc0-license.txt",
                        "assets/licenses/fonts/lexend-ofl.txt"]), [])
check("D2: a dataset-scoped licence is not the repo's code grant",
      candidate_grants(["dataset/LICENSE"]), [])
check("D2: twelve translations of one licence are not twelve grants",
      candidate_grants(["html/license.txt", "html/lib/System/license/license_english.txt",
                        "html/lib/System/license/license_tamil.txt"]), ["html/license.txt"])
check("D2 positive arm: debian/copyright IS a grant (scoped, but real)",
      candidate_grants(["debian/copyright"]), ["debian/copyright"])
check("D2 positive arm: a LICENSE directory's contents are still a grant",
      candidate_grants(["LICENSE/LICENSE.txt"]), ["LICENSE/LICENSE.txt"])

# --- D3: the grant-evidence vocabulary did not match this base's house style ----------
check("D3a: a byte count written in the house style `1 531` B is grant evidence",
      states_a_grant("🟢 **`BSD-3-Clause`** — `1 531` B, all three clauses verbatim"), True)
check("D3b: a payload read asserted in prose is grant evidence",
      states_a_grant("BSD-3-Clause | the payload is the verbatim BSD-3 form; "
                     "its opening *All rights reserved* belongs to that form"), True)
check("D3c: a grant published by NAMING THE MANIFEST is grant evidence",
      states_a_grant("🟢 **Apache-2.0** · 🔴 no payload at all — per-file headers + "
                     "pom.xml <licenses> + README"), True)
check("D3 negative arm: an SPDX token alone does NOT silence a live negative verdict",
      states_a_grant("commonly cited as MIT, but this base publishes no grant it has not read"),
      False)

# --- D1: the gate read only the FILE channel, which was p275's own headline case -------
check("D1: an absence marker is matched by PREDICATE, not by equality",
      bool(ABSENT_KEY.search("<no license key in any>")), True)
check("D1: a real declared key is not read as an absence",
      bool(ABSENT_KEY.search('"license": "MIT" (l.66)')), False)
check("D1: a bare dash is an absence",
      bool(ABSENT_KEY.search("-")), True)

if FAILED:
    print(f"# {len(FAILED)} FAILING:")
    for f in FAILED:
        print("  FAIL", f)
    sys.exit(1)
print("# p275+p276 enumeration-gate suite: 47/47 PASS")
