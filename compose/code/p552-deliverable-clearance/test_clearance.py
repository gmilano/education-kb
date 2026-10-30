#!/usr/bin/env python3
"""Controls for clearance.py. Run from THIS directory (p355-cwd-portability)."""
from clearance import clear

WISEPEN = """Business Source License 1.1
Parameters
Licensor:             Fudan University Oriole Team and WisePen contributors
Licensed Work:        WisePen Project
Additional Use Grant: You may make non-production use of the Licensed Work.
                      You may also make production use of the Licensed Work for
                      personal, educational, academic research, or other
                      non-commercial purposes, provided that such use does not
                      include offering the Licensed Work, or any modified or
                      derivative version of it, as part of a commercial product,
                      paid service, hosted service, SaaS offering, consulting
                      deliverable, or revenue-generating business activity.

Change Date:          Four years from the release date of each version
Change License:       Apache License, Version 2.0
"""

ok = fail = 0
def check(name, got, want):
    global ok, fail
    if got == want: ok += 1
    else: fail += 1; print(f"FAIL {name}: got {got!r} want {want!r}")

# --- OSI families
check("MIT embeds",            clear("MIT")["embed_in_product"], True)
check("Apache embeds",         clear("Apache-2.0")["embed_in_product"], True)
check("GPL3 deploys",          clear("GPL-3.0")["deploy_for_client"], True)
check("GPL3 does not embed",   clear("GPL-3.0")["embed_in_product"], False)
check("LGPL deploys",          clear("LGPL")["deploy_for_client"], True)
check("LGPL does not embed",   clear("LGPL")["embed_in_product"], False)
# the one most often got wrong:
check("AGPL does NOT deploy",  clear("AGPL-3.0")["deploy_for_client"], False)

# --- the real WisePen payload
w = clear("BUSL-1.1", WISEPEN)
check("BUSL embed refused",    w["embed_in_product"], False)
check("BUSL deploy deferred",  w["deploy_for_client"], "READ-THE-PARAMETERS")
check("BUSL names consulting", "consulting deliverable" in w["named_exclusions"], True)
check("BUSL change licence",   w["change_license"], "Apache License, Version 2.0")
check("BUSL grant extracted",  "non-commercial purposes" in w["additional_use_grant"], True)

# --- UNREAD is not NO-GRANT (Gap 552-C)
check("unread is not refusal", clear("UNREAD")["embed_in_product"], None)
check("19-byte assertion",     clear("", "License: GNU GPL V3")["family"], "UNREAD")

print(f"\n{ok}/{ok+fail} controls pass")
raise SystemExit(1 if fail else 0)
