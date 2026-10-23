# PROPOSED patch to `licence-grant-gate/grant_gate.py` — `394-A` + `394-B`

🔴 **Unapplied.** See the README: the repository's own Python could not be run in `p395`'s
environment, so `test_grant_gate.py`'s controls for `P453`–`P459` were not executed. Apply this only
together with a run of that suite.

The change is confined to `probe_repo` plus two module-level additions. `verdict`, `reads_as_grant`,
`family_of`, `holder_of` and every other pure function are **untouched**, so no existing control over
them can change outcome.

## 1. Two module-level additions

```python
# ---------------------------------------------------------------- 394-B
# CRAN enforces the `License:` field in DESCRIPTION, and five shelved R
# packages carry their grant NOWHERE ELSE - no licence-shaped file at any tree
# path, and GitHub's own sidebar shows nothing. p1052-stale-absence already
# knew this; the instrument that writes verdicts did not.
MANIFEST_PATHS = ("DESCRIPTION", "package.json", "pyproject.toml", "Cargo.toml")

# The exact note reads_as_grant() returns when a payload is present but no
# family is recognisable in the title region. This is the ONLY condition the
# 394-A fall-through may act on: a payload that yields a family, or that is an
# explicit refusal (P455), must still decide the row immediately.
NO_FAMILY_NOTE = "payload present but no known licence family in title region"
```

and a reader for the manifest arm:

```python
def manifest_grant(name, text):
    """394-B. DESCRIPTION is read verbatim because CRAN enforces the field."""
    if name == "DESCRIPTION":
        m = re.search(r"^License:\s*(.+)$", text, re.I | re.M)
        return m.group(1).strip() if m else None
    m = re.search(r'"license"\s*:\s*"([^"]+)"', text, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r'^license\s*=\s*[\{"]?\s*(?:text\s*=\s*")?([^"\}\n]+)',
                  text, re.I | re.M)
    return m.group(1).strip() if m else None
```

## 2. `probe_repo` — the fall-through and the manifest arm

```diff
 def probe_repo(repo, branches=("main", "master", "develop"), get=None):
     """Only network entry point. `get(url) -> (status, text)`; injectable."""
     ...
     base = "https://raw.githubusercontent.com/%s/%s/%s"
+    fallback = None
     for b in branches:
         for name in LICENCE_PATHS:
             st, body = get(base % (repo, b, name))
             if st == 200 and body.strip():
                 v = verdict(body)
                 v["path"] = "%s/%s" % (b, name)
                 v["bytes"] = len(body.encode("utf-8"))
-                return v
+                # 394-A: a family, or an explicit refusal, decides the row.
+                if v["note"] != NO_FAMILY_NOTE:
+                    return v
+                # A stub-shaped payload. Remember it and KEEP READING.
+                if fallback is None:
+                    fallback = v
+    # 394-B: the manifest arm, between the ladder and the existence fallback.
+    for b in branches:
+        for name in MANIFEST_PATHS:
+            st, body = get(base % (repo, b, name))
+            if st != 200 or not body.strip():
+                continue
+            dec = manifest_grant(name, body)
+            if dec:
+                return {"state": "MANIFEST-ONLY", "family": dec[:40],
+                        "granted": True, "holder": None,
+                        "path": "%s/%s" % (b, name),
+                        "bytes": len(body.encode("utf-8")),
+                        "note": "MANIFEST-ONLY: %s declares %r" % (name, dec[:40])}
     for b in branches:
         for name in EXISTENCE_PATHS:
             st, body = get(base % (repo, b, name))
             if st == 200:
                 v = verdict(None, readme_text=body or " ")
                 v["path"] = "%s/%s" % (b, name)
                 return v
-    return verdict(None)
+    return fallback or verdict(None)
```

## 3. Controls a successor should add to `test_grant_gate.py`

All offline, all with a negative control, in the suite's existing style:

| Control | Asserts |
|---|---|
| stub at `LICENSE`, MIT at `LICENSE.md`, injected `get` | `LICENSED/MIT`, `path` ends `LICENSE.md` — **394-A positive** |
| the same stub **alone**, nothing else in the tree | state is the stub verdict, **not** `ABSENT` — the fall-through must not lose a payload it skipped |
| MIT at `LICENSE` (position 0) | returns at position 0 — **negative control: first-hit-correct is undisturbed** |
| an explicit `all rights reserved` payload at position 0 with MIT at position 1 | returns the **refusal** — a reservation is not a stub, and `P455`/`P459` must still decide |
| `DESCRIPTION` with `License: GPL (>= 3)` and no licence file | `MANIFEST-ONLY`, family read verbatim — **394-B positive** |
| `DESCRIPTION` with **no** `License:` line | falls through to the existence arm — **394-B negative control** |
| a tree with nothing at all | `ABSENT` — the whole chain can still say no |

🔵 The last one matters most. Every change here moves in one direction — absence to grant — so the
control that keeps it honest is the one proving the instrument can still refuse.
