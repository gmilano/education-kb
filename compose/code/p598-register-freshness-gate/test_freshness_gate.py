#!/usr/bin/env python3
"""Suite de `p598-register-freshness-gate`. Pase 49 del 2026-10-08.

🔴 El caso que decide si el instrumento sirve es `test_opposite_verdicts_on_real_rows`:
dos filas REALES de este arbol tienen que salir con veredicto OPUESTO. Si las dos
salieran RANCIA, el gate seria un `grep 'unmeasured'`.
"""
import os
import sys

import freshness_gate as g

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))

# Filas reales, copiadas del registro (recortadas a lo que decide el veredicto).
ROW_246 = (
    "| 🆕 **246** | **2026-10-07**, pass 44 | `agents/top.md` · `P544` | 🔴 **OPEN.** "
    '*"No permissively-licensed Portuguese text-complexity feature extractor exists, and '
    "the spaCy `pt_core_news_*` **model artefact** licences are unmeasured.\"* |"
)
ROW_244 = (
    "| 🆕 **244** | **2026-10-07**, pass 44 | `repos/foundations.md` · `P542` | 🔴 **OPEN.** "
    '*"The read-count oracle does not reach shell, so 31 shell instruments that exit `0` '
    'after emitting output are unjudged, and 9 more time out."* |'
)
ROW_NO_CLAIM = (
    "| **233** | `intel-trends.md:62` | Gap 233 CERRADO —hay dos puertas MIT de Canvas. |"
)

FAILURES = []


def check(name, cond, detail=""):
    if cond:
        return True
    FAILURES.append(f"{name}: {detail}")
    return False


def run():
    tree = g.read_tree(ROOT)
    check("arbol_no_vacio", len(tree) >= 8, f"solo {len(tree)} archivos")

    # 🔴 El registro NO puede estar en el arbol de contradiccion.
    check("registro_excluido", all(p != g.REGISTER for p, _ in tree),
          "intel/open-gaps.md entro al arbol vivo")

    # --- EL CASO OBLIGATORIO: veredictos opuestos sobre filas reales -----------
    v246, c246, s246, h246 = g.verdict(ROW_246, tree)
    v244, c244, s244, h244 = g.verdict(ROW_244, tree)
    check("fila_246_rancia", v246 == g.V_RANCIA, f"dio {v246} (sujetos={s246}, hits={len(h246)})")
    check("fila_244_sostenida", v244 == g.V_SOSTENIDA, f"dio {v244} (sujetos={s244}, hits={len(h244)})")
    check("fila_244_es_un_claim", g.CLASS_MEASUREMENT in c244, f"clases={c244}")
    check("fila_244_sin_sujeto_medible", s244 == [], f"sujetos={s244}")
    check("opposite_verdicts_on_real_rows", v246 != v244, f"{v246} == {v244}")
    check("246_senala_el_archivo", any("verticals" in p for _, p, _, _ in h246),
          f"no cito verticals/: {[p for _, p, _, _ in h246][:4]}")
    check("246_sujeto_correcto", "pt_core_news_*" in s246, f"sujetos={s246}")

    # --- NO-CLAIM: una fila sin afirmacion de frescura no se juzga -------------
    vnc, cnc, _, _ = g.verdict(ROW_NO_CLAIM, tree)
    check("fila_sin_claim", vnc == g.V_NO_CLAIM, f"dio {vnc} clases={cnc}")

    # --- Clases de afirmacion --------------------------------------------------
    check("clase_medicion", g.CLASS_MEASUREMENT in g.claim_classes(ROW_246), "no detecto MEDICION")
    check("clase_prioridad",
          g.CLASS_PRIORITY in g.claim_classes("x the cheapest remaining win on this KB y"),
          "no detecto PRIORIDAD")
    check("prioridad_sin_medicion",
          g.claim_classes("declared the smallest gap on this KB") == [g.CLASS_PRIORITY],
          "clasifico de mas")

    # --- Sujetos: lo que NO es sujeto -----------------------------------------
    subs = g.subjects_of("| **9** | `Gap 246` `P544` `agents/top.md` `main` `LICENSE` unmeasured |")
    check("no_sujeto_gap", "Gap 246" not in subs, f"{subs}")
    check("no_sujeto_hallazgo", "P544" not in subs, f"{subs}")
    check("no_sujeto_archivo_md", "agents/top.md" not in subs, f"{subs}")
    check("no_sujeto_rama", "main" not in subs and "LICENSE" not in subs, f"{subs}")
    check("sujeto_subrayado", "EqUMP" in g.subjects_of("x `EqUMP` y unmeasured"),
          f"{g.subjects_of('x `EqUMP` y unmeasured')}")

    # --- El glob del sujeto ----------------------------------------------------
    rx = g.subject_regex("pt_core_news_*")
    check("glob_expande", bool(rx.search("spaCy pt_core_news_sm 3.8.0")), "no matcheo _sm")
    check("glob_no_sobra", not rx.search("es_core_news_sm"), "matcheo el idioma equivocado")

    # --- Marcador de medicion: hace falta, no alcanza el sujeto ---------------
    fake = [("agents/top.md", "una linea que nombra pt_core_news_sm en prosa y nada mas")]
    vf, _, _, hf = g.verdict(ROW_246, fake)
    check("sujeto_sin_marcador_no_basta", vf == g.V_SOSTENIDA,
          f"dio {vf} con {len(hf)} hits sobre prosa sin medicion")
    real = [("verticals/solutions.md", "| 2 | `pt_core_news_sm` | CC-BY-SA-4.0 | x |")]
    vr, _, _, _ = g.verdict(ROW_246, real)
    check("marcador_licencia_cuenta", vr == g.V_RANCIA, f"dio {vr}")
    byt = [("repos/foundations.md", "| `pt_core_news_sm` | payload 1,072 B | x |")]
    check("marcador_bytes_cuenta", g.verdict(ROW_246, byt)[0] == g.V_RANCIA, "bytes no contaron")

    # --- P541 / Gap 245: el gate TIENE que rechazar la invocacion vacia -------
    check("refuses_empty_input", g.main([]) == 2, f"main([]) dio {g.main([])}")
    check("refuses_sweep_sin_raiz", g.main(["--sweep"]) == 2, "--sweep sin raiz no fue rechazado")

    # --- El barrido real sobre este arbol -------------------------------------
    rows = sweep_rows = g.sweep(ROOT)
    check("barrido_no_vacio", len(sweep_rows) > 0, "el barrido no encontro filas con afirmacion")
    rancias = [r for r in rows if r[2] == g.V_RANCIA]
    sostenidas = [r for r in rows if r[2] == g.V_SOSTENIDA]
    # 🔴 La v2 de esta suite exigia que el barrido VIVO trajera rancias y sostenidas.
    # Eso ataba la suite a que el arbol siguiera ROTO: al arreglar las tres filas, la
    # asercion fallo por el motivo correcto. 🔵 La discriminacion se prueba sobre filas
    # CONSTRUIDAS, que es donde se controla la entrada; sobre el arbol vivo lo unico
    # legitimo que se puede exigir es que el barrido CLASIFIQUE, no que acuse.
    check("barrido_clasifica_todo", all(r[2] in (g.V_RANCIA, g.V_SOSTENIDA, g.V_CITA)
                                        for r in rows),
          f"veredicto fuera de vocabulario: {[r[2] for r in rows]}")
    check("barrido_discrimina_en_filas_construidas",
          g.verdict(ROW_246, [("verticals/solutions.md",
                              "| `pt_core_news_sm` | CC-BY-SA-4.0 |")])[0] == g.V_RANCIA
          and g.verdict(ROW_246, [("agents/top.md", "prosa con pt_core_news_sm")])[0]
          == g.V_SOSTENIDA,
          "el gate no parte sobre entrada controlada")

    # --- v2: la guarda de CITA (los 3 falsos positivos del barrido v1) ----------
    ROW_QUOTE = (
        "| **39** | *\"inferido de la descripcion, no probado\"* | 🔴 **SUPERSEDED — DO NOT "
        "ACT ON THIS ROW.** Pass 40 wrote: *\"still untested, the cheapest remaining win\"*. |"
    )
    vq, cq, _, hq = g.verdict(ROW_QUOTE, tree)
    check("cita_no_es_rancia", vq == g.V_CITA, f"dio {vq}")
    check("cita_igual_lleva_claim", cq, "no reconocio la afirmacion citada")
    check("cita_sin_evidencia", hq == [], f"{len(hq)} hits sobre una cita")
    check("is_quotation_detecta_cerrado", g.is_quotation("| **238** | Gap 238 CERRADO. |"), "")
    check("is_quotation_no_dispara_de_mas",
          not g.is_quotation("| **246** | OPEN. licences are unmeasured |"),
          "marco como cita una fila viva")

    # --- v2: sujetos en MAYUSCULAS (los otros 4 falsos positivos) --------------
    caps = g.subjects_of("| x `REFUSES` `MEASURES` `PATH` `P541-*` unmeasured |")
    check("no_sujeto_clase_de_veredicto", "REFUSES" not in caps and "MEASURES" not in caps, f"{caps}")
    check("no_sujeto_variable_de_entorno", "PATH" not in caps, f"{caps}")
    check("no_sujeto_clase_de_hallazgo", "P541-*" not in caps, f"{caps}")
    check("sujeto_real_sobrevive_al_filtro",
          "pt_core_news_*" in g.subjects_of("x `pt_core_news_*` `PATH` unmeasured"),
          "el filtro de mayusculas se comio un sujeto real")

    # --- v2: la PRIORIDAD se refuta con un CIERRE, no con una medicion ---------
    reg = ("| **238** | OPEN, and it is the cheapest gap on this KB |\n"
           "| **238** | Gap 238 CERRADO con un artefacto probado |\n")
    hit = g.closure_lines(238, reg, 1)
    check("cierre_posterior_cuenta", len(hit) == 1, f"{hit}")
    check("cierre_anterior_no_cuenta", g.closure_lines(238, reg, 99) == [], "conto hacia atras")
    row_pri = "| **238** | **OPEN, and it is the cheapest gap on this KB.** `qti3` |"
    vp, _, _, hp = g.verdict(row_pri, tree, 238, reg, 1)
    check("prioridad_rancia_por_cierre", vp == g.V_RANCIA, f"dio {vp}")
    check("prioridad_evidencia_es_el_cierre",
          hp and hp[0][1] == g.REGISTER, f"evidencia={hp[:1]}")
    vp2, _, _, _ = g.verdict(row_pri, tree, 238, "| **238** | sigue OPEN |", 1)
    check("prioridad_sostenida_sin_cierre", vp2 == g.V_SOSTENIDA, f"dio {vp2}")

    # --- v3: un cierre pertenece al gap DECLARADO, no al CITADO ---------------
    reg_cit = ("| **238** | OPEN, and it is the cheapest gap on this KB |\n"
               "| 🆕 **245** | PARTIALLY CLOSED at pass 49, cheaper than `Gap 240` |\n")
    check("cierre_no_se_atribuye_al_gap_citado",
          g.closure_lines(240, reg_cit, 1) == [],
          f"atribuyo el cierre de 245 a 240: {g.closure_lines(240, reg_cit, 1)}")
    check("cierre_si_cuenta_para_el_declarado",
          len(g.closure_lines(245, reg_cit, 1)) == 1,
          f"{g.closure_lines(245, reg_cit, 1)}")

    # --- v2: el barrido real, adjudicado a mano -------------------------------
    rr = [r for r in g.sweep(ROOT) if r[2] == g.V_RANCIA]
    gaps_rancios = sorted(r[1] for r in rr)
    # 🟢 Tras los punteros adelante del pase 49, las filas de `Gap 246`/`238`/`245`
    # llevan su propia correccion y salen CITA. El barrido tiene que quedar LIMPIO.
    check("barrido_v3_limpio", gaps_rancios == [], f"quedan rancias: {gaps_rancios}")
    check("barrido_v3_no_marca_39", 39 not in gaps_rancios,
          "marco Gap 39, cuyo puntero adelante ya lo arreglo el pase 48")
    citas = [r for r in g.sweep(ROOT) if r[2] == g.V_CITA]
    check("barrido_v3_reconoce_las_citas", len(citas) >= 4,
          f"solo {len(citas)} CITA — los punteros adelante del pase 49 no se reconocen")

    # --- MUTANTES: cada uno tiene que cambiar una respuesta del instrumento -----
    # 🔴 La asercion del mutante NO entra en FAILURES: se evalua aparte y se descarta.
    # Un arnes que contamina su propia lista de fallos no mide nada (la leccion de P480).
    mutants = []

    def mutant(name, apply_fn, probe_fn, restore_fn):
        """Mata al mutante si `probe_fn` cambia de respuesta con la mutacion puesta."""
        before = probe_fn()
        apply_fn()
        try:
            after = probe_fn()
        finally:
            restore_fn()
        mutants.append((name, before != after, before, after))

    import re as _re

    # 1. Sin marcadores de medicion, `Gap 246` ya no puede salir RANCIA.
    orig_markers = g.MEASURE_MARKER
    mutant("ignora_marcadores_de_medicion",
           lambda: setattr(g, "MEASURE_MARKER", (r"ZZZ_NUNCA_APARECE",)),
           lambda: g.verdict(ROW_246, tree)[0],
           lambda: setattr(g, "MEASURE_MARKER", orig_markers))

    # 2. Sin el filtro de no-sujeto, `agents/top.md` entra como sujeto.
    #    🔵 Se prueba con ESE token a proposito: `Gap 246` y `P544` los rechaza ya
    #    `SUBJECT_SHAPE`, asi que no discriminarian este mutante.
    orig_not = g.NOT_SUBJECT
    mutant("ignora_filtro_de_no_sujeto",
           lambda: setattr(g, "NOT_SUBJECT", _re.compile(r"^$")),
           lambda: "agents/top.md" in g.subjects_of("| `agents/top.md` `P544` unmeasured |"),
           lambda: setattr(g, "NOT_SUBJECT", orig_not))

    # 3. Si el registro entra al arbol vivo, se contradice consigo mismo.
    orig_reg = g.REGISTER
    mutant("incluye_el_registro_en_el_arbol",
           lambda: setattr(g, "REGISTER", os.path.join("intel", "NUNCA.md")),
           lambda: any(p == os.path.join("intel", "open-gaps.md")
                       for p, _ in g.read_tree(ROOT)),
           lambda: setattr(g, "REGISTER", orig_reg))

    # 4. Sin el rechazo de entrada vacia, el gate reproduce el defecto P541.
    orig_main = g.main
    def _no_guard(argv):
        if "--self-test" in argv:
            return 0
        return 0
    mutant("ignora_el_rechazo_de_entrada_vacia",
           lambda: setattr(g, "main", _no_guard),
           lambda: g.main([]),
           lambda: setattr(g, "main", orig_main))

    # 5. Sin la guarda de CITA, las tablas de correccion vuelven a marcarse.
    orig_corr = g.CORRECTION_MARKERS
    mutant("ignora_la_guarda_de_cita",
           lambda: setattr(g, "CORRECTION_MARKERS", (r"ZZZ_NUNCA",)),
           lambda: g.verdict(ROW_QUOTE, tree)[0],
           lambda: setattr(g, "CORRECTION_MARKERS", orig_corr))

    # 7. Sin la exigencia del numero DECLARADO, el cierre se atribuye al gap CITADO.
    #    🔵 Se muta `declared_gap` y no `GAP_ROW`: aflojar la regex no reproduce el bug
    #    (sigue capturando el primer numero, que es el declarado), asi que un mutante
    #    sobre ella SOBREVIVE sin decir nada. El defecto real era aceptar una linea que
    #    solo MENCIONA el gap, y eso es lo que este mutante hace.
    orig_decl = g.declared_gap
    mutant("atribuye_el_cierre_al_gap_citado",
           lambda: setattr(g, "declared_gap", lambda line: 240 if "Gap 240" in line
                           else orig_decl(line)),
           lambda: len(g.closure_lines(240, reg_cit, 1)),
           lambda: setattr(g, "declared_gap", orig_decl))

    # 6. Sin el filtro de MAYUSCULAS, `PATH` vuelve a entrar como sujeto.
    orig_not2 = g.NOT_SUBJECT
    mutant("ignora_el_filtro_de_mayusculas",
           lambda: setattr(g, "NOT_SUBJECT", _re.compile(r"^(?:Gap|gap)\s*\d+$")),
           lambda: "PATH" in g.subjects_of("x `PATH` unmeasured"),
           lambda: setattr(g, "NOT_SUBJECT", orig_not2))

    killed = sum(1 for _, k, _, _ in mutants if k)
    for name, k, before, after in mutants:
        if not k:
            FAILURES.append(f"MUTANTE SOBREVIVIO: {name} ({before!r} -> {after!r})")

    total = 51 + len(mutants)
    print(f"# p598 suite: {total - len(FAILURES)}/{total} aserciones, "
          f"mutantes muertos {killed}/{len(mutants)}")
    print(f"# barrido: {len(rows)} filas con afirmacion -> "
          f"{len(rancias)} RANCIA / {len(sostenidas)} SOSTENIDA")
    for f in FAILURES:
        print(f"FAIL  {f}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(run())
