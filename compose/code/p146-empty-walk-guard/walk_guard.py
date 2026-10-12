"""p146-empty-walk-guard — a verdict over zero files is not a verdict.

## Why this exists

`P145-A` found `surface_gate2.py` excluding `dist` and `build` unconditionally while
7 of the 8 npm packages on this shelf keep their entire payload under exactly those two
names. It walked **zero files** and returned
`NOT_AN_MCP_SERVER (0 'mcp' tokens, no SDK import)` — a verdict over an empty file set,
published for two passes. `T42` names the class.

p145 fixed the exclusion list in its own successor (`surface_gate3.py` re-admits a built
tree its `package.json` declares). 🔴 **It did not make the shelf able to DETECT the
condition.** `p146-exclusion-reach` reads every traversing instrument on this shelf:

| | count |
|---|---|
| instruments that traverse a tree | **35** |
| …that carry an empty-walk guard | 🔴 **0** |
| …that exclude `dist`/`build` with no re-admission AND emit a verdict | 🔴 **5** |
| …that can only read a git clone, never a loose payload | 🔴 **16** |

🔵 **The exclusion list was one instrument's bug. The inability to notice is the shelf's.**

## What this module does

One function, used at the point a verdict is formed:

    status, detail = walked_or_refuse(files, root, excluded=…)

`status` is `WALKED` when at least one file was read, and `NO_PAYLOAD_WALKED` when none
was. A caller that refuses to classify on `NO_PAYLOAD_WALKED` cannot publish `P145-A`'s
error, whatever its exclusion list says.

🔵 **This is deliberately not a fix to any exclusion list.** Whether `dist/` should be
read is artefact-relative and `P144-O`/`T39` settled how to decide it: ask the artefact,
not the name. This module answers the prior question — *did I read anything at all?* — and
that question has one right answer in every artefact kind.

## The distinction the guard has to preserve

An empty walk and a walk that found nothing relevant are different states, and only the
first is an instrument failure:

  * **zero files walked** → the instrument saw no input. No verdict is available.
  * **files walked, none matched** → the instrument saw input and found no surface. That
    is a finding, and `NOT_AN_MCP_SERVER` is the correct verdict for it.

🔴 **`P145-A`'s seven rows were the first state, published as the second.**
"""

WALKED = "WALKED"
NO_PAYLOAD_WALKED = "NO_PAYLOAD_WALKED"


def walked_or_refuse(files, root="", excluded=()):
    """(status, detail) for a file set an instrument is about to form a verdict over.

    `files` is any iterable of paths the instrument actually read. It is consumed once,
    so a generator is acceptable; the count is returned in `detail`.

    `excluded` is the exclusion set the instrument applied, recorded in the detail string
    so a refusal names the likely cause rather than only the symptom.
    """
    n = sum(1 for _ in files)
    if n:
        return WALKED, "%d file(s) walked" % n
    names = ",".join(sorted(str(e) for e in excluded))
    detail = "0 files walked under %r" % (str(root),)
    if names:
        detail += " with exclusions {%s} applied" % names
    detail += " — no verdict is available over an empty file set (T42)"
    return NO_PAYLOAD_WALKED, detail


def guard_verdict(verdict, files, root="", excluded=()):
    """`verdict` unless nothing was walked, in which case `NO_PAYLOAD_WALKED`.

    The drop-in form, for an instrument whose verdict is already computed:

        return guard_verdict(v, walked_paths, root, SKIP_DIRS)
    """
    status, detail = walked_or_refuse(files, root, excluded)
    if status == NO_PAYLOAD_WALKED:
        return NO_PAYLOAD_WALKED, detail
    return verdict, detail
