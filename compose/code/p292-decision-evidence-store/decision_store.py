"""`ACTION p292` — the append-only decision evidence store, as a reference implementation.

🔵 WHY THIS FILE EXISTS.  `P45` (admissions), `P46` (retention), `P47` (grading) and `P48`
(vocational / Annex III retrofit) each terminate in "an append-only record of *who decided
what, shown what, under which rubric version*", each says **you build it**, and for four
passes nothing on these shelves supplied it.  `p291` ranked it item 1: load-bearing for four
recipes, no network needed, the one item a client would pay for.  This is that component.

🔴 WHAT IT IS NOT.  It is not a product, not a database and not tamper-PROOF.  The chain here
is tamper-EVIDENT against an edit or a deletion in place; a writer who can rewrite the whole
file can recompute every link.  What closes that gap is publishing `head()` somewhere the
writer does not control, and **the anchor is the client's** — see `anchor_statement()` and the
README's boundary section.  Saying otherwise would sell a hash chain as an immutability
guarantee, which is the single most common overclaim in this product category.

🟢 WHAT IT DOES SUPPLY, and why each refusal is a control and not a schema nicety:

  `R1` the decider must be a **natural person**.  Under the education limb the regulated act
       is the *decision*; an agent may contribute `advisory` observations and nothing else.
       `P45` says in prose "the prompt is not a control" — this is where that becomes one.
  `R2` **no decision without what was shown**, bound by digest.  An oversight record that
       cannot reproduce the observations the human read answers nothing.
  `R3` the **rubric version in force** is required.  "Apply the rubric consistently" is only
       auditable against the rubric that was in force at decision time.
  `R4` the operative act comes from a **closed vocabulary per surface**, so "scored" can
       never be recorded in the slot that means "decided".
  `R5` concurrence with the agent is **recorded, never refused** — see `concurred_with_agent`.
  `R6` **append-only** by hash chain, with `verify()` walking it.
  `R7` monotonic `seq`, unique `decision_id`.
  `R8` `decided_at` is RFC3339 **UTC** and the chain's clock may not run backwards.
  `R9` `subject_ref` must be **pseudonymous** — this is the record retained longest.
  `R10` a `distress_flag` requires a **named human recipient**, not a queue (`P45` step 5).

🟡 THE REGULATORY MAPPING IS `ATTRIBUTED`, NOT QUOTED.  `p289` measured 12 authority hosts
`POLICY-REFUSED` across 2 egress paths and `p291` did not reach EUR-Lex.  The Annex III(3)
limb tokens below are this base's working vocabulary keyed to a conference reproduction plus
commentary.  A client-facing use checks the Official Journal.  The code does not depend on the
wording: `ANNEX_LIMBS` is a closed token set and `NONE-DECLARED` is a first-class member,
because `P48` step 2 says the **exclusions** are what an auditor probes first.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

GENESIS = "GENESIS"

# --- the closed vocabularies -------------------------------------------------------------
# 🔴 Closed on purpose.  An open vocabulary here is how "the model scored it" ends up stored
# in the field an auditor reads as "a human decided it".
SURFACES = {
    "admissions": {"admit", "deny", "waitlist", "refer-to-committee", "withdrawn-by-applicant"},
    "retention": {"invite-to-support", "no-contact", "refer-to-adviser", "escalate-safeguarding"},
    "grading": {"accept-draft", "amend-draft", "reject-draft", "refer-to-second-marker"},
    "credential": {"award", "withhold", "refer-for-evidence"},
    "vocational": {"certify", "not-yet-competent", "refer-to-assessor"},
}

# 🟡 ATTRIBUTED (see module docstring).  Tokens, not a quotation of the Official Journal.
ANNEX_LIMBS = {
    "III-3-a-admission",          # admission / assignment to education and vocational training
    "III-3-b-learning-outcomes",  # evaluating learning outcomes, incl. steering the learning process
    "III-3-c-education-level",    # assessing the appropriate level of education
    "III-3-d-proctoring",         # monitoring prohibited behaviour during tests
    "NONE-DECLARED",              # 🟢 a first-class verdict: P48 step 2's recorded exclusion
}

DECIDER_KINDS = {"human", "agent", "service-account", "unattributed"}

RFC3339_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
# 🔴 R9's detector.  Deliberately narrow: it catches the shapes that are unarguably direct
# identifiers (e-mail, national-ID-looking digit runs) and does NOT pretend to be a general
# PII classifier.  A narrow detector that is right beats a broad one that gets switched off.
EMAILISH = re.compile(r"[^@\s]+@[^@\s]+\.[a-z]{2,}", re.I)
LONG_DIGITS = re.compile(r"(?<!\d)\d{9,}(?!\d)")

ENVELOPE = (
    "seq", "decision_id", "prev", "decided_at", "surface", "annex_limb", "decision",
    "decider", "rubric_version", "shown", "shown_digest", "agent", "subject_ref",
    "distress_flag", "distress_routed_to", "concurred_with_agent",
)


def canonical(obj) -> bytes:
    """Byte-stable serialisation.  Two readers must derive the same digest from one record."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def digest(data) -> str:
    if not isinstance(data, (bytes, bytearray)):
        data = canonical(data)
    return hashlib.sha256(data).hexdigest()


def shown_digest(shown) -> str:
    """The digest an oversight record is bound to: what the human was shown, canonically."""
    return digest(canonical(shown))


def link_digest(entry: dict) -> str:
    """A record's own link value: the digest of the whole record, `prev` included.

    🔵 That is what makes it a chain rather than a list of digests — record *i* commits to
    record *i-1*'s link, so one digest at the head commits to every record below it.
    🔵 `concurred_with_agent` is derived but IS inside the digest on purpose: a reader who
    recomputes concurrence and gets a different answer has found a tampered record, not a
    formatting convention.
    """
    return digest(canonical(entry))


def concurred(decision, agent) -> bool | None:
    """🟢 `R5`.  Agreement with the agent is RECORDED, never refused.

    Refusing it would be wrong twice over: a human who agrees with a correct recommendation has
    still decided, and a store that rejects agreement teaches its users to stop recording the
    recommendation.  What an auditor actually needs is the *rate*, so the field is derived here
    and sealed into the digest.  `None` means the agent made no recommendation to concur with.
    """
    rec = (agent or {}).get("recommendation")
    if rec in (None, ""):
        return None
    return rec == decision


def _finding(code, detail):
    return f"{code}\t{detail}"


def validate(entry: dict) -> list[str]:
    """Every refusal `R1`-`R10` that can be judged from one record alone."""
    f = []
    missing = [k for k in ENVELOPE if k not in entry]
    if missing:
        f.append(_finding("R0-INCOMPLETE-ENVELOPE", ",".join(missing)))
        return f

    # R4 — the operative act, per surface
    surface = entry["surface"]
    if surface not in SURFACES:
        f.append(_finding("R4-UNKNOWN-SURFACE", str(surface)))
    elif entry["decision"] not in SURFACES[surface]:
        f.append(_finding("R4-DECISION-OUTSIDE-VOCABULARY", f"{surface}/{entry['decision']}"))

    if entry["annex_limb"] not in ANNEX_LIMBS:
        f.append(_finding("R3b-UNKNOWN-ANNEX-LIMB", str(entry["annex_limb"])))

    # R1 — the decider is a natural person
    decider = entry["decider"] or {}
    kind = decider.get("kind")
    if kind not in DECIDER_KINDS:
        f.append(_finding("R1-UNKNOWN-DECIDER-KIND", str(kind)))
    elif kind != "human":
        f.append(_finding("R1-DECIDER-NOT-HUMAN", str(kind)))
    if not str(decider.get("id") or "").strip():
        f.append(_finding("R1b-DECIDER-UNIDENTIFIED", "decider.id is empty"))

    # R2 — no decision without what was shown, bound by digest
    if entry["shown"] in (None, {}, [], ""):
        f.append(_finding("R2-NOTHING-SHOWN", "the oversight record has no observations"))
    elif not HEX64.match(str(entry["shown_digest"] or "")):
        f.append(_finding("R2b-SHOWN-DIGEST-MALFORMED", str(entry["shown_digest"])[:32]))
    elif shown_digest(entry["shown"]) != entry["shown_digest"]:
        f.append(_finding("R2c-SHOWN-DIGEST-MISMATCH", "payload does not hash to its digest"))

    # R3 — the rubric in force
    if not str(entry["rubric_version"] or "").strip():
        f.append(_finding("R3-RUBRIC-VERSION-ABSENT", "not auditable for consistency"))

    # R5 — concurrence is derived, and must agree with the record it is sealed beside
    want = concurred(entry["decision"], entry["agent"])
    if entry["concurred_with_agent"] != want:
        f.append(_finding("R5-CONCURRENCE-MISSTATED", f"got {entry['concurred_with_agent']!r} want {want!r}"))
    agent = entry["agent"] or {}
    if agent and agent.get("role") not in (None, "advisory"):
        f.append(_finding("R5b-AGENT-ROLE-NOT-ADVISORY", str(agent.get("role"))))

    # R8 — RFC3339 UTC
    if not RFC3339_UTC.match(str(entry["decided_at"] or "")):
        f.append(_finding("R8-TIMESTAMP-NOT-RFC3339-UTC", str(entry["decided_at"])))

    # R9 — pseudonymous subject
    sref = str(entry["subject_ref"] or "")
    if not sref.strip():
        f.append(_finding("R9b-SUBJECT-REF-ABSENT", "cannot bind the record to a subject"))
    elif EMAILISH.search(sref) or LONG_DIGITS.search(sref):
        f.append(_finding("R9-SUBJECT-REF-DIRECTLY-IDENTIFYING", sref[:40]))

    # R10 — distress routes to a named human
    if entry["distress_flag"]:
        to = entry["distress_routed_to"] or {}
        if not isinstance(to, dict) or to.get("kind") != "human" or not str(to.get("id") or "").strip():
            f.append(_finding("R10-DISTRESS-NOT-ROUTED-TO-NAMED-HUMAN", json.dumps(to)[:60]))
    elif entry["distress_routed_to"] not in (None, {}):
        f.append(_finding("R10b-DISTRESS-ROUTE-WITHOUT-FLAG", "routed but not flagged"))

    # R7 — seq shape
    if not isinstance(entry["seq"], int) or isinstance(entry["seq"], bool) or entry["seq"] < 0:
        f.append(_finding("R7-SEQ-NOT-A-NATURAL-NUMBER", repr(entry["seq"])))
    if not str(entry["decision_id"] or "").strip():
        f.append(_finding("R7b-DECISION-ID-ABSENT", "the chain cannot be cross-referenced"))
    return f


class Refused(Exception):
    """🟢 An append that would have produced an unauditable record.  Nothing is written."""

    def __init__(self, findings):
        self.findings = list(findings)
        super().__init__("; ".join(self.findings))


class Store:
    """A JSON-Lines, hash-chained, append-only decision record.

    🔵 One record per line and one `fsync` per append: the format a client's auditor can read
    with `cut`/`jq` and a court can be handed, with no server to stand up.  The deliberate
    non-feature is query — put a read model beside it, never in it.
    """

    def __init__(self, path):
        self.path = str(path)

    # --- reading ------------------------------------------------------------------------
    def records(self):
        if not os.path.exists(self.path):
            return
        with open(self.path, "r", encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    yield lineno, json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{self.path}:{lineno}: not JSON ({exc.msg})") from exc

    def head(self) -> str:
        """The anchor value.  `GENESIS` on an empty store."""
        last = GENESIS
        for _, rec in self.records():
            last = link_digest(rec)
        return last

    def __len__(self):
        return sum(1 for _ in self.records())

    # --- writing ------------------------------------------------------------------------
    def append(self, *, decision_id, surface, decision, annex_limb, decider, rubric_version,
               shown, subject_ref, decided_at, agent=None, distress_flag=False,
               distress_routed_to=None) -> dict:
        prev = GENESIS
        seq = 0
        last_ts = None
        seen_ids = set()
        for _, rec in self.records():
            prev = link_digest(rec)
            seq = rec["seq"] + 1
            last_ts = rec["decided_at"]
            seen_ids.add(rec["decision_id"])

        entry = {
            "seq": seq,
            "decision_id": decision_id,
            "prev": prev,
            "decided_at": decided_at,
            "surface": surface,
            "annex_limb": annex_limb,
            "decision": decision,
            "decider": decider,
            "rubric_version": rubric_version,
            "shown": shown,
            "shown_digest": shown_digest(shown),
            "agent": agent,
            "subject_ref": subject_ref,
            "distress_flag": bool(distress_flag),
            "distress_routed_to": distress_routed_to,
            "concurred_with_agent": concurred(decision, agent),
        }

        findings = validate(entry)
        if decision_id in seen_ids:
            findings.append(_finding("R7c-DECISION-ID-REPLAYED", str(decision_id)))
        # R8 — the chain's clock may not run backwards
        if last_ts is not None and RFC3339_UTC.match(str(entry["decided_at"] or "")) \
                and entry["decided_at"] < last_ts:
            findings.append(_finding("R8b-CLOCK-WENT-BACKWARDS", f"{last_ts} -> {entry['decided_at']}"))
        if findings:
            raise Refused(findings)

        line = json.dumps(entry, sort_keys=True, ensure_ascii=False) + "\n"
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write(line)
            fh.flush()
            os.fsync(fh.fileno())
        return entry

    # --- verifying ----------------------------------------------------------------------
    def verify(self) -> list[str]:
        """Walk the chain.  An empty list means every record is internally sound AND linked."""
        findings = []
        prev = GENESIS
        expect_seq = 0
        last_ts = None
        seen = {}
        for lineno, rec in self.records():
            for item in validate(rec):
                findings.append(f"{self.path}:{lineno}\t{item}")
            if rec.get("prev") != prev:
                findings.append(f"{self.path}:{lineno}\t" + _finding(
                    "R6-CHAIN-BROKEN", f"prev={str(rec.get('prev'))[:12]} expected={prev[:12]}"))
            if rec.get("seq") != expect_seq:
                findings.append(f"{self.path}:{lineno}\t" + _finding(
                    "R7-SEQ-NOT-MONOTONIC", f"got {rec.get('seq')!r} expected {expect_seq}"))
            did = rec.get("decision_id")
            if did in seen:
                findings.append(f"{self.path}:{lineno}\t" + _finding(
                    "R7c-DECISION-ID-REPLAYED", f"{did} first at line {seen[did]}"))
            else:
                seen[did] = lineno
            ts = rec.get("decided_at")
            if last_ts is not None and isinstance(ts, str) and RFC3339_UTC.match(ts) and ts < last_ts:
                findings.append(f"{self.path}:{lineno}\t" + _finding(
                    "R8b-CLOCK-WENT-BACKWARDS", f"{last_ts} -> {ts}"))
            prev = link_digest(rec)
            expect_seq = (rec.get("seq") if isinstance(rec.get("seq"), int) else expect_seq) + 1
            if isinstance(ts, str):
                last_ts = ts
        return findings

    # --- the measurement an auditor actually asks for ------------------------------------
    def concurrence_rate(self, surface=None):
        """🔵 `R5`'s point.  Returns (concurred, comparable, rate-or-None).

        A rate near 1.0 over a large `comparable` is the rubber-stamp shape — the finding an
        oversight audit is looking for, and it is only measurable because concurrence is
        recorded rather than refused.
        """
        con = comparable = 0
        for _, rec in self.records():
            if surface and rec.get("surface") != surface:
                continue
            v = rec.get("concurred_with_agent")
            if v is None:
                continue
            comparable += 1
            con += 1 if v else 0
        return con, comparable, (con / comparable if comparable else None)

    def limb_census(self):
        """Every Annex III limb exercised, `NONE-DECLARED` included.  `P48` step 2's output."""
        out = {}
        for _, rec in self.records():
            out[rec.get("annex_limb")] = out.get(rec.get("annex_limb"), 0) + 1
        return out


def anchor_statement(store: Store) -> str:
    """🔴 The honest sentence to put in the SOW, printed from the real head value."""
    return (f"head={store.head()} records={len(store)}  "
            "TAMPER-EVIDENT against edit-in-place and deletion; NOT tamper-proof. "
            "A writer with write access to the whole file can recompute every link. "
            "Publish this head where the writer cannot reach it — the anchor is the client's.")


# --- the shelf arm -----------------------------------------------------------------------
# 🔴 `ACTION p292`'s standing check.  For four passes the shelves said "the evidence store:
# you build it" and no pass built it.  The defect that replaces that one is the opposite:
# a recipe terminating in a component that now EXISTS, without citing where it is.  A reader
# who cannot find it builds it a fifth time.
LOADBEARING = re.compile(r"evidence store|append-only (?:decision )?(?:record|store)", re.I)
CITATION = re.compile(r"p292-decision-evidence-store")

# 🔴 `S2` — the defect `ACTION p292` found in its OWN backlog entry, made standing.
# `p290` wrote "three recipes ... and one evidence store", `p291` wrote "now FOUR recipes, one
# build".  Measured against the shelves, **two** recipes terminate in the decision record.
# `P46` names an **intervention log** (date, method, response, outcome) and `P47` a
# **deadline-and-evidence layer** (statutory, calendar-bound) — adjacent components, not the
# same one.  Collapsing them under one name is what let it be deferred for four passes: "one
# build" sounds like one thing, so it was costed as one thing and never started.
# 🔵 The control therefore compares an ASSERTED recipe count against the MEASURED one.
WORDNUM = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
           "eight": 8, "nine": 9, "ten": 10}
# A claim of the shape "four recipes" / "FOUR recipes, one build" within a store context.
COUNT_CLAIM = re.compile(
    r"\b(?:now\s+)?(?:\*\*)?(one|two|three|four|five|six|seven|eight|nine|ten|\d+)(?:\*\*)?\s+"
    r"(?:recipes?|patterns?)\b", re.I)
# 🔴 THE GATE'S FIRST DRAFT OVER-MATCHED, and running it on the real shelf is what found it.
# `p290`'s own heading — *"three recipes whose compliance layer is a DEPENDENCY instead of a
# deliverable, and one evidence store that is neither"* — was flagged.  That sentence does not
# claim three store-bearing recipes; it CONTRASTS the three with the store.  Mentioning a count
# and the store in one sentence is not a claim that the count depends on the store, so a
# DEPENDENCY PREDICATE is required between them.
# 🔴 Worse, this instrument's own control `C28h` had asserted the false positive as desired
# behaviour.  A control written from the gate's intent rather than from a real sentence will
# happily pin a defect.  `C28h` is now inverted and says so.
# 🔴 SECOND over-match, same sentence.  The first repair matched the bare noun *"DEPENDENCY"*
# — which is the very word in `p290`'s heading ("whose compliance layer is a DEPENDENCY") — so
# the clause scope was right and the vocabulary was still wrong.  A dependency must be stated
# as a PREDICATE the recipes bear toward the component, not as a noun they are described with.
DEPENDS = re.compile(
    r"(needs?\b|needed\b|depends?\s+on|depending\s+on|requires?\b|required\b|terminat|"
    r"load-bearing\s+for|rests?\s+on|built\s+on|identical\s+component|same\s+component|"
    r"one\s+build|serves?\b)", re.I)
SENT_SPLIT = re.compile(r"(?<=[.!?;])\s|\s+—\s+")


def pattern_sections(text):
    """Split `compose/patterns.md` into `## P<N>` sections: (heading, start_line, body)."""
    lines = text.splitlines()
    marks = [(i, l) for i, l in enumerate(lines) if re.match(r"^## P\d+\b", l)]
    out = []
    for n, (i, head) in enumerate(marks):
        end = marks[n + 1][0] if n + 1 < len(marks) else len(lines)
        out.append((head.strip(), i + 1, "\n".join(lines[i:end])))
    return out


def loadbearing_labels(text):
    """Which `P<N>` recipes actually terminate in the decision record, measured not assumed."""
    out = []
    for head, _, body in pattern_sections(text):
        if LOADBEARING.search(body):
            out.append(re.match(r"^## (P\d+)", head).group(1))
    return out


def shelf_findings(text, filename="compose/patterns.md"):
    """A pattern whose deliverable IS the store must name the implementation."""
    out = []
    for head, line, body in pattern_sections(text):
        if LOADBEARING.search(body) and not CITATION.search(body):
            label = re.match(r"^## (P\d+)", head).group(1)
            out.append(f"{filename}:{line}\t" + _finding(
                "S1-LOADBEARING-STORE-UNCITED",
                f"{label} terminates in the evidence store and does not cite its implementation"))
    return out


# 🟢 `p223-selfclaim-date-gate`'s posture vocabulary, ADOPTED VERBATIM rather than invented
# twice — the same reason `p291` took `p279`'s live-section convention instead of writing its
# own.  A pass that QUOTES a refuted count in order to correct it is doing the right thing;
# a gate that cannot tell quotation from assertion would punish exactly that.
# 🔴 And block scope, not line scope: `p291`'s own shelf arm shipped line-scoped and was wrong
# on 6 of 7 findings because "a line is not the unit a reader reads".
QUOTE_SPAN = re.compile(r"[\"“‘«'][^\"”’»']{0,400}[\"”’»']")
QUOTE_CHARS = re.compile(r"[\"“”‘’«»]")
CORRECTED_CUE = re.compile(
    r"(corrected|refut|overclaim|wrong|stale|contradic|obsolet|measured against|"
    r"used to read|no longer|adjacent)", re.I)


def _clause_around(block, start, end):
    """The clause containing the match — sentence, or the comma-delimited part of one.

    🔵 Clause rather than sentence because `p290`'s heading puts the count and the store in two
    halves of ONE sentence joined by *"and"*, and the whole point is that the halves contrast.
    """
    head = block[:start]
    cuts = [m.end() for m in SENT_SPLIT.finditer(head)] + \
           [i + 1 for i, c in enumerate(head) if c == ","]
    lo = max(cuts) if cuts else 0
    nxt = SENT_SPLIT.search(block, end)
    hi = nxt.start() if nxt else len(block)
    comma = block.find(",", end)
    if comma != -1 and comma < hi:
        hi = comma
    return block[lo:hi]


def count_posture(block, start, end):
    """`ASSERTED` / `QUOTED` / `QUOTED-MULTILINE` / `CORRECTED`, per `p223`'s convention."""
    if block.lstrip().startswith(">") or block[:start].split("\n")[-1].lstrip().startswith(">"):
        return "QUOTED"
    if CORRECTED_CUE.search(block):
        return "CORRECTED"
    for q in QUOTE_SPAN.finditer(block):
        if q.start() <= start and end <= q.end():
            return "QUOTED"
    if len(QUOTE_CHARS.findall(block[:start])) % 2 == 1 or \
            len(QUOTE_CHARS.findall(block[end:])) % 2 == 1:
        return "QUOTED-MULTILINE"
    return "ASSERTED"


def blocks(text):
    """Blank-line-delimited blocks as `(first_line_number, body)`.  Table rows stand alone."""
    out = []
    cur, start = [], None
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip():
            if start is None:
                start = n
            cur.append(line)
        elif cur:
            out.append((start, "\n".join(cur)))
            cur, start = [], None
    if cur:
        out.append((start, "\n".join(cur)))
    return out


def count_findings(text, measured, filename="compose/patterns.md"):
    """`S2` — no block may ASSERT more store-bearing recipes than the shelves carry.

    Scoped to blocks that mention the store, so an unrelated "three patterns" sentence is not
    swept in.  Under-claiming is not a finding: a pass may cite a subset deliberately.
    🟢 `QUOTED` and `CORRECTED` are clean — see `count_posture`.
    """
    out = []
    for first, block in blocks(text):
        if not LOADBEARING.search(block):
            continue
        for m in COUNT_CLAIM.finditer(block):
            raw = m.group(1)
            claimed = WORDNUM.get(raw.lower()) or (int(raw) if raw.isdigit() else None)
            if claimed is None or claimed <= measured:
                continue
            # 🔴 the over-match repair: the count must be PREDICATED on the store, in its own
            # clause.  Read at clause scope so a dependency verb elsewhere in the paragraph
            # cannot manufacture a claim the sentence does not make.
            if not DEPENDS.search(_clause_around(block, m.start(), m.end())):
                continue
            if count_posture(block, m.start(), m.end()) != "ASSERTED":
                continue
            line = first + block[:m.start()].count("\n")
            out.append(f"{filename}:{line}\t" + _finding(
                "S2-STORE-RECIPE-COUNT-OVERCLAIMED",
                f"asserts {claimed} store-bearing recipe(s), shelves carry {measured}"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description="ACTION p292 — the decision evidence store")
    ap.add_argument("--root", help="KB root: run the shelf arm over compose/patterns.md")
    ap.add_argument("--verify", help="walk an existing store's chain")
    ap.add_argument("--head", help="print the anchor statement for a store")
    args = ap.parse_args(argv)

    rc = 0
    if args.verify:
        findings = Store(args.verify).verify()
        for item in findings:
            print(item)
        n = len(Store(args.verify))
        print(f"# p292 chain walk — {n} record(s), {len(findings)} finding(s)")
        print("🟢 PASS — the chain is unbroken and every record is auditable." if not findings
              else f"🔴 FAIL — {len(findings)} finding(s).")
        rc |= 1 if findings else 0

    if args.head:
        print(anchor_statement(Store(args.head)))

    if args.root:
        path = os.path.join(args.root, "compose", "patterns.md")
        text = open(path, "r", encoding="utf-8").read() if os.path.exists(path) else ""
        labels = loadbearing_labels(text)
        findings = shelf_findings(text) + count_findings(text, len(labels))
        for item in findings:
            print(item)
        print(f"# p292 evidence-store citation — {len(labels)} load-bearing recipe(s) "
              f"({', '.join(labels) or 'none'}), {len(findings)} finding(s)")
        print("🟢 PASS — every recipe that terminates in the store names its implementation, "
              "and no line claims more of them than the shelves carry."
              if not findings else
              f"🔴 FAIL — {len(findings)} finding(s).")
        rc |= 1 if findings else 0
    return rc


if __name__ == "__main__":
    sys.exit(main())
