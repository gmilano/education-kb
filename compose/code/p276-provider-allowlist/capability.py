#!/usr/bin/env python3
"""P277 — la superficie de CAPACIDAD de un proveedor se lee de sus interfaces, y no es uniforme.

«La plataforma soporta el proveedor X» no es una afirmacion completa. En Chamilo cada
clase `*Provider.php` declara QUE tipos de servicio implementa, y el factory solo registra
un (proveedor, tipo) si la clase satisface la interfaz de ese tipo:

    'text'             => AiProviderInterface
    'image'            => AiImageProviderInterface
    'video'            => AiVideoProviderInterface      (ver nota JOB abajo)
    'document'         => AiDocumentProviderInterface
    'document_process' => AiDocumentProcessProviderInterface

**P277**: *el conjunto de proveedores y el conjunto de CAPACIDADES por proveedor son dos
mediciones distintas. Un «swap de proveedor» es gratis solo en los tipos que las dos clases
implementan; en los demas el swap es un desarrollo.*

Y la herencia importa: `AnthropicProvider extends ClaudeProvider` y no declara `implements`
propio, asi que su superficie es la HEREDADA. Un lector de `implements` que no resuelva
`extends` publicaria «anthropic: cero capacidades», que es dato incorrecto.

Uso:  python3 capability.py NOMBRE=ARCHIVO.php [NOMBRE=ARCHIVO.php ...]
Salida: TSV `clase<TAB>extends<TAB>interfaces,separadas,por,coma`
"""
import re
import sys

CLASS_RE = re.compile(
    r"^\s*(?:final\s+|abstract\s+)?class\s+(\w+)"
    r"(?:\s+extends\s+(\w+))?"
    r"(?:\s+implements\s+([^{]+))?",
    re.MULTILINE,
)

# Interfaz -> tipo de servicio que habilita, segun el mapa $typeInterface del factory.
IFACE_TYPE = {
    "AiProviderInterface": "text",
    "AiImageProviderInterface": "image",
    "AiVideoProviderInterface": "video",
    "AiDocumentProviderInterface": "document",
    "AiDocumentProcessProviderInterface": "document_process",
}

# 🔴 Segunda arista de herencia, y sin ella el veredicto de `video` sale al reves:
# NINGUN proveedor declara `AiVideoProviderInterface`. Los tres que hacen video declaran
# `AiVideoJobProviderInterface`, y medido en el payload de `v3.0.1`:
#     interface AiVideoJobProviderInterface extends AiVideoProviderInterface
# El factory exige `AiVideoProviderInterface` para el tipo `video` (`instanceof`), que la
# Job SATISFACE por herencia. Un lector que compare nombres de interfaz literalmente
# publicaria «cero proveedores de video» teniendo tres.
IFACE_PARENT = {
    "AiVideoJobProviderInterface": "AiVideoProviderInterface",
}

# ⚠️ Interfaces que el proveedor declara y que el factory NO mapea a ningun tipo de
# servicio: existen en el arbol pero no habilitan un (proveedor, tipo) registrable.
# `AiSearchMediaTextProviderInterface` es el caso en `v3.0.x`. Se declara para que
# «seis interfaces» no se lea como «seis tipos»: los tipos registrables son CINCO.
NOT_A_FACTORY_TYPE = {"AiSearchMediaTextProviderInterface"}


def parse(src):
    """Devuelve (clase, extends|None, [interfaces]) de la PRIMERA clase del archivo."""
    m = CLASS_RE.search(src)
    if not m:
        return None
    name, ext, impl = m.group(1), m.group(2), m.group(3) or ""
    ifaces = [i.strip() for i in impl.split(",") if i.strip()]
    return name, ext, ifaces


def resolve(parsed):
    """Resuelve la superficie heredada.

    `parsed` es {clase: (extends, [interfaces])}. Una clase sin `implements` propio
    hereda la de su padre. Sin esto, `AnthropicProvider` mediria CERO.
    """
    out = {}

    def surface(cls, seen=()):
        if cls not in parsed or cls in seen:
            return []
        ext, ifaces = parsed[cls]
        inherited = surface(ext, seen + (cls,)) if ext else []
        # Union: una subclase puede AGREGAR interfaces sin perder las del padre.
        merged = list(inherited)
        for i in ifaces:
            if i not in merged:
                merged.append(i)
        return merged

    for cls in parsed:
        out[cls] = surface(cls)
    return out


def closure(ifaces):
    """Cierra la lista de interfaces por herencia de INTERFAZ (`IFACE_PARENT`)."""
    out = []
    for i in ifaces:
        cur = i
        while cur:
            if cur not in out:
                out.append(cur)
            cur = IFACE_PARENT.get(cur)
    return out


def types_of(ifaces):
    """Tipos de servicio REGISTRABLES, en el orden del mapa del factory.

    Cierra por herencia de interfaz primero: si no, `video` sale CERO teniendo tres.
    """
    order = ["text", "image", "video", "document", "document_process"]
    got = {IFACE_TYPE[i] for i in closure(ifaces) if i in IFACE_TYPE}
    return [t for t in order if t in got]


def main(argv):
    if not argv:
        print("uso: capability.py NOMBRE=ARCHIVO.php ...", file=sys.stderr)
        return 2
    parsed, order = {}, []
    for arg in argv:
        _, _, path = arg.partition("=")
        path = path or arg
        p = parse(open(path, encoding="utf-8").read())
        if not p:
            print(f"NO-CLAIM\tsin-clase\t{path}", file=sys.stderr)
            continue
        name, ext, ifaces = p
        parsed[name] = (ext, ifaces)
        order.append(name)
    surfaces = resolve(parsed)
    for name in order:
        ext = parsed[name][0] or "-"
        ifaces = surfaces[name]
        extra = [i for i in ifaces if i in NOT_A_FACTORY_TYPE]
        print("\t".join([
            name,
            ext,
            ",".join(types_of(ifaces)) or "-",
            str(len(types_of(ifaces))),
            ",".join(extra) or "-",
        ]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
