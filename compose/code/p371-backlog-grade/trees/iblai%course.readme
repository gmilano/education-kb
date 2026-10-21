<div align="center">

<a href="https://ibl.ai"><img src="https://ibl.ai/images/iblai-logo.png" alt="ibl.ai" width="300"></a>

# Course

AI-assisted course authoring and delivery — design programs, browse the catalog, and chat with course agents on the ibl.ai platform.

The video demo is available [here](https://drive.google.com/file/d/1IcfMBCSjZ5jqnCj_hQr6l1bxGjXY_xi9/view?usp=sharing).

[![Next.js](https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![Claude Code](https://img.shields.io/badge/Claude_Code-CC785C?logoColor=white)](https://claude.ai)
[![Desktop & Mobile](https://img.shields.io/badge/Desktop_%26_Mobile-supported-blue)](https://github.com/iblai/vibe/blob/main/skills/iblai-ops-build/SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#license)

</div>

---

## What is Course
Course is deployed at [course.ibl.ai](https://course.ibl.ai).

Course is an end-to-end course-authoring workspace on the [ibl.ai](https://ibl.ai) platform. Plan a project, attach mentors, browse or create courses, and chat with an agent that helps draft outlines and unit content — all from one shell powered by the [@iblai/iblai-js](https://www.npmjs.com/package/@iblai/iblai-js) SDK and connected to [iblai.app](https://iblai.app).

## Screenshots

| Home | My Courses |
|------|------------|
| ![Course home](docs/screenshots/homepage.png) | ![My Courses](docs/screenshots/my_courses.png) |

| Feature | Description |
|---------|-------------|
| **Chat** | Agent chat at `/platform/{tenant}/{mentor}` via the SDK chat surface — streaming, sessions, files, voice |
| **Explore Agents** | Browse agents through the SDK `<AgentSearch>` component at `/agents` |
| **My Courses** | Per-tenant course list fetched from the course-creation API (`/api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/`) with About / Schedule / Edit / Preview / Delete actions and the "View Creation Prompt" dialog |
| **Course Catalog** | Cross-tenant public marketplace via the SDK `useDiscover({ tenantOverride: "main" })` hook |
| **Course Content** | edX learner UI at `/course-content/[id]/{course,dates,progress,discussion,bookmarks}` |
| **Projects** | Create + manage projects in the sidebar, attach mentors per project |
| **Customize** | Tenant-wide configuration surface at `/customize` |
| **Users** | User directory + role management |
| **Account** | Profile, social, security, and admin tabs in the SDK account dialog |
| **SSO Authentication** | Login via iblai.app — no tokens to manage |
| **Tenant Switching** | Switch organizations from the avatar dropdown |

## AGENTS.md / CLAUDE.md

Refer to `CLAUDE.md` (when present) at the repository root for component priorities, SDK import conventions, and the env-setup flow Claude Code should follow when running the app for the first time.

## Quick Start

### Prerequisites

- Node.js 18+
- pnpm (fall back to npm only if unavailable)
- An ibl.ai platform login (or a tenant you can SSO into via [iblai.app](https://iblai.app))
- The `iblai` CLI — install from source (see below)

### Install the `iblai` CLI

The CLI is installed from source via `make`. `clone + make install` is the supported install path — the version you run tracks the templates the team is editing.

**macOS / Linux** (Python 3.11+, pip, git, make):

```bash
git clone https://github.com/iblai/iblai-app-cli.git
cd iblai-app-cli
make -C .iblai install
cd -   # back to your project
```

If `iblai` isn't found afterwards, add `~/.local/bin` to your `PATH`:

```bash
export PATH="$HOME/.local/bin:$PATH"   # add to ~/.bashrc or ~/.zshrc to persist
```

**Windows** (Python 3.11+, pip, git):

```powershell
git clone https://github.com/iblai/iblai-app-cli.git
cd iblai-app-cli
pip install -e .iblai/
cd -
```

If `iblai` isn't found, ensure Python Scripts is on `PATH` (typically `%APPDATA%\Python\Python311\Scripts\`).

Verify the install:

```bash
iblai --version
```

### Install & Run

```bash
pnpm install
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000). You'll be redirected to `https://login.iblai.app` for SSO; on return, the home page resolves your active tenant and lands you on the workspace home.

`.env.local` is already populated with the iblai.app endpoints — no manual platform credentials are needed up front. Tenant + username are resolved at runtime from the SDK after SSO completes.

### Build

```bash
pnpm build
pnpm start
```

### Tests

Vitest covers the libraries, hooks, providers, components, and modals:

```bash
pnpm test                # one-shot
pnpm test:watch          # rerun on file changes
pnpm test:coverage       # html + console v8 report under coverage/
```

Playwright covers user journeys via real SSO:

```bash
pnpm test:e2e            # spins up `next dev`, runs auth.setup.ts once, then the journeys
pnpm test:e2e:ui         # Playwright UI mode
pnpm test:e2e:headed     # headed browser
```

### Deploy to Vercel

```bash
iblai deploy vercel
```

The CLI auto-detects the deploy mode from `next.config.mjs`. Course is a server-rendered Next.js app, so the CLI will:

- deploy the repo root to Vercel for a remote build,
- disable Vercel authentication / password protection,
- upload env vars from `.env.local` to production + preview (`NEXT_PUBLIC_*` as `plain`, the rest as `encrypted`; reserved keys and `your-…` placeholders are skipped),
- rerun the deploy with `--force` + `VERCEL_FORCE_NO_BUILD_CACHE=1` whenever env vars changed so the new `NEXT_PUBLIC_*` values are re-inlined into the client bundle.

Override detection with `--mode static` or `--mode server` when needed. Full guide: [`/iblai-ops-deploy`](https://github.com/iblai/vibe/blob/main/skills/iblai-ops-deploy/SKILL.md).

**Setup:** generate a Vercel token at [https://vercel.com/account/tokens](https://vercel.com/account/tokens) and add it to `iblai.env`:

```bash
echo 'VERCEL_TOKEN=<token>' >> iblai.env
```

> **Tip:** You can change the Vercel domain name by clicking on the three-dot button on your Vercel project on [`vercel.com`](https://vercel.com) and selecting "Manage Domains".

### Native builds (iOS, Android, macOS, Linux, Surface)

Wrap Course in a native shell with [Tauri v2](https://tauri.app) using the `iblai builds` family of commands (full guide: [`/iblai-ops-build`](https://github.com/iblai/vibe/blob/main/skills/iblai-ops-build/SKILL.md)). All platforms share a single static `next build` export — the CLI runs the frontend build automatically before starting the Tauri dev server, and the WebView loads the same `out/` bundle. **Stop `pnpm dev` (and any other process on port 3000) before running a dev build.**

#### One-time setup

```bash
iblai add builds                    # Add Tauri support to the project
pnpm install
iblai builds iconography logo.png   # Generate per-platform app icons
```

You'll also need [Rust via rustup](https://rustup.rs).

For mobile SSO, set `TAURI_CUSTOM_SCHEME=courseai` in `iblai.env` so the auth SPA redirects via a custom URI scheme (mobile WebViews can't return from an `https://` redirect to a native app).

#### iOS

Requires macOS + Xcode + Xcode Command Line Tools.

```bash
rustup target add aarch64-apple-ios aarch64-apple-ios-sim
iblai builds ios init                          # one-time
iblai builds device                            # list simulators
iblai builds ios dev "iPhone 16 Pro Max"       # run on simulator
iblai builds ios dev --device                  # run on a connected iPhone
iblai builds ios build                         # produce .ipa
iblai builds ci-workflow --ios                 # generate App Store CI
```

#### Android

Requires Android Studio with the Android SDK + NDK installed.

```bash
rustup target add aarch64-linux-android armv7-linux-androideabi i686-linux-android x86_64-linux-android
iblai builds android init                      # one-time
iblai builds device                            # list emulators
iblai builds android dev "Pixel_9"             # run on emulator
iblai builds android dev --device              # run on a connected device
iblai builds android build                     # produce APK
iblai builds ci-workflow --android             # generate Play Store CI
```

#### macOS desktop

Requires `xcode-select --install`.

```bash
iblai builds dev                               # run as a desktop app
iblai builds build                             # produce .dmg / .app
iblai builds ci-workflow --mac                 # generate macOS CI
```

#### Linux desktop

System deps (Debian/Ubuntu):

```bash
sudo apt install libwebkit2gtk-4.1-dev build-essential libssl-dev \
  libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev
```

```bash
iblai builds dev                               # dev shell
iblai builds build                             # produce .deb / .AppImage
iblai builds ci-workflow --linux               # generate Linux CI
```

#### Surface (Windows tablet / desktop)

Requires Visual Studio Build Tools (C++ workload) and WebView2 (bundled with Windows 11).

```bash
iblai builds dev                               # dev shell
iblai builds build                             # produce .msi / .exe
iblai builds ci-workflow --windows             # generate Windows CI
```

#### Generate every CI workflow at once

```bash
iblai builds ci-workflow --all
```

## Project Structure

```
app/
├── layout.tsx                          # Root layout — wraps with providers
├── page.tsx                            # Home redirect (auth check → workspace)
├── login/                              # SSO entry
├── sso-login-complete/                 # SSO callback (SDK <SsoLogin>)
├── home/                               # Authed home / dashboard
├── agents/                             # <AgentSearch> grid
├── platform/[tenantId]/[mentorId]/     # Mentor chat
├── chat/                               # Standalone chat surface
├── course/                             # Per-course landing
├── course-catalog/                     # Cross-tenant public catalog (useDiscover tenantOverride:"main")
├── course-content/[id]/                # edX learner UI (course / dates / progress / discussion / bookmarks)
├── courses/                            # My Courses — course-creation list view
├── customize/                          # Tenant customization
├── project/                            # Project workspaces
└── users/                              # User directory + roles
components/
├── account-dialog.tsx                  # Profile / social / security / admin tabs in a modal
├── analytics-navigation.tsx            # Analytics surface (when enabled)
├── chat-input/                         # Custom chat input form
├── chat-tabs/                          # Chat tab strip
├── course-creation-academy-block.tsx   # AI-assisted course-creation entry point
├── create-academy-dialog.tsx           # School / academy creation flow
├── credential-detail-modal.tsx         # Integration credential viewer
└── modals/                             # Shared dialogs (invite, rename, delete, create project, ...)
lib/iblai/
├── config.ts                           # NEXT_PUBLIC_* env reader
├── tenant.ts                           # Tenant resolution
├── course-actions.ts                   # Course-creation REST helpers (list, delete, brief lookup)
├── auth-utils.ts                       # redirectToAuthSpa, logout, handleTenantSwitch
└── use-url-context.ts                  # tenantKey + mentorId + username from URL params
providers/
└── iblai-providers.tsx                 # Redux + AuthProvider + TenantProvider
```

## Built With

- [Next.js](https://nextjs.org) — App Router
- [@iblai/iblai-js](https://www.npmjs.com/package/@iblai/iblai-js) — SDK for auth, UI components, and data
- [@iblai/data-layer](https://www.npmjs.com/package/@iblai/data-layer) — RTK Query data layer
- [@iblai/web-containers](https://www.npmjs.com/package/@iblai/web-containers) — framework-agnostic SDK components
- [LiveKit](https://livekit.io) — WebRTC transport for real-time avatar / voice sessions
- [Tailwind CSS](https://tailwindcss.com) — utility-first styling with ibl.ai design tokens
- [shadcn/ui](https://ui.shadcn.com) — accessible UI primitives
- [iblai.app](https://iblai.app) — production backend for auth, AI agents, billing, and analytics

## Contributing

### Setup

1. Fork the repo and clone it
2. Install dependencies: `pnpm install`
3. Start the dev server: `pnpm dev`

### Development Workflow

1. Create a branch from `main`: `git checkout -b feat/my-feature`
2. Make your changes
3. Run `pnpm build` and `pnpm test` to verify
4. Commit and push your branch
5. Open a pull request against `main`

### Guidelines

- **Use ibl.ai SDK components first** — do not build custom components when an SDK equivalent exists
- **Use shadcn/ui for custom UI** — install via `npx shadcn@latest add <component>`, not raw HTML or third-party libraries
- **Do not override SDK styles** — SDK components ship with their own styling
- **Use SDK design tokens** — reference CSS variables like `var(--primary-color)`, `var(--border-color)`, `var(--text-secondary)` instead of hardcoded colors
- **Course-creation API**: paths like `/api/ai-mentor/orgs/{org}/users/{user_id}/course-creation/course/{id}/` take the **integer `EdxCourse.id`**, not the edX locator. See `lib/iblai/course-actions.ts`.
- **Use `pnpm`** as the package manager

### Adding Features

Use the iblai CLI and Claude Code skills to add new features:

```bash
iblai add auth           # SSO authentication
iblai add profile        # User profile
iblai add account        # Account/org settings
iblai add analytics      # Analytics dashboard
iblai add notification   # Notification bell
iblai add invite         # Invite dialogs
iblai add builds         # Tauri v2 desktop/mobile shell
```

See `CLAUDE.md` for the full list of skills and component priority rules.

## Resources

- [ibl.ai Documentation](https://docs.ibl.ai)
- [iblai-app-cli](https://github.com/iblai/iblai-app-cli) — CLI for scaffolding ibl.ai apps
- [@iblai/mcp](https://www.npmjs.com/package/@iblai/mcp) — MCP server for AI-assisted development
- [Vibe](https://github.com/iblai/vibe) — developer toolkit for building with ibl.ai
- [Vibe Starter](https://github.com/iblai/vibe-starter) — pre-wired Next.js + ibl.ai SSO template

## License

Released under the [MIT License](LICENSE).

---

<sub>Built with <a href="https://github.com/iblai/vibe">ibl.ai Vibe</a></sub>
