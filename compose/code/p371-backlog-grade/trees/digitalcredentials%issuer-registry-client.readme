# Known Issuer Registry Client _(@digitalcredentials/issuer-registry-client)_

[![Build status](https://img.shields.io/github/actions/workflow/status/digitalcredentials/issuer-registry-client/main.yml?branch=main)](https://github.com/digitalcredentials/issuer-registry-client/actions?query=workflow%3A%22Node.js+CI%22)
[![NPM Version](https://img.shields.io/npm/v/@digitalcredentials/issuer-registry-client.svg)](https://npm.im/@digitalcredentials/issuer-registry-client)

> Isomorphic client for looking up DIDs in Known Issuer/Known Verifier
> registries. For Node, browser and React Native.

## Table of Contents

- [Description](#description)
- [Install](#install)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Description

This is a client library that looks up DIDs in either:

- an OIDF registry using the /fetch?sub= oidf endpoint to lookup the did,
  passing it as the value of the 'sub' paramter
- a static list of DIDs encoded in a format previously used by the DCC for it's
  member and community registries, and served publicly, like this one:
  https://github.com/digitalcredentials/dcc-community-registry/registry.json

Note that an individual DID can appear in multiple registries. Because of that,
the _order_ of registries loaded matters. For example, given a registry list:

```js
const knownRegistries = [
  {
    type: 'oidf',
    fetchEndpoint: 'https://registry.dcconsortium.org/fetch?sub=',
    name: 'DCC Member Registry'
  },
  {
    name: 'DCC Sandbox Registry',
    url: 'https://digitalcredentials.github.io/sandbox-registry/registry.json',
    type: 'dcc-legacy'
  }
]
```

If an issuer DID is contained in both of those registries, the issuer entry
(that contains the issuer name and URL) will come from the _first_ registry,
"DCC Member Registry".

In other words, verifiers and other implementers must order the registries _in
order of most authoritative to least_.

## Install

- Node.js 24+ is recommended.

### NPM

To install via NPM:

```
npm install @digitalcredentials/issuer-registry-client
```

### Development

This project uses [pnpm](https://pnpm.io/). To install locally (for
development):

```
git clone https://github.com/digitalcredentials/issuer-registry-client.git
cd issuer-registry-client
pnpm install
```

Build, lint, and test:

```
pnpm run build         # compile to dist/ via tsc
pnpm run lint          # eslint
pnpm run test-node     # vitest (Node)
pnpm run test-browser  # playwright (browser); run `pnpm exec playwright install chromium` first
pnpm test              # fix + lint + node + browser
```

## Usage

You'll need an array of known issuer and verifier registries you would like to
check against, like this publicly available copy of the DCC known registries:

https://digitalcredentials.github.io/dcc-known-registries/known-did-registries.json

which as of apr 22 2025 looked like so (reproduced here for convenience):

```json
[
  {
    "type": "oidf",
    "fetchEndpoint": "https://registry.dcconsortium.org/fetch?sub=",
    "name": "DCC Member Registry"
  },
  {
    "type": "dcc-legacy",
    "name": "DCC Sandbox Registry",
    "url": "https://digitalcredentials.github.io/sandbox-registry/registry.json"
  },
  {
    "type": "dcc-legacy",
    "name": "DCC Community Registry",
    "url": "https://digitalcredentials.github.io/community-registry/registry.json"
  },
  {
    "type": "dcc-legacy",
    "name": "MSP Registry",
    "url": "https://sandbox-issuer.myskillspocket.com/registry.json"
  }
]
```

You would use that list thusly:

```js
import { RegistryClient } from '@digitalcredentials/issuer-registry-client'

const registryClient = new RegistryClient()

// get the list of known issuers from wherever you store it, which could just be in a variable,
// but here we show how to fetch the DCC's list from it's github repository:
const response = await fetch("https://digitalcredentials.github.io/dcc-known-registries/known-did-registries.json");
const knownRegistries = await response.json();

// set the registry client to use that list
await registryClient.use({ registries: knownRegistries })

// You can now query to see if a DID is known in any registry
const results = registryClient.lookupIssuersFor('did:key:z6MkpLDL3RoAoMRTwTgo3rs39ZwssfaPKtGdZw7AGRN7CK4W'))
```

The lookup returns:

- a list of issuers in which the provided DID is registered
- a list of any registries (from the provided known issuers list) that couldn't
  be checked

Each returned issuer includes metadata for the issuer and metadata for the
registry in which the issuer was registered.

### Supplying your own `fetch`

Every registry request goes through `globalThis.fetch` by default. Pass a
`fetch` of your own to take that over -- to apply a timeout, add headers, serve
from a cache, or reach a registry the runtime cannot request directly (in a
browser, one that sends no CORS headers), which would otherwise come back in
`uncheckedRegistries`:

```js
const registryClient = new RegistryClient({
  fetch: async url =>
    await fetch(`https://gateway.example/fetch?url=${encodeURIComponent(url)}`)
})
```

It is called with a URL and returns a `Response`, exactly like `fetch`.

Note that it is called as a method of the client, so a bare global reference --
`{ fetch }` or `{ fetch: globalThis.fetch }` -- is a detached call. In a browser
that throws `TypeError: Illegal invocation`, and every registry comes back in
`uncheckedRegistries`. Wrap it, as in the example above, or bind it:

```js
const registryClient = new RegistryClient({
  fetch: globalThis.fetch.bind(globalThis)
})
```

Here is an example lookup response for a DID that is registered in one legacy
registry, one OIDF regsitry, and also lists one registry that couldn't checked
for some reason (e.g., the server was down):

```json
{
  "matchingIssuers": [
    {
      "issuer": {
        "federation_entity": {
          "organization_name": "OneUni University",
          "homepage_uri": "https://oneuni.edu",
          "logo_uri": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAB4SURBVEhLY1Da6ENTNGoBQTRqAUE0Yixwkq3X5tNgAANBkRlosvgQERbM0OaAmAwFNLFAkMNdW2KGkwjIE1S3AIFGLSCIRi0giEYtwIHq5Tk0BCEIaDwIwLh89RiKMRBRFkDNxQBUsoAyNGoBQTRqAUE01C3Y6AMAsDxJowXOs6oAAAAASUVORK5CYII="
        },
        "institution_additional_information": {
          "legal_name": "Board and Trustees of OneUni University"
        },
        "credential_registry_entity": {
          "ctid": "ce-e8a41a52-6ff6-48f0-9872-889c87b093b7",
          "ce_url": "https://credentialengineregistry.org/resources/ce-e8a41a52-6ff6-48f0-9872-889c87b093b7"
        },
        "ror_entity": {
          "rorid": "042nb2s44",
          "ror_url": "https://ror.org/042nb2s44"
        }
      },
      "registry": {
        "type": "oidf",
        "fetchEndpoint": "https://test.registry.dcconsortium.org/fetch?sub=",
        "name": "DCC Member Registry"
      }
    },
    {
      "issuer": {
        "federation_entity": {
          "organization_name": "Issuer Registry Client test",
          "homepage_uri": "https://dcconsortium.org/",
          "location": "here"
        }
      },
      "registry": {
        "type": "dcc-legacy",
        "name": "DCC Community Registry",
        "url": "https://digitalcredentials.github.io/community-registry/registry.json"
      }
    }
  ],
  "uncheckedRegistries": [
    {
      "type": "oidf",
      "fetchEndpoint": "https://registryyyyy.dcconsortium.org/fetch?sub=",
      "name": "DCC Member Registry Not Real"
    }
  ]
}
```

## Contribute

PRs accepted.

If editing the Readme, please conform to the
[standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[MIT License](LICENSE.md) © 2025 Digital Credentials Consortium.
