"""Controls for `ACTION p292`. Run from this directory: `python3 test_decision_store.py`."""
import json
import os
import sys
import tempfile

from decision_store import (ANNEX_LIMBS, GENESIS, Refused, SURFACES, Store, anchor_statement,
                            blocks, canonical, concurred, count_findings, count_posture,
                            digest, link_digest, loadbearing_labels, pattern_sections,
                            shelf_findings, shown_digest, validate)

FAILED = []


def check(name, got, want):
    ok = got == want
    if not ok:
        FAILED.append(f"{name}: got {got!r} want {want!r}")
    print(f"  {'🟢' if ok else '🔴'} {name}")


SHOWN = {"academic": ["GPA 3.4 in-context"], "anomalies": ["unexplained 2024 gap — observation"],
         "not_captured": ["portfolio", "interview"]}
AGENT = {"slug": "iblai/higher-education-agents", "ref": "1a2d898bbd04",
         "recommendation": "refer-to-committee", "role": "advisory"}
HUMAN = {"id": "reader-7741", "kind": "human"}


def entry(**kw):
    base = dict(seq=0, decision_id="d-1", prev=GENESIS, decided_at="2026-10-18T12:00:00Z",
                surface="admissions", annex_limb="III-3-a-admission",
                decision="refer-to-committee", decider=dict(HUMAN),
                rubric_version="ug-2027-rev3", shown=SHOWN,
                shown_digest=shown_digest(SHOWN), agent=dict(AGENT),
                subject_ref="appl-9f2c1b", distress_flag=False, distress_routed_to=None,
                concurred_with_agent=True)
    base.update(kw)
    return base


def nfind(e):
    return len(validate(e))


def codes(e):
    return sorted(x.split("\t")[0] for x in validate(e))


def appended(**kw):
    """Append one record into a throwaway store and hand back (store, result-or-exception)."""
    fh = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
    fh.close()
    s = Store(fh.name)
    fields = dict(decision_id="d-1", surface="admissions", decision="refer-to-committee",
                  annex_limb="III-3-a-admission", decider=dict(HUMAN),
                  rubric_version="ug-2027-rev3", shown=SHOWN, subject_ref="appl-9f2c1b",
                  decided_at="2026-10-18T12:00:00Z", agent=dict(AGENT))
    fields.update(kw)
    try:
        return s, s.append(**fields)
    except Refused as exc:
        return s, exc


print("── p292-decision-evidence-store")

# --- the happy path ----------------------------------------------------------------------
check("C1 a well-formed oversight record is clean", nfind(entry()), 0)

# --- R1: the decider must be a natural person --------------------------------------------
check("C2 R1 an AGENT recorded as the decider is REFUSED",
      "R1-DECIDER-NOT-HUMAN" in codes(entry(decider={"id": "application-reader-agent",
                                                      "kind": "agent"})), True)
check("C2b R1 a service account is the same defect",
      "R1-DECIDER-NOT-HUMAN" in codes(entry(decider={"id": "svc-admissions",
                                                     "kind": "service-account"})), True)
check("C2c R1 'unattributed' is refused — oversight with no overseer answers nothing",
      "R1-DECIDER-NOT-HUMAN" in codes(entry(decider={"id": "x", "kind": "unattributed"})), True)
check("C2d R1 a decider kind outside the vocabulary fails",
      "R1-UNKNOWN-DECIDER-KIND" in codes(entry(decider={"id": "x", "kind": "committee"})), True)
check("C2e R1b a human with no identity is refused",
      "R1b-DECIDER-UNIDENTIFIED" in codes(entry(decider={"id": "  ", "kind": "human"})), True)

# --- R2: no decision without what was shown ----------------------------------------------
check("C3 R2 a decision with nothing shown is REFUSED",
      "R2-NOTHING-SHOWN" in codes(entry(shown={})), True)
check("C3b R2c a payload that does not hash to its digest is REFUSED",
      "R2c-SHOWN-DIGEST-MISMATCH" in codes(
          entry(shown=dict(SHOWN, anomalies=["edited after the fact"]))), True)
check("C3c R2b a malformed digest is caught before the mismatch arm",
      codes(entry(shown_digest="sha256:nope")), ["R2b-SHOWN-DIGEST-MALFORMED"])
check("C3d R2 the digest is over CANONICAL bytes, so key order cannot change it",
      shown_digest({"a": 1, "b": 2}) == shown_digest({"b": 2, "a": 1}), True)
check("C3e R2 a changed VALUE does change the digest",
      shown_digest({"a": 1}) == shown_digest({"a": 2}), False)

# --- R3: the rubric in force --------------------------------------------------------------
check("C4 R3 a decision with no rubric version is REFUSED",
      "R3-RUBRIC-VERSION-ABSENT" in codes(entry(rubric_version="")), True)
check("C4b R3b an Annex limb outside the vocabulary fails",
      "R3b-UNKNOWN-ANNEX-LIMB" in codes(entry(annex_limb="high-risk")), True)
check("C4c R3b NONE-DECLARED is a FIRST-CLASS verdict, not an error — P48 step 2",
      nfind(entry(annex_limb="NONE-DECLARED")), 0)

# --- R4: the closed vocabulary per surface -------------------------------------------------
check("C5 R4 'scored' can never be recorded in the slot that means 'decided'",
      "R4-DECISION-OUTSIDE-VOCABULARY" in codes(entry(decision="scored")), True)
check("C5b R4 a decision valid on ANOTHER surface is still refused on this one",
      "R4-DECISION-OUTSIDE-VOCABULARY" in codes(entry(decision="invite-to-support")), True)
check("C5c R4 an unknown surface fails", "R4-UNKNOWN-SURFACE" in codes(entry(surface="hiring")),
      True)
check("C5d R4 every listed act on every listed surface is accepted",
      sum(nfind(entry(surface=s, decision=d,
                      concurred_with_agent=concurred(d, AGENT)))
          for s, acts in SURFACES.items() for d in acts), 0)

# --- R5: concurrence is RECORDED, never refused -------------------------------------------
check("C6 R5 a human who AGREES with the agent is recorded, not rejected",
      nfind(entry(decision="refer-to-committee", concurred_with_agent=True)), 0)
check("C6b R5 disagreement is recorded as disagreement",
      nfind(entry(decision="admit", concurred_with_agent=False)), 0)
check("C6c R5 concurrence may not be MISSTATED beside the record it is sealed with",
      "R5-CONCURRENCE-MISSTATED" in codes(entry(decision="admit", concurred_with_agent=True)),
      True)
check("C6d R5 no recommendation means concurrence is None, not False",
      concurred("admit", {"slug": "x", "recommendation": None}), None)
check("C6e R5 a None-concurrence record is clean",
      nfind(entry(agent={"slug": "x", "recommendation": None, "role": "advisory"},
                  concurred_with_agent=None)), 0)
check("C6f R5b an agent recorded as anything but advisory is REFUSED",
      "R5b-AGENT-ROLE-NOT-ADVISORY" in codes(
          entry(agent=dict(AGENT, role="decider"))), True)

# --- R8: the timestamp --------------------------------------------------------------------
check("C7 R8 a non-UTC offset is REFUSED — one clock or no comparison",
      "R8-TIMESTAMP-NOT-RFC3339-UTC" in codes(entry(decided_at="2026-10-18T12:00:00+02:00")),
      True)
check("C7b R8 a date with no time is refused",
      "R8-TIMESTAMP-NOT-RFC3339-UTC" in codes(entry(decided_at="2026-10-18")), True)
check("C7c R8 fractional seconds are accepted",
      nfind(entry(decided_at="2026-10-18T12:00:00.123Z")), 0)

# --- R9: the subject reference is pseudonymous --------------------------------------------
check("C8 R9 a raw e-mail as the subject reference is REFUSED",
      "R9-SUBJECT-REF-DIRECTLY-IDENTIFYING" in codes(
          entry(subject_ref="ana.silva@uni.example.edu")), True)
check("C8b R9 a long digit run (national-ID shape) is refused",
      "R9-SUBJECT-REF-DIRECTLY-IDENTIFYING" in codes(entry(subject_ref="123456789012")), True)
check("C8c R9 a short opaque reference is accepted", nfind(entry(subject_ref="appl-9f2c1b")), 0)
check("C8d R9 a cohort year inside an opaque ref is NOT a false positive",
      nfind(entry(subject_ref="appl-2027-9f2c1b")), 0)
check("C8e R9b an absent subject reference is refused",
      "R9b-SUBJECT-REF-ABSENT" in codes(entry(subject_ref="")), True)

# --- R10: distress routes to a NAMED human, not a queue -----------------------------------
check("C9 R10 a distress flag routed to a QUEUE is REFUSED — P45 step 5",
      "R10-DISTRESS-NOT-ROUTED-TO-NAMED-HUMAN" in codes(
          entry(distress_flag=True,
                distress_routed_to={"id": "safeguarding-queue", "kind": "queue"})), True)
check("C9b R10 a distress flag with no route at all is refused",
      "R10-DISTRESS-NOT-ROUTED-TO-NAMED-HUMAN" in codes(entry(distress_flag=True)), True)
check("C9c R10 routed to a named human is clean",
      nfind(entry(distress_flag=True,
                  distress_routed_to={"id": "dean-of-students-3", "kind": "human"})), 0)
check("C9d R10b a route recorded without the flag is a finding",
      "R10b-DISTRESS-ROUTE-WITHOUT-FLAG" in codes(
          entry(distress_routed_to={"id": "x", "kind": "human"})), True)

# --- R0: the envelope ---------------------------------------------------------------------
e = entry()
del e["rubric_version"]
check("C10 R0 an incomplete envelope fails FAST and names the missing field",
      codes(e), ["R0-INCOMPLETE-ENVELOPE"])

# --- R7: seq and id shape -----------------------------------------------------------------
check("C11 R7 a negative seq fails", "R7-SEQ-NOT-A-NATURAL-NUMBER" in codes(entry(seq=-1)), True)
check("C11b R7 a bool is not a seq — True would otherwise pass as 1",
      "R7-SEQ-NOT-A-NATURAL-NUMBER" in codes(entry(seq=True)), True)
check("C11c R7b an absent decision id fails",
      "R7b-DECISION-ID-ABSENT" in codes(entry(decision_id="")), True)

# --- the append path refuses rather than writing -------------------------------------------
s, res = appended(decider={"id": "reader-agent", "kind": "agent"})
check("C12 append REFUSES an agent-decided record", isinstance(res, Refused), True)
check("C12b a refused append writes NOTHING — the store is still empty", len(s), 0)
check("C12c the refusal names the control",
      any(f.startswith("R1-DECIDER-NOT-HUMAN") for f in res.findings), True)

s, res = appended()
check("C13 a clean append returns the sealed record", res["seq"], 0)
check("C13b append computes the shown digest itself", res["shown_digest"], shown_digest(SHOWN))
check("C13c append derives concurrence itself", res["concurred_with_agent"], True)
check("C13d the first record links to GENESIS", res["prev"], GENESIS)
check("C13e a fresh append is verifiable", s.verify(), [])

# --- R6: the chain ------------------------------------------------------------------------
fh = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
fh.close()
chain = Store(fh.name)
for i in range(3):
    chain.append(decision_id=f"d-{i}", surface="admissions", decision="refer-to-committee",
                 annex_limb="III-3-a-admission", decider=dict(HUMAN),
                 rubric_version="ug-2027-rev3", shown=dict(SHOWN, n=i),
                 subject_ref=f"appl-{i}", decided_at=f"2026-10-18T12:0{i}:00Z", agent=dict(AGENT))
check("C14 three appends verify clean", chain.verify(), [])
check("C14b seq is monotonic", [r["seq"] for _, r in chain.records()], [0, 1, 2])
check("C14c each record links to the one below it",
      [r["prev"] for _, r in chain.records()][1:],
      [link_digest(r) for _, r in list(chain.records())[:-1]])
check("C14d head() is the last record's link",
      chain.head(), link_digest(list(chain.records())[-1][1]))

rows = [json.loads(l) for l in open(chain.path, encoding="utf-8")]

# R6 — edit a middle record in place
tampered = [dict(r) for r in rows]
tampered[1]["decision"] = "admit"
with open(chain.path, "w", encoding="utf-8") as fo:
    for r in tampered:
        fo.write(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n")
v = chain.verify()
check("C15 R6 an EDIT IN PLACE breaks the chain at the next record",
      any("R6-CHAIN-BROKEN" in x for x in v), True)
check("C15b the edited record is ALSO caught by R5 — the derived field no longer agrees",
      any("R5-CONCURRENCE-MISSTATED" in x for x in v), True)

# R6 — delete a record
with open(chain.path, "w", encoding="utf-8") as fo:
    for r in (rows[0], rows[2]):
        fo.write(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n")
v = chain.verify()
check("C16 R6 a DELETION is caught", any("R6-CHAIN-BROKEN" in x for x in v), True)
check("C16b R7 the seq gap is reported beside it",
      any("R7-SEQ-NOT-MONOTONIC" in x for x in v), True)

# R6 — reorder
with open(chain.path, "w", encoding="utf-8") as fo:
    for r in (rows[0], rows[2], rows[1]):
        fo.write(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n")
check("C17 R6 a REORDER is caught", any("R6-CHAIN-BROKEN" in x for x in chain.verify()), True)

# 🔴 the honest limit, as a control: a full rewrite verifies CLEAN
fh2 = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
fh2.close()
rewritten = Store(fh2.name)
for i, r in enumerate(rows):
    if i == 1:
        continue
    rewritten.append(decision_id=r["decision_id"], surface=r["surface"],
                     decision=r["decision"], annex_limb=r["annex_limb"],
                     decider=r["decider"], rubric_version=r["rubric_version"],
                     shown=r["shown"], subject_ref=r["subject_ref"],
                     decided_at=r["decided_at"], agent=r["agent"])
check("C18 🔴 A FULL REWRITE VERIFIES CLEAN — the chain is tamper-EVIDENT, not tamper-proof",
      rewritten.verify(), [])
check("C18b what detects it is the ANCHOR: the head moved",
      rewritten.head() == chain.head(), False)
check("C18c and the anchor statement says so in words, not in a footnote",
      "NOT tamper-proof" in anchor_statement(rewritten), True)

# --- R7c: replay --------------------------------------------------------------------------
fh3 = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
fh3.close()
rp = Store(fh3.name)
rp.append(decision_id="d-dup", surface="admissions", decision="refer-to-committee",
          annex_limb="III-3-a-admission", decider=dict(HUMAN), rubric_version="r1",
          shown=SHOWN, subject_ref="a-1", decided_at="2026-10-18T12:00:00Z", agent=dict(AGENT))
try:
    rp.append(decision_id="d-dup", surface="admissions", decision="admit",
              annex_limb="III-3-a-admission", decider=dict(HUMAN), rubric_version="r1",
              shown=SHOWN, subject_ref="a-1", decided_at="2026-10-18T12:05:00Z", agent=dict(AGENT))
    replay = None
except Refused as exc:
    replay = exc
check("C19 R7c a replayed decision id is REFUSED",
      replay is not None and any("R7c-DECISION-ID-REPLAYED" in f for f in replay.findings), True)
check("C19b the store still holds exactly one record", len(rp), 1)

# --- R8b: the clock -----------------------------------------------------------------------
try:
    rp.append(decision_id="d-back", surface="admissions", decision="admit",
              annex_limb="III-3-a-admission", decider=dict(HUMAN), rubric_version="r1",
              shown=SHOWN, subject_ref="a-2", decided_at="2026-10-18T11:00:00Z", agent=dict(AGENT))
    back = None
except Refused as exc:
    back = exc
check("C20 R8b an append whose clock runs backwards is REFUSED",
      back is not None and any("R8b-CLOCK-WENT-BACKWARDS" in f for f in back.findings), True)

# --- the measurement an oversight audit asks for -------------------------------------------
fh4 = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False)
fh4.close()
rate = Store(fh4.name)
for i in range(4):
    rate.append(decision_id=f"r-{i}", surface="admissions",
                decision="refer-to-committee" if i < 3 else "admit",
                annex_limb="III-3-a-admission" if i < 3 else "NONE-DECLARED",
                decider=dict(HUMAN), rubric_version="r1", shown=dict(SHOWN, n=i),
                subject_ref=f"a-{i}", decided_at=f"2026-10-18T12:0{i}:00Z", agent=dict(AGENT))
check("C21 concurrence_rate measures the RUBBER-STAMP shape", rate.concurrence_rate(),
      (3, 4, 0.75))
check("C21b a record with no recommendation is excluded from the denominator, not counted 0",
      Store(fh4.name).concurrence_rate("retention"), (0, 0, None))
check("C22 limb_census reports NONE-DECLARED alongside the limbs — P48 step 2",
      rate.limb_census(), {"III-3-a-admission": 3, "NONE-DECLARED": 1})

# --- canonical form ------------------------------------------------------------------------
check("C23 canonical bytes are key-order independent",
      canonical({"b": 1, "a": 2}), canonical({"a": 2, "b": 1}))
check("C23b canonical form keeps non-ASCII as itself, so a digest is not encoding-dependent",
      "ñ" in canonical({"k": "mañana"}).decode("utf-8"), True)
try:
    canonical({"k": float("nan")})
    nan_serialised = True
except ValueError:
    nan_serialised = False
check("C23c NaN RAISES instead of emitting a record no JSON reader can parse back",
      nan_serialised, False)
check("C24 digest accepts an object or its bytes and agrees",
      digest({"a": 1}), digest(canonical({"a": 1})))

# --- the empty store -----------------------------------------------------------------------
empty = Store(os.path.join(tempfile.mkdtemp(), "none.jsonl"))
check("C25 an absent store is empty rather than an error", len(empty), 0)
check("C25b an empty store's head is GENESIS", empty.head(), GENESIS)
check("C25c an empty store verifies clean", empty.verify(), [])

# --- the shelf arm -------------------------------------------------------------------------
UNCITED = ("## P45 — the reader\n\nIt terminates in the evidence store.\n\n"
           "## P46 — the loop\n\nNothing load-bearing here.\n")
check("C26 S1 a recipe terminating in the store without citing it is a finding",
      len(shelf_findings(UNCITED)), 1)
check("C26b the finding names the pattern, not the file alone",
      "P45" in shelf_findings(UNCITED)[0], True)
check("C26c a recipe that cites the implementation is clean",
      shelf_findings("## P45 — x\n\nthe evidence store: "
                     "`compose/code/p292-decision-evidence-store`\n"), [])
check("C26d a recipe with no load-bearing mention is not scanned for the citation",
      shelf_findings("## P46 — x\n\nNothing relevant.\n"), [])
check("C26e the 'append-only decision record' phrasing is recognised too — a gate that "
      "matches only its own jargon measures the jargon",
      len(shelf_findings("## P47 — x\n\nan append-only decision record\n")), 1)
check("C27 pattern_sections stops each section at the next `## P`",
      [h.split(" ")[1] for h, _, _ in pattern_sections(UNCITED)], ["P45", "P46"])
check("C27b section line numbers are 1-based",
      [l for _, l, _ in pattern_sections(UNCITED)], [1, 5])
check("C27c a file with no pattern headings yields nothing rather than one giant section",
      pattern_sections("plain text\n"), [])
check("C27d loadbearing_labels NAMES them, so a count is never the only evidence",
      loadbearing_labels(UNCITED), ["P45"])

# --- S2: the overclaim this instrument found in its own backlog entry ----------------------
P291_SENTENCE = ("🔵 It is still missing, it is still the billable half, and `P48` makes "
                 "**four** recipes that need the identical evidence store.\n")
check("C28 S2 p291's own 'four recipes' sentence FAILS against a measured two",
      len(count_findings(P291_SENTENCE, 2)), 1)
check("C28b the finding reports both numbers, not just a verdict",
      "asserts 4 store-bearing recipe(s), shelves carry 2" in count_findings(P291_SENTENCE, 2)[0],
      True)
check("C28c the same sentence is clean once the shelves really carry four",
      count_findings(P291_SENTENCE, 4), [])
check("C28d UNDER-claiming is not a finding — a pass may cite a subset deliberately",
      count_findings("the evidence store serves **two** recipes\n", 4), [])
check("C28e a digit is read as well as a word",
      len(count_findings("the evidence store: 4 recipes depend on it\n", 2)), 1)
check("C28f a count on a line that does NOT mention the store is not swept in",
      count_findings("this pass ships four recipes\n", 2), [])
check("C28g 'one build' is not a recipe count and must not be parsed as one",
      count_findings("the evidence store — four recipes, one build\n", 4), [])
# 🔴 C28h IS INVERTED FROM ITS FIRST DRAFT, and the real shelf is what inverted it.
# This control originally asserted that p290's heading SHOULD be flagged.  Running the gate
# over compose/patterns.md showed the heading does not claim three store-bearing recipes --
# it CONTRASTS the three recipes with the store ("...and one evidence store that is neither").
# A control written from the gate's intent rather than from a real sentence pinned a defect.
check("C28h 🔴 p290's real heading is a FALSE POSITIVE and must NOT be flagged — it contrasts "
      "the count with the store instead of predicating it on the store",
      count_findings("## Pass 290 — three recipes whose compliance layer is a DEPENDENCY "
                     "instead of a deliverable, and one evidence store that is neither\n", 2),
      [])
check("C28i a DEPENDENCY PREDICATE is what makes it a claim",
      len(count_findings("the evidence store: three recipes need it\n", 2)), 1)
check("C28j 'terminate in' is a dependency predicate",
      len(count_findings("three recipes terminate in the evidence store\n", 2)), 1)
check("C28k a dependency verb in ANOTHER clause cannot manufacture the claim",
      count_findings("three recipes shipped, and the evidence store is needed elsewhere\n", 2),
      [])
# 🔴 The SECOND over-match on the same sentence: the repair's first vocabulary matched the
# bare noun "DEPENDENCY", which is the very word p290's heading uses.  Clause scope was
# right; the vocabulary was still wrong.
check("C28l 🔴 the bare NOUN 'dependency' is not a dependency predicate",
      count_findings("three recipes whose compliance layer is a DEPENDENCY, beside the "
                     "evidence store\n", 2), [])
check("C28m but 'depends on' is", 
      len(count_findings("three recipes depend on the evidence store\n", 2)), 1)
check("C28n p291's real sentence still fails when ASSERTED rather than quoted",
      len(count_findings("The evidence store is the billable half, and `P48` makes four "
                         "recipes that need the identical component.\n", 2)), 1)

# --- S2's postures: p223's vocabulary, adopted rather than re-invented --------------------
QUOTED = ('`p291` wrote *"now **four** recipes, one build"* about the evidence store, '
          'and it was not so.\n')
check("C29 S2 a count QUOTED in order to correct it is CLEAN",
      count_findings(QUOTED, 2), [])
check("C29b the posture is named QUOTED or CORRECTED, not ASSERTED",
      count_posture(QUOTED, QUOTED.index("four"), QUOTED.index("four") + 4) != "ASSERTED", True)
check("C29c a block carrying a CORRECTED cue is clean even unquoted",
      count_findings("the evidence store: four recipes — CORRECTED, the shelves carry two\n",
                     2), [])
check("C29d a blockquote line is clean",
      count_findings("> the evidence store serves four recipes\n", 2), [])
check("C29e a BARE assertion with no quote and no correction cue still FAILS",
      len(count_findings("the evidence store is load-bearing for four recipes\n", 2)), 1)
check("C29f the posture is read at BLOCK scope — p291's line-scope defect, not repeated",
      count_findings("the evidence store is load-bearing\nfor four recipes here, which this "
                     "pass refuted\n", 2), [])
check("C29g a separate block cannot launder an assertion in another one",
      len(count_findings("this pass refuted a lot.\n\nthe evidence store needs four "
                         "recipes\n", 2)), 1)
check("C30 blocks() splits on blank lines and reports 1-based first lines",
      [n for n, _ in blocks("a\nb\n\n\nc\n")], [1, 5])
check("C30b blocks() emits no empty blocks for consecutive blank lines",
      len(blocks("a\n\n\n\nb\n")), 2)
check("C30c the reported line is the CLAIM's line, not the block's first",
      count_findings("the evidence store is load-bearing\nfor four recipes\n", 2)[0]
      .startswith("compose/patterns.md:2"), True)

print()
if FAILED:
    print(f"🔴 {len(FAILED)} control(s) FAILED:")
    for f in FAILED:
        print(f"   {f}")
    sys.exit(1)
print("   PASS")
