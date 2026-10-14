#!/usr/bin/env python3
"""Suite de `p1049`. Cada caso es una forma MEDIDA en el pase 185 sobre una fila real.

🔵 Dos casos son FALSOS POSITIVOS del limbo 1 y están marcados como tales: el test fija el
comportamiento actual y nombra lo que debería pasar, para que una futura versión no los
apruebe por accidente.

    python3 -I test_bare_token_grant.py
"""
import importlib.util, pathlib, re, sys

HERE = pathlib.Path(__file__).parent
FIX = HERE / "fixtures"


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace(".py", ""), HERE / name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


L1 = load("bare_token_grant.py")
L2 = load("whole_readme_scan.py")

# (fixture, verdicto esperado del limbo 1, identificador esperado o None)
CASES_L1 = [
    ("md-bare-token.md",                 "BARE_TOKEN",  "MIT"),
    ("md-licence-british-spelling.md",   "BARE_TOKEN",  "Apache 2.0"),
    ("md-incorporation-by-reference.md", "PROSE_TERMS", None),
    ("md-badge-only.md",                 "BADGE_ONLY",  "MIT"),
    ("md-dangling-file-reference.md",    "BARE_TOKEN",  "MIT"),
    ("md-restricted-token.md",           "BARE_TOKEN",  "MIT"),
    ("md-claim-not-grant.md",            "PROSE_TERMS", None),
    ("md-spanish-bespoke-grant.md",      "PROSE_TERMS", None),
    ("md-no-licence-anywhere.md",        "NO_HEADING",  None),
    # 🔴 FALSO POSITIVO 1: el token pertenece a una DEPENDENCIA y la sección reserva derechos.
    # Lo correcto sería PROSE_TERMS/RESERVED. Queda fijado para que se vea cuando cambie.
    ("md-dependency-inventory.md",       "BARE_TOKEN",  "AGPL-3"),
    # 🟢 CORREGIDO en p185: este caso era BARE_TOKEN por DOS bugs a la vez — el encabezado es
    # una POLÍTICA de contribución, y el token "MIT" venía de "sub|mit ". Con el límite de
    # palabra delante, la sección ya no declara identificador y el veredicto es el correcto.
    ("md-policy-heading.md",             "PROSE_TERMS", None),
    # 🔴 El control positivo que venció al limbo 1: cesión en prosa, sin encabezado.
    ("md-prose-grant-no-heading-zh.md",  "NO_HEADING",  None),
]

# El limbo 2 debe VER los dos que el limbo 1 no ve.
CASES_L2_MUST_HIT = [
    "md-prose-grant-no-heading-zh.md",
    "md-incorporation-by-reference.md",
]

FALSE_POSITIVES = {"md-dependency-inventory.md"}  # p185 corrigió el segundo


def main():
    fails = []
    for fixture, want_verdict, want_token in CASES_L1:
        text = (FIX / fixture).read_text(encoding="utf-8")
        got = L1.classify_text(fixture, text)
        if got["verdict"] != want_verdict:
            fails.append(f"{fixture}: verdict {got['verdict']!r} != {want_verdict!r}")
        if want_token and want_token.lower() not in got["token"].lower():
            fails.append(f"{fixture}: token {got['token']!r} does not contain {want_token!r}")

    for fixture in CASES_L2_MUST_HIT:
        text = (FIX / fixture).read_text(encoding="utf-8")
        hits = [l for l in text.split("\n") if L2.IDENT.search(l)]
        if not hits:
            fails.append(f"{fixture}: limbo 2 no encontró identificador y debía")

    # El filtro NOISE del limbo 2 es el que costó una fila real (Omni-Edu). Lo dejamos MEDIDO.
    omni = "The code is licensed under Apache-2.0. Model weights and third-party datasets and benchmarks retain their respective licenses."
    if not L2.IDENT.search(omni):
        fails.append("regresión: el identificador de Omni-Edu ya no se detecta")
    if not L2.NOISE.search(omni):
        fails.append("el filtro NOISE dejó de suprimir la línea de Omni-Edu: "
                     "si es intencional, retirar esta aserción y actualizar el README")

    # Un id hexadecimal NO debe contar como CC0 (bug medido en speedyapply).
    # Los dos bugs de límite de palabra medidos en p185, fijados contra regresión.
    hexline = "https://jobs.ashbyhq.com/g2/64dcc04a-a0e7-493b-b899-dd4c56e561fd"
    if L2.IDENT.search(hexline):
        fails.append(f"CC0/BSD no debe coincidir dentro de un id hexadecimal: {hexline}")
    if L1.TOKEN_RE.search("Please do not submit content that is not licensed"):
        fails.append('MIT no debe coincidir dentro de "submit"')

    print(f"casos limbo 1: {len(CASES_L1)}  (de los cuales FALSOS POSITIVOS fijados: {len(FALSE_POSITIVES)})")
    print(f"casos limbo 2: {len(CASES_L2_MUST_HIT)} + 2 aserciones de regresión")
    if fails:
        print("\nFALLOS:")
        for f in fails:
            print("  🔴", f)
        return 1
    print("🟢 todo verde")
    return 0


if __name__ == "__main__":
    sys.exit(main())
