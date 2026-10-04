#!/usr/bin/env python3
"""p294 — `pom.xml` en el camino de PRODUCCION, con los negativos que mantienen P280 cerrado.

Pase 97 del 2026-10-04.  El pase 96 diagnostico que `p283/manifest_license.py` es ciego a
Maven, escribio el lector correcto (`p289`, 11/11) y NO lo conecto: medido, `PARSERS` tenia
cinco nombres y nada fuera de `p289/` referenciaba el lector.  Esta suite afirma las cuatro
cosas que el cableado tiene que cumplir:

  1. el lector de XML es el de p289 (P237: uno solo, no dos divergentes);
  2. la identidad de un pom se resuelve con los TRES campos y contra los DOS segmentos del
     slug -- si no, `kuali/kc` y `sakaiproject/sakai` salen FOREIGN siendo propios;
  3. P280 sigue cerrado: un pom de un tercero vendorizado sigue FOREIGN;
  4. el `<parent>` NO presta identidad ni licencia.

Uso: python3 test_wiring.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P283 = os.path.normpath(os.path.join(HERE, "..", "p283-manifest-named-license"))
sys.path.insert(0, P283)

import manifest_license as ml  # noqa: E402

OK = FAIL = 0


def check(label, got, want):
    global OK, FAIL
    if got == want:
        OK += 1
        print("ok   %-62s %s" % (label, got))
    else:
        FAIL += 1
        print("FAIL %-62s got=%r want=%r" % (label, got, want))


def fixture(name):
    with open(os.path.join(HERE, "fixtures", name), encoding="utf-8") as fh:
        return fh.read()


# --- 1. pom.xml esta REGISTRADO en el camino de produccion -------------------------------
check("pom.xml registrado en PARSERS", "pom.xml" in ml.PARSERS, True)

# --- 2. el lector de XML es el de p289, no una copia -------------------------------------
# Si p289 se mueve o se borra, esto FALLA en voz alta en vez de dejar dos lectores.
reader = ml._p289_reader()
check("el lector expone declared_license_names",
      callable(getattr(reader, "declared_license_names", None)), True)
check("y es el modulo de p289",
      "p289-maven-manifest" in os.path.normpath(reader.__file__), True)

# --- 3. identidad: los tres campos, en orden de fuerza -----------------------------------
check("identidad de kuali/kc (groupId, artifactId, name)",
      ml._maven_identity(fixture("kuali-kc.reduced.pom.xml")),
      ["org.kuali.coeus", "coeus", "Kuali Coeus"])

# --- 4. el <parent> NO presta identidad --------------------------------------------------
# seb-server hereda de org.springframework.boot. Si el parent prestara identidad, el repo
# reclamaria ser Spring Boot.
check("el <parent> no entra en la identidad",
      ml._maven_identity(fixture("parent-identity.pom.xml")), ["seb-server"])
check("sakai: el <parent> no agrega candidatos",
      ml._maven_identity(fixture("sakai-base.reduced.pom.xml")),
      ["org.sakaiproject", "base", "Sakai base pom"])

# --- 5. el defecto que este pase existe para arreglar ------------------------------------
# Con artifactId como identidad UNICA, estas dos filas salen FOREIGN siendo propias.
check("regresion medida: artifactId solo -> kuali/kc FOREIGN",
      ml.ownership("kuali/kc", "coeus"), ml.FOREIGN)
check("regresion medida: artifactId solo -> sakai FOREIGN",
      ml.ownership("sakaiproject/sakai", "base"), ml.FOREIGN)

# ... y con la resolucion de P294 pasan a propias.
check("P294: kuali/kc es propio",
      ml.ownership_any("kuali/kc", ["org.kuali.coeus", "coeus", "Kuali Coeus"])[0], ml.OWN)
check("P294: y lo gana el groupId",
      ml.ownership_any("kuali/kc", ["org.kuali.coeus", "coeus", "Kuali Coeus"])[1],
      "org.kuali.coeus")
check("P294: sakai es propio",
      ml.ownership_any("sakaiproject/sakai",
                       ["org.sakaiproject", "base", "Sakai base pom"])[0], ml.OWN)

# --- 6. P280 SIGUE CERRADO: el negativo que importa --------------------------------------
# Un pom de un tercero vendorizado no puede volverse propio por tener tres candidatos.
vend = ml.read_manifest("pom.xml", fixture("vendored-foreign.pom.xml"), "universidad/campus-lms")
check("P280 cerrado: pom vendorizado sigue FOREIGN", vend["ownership"], ml.FOREIGN)
check("P280 cerrado: y su licencia NO es atribuible", vend["attributable"], False)
check("P280 cerrado: la GPL-2 del tercero se LEE pero no se atribuye",
      vend["license"], "GNU General Public License, Version 2")

# El caso de P280 original (pase 95), en version Maven: el nombre ajeno no gana por el org.
check("P280 cerrado: ni el segmento de org crea propiedad falsa",
      ml.ownership_any("alfredang/ai-mms", ["openmage/magento-lts", "magento-lts"])[0],
      ml.FOREIGN)

# --- 7. el contrato de salida no cambio: `sweep_named.sh` lee "name" como CADENA ---------
kc = ml.read_manifest("pom.xml", fixture("kuali-kc.reduced.pom.xml"), "kuali/kc")
check('"name" sigue siendo una cadena', isinstance(kc["name"], str), True)
check('"name" es el candidato que GANO', kc["name"], "org.kuali.coeus")
check('"names" expone los tres candidatos', len(kc["names"]), 3)
check('"license_files" vacio: un pom no NOMBRA archivos (P279 no se responde aca)',
      kc["license_files"], [])
check("la declaracion de kuali/kc se lee",
      kc["license"], "GNU Affero General Public License, Version 3")
check("y es ATRIBUIBLE, que es el punto del pase", kc["attributable"], True)
check("el JSON serializa (lo que consume el barrido)",
      isinstance(json.dumps(kc, ensure_ascii=False), str), True)

# --- 8. un pom sin <licenses> no inventa licencia ----------------------------------------
noliclic = ml.read_manifest("pom.xml",
                            '<project xmlns="http://maven.apache.org/POM/4.0.0">'
                            '<artifactId>rice</artifactId></project>', "kuali/rice")
check("pom sin <licenses>: no declara licencia", noliclic["license"], None)
check("pom sin <licenses>: pero la identidad se lee", noliclic["name"], "rice")

# --- 9. lo que NO es un pom no entra por esta puerta -------------------------------------
check("un XML que no es <project> no da identidad",
      ml._maven_identity("<settings><artifactId>x</artifactId></settings>"), [])
check("XML roto no revienta", ml._maven_identity("<project><bad"), [])
check("un pom vacio devuelve None (no una fila fantasma)",
      ml.read_manifest("pom.xml", '<project xmlns="http://maven.apache.org/POM/4.0.0"/>',
                       "a/b"), None)

print("\n%d/%d" % (OK, OK + FAIL))
sys.exit(1 if FAIL else 0)
