#!/usr/bin/env python3
"""`manifest_license.py` — el nombre AUTORITATIVO del archivo de licencia vive en el
manifiesto, y el manifiesto puede describir a OTRO proyecto.

Pase 95 del 2026-10-04. Existe porque el pase 94 dejo DOS huecos escritos y una accion
pre-registrada que los junta:

- **P279**: una lista fija de nombres de licencia siempre tiene un hueco, porque el espacio
  de nombres es libre y `raw.githubusercontent.com` distingue MAYUSCULAS **tambien en la
  extension** (`openedx/XBlock` -> 33 sondas, 0 hits; el archivo es `LICENSE.TXT`). El nombre
  no hay que adivinarlo: el manifiesto lo NOMBRA en `license-files`.
- **P280**: el manifiesto hallado en la raiz puede describir a otro proyecto
  (`alfredang/ai-mms` trae un `composer.json` que se llama `openmage/magento-lts` y declara
  `["OSL-3.0","AFL-3.0"]`). Leerlo sin control de propiedad publica una licencia FALSA.

Este modulo es la parte PURA: no toca la red. Dado el payload de un manifiesto y el `org/repo`
que lo hospeda, devuelve el nombre del proyecto que el manifiesto declara, la licencia que
declara, los nombres de archivo que NOMBRA, y el veredicto de PROPIEDAD.

La clasificacion de FAMILIA de licencia no se hace aqui: es de `lib/license_family.sh` (P237).
"""
import json
import re

OWN, WEAK, FOREIGN, NONAME = "OWN", "WEAK", "FOREIGN", "NONAME"


def _tokens(s):
    """Tokens alfanumericos minusculos de la ULTIMA ruta de un nombre de paquete.

    `openmage/magento-lts` -> {'magento','lts'};  `@scope/canvas-mcp` -> {'canvas','mcp'}
    """
    if not s:
        return set()
    seg = str(s).strip().strip('"').strip("'").split("/")[-1]
    return {t for t in re.split(r"[^A-Za-z0-9]+", seg.lower()) if t}


# Tokens que NO distinguen un proyecto de otro: si la interseccion es solo esto, no es prueba
# de propiedad.  Salen de los nombres reales de esta base (`*-mcp-server`, `moodle-*`, ...).
STOPWORDS = {"server", "mcp", "ai", "app", "api", "py", "js", "ts", "node", "python",
             "lib", "core", "main", "src", "tool", "plugin", "client", "sdk", "demo"}


def ownership(repo, manifest_name):
    """P280: ¿el manifiesto describe al repo que lo hospeda?

    OWN     -> un nombre contiene al otro (modulo tokens)        -> la licencia es atribuible
    WEAK    -> se solapan, pero solo parcialmente                -> atribuible con reserva
    FOREIGN -> no se solapan en nada significativo               -> NO atribuir (P280)
    NONAME  -> el manifiesto no declara nombre                   -> no se puede decidir
    """
    if manifest_name is None or not str(manifest_name).strip():
        return NONAME
    r, m = _tokens(repo.split("/")[-1]), _tokens(manifest_name)
    if not r or not m:
        return NONAME
    if r <= m or m <= r:
        return OWN
    shared = (r & m) - STOPWORDS
    return WEAK if shared else FOREIGN


def _json_manifest(body):
    """package.json / composer.json. Devuelve (name, license, [files])."""
    try:
        d = json.loads(body)
    except Exception:
        return _loose_json(body)
    if not isinstance(d, dict):
        return (None, None, [])
    name = d.get("name")
    lic = d.get("license")
    if isinstance(lic, dict):                      # {"type":"MIT","url":...}
        lic = lic.get("type") or lic.get("name")
    elif isinstance(lic, list):                    # composer: ["OSL-3.0","AFL-3.0"]
        lic = " OR ".join(str(x) for x in lic)
    if lic is None and isinstance(d.get("licenses"), list):   # npm legado
        parts = [x.get("type") if isinstance(x, dict) else str(x) for x in d["licenses"]]
        lic = " OR ".join(p for p in parts if p)
    files = []
    for key in ("license-files", "licenseFiles", "license_files"):
        v = d.get(key)
        if isinstance(v, list):
            files += [str(x) for x in v]
        elif isinstance(v, str):
            files.append(v)
    return (name, lic, files)


def _loose_json(body):
    """JSON roto (pasa: comentarios, comas finales). Se leen las claves de primer nivel a mano."""
    def grab(key):
        m = re.search(r'"%s"\s*:\s*"([^"]*)"' % key, body)
        return m.group(1) if m else None
    name, lic = grab("name"), grab("license")
    if lic is None:
        m = re.search(r'"license"\s*:\s*\[([^\]]*)\]', body)
        if m:
            lic = " OR ".join(re.findall(r'"([^"]+)"', m.group(1)))
    files = []
    m = re.search(r'"license-files"\s*:\s*\[([^\]]*)\]', body)
    if m:
        files = re.findall(r'"([^"]+)"', m.group(1))
    return (name, lic, files)


def _toml_manifest(body):
    """pyproject.toml / Cargo.toml. Sin dependencias: se leen las lineas que importan.

    Soporta las tres formas que PEP 621 y Cargo admiten para `license`:
      license = "Apache-2.0"        -> expresion
      license = {file = "LICENSE"}  -> NOMBRA un archivo
      license = {text = "MIT"}      -> expresion embutida
    y las dos de archivo: `license-files = [...]` (PEP 639) y `license-file = "..."` (Cargo).
    """
    name = lic = None
    files = []
    for raw in body.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        m = re.match(r'^name\s*=\s*["\']([^"\']+)["\']', line)
        if m and name is None:
            name = m.group(1)
            continue
        m = re.match(r'^license[-_]files?\s*=\s*(.+)$', line)
        if m:
            files += re.findall(r'["\']([^"\']+)["\']', m.group(1))
            continue
        m = re.match(r'^license\s*=\s*(.+)$', line)
        if m and lic is None:
            val = m.group(1).strip()
            if val.startswith("{"):
                f = re.search(r'file\s*=\s*["\']([^"\']+)["\']', val)
                t = re.search(r'text\s*=\s*["\']([^"\']+)["\']', val)
                if f:
                    files.append(f.group(1))
                if t:
                    lic = t.group(1)
            else:
                q = re.match(r'^["\']([^"\']+)["\']', val)
                if q:
                    lic = q.group(1)
    return (name, lic, files)


def _ini_manifest(body):
    """setup.cfg. `license`/`license_files` viven bajo [metadata], sin comillas."""
    name = lic = None
    files = []
    for raw in body.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line or line.lstrip().startswith("["):
            continue
        m = re.match(r'^\s*name\s*=\s*(.+)$', line)
        if m and name is None:
            name = m.group(1).strip()
            continue
        m = re.match(r'^\s*license[-_]files?\s*=\s*(.*)$', line)
        if m:
            files += [x.strip() for x in re.split(r'[,\s]+', m.group(1)) if x.strip()]
            continue
        m = re.match(r'^\s*license\s*=\s*(.+)$', line)
        if m and lic is None:
            lic = m.group(1).strip()
    return (name, lic, files)



# ---------------------------------------------------------------------------
# P294 (pase 97): `pom.xml` entra al camino de PRODUCCION.
#
# El pase 96 diagnostico que este modulo es CIEGO a Maven --su `PARSERS` son Python, JS, PHP
# y Rust-- mientras la capa de plataforma educativa es JAVA/MAVEN (Kuali, Sakai, DSpace,
# OpenOLAT, UniTime, SEB Server), y escribio el lector correcto en `p289-maven-manifest/`
# con su suite en 11/11.  Lo que NO hizo fue conectarlo: medido hoy, `PARSERS` seguia con
# cinco nombres y NADA fuera de `p289/` referenciaba ese lector.  El hueco que el pase 96
# diagnostico seguia abierto justo donde se producen los veredictos.
#
# El XML no se reimplementa (P237): se importa de p289, que conserva su suite como el
# control de la lectura.  `test_wiring.py` de `p294-pom-in-production/` afirma que este
# import resuelve a ese archivo, para que mover p289 FALLE en voz alta en vez de que esta
# base termine con dos lectores de XML divergentes.
def _p289_reader():
    import importlib.util
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.normpath(os.path.join(here, "..", "p289-maven-manifest", "maven_license.py"))
    spec = importlib.util.spec_from_file_location("p289_maven_license", path)
    if spec is None or spec.loader is None:
        raise ImportError("P294: no se pudo cargar el lector de pom.xml de p289: %s" % path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _maven_identity(body):
    """Los nombres con que un `pom.xml` se identifica, en orden de fuerza (P294).

    `groupId` primero porque es un namespace reverse-DNS que suele CODIFICAR a la
    organizacion dueniaa (`org.kuali.coeus` en `kuali/kc`), que es exactamente la identidad
    que P280 quiere comparar.  Despues `artifactId` y el `<name>` humano.

    Solo hijos DIRECTOS de `<project>`: el `<parent>` de un pom es OTRO proyecto --el de
    `SafeExamBrowser/seb-server` es `org.springframework.boot`-- y tomar su identidad como
    propia es el error que P280 existe para impedir.  La suite lo afirma con su negativo.
    """
    import xml.etree.ElementTree as ET
    def local(tag):
        return tag.rsplit("}", 1)[-1] if "}" in tag else tag
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return []
    if local(root.tag) != "project":
        return []
    found = {}
    for child in root:
        key = local(child.tag)
        if key in ("groupId", "artifactId", "name") and (child.text or "").strip():
            found.setdefault(key, " ".join(child.text.split()))
    return [found[k] for k in ("groupId", "artifactId", "name") if k in found]


def _maven_manifest(body):
    """pom.xml -> (candidatos_de_identidad, licencia_declarada, []).

    Devuelve el nombre como LISTA: un pom se identifica con hasta tres campos y ninguno
    solo alcanza (medido: con `artifactId` como identidad unica, `kuali/kc` y
    `sakaiproject/sakai` salen FOREIGN siendo propios).  `read_manifest` sabe resolver
    una lista con `ownership_any`.

    Un pom no NOMBRA archivos de licencia, asi que la tercera posicion es siempre `[]`:
    de esta capa no sale la respuesta a P279, sale la DECLARACION.
    """
    names = _p289_reader().declared_license_names(body)
    lic = " OR ".join(names) if names else None
    ids = _maven_identity(body)
    return (ids or None, lic, [])


# Orden de preferencia de un veredicto de propiedad: OWN gana, NONAME es "no se sabe".
_OWN_RANK = {OWN: 3, WEAK: 2, FOREIGN: 1, NONAME: 0}


def ownership_any(repo, candidates):
    """El MEJOR veredicto de P280 entre varios candidatos, contra los DOS segmentos del slug.

    -> (veredicto, candidato_que_lo_gano)

    Por que los dos segmentos: `ownership()` compara contra `repo.split("/")[-1]`, o sea
    descarta la organizacion.  En Maven eso es fatal --`kuali/kc` declara `org.kuali.coeus`
    y `Kuali Coeus`, y NINGUNO se parece a `kc`, pero los dos se parecen a `kuali`--, y la
    fila perdida es la de licencia mas consecuente del inventario (AGPL-3.0 §13 sobre un ERP
    universitario entregado como SaaS).

    `ownership()` queda INTACTA: sus 34 aserciones siguen valiendo y las 200 filas ya
    publicadas no se mueven.  Esto es una capa de resolucion ENCIMA, no un cambio de regla.
    """
    if not candidates:
        return (NONAME, None)
    org = repo.split("/")[0] if "/" in repo else repo
    best, who = NONAME, None
    for cand in candidates:
        for target in (repo, "org/" + org):
            v = ownership(target, cand)
            if _OWN_RANK[v] > _OWN_RANK[best]:
                best, who = v, cand
    return (best, who)

PARSERS = {
    "package.json": _json_manifest,
    "composer.json": _json_manifest,
    "pyproject.toml": _toml_manifest,
    "Cargo.toml": _toml_manifest,
    "setup.cfg": _ini_manifest,
    "pom.xml": _maven_manifest,
}


def read_manifest(filename, body, repo):
    """-> dict con lo que el manifiesto declara y si es ATRIBUIBLE al repo (P280)."""
    parser = PARSERS.get(filename.split("/")[-1])
    if parser is None or not body:
        return None
    name, lic, files = parser(body)
    if name is None and lic is None and not files:
        return None
    # P294: un parser puede devolver VARIOS candidatos de identidad (pom.xml). El contrato de
    # salida no cambia -- "name" sigue siendo una cadena, la que GANO el veredicto -- porque
    # `sweep_named.sh` lee esa clave.
    candidates = list(name) if isinstance(name, (list, tuple)) else None
    if candidates is not None:
        own, winner = ownership_any(repo, candidates)
        name = winner if winner is not None else (candidates[0] if candidates else None)
    else:
        own = ownership(repo, name)
    return {
        "manifest": filename,
        "name": name,
        "names": candidates,
        "license": lic,
        "license_files": files,
        "ownership": own,
        # P280: si el manifiesto es de otro proyecto, su licencia NO se publica como la del repo.
        "attributable": own in (OWN, WEAK),
    }


if __name__ == "__main__":
    import sys
    fn, repo = sys.argv[1], sys.argv[2]
    r = read_manifest(fn, sys.stdin.read(), repo)
    print(json.dumps(r, ensure_ascii=False) if r else "null")
