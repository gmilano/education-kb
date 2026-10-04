#!/usr/bin/env python3
"""p289 — leer la licencia DECLARADA en un `pom.xml` de Maven.

Por que existe (pase 96 del 2026-10-04).  `p283/sweep_named.sh` es el barrido
manifiesto-consciente de esta base, y su lista de manifiestos es

    MANIFESTS="pyproject.toml package.json composer.json Cargo.toml setup.cfg"

o sea Python, JS, PHP y Rust.  **No tiene `pom.xml`.**  Y la capa de PLATAFORMA educativa
—justo la capa a la que el pase 95 apunto su accion pre-registrada— es JAVA/MAVEN: Kuali,
Sakai, OpenEMIS, TAO, SEB Server.  Medido hoy: `kuali/kc` (Kuali Coeus, administracion de
investigacion) NO tiene archivo de licencia entre los 5 nombres sondeados, y su `pom.xml`
declara `<name>GNU Affero General Public License, Version 3</name>`.  Con el instrumento
viejo esa fila sale `SIN_LICENCIA`; es `SOLO_MANIFIESTO`, y la familia es AGPL-3.0, que es
la mas consecuente de todas para un entregable SaaS.

**No trae classificador propio (P237).**  Extrae el NOMBRE declarado y lo entrega a
`lib/license_family.sh::osi_family_of`, que ya classifica declaraciones cortas bajo su
guarda de tamanio.  Este archivo solo responde "que nombre declara el pom".

Y lee XML, no texto (P171 en version XML): el propio `pom.xml` de `kuali/kc` nombra la AGPL
en un COMENTARIO de cabecera, asi que un lector por `grep` acierta por la via equivocada y
acertaria igual en un pom que solo MENCIONE una licencia.  El control negativo esta en la suite.

Uso:  python3 maven_license.py <pom.xml>     -> un nombre declarado por linea (vacio si no hay)
"""
import sys
import xml.etree.ElementTree as ET


def _local(tag):
    """Nombre de etiqueta sin namespace: los pom traen xmlns de Maven."""
    return tag.rsplit('}', 1)[-1] if '}' in tag else tag


def declared_license_names(pom_text):
    """Los <name> de <project><licenses><license>, en orden. [] si no hay declaracion.

    Solo mira el <licenses> que es hijo DIRECTO de <project>: un pom puede traer
    <licenses> dentro de un perfil o de un plugin, y esa no es la licencia del proyecto.
    """
    try:
        root = ET.fromstring(pom_text)
    except ET.ParseError:
        return []
    if _local(root.tag) != 'project':
        return []
    out = []
    for lics in root:
        if _local(lics.tag) != 'licenses':
            continue
        for lic in lics:
            if _local(lic.tag) != 'license':
                continue
            for child in lic:
                if _local(child.tag) == 'name' and (child.text or '').strip():
                    out.append(' '.join(child.text.split()))
    return out


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('uso: python3 maven_license.py <pom.xml>')
    with open(sys.argv[1], encoding='utf-8', errors='replace') as fh:
        for name in declared_license_names(fh.read()):
            print(name)
