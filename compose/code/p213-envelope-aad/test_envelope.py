"""P213 -- what the usp-mcp login envelope actually authenticates.

`iDavi/usp-mcp` (GPL-3.0, Brazil -- the first LATAM piece of code this base has
measured since pass 68) is the only piece in the KB that refuses to send an
institutional password in the clear: it seals the USP Senha Unica to the
backend's published login key before `POST /auth/login`.

That is a real, and so far unique, architectural answer to the credential
problem this base has been measuring since pass 53.  This test does NOT dispute
it.  It measures the two things the README's one-line claim --
"HPKE-Base(X25519, HKDF-SHA256, AES-256-GCM)" -- is stronger than the code:

  D1  The envelope's own metadata is NOT authenticated.  The AEAD's additional
      data is the constant `HKDF_INFO`, so `key_id` and `encrypted_at` travel
      beside the ciphertext with nothing binding them to it.  A relay can
      rewrite either field and the backend's AES-GCM tag still verifies.

  D2  The key schedule is HPKE-SHAPED, not RFC 9180.  `_hkdf_sha256` is a
      single-block extract-and-expand with a ZERO salt and one constant
      `info`; RFC 9180 derives through a suite-bound schedule
      (`suite_id`, "HPKE-v1" labels, `psk_id_hash`, `info_hash`).  The
      docstring says so itself -- "matching the backend's vault" -- so the
      envelope interoperates with ONE backend, not with HPKE libraries.

Neither finding is a vulnerability claim.  D1 is a property to know before a
deployment puts a relay in that path; D2 is a portability fact: a client that
cannot reach `heidy-backend.fly.dev` cannot be rebuilt from an off-the-shelf
HPKE implementation.

`vendored_crypto.py` is `src/usp_mcp/crypto.py` fetched verbatim from HEAD on
2026-10-03, sha256:bfe4ecaf4e48fd1c97028f7403f3bbaf985609e314d2927f34588a49bc680149
(2.136 B).  Vendored so the measurement stays reproducible if upstream moves.

Run:  python3 test_envelope.py
"""

import base64
import hashlib
import hmac
import inspect
import sys

from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

import vendored_crypto as vc

FAILURES = []


def check(name, cond, detail=""):
    print(("  PASS  " if cond else "  FAIL  ") + name + (" -- " + detail if detail else ""))
    if not cond:
        FAILURES.append(name)


def backend_side(envelope, server_private):
    """What the backend must do to open the envelope, derived from the client."""
    enc = base64.b64decode(envelope["enc"])
    from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PublicKey

    shared = server_private.exchange(X25519PublicKey.from_public_bytes(enc))
    key = vc._hkdf_sha256(shared, vc.HKDF_INFO)
    blob = base64.b64decode(envelope["ciphertext"])
    return AESGCM(key).decrypt(blob[:12], blob[12:], vc.HKDF_INFO).decode()


def main():
    server_private = X25519PrivateKey.generate()
    server_public_b64 = base64.b64encode(
        server_private.public_key().public_bytes_raw()
    ).decode()

    print("Control -- the envelope works as documented:")
    env = vc.seal_envelope(server_public_b64, "key-2026-10", "SenhaUnica-correct-horse")
    check("backend opens the envelope and recovers the password",
          backend_side(env, server_private) == "SenhaUnica-correct-horse")
    check("the password does not appear in the envelope in the clear",
          all("correct-horse" not in str(v) for v in env.values()))

    print("\nD1 -- is the envelope's metadata authenticated?")
    tampered = dict(env)
    tampered["encrypted_at"] = "1999-01-01T00:00:00Z"
    tampered["key_id"] = "key-attacker-chose"
    opened = backend_side(tampered, server_private)
    check("ciphertext still verifies after key_id AND encrypted_at are rewritten",
          opened == "SenhaUnica-correct-horse",
          "metadata is NOT covered by the AEAD")
    src = inspect.getsource(vc.seal_envelope)
    check("the AEAD additional-data argument is the constant HKDF_INFO",
          "AESGCM(key).encrypt(nonce, secret.encode(), HKDF_INFO)" in src,
          "so no envelope field is bound to the ciphertext")

    print("\n  Negative control -- the AEAD is intact where it does apply:")
    broken = dict(env)
    raw = bytearray(base64.b64decode(broken["ciphertext"]))
    raw[-1] ^= 0x01
    broken["ciphertext"] = base64.b64encode(bytes(raw)).decode()
    try:
        backend_side(broken, server_private)
        check("flipping one bit of the ciphertext is rejected", False, "it was ACCEPTED")
    except Exception as exc:
        check("flipping one bit of the ciphertext is rejected", True, type(exc).__name__)

    print("\nD2 -- is the key schedule RFC 9180?")
    ikm = b"\x11" * 32
    theirs = vc._hkdf_sha256(ikm, vc.HKDF_INFO)
    prk = hmac.new(b"\x00" * 32, ikm, hashlib.sha256).digest()
    expected = hmac.new(prk, vc.HKDF_INFO + b"\x01", hashlib.sha256).digest()
    check("the KDF is a single-block HKDF with a ZERO salt", theirs == expected,
          "32-byte output, one HMAC block, salt = 32 zero bytes")
    kdf_src = inspect.getsource(vc._hkdf_sha256) + inspect.getsource(vc.seal_envelope)
    for label in ("HPKE-v1", "suite_id", "psk_id_hash", "info_hash", "KEM", "base_nonce"):
        check("RFC 9180 element absent: " + label, label not in kdf_src)
    check("the info string is a single project-local constant",
          vc.HKDF_INFO == b"heidy-login-v1",
          repr(vc.HKDF_INFO))

    print()
    if FAILURES:
        print("FAILED: " + ", ".join(FAILURES))
        return 1
    print("All checks passed. D1 and D2 are properties of the published code, "
          "measured against a control that shows the AEAD itself is sound.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
