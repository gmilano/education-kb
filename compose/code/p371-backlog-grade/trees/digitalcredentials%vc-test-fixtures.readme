# vc-test-fixtures

A set of test VCs, status lists, and DIDs for testing.

>[!TIP]
>You might want to jump straight to the [list of the verifiable credentials](./listOfTestVCs.md), which includes a QR code, copy/pastable JSON, link to raw JSON, and a VerifierPlus link for each credential.

The structure of this repository is mostly self-explanatory. There are three main directories, one each for:

- verifiable credentials
- DIDs
- static bitstring status lists

The verifiable credentials directory is further split into subdirectories with one each for versions 1 and 2 of the verifiable credentials specification, each of which in turn have three subdirectories: one each for the two signature types ed25519-signature-2020 and data-integrity/eddsa-rdfc-2022-cryptosuite and one for vcs with both signatures. Within those directories the VCs themselves are named with following pattern:

[registryType]-[status]-[expiry].json

so like this example:

legacy-noStatus-noExpiry.json 

which means the VC was signed with a DID that is registered in one of our legacy regsitries, most likely the sandbox registry, and has neither a status nor an expiration property.

## DIDs

### did:web in legacy sandbox registry

- seed: z1AcqywgC3eXpYgiiKELLZ18uMvNPHHUGSZPYYkiCs7KX6T
- did: did:web:digitalcredentials.github.io:vc-test-fixtures:dids:legacy

registered in:

- [DCC Sandbox Registry](https://digitalcredentials.github.io/sandbox-registry/registry.json)

### did:web in oidf test registry

- seed: z1AcqywgC3eXpYgiiKELLZ18uMvNPHHUGSZPYYkiCs7KX6T
- did: did:web:digitalcredentials.github.io:vc-test-fixtures:dids:oidf

registered in:

- [DCC OIDF Test Registry](https://test.registry.dcconsortium.org/.well-known/openid-federation)

### did:key in oidf test registry and legacy sandbox registry

- seed:  z1Ad8J9rdHCQMyfPJcoiyuVcKunAneJ49pX18ay5Apv7MUg
- did: did:key:z6Mki7DqKQswPsjqMVhP4W3n2ABFb5wBegZC5erEVg5qcgEw

registered in:

- [DCC OIDF Test Registry](https://test.registry.dcconsortium.org/.well-known/openid-federation)
- [DCC Sandbox Registry](https://digitalcredentials.github.io/sandbox-registry/registry.json)

Used to sign test VCs whose file names start with 'mixedRegistry'

### did:key in oidf test registry

- seed: z1AfeAsXeuZsPj9ftDo8UweMYYWmWdrdqud2o14n5QxtiiS
- did: did:key:z6MkjoriXdbyWD25YXTed114F8hdJrLXQ567xxPHAUKxpKkS

registered in:

- [DCC OIDF Test Registry](https://test.registry.dcconsortium.org/.well-known/openid-federation)

### did:key in legacy sandbox registry

- seed: z1AeiPT496wWmo9BG2QYXeTusgFSZPNG3T9wNeTtjrQ3rCB
- did: did:key:z6MknNQD1WHLGGraFi6zcbGevuAgkVfdyCdtZnQTGWVVvR5Q

registered in:

- [DCC Sandbox Registry](https://digitalcredentials.github.io/sandbox-registry/registry.json)

### did:key in four registries

- seed:  not posting here because the key is used to sign VCs in trusted registries
- did: did:key:z6MkuL7x2mTEoBmUuuaQ2hvEUd2YsEtmsHeX9JzqJZ8VYaVH

registered in:

- [DCC OIDF Test Registry](https://test.registry.dcconsortium.org/.well-known/openid-federation)
- [DCC Sandbox Registry](https://digitalcredentials.github.io/sandbox-registry/registry.json)
- [DCC Community Registry](https://github.com/digitalcredentials/community-registry/blob/main/registry.json)
- [DCC Member Registry](https://github.com/digitalcredentials/dcc-registry/blob/main/registry.json)

