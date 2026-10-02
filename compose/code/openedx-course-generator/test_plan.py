#!/usr/bin/env python3
"""Executable proof for the Open edX course generator (pass 45, action 2, gap 94).

Open edX is never started. The plan is computed from the outline, then replayed
against stub.CreateStub, which answers with the four behaviours measured in
openedx/edx-platform @ master. Asserts the three things action 2 asked for:

  1. no POST is emitted before the locator of its parent exists;
  2. siblings are grouped into parallelizable waves;
  3. a POST with no `category` is refused BY THE CLIENT, because the server
     answers 500 and not 400.

...plus the two the measurement added: a POST with no `parent_locator` is refused
by the client too (the server answers 403, which reads as a credentials problem),
and the call count is a number, not an estimate.

    python3 test_plan.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import (ALLOWED_POST_FIELDS, CREATE_PATH, OutlineError, cost,
                      execute, plan, validate_outline)
from stub import CreateStub, HttpError

HERE = os.path.dirname(os.path.abspath(__file__))
ok = True


def check(label, got, want):
    global ok
    good = got == want
    ok = ok and good
    print(f"{'PASS' if good else 'FAIL'}  {label}: got={got!r} want={want!r}")


def raises(label, fn, exc, needle=""):
    global ok
    try:
        fn()
        ok = False
        print(f"FAIL  {label}: no exception raised")
    except exc as e:
        good = needle in str(e)
        ok = ok and good
        print(f"{'PASS' if good else 'FAIL'}  {label}: {type(e).__name__}: {str(e)[:70]}")
    except Exception as e:  # noqa: BLE001
        ok = False
        print(f"FAIL  {label}: wrong exception {type(e).__name__}: {e}")


outline = json.load(open(os.path.join(HERE, "outline.example.json"), encoding="utf-8"))

# ------------------------------------------------------------------ the number
print("-- the cost, which is what goes in a proposal --")
c = cost(outline)
check("reading the course is ONE call (course_index)", c["reads"], 1)
check("writing it is one POST per block", c["writes"], 17)
check("total calls", c["calls"], 18)
check("sequential waves = outline depth", c["sequential_waves"], 4)
check("widest wave (the parallelism available)", c["widest_wave"], 8)

# -------------------------------------------------- 2. siblings batch per wave
print("\n-- 2. siblings are grouped into parallelizable waves --")
waves = plan(outline)
check("wave sizes", [len(w) for w in waves], [2, 3, 4, 8])
check("each wave holds exactly one level of the outline",
      [sorted({r["body"]["category"] for r in w}) for w in waves],
      [["chapter"], ["sequential"], ["vertical"],
       ["discussion", "html", "problem", "video"]])
# No two requests in the same wave are parent and child of each other.
for i, w in enumerate(waves):
    refs = {r["ref"] for r in w}
    check(f"wave {i}: no request depends on a sibling in its own wave",
          [r["ref"] for r in w if r["parent_ref"] in refs], [])

# ----------------------------------------- 1. a child never precedes its parent
print("\n-- 1. no POST is emitted before its parent's locator exists --")
seen = {outline["course_id"]}
violations = []
for i, w in enumerate(waves):
    for r in w:
        if r["parent_ref"] not in seen:
            violations.append((i, r["ref"], r["parent_ref"]))
    seen |= {r["ref"] for r in w}
check("plan: parents always precede children", violations, [])

stub = CreateStub(outline["course_id"])
log, locators = execute(outline, stub.post)
check("execute: one POST per block", stub.calls, 17)
check("execute: every POST answered 200", stub.by_status, {200: 17})
check("execute: 17 distinct locators came back", len(locators), 17)

known = {outline["course_id"]}
bad = []
for entry in log:
    if entry["parent"] not in known:
        bad.append(entry)
    known.add(entry["locator"])
check("execute: no POST used a locator that did not exist yet", bad, [])
check("execute: the wave numbering survived the replay",
      sorted({e["wave"] for e in log}), [0, 1, 2, 3])
check("execute: the locator came back as the new block's usage key, so no extra GET",
      all(e["locator"].startswith("block-v1:") and f"type@{e['category']}" in e["locator"]
          for e in log), True)

# --------------------------- 3. the client refuses what the server mis-reports
print("\n-- 3. the client refuses the bodies the server answers 500 / 403 --")
no_cat = {"course_id": outline["course_id"],
          "children": [{"display_name": "Sin categoria"}]}
raises("outline with no category is refused by the client",
       lambda: validate_outline(no_cat), OutlineError, "missing 'category'")
raises("plan() refuses it too, before any transport",
       lambda: plan(no_cat), OutlineError, "missing 'category'")

no_name = {"course_id": outline["course_id"],
           "children": [{"category": "chapter"}]}
raises("outline with no display_name is refused by the client",
       lambda: validate_outline(no_name), OutlineError, "missing 'display_name'")

bad_course = {"course_id": "AIS101", "children": []}
raises("a course_id that is not a course-v1 key is refused by the client",
       lambda: validate_outline(bad_course), OutlineError, "not a course-v1 key")

extra = {"course_id": outline["course_id"],
         "children": [{"category": "chapter", "display_name": "M1", "graderType": "Homework"}]}
raises("an unexpected key is refused by the client (server: 400)",
       lambda: validate_outline(extra), OutlineError, "unexpected key")

wrong_depth = {"course_id": outline["course_id"],
               "children": [{"category": "vertical", "display_name": "suelto"}]}
raises("a level out of order is refused by the client",
       lambda: validate_outline(wrong_depth), OutlineError, "expected 'chapter'")

check("the generator only ever sends the four fields the create path reads",
      sorted(ALLOWED_POST_FIELDS),
      ["boilerplate", "category", "display_name", "parent_locator"])
sent = {k for w in waves for r in w for k in r["body"]}
check("and the plan's bodies hold nothing else", sorted(sent - ALLOWED_POST_FIELDS), [])

# ---------------------- the stub really does punish what the client prevents
print("\n-- the stub is a contract, not a yes-man: the three failures reproduce --")
s = CreateStub(outline["course_id"])
raises("stub: no category -> 500 (bare subscript in _create_block_core)",
       lambda: s.post(CREATE_PATH, {"parent_locator": outline["course_id"]}),
       HttpError, "500")
raises("stub: no parent_locator -> 403 (course_key None, HasCourseAuthorAccess)",
       lambda: s.post(CREATE_PATH, {"category": "chapter"}), HttpError, "403")
raises("stub: unexpected field -> 400 (StrictSerializer)",
       lambda: s.post(CREATE_PATH, {"parent_locator": outline["course_id"],
                                    "category": "chapter", "graderType": "Homework"}),
       HttpError, "400")
raises("stub: a parent locator that was never created -> 403",
       lambda: s.post(CREATE_PATH, {"parent_locator": "block-v1:X+Y+Z+type@chapter+block@00",
                                    "category": "sequential"}), HttpError, "403")
check("stub: four malformed bodies, three distinct statuses",
      s.by_status, {500: 1, 403: 2, 400: 1})
check("stub: three distinct statuses for one class of defect (a bad body)",
      sorted(s.by_status), [400, 403, 500])
check("stub: none of the malformed bodies was accepted", s.created, {})

print()
print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
