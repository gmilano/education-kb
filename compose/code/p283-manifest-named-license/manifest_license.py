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


PARSERS = {
    "package.json": _json_manifest,
    "composer.json": _json_manifest,
    "pyproject.toml": _toml_manifest,
    "Cargo.toml": _toml_manifest,
    "setup.cfg": _ini_manifest,
}


def read_manifest(filename, body, repo):
    """-> dict con lo que el manifiesto declara y si es ATRIBUIBLE al repo (P280)."""
    parser = PARSERS.get(filename.split("/")[-1])
    if parser is None or not body:
        return None
    name, lic, files = parser(body)
    if name is None and lic is None and not files:
        return None
    own = ownership(repo, name)
    return {
        "manifest": filename,
        "name": name,
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
