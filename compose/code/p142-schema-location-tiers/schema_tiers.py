"""p142-schema-location-tiers — `ACTION DD`: is `T31` a property of `tutor-mcp`, or of
embedded-migration stacks generally?

p141 pre-registered:

> Test `T31` on a **second** non-`.sql` component: run `p141-schema-location` over
> `nitsuah/bb-mcp` (TypeScript) and one Python education component as a control, and report the
> `.sql`-visible share for each. 🔴 *Refuted if the majority of tables in the second component
> are declared in `.sql` -- which would make `T31` a property of `tutor-mcp` rather than of
> embedded-migration stacks, and it must then be withdrawn rather than narrowed.*

## What had to change from p141's probe, and why it is a correction rather than a port

p141's `schema_location.py` globs `db/*.sql` and `db/*.go`. 🔴 **That is not a method, it is
`tutor-mcp`'s directory layout.** Run unchanged against any other project it returns zero tables
and the honest reading of that zero is "the probe looked in the wrong place", not "this project
declares no schema". So the population here is the whole tracked tree, partitioned by extension,
with vendored and generated trees excluded.

p141's comment-stripping is kept and extended per language, because its reason generalises
exactly: 🔵 **a comment that quotes DDL is not DDL**, in any language.

  * Go      -- `//`, `/* */` stripped; backtick raw strings KEPT (p141's rule, unchanged)
  * TS / JS -- `//`, `/* */` stripped; backtick template literals KEPT, for the same reason
  * Python  -- `#` stripped; triple-quoted strings KEPT, since that is where Python puts DDL
  * SQL     -- `--`, `/* */` stripped

🔴 **Python needed one rule Go did not.** A triple-quoted docstring is lexically identical to a
triple-quoted DDL literal, so keeping triple-quotes keeps docstrings too -- and a docstring that
documents a table (*"Creates table learners if absent"*) is prose. The `CREATE TABLE` regex only
fires on the SQL keyword pair, so documentation ABOUT a table does not match while DDL inside a
docstring does; `test_schema_tiers.py` pins both halves.
"""

import os
import re
import subprocess
import sys

CREATE_TABLE = re.compile(
    r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[`\"'\[]?([A-Za-z_][A-Za-z0-9_]*)",
    re.IGNORECASE,
)

SQL_EXT = (".sql",)
HOST_EXT = {
    ".go": "go", ".ts": "ts", ".tsx": "ts", ".js": "ts", ".jsx": "ts", ".mjs": "ts",
    ".py": "py", ".rb": "rb", ".php": "php", ".java": "java", ".kt": "java",
    ".rs": "rs", ".cs": "java",
}
EXCLUDE = ("/node_modules/", "/vendor/", "/.git/", "/dist/", "/build/", "/target/",
           "/__pycache__/", "/.venv/", "/venv/", "/third_party/", "/site-packages/")
TEST_HINT = ("_test.go", "test_", "_test.py", ".test.ts", ".test.js", ".spec.ts",
             ".spec.js", "/tests/", "/test/", "/__tests__/")


def tracked(repo):
    out = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", "HEAD"],
                         capture_output=True, text=True, timeout=180).stdout
    return [p for p in out.splitlines() if not any(e in "/" + p for e in EXCLUDE)]


def is_test(rel):
    low = "/" + rel.lower()
    return any(h in low for h in TEST_HINT)


def strip_comments(text, lang):
    """Remove comments without disturbing the string literals that hold DDL."""
    line_tok = {"go": "//", "ts": "//", "java": "//", "rs": "//", "cs": "//",
                "py": "#", "rb": "#", "php": "//", "sql": "--"}.get(lang, "//")
    keep_raw = {"go": ("`",), "ts": ("`",), "py": ('"""', "'''"), "rb": (), "sql": ()}
    raws = keep_raw.get(lang, ())
    out, i, n = [], 0, len(text)
    in_raw = None
    while i < n:
        if in_raw:
            if text.startswith(in_raw, i):
                out.append(in_raw)
                i += len(in_raw)
                in_raw = None
                continue
            out.append(text[i])
            i += 1
            continue
        hit = next((r for r in raws if text.startswith(r, i)), None)
        if hit:
            in_raw = hit
            out.append(hit)
            i += len(hit)
            continue
        if text.startswith(line_tok, i):
            j = text.find("\n", i)
            j = n if j < 0 else j
            out.append(" " * (j - i))
            i = j
            continue
        if lang != "py" and text.startswith("/*", i):
            j = text.find("*/", i + 2)
            j = n if j < 0 else j + 2
            out.append(" " * (j - i))
            i = j
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def tables(repo, paths, lang):
    found = {}
    for rel in paths:
        full = os.path.join(repo, rel)
        try:
            if os.path.getsize(full) > 4_000_000:
                continue
            raw = open(full, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in CREATE_TABLE.finditer(strip_comments(raw, lang)):
            found.setdefault(m.group(1), set()).add(rel)
    return found


def survey(repo):
    files = [p for p in tracked(repo) if not is_test(p)]
    sql = [p for p in files if p.lower().endswith(SQL_EXT)]
    hosts = {}
    for p in files:
        ext = os.path.splitext(p)[1].lower()
        if ext in HOST_EXT:
            hosts.setdefault(HOST_EXT[ext], []).append(p)
    S = tables(repo, sql, "sql")
    H = {}
    for lang, paths in hosts.items():
        for t, where in tables(repo, paths, lang).items():
            H.setdefault(t, set()).update(where)
    return S, H, len(sql), sum(len(v) for v in hosts.values()), sorted(hosts)


COLS = ["subject", "languages", "sql_files", "host_files", "tables_total",
        "in_sql", "host_only", "sql_only", "both", "sql_visible_share", "verdict"]


def main(argv):
    print("\t".join(COLS))
    for spec in argv:
        subject, _, repo = spec.partition("=")
        S, H, nsql, nhost, langs = survey(repo)
        distinct = set(S) | set(H)
        total = len(distinct)
        host_only = sorted(set(H) - set(S))
        sql_only = sorted(set(S) - set(H))
        both = sorted(set(S) & set(H))
        share = (100.0 * len(S) / total) if total else 0.0
        if total == 0:
            verdict = "NO_DDL_FOUND"
        elif len(S) * 2 > total:
            verdict = "MAJORITY_IN_SQL"
        else:
            verdict = "MINORITY_IN_SQL"
        print("\t".join([subject, "+".join(langs) or "-", str(nsql), str(nhost),
                         str(total), str(len(S)), str(len(host_only)),
                         str(len(sql_only)), str(len(both)),
                         "%.0f%%" % share, verdict]))
        print("# %-28s %d tables; %d in .sql (%.0f%%); %d host-only -> %s"
              % (subject, total, len(S), share, len(host_only), verdict), file=sys.stderr)
        if host_only:
            print("#   host-only: %s" % ", ".join(host_only[:14]), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
