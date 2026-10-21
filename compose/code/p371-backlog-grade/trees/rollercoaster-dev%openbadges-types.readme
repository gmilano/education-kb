# Open Badges Types

A comprehensive TypeScript types package for Open Badges 2.0 and 3.0 specifications.

[![npm version](https://img.shields.io/npm/v/openbadges-types.svg)](https://www.npmjs.com/package/openbadges-types)
[![license](https://img.shields.io/npm/l/openbadges-types.svg)](https://github.com/rollercoaster-dev/openbadges-types/blob/main/LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-4.7+-blue)](https://www.typescriptlang.org/)
[![CI Status](https://img.shields.io/github/actions/workflow/status/rollercoaster-dev/openbadges-types/test.yml?branch=main&label=ci)](https://github.com/rollercoaster-dev/openbadges-types/actions)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Open Badges 2.0](#open-badges-20)
  - [Open Badges 3.0](#open-badges-30)
  - [Using Shared Types](#using-shared-types)
  - [Version-Specific Operations](#version-specific-operations)
  - [Open Badges JSON-LD Context Schemas](#open-badges-json-ld-context-schemas)
- [API Documentation](#api-documentation)
  - [Open Badges 2.0 Types](#open-badges-20-types)
  - [Open Badges 3.0 Types](#open-badges-30-types)
  - [Shared Types](#shared-types)
- [Type Guards and Validation](#type-guards-and-validation)
  - [Basic Type Guards](#basic-type-guards)
  - [Composite Type Guards](#composite-type-guards)
  - [Badge Normalization](#badge-normalization)
  - [OB3 Validation Limitations](#ob3-validation-limitations)
- [Development](#development)
  - [Testing](#testing)
  - [Building](#building)
  - [Linting and Formatting](#linting-and-formatting)
  - [Validation](#validation)
- [Version Compatibility](#version-compatibility)
- [Migration Guide](#migration-guide)
- [Consuming Applications](#consuming-applications)
- [License](#license)

## Overview

This package provides TypeScript type definitions for both Open Badges 2.0 and Open Badges 3.0 specifications. It can be used in badge servers, component libraries, and applications that work with Open Badges.

### What are Open Badges?

Open Badges are digital credentials that represent achievements, skills, or competencies. They are designed to be verifiable, portable, and stackable, allowing individuals to showcase their accomplishments across different platforms and contexts.

### Open Badges Versions

**Open Badges 2.0** is the established standard developed by the IMS Global Learning Consortium. It defines a structured format for digital badges, including information about the issuer, recipient, criteria, and evidence.

**Open Badges 3.0** represents a significant evolution, adopting the W3C Verifiable Credentials Data Model. This alignment with broader digital credential standards enhances interoperability and security while maintaining the core concepts of Open Badges.

This package supports both versions to ensure backward compatibility while enabling adoption of the newer standard. It provides type-safe interfaces for working with badges in either format, as well as utilities for converting between versions.

## Installation

```bash
npm install openbadges-types
```

or

```bash
yarn add openbadges-types
```

## Usage

### Open Badges 2.0

```typescript
import { OB2 } from 'openbadges-types';

// Create a BadgeClass
const badgeClass: OB2.BadgeClass = {
  '@context': 'https://w3id.org/openbadges/v2',
  id: 'https://example.org/badges/5',
  type: 'BadgeClass',
  name: '3-D Printmaster',
  description: 'This badge is awarded for passing the 3-D printing knowledge and safety test.',
  image: 'https://example.org/badges/5/image',
  criteria: {
    narrative:
      'Students are tested on knowledge and safety, both through a paper test and a supervised performance evaluation on key skills.',
  },
  issuer: {
    id: 'https://example.org/issuer',
    type: 'Profile',
    name: 'Example Maker Society',
    url: 'https://example.org',
    email: 'contact@example.org',
    verification: {
      type: 'hosted',
      allowedOrigins: 'example.org',
    },
  },
};

// Create an Assertion
const assertion: OB2.Assertion = {
  '@context': 'https://w3id.org/openbadges/v2',
  id: 'https://example.org/assertions/123',
  type: 'Assertion',
  recipient: {
    type: 'email',
    identity: 'alice@example.org',
  },
  issuedOn: '2016-12-31T23:59:59+00:00',
  verification: {
    type: 'hosted',
  },
  badge: badgeClass,
};
```

### Open Badges 3.0

```typescript
import { OB3 } from 'openbadges-types';

// Create an Achievement
const achievement: OB3.Achievement = {
  type: ['Achievement'],
  name: '3-D Printmaster',
  description: 'This badge is awarded for passing the 3-D printing knowledge and safety test.',
  criteria: {
    narrative:
      'Students are tested on knowledge and safety, both through a paper test and a supervised performance evaluation on key skills.',
  },
  alignments: [
    {
      targetName: 'ISTE Standard 3',
      targetUrl: 'https://example.org/standards/iste3',
    },
  ],
};

// Create a Verifiable Credential
const credential: OB3.VerifiableCredential = {
  '@context': [
    'https://www.w3.org/2018/credentials/v1',
    'https://purl.imsglobal.org/spec/ob/v3p0/context.json',
  ],
  id: 'https://example.org/credentials/3732',
  type: ['VerifiableCredential'],
  issuer: {
    id: 'https://example.org/issuers/123',
    type: ['Profile'],
    name: 'Example Maker Society',
    url: 'https://example.org',
    email: 'contact@example.org',
  },
  issuanceDate: '2023-06-15T12:00:00Z',
  credentialSubject: {
    id: 'did:example:ebfeb1f712ebc6f1c276e12ec21',
    achievement: achievement,
  },
  proof: {
    type: 'Ed25519Signature2020',
    created: '2023-06-15T12:05:00Z',
    verificationMethod: 'https://example.org/issuers/123#keys-1',
    proofPurpose: 'assertionMethod',
    proofValue: 'z58DAdFfa9SkqZMVPxAQpic6FPCsJWa6SpsfDqwmUbHEVnWxeh',
  },
};
```

### Using Shared Types

```typescript
import { Shared } from 'openbadges-types';

// Use shared types
const dateTime: Shared.DateTime = '2023-06-15T12:00:00Z';
const iri: Shared.IRI = 'https://example.org/badges/5';
```

### Version-Specific Operations

```typescript
import { OpenBadgesVersion, VersionedBadge } from 'openbadges-types';

// Function that works with either version
function processBadge<T extends OpenBadgesVersion>(badge: VersionedBadge<T>, version: T): string {
  if (version === OpenBadgesVersion.V2) {
    // badge is typed as OB2.Assertion
    return (badge as OB2.Assertion).badge.name;
  } else {
    // badge is typed as OB3.VerifiableCredential
    const vc = badge as OB3.VerifiableCredential;
    const achievement = vc.credentialSubject.achievement;
    return Array.isArray(achievement)
      ? achievement[0].name.toString()
      : achievement.name.toString();
  }
}
```

### Open Badges JSON-LD Context Schemas

You can import the official JSON-LD context objects for Open Badges 2.0 and 3.0 for use in validation or tooling:

```typescript
import { OB2_CONTEXT, OB3_CONTEXT } from 'openbadges-types';

// OB2_CONTEXT and OB3_CONTEXT are the official JSON-LD context objects
console.log(OB2_CONTEXT['@context']);
console.log(OB3_CONTEXT['@context']);
```

## API Documentation

### Open Badges 2.0 Types

#### Core Types

- `Assertion`: Represents an awarded badge to a specific recipient

  ```typescript
  interface Assertion extends JsonLdObject {
    '@context': string | string[] | Record<string, any>;
    id: IRI;
    type: 'Assertion' | string;
    recipient: IdentityObject;
    badge: BadgeClass | IRI;
    issuedOn: DateTime;
    expires?: DateTime;
    image?: string | ImageObject;
    evidence?: Evidence | Evidence[];
    narrative?: MarkdownText;
    verification: VerificationObject;
    [key: string]: any;
  }
  ```

- `BadgeClass`: Represents the type of achievement being awarded

  ```typescript
  interface BadgeClass extends JsonLdObject {
    '@context': string | string[] | Record<string, any>;
    id: IRI;
    type: 'BadgeClass' | string;
    name: string;
    description: string;
    image: string | ImageObject;
    criteria: string | Criteria;
    issuer: Profile | IRI;
    alignment?: AlignmentObject[];
    tags?: string[];
    [key: string]: any;
  }
  ```

- `Profile`: Represents an issuer of badges
  ```typescript
  interface Profile extends JsonLdObject {
    '@context': string | string[] | Record<string, any>;
    id: IRI;
    type: 'Profile' | 'Issuer' | string;
    name: string;
    url?: string;
    email?: string;
    description?: string;
    image?: string | ImageObject;
    verification?: VerificationObject;
    [key: string]: any;
  }
  ```

#### Supporting Types

- `IdentityObject`: Represents the identity of a badge recipient
- `VerificationObject`: Contains instructions for third parties to verify an assertion
- `Evidence`: Describes the work that the recipient did to earn the achievement
- `AlignmentObject`: Describes an alignment to an educational standard
- `Image`: Represents an image associated with a badge
- `Criteria`: Describes the criteria for earning the badge
- `RevocationList`: Contains a list of revoked assertions
- `CryptographicKey`: Represents a cryptographic key used for verification
- `Extension`: Represents an extension to the Open Badges specification

### Open Badges 3.0 Types

#### Core Types

- `VerifiableCredential`: Based on the W3C Verifiable Credentials Data Model

  ```typescript
  interface VerifiableCredential extends JsonLdObject {
    '@context': string | string[] | Record<string, any>;
    id: IRI;
    type: 'VerifiableCredential' | string | string[];
    issuer: IRI | Issuer;
    issuanceDate: DateTime;
    expirationDate?: DateTime;
    credentialSubject: CredentialSubject;
    proof?: Proof;
    credentialStatus?: CredentialStatus;
    refreshService?: RefreshService;
    termsOfUse?: TermsOfUse | TermsOfUse[];
    evidence?: Evidence | Evidence[];
    [key: string]: any;
  }
  ```

- `Achievement`: Represents the achievement being recognized

  ```typescript
  interface Achievement extends JsonLdObject {
    type: 'Achievement' | string | string[];
    id?: IRI;
    name: string | MultiLanguageString;
    description?: string | MultiLanguageString;
    criteria?: Criteria;
    image?: string | ImageObject;
    creator?: IRI | Issuer;
    alignments?: Alignment[];
    resultDescriptions?: ResultDescription[];
    [key: string]: any;
  }
  ```

- `CredentialSubject`: Represents the entity receiving the credential
  ```typescript
  interface CredentialSubject extends JsonLdObject {
    id?: IRI;
    achievement: Achievement | Achievement[];
    results?: Results;
    [key: string]: any;
  }
  ```

#### Supporting Types

- `Issuer`: Represents the entity issuing the credential
- `Proof`: Contains cryptographic proof information
- `Evidence`: Describes the evidence for the achievement
- `Criteria`: Describes the criteria for earning the achievement
- `Alignment`: Describes an alignment to an educational standard
- `ResultDescription`: Describes possible results for an achievement
- `Results`: Represents the results achieved by the recipient
- `CredentialStatus`: Represents the status of a credential
- `RefreshService`: Provides a way to refresh the credential
- `TermsOfUse`: Describes the terms of use for the credential

### Shared Types

- `IRI`: URI/URL type (branded string type for type safety)

  ```typescript
  type IRI = string & { readonly __brand: unique symbol };
  ```

- `DateTime`: ISO 8601 date format (branded string type for type safety)

  ```typescript
  type DateTime = string & { readonly __brand: unique symbol };
  ```

- `JsonLdContext`: JSON-LD context type

  ```typescript
  type JsonLdContext = string | string[] | Record<string, any>;
  ```

- `MultiLanguageString`: Internationalization support

  ```typescript
  interface MultiLanguageString {
    [language: string]: string;
  }
  ```

- `LanguageMap`: Record mapping language codes to strings

  ```typescript
  type LanguageMap = Record<string, string>;
  ```

- `MarkdownText`: String that may contain Markdown

  ```typescript
  type MarkdownText = string;
  ```

- `ImageObject`: Common image properties

  ```typescript
  interface ImageObject {
    id?: IRI;
    type?: string;
    caption?: string | MultiLanguageString;
    author?: string;
  }
  ```

- `JsonLdObject`: Base interface for JSON-LD objects

  ```typescript
  interface JsonLdObject {
    '@context'?: string | string[] | Record<string, any>;
    type?: string | string[];
    id?: string;
    [key: string]: any;
  }
  ```

- `JsonLdArray`: Helper type for JSON-LD arrays
  ```typescript
  type JsonLdArray<T> = T | T[];
  ```

## Development

For detailed development instructions, see [DEVELOPMENT.md](DEVELOPMENT.md).

### Package Structure

This package is built to support both CommonJS and ESM environments, with proper TypeScript type definitions for each format:

```json
{
  "exports": {
    ".": {
      "require": {
        "types": "./dist/index.d.cts",
        "default": "./dist/index.cjs"
      },
      "import": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      },
      "default": "./dist/index.js"
    }
  }
}
```

This structure ensures:

- CommonJS consumers get the correct `.cjs` file with `.d.cts` type definitions
- ESM consumers get the correct `.js` file with `.d.ts` type definitions
- TypeScript can properly resolve types in both module formats

The package is validated using:

- `publint` - Validates package.json exports and entry points
- `@arethetypeswrong/cli` - Checks for TypeScript type resolution issues

### Testing

This package uses Jest for testing. The tests verify that the type definitions correctly match the OpenBadges 2.0 and 3.0 specifications.

To run the tests:

```bash
npm test
```

To run the tests with coverage:

```bash
npm run test:coverage
```

### Building

To build the package:

```bash
npm run build
```

### Linting and Formatting

This package uses ESLint for linting and Prettier for code formatting.

To lint the code:

```bash
npm run lint
```

To format the code:

```bash
npm run format
```

### Validation

To validate the codebase (lint, format check, and test):

```bash
npm run validate
```

## Type Guards and Validation

This package includes type guards and runtime validation for both Open Badges 2.0 and 3.0 objects:

### Basic Type Guards

- **OB2 (Open Badges 2.0):**
  - Uses custom, spec-aligned validation logic (see `src/validation.ts`).
  - Covers all required fields, types, and edge cases for Assertion, BadgeClass, Profile, and supporting types.
  - Comprehensive positive and negative test cases in `test/validation.test.ts` and `test/ob2-guards.test.ts`.
- **OB3 (Open Badges 3.0):**
  - Uses AJV for JSON Schema-based validation (see `src/validateWithSchema.ts`).
  - Validates VerifiableCredential and all nested types against the official OB3 JSON-LD context.
  - Comprehensive positive and negative test cases in `test/ob3-schema-validation.test.ts` and `test/ob3-guards.test.ts`.

**Example:**

```typescript
import { validateBadge } from 'openbadges-types';

const result = validateBadge(badgeObject);
if (result.isValid) {
  // Badge is valid OB2 or OB3
  console.log('Version:', result.version);
} else {
  console.error('Validation errors:', result.errors);
}
```

### Composite Type Guards

The package provides composite type guards that work with both OB2 and OB3 badges:

```typescript
import { CompositeGuards } from 'openbadges-types';

// Check if an object is a valid badge (either OB2 or OB3)
if (CompositeGuards.isBadge(badge)) {
  // Get badge properties regardless of version
  const name = CompositeGuards.getBadgeName(badge);
  const description = CompositeGuards.getBadgeDescription(badge);
  const issuerName = CompositeGuards.getBadgeIssuerName(badge);
  const issuanceDate = CompositeGuards.getBadgeIssuanceDate(badge);

  console.log(`Badge: ${name} issued by ${issuerName} on ${issuanceDate}`);
  console.log(`Description: ${description}`);
}
```

### Badge Normalization

For applications that need to work with both OB2 and OB3 badges, the package provides utilities to normalize badges to a common format:

```typescript
import { BadgeNormalizer } from 'openbadges-types';

// Normalize a badge to a common format
const normalizedBadge = BadgeNormalizer.normalizeBadge(badgeObject);

// Now you can access common properties regardless of badge version
console.log(`Badge: ${normalizedBadge.name}`);
console.log(`Issued by: ${normalizedBadge.issuerName}`);
console.log(`Issued on: ${normalizedBadge.issuanceDate}`);

// You can also filter, sort, and group badges
const badges = BadgeNormalizer.normalizeBadges(badgeArray);
const filteredBadges = BadgeNormalizer.filterBadgesBySearchTerm(badges, 'search term');
const sortedBadges = BadgeNormalizer.sortBadges(badges, 'name', 'asc');
const groupedBadges = BadgeNormalizer.groupBadges(badges, 'issuerName');
```

See the test files and [Consuming Applications](#consuming-applications) documentation for more usage examples and edge case coverage.

### OB3 Validation Limitations

> **Note:** OB3 validation currently uses the official JSON-LD context (not a strict JSON Schema) and a combination of AJV and manual checks. This means:
>
> - Some edge cases or nuanced spec requirements may not be fully enforced.
> - The validation logic is as strict as possible given the available context, but is not a full substitute for a formal JSON Schema.
> - If/when an official OB3 JSON Schema is published, it is recommended to update the validation logic to use it for maximum conformance.

## Version Compatibility

This package supports:

- **Open Badges 2.0**: The IMS Global Final Release specification
- **Open Badges 3.0**: Based on the W3C Verifiable Credentials Data Model

## Migration Guide

For detailed information about migrating from Open Badges 2.0 to 3.0, see our [Migration Guide](MIGRATION.md).

## Consuming Applications

For detailed examples of how to use this package in your applications, see our [Consuming Applications Guide](docs/consuming-applications.md). This guide includes:

- Examples for using type guards in Vue components
- Examples for using badge normalization in services
- Patterns for filtering, sorting, and grouping badges
- Best practices for working with both OB2 and OB3 badges

## License

MIT
