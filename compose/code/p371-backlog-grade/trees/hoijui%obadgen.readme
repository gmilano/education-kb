<!--
SPDX-FileCopyrightText: 2021 - 2023 Robin Vobruba <hoijui.quaero@gmail.com>

SPDX-License-Identifier: CC0-1.0
-->

# _O_pen-_Bad_ges _Gen_erator (`obadgen`)

[![License: AGPL-3.0-or-later](
    https://img.shields.io/badge/License-AGPL%203.0+-blue.svg)](
    LICENSE.txt)
[![REUSE status](
    https://api.reuse.software/badge/github.com/hoijui/obadgen)](
    https://api.reuse.software/info/github.com/hoijui/obadgen)
[![Repo](
    https://img.shields.io/badge/Repo-GitHub-555555&logo=github.svg)](
    https://github.com/hoijui/obadgen)
[![Package Releases](
    https://img.shields.io/crates/v/obadgen.svg)](
    https://crates.io/crates/obadgen)
[![Documentation Releases](
    https://docs.rs/obadgen/badge.svg)](
    https://docs.rs/obadgen)
[![Dependency Status](
    https://deps.rs/repo/github/hoijui/obadgen/status.svg)](
    https://deps.rs/repo/github/hoijui/obadgen)
[![Build Status](
    https://github.com/hoijui/obadgen/workflows/build/badge.svg)](
    https://github.com/hoijui/obadgen/actions)

[![In cooperation with Open Source Ecology Germany](
    https://raw.githubusercontent.com/osegermany/tiny-files/master/res/media/img/badge-oseg.svg)](
    https://opensourceecology.de)

`obadgen` is a CLI ([Command-line Interface](
https://en.wikipedia.org/wiki/Command-line_interface)) tool,
which helps in generating ["baking"](
https://github.com/mozilla/openbadges-backpack/wiki/Badge-Baking)
[Open Badge](https://openbadges.org/) 2.0 (latest release as of Nov. 2023)
annotated images.

## Usage

To use this tool, you need some prerequisites:

- This tool itsself
- an **input badge image** in SVG or PNG format
  ("unbaked"/without Open Badge meta-data)
- an Open Badge **Assertion file** in JSON-LD format;
  see [Assertion Content](#assertion-content)
- (optional) if a [signed](
  https://github.com/mozilla/openbadges-specification/blob/master/Assertion/latest.md#signed)
  instead of a [hosted](https://github.com/mozilla/openbadges-specification/blob/master/Assertion/latest.md#hosted)
  asssertion is supplied,
  you need to supply a **DER encoded private key**,
  prefferably from an x.509 certificate.
  See [Certificate or Key-Pair](#certificate-or-key-pair)
- (optional) [OpenSSL](https://www.openssl.org/)'s CLI tool `openssl`,
  which allows you to [generate](#generate) and [convert](#convert)
  cryptographic certificates and keys.

## Assertion Content

In Open Badg 2.0,
the assertion JSON-LD content can either be:

- _hosted_, which means it has to be hosted under the URL under its ID,
  which should be a location under the control of the issuing party
- _signed_, which means it has to be cryptographically signed with a key
  (prefferably from an x.509 certificate)
  under the control of the issuing party,
  but it may be hosted/stored anywhere after that

Also see [Full Example](#full-example) further down.

### Assertion Examples

#### Hosted

[res/ob-ents/badge-assertion-simple.json](
res/ob-ents/badge-assertion-simple.json):

```json
{
  "@context": "https://w3id.org/openbadges/v2",
  "type": "Assertion",
  "id": "https://raw.githubusercontent.com/hoijui/obadgen/master/res/ob-ents/badge-assertion-simple.json",
  "badge": "https://raw.githubusercontent.com/hoijui/obadgen/master/res/ob-ents/badge-definition-simple.json",
  "recipient": {
    "type": "email",
    "identity": "sha256$488842626ec74a0468d90ea17dc4e11c2d0e8e54e45c5075fbd1d2e767f44249",
    "hashed": true
  },
  "verification": {
    "type": "HostedBadge"
  },
  "issuedOn": "2022-06-17T23:59:59Z",
  "expires": "2099-06-30T23:59:59Z"
}
```

#### Signed

[res/ob-ents/badge-assertion-with-key.json](
res/ob-ents/badge-assertion-with-key.json):

```json
{
  "@context": "https://w3id.org/openbadges/v2",
  "type": "Assertion",
  "id": "https://raw.githubusercontent.com/hoijui/obadgen/master/res/ob-ents/badge-assertion-with-key.json",
  "badge": "https://raw.githubusercontent.com/hoijui/obadgen/master/res/ob-ents/badge-definition-with-key.json",
  "recipient": {
    "type": "email",
    "identity": "sha256$a596420c9e6e6d4a7a552b2073a3b6c28807d808b37c97454ab4e419c9e5e4ad",
    "hashed": true,
    "salt": "dfvnk0923#%^&87t6iubasr"
  },
  "verification": {
    "type": "SignedBadge",
    "creator": "https://raw.githubusercontent.com/hoijui/obadgen/master/res/ob-ents/issuer-with-key.json"
  },
  "issuedOn": "2022-06-17T23:59:59Z",
  "expires": "2099-06-30T23:59:59Z"
}
```

### Bakeing

Both the examples below create the file _baked-badge.svg_.

Example for a _hosted_ badge:

```shell
obadgen \
    --assertion assertion.json \
    --source-image raw-badge.svg \
    --baked baked-badge.svg
```

Example for a _signed_ badge:

```shell
obadgen \
    --assertion assertion.json \
    --signing-algorithm es256 \
    --key my_organization.x509_cert.priv_key.der \
    --source-image raw-badge.svg \
    --baked baked-badge.svg
```

### Full Example

Here we create a badge assertion,
which we then sign and bake into an SVG.
This SVG can thereafter be stored and verified anywhere.

```shell
PRIV_KEY="res/ob-ents/issuer-key.priv.der"
ALG="es256"
ISSUER_ID="https://raw.githubusercontent.com/hoijui/obadgen/master/res/ob-ents/issuer-with-key.json"
BADGE_CLASS_ID="https://raw.githubusercontent.com/hoijui/obadgen/master/res/ob-ents/badge-definition-with-key.json"
ASSERTION_ID="https://some-domain.com/anywhere/does-not-even-have-to-exist/because-signed/badge-assertion-with-key.json"
EMAIL="recipient@email.com"
RECIPIENT_SALT="dfvnk097t6iubasr"
IDENTITY_HASH="sha256\$$(printf '%s%s' "$EMAIL" "$RECIPIENT_SALT" | sha256sum - | sed -e 's/ .*//')"
DATE_NOW="$(date --iso-8601=seconds)"
DATE_FUTURE="$(date --iso-8601=seconds --date="2099-12-30")"
ASSERTION_FILE_PATH="assertion.json"
IMG_EXT="svg"
#IMG_EXT="png"
SOURCE_IMAGE_BASE="res/media/img/test"

# Writing the badge asserion JSON-LD file
cat > "$ASSERTION_FILE_PATH" << EOF
{
  "@context": "https://w3id.org/openbadges/v2",
  "type": "Assertion",
  "id": "$ASSERTION_ID",
  "badge": "$BADGE_CLASS_ID",
  "recipient": {
    "type": "email",
    "identity": "$IDENTITY_HASH",
    "hashed": true,
    "salt": "$RECIPIENT_SALT"
  },
  "verification": {
    "type": "SignedBadge",
    "creator": "$ISSUER_ID"
  },
  "issuedOn": "$DATE_NOW",
  "expires": "$DATE_FUTURE"
}
EOF

# Signs and bakes the assertion to baked-badge.svg
obadgen \
    --assertion "$ASSERTION_FILE_PATH" \
    --signing-algorithm "$ALG" \
    --key "$PRIV_KEY" \
    --source-image "$SOURCE_IMAGE_BASE.$IMG_EXT" \
    --baked "baked-badge.$IMG_EXT"
```

## Certificate or Key-Pair

If you desicde to sign your badge (vs simply hosting it)
as your verification method,
you will need a private-key.

It could come from a simple public-private key-pair,
or prefferably from an [x.509 certificate](
https://en.wikipedia.org/wiki/X.509),
both of which can be generated with OpenSSL (shown below),
if you do not yet have it.

The private-key you supply to this tool **must** be in [DER format](
https://wiki.openssl.org/index.php/DER).
If yours is in any other format (most likely [PEM](
https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail)),
you can convert it to DER suing OpenSSL (shown below).

Currently supported key-types are:

- RS256 - RSASSA-PKCS1-v1_5 using SHA-256
- RS384 - RSASSA-PKCS1-v1_5 using SHA-384
- RS512 - RSASSA-PKCS1-v1_5 using SHA-512
- ES256 - ECDSA using P-256 and SHA-256
- ES384 - ECDSA using P-384 and SHA-384

This list is what the library we use ([`biscuit`](
https://crates.io/crates/biscuit))
supports for [JSON Web Signature (JWS))](
http://self-issued.info/docs/draft-ietf-jose-json-web-signature.html),
which is what Open Badge signing requires.

In the following sub-sections,
you find how to [generate](#generate) and [convert](#convert)
certificates and keys.

For all these examples we use a common base (`FILE_BASE`)
for the certificates and keys file names,
extended with verbose suffixes.
We also provide the algorithm name (`ALG`)
as it has to be supplied to this tool later on. \
NOTE: In cryptographic practice,
each private-key file also contains its corresponding public-key. \

So in any case, you will either have:

- key-pair "package":
  - private file: contains the _private-_ and the _public-key_
  - public file: contains the _public-key_
- certificate "package":
  - private file: contains the _private-_ and the _public-key_
  - public file: contains the certificate with all its meta-data properties,
    one of which also is its _public-key_

### Generate

#### Certificate (preffered)

Both of the two exampels below,
create these two files:

- `my_organization.x509_cert.priv_key.der` (private file)
- `my_organization.x509_cert.cert.pem` (public file)

##### ECDSA Certificate

Create a self-signed x.509 certificate in PEM format
using `ES256` (ECDSA) key types,
with its private-key in DER format:

```shell
FILE_BASE="my_organization"
ALG="es256"
openssl req \
    -new \
    -x509 \
    -subj "/C=DE/ST=Berlin/L=Berlin/O=OSEG/OU=SW-Dev/CN=ose-germany.de/emailAddress=open-badges-123@ose-germany.de" \
    -sha256 \
    -nodes \
    -pkeyopt ec_paramgen_curve:prime256v1 \
    -newkey ec \
    -keyform DER \
    -keyout "$FILE_BASE.x509_cert.priv_key.der" \
    -days 730 \
    -outform PEM \
    -out "$FILE_BASE.x509_cert.cert.pem"
```

##### RSA Certificate

Create a self-signed x.509 certificate in PEM format
using `RS256` (RSA) key types,
with its private-key in DER format:

```shell
FILE_BASE="my_organization"
ALG="rs256"
openssl req \
    -new \
    -x509 \
    -subj "/C=DE/ST=Berlin/L=Berlin/O=OSEG/OU=SW-Dev/CN=ose-germany.de/emailAddress=open-badges-123@ose-germany.de" \
    -sha256 \
    -nodes \
    -newkey rsa:4096 \
    -keyform DER \
    -keyout "$FILE_BASE.x509_cert.priv_key.der" \
    -days 730 \
    -outform PEM \
    -out "$FILE_BASE.x509_cert.cert.pem"
```

#### Key-Pair

Both of the two exampels below,
create these two files:

- `my_organization.priv.der` (private file)
- `my_organization.pub.pem` (public file)

##### ECDSA Pair

Create an `ES256` (ECDSA) key pair,
with the private-key in DER format
and the public-key in PEM format:

```shell
FILE_BASE="my_organization"
ALG="es256"
openssl genpkey \
    -algorithm RSA \
    -pkeyopt rsa_keygen_bits:4096 \
    -outform der \
    -out "$FILE_BASE.priv.der"
```

##### RSA Pair

Create an `RS256` (RSA) key pair,
with the private-key in DER format
and the public-key in PEM format:

```shell
FILE_BASE="my_organization"
ALG="rs256"
# TODO FIXME This is still the certificate, not a key-pair only!
openssl req \
    -x509 \
    -sha256 \
    -nodes \
    -newkey rsa:4096 \
    -keyform DER \
    -keyout "$FILE_BASE.x509_cert.priv_key.der" \
    -days 730 \
    -outform PEM \
    -out "$FILE_BASE.x509_cert.cert.pem"
```

### Convert

#### RSA encoding

Converts an RSA _private_-key in PEM format
into the DER format:

```shell
FILE_BASE="my_organization"
openssl rsa \
    -inform PEM \
    -in "$FILE_BASE.pem" \
    -outform DER \
    -out "$FILE_BASE.der"
```

Converts an RSA _public_-key in DER format
into the PEM format:

```shell
FILE_BASE="my_organization"
openssl rsa \
    -RSAPublicKey_in \
    -inform PEM \
    -in "$FILE_BASE.pem" \
    -outform DER \
    -RSAPublicKey_out \
    -out "$FILE_BASE.der"
```

#### ECDSA encoding

Converts an ECDSA _private_-key in PEM format
into the DER format:

```shell
FILE_BASE="my_organization"
openssl ec \
    -inform PEM \
    -in "$FILE_BASE.pem" \
    -outform DER \
    -out "$FILE_BASE.der"
```

Converts an ECDSA _public_-key in DER format
into the PEM format:

```shell
FILE_BASE="my_organization"
openssl ec \
    -pubin \
    -inform PEM \
    -in "$FILE_BASE.pem" \
    -outform DER \
    -pubout \
    -out "$FILE_BASE.der"
```

#### Extract

Extracts the public key from an RSA private key-pair file
(here one from an x.509 certificate, but can be any other)
into a separate file,
and reformats that files content to be pasted directly
into an Open Badge 2.0 _assertion.json_ file:

```shell
FILE_BASE="my_organization"
openssl rsa \
    -in "$FILE_BASE.x509_cert.priv_key.der" \
    -inform DER \
    -RSAPublicKey_out \
    -outform PEM \
    -out "$FILE_BASE.x509_cert.pub_key.pem"
sed -e 's/\n/\\n/' "$FILE_BASE.x509_cert.pub_key.pem"
```

Visualizes certificate info for human eyes:

```shell
openssl x509 \
    -in "$FILE_BASE.x509_cert.cert.pem" \
    -inform PEM \
    -text
```
