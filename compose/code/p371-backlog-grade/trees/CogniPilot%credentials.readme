# CogniPilot Credentials

OpenBadges 3.0 digital credentials for the CogniPilot community.

## Issuing a Credential

### Via GitHub Issue (Recommended)

1. [Create a new badge request issue](../../issues/new?template=badge-request.yml)
2. Fill out the form with recipient details and badge type
3. A member of the [@CogniPilot/credentials](https://github.com/orgs/CogniPilot/teams/credentials) team adds the `issue-badge` label
4. The workflow automatically:
   - Creates the signed credential
   - Generates baked SVG and PNG badges
   - Creates the credential page
   - Comments on the issue with links
   - Closes the issue

### Manual Method

1. Create a request file in `requests/`:

```json
{
  "recipient_name": "Jane Doe",
  "recipient_email": "jane@example.com",
  "achievement": "tsc-member-2026",
  "valid_from": "2026-01-01T00:00:00Z",
  "status": "pending"
}
```

2. Run `python scripts/process_requests.py` or commit and push to trigger the GitHub Actions workflow

### Wallet Slug Options

By default, your wallet URL is derived from your name (e.g., `jane-doe`). You can customize this:

**Custom slug** - Specify your own URL-friendly identifier:
```json
{
  "recipient_name": "Jane Doe",
  "recipient_email": "jane@example.com",
  "achievement": "tsc-member-2026",
  "valid_from": "2026-01-01T00:00:00Z",
  "wallet_slug": "jdoe-credentials"
}
```

**Anonymous slug** - Generate a random alphanumeric identifier for privacy:
```json
{
  "recipient_name": "Jane Doe",
  "recipient_email": "jane@example.com",
  "achievement": "tsc-member-2026",
  "valid_from": "2026-01-01T00:00:00Z",
  "anonymize_slug": true
}
```

This creates a wallet URL like `profile/a7b2c9d4e1f8/wallet` instead of `profile/jane-doe/wallet`.

**Note:** Wallet slug options only apply when creating a new wallet. If your email already has an associated wallet, new credentials are added to that existing wallet. To change an existing wallet's slug, see [Renaming Wallet Slug](#renaming-wallet-slug).

Generated files are saved to `docs/profile/<wallet-slug>/<achievement-id>/`:
- `credential.json` - Signed verifiable credential
- `badge.svg` - Baked SVG badge with earner name and embedded credential
- `badge.png` - PNG badge with embedded credential metadata
- `index.html` - Credential page for sharing

## Updating Credentials

### Via GitHub Issue (Recommended)

1. [Create an update request issue](../../issues/new?template=update-credential.yml)
2. Fill out the form with your current email and requested changes
3. A maintainer will review and process your request

**Note:** If you have credentials in multiple wallets (e.g., from using different email addresses), updating to an email that already has a wallet will consolidate/merge your credentials into that existing wallet.

### Manual Method

Create an update request file in `requests/`:

```json
{
  "request_type": "update",
  "old_email": "old-email@example.com",
  "recipient_name": "Jane Doe",
  "recipient_email": "new-email@example.com",
  "achievement": "achievement-id",
  "valid_from": "2026-01-01T00:00:00Z",
  "valid_until": "2026-12-31T23:59:59Z"
}
```

## Renaming Wallet Slug

To change your profile URL slug, create a rename request:

```json
{
  "request_type": "rename_wallet",
  "recipient_email": "email@example.com",
  "recipient_name": "Display Name",
  "new_wallet_slug": "new-slug-name"
}
```

To convert an existing wallet to an anonymous slug:

```json
{
  "request_type": "rename_wallet",
  "recipient_email": "email@example.com",
  "anonymize_slug": true
}
```

## Removing Credentials

### Via GitHub Issue (Recommended)

1. [Create a removal request issue](../../issues/new?template=remove-credential.yml)
2. Choose whether to remove specific credentials or your entire profile
3. Confirm the removal is intentional
4. A maintainer will review and process your request

### Manual Method

Create a removal request file in `requests/`:

```json
{
  "request_type": "remove",
  "recipient_email": "email@example.com",
  "remove_profile": false,
  "achievements": ["achievement-id-1", "achievement-id-2"]
}
```

Set `remove_profile` to `true` to remove your entire wallet and all credentials. Otherwise, list specific achievement IDs to remove.

## Revoking Credentials

Revocation marks a credential as invalid without deleting it. Revoked credentials will fail verification even if the recipient has already downloaded a copy. This is useful when:
- A credential was issued in error
- The recipient's status has changed
- The credential was compromised

### Via GitHub Issue (Recommended)

1. [Create a revocation request issue](../../issues/new?template=revoke-credential.yml)
2. Provide the credential holder's email and achievement ID
3. Explain the reason for revocation
4. A maintainer adds the `approve-revocation` label to process

### Manual Method

```bash
cd scripts
python revoke_credential.py --email user@example.com --achievement achievement-id
```

Or using the credential ID directly:

```bash
python revoke_credential.py --credential wallet-slug/achievement-id
```

To list all credentials and their revocation status:

```bash
python revoke_credential.py --list
```

### Reinstating Revoked Credentials

Revoked credentials can be reinstated if the revocation was done in error or the situation has changed.

**Via GitHub Issue:**

1. [Create a reinstatement request issue](../../issues/new?template=unrevoke-credential.yml)
2. Provide the credential holder's email and achievement ID
3. Explain the reason for reinstatement
4. A maintainer adds the `approve-unrevocation` label to process

**Manual Method:**

```bash
cd scripts
python revoke_credential.py --email user@example.com --achievement achievement-id --unrevoke
```

### How Revocation Works

Credentials include a `credentialStatus` field pointing to a [Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/). When a credential is revoked:

1. The credential's bit is set in the status list
2. The status list credential is regenerated and signed
3. Verifiers check the status list during validation
4. The credential fails verification with "Credential has been revoked"

When a credential is reinstated, the bit is cleared and the credential passes verification again.

The status list is hosted at: `https://credentials.cognipilot.org/status/revocation-list`

## Verification

Verify credentials at: https://credentials.cognipilot.org/verify

The verifier supports:
- **JSON credentials** - Upload or paste a `credential.json` file
- **SVG badges** - Upload an SVG badge with embedded credential
- **PNG badges** - Upload a PNG badge with embedded credential metadata

### Example Credentials

An [example wallet](https://credentials.cognipilot.org/profile/examples/wallet) is available to demonstrate credential states:

- **Expired** - [Rumoca Maintainer](https://credentials.cognipilot.org/profile/examples/maintainer-rumoca) (expired 2024-12-31)
- **Expiring Soon** - [CogniPilot Collaborator](https://credentials.cognipilot.org/profile/examples/collaborator-cognipilot) (expires within 30 days)
- **Valid** - [CogniPilot Contributor](https://credentials.cognipilot.org/profile/examples/contributor-cognipilot) (no expiration)
- **Revoked** - [CogniPilot Maintainer](https://credentials.cognipilot.org/profile/examples/maintainer-cognipilot) (revoked credential)

Use these to test verification behavior for different credential states.
