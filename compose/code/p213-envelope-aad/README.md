---
industry: education
region: Global
updated: 2026-10-04
---

# P213 — Qué autentica realmente el sobre de login de `usp-mcp` (pase 72 del 2026-10-03)

`iDavi/usp-mcp` (GPL-3.0, Brasil) es **la primera pieza de código LATAM que esta base mide desde el
pase 68** y es **la única del inventario que se niega a mandar la contraseña institucional en
claro**: sella la *Senha Única* de la USP contra la clave pública publicada por el backend antes
del `POST /auth/login`. Es una respuesta **arquitectónica** al problema de credencial que esta base
viene midiendo desde el pase 53, y es la mejor que tiene.

**Este test no la discute. Mide las dos cosas en que la frase del README —
*«HPKE-Base(X25519, HKDF-SHA256, AES-256-GCM)»*— es más fuerte que el código:**

- **D1 — los metadatos del sobre NO están autenticados.** El *additional data* del AEAD es la
  constante `HKDF_INFO`, así que `key_id` y `encrypted_at` viajan al lado del *ciphertext* sin
  nada que los ate. **Reescritos los dos, el tag de AES-GCM sigue verificando.**
- **D2 — el *key schedule* tiene FORMA de HPKE, no es RFC 9180.** `_hkdf_sha256` es un
  extract-and-expand de **un solo bloque con salt CERO** y un `info` constante; RFC 9180 deriva por
  un *schedule* atado a la suite (`suite_id`, etiquetas `"HPKE-v1"`, `psk_id_hash`, `info_hash`).
  El propio docstring lo dice —*«matching the backend's vault»*—: el sobre **interopera con UN
  backend**, no con bibliotecas HPKE.

**Ninguno de los dos es una afirmación de vulnerabilidad.** D1 es una propiedad que hay que saber
**antes** de que un despliegue ponga un relay en ese camino; D2 es un hecho de **portabilidad**: un
cliente que no pueda alcanzar `heidy-backend.fly.dev` **no se reconstruye con una implementación
HPKE de estantería**.

**Control negativo, en la misma corrida:** volteado **un bit** del *ciphertext*, el backend
**rechaza** (`InvalidTag`). El AEAD está intacto donde sí aplica — que es lo que hace que D1 sea una
observación sobre el **alcance** del AAD y no sobre la criptografía.

`vendored_crypto.py` es `src/usp_mcp/crypto.py` traído textual de `HEAD` el 2026-10-03,
`sha256:bfe4ecaf4e48fd1c97028f7403f3bbaf985609e314d2927f34588a49bc680149` (2.136 B).

```
python3 test_envelope.py      # 13 checks, control positivo y negativo incluidos
```
