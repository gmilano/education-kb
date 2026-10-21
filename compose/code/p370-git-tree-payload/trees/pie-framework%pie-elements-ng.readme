# PIE Elements NG

A modern, ESM-first implementation of the PIE (Platform Independent Elements) specification. This is a **new project** (not a refactor) that provides a clean foundation for future PIE development while maintaining backwards compatibility through the legacy pie-elements project.

**Current Status**: Early development (v0.1.0) - 27 React-based elements ported from the legacy `pie-elements`, core infrastructure in place.

## Why a New Project?

The PIE team's work on library modernization (React 18, MUI 7, Tiptap editor) now enables full ESM adoption and modern tooling. This new project takes advantage of those improvements while keeping the legacy pie-elements available for existing consumers.

## Key Improvements Over Legacy pie-elements

1. **Framework-agnostic architecture** - Architecture designed to support multiple frameworks (React, Svelte, future Vue/Angular) via web components. Currently: React implementations ported from the legacy `pie-elements`.
2. **ESM-first build system** - Static browser ESM entries for players, standard ESM exports for tooling, and legacy IIFE compatibility where needed
3. **Unified player approach** - Element-level players for development (interactive + print), item-level players in pie-players for production
4. **Symmetric package organization** - Peer folders (delivery/author/controller/print) vs asymmetric legacy structure
5. **Modern standard tooling** - Vite + Bun + Turbo vs bespoke pie-cli + pie-shared-lib-builder
6. **Consolidated demo system** - Single unified SvelteKit app for all elements vs per-element tool-generated demos
7. **Integrated monorepo** - @pie-lib pulled in vs separate repository
8. **Independent package versioning** - Each package versions on its own through Changesets, with release labels when several ship together
9. **GitHub Actions CI/CD** - Modern GitHub-native workflows vs CircleCI

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for detailed explanations of each difference.

## Getting started

### Prerequisites

- Bun >= 1.3.11
- Node.js >= 20.0.0

### Initial Setup (First Time)

**Note:** `pie-elements` and `pie-lib` are legacy. `packages/elements-react` and `packages/lib-react` live in this repository; you don't need the legacy repositories checked out.

```bash
# 1. Clone the repository
git clone <repo-url>
cd pie-elements-ng

# 2. Install dependencies
bun install

# Hooks are installed automatically via postinstall.
# If needed, you can reinstall them manually:
bun run hooks:install

# 3. Build all packages
bun run build
```

That's it! All packages are in the repository, so you can get started immediately.

### Development Commands

`bun run build` - Build all packages in the monorepo; each package's build type-checks it with `tsc`

`bun run dev:element-demo` - Start the demo application in development mode

`bun run dev` - Watch mode for all packages (does not start the demo application)

`bun run test` - Run all tests

### Controller And Configure Shim Compatibility

Some external PIE builders (including `pie-api-aws`) resolve `@pie-element/<name>/controller` and `@pie-element/<name>/configure` through filesystem aliases instead of package subpath exports. For packages that declare:

- `package.json` `pie.controller`: `@pie-element/<name>/controller`
- `package.json` `pie.configure`: `@pie-element/<name>/configure`

also expose the controller/configure entries through ESM subpaths, ship root shims, and publish them via `files`:

- `exports["./controller"]`: `./dist/controller/index.js`
- `exports["./controller.js"]`: `./dist/controller/index.js`
- `exports["./configure"]`: usually `./dist/author/index.js`
- `files`: includes `controller.js` and `configure.js`

```js
export * from './dist/controller/index.js';
```

```js
export { default } from './dist/author/index.js';
export * from './dist/author/index.js';
```

This keeps compatibility with alias-based resolvers while preserving standard ESM `exports["./controller"]` and `exports["./author"]` for normal consumers.

Packages that export `./author` or `./print` also ship root `author.js` and `print.js` shims for the same resolvers. [Controller And Configure Packaging](docs/PIE_ELEMENT_CONTRACT.md#controller-and-configure-packaging) lists every shim, and `bun run check:publish-surface` enforces them.

### Browser ESM Package Contract

The canonical JavaScript and npm packaging contract is
[`docs/PIE_ELEMENT_CONTRACT.md`](docs/PIE_ELEMENT_CONTRACT.md). The summary below
calls out the browser ESM package surface.

Player-facing ESM does not use CDN package transforms for element packages such as jsDelivr `+esm`. React packages that support browser ESM publish static files under:

- `dist/browser/delivery/index.js`
- `dist/browser/author/index.js`
- `dist/browser/print/index.js`
- `dist/browser/controller/index.js`

Their package exports expose those files as `./browser/delivery`, `./browser/author`, `./browser/print`, and `./browser/controller`. These entries use a hybrid policy defined in `tools/vite/browser-esm-policy.json`: React and React DOM remain shared bare imports that `pie-players` pins through an import map, while MUI, Emotion, workspace helpers, and smaller leaf dependencies stay bundled for reliability. Browser-ESM packages must declare the exact shared runtime contract in `pie.browserSharedDependencies`; dependency or peer-dependency ranges are not a substitute for this field.

Browser ESM builds use the shared `tools/vite/element-browser.config.ts` config. Element package scripts pass that config to Vite from the package directory, so the config can discover the package's delivery/author/print/controller entries without generating a duplicate `vite.config.browser.ts` in every element package.

If a future dependency should become shared instead of bundled, add it to `tools/vite/browser-esm-policy.json` and update `pie-players` import-map generation in the same change. `check:publish-surface` enforces the allowed bare imports, exact `pie.browserSharedDependencies`, and the browser JS size budget so dependency updates cannot silently drift back toward IIFE-sized bundles.

### Release Labels

Use release labels to tag a coordinated release wave across packages while keeping package versions independent.

`bun run release:label` - Create an annotated tag (default: `pie-elements-ng-YYYY.MM.DD`)

`bun run release:label -- --label elements-ng-2026.02` - Create a custom release tag name

`bun run release:label:push` - Create and push the release tag to origin

### Manual Publish Recovery (GitHub Actions)

`@pie-element/*` and `@pie-lib/*` packages are configured as publishable and are released through this workflow.

If a publish fails after the version PR was already merged, rerun the Release workflow manually:

1. Actions → **Release** → **Run workflow**
2. Branch: `master` for stable (`latest`) or `develop` for prerelease (`next`)
3. `release_intent`: `publish`
4. `release_channel`: `stable` on `master`, `next` on `develop`
5. `force_publish`: `true`

This is intended for recovery/rerun scenarios only.

Release and dist-tag policy details are documented in [docs/PUBLISHING.md](docs/PUBLISHING.md).

### Targeted Package Release (Changesets)

To release one or more specific packages, create a changeset scoped to those packages:

```bash
bun run changeset:plan -- --packages @pie-element/mc-populated-blank --type patch --summary "Fix CQT parity for VIC/SEL VIC variants"
```

For multiple packages:

```bash
bun run changeset:plan -- --packages @pie-element/mc-populated-blank,@pie-element/simple-cloze --type minor --summary "Add Svelte release updates"
```

Then run the normal Changesets flow:

```bash
# 1) Commit and merge the PR with the generated .changeset file
# 2) On develop, the Release run publishes the changed packages as next snapshots
#    and commits nothing but the PR's changeset.
#    On master, CI raises a version PR, and merging it publishes latest.
# 3) CI publishes through the same contract checks as a manual publish:
bun run release:publish
```

See [Release Flow](docs/PUBLISHING.md#release-flow).

## Print Support

PIE elements include print views for generating paper-based assessments and answer keys. Two complementary players serve different use cases:

### Element-Level Print Player (This Project)

For development and testing of individual elements:

```html
<pie-element-player view="print" element-name="multiple-choice" role="student"></pie-element-player>
```

- **Package:** `@pie-element/element-player`
- **Use for:** Element development, testing, documentation, and optional composable embedding
- **Location:** `packages/element-player/src/players/PieElementPlayer.svelte`

For most production app flows, prefer the standard player stacks from the `pie-elements` and `pie-players` projects.

### Item-Level Print Player (pie-players)

For production rendering of complete assessment items:

```html
<pie-print config={{ item: {...}, options: { role: 'student' } }}></pie-print>
```

- **Package:** `@pie-players/pie-print-player` (in pie-players repository)
- **Use for:** Production apps, multi-element items, markup-driven rendering
- **Location:** `../pie-players/packages/print-player`

See [docs/PRINT_SUPPORT.md](docs/PRINT_SUPPORT.md) for complete documentation.

## Documentation

- [Architecture](docs/ARCHITECTURE.md) - Detailed architecture and design decisions
- [Print Support](docs/PRINT_SUPPORT.md) - Print architecture and usage
- [Element Interfaces and JSON Schemas](docs/ELEMENT_SCHEMAS.md) - Declaring an element's model, configuration and session, and using the published schemas
