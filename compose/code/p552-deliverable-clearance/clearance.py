#!/usr/bin/env python3
"""p552 -- two licence verdicts per row, not one.  (`Gap 552-B`, recipe `P606`)

WHY THIS EXISTS
  `Oriole-FDU/Wisepen` is BUSL-1.1.  Its Additional Use Grant permits personal,
  educational, academic and non-commercial PRODUCTION use, and excludes
  "consulting deliverable" BY NAME.  A university may deploy it; Globant may not
  ship it.  No family-name check separates those two readings, because the
  exclusion lives in a BUSL PARAMETER BLOCK -- two BUSL-1.1 repositories can
  differ completely on whether a deliverable may contain them.

  So every row needs TWO verdicts:
      deploy_for_client   -- may we stand it up and customise it for a client?
      embed_in_product    -- may we ship it inside something Globant sells?

WHAT THIS INSTRUMENT CANNOT DO, STATED FIRST
  * It is NOT legal advice and it does not replace counsel on a real engagement.
  * For OSI families it applies the well-known rule-of-thumb mapping below. The
    AGPL row is the one most often got wrong and is the one to check by hand.
  * For source-available families it DOES NOT GUESS: it extracts the Additional
    Use Grant and Change Date verbatim and returns `READ-THE-PARAMETERS`, because
    the answer is per-repository, not per-family.
  * `hosting is not distribution` is true for GPL and FALSE for AGPL; that single
    distinction is why `embed_in_product` and `deploy_for_client` are separate.
"""
import re, sys

OSI = {
    # family      deploy_for_client, embed_in_product, note
    "MIT":        (True,  True,  "permissive; keep the copyright notice"),
    "Apache-2.0": (True,  True,  "permissive; NOTICE file + patent grant"),
    "BSD-3":      (True,  True,  "permissive; no-endorsement clause"),
    "BSD-2":      (True,  True,  "permissive"),
    "LGPL":       (True,  False, "linked modules may stay proprietary; changes to the library itself do not"),
    "GPL-2.0":    (True,  False, "hosting is not distribution; shipping a binary is"),
    "GPL-3.0":    (True,  False, "hosting is not distribution; shipping a binary is"),
    "MPL-2.0":    (True,  False, "file-level copyleft; modified files stay open"),
    "AGPL-3.0":   (False, False, "*** NETWORK USE IS DISTRIBUTION -- hosting for a client TRIGGERS it ***"),
}
SOURCE_AVAILABLE = ("Business Source License", "BUSL", "BSL 1.1", "Server Side Public License",
                    "SSPL", "Elastic License", "PolyForm", "Fair Source", "Functional Source")

AUG   = re.compile(r"Additional Use Grant:(.*?)(?:\n\s*\n|Change Date:)", re.S | re.I)
CHANGE= re.compile(r"Change Date:\s*(.+?)\n", re.I)
CHLIC = re.compile(r"Change License:\s*(.+?)\n", re.I)
# the user-classes a consultancy must look for by name
EXCLUSIONS = ["consulting deliverable", "commercial product", "paid service", "hosted service",
              "SaaS offering", "revenue-generating", "non-commercial"]

def clear(family: str, payload: str = ""):
    if family in OSI:
        d, e, note = OSI[family]
        return {"family": family, "deploy_for_client": d, "embed_in_product": e,
                "basis": "OSI family rule-of-thumb", "note": note}
    if any(s.lower() in payload.lower() for s in SOURCE_AVAILABLE):
        aug = AUG.search(payload)
        grant = re.sub(r"\s+", " ", aug.group(1)).strip() if aug else "(not found)"
        hits = [x for x in EXCLUSIONS if x.lower() in grant.lower()]
        cd  = CHANGE.search(payload)
        cl  = CHLIC.search(payload)
        return {"family": family or "SOURCE-AVAILABLE",
                "deploy_for_client": "READ-THE-PARAMETERS",
                "embed_in_product": False if "consulting deliverable" in grant.lower() else "READ-THE-PARAMETERS",
                "basis": "Additional Use Grant, extracted verbatim",
                "additional_use_grant": grant,
                "named_exclusions": hits,
                "change_date": re.sub(r"\s+"," ",cd.group(1)).strip() if cd else None,
                "change_license": cl.group(1).strip() if cl else None,
                "note": "per-repository; the family name does NOT answer this"}
    return {"family": family or "UNREAD", "deploy_for_client": None, "embed_in_product": None,
            "basis": "no grant text read", "note": "UNREAD is not NO-GRANT -- widen the filename list first (Gap 552-C)"}

if __name__ == "__main__":
    payload = sys.stdin.read() if not sys.stdin.isatty() else ""
    fam = sys.argv[1] if len(sys.argv) > 1 else ""
    import json; print(json.dumps(clear(fam, payload), indent=2, ensure_ascii=False))
