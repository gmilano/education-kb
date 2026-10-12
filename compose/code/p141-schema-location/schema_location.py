"""p141-schema-location — `ACTION CX`: where does a schema actually live?

p140 pre-registered this as a question about one table:

> Resolve where `tutor-mcp` defines `pedagogical_decisions`. The table is absent from
> `db/schema.sql` while `db/pedagogical_decisions.go` and `get_decision_replay_summary`
> both exist, so the *"auditable pedagogical decisions"* half of `ACTION CT` is only half
> answered. 🔴 *Refuted if the decision log turns out to persist no learner-linked row at
> all -- which would make `P19`'s audit-trail claim rest on the affect tables alone.*

🟢 **The table is found, and it is learner-linked, so the falsifier does NOT fire.** It is
declared in `db/pedagogical_contract_schema.go` as a Go string constant holding DDL, applied
as a migration body -- not in any `.sql` file.

🔵 **And the general fact is larger than the one table.** `db/schema.sql` DOES exist, so
p140's observation was accurate about that file and misleading about the project: the schema
is composed across `.sql` files AND Go-embedded migration bodies, and the second layer holds
the large majority of it. A reviewer who reads the `.sql` files -- the conventional place, and
the only place a schema-diff tool looks -- sees a minority of the tables.

That matters here beyond tidiness. The tables that carry learner identity, affect state and
pedagogical decisions are exactly the ones a DPIA, a records-of-processing exercise or an
EU AI Act Annex III review has to enumerate. An enumeration that reads `db/*.sql` and stops
is incomplete, and nothing in the repository layout says so.

## Method

Count `CREATE TABLE [IF NOT EXISTS] <name>` declarations in two populations -- `db/*.sql`
and non-test `db/*.go` -- and report the set difference.

🔴 **This probe's first draft reported 112 tables in Go and 97 Go-only, and both figures were
one too high.** The regex matched this line of `db/postgres.go`:

    // Serialize migration across the fleet. CREATE TABLE IF NOT EXISTS is not

...yielding a table named `is`. 🔵 **A comment that quotes DDL is not DDL**, and a counter
that cannot tell the difference inflates every Go-side figure. Comments are therefore stripped
before matching, and `test_schema_location.py` pins that exact line as a fixture so the
regression cannot return. The published figures are the post-correction ones.

Line comments are stripped; `/* ... */` blocks are stripped; Go raw-string literals
(backtick-delimited) are KEPT, because that is precisely where the DDL lives.
"""

import glob
import os
import re
import sys

CREATE_TABLE = re.compile(
    r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([A-Za-z_][A-Za-z0-9_]*)", re.IGNORECASE
)


def strip_comments(text, is_go):
    """Remove comments without changing offsets of what remains.

    For Go we must not strip backtick raw strings -- the DDL is inside them -- so only
    `//` line comments and `/* */` blocks go. For SQL, `--` line comments go.
    """
    out = []
    i, n = 0, len(text)
    in_raw = False
    while i < n:
        c = text[i]
        if is_go and c == "`":
            in_raw = not in_raw
            out.append(c)
            i += 1
            continue
        if not in_raw:
            if is_go and text.startswith("//", i):
                j = text.find("\n", i)
                j = n if j < 0 else j
                out.append(" " * (j - i))
                i = j
                continue
            if not is_go and text.startswith("--", i):
                j = text.find("\n", i)
                j = n if j < 0 else j
                out.append(" " * (j - i))
                i = j
                continue
            if text.startswith("/*", i):
                j = text.find("*/", i + 2)
                j = n if j < 0 else j + 2
                out.append(" " * (j - i))
                i = j
                continue
        out.append(c)
        i += 1
    return "".join(out)


def tables_in(paths, is_go):
    found = {}
    for p in paths:
        try:
            raw = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for m in CREATE_TABLE.finditer(strip_comments(raw, is_go)):
            found.setdefault(m.group(1), set()).add(os.path.basename(p))
    return found


def survey(root):
    sql = sorted(glob.glob(os.path.join(root, "db", "*.sql")))
    go = sorted(
        p for p in glob.glob(os.path.join(root, "db", "*.go"))
        if not p.endswith("_test.go")
    )
    S = tables_in(sql, is_go=False)
    G = tables_in(go, is_go=True)
    both = set(S) & set(G)
    return {
        "sql_files": [os.path.basename(p) for p in sql],
        "go_files": len(go),
        "sql_tables": S,
        "go_tables": G,
        "only_sql": sorted(set(S) - set(G)),
        "only_go": sorted(set(G) - set(S)),
        "both": sorted(both),
        "distinct": sorted(set(S) | set(G)),
    }


COLS = ["table", "in_sql", "in_go", "go_file", "verdict"]


def main(argv):
    root = argv[0] if argv else "."
    r = survey(root)
    print("\t".join(COLS))
    for t in r["distinct"]:
        in_sql = t in r["sql_tables"]
        in_go = t in r["go_tables"]
        gof = ",".join(sorted(r["go_tables"].get(t, []))) or "-"
        verdict = "BOTH" if in_sql and in_go else ("SQL_ONLY" if in_sql else "GO_ONLY")
        print("\t".join([t, str(in_sql), str(in_go), gof, verdict]))
    tot = len(r["distinct"])
    print(
        "\n# %d distinct tables: %d in db/*.sql, %d in db/*.go (non-test), "
        "%d GO_ONLY, %d SQL_ONLY, %d BOTH"
        % (tot, len(r["sql_tables"]), len(r["go_tables"]),
           len(r["only_go"]), len(r["only_sql"]), len(r["both"])),
        file=sys.stderr,
    )
    print(
        "# a reviewer reading only db/*.sql sees %d of %d (%.0f%%)"
        % (len(r["sql_tables"]), tot, 100.0 * len(r["sql_tables"]) / tot),
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
