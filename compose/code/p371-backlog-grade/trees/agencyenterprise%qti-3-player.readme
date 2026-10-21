# QTI 3.x Renderer

[**Live Sandbox Demo**](https://agencyenterprise.github.io/qti-3-player/)

A framework-agnostic QTI 3.x renderer with support for multiple frontend frameworks.

## Structure

```
qti-3-player/
├── packages/
│   ├── qti-renderer/     # Core renderer library (TypeScript, framework-agnostic)
│   ├── qti-react/        # React wrapper component
│   ├── qti-vue/          # Vue wrapper component
│   └── qti-vanilla/      # Vanilla JS wrapper
├── sandbox/              # Standalone demo application
└── stories/              # Storybook examples and stories
```

## Packages

### Core Library (`packages/qti-renderer`)

Framework-agnostic npm package that renders QTI 3.x assessment items to HTML with full response processing support.

**API:**

```typescript
import { QtiRenderer } from '@ae-studio/qti-renderer';

const renderer = new QtiRenderer(qtiXmlString);
renderer.render(containerElement);
```

**Features:**

- XML validation against QTI 3.0 schema
- Response processing with conditional logic
- Outcome variable management (RESPONSE)
- Feedback display (inline and modal)
- Response state management

## Supported QTI Elements

See [QTI Support Documentation](docs/qti_support/README.md) for a complete checklist of supported elements and attributes.

## Design Decisions

- Uses `DOMParser` for XML parsing (no external dependencies)
- Renders to vanilla DOM elements (framework-agnostic)
- Maintains response state internally
- Uses semantic HTML (`fieldset`, `legend`, `label`) for accessibility
- Registry pattern for extensible element rendering
- Event-driven response processing

## Development

### Running Storybook

```bash
npm install
npm run dev
```

This will start Storybook on `http://localhost:6006` with examples for React, Vue, and Vanilla JS.

### Building

```bash
npm run build
```

Builds all packages in the monorepo.

### Sandbox

The sandbox provides a standalone demo application:

```bash
cd sandbox
npm install
npm run dev
```

## Current Limitations

- **No scoring** - No calculation or evaluation of responses
- **No test structure** - Only single assessment items, no tests/sections
- **Limited interaction types** - Currently supports `choice-interaction` (single and multiple choice)
- **Partial expression support** - Basic expressions like `match` and `correct` are supported, but not all QTI expressions
- **No adaptive behavior** - Static rendering only, no adaptive item selection

## MathML Support

This renderer supports MathML rendering via MathJax. We do not bundle MathJax with the library to keep it lightweight and flexible. You must include MathJax in your application, and the `MathJax` object must be defined on the `window` object.

We support MathJax versions 2, 3, and 4. Here are examples of how to include them in your HTML:

### MathJax 2

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

### MathJax 3

```html
<script>
  MathJax = {
    loader: { load: ['[mml]/mml3'] },
  };
</script>
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.0.0/es5/tex-mml-chtml.min.js"
  integrity="sha512-yxTB34XQUKlyuz73upeDrZ91/tbZW/YAURVWL3s+09bEWdmORQzUZwSKyBIRxSeHuSwh1aOKEffn2/D65kwyYg=="
  crossorigin="anonymous"
  referrerpolicy="no-referrer"
></script>
```

### MathJax 4

```html
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/4.0.0/tex-mml-chtml.min.js"
  integrity="sha512-yxTB34XQUKlyuz73upeDrZ91/tbZW/YAURVWL3s+09bEWdmORQzUZwSKyBIRxSeHuSwh1aOKEffn2/D65kwyYg=="
  crossorigin="anonymous"
  referrerpolicy="no-referrer"
></script>
```
