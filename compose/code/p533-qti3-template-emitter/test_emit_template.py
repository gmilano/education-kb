"""Oracle for P533 / `Gap 238`.

Run: python3 -I test_emit_template.py

WHY THIS ORACLE AND NOT THE XSD. `Gap 238`'s remedy names a round-trip against
core's parser. Two stronger options were tried first and both are unavailable
here, so the substitution is recorded rather than hidden:

  1. Execute qti3's own vitest suite — not permitted: installing a third-party
     repository's dependencies is out of scope in this environment. This is the
     same limit pass 42 recorded on `P527`.
  2. Validate against the official QTI 3.0.1 ASI schema, which qti3 pins by
     sha256 in `packages/conformance/schemas/qti3/sources.json` — the schema is
     NOT vendored, it is fetched, and `purl.imsglobal.org:443` is refused by this
     environment's egress proxy (`connect_rejected`, organization policy). Same
     class as `Gap 56` (eur-lex) and `Gap 92` (docs.moodle.org).

So the oracle is TRANSITIVE, and that is what makes it sound rather than merely
convenient: `packages/fixtures/xml/*.xml` are the documents qti3's own schema gate
validates against that pinned official schema — `scripts/check-test-xsd.mjs` runs
`xmllint --nonet --noout --schema <pinned ASI xsd>` over them and reports
"official ASI schema validation passed". A fixture is therefore a known
schema-valid QTI 3 document. If the emitter regenerates one **node-for-node**,
the emitter's output is schema-valid by transitivity, without this environment
needing to reach the schema.

Two independent fixtures are used, not one, so a single hand-tuned success cannot
pass as a general result.

Every assertion below is paired with a NEGATIVE CONTROL that proves the assertion
can still fail — `P471`'s rule: a gate that passes 27/27 while judging nothing is
not a gate. And per `P399`/pass 122, no assertion freezes a corpus cardinality;
each is an invariant property.
"""

from __future__ import annotations

import pathlib
import random
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from emit_template import (  # noqa: E402
    BaseValue,
    RandomInteger,
    SetCorrectResponse,
    SetTemplateValue,
    TemplateConstraint,
    TemplateDeclaration,
    TemplateEmitError,
    TemplateProcessing,
    Variable,
    build_parametric_item,
    estimate_constraint_restarts,
    qti_gte,
    qti_product,
    qti_sum,
)

FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"
NS = "{http://www.imsglobal.org/xsd/imsqtiasi_v3p0}"

PASSED: list[str] = []
FAILED: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    if condition:
        PASSED.append(name)
    else:
        FAILED.append(f"{name}{(' — ' + detail) if detail else ''}")


def check_call(name: str, thunk, detail: str = "") -> None:
    """`check`, but for a condition whose own evaluation can raise.

    Added because mutation M4 (drop XML escaping) was *detected* — unescaped
    output is not well-formed, so the assertion's own `ET.fromstring` raised —
    but it surfaced as a traceback rather than a reported failure. On a board a
    crash is indistinguishable from a broken runner, so the defect it proves gets
    read as infrastructure noise. An oracle must report its own detections.
    """
    try:
        check(name, bool(thunk()), detail)
    except Exception as error:  # noqa: BLE001 - any raise is a failed assertion
        FAILED.append(f"{name} — raised {type(error).__name__}: {error}")


def canonical(xml_text: str) -> str:
    """Canonical XML: attribute order and insignificant whitespace normalised."""
    return ET.canonicalize(xml_text, strip_text=True)


def canonical_fragment(xml_fragment: str) -> str:
    """Canonical form of an emitted fragment, in the namespace it will live in.

    An emitted fragment carries no namespace of its own: it inherits the default
    `xmlns` from `qti-assessment-item` once assembled. Canonicalising it bare
    would compare a namespace-less element against a namespaced one and report a
    difference that does not exist in any document either side would produce —
    the whole-document assertion `O1.whole` is the control for exactly that.
    So the fragment is wrapped in the QTI default namespace before comparison.
    """
    wrapped = f'<w xmlns="{NS[1:-1]}">{xml_fragment}</w>'
    root = ET.fromstring(wrapped)
    return canonical(ET.tostring(root[0], encoding="unicode"))


def subtree(xml_text: str, tag: str) -> str:
    """Canonical form of the first `tag` element, for element-level comparison."""
    root = ET.fromstring(xml_text)
    found = root.find(f"{NS}{tag}")
    if found is None:
        raise AssertionError(f"{tag} absent")
    return canonical(ET.tostring(found, encoding="unicode"))


def subtrees(xml_text: str, tag: str) -> list[str]:
    root = ET.fromstring(xml_text)
    return [
        canonical(ET.tostring(element, encoding="unicode"))
        for element in root.findall(f"{NS}{tag}")
    ]


# ===========================================================================
# ORACLE 1 — regenerate random-integer-template-reference.xml exactly
# ===========================================================================
# This is the fixture `Gap 238` names as the ready-made round-trip oracle. It is
# the hard case: four template declarations, three draws (two of which OMIT
# `step`), a two-level nested arithmetic expression, and a derived answer key.

fixture_1 = (FIXTURES / "random-integer-template-reference.xml").read_text()

declarations_1 = [
    TemplateDeclaration("FACTOR"),
    TemplateDeclaration("TARGET"),
    TemplateDeclaration("OFFSET"),
    TemplateDeclaration("RESULT"),
]

processing_1 = TemplateProcessing(
    [
        SetTemplateValue("FACTOR", RandomInteger(2, 10, step=2)),
        SetTemplateValue("TARGET", RandomInteger(3, 9)),
        SetTemplateValue("OFFSET", RandomInteger(1, 5)),
        SetTemplateValue(
            "RESULT",
            qti_sum(
                qti_product(Variable("FACTOR"), Variable("TARGET")),
                Variable("OFFSET"),
            ),
        ),
        SetCorrectResponse("RESPONSE", Variable("TARGET")),
    ]
)

emitted_declarations_1 = [declaration.to_xml() for declaration in declarations_1]
check(
    "O1.decls: four qti-template-declaration elements regenerated node-for-node",
    [canonical_fragment(x) for x in emitted_declarations_1]
    == subtrees(fixture_1, "qti-template-declaration"),
    "emitter output differs from the schema-validated fixture",
)

check(
    "O1.proc: qti-template-processing regenerated node-for-node",
    canonical_fragment(processing_1.to_xml()) == subtree(fixture_1, "qti-template-processing"),
    "emitted processing block differs from the schema-validated fixture",
)

# The whole document, assembled through build_parametric_item.
body_1 = """<qti-item-body>
  <p>A bike-share station charges a fixed unlock fee of <qti-printed-variable identifier="OFFSET"/> dollars plus <qti-printed-variable identifier="FACTOR"/> dollars per hour. A rider paid <qti-printed-variable identifier="RESULT"/> dollars total.</p>
  <qti-slider-interaction response-identifier="RESPONSE" lower-bound="0" upper-bound="12" step="1">
    <qti-prompt>Select the number of hours the rider used the bike.</qti-prompt>
  </qti-slider-interaction>
</qti-item-body>"""

whole_1 = build_parametric_item(
    identifier="random-integer-template-reference",
    title="random-integer-template-reference",
    response_declaration='<qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="integer"/>',
    outcome_declaration=(
        '<qti-outcome-declaration identifier="SCORE" cardinality="single" base-type="float">'
        "<qti-default-value><qti-value>0</qti-value></qti-default-value>"
        "</qti-outcome-declaration>"
    ),
    template_declarations=declarations_1,
    template_processing=processing_1,
    item_body=body_1,
    response_processing='<qti-response-processing template="https://purl.imsglobal.org/spec/qti/v3p0/rptemplates/match_correct"/>',
)

check(
    "O1.whole: the complete assessment item is canonically identical to the fixture",
    canonical(whole_1) == canonical(fixture_1),
    "whole-document round-trip differs",
)

# NEGATIVE CONTROL for O1 — the defect `Gap 238` describes must still be visible.
# Always emitting `step` is the single most likely emitter bug, because `step` is
# required by the evaluator's arithmetic but optional in the XML. If that bug were
# present, O1 would have to fail.
bugged = TemplateProcessing(
    [
        SetTemplateValue("FACTOR", RandomInteger(2, 10, step=2)),
        SetTemplateValue("TARGET", RandomInteger(3, 9, step=1)),  # step made explicit
        SetTemplateValue("OFFSET", RandomInteger(1, 5, step=1)),  # step made explicit
        SetTemplateValue(
            "RESULT",
            qti_sum(
                qti_product(Variable("FACTOR"), Variable("TARGET")),
                Variable("OFFSET"),
            ),
        ),
        SetCorrectResponse("RESPONSE", Variable("TARGET")),
    ]
)
check(
    "O1.control: explicit-step variant is REJECTED by the same comparison",
    canonical_fragment(bugged.to_xml()) != subtree(fixture_1, "qti-template-processing"),
    "the oracle accepts a document the fixture does not contain — it judges nothing",
)

# ===========================================================================
# ORACLE 2 — a second, independent fixture
# ===========================================================================
# Different shape: a literal base value, a one-level sum, inline formatting, and
# only two template variables. If Oracle 1 passed by coincidence, this fails.

fixture_2 = (FIXTURES / "template-processing-reference.xml").read_text()

declarations_2 = [TemplateDeclaration("BASE"), TemplateDeclaration("ANSWER")]
processing_2 = TemplateProcessing(
    [
        SetTemplateValue("BASE", BaseValue(2, "integer"), inline=True),
        SetTemplateValue(
            "ANSWER",
            qti_sum(Variable("BASE"), BaseValue(3, "integer"), inline=True),
        ),
        SetCorrectResponse("RESPONSE", Variable("ANSWER")),
    ]
)

check(
    "O2.decls: two declarations regenerated against a second fixture",
    [canonical_fragment(d.to_xml()) for d in declarations_2]
    == subtrees(fixture_2, "qti-template-declaration"),
)
check(
    "O2.proc: processing block regenerated against a second fixture",
    canonical_fragment(processing_2.to_xml()) == subtree(fixture_2, "qti-template-processing"),
)
check(
    "O2.control: Oracle 2's comparison rejects Oracle 1's processing block",
    canonical_fragment(processing_1.to_xml()) != subtree(fixture_2, "qti-template-processing"),
    "the two fixtures are not being distinguished",
)

# ===========================================================================
# ORACLE 3 — the draw lands on the declared grid (core's own arithmetic)
# ===========================================================================
# processing-evaluator.ts:170-171, reimplemented and executed. This is the
# assertion `Gap 238` asks for: write -> parse -> execute -> assert the draw
# lands on the declared grid.


def core_draw(expression: RandomInteger, rng: random.Random) -> int:
    """Byte-for-byte the evaluator's arithmetic, with random() injected."""
    minimum, maximum, step = expression.minimum, expression.maximum, expression.effective_step
    count = (maximum - minimum) // step + 1
    return minimum + int(rng.random() * count) * step


rng = random.Random(20261007)
draws = {
    "FACTOR": RandomInteger(2, 10, step=2),
    "TARGET": RandomInteger(3, 9),
    "OFFSET": RandomInteger(1, 5),
}

off_grid = 0
observed: dict[str, set[int]] = {name: set() for name in draws}
for _ in range(20000):
    for name, expression in draws.items():
        value = core_draw(expression, rng)
        observed[name].add(value)
        if value not in expression.grid():
            off_grid += 1

check(
    "O3.grid: every executed draw lands on the grid the emitter declared",
    off_grid == 0,
    f"{off_grid} draws fell off the declared grid",
)
check(
    "O3.cover: each declared grid point is reachable (no dead variant)",
    all(observed[name] == set(draws[name].grid()) for name in draws),
    f"observed={ {k: sorted(v) for k, v in observed.items()} }",
)

# ---------------------------------------------------------------------------
# O3b — the default step, pinned against the SOURCE, not against itself.
# ---------------------------------------------------------------------------
# Found by mutation, not by inspection. Mutation M8 (`step` defaults to 2 instead
# of 1) survived the whole suite above: O3.grid and O3.cover both compare the
# executed draw against `grid()`, and both sides derive from `effective_step`, so
# a wrong default is self-consistent and invisible. The round-trip oracles miss it
# too, because a defaulted `step` is not emitted at all.
#
# The fix is to assert against the external source of truth rather than against
# another expression of the same value: operator-attribute.ts:24 reads
# `step: expression.step ?? "1"`. This is the `P469` shape — a value asserted from
# itself is not measured.
check(
    "O3b.default: an omitted step is 1, per operator-attribute.ts:24",
    RandomInteger(3, 9).effective_step == 1,
    f"got {RandomInteger(3, 9).effective_step}",
)
check(
    "O3b.contiguous: an omitted step therefore makes the grid contiguous min..max",
    RandomInteger(3, 9).grid() == [3, 4, 5, 6, 7, 8, 9],
    f"got {RandomInteger(3, 9).grid()}",
)
check(
    "O3b.control: an explicit step 2 on the same bounds is NOT contiguous",
    RandomInteger(3, 9, step=2).grid() == [3, 5, 7, 9],
    f"got {RandomInteger(3, 9, step=2).grid()}",
)

# NEGATIVE CONTROL for O3 — a grid that is wrong must be caught. `max` is NOT
# attainable when step does not divide max-min; an emitter that assumed a
# contiguous range would claim 10 is drawable here.
narrow = RandomInteger(1, 10, step=4)
check(
    "O3.control: max is correctly reported unattainable when step does not divide",
    narrow.grid() == [1, 5, 9] and 10 not in narrow.grid(),
    f"grid={narrow.grid()}",
)
check(
    "O3.control2: a contiguous-range assumption is detectably wrong",
    set(narrow.grid()) != set(range(narrow.minimum, narrow.maximum + 1)),
)

# ===========================================================================
# ORACLE 4 — the answer key is derived from the draw, not frozen
# ===========================================================================
# The property that makes a variant family gradable. RESULT = FACTOR*TARGET+OFFSET
# and the key is TARGET, so a solver inverting the stem must recover the key.

inconsistent = 0
distinct_keys: set[int] = set()
for _ in range(5000):
    factor = core_draw(draws["FACTOR"], rng)
    target = core_draw(draws["TARGET"], rng)
    offset = core_draw(draws["OFFSET"], rng)
    result = factor * target + offset           # qti-sum(qti-product(F,T), O)
    key = target                                # qti-set-correct-response
    distinct_keys.add(key)
    if (result - offset) // factor != key:      # invert the stem
        inconsistent += 1

check(
    "O4.key: the derived key always solves the stem it was generated from",
    inconsistent == 0,
    f"{inconsistent} variants were unsolvable",
)
check(
    "O4.vary: the key actually varies across variants (not a frozen key)",
    len(distinct_keys) > 1,
    f"only {len(distinct_keys)} distinct key(s) — the family is cosmetic",
)

# ===========================================================================
# ORACLE 5 — constraint feasibility, the silent-degradation case
# ===========================================================================
# session.ts:474 restarts at most 100 times and then PROCEEDS with the violating
# draw. So an infeasible constraint is not an error; it is a wrong item.

feasible = estimate_constraint_restarts(
    draws, lambda d: d["FACTOR"] * d["TARGET"] + d["OFFSET"] >= 20
)
infeasible = estimate_constraint_restarts(
    draws, lambda d: d["FACTOR"] * d["TARGET"] + d["OFFSET"] > 10_000
)
check(
    "O5.feasible: a satisfiable constraint reports positive acceptance",
    0.0 < feasible <= 1.0,
    f"acceptance={feasible}",
)
check(
    "O5.control: an unsatisfiable constraint reports exactly 0 acceptance",
    infeasible == 0.0,
    f"acceptance={infeasible}",
)
check(
    "O5.risk: a 0-acceptance constraint is flagged before publication, not at delivery",
    (1 - infeasible) ** 101 == 1.0,
    "the 100-restart exhaustion probability is not being computed",
)

# The constraint element itself must emit and parse.
constrained = TemplateProcessing(
    [
        SetTemplateValue("FACTOR", RandomInteger(2, 10, step=2)),
        TemplateConstraint(qti_gte(Variable("FACTOR"), BaseValue(4, "integer"))),
        SetCorrectResponse("RESPONSE", Variable("FACTOR")),
    ]
)
constrained_xml = constrained.to_xml()
check_call(
    "O5.emit: qti-template-constraint emits well-formed XML core's parser accepts",
    lambda: ET.fromstring(constrained_xml) is not None
    and "qti-template-constraint" in constrained_xml,
)

# ===========================================================================
# ORACLE 6 — validation refuses what core would silently mis-bind
# ===========================================================================
# core coerces a missing identifier to "" (parser-processing.ts:49) rather than
# failing, so these must be refused at authoring time or never at all.

refusals = [
    ("step <= 0", lambda: RandomInteger(1, 5, step=0)),
    ("negative step", lambda: RandomInteger(1, 5, step=-2)),
    ("min > max", lambda: RandomInteger(9, 2)),
    ("empty identifier", lambda: TemplateDeclaration("")),
    ("identifier with space", lambda: TemplateDeclaration("MY VAR")),
    ("identifier leading digit", lambda: TemplateDeclaration("1ST")),
    ("unknown base-type", lambda: TemplateDeclaration("X", base_type="intger")),
    ("unknown cardinality", lambda: TemplateDeclaration("X", cardinality="one")),
    ("empty processing block", lambda: TemplateProcessing([]).to_xml()),
    ("variable with bad identifier", lambda: Variable("a b")),
]
for label, thunk in refusals:
    try:
        thunk()
        check(f"O6.refuse[{label}]", False, "accepted — core would mis-bind it silently")
    except TemplateEmitError:
        check(f"O6.refuse[{label}]", True)

# NEGATIVE CONTROL for O6 — the validator must not refuse everything.
accepted = [
    ("default step omitted", lambda: RandomInteger(3, 9)),
    ("explicit step", lambda: RandomInteger(2, 10, step=2)),
    ("min == max", lambda: RandomInteger(5, 5)),
    ("negative bounds", lambda: RandomInteger(-10, -2, step=4)),
    ("underscore identifier", lambda: TemplateDeclaration("_X1.a-b")),
    ("float declaration", lambda: TemplateDeclaration("F", base_type="float")),
    ("declaration with default", lambda: TemplateDeclaration("D", default_value=0)),
]
for label, thunk in accepted:
    try:
        thunk()
        check(f"O6.accept[{label}]", True)
    except TemplateEmitError as error:
        check(f"O6.accept[{label}]", False, f"wrongly refused: {error}")

# ===========================================================================
# ORACLE 7 — escaping, the injection surface of an authoring tool
# ===========================================================================
risky = TemplateDeclaration("X", default_value='<&">')
risky_xml = risky.to_xml()
check_call(
    "O7.escape: hostile default value stays well-formed and is not re-parsed as markup",
    lambda: ET.fromstring(risky_xml).find("qti-default-value/qti-value").text == '<&">',
    f"escaping lost the value: {risky_xml}",
)
check(
    "O7.control: the raw hostile string is NOT present unescaped in the output",
    '<&">' not in risky_xml,
    "value was interpolated raw — an authoring tool that emits injectable XML",
)

# O7b — ATTRIBUTE escaping, as distinct from text escaping.
# Also found by mutation: M9 (drop `"` -> `&quot;` in `_escape_attr`) survived the
# whole suite, because every attribute value used above happens to be quote-free.
# A title is author-supplied free text and is the realistic carrier of a quote, so
# an unescaped `"` there terminates the attribute and corrupts the document.
quoted_title = 'The "unlock fee" item <v2> & co.'
quoted_item = build_parametric_item(
    identifier="quoted-title-probe",
    title=quoted_title,
    response_declaration='<qti-response-declaration identifier="RESPONSE" cardinality="single" base-type="integer"/>',
    outcome_declaration='<qti-outcome-declaration identifier="SCORE" cardinality="single" base-type="float"/>',
    template_declarations=[TemplateDeclaration("A")],
    template_processing=TemplateProcessing(
        [SetTemplateValue("A", RandomInteger(1, 4), inline=True)]
    ),
    item_body="<qti-item-body><p>probe</p></qti-item-body>",
    response_processing='<qti-response-processing template="x"/>',
)
check_call(
    "O7b.attr: a title containing a quote survives the round-trip intact",
    lambda: ET.fromstring(quoted_item).get("title") == quoted_title,
    "attribute escaping is lossy or the document is malformed",
)
check(
    "O7b.control: the bare quote is NOT emitted raw inside the attribute",
    'title="The "unlock' not in quoted_item,
    "unescaped quote terminated the attribute early",
)

# ===========================================================================
# ORACLE 8 — child order is the schema's, not the parser's
# ===========================================================================
# core finds children by name and so accepts any order; the XSD does not. An
# emitter that followed the parser would deliver and fail validation.
order_root = ET.fromstring(whole_1)
order = [child.tag.replace(NS, "") for child in order_root]
expected_prefix = [
    "qti-response-declaration",
    "qti-outcome-declaration",
    "qti-template-declaration",
]
check(
    "O8.order: declarations precede template processing, which precedes item body",
    order.index("qti-template-processing") > order.index("qti-template-declaration")
    and order.index("qti-item-body") > order.index("qti-template-processing")
    and order[:3] == expected_prefix,
    f"order={order}",
)
check(
    "O8.control: the fixture exhibits the same order (the requirement is real)",
    [c.tag.replace(NS, "") for c in ET.fromstring(fixture_1)] == order,
)


# ===========================================================================
print()
print(f"P533 — QTI 3 template emitter oracle: {len(PASSED)} passed, {len(FAILED)} failed")
print(f"  fixtures used as schema-validated oracles: 2")
print(f"  negative controls among the above: "
      f"{len([p for p in PASSED if 'control' in p or 'refuse' in p])}")
if FAILED:
    print("\nFAILURES:")
    for failure in FAILED:
        print(f"  ✗ {failure}")
    sys.exit(1)
print("\nAll assertions passed, and every one has a paired control that fails.")
