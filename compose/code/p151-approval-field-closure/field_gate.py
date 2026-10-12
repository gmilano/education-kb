#!/usr/bin/env python3
"""p151-approval-field-closure — `ACTION FF`: close `P35`'s data-layer gap.

> 🔴 **`ACTION FF`** *(re-registered twice)* — close `P35`'s data-layer gap: state the
> exact change that would make the approval gate unbypassable (`StudentServer.store`
> private, or an approval token threaded into `StudentStore`'s write methods) and write
> the failing test that would hold it.
> 🔴 *Refuted if no change to the subject's own code can close it* — which would mean the
> gate is inherently a protocol-boundary control, and `P35` must be re-pitched as an
> MCP-surface pattern with the data layer named as out of scope.

🟢 **The falsifier is SILENT. Two lines of the subject's own code close it.**

## The exact change

    - pub struct StudentServer { pub store: Arc<StudentStore> }
    + pub struct StudentServer { store: Arc<StudentStore> }
    +
    + impl StudentServer {
    +     pub fn new(store: Arc<StudentStore>) -> Self { Self { store } }
    + }

and the ONE call site, `src/main.rs`:

    -     let server = StudentServer { store };
    +     let server = StudentServer::new(store);

🟢 **One call site in the whole repository.** The repo's own 24 tests never construct a
`StudentServer`, so nothing else moves.

## Why the privacy keyword is the whole fix, and not half of one

🔵 **A Rust integration test is its own crate.** p149 demonstrated the bypass from
`tests/`, so the bypass it demonstrated is the bypass a *downstream consumer* has — and
`pub`/private is exactly the boundary that closes. Measured, pass 151:

| tree | the bypass test | the repo's own suite |
|---|---|---|
| HEAD | 🔴 **compiles and PASSES** — `place_hold` returns `active == true` with no approval, no protocol version and no sealed state | 🟢 24 pass |
| patched | 🟢 **FAILS TO COMPILE** — `E0616` ×2 on the two `.store` reads, and `E0451` on the struct literal | 🟢 24 pass, plus the constructor control |

🔵 **Two distinct compiler errors, because there are two surfaces**: reading the field
(`E0616`) and building the struct around it (`E0451`). 🔴 **An honest note on how they
were observed**: in one file rustc reported only the two `E0616`s; `E0451` appeared when
the struct literal was isolated into a test of its own. Both surfaces are closed; the
*reporting* is ordered, not the closure.

## 🔴 What this does NOT close, said rather than implied

🔴 **An IN-CRATE bypass remains.** `pub`/private is a module boundary, so a future module
inside `mcp-student-records` can still reach `self.store` and call a `pub fn` write on
`StudentStore`. Closing *that* needs the action's second option — a sealed approval token
minted only by the gate and threaded into all 23 write signatures — which is a 23-site
change to a repository this KB does not own. 🟢 **So the recommendation is split: ship the
two-line privacy change, and hold the in-crate surface with THIS GATE in CI**, which is
the artefact below. 🆕 **`T83`.**

## The gate

`gate()` reads the crate's own source and asserts three things, which is why it is the
failing test the action asked for — it returns non-zero on HEAD and zero after the patch:

  1. the `store` field is NOT `pub`;
  2. a public constructor exists, so the private field is still usable;
  3. no module in the crate reads `.store` outside `server.rs` — the in-crate surface
     that the privacy keyword cannot hold.

    python3 field_gate.py /path/to/mcp-student-records
"""
import os
import re
import sys

FIELD_PUB = re.compile(r"pub\s+struct\s+StudentServer\s*\{\s*pub\s+store\b")
FIELD_PRIVATE = re.compile(r"pub\s+struct\s+StudentServer\s*\{\s*store\b")
CONSTRUCTOR = re.compile(r"pub\s+fn\s+new\s*\(\s*store\s*:")
STORE_READ = re.compile(r"\bself\.store\b|\b\w+\.store\b")
APPROVAL_TOOLS = re.compile(r"approval_tools\s*:\s*\[(.*?)\]", re.S)
TOOL_NAME = re.compile(r'"([a-z0-9_]+)"')


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def sources(crate):
    src = os.path.join(crate, "src")
    if not os.path.isdir(src):
        return []
    return [os.path.join(src, f) for f in sorted(os.listdir(src))
            if f.endswith(".rs")]


def approval_tools(crate):
    """The names the macro gates. 🔵 The denominator for any claim about the gate."""
    for p in sources(crate):
        m = APPROVAL_TOOLS.search(read(p))
        if m:
            return TOOL_NAME.findall(m.group(1))
    return []


def field_state(crate):
    """`PUB`, `PRIVATE` or `ABSENT` for `StudentServer.store`."""
    for p in sources(crate):
        t = read(p)
        if FIELD_PUB.search(t):
            return "PUB"
        if FIELD_PRIVATE.search(t):
            return "PRIVATE"
    return "ABSENT"


def has_constructor(crate):
    return any(CONSTRUCTOR.search(read(p)) for p in sources(crate))


def external_store_reads(crate):
    """Files other than `server.rs` that touch a `.store` — the in-crate surface."""
    out = []
    for p in sources(crate):
        if os.path.basename(p) in ("server.rs",):
            continue
        for i, line in enumerate(read(p).splitlines(), 1):
            if STORE_READ.search(line) and "StudentStore" not in line:
                out.append("%s:%d" % (os.path.basename(p), i))
    return out


def gate(crate):
    """(exit_code, report). Non-zero while the data layer is reachable from outside."""
    state = field_state(crate)
    ctor = has_constructor(crate)
    reads = external_store_reads(crate)
    tools = approval_tools(crate)
    report = ["approval_tools=%d  field=%s  constructor=%s  in-crate .store reads=%d"
              % (len(tools), state, "yes" if ctor else "no", len(reads))]
    bad = []
    if state != "PRIVATE":
        bad.append("1. StudentServer.store is %s — every consumer can bypass the gate"
                   % state)
    if state == "PRIVATE" and not ctor:
        bad.append("2. the field is private and no public constructor exists — the "
                   "server cannot be built")
    for r in reads:
        bad.append("3. in-crate .store read at %s — the surface privacy cannot hold" % r)
    report.extend("  FAIL " + b for b in bad)
    if not bad:
        report.append("  OK   the data layer is reachable only through the tool router")
    return (1 if bad else 0), report


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    code, report = gate(argv[1])
    for ln in report:
        print(ln)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
