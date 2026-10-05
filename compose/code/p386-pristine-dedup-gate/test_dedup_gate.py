#!/usr/bin/env python3
"""Suite de P386. El caso 1 es el defecto REAL medido en el pase 118."""
import dedup_gate as g

ok = fail = 0


def t(name, cond):
    global ok, fail
    if cond:
        ok += 1; print(f"PASS {name}")
    else:
        fail += 1; print(f"FAIL {name}")


# --- Caso 1: el defecto real. Tres repos SIN relacion, mismo sha256 Apache-2.0 pristino.
PRISTINE = [
    {"repo": "buriro-ezekia/mwalimulens-agent", "sha256": "c71d239df917", "bytes": 11357, "holder": "NOT-APPLICABLE"},
    {"repo": "mazhar266/fedena",                "sha256": "c71d239df917", "bytes": 11357, "holder": "NOT-APPLICABLE"},
    {"repo": "webtech-network/autograder",      "sha256": "c71d239df917", "bytes": 11357, "holder": "NOT-APPLICABLE"},
]
clusters, abstained = g.group(PRISTINE)
t("licencia pristina NO produce ningun cluster", len(clusters) == 0)
t("los 3 repos ajenos quedan abstenidos, no fundidos", len(abstained) == 3)

# --- Caso 2: linaje REAL (titular presente) SI deduplica.
REAL = [
    {"repo": "vishalsachdev/canvas-mcp", "sha256": "5385a26e2face987", "bytes": 1071, "holder": "Vishal Sachdev"},
    {"repo": "sirdanielm/canvas-mcp",    "sha256": "5385a26e2face987", "bytes": 1071, "holder": "Vishal Sachdev"},
    {"repo": "fdis111/canvas-mcp",       "sha256": "5385a26e2face987", "bytes": 1071, "holder": "Vishal Sachdev"},
]
clusters, abstained = g.group(REAL)
t("titular presente produce 1 cluster de linaje", len(clusters) == 1)
t("el cluster de linaje tiene los 3 forks", len(list(clusters.values())[0]) == 3)
t("no hay abstenidos cuando el titular esta presente", abstained == [])

# --- Caso 3: no fundir lo pristino con lo real aunque compartan hash.
MIX = PRISTINE + REAL
clusters, abstained = g.group(MIX)
t("mezcla: 1 cluster real + 3 abstenidos", len(clusters) == 1 and len(abstained) == 3)

# --- Caso 4: GPL-3.0 pristino se comporta igual que Apache-2.0.
t("GPL-3.0 pristino (35.187 B) tambien se abstiene",
  g.dedup_key({"repo": "a/b", "sha256": "f7fe4d0adcbc", "bytes": 35187, "holder": "NOT-APPLICABLE"}) is None)

# --- Caso 5: tamaño de boilerplate PERO titular presente -> no es pristino.
t("11.357 B con titular presente NO es pristino (no se abstiene)",
  g.dedup_key({"repo": "a/b", "sha256": "x", "bytes": 11357, "holder": "Alguien"}) is not None)

# --- Caso 6: titular ausente con tamaño desconocido tambien se abstiene.
t("titular ausente se abstiene aunque el tamaño no sea boilerplate conocido",
  g.dedup_key({"repo": "a/b", "sha256": "y", "bytes": 999, "holder": ""}) is None)

# --- Caso 7: el deduplicador ingenuo de P379 habria fundido los 3. Control negativo.
naive = {}
for r in PRISTINE:
    naive.setdefault((r["sha256"], r["holder"]), []).append(r["repo"])
t("control: el par ingenuo (sha256,titular) SI funde los 3 ajenos",
  len(naive) == 1 and len(list(naive.values())[0]) == 3)

print(f"\n{ok}/{ok+fail} checks passed")
raise SystemExit(1 if fail else 0)
