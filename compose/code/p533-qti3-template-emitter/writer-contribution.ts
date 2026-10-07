/**
 * P533 — `buildQti3TemplateDeclaration` and `buildQti3TemplateProcessing`,
 * shaped for contribution to `LongsightGroup/qti3`'s `packages/writer`.
 *
 * This is the artefact `Gap 238` names. `qti3` is MIT (© 2026 Longsight, Inc.),
 * so this is a contribution rather than a procurement.
 *
 * 🔴 STATED LIMIT, and it is the whole caveat on this file: THIS TYPESCRIPT IS
 * NOT EXECUTED in this environment. Installing a third-party repository's
 * dependencies is out of scope here, which is the same limit pass 42 recorded on
 * `P527`. The *executed and tested* artefact of `P533` is `emit_template.py` in
 * this directory, whose oracle regenerates two schema-gate-validated fixtures
 * node-for-node and survives an 11-mutation matrix. This file is the same
 * emitter expressed in the host project's idiom so that the upstream diff is a
 * review rather than a translation. 🔵 Whoever lands it upstream must run
 * `pnpm test` there first — `Gap 238` records that prerequisite.
 *
 * Imports are verified to exist at HEAD `0ca7d6fc` (2026-10-07):
 *   ./xml.js         -> escapeXmlAttribute, escapeXmlText, indentXml   (xml.ts:3,29)
 *   ./identifier.js  -> assertQtiIdentifier                            (identifier.ts:5)
 *   ./diagnostics.js -> writerDiagnostic                               (diagnostics.ts:6)
 *
 * Grammar targets core's parser, not the specification prose:
 *   parser.ts:139-148, parser-processing.ts:47/73/109/258,
 *   operator-attribute.ts:24, processing-evaluator.ts:163-172,
 *   session.ts:449-476, validation-random-expression.ts
 */

import { assertQtiIdentifier } from "./identifier.js";
import { writerDiagnostic } from "./diagnostics.js";
import { escapeXmlAttribute, escapeXmlText, indentXml } from "./xml.js";
import type { Qti3WriterDiagnostic } from "./types.js";

export type Qti3BaseType =
  | "identifier"
  | "boolean"
  | "integer"
  | "float"
  | "string"
  | "point"
  | "pair"
  | "directedPair"
  | "duration"
  | "file"
  | "uri";

export type Qti3Cardinality = "single" | "multiple" | "ordered" | "record";

export interface Qti3TemplateDeclarationInput {
  readonly identifier: string;
  readonly baseType?: Qti3BaseType;
  readonly cardinality?: Qti3Cardinality;
  readonly defaultValue?: string | number | boolean;
  readonly paramVariable?: boolean;
  readonly mathVariable?: boolean;
}

/** A processing expression. Discriminated so the renderer stays total. */
export type Qti3TemplateExpression =
  | { readonly kind: "randomInteger"; readonly min: number; readonly max: number; readonly step?: number }
  | { readonly kind: "randomFloat"; readonly min: number; readonly max: number }
  | { readonly kind: "variable"; readonly identifier: string }
  | { readonly kind: "baseValue"; readonly baseType: Qti3BaseType; readonly value: string | number | boolean }
  | { readonly kind: "operator"; readonly name: string; readonly operands: readonly Qti3TemplateExpression[] };

export type Qti3TemplateRule =
  | { readonly kind: "setTemplateValue"; readonly identifier: string; readonly expression: Qti3TemplateExpression }
  | { readonly kind: "setDefaultValue"; readonly identifier: string; readonly expression: Qti3TemplateExpression }
  | { readonly kind: "setCorrectResponse"; readonly identifier: string; readonly expression: Qti3TemplateExpression }
  | { readonly kind: "templateConstraint"; readonly expression: Qti3TemplateExpression }
  | { readonly kind: "exitTemplate" };

const BASE_TYPES = new Set<string>([
  "identifier", "boolean", "integer", "float", "string",
  "point", "pair", "directedPair", "duration", "file", "uri",
]);
const CARDINALITIES = new Set<string>(["single", "multiple", "ordered", "record"]);

/**
 * The grid `qti-random-integer` can actually draw from.
 *
 * processing-evaluator.ts:170-171. Exported because the attribute names mislead:
 * when `step` does not divide `max - min`, `max` is NOT attainable.
 * `{min: 1, max: 10, step: 4}` draws from `[1, 5, 9]`.
 */
export function qti3RandomIntegerGrid(min: number, max: number, step?: number): number[] {
  const effectiveStep = step ?? 1; // operator-attribute.ts:24
  const count = Math.floor((max - min) / effectiveStep) + 1;
  return Array.from({ length: count }, (_, index) => min + index * effectiveStep);
}

export function validateQti3TemplateDeclaration(
  input: Qti3TemplateDeclarationInput,
): Qti3WriterDiagnostic[] {
  const diagnostics: Qti3WriterDiagnostic[] = [];
  if (input.baseType !== undefined && !BASE_TYPES.has(input.baseType))
    diagnostics.push(
      writerDiagnostic("templateDeclaration.baseType", `Unknown base-type ${input.baseType}.`),
    );
  if (input.cardinality !== undefined && !CARDINALITIES.has(input.cardinality))
    diagnostics.push(
      writerDiagnostic("templateDeclaration.cardinality", `Unknown cardinality ${input.cardinality}.`),
    );
  return diagnostics;
}

/**
 * Emit one `qti-template-declaration`.
 *
 * `step` is emitted only when authored, because `packages/fixtures/xml/
 * random-integer-template-reference.xml` omits it on two of three draws and that
 * fixture is validated by the repository's own schema gate. Always emitting it
 * would still deliver correctly but would no longer round-trip the fixture.
 */
export function buildQti3TemplateDeclaration(input: Qti3TemplateDeclarationInput): string {
  const identifier = assertQtiIdentifier(input.identifier, "Template declaration identifier");
  const baseType = input.baseType ?? "integer";
  const cardinality = input.cardinality ?? "single";

  let attrs =
    `identifier="${escapeXmlAttribute(identifier)}" ` +
    `cardinality="${escapeXmlAttribute(cardinality)}" ` +
    `base-type="${escapeXmlAttribute(baseType)}"`;
  if (input.paramVariable !== undefined) attrs += ` param-variable="${input.paramVariable}"`;
  if (input.mathVariable !== undefined) attrs += ` math-variable="${input.mathVariable}"`;

  if (input.defaultValue === undefined) return `<qti-template-declaration ${attrs}/>`;
  return (
    `<qti-template-declaration ${attrs}>` +
    `<qti-default-value><qti-value>${escapeXmlText(String(input.defaultValue))}</qti-value></qti-default-value>` +
    `</qti-template-declaration>`
  );
}

function renderExpression(expression: Qti3TemplateExpression): string {
  switch (expression.kind) {
    case "randomInteger": {
      if (expression.min > expression.max)
        throw new Error("qti-random-integer requires min to be less than or equal to max.");
      if (expression.step !== undefined && expression.step <= 0)
        throw new Error("qti-random-integer requires step to be greater than 0.");
      const step = expression.step === undefined ? "" : ` step="${expression.step}"`;
      return `<qti-random-integer min="${expression.min}" max="${expression.max}"${step}/>`;
    }
    case "randomFloat": {
      if (expression.min > expression.max)
        throw new Error("qti-random-float requires min to be less than or equal to max.");
      return `<qti-random-float min="${expression.min}" max="${expression.max}"/>`;
    }
    case "variable": {
      const identifier = assertQtiIdentifier(expression.identifier, "Variable identifier");
      return `<qti-variable identifier="${escapeXmlAttribute(identifier)}"/>`;
    }
    case "baseValue":
      return (
        `<qti-base-value base-type="${escapeXmlAttribute(expression.baseType)}">` +
        `${escapeXmlText(String(expression.value))}</qti-base-value>`
      );
    case "operator": {
      if (expression.operands.length === 0)
        throw new Error(`${expression.name} requires at least one operand.`);
      const inner = expression.operands
        .map((operand) => indentXml(renderExpression(operand), 2))
        .join("\n");
      return `<${expression.name}>\n${inner}\n</${expression.name}>`;
    }
  }
}

function renderRule(rule: Qti3TemplateRule): string {
  switch (rule.kind) {
    case "exitTemplate":
      return "<qti-exit-template/>";
    case "templateConstraint":
      return (
        `<qti-template-constraint>\n` +
        `${indentXml(renderExpression(rule.expression), 2)}\n` +
        `</qti-template-constraint>`
      );
    default: {
      const element =
        rule.kind === "setTemplateValue"
          ? "qti-set-template-value"
          : rule.kind === "setDefaultValue"
            ? "qti-set-default-value"
            : "qti-set-correct-response";
      const identifier = assertQtiIdentifier(rule.identifier, `${element} identifier`);
      return (
        `<${element} identifier="${escapeXmlAttribute(identifier)}">\n` +
        `${indentXml(renderExpression(rule.expression), 2)}\n` +
        `</${element}>`
      );
    }
  }
}

/**
 * Emit one `qti-template-processing` block.
 *
 * 🔴 Authoring note that belongs next to the emitter rather than in a wiki: a
 * `qti-template-constraint` that few grid points satisfy does NOT fail loudly.
 * session.ts:474 restarts at most 100 times and then proceeds with the violating
 * draw. Check feasibility over `qti3RandomIntegerGrid` before publishing.
 */
export function buildQti3TemplateProcessing(rules: readonly Qti3TemplateRule[]): string {
  if (rules.length === 0)
    throw new Error(
      "qti-template-processing with no rules declares variants and produces none; omit the element.",
    );
  const inner = rules.map((rule) => indentXml(renderRule(rule), 2)).join("\n");
  return `<qti-template-processing>\n${inner}\n</qti-template-processing>`;
}
