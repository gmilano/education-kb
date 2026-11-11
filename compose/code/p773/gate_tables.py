#!/usr/bin/env python3
"""p773 gate-tables -- written from scratch per ACTION p772-A.
Contract: no markdown table BODY row on a curated shelf may be a column-header,
a placeholder, or an example row -- i.e. a row that compiles into a KB entity
with a generic label as its name ("nombre", "repo", "licencia").
Reports candidates for a HAND READ. It does not publish a verdict by itself.
"""
import re, sys, json, unicodedata

# Generic column-label vocabulary. A row whose EVERY non-empty cell is one of
# these carries no specific referent and cannot be a real entity.
GENERIC = {
 "name","nombre","nome","repo","repos","repository","repositorio","url","link","enlace",
 "license","licence","licencia","licenca","licença","grant","description","descripcion",
 "descripción","desc","agent","agente","agents","tool","tools","platform","plataforma",
 "project","proyecto","stars","star","estrellas","notes","note","nota","notas","comment",
 "comments","category","categoria","categoría","type","tipo","class","status","estado",
 "verdict","region","industry","updated","date","fecha","version","owner","author",
 "language","lang","idioma","use case","usecase","what it is","what it does","purpose",
 "why","how","value","count","rows","row","field","campo","key","id","summary","detail",
 "details","address","direction","source","fuente","evidence","score","rank","metric",
 "item","element","title","titulo","título","org","organization","vendor","provider",
}
PLACEHOLDER = {
 "...","…","tbd","tba","todo","xxx","yyy","zzz","n/a","na","none","-","--","---","?","??",
 "ejemplo","example","examples","sample","foo","bar","baz","qux","lorem ipsum","lorem",
 "placeholder","your repo","your-repo","repo-name","nombre del repo","etc","etc.",
}

def norm(cell: str) -> str:
    s = cell.strip()
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", s)      # images
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)   # links -> label
    s = s.replace("`","").replace("*","").replace("_","")
    s = re.sub(r"<[^>]+>", " ", s)                   # html
    # strip emoji / symbols
    s = "".join(ch for ch in s if unicodedata.category(ch)[0] not in ("S","C"))
    s = re.sub(r"\s+", " ", s).strip().lower()
    s = s.rstrip(":").strip()
    return s

SEP = re.compile(r"^\s*\|?[\s:\-\|]+\|[\s:\-\|]*$")
def is_sep(line):
    return bool(SEP.match(line)) and "-" in line

def cells(line):
    t = line.strip()
    if t.startswith("|"): t = t[1:]
    if t.endswith("|"): t = t[:-1]
    return [c for c in t.split("|")]

def tables(lines):
    """yield (header_idx, sep_idx, [body_idx...])"""
    i = 0
    n = len(lines)
    while i < n:
        if "|" in lines[i] and i+1 < n and is_sep(lines[i+1]) and not is_sep(lines[i]):
            h, s = i, i+1
            body = []
            j = i+2
            while j < n and "|" in lines[j] and lines[j].strip().startswith("|"):
                if is_sep(lines[j]): break
                body.append(j); j += 1
            yield (h, s, body)
            i = j
        else:
            i += 1

# D1 (p773): key/value meta-tables quote field names AS DATA. Exempt that shape.
KV_HEADERS = [{"field","value"},{"key","value"},{"property","value"},{"field","content"},
              {"name","value"},{"setting","value"},{"attribute","value"}]
def is_kv_table(hdr_cells):
    hn = {norm(c) for c in hdr_cells if norm(c) != ""}
    return any(hn == kv for kv in KV_HEADERS)

def classify(hdr_cells, row_cells):
    if is_kv_table(hdr_cells):
        return None
    nz = [norm(c) for c in row_cells]
    nz = [c for c in nz if c != ""]
    if len(nz) < 2:
        return None
    hn = [norm(c) for c in hdr_cells if norm(c) != ""]
    if nz == hn:
        return "DUPLICATE-HEADER"
    if all(c in GENERIC for c in nz):
        return "HEADER-ROW-AS-DATA"
    if all(c in PLACEHOLDER for c in nz):
        return "PLACEHOLDER-ROW"
    if all((c in GENERIC or c in PLACEHOLDER) for c in nz):
        return "GENERIC-OR-PLACEHOLDER"
    return None

TAB=[0]; ROW=[0]
def scan(path):
    out = []
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.read().split("\n")
    for h, s, body in tables(lines):
        TAB[0]+=1; ROW[0]+=len(body)
        hc = cells(lines[h])
        for b in body:
            rc = cells(lines[b])
            v = classify(hc, rc)
            if v:
                out.append({"file":path,"line":b+1,"verdict":v,
                            "header":" | ".join(x.strip() for x in hc)[:90],
                            "row":lines[b].strip()[:140]})
    return out

# ---- self-controls: the gate must pass these before its output is trusted ----
CONTROLS = [
 # (name, markdown, expect_flag_count)
 ("C1 positive: literal header row as data",
  "| Name | Repo | License |\n|---|---|---|\n| Nombre | Repo | Licencia |\n", 1),
 ("C2 negative: real rows",
  "| Name | Repo | License |\n|---|---|---|\n| Kolibri | learningequality/kolibri | MIT |\n", 0),
 ("C3 positive: placeholder row",
  "| Name | Repo | License |\n|---|---|---|\n| ... | TBD | N/A |\n", 1),
 ("C4 negative: numeric/verdict table",
  "| Verdict | Rows | What it means |\n|---|---|---|\n| body:canonical | 1,258 | Build on it |\n", 0),
 ("C5 negative: a cell that merely CONTAINS a generic word",
  "| Field | Value |\n|---|---|\n| region | North America |\n", 0),
 ("C6 negative: two-col real data",
  "| Address | State |\n|---|---|\n| enovation/moodle-local_mcp_helper | EXISTS-BUT-EMPTY |\n", 0),
 ("C7 positive: emoji/backtick-wrapped header row as data",
  "| Name | Repo |\n|---|---|\n| **`Nombre`** | 🟢 `Repo` |\n", 1),
 ("C8 negative: single-cell row",
  "| Name | Repo |\n|---|---|\n| MIT | |\n", 0),
 ("C9 negative (D1): key/value meta-table quoting field names as data",
  "| field | value |\n|---|---|\n| `type` | `project` |\n", 0),
 ("C10 positive: kv-exemption must NOT leak to entity tables",
  "| Name | Repo | License |\n|---|---|---|\n| name | repo | licencia |\n", 1),
]

def run_controls():
    import tempfile, os
    fails = []
    for nm, md, exp in CONTROLS:
        fd, p = tempfile.mkstemp(suffix=".md"); os.close(fd)
        open(p,"w",encoding="utf-8").write(md)
        got = len(scan(p))
        os.unlink(p)
        if got != exp:
            fails.append(f"{nm}: expected {exp} got {got}")
    return fails

if __name__ == "__main__":
    if sys.argv[1:2] == ["--controls"]:
        f = run_controls()
        print("CONTROLS: %d/%d pass" % (len(CONTROLS)-len(f), len(CONTROLS)))
        for x in f: print("  FAIL", x)
        sys.exit(1 if f else 0)
    f = run_controls()
    if f:
        print("REFUSING TO REPORT: gate's own controls fail:")
        for x in f: print("  FAIL", x)
        sys.exit(2)
    allout = []
    for p in sys.argv[1:]:
        allout += scan(p)
    print(json.dumps(allout, indent=1, ensure_ascii=False))
    print("TOTAL CANDIDATES: %d" % len(allout), file=sys.stderr)
    print("DENOMINATOR: %d tables, %d body rows over %d files" % (TAB[0], ROW[0], len(sys.argv)-1), file=sys.stderr)
