#!/usr/bin/env python3
"""Pass 45, action 1: re-extract the UniTime API surface from the tree.

The pass-42 version of this gate was built BEFORE the four controls that pass 44
had to invent for SEB Server existed. This extractor is the audited replacement.
It changes WHERE the route comes from, which is the whole point:

  * the route is the Spring BEAN NAME -- the value of @Service("/api/x") -- because
    ApiServlet.getConnector() does applicationContext.getBean(servletPath+pathInfo).
    getName() is NOT the route: ApiConnector only feeds it to getCacheMode().
    The pass-42 table carried getName() and the gate pasted "/api/" in a Python
    f-string, so the route was inferred twice and never read.
  * the servlet prefix is read from WEB-INF/web.xml (<url-pattern>/api/*</url-pattern>),
    not assumed, and the deploy context is read from pom.xml (<warName>UniTime</warName>).
  * a verb that the connector does not override is still a live HTTP route: the
    ApiConnector base class answers 501, not 404. 15 connectors x 4 verbs = 60
    routes, of which 26 are implemented.
  * a connector whose doGet dispatches on a query parameter into doPost crosses the
    read/write boundary, so the verb cannot be the write boundary for it.

Reproduce the checkout with:
    git clone --depth 1 --filter=blob:none --sparse https://github.com/UniTime/unitime ut
    cd ut && git sparse-checkout set JavaSource WebContent/WEB-INF

    python3 extract_surface.py [path-to-unitime-checkout] [out-dir]
"""
import os
import re
import sys

TREE = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("UNITIME_TREE", "./ut")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
CDIR = os.path.join(TREE, "JavaSource/org/unitime/timetable/api/connectors")
WEBXML = os.path.join(TREE, "WebContent/WEB-INF/web.xml")
POM = os.path.join(TREE, "pom.xml")

VERBS = ("Get", "Post", "Put", "Delete")
# A doGet body that reaches one of these is mutating state despite the verb.
CROSS = re.compile(r"do(Post|Put|Delete)\(helper\)|getQueueProcessor\(\)\.remove\(")


def read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def servlet_prefix():
    """The ApiServlet url-pattern, read from web.xml. Returns e.g. '/api'."""
    xml = read(WEBXML)
    m = re.search(r"<servlet-mapping>\s*<servlet-name>\s*apiServlet\s*</servlet-name>"
                  r"\s*<url-pattern>\s*([^<\s]+)\s*</url-pattern>", xml)
    if not m:
        raise SystemExit("web.xml: apiServlet has no url-pattern -- do not guess it")
    return m.group(1).rstrip("/*").rstrip("/")


def war_context():
    """The deploy context path, read from pom.xml <warName>. '' if absent (ROOT)."""
    if not os.path.exists(POM):
        return ""
    m = re.search(r"<warName>\s*([^<\s]+)\s*</warName>", read(POM))
    return "/" + m.group(1) if m else ""


def body_of(src, verb):
    """The source text of public void do<verb>(ApiHelper ...) { ... }, brace-matched."""
    m = re.search(r"public\s+void\s+do%s\s*\(\s*(?:final\s+)?ApiHelper\b[^)]*\)[^{]*\{" % verb, src)
    if not m:
        return None
    i, depth = m.end(), 1
    while i < len(src) and depth:
        if src[i] == "{":
            depth += 1
        elif src[i] == "}":
            depth -= 1
        i += 1
    return src[m.end():i]


def guard_methods(src):
    """Names of methods that raise 'Application Properties: ... must be set'.

    Walks the file once, tracking the most recent method signature, and returns
    the methods whose body contains the guard. That is the measurement the
    'guarded' column needs: the guard sits in a validator, not in the handler.
    """
    out, cur = [], None
    sig = re.compile(r"(?:public|private|protected)\s+[\w<>\[\],.\s]+?(\w+)\s*\([^;{]*\)[^;{]*\{")
    for line in src.splitlines():
        m = sig.search(line)
        if m:
            cur = m.group(1)
        if cur and re.search(r"Application Properties:.*must be set", line):
            out.append(cur)
    return sorted(set(out))


def extract():
    prefix, ctx = servlet_prefix(), war_context()
    rows = []
    for fn in sorted(os.listdir(CDIR)):
        if not fn.endswith(".java"):
            continue
        src = read(os.path.join(CDIR, fn))
        cls = fn[:-5]

        bean = re.search(r'@Service\(\s*"([^"]+)"\s*\)', src)
        if not bean:                      # not a routed connector; skip, do not invent
            continue
        route = bean.group(1)

        name = re.search(r"protected\s+String\s+getName\(\)\s*\{[^}]*?return\s+\"([^\"]*)\"", src, re.S)
        name = name.group(1) if name else ""

        impl, crossing = [], []
        for v in VERBS:
            b = body_of(src, v)
            if b is None:
                continue
            impl.append(v)
            if CROSS.search(b):
                crossing.append(v)

        # A route whose handler refuses unless application properties are set.
        # Measured, not assumed: find the method that raises the "must be set"
        # IllegalArgumentException, then see which do<Verb> bodies call it.
        guarded = []
        guard_fns = guard_methods(src)
        for v in impl:
            b = body_of(src, v) or ""
            if any(re.search(r"\b%s\s*\(" % re.escape(fn), b) for fn in guard_fns):
                guarded.append(v)

        rows.append({
            "cls": cls,
            "route": route,
            "name": name,
            "verbs": impl,
            "crossing": crossing,
            "guarded": guarded,
            "prefix": prefix,
            "ctx": ctx,
        })
    return rows, prefix, ctx


def main():
    rows, prefix, ctx = extract()
    path = os.path.join(OUT, "connectors.tsv")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("# UniTime API surface, extracted from UniTime/unitime JavaSource.\n")
        fh.write("# route = the @Service bean name, which is what ApiServlet.getBean() looks up.\n")
        fh.write("# It is absolute inside the webapp context; the deployed URL is <context>+route.\n")
        fh.write("# servlet url-pattern read from WEB-INF/web.xml: %s/*\n" % prefix)
        fh.write("# deploy context read from pom.xml <warName>: %s\n" % (ctx or "(ROOT)"))
        fh.write("# verbs = the do<Verb>(ApiHelper) overrides. A verb NOT listed is still a live\n")
        fh.write("# route: ApiConnector answers 501 NOT_IMPLEMENTED, not 404.\n")
        fh.write("# crossing = verbs whose handler mutates state or delegates to another verb.\n")
        fh.write("# guarded  = verbs that refuse at runtime unless application properties are set.\n")
        fh.write("#class\troute\tname\tverbs\tcrossing\tguarded\n")
        for r in rows:
            fh.write("\t".join([
                r["cls"], r["route"], r["name"],
                " ".join(r["verbs"]),
                " ".join(r["crossing"]) or "-",
                " ".join(r["guarded"]) or "-",
            ]) + "\n")

    tools = sum(len(r["verbs"]) for r in rows)
    print(f"connectors with a @Service bean name : {len(rows)}")
    print(f"implemented (connector x verb)       : {tools}")
    print(f"live HTTP routes incl. 501 fallbacks : {len(rows) * len(VERBS)}")
    print(f"servlet prefix (web.xml)             : {prefix}/*")
    print(f"deploy context (pom.xml warName)     : {ctx or '(ROOT)'}")
    print(f"routes that are NOT literal          : "
          f"{len([r for r in rows if '${' in r['route'] or not r['route'].startswith('/')])}")
    for r in rows:
        if r["crossing"]:
            print(f"  verb-crossing: {r['route']} {r['crossing']}")
        if r["guarded"]:
            print(f"  property-guarded: {r['route']} {r['guarded']}")
    print(f"written: {path}")


if __name__ == "__main__":
    main()
