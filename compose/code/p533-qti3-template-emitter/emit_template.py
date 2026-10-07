"""P533 — a QTI 3 template-declaration / template-processing emitter.

Closes `Gap 238`. The gap, declared by pass 42 (`P527`), is that
`LongsightGroup/qti3` (MIT, v0.13.2) can **deliver** parametric item variants —
`packages/core` implements declaration parsing, a real `randomInteger` draw over
`min`/`max`/`step`, answer keys derived from the draw, and a constraint-retry loop
up to 100 restarts — but cannot **author** them: `packages/writer` has 0 of 33
exports referencing `qti-template-declaration` / `qti-template-processing`.

This module is the missing authoring half, written against the grammar read from
core's own parser rather than from the QTI specification prose, so the contract it
targets is the contract the runtime actually enforces.

Grammar sources, all read from the cloned tree at HEAD `0ca7d6fc` (2026-10-07):

  packages/core/src/parser.ts                  childElements(node, "qti-template-declaration")
                                               childElements(node, "qti-template-processing")[0]
  packages/core/src/parser-processing.ts:47    qti-set-template-value   -> setTemplateValue
  packages/core/src/parser-processing.ts:73    qti-set-correct-response -> setCorrectResponse
  packages/core/src/parser-processing.ts:109   qti-template-constraint  -> templateConstraint
  packages/core/src/parser-processing.ts:258   qti-random-integer       -> min / max / step
  packages/core/src/operator-attribute.ts:24   min defaults "0", step defaults "1", max required
  packages/core/src/processing-evaluator.ts:163
        count = floor((max - min) / step) + 1
        draw  = min + floor(random() * count) * step
  packages/core/src/session.ts:449-476         constraint failure resets and restarts, `restarts <= 100`
  packages/core/src/validation-random-expression.ts
        step must be > 0; min must be <= max

NOTE ON SCOPE. This is a Python emitter, executable and tested here. The upstream
contribution `Gap 238` names is a TypeScript `buildQti3TemplateDeclaration` in
`packages/writer`; the TypeScript port is in `writer-contribution.ts` in this
directory and is **not executed** here, because installing a third-party
repository's dependencies is not permitted in this environment. The Python module
is the executed artefact and the oracle; the TypeScript file is the deliverable
shaped for upstream and is marked unexecuted wherever it is cited.

Stdlib only. No third-party imports, by `P237`'s shape: an instrument that needs
a dependency to run is an instrument that does not run.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Sequence

# ---------------------------------------------------------------------------
# Identifier and attribute discipline
# ---------------------------------------------------------------------------

# QTI identifiers are XML NCNames. core does not reject a bad identifier — it
# coerces a missing one to "" (parser-processing.ts:49) — so a malformed
# identifier becomes a silent mis-binding at delivery rather than a parse error.
# The emitter refuses it instead. This is the `P473` rule applied at the source:
# a control that is not in the path of new output is documentation.
_NCNAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_.\-]*$")

_BASE_TYPES = frozenset(
    {
        "identifier", "boolean", "integer", "float", "string", "point",
        "pair", "directedPair", "duration", "file", "uri",
    }
)
_CARDINALITIES = frozenset({"single", "multiple", "ordered", "record"})


class TemplateEmitError(ValueError):
    """Raised when a requested document could not be emitted as valid QTI 3."""


def _check_identifier(identifier: str, what: str) -> str:
    if not isinstance(identifier, str) or not _NCNAME.match(identifier):
        raise TemplateEmitError(
            f"{what} must be an XML NCName (letter or underscore, then "
            f"letters/digits/._-); got {identifier!r}"
        )
    return identifier


def _escape_attr(value: str) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _escape_text(value: str) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _indent(xml: str, level: int) -> str:
    pad = "  " * level
    return "\n".join(pad + line if line else line for line in xml.split("\n"))


# ---------------------------------------------------------------------------
# Expressions
# ---------------------------------------------------------------------------


class Expression:
    """A QTI processing expression that can render itself as XML."""

    def to_xml(self) -> str:  # pragma: no cover - interface
        raise NotImplementedError


@dataclass(frozen=True)
class RandomInteger(Expression):
    """`qti-random-integer`. The draw is a grid, not a range — see `grid()`."""

    minimum: int
    maximum: int
    step: int | None = None

    def __post_init__(self) -> None:
        for name, value in (("min", self.minimum), ("max", self.maximum)):
            if not isinstance(value, int) or isinstance(value, bool):
                raise TemplateEmitError(f"qti-random-integer {name} must be an int")
        # validation-random-expression.ts: min <= max, step > 0.
        if self.minimum > self.maximum:
            raise TemplateEmitError(
                f"qti-random-integer requires min <= max; got min={self.minimum} "
                f"max={self.maximum}"
            )
        if self.step is not None:
            if not isinstance(self.step, int) or isinstance(self.step, bool):
                raise TemplateEmitError("qti-random-integer step must be an int")
            if self.step <= 0:
                raise TemplateEmitError(
                    f"qti-random-integer requires step > 0; got step={self.step}"
                )

    @property
    def effective_step(self) -> int:
        """operator-attribute.ts:24 — a missing `step` is `1`, not "no step"."""
        return 1 if self.step is None else self.step

    def grid(self) -> list[int]:
        """Exactly the values core can draw.

        processing-evaluator.ts:170-171. Note the consequence the attribute names
        hide: when `step` does not divide `max - min`, `max` is NOT attainable.
        `min=1 max=10 step=4` draws from {1, 5, 9}; 10 never occurs. An author
        who reads `max` as "the largest value" authors a different item from the
        one delivered, so the emitter exposes the grid and the tests assert on it.
        """
        count = (self.maximum - self.minimum) // self.effective_step + 1
        return [self.minimum + k * self.effective_step for k in range(count)]

    def to_xml(self) -> str:
        attrs = f'min="{self.minimum}" max="{self.maximum}"'
        # Emit `step` only when it was authored. The fixture omits it on two of
        # three draws, so always emitting it would break round-trip equality
        # against a document the upstream schema gate has already validated.
        if self.step is not None:
            attrs += f' step="{self.step}"'
        return f"<qti-random-integer {attrs}/>"


@dataclass(frozen=True)
class Variable(Expression):
    """`qti-variable` — a reference to a template, response or outcome variable."""

    identifier: str

    def __post_init__(self) -> None:
        _check_identifier(self.identifier, "qti-variable identifier")

    def to_xml(self) -> str:
        return f'<qti-variable identifier="{_escape_attr(self.identifier)}"/>'


@dataclass(frozen=True)
class BaseValue(Expression):
    """`qti-base-value` — a typed literal."""

    value: object
    base_type: str = "integer"

    def __post_init__(self) -> None:
        if self.base_type not in _BASE_TYPES:
            raise TemplateEmitError(f"unknown base-type {self.base_type!r}")

    def to_xml(self) -> str:
        return (
            f'<qti-base-value base-type="{_escape_attr(self.base_type)}">'
            f"{_escape_text(self.value)}</qti-base-value>"
        )


@dataclass(frozen=True)
class Operator(Expression):
    """An n-ary arithmetic/logical operator such as `qti-sum` or `qti-product`."""

    name: str
    operands: Sequence[Expression]
    inline: bool = False

    def to_xml(self) -> str:
        if not self.operands:
            raise TemplateEmitError(f"{self.name} requires at least one operand")
        if self.inline:
            inner = "".join(operand.to_xml() for operand in self.operands)
            return f"<{self.name}>{inner}</{self.name}>"
        inner = "\n".join(_indent(operand.to_xml(), 1) for operand in self.operands)
        return f"<{self.name}>\n{inner}\n</{self.name}>"


def qti_sum(*operands: Expression, inline: bool = False) -> Operator:
    return Operator("qti-sum", operands, inline=inline)


def qti_product(*operands: Expression, inline: bool = False) -> Operator:
    return Operator("qti-product", operands, inline=inline)


def qti_subtract(left: Expression, right: Expression, inline: bool = False) -> Operator:
    return Operator("qti-subtract", (left, right), inline=inline)


def qti_gte(left: Expression, right: Expression, inline: bool = False) -> Operator:
    return Operator("qti-gte", (left, right), inline=inline)


def qti_not_equal(left: Expression, right: Expression, inline: bool = False) -> Operator:
    return Operator("qti-not-equal", (left, right), inline=inline)


# ---------------------------------------------------------------------------
# Declarations
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TemplateDeclaration:
    """`qti-template-declaration` — the element `packages/writer` cannot emit.

    This is the `buildQti3TemplateDeclaration` of `Gap 238`'s remedy.
    """

    identifier: str
    base_type: str = "integer"
    cardinality: str = "single"
    default_value: object | None = None
    param_variable: bool | None = None
    math_variable: bool | None = None

    def __post_init__(self) -> None:
        _check_identifier(self.identifier, "qti-template-declaration identifier")
        if self.base_type not in _BASE_TYPES:
            raise TemplateEmitError(f"unknown base-type {self.base_type!r}")
        if self.cardinality not in _CARDINALITIES:
            raise TemplateEmitError(f"unknown cardinality {self.cardinality!r}")

    def to_xml(self) -> str:
        attrs = (
            f'identifier="{_escape_attr(self.identifier)}" '
            f'cardinality="{_escape_attr(self.cardinality)}" '
            f'base-type="{_escape_attr(self.base_type)}"'
        )
        # Attribute order follows the XSD's declared order for these optional
        # attributes; xmllint is order-insensitive for attributes but the
        # round-trip oracle compares canonical XML, which sorts them anyway.
        if self.param_variable is not None:
            attrs += f' param-variable="{str(self.param_variable).lower()}"'
        if self.math_variable is not None:
            attrs += f' math-variable="{str(self.math_variable).lower()}"'
        if self.default_value is None:
            return f"<qti-template-declaration {attrs}/>"
        return (
            f"<qti-template-declaration {attrs}>"
            f"<qti-default-value><qti-value>{_escape_text(self.default_value)}"
            f"</qti-value></qti-default-value>"
            f"</qti-template-declaration>"
        )


# ---------------------------------------------------------------------------
# Template rules
# ---------------------------------------------------------------------------


class TemplateRule:
    def to_xml(self) -> str:  # pragma: no cover - interface
        raise NotImplementedError


@dataclass(frozen=True)
class SetTemplateValue(TemplateRule):
    """`qti-set-template-value` — bind a template variable to a drawn value."""

    identifier: str
    expression: Expression
    inline: bool = False

    def __post_init__(self) -> None:
        _check_identifier(self.identifier, "qti-set-template-value identifier")

    def to_xml(self) -> str:
        ident = _escape_attr(self.identifier)
        if self.inline:
            return (
                f'<qti-set-template-value identifier="{ident}">'
                f"{self.expression.to_xml()}</qti-set-template-value>"
            )
        inner = _indent(self.expression.to_xml(), 1)
        return (
            f'<qti-set-template-value identifier="{ident}">\n'
            f"{inner}\n</qti-set-template-value>"
        )


@dataclass(frozen=True)
class SetCorrectResponse(TemplateRule):
    """`qti-set-correct-response` — derive the answer key from the draw.

    This is the rule that makes a variant family *gradable*. Without it every
    variant shares one authored key and all but one variant is marked wrong.
    """

    identifier: str
    expression: Expression
    inline: bool = True

    def __post_init__(self) -> None:
        _check_identifier(self.identifier, "qti-set-correct-response identifier")

    def to_xml(self) -> str:
        ident = _escape_attr(self.identifier)
        if self.inline:
            return (
                f'<qti-set-correct-response identifier="{ident}">'
                f"{self.expression.to_xml()}</qti-set-correct-response>"
            )
        inner = _indent(self.expression.to_xml(), 1)
        return (
            f'<qti-set-correct-response identifier="{ident}">\n'
            f"{inner}\n</qti-set-correct-response>"
        )


@dataclass(frozen=True)
class TemplateConstraint(TemplateRule):
    """`qti-template-constraint` — reject a draw and restart.

    core restarts at most 100 times (session.ts:474) and then **proceeds with the
    failing draw** rather than raising. A constraint satisfied by too few points
    on the grid therefore degrades silently into a bad item, which is why
    `estimate_constraint_restarts` exists in this module.
    """

    expression: Expression
    inline: bool = False

    def to_xml(self) -> str:
        if self.inline:
            return f"<qti-template-constraint>{self.expression.to_xml()}</qti-template-constraint>"
        inner = _indent(self.expression.to_xml(), 1)
        return f"<qti-template-constraint>\n{inner}\n</qti-template-constraint>"


# ---------------------------------------------------------------------------
# Template processing block
# ---------------------------------------------------------------------------


@dataclass
class TemplateProcessing:
    """`qti-template-processing` — the ordered rule list core executes."""

    rules: list[TemplateRule] = field(default_factory=list)

    def to_xml(self) -> str:
        if not self.rules:
            # core tolerates an empty block; an author almost never means it.
            raise TemplateEmitError(
                "qti-template-processing with no rules declares variants and "
                "produces none; omit the element instead"
            )
        inner = "\n".join(_indent(rule.to_xml(), 1) for rule in self.rules)
        return f"<qti-template-processing>\n{inner}\n</qti-template-processing>"


def build_template_declaration(*args, **kwargs) -> str:
    """Emit one `qti-template-declaration`. The named remedy of `Gap 238`."""
    return TemplateDeclaration(*args, **kwargs).to_xml()


def build_template_processing(rules: Sequence[TemplateRule]) -> str:
    """Emit one `qti-template-processing` block."""
    return TemplateProcessing(list(rules)).to_xml()


# ---------------------------------------------------------------------------
# The draw, reimplemented from core, for pre-publication checking
# ---------------------------------------------------------------------------


def estimate_constraint_restarts(
    draws: dict[str, RandomInteger],
    predicate,
) -> float:
    """Fraction of the cartesian product of the declared grids that satisfies
    `predicate`.

    Returned as a probability in [0, 1]. core restarts up to 100 times, so a
    predicate with acceptance probability `p` fails to find a satisfying draw with
    probability `(1 - p) ** 101`. At `p = 0.05` that is ~0.5%; at `p = 0.001` it is
    ~90%, and core then delivers the *violating* draw. An author cannot see this
    from the XML, so it is computed here rather than discovered in production.
    """
    import itertools

    names = list(draws)
    grids = [draws[name].grid() for name in names]
    total = 0
    accepted = 0
    for combination in itertools.product(*grids):
        total += 1
        if predicate(dict(zip(names, combination))):
            accepted += 1
    return accepted / total if total else 0.0


# ---------------------------------------------------------------------------
# Whole-item assembly
# ---------------------------------------------------------------------------

_QTI_NS = "http://www.imsglobal.org/xsd/imsqtiasi_v3p0"


def build_parametric_item(
    *,
    identifier: str,
    title: str,
    response_declaration: str,
    outcome_declaration: str,
    template_declarations: Sequence[TemplateDeclaration],
    template_processing: TemplateProcessing,
    item_body: str,
    response_processing: str,
    language: str = "en",
    time_dependent: bool = False,
) -> str:
    """Assemble a complete parametric `qti-assessment-item`.

    Child order is the XSD's required sequence: response declarations, outcome
    declarations, template declarations, template processing, item body, response
    processing. core's parser is order-insensitive (it uses `childElements` by
    name), but the schema is not, so emitting in parser order would produce a
    document that delivers and does not validate.
    """
    _check_identifier(identifier, "qti-assessment-item identifier")
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<qti-assessment-item xmlns="{_QTI_NS}" '
        f'identifier="{_escape_attr(identifier)}" title="{_escape_attr(title)}" '
        f'time-dependent="{str(time_dependent).lower()}" '
        f'xml:lang="{_escape_attr(language)}">',
        _indent(response_declaration, 1),
        _indent(outcome_declaration, 1),
    ]
    for declaration in template_declarations:
        parts.append(_indent(declaration.to_xml(), 1))
    parts.append(_indent(template_processing.to_xml(), 1))
    parts.append(_indent(item_body, 1))
    parts.append(_indent(response_processing, 1))
    parts.append("</qti-assessment-item>")
    return "\n".join(parts) + "\n"
