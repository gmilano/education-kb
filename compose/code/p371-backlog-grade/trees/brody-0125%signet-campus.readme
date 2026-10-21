# Signet Campus

Signet Campus turns campus accessibility work into portable Open Badges credentials. Learners submit evidence, reviewers assess it against published criteria, and approved work earns a signed badge. Learning pathways group badges into a larger achievement.

The use case is inspired by [Bowdoin's digital badge pathways and personal-account guidance](https://bowdoin.teamdynamix.com/TDClient/1814/Portal/KB/Article/157578/Understand-the-Digital-Badge-Learning-Pathway-Subscription-Email). Campus defines its own assessment, prerequisite and completion policies; it is not a Bowdoin service. The included program starts with accessible documents and keyboard access.

## Run locally

Install Docker with Compose v2. The optional overlays require Compose 2.24.4 or newer. Network access is needed for container images, npm, Maven Central and JitPack. A host JDK is not required for Docker builds.

```sh
git clone https://github.com/brody-0125/signet-campus.git
cd signet-campus
docker compose up -d --build web
```

Allow the API and identity provider to finish starting, then open [Signet Campus](http://localhost:5173). The API is at port 8080, Keycloak at 8081 and the local email inbox at [Mailpit](http://localhost:8025). Published ports bind to loopback. Database, identity and signing keys persist in named volumes.

| Demo account | Password | Access |
|---|---|---|
| `learner` | `local-learner-only` | Submit evidence and receive badges |
| `reviewer` | `local-reviewer-only` | Manage achievements/pathways and review evidence |

These are synthetic local accounts. You can also select **Sign in → Register** and verify a synthetic address through Mailpit. Registration does not grant reviewer privileges. See [local configuration](docs/LOCAL_DEVELOPMENT.md) and [account access](docs/ACCOUNT.md) for existing realms and durable personal sign-in.

## Use the application

1. In **Explore**, inspect an achievement's criteria and submit evidence.
2. As a reviewer, open **Review queue** to approve the work or request changes. Learners can revise rejected evidence.
3. As the learner, open the approved submission and select **Issue badge**. Verify it and download JSON, PNG or SVG. Public sharing is optional and private by default.
4. In **Pathways**, inspect prerequisites, enroll and earn every required current badge. Eligible learners can issue a separate completion award.

| Capability | Details |
|---|---|
| Catalog lifecycle | [Draft, publish, archive, restore and next editions](docs/CATALOG.md); criteria freeze on first submission |
| Assessment | [Owner-only evidence, reviewer decisions, resubmission and optimistic concurrency](docs/EVIDENCE_REVIEW.md) |
| Credentials | [Ed25519 signing, registry verification, revocation and key rotation](docs/CREDENTIALS.md) |
| Portability | [Embedded PNG/SVG credentials](docs/PORTABLE_BADGES.md), [explicit public sharing](docs/SHARING.md) and independent verification |
| Learning pathways | [Prerequisites, enrollment, progress and completion awards](docs/PATHWAYS.md) |
| Notifications | [Transactional outbox, retries and local SMTP](docs/NOTIFICATIONS.md) |
| Personal access | [Registration, verified email, account settings and institutional unlinking](docs/ACCOUNT.md) |

## Technology and architecture

The web client uses React, Zustand, TanStack Query and Vite. The server uses Kotlin 2.2.21, Spring Boot 3.5.11, Gradle 8.14.3 and hexagonal boundaries checked by Konsist. Kotest and PostgreSQL integration tests cover domain and API behavior; Kover enforces a 90% line-coverage gate. Logging uses kotlin-logging with optional Micrometer/OpenTelemetry instrumentation.

The server consumes JitPack releases `com.github.brody-0125:signet-spring-boot-starter:v0.1.6` and its transitive Signet Core `v0.1.5`. Dependencies use semantic release tags. See [architecture](docs/ARCHITECTURE.md), [the resolved dependency inventory](docs/third-party/inventory.json) and [license declarations](docs/DEPENDENCY_LICENSES.md).

The [HTTPS overlay](docs/HTTPS.md) serves an isolated deployment at port 8443. [Replica tests](docs/REPLICAS.md) exercise two API processes and worker crash recovery. [Telemetry](docs/TELEMETRY.md), [application backup/restore](docs/RECOVERY.md) and [identity recovery](docs/IDENTITY_RECOVERY.md) document operational behavior. Local Compose uses development credentials and identity settings; the architecture guide describes the service deployment boundaries and required infrastructure.

## Verify

Run from the repository root. Node 24 and npm are needed for web and acceptance tools.

```sh
docker compose --profile test run --rm tests
npm ci --prefix web
npm test --prefix web
npm run build --prefix web
```

With the local application and identity provider running:

```sh
npm ci --prefix dev --ignore-scripts
node dev/prepare-verification-resources.mjs
node --test dev/independent-verification.test.mjs
```

The independent verifier checks actual issued badges and pathway awards with a separate JavaScript cryptographic implementation, including Unicode, tampering, images and revocation. Acceptance tests create synthetic records. See [testing](docs/TESTING.md) for all gates and fixture commands, and [interoperability](docs/INTEROPERABILITY.md) for exact coverage and compatibility.

## Standards and license

Campus implements credential features from [1EdTech Open Badges 3.0](https://www.imsglobal.org/spec/ob/v3p0) and [W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/). It is not certified by 1EdTech. [NOTICE](NOTICE) retains standards attribution.

Original code and documentation use the [MIT License](LICENSE). Dependencies, fonts, covered third-party source and preserved upstream notices retain their own terms. [Third-party notices](THIRD_PARTY_NOTICES.md), [distribution contents and source availability](docs/DISTRIBUTION.md), and [standards requirements](docs/COMPLIANCE.md) accompany the project.

See [the submission API](docs/API.md), [contributing](CONTRIBUTING.md), [security reporting](SECURITY.md) and [changelog](CHANGELOG.md).
