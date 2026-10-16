#!/usr/bin/env python3
"""Controls for `p244-absence-states`.  Run either way — that is itself a control.

🟢 `p241` found that `p1058`'s suite died under `python3 -I` with `ModuleNotFoundError`, because
`-I` strips the script's own directory from `sys.path`, and that a working gate therefore stayed
a one-off for `53` passes: it could not be invoked from the place a hook runs.  This file fixes
its own invocation rather than asking the Makefile to `cd` for it.

    python3 -I compose/code/p244-absence-states/test_absence_states.py   # from the repo root
    cd compose/code/p244-absence-states && python3 test_absence_states.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from absence_states import (  # noqa: E402
    address_exists,
    address_state,
    carveout_holder,
    grant_completeness,
    payload_is_usable,
    payload_remedy,
    payload_state,
    query_shape,
    report,
    zero_result_is_absence,
)

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")

_passed = 0
_failed = []


def check(name, got, want):
    global _passed
    if got == want:
        _passed += 1
    else:
        _failed.append("%s\n    got:  %r\n    want: %r" % (name, got, want))


def read(fname):
    with open(os.path.join(FIX, fname), "rb") as fh:
        return fh.read().decode("utf-8", "replace")


def size(fname):
    return os.path.getsize(os.path.join(FIX, fname))


# ─── channel 1: PAYLOAD ───────────────────────────────────────────────────────────────────────
# The pass's proof pair.  These two rows get the SAME cell from the shared probe and they are
# different facts.  If this instrument ever gives them the same answer, it has bought nothing.

EMPTY = "meineschule-digital.LICENSE.empty"
check("meineschule-digital: 200 + 0 bytes is not a grant",
      payload_state(200, size(EMPTY), read(EMPTY), declared_in_readme=True), "EMPTY-DECLARED")
check("meineschule-digital: the fixture really is 0 bytes", size(EMPTY), 0)
check("meineschule-digital: not usable", payload_is_usable(200, 0, "", True), False)
check("HAZA-SMS: a declared path that 404s is a different state",
      payload_state(404, 0, None, declared_in_readme=True), "ABSENT-DECLARED")
check("THE PROOF: the two states differ",
      payload_state(200, 0, "", True) != payload_state(404, 0, None, True), True)
check("and their remedies differ",
      payload_remedy("EMPTY-DECLARED") != payload_remedy("ABSENT-DECLARED"), True)
check("no README claim is a third state",
      payload_state(404, 0, None, declared_in_readme=False), "ABSENT-UNDECLARED")

# The refusal served as a body.  14 bytes is a plausible-looking payload size.
NF = "haza-sms.LICENSE.notfound-body"
check("the 404 body is 14 bytes", size(NF), 14)
check("a refusal body is never a payload, even with a 200 plumbed in",
      payload_state(200, size(NF), read(NF)), "NOT-FOUND-BODY")
check("…and never usable", payload_is_usable(200, 14, read(NF)), False)

CANON = "iblai.LICENSE.mit-canonical"
check("a real grant is GRANTED", payload_state(200, size(CANON), read(CANON)), "GRANTED")
check("a real grant is usable", payload_is_usable(200, size(CANON), read(CANON)), True)
check("the canonical iblai payload is 1063 B", size(CANON), 1063)
check("a transport answer is not a licence answer", payload_state(502, 0), "UNREADABLE")

# ─── channel 2: ADDRESS ───────────────────────────────────────────────────────────────────────
# Measured on three real slugs this pass.  Two of the three EXIST.

check("edfi-mcp-server: rc=0 with 0 refs is an EMPTY repo, not a dead address",
      address_state(0, 0, ""), "EMPTY-REPO")
check("edgenuity-aeries-grade-passback: same shape, same verdict",
      address_state(0, 0, ""), "EMPTY-REPO")
check("an EMPTY repo EXISTS", address_exists(0, 0, ""), True)
check("scormplayer: an auth demand is unreachable",
      address_state(128, 0, "fatal: could not read Username for 'https://github.com': "
                            "terminal prompts disabled"), "UNREACHABLE-AUTH")
check("…and does not count as existing", address_exists(128, 0, "could not read Username"), False)
check("a live repo is LIVE", address_state(0, 2131, ""), "LIVE")
check("THE PROOF: empty and unreachable are not the same cell",
      address_state(0, 0, "") != address_state(128, 0, "could not read Username"), True)
check("a non-auth failure is a transport error, not a deletion",
      address_state(128, 0, "fatal: unable to access: Could not resolve host"), "TRANSPORT-ERROR")

# ─── channel 3: QUERY ─────────────────────────────────────────────────────────────────────────
# The two queries this pass ran that returned 0 for the wrong reason.

check("topic:deped OR … is a void shape",
      query_shape("topic:deped OR topic:nigeria school management"),
      "VOID-OR-BETWEEN-QUALIFIERS")
check("topic:cbse OR … is a void shape",
      query_shape("topic:cbse OR topic:ncert school AI"), "VOID-OR-BETWEEN-QUALIFIERS")
check("topic:deped alone is valid", query_shape("topic:deped"), "VALID")
check("topic:cbse alone is valid", query_shape("topic:cbse"), "VALID")
check("a two-topic AND is valid", query_shape("topic:enrollment topic:education"), "VALID")
check("org: queries are valid", query_shape("org:iblai"), "VALID")
# `OR` between BARE terms is accepted by the API, so the gate must not over-fire.
check("OR between bare terms is NOT void", query_shape("gradebook OR markbook"), "VALID")
check("an empty query is its own state", query_shape(""), "EMPTY-QUERY")

check("THE GATE: 0 from a void query may not be published as an absence",
      zero_result_is_absence("topic:deped OR topic:nigeria school management", 0), False)
check("THE GATE: 0 from a valid query may be",
      zero_result_is_absence("topic:school-fees", 0), True)
check("a non-zero count is never an absence",
      zero_result_is_absence("topic:deped", 10), False)
check("the axis that actually paid: 10 rows behind the void query",
      zero_result_is_absence("topic:deped", 10), False)

# ─── the dual: TRUNCATION ─────────────────────────────────────────────────────────────────────

TRUNC = "aprende-brasil.LICENSE.mit-truncated"
check("aprende-brasil is 814 B", size(TRUNC), 814)
check("aprende-brasil: the liability paragraph is gone",
      grant_completeness(read(TRUNC)), "TRUNCATED-AFTER-WARRANTY")
check("the truncated payload still CARRIES the grant verb",
      "permission is hereby granted" in read(TRUNC).lower(), True)
check("…and the warranty disclaimer", 'AS IS' in read(TRUNC), True)
check("…and does NOT carry the liability clause",
      "IN NO EVENT SHALL" in read(TRUNC).upper(), False)
check("a canonical MIT is COMPLETE", grant_completeness(read(CANON)), "COMPLETE")
check("a team-holder MIT is COMPLETE", grant_completeness(read("lara.LICENSE.mit-team-holder")),
      "COMPLETE")
check("a holderless MIT is still COMPLETE",
      grant_completeness(read("iron-county.LICENSE.mit-holderless")), "COMPLETE")
check("an Ltda-holder MIT is COMPLETE",
      grant_completeness(read("bncc-dados.LICENSE.mit-ltda-holder")), "COMPLETE")
check("an empty payload is EMPTY, not truncated", grant_completeness(read(EMPTY)), "EMPTY")
check("a non-MIT body is not judged on MIT clauses",
      grant_completeness("GNU AFFERO GENERAL PUBLIC LICENSE Version 3"), "NOT-MIT-SHAPED")
# Reflow control: the clause is prose, so its line breaks must not be load-bearing.
check("a reflowed complete MIT is still COMPLETE",
      grant_completeness(" ".join(read(CANON).split())), "COMPLETE")

# ─── the carve-out that grants to nobody ──────────────────────────────────────────────────────

CARVE = "schul-system.LICENSE.md.mit-plus-carveout"
check("Schul-System is 1324 B", size(CARVE), 1324)
check("its MIT text is COMPLETE — the carve-out is not a truncation",
      grant_completeness(read(CARVE)), "COMPLETE")
check("the carve-out names an entity that cannot hold the copyright",
      carveout_holder(read(CARVE)), "CARVEOUT-NON-HOLDER:chat-gpt")
check("a canonical MIT has no carve-out", carveout_holder(read(CANON)), "NO-CARVEOUT")
check("a carve-out that names a real holder is a different state",
      carveout_holder('NOTA DE EXCLUSION. assets/ - (c) Oksigenia SL, '
                      'todos los derechos reservados.'), "CARVEOUT-HOLDER-STATED")
# The guard must survive the words it guards against still being present (p243's T243-B shape).
check("the offending phrase is STILL IN THE FIXTURE",
      "Chat-GPT" in read(CARVE), True)
check("…and the German disclaimer too",
      "nicht unter dem Urheberrecht" in read(CARVE), True)

# ─── the combined report ──────────────────────────────────────────────────────────────────────

r = report(http_code=200, byte_count=0, body="", declared_in_readme=True)
check("report: payload only", sorted(r), ["payload_remedy", "payload_state"])
check("report: the empty state travels", r["payload_state"], "EMPTY-DECLARED")
r2 = report(returncode=0, ref_count=0, query="topic:deped OR topic:x", total_count=0,
            text=read(TRUNC))
check("report: address", r2["address_state"], "EMPTY-REPO")
check("report: query gate", r2["zero_is_absence"], False)
check("report: completeness", r2["grant_completeness"], "TRUNCATED-AFTER-WARRANTY")
check("report: no payload keys when not asked", "payload_state" in r2, False)

# ─── P237 / P171: this instrument must NOT re-ask the family question ─────────────────────────

_src = read("../absence_states.py") if os.path.exists(os.path.join(FIX, "../absence_states.py")) \
    else open(os.path.join(os.path.dirname(FIX), "absence_states.py")).read()
check("no family classifier is reimplemented here (P237)",
      ("def family_of" in _src) or ("AGPL" in _src and "def family" in _src), False)
check("the module does not import a family classifier either",
      "license_family" in _src.replace("lib/license_family.sh", ""), False)

# ─── report ───────────────────────────────────────────────────────────────────────────────────

total = _passed + len(_failed)
if _failed:
    print("FAIL %d/%d" % (len(_failed), total))
    for f in _failed:
        print("  " + f)
    sys.exit(1)
print("p244-absence-states: %d/%d controls pass" % (_passed, total))
