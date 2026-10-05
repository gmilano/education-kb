#!/usr/bin/env python3
"""Suite de P385. Cada caso nombra el sesgo que demuestra."""
import binding_interval as b

ok = fail = 0


def t(name, cond):
    global ok, fail
    if cond:
        ok += 1; print(f"PASS {name}")
    else:
        fail += 1; print(f"FAIL {name}")


# El defecto REAL: una fila que nombra los forks como HANDLES pelados.
HANDLES = [
    "| upstream | https://github.com/vishalsachdev/canvas-mcp | MIT, `sha256:5385a26e2face987` |",
    "| forks | `sirdanielm` `fdis111` `BartMassey-upstream` | `sha256:5385a26e2face987` |",
]
t("anclado a URL NO ve el racimo escrito como handles",
  len(b.clusters(b.extract(HANDLES, permissive=False))) == 0)

# Dos URLs en filas distintas: los dos extractores lo ven.
URLS = [
    "| a | https://github.com/krishna16-origin/ai-tutor | `sha256:de8107bf9312862c` |",
    "| b | https://github.com/maxew6/ai-tutor-project | `sha256:de8107bf9312862c` |",
]
t("anclado a URL si ve un racimo escrito como URLs",
  len(b.clusters(b.extract(URLS, permissive=False))) == 1)
t("los dos extractores convergen cuando la convencion es uniforme",
  b.interval(URLS)[0] == b.interval(URLS)[1] == 1)

# Co-ocurrencia de parrafo: el permisivo infla.
COOC = [
    "Resumen: `VedShh/Tutor-AI` y `pupilfirst/pupilfirst` y `krishna16-origin/ai-tutor` con `sha256:de8107bf9312862c`",
]
t("el permisivo liga repos que solo comparten el parrafo",
  len(b.clusters(b.extract(COOC, permissive=True))) == 1)
t("el anclado no se deja enganar por el parrafo de resumen",
  len(b.clusters(b.extract(COOC, permissive=False))) == 0)

# El intervalo es la medicion: piso <= techo siempre.
MIX = HANDLES + URLS + COOC
floor, ceil = b.interval(MIX)
t("piso <= techo", floor <= ceil)
t("en el estante mezclado los extractores DIVERGEN", floor < ceil)

# Normalizacion: 16 y 64 hex del mismo valor son el mismo fingerprint.
NORMALIZE = [
    "| a | https://github.com/x/one | `sha256:8b211ca07d3f7842a35b8926d4958200735eeb53ee6433ccfb29ffc3c3120efa` |",
    "| b | https://github.com/y/two | `sha256:8b211ca07d3f` |",
]
t("16-hex y 64-hex del mismo valor normalizan al mismo fingerprint",
  len(b.clusters(b.extract(NORMALIZE, permissive=False))) == 1)

# Ruido de rutas no es un repo.
NOISEY = [
    "| a | https://github.com/x/one | `main/LICENSE` `sha256:aaaaaaaaaaaa` |",
    "| b | https://github.com/x/one | `docs/README.md` `sha256:aaaaaaaaaaaa` |",
]
t("rutas y archivos no se cuentan como repos",
  len(b.clusters(b.extract(NOISEY, permissive=True))) == 0)

print(f"\n{ok}/{ok+fail} checks passed")
raise SystemExit(1 if fail else 0)
