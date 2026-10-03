"""Login envelope sealing for the Heidy API.

The backend never accepts a plaintext password: clients fetch the current
login public key (`GET /auth/login-key`) and seal the Senha Única into an
HPKE-Base(X25519, HKDF-SHA256, AES-256-GCM) envelope. Only the backend's
in-memory decapsulation key can open it.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import os
from datetime import datetime, timezone

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey,
    X25519PublicKey,
)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

HKDF_INFO = b"heidy-login-v1"


def _hkdf_sha256(ikm: bytes, info: bytes) -> bytes:
    # Single-block extract-and-expand with a zero salt, matching the
    # backend's vault (HeidyApi.Credentials.Vault.Local.hkdf/2).
    prk = hmac.new(b"\x00" * 32, ikm, hashlib.sha256).digest()
    return hmac.new(prk, info + b"\x01", hashlib.sha256).digest()


def seal_envelope(public_key_b64: str, key_id: str, secret: str) -> dict[str, str]:
    """Seal `secret` to the backend's login key, returning the login envelope.

    The returned dict is the `envelope` object `POST /auth/login` expects:
    `key_id`, `enc` (ephemeral X25519 public key), `ciphertext`
    (nonce || AES-GCM ciphertext || tag) and `encrypted_at`.
    """
    server_public = X25519PublicKey.from_public_bytes(base64.b64decode(public_key_b64))
    ephemeral = X25519PrivateKey.generate()
    shared = ephemeral.exchange(server_public)
    key = _hkdf_sha256(shared, HKDF_INFO)

    nonce = os.urandom(12)
    sealed = AESGCM(key).encrypt(nonce, secret.encode(), HKDF_INFO)
    ephemeral_public = ephemeral.public_key().public_bytes(
        serialization.Encoding.Raw, serialization.PublicFormat.Raw
    )

    return {
        "key_id": key_id,
        "enc": base64.b64encode(ephemeral_public).decode(),
        "ciphertext": base64.b64encode(nonce + sealed).decode(),
        "encrypted_at": datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z"),
    }
