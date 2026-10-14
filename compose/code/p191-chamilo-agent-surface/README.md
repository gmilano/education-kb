---
industry: education
region: Global
updated: 2026-10-14
---

# `P1060` — the agent surface of a SECOND platform, and the difference between a decorator and a prompt

**Pass 191 · 2026-10-14 · 16/16 controls passing · `68` tool definitions read from `67` sources at a pinned sha**

## Why a second platform

p190 counted `openedx-mcp`'s agent surface from its decorators — `33` definitions against
`0` tool names in the README it had been counted from — and corrected a verdict it had
published from prose one pass earlier. 🔴 **One platform is an anecdote.** This instrument
asks the same question of [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms),
which ships a **native** MCP server rather than a third-party facade:

```
config/packages/mcp.yaml:  app: 'Chamilo'   version: '2.1.0'   http: { path: /mcp }
```

HEAD `6f9bb2c6198564108eae11fc57d76a7879b0017d`, `2026-10-13`. Trees via
`git clone --filter=blob:none`, bodies over `raw.githubusercontent.com` **at that sha**, not
at `HEAD`, so the count is reproducible.

## Measured

| measure | value |
|---|---|
| `#[McpTool]` definitions | **`68`** |
| reads / writes | `21` / **`47`** |
| files carrying enforcement | `18` of `67` |
| enforcement sites *(`isGranted` / `AccessDeniedException`)* | **`48`** |
| roles enforced | `ROLE_ADMIN`, `ROLE_GLOBAL_ADMIN`, `ROLE_QUESTION_MANAGER`, `ROLE_TEACHER` |
| guard words appearing **only in prose** | `confirm` |
| tools a verb cannot classify | `3`, **listed** — `generate_student_success_feedback`, `illustrate_document_paragraph`, `review_course_quality` |

## 🔴 The rule this instrument exists to enforce: a YAML `instructions:` block is a PROMPT

Chamilo's `mcp.yaml` carries an `instructions:` string of some `6` kB addressed to the model,
and it contains this sentence:

> *"Every capability must respect the permissions of the authenticated Chamilo user."*

🟢 **That is an intention, and in Chamilo's case a largely honoured one** — `48` enforcement
sites exist in code. 🔴 **But it is not evidence, and p190 is the pass that paid for
treating a security sentence as a fact.** So `guard_report()` splits what it finds: a check
in an executable body is `enforced`; the same word inside a `description:` or an
`instructions:` block is `in_prose`, counted separately and never as enforcement. The
obligatory controls in `test_surface.py` are two fixtures that differ **only** in whether
the promise is in the attribute or in the body.

## Declared limits

- 🔴 **read/write is from the tool's VERB.** It settles `68` of `68` into a class and
  `3` of those are judgement calls, which are **listed** rather than guessed:
  `generate_student_success_feedback` is counted a WRITE because it persists feedback about
  a named learner; `review_course_quality` a READ because it reports.
- 🔴 **`48` enforcement sites is not `48` guarded tools.** Sites are counted, not joined to
  tools; a file with four checks and one tool counts four. The join is `P1061`'s job if a
  later pass wants it.
- 🟡 The absence of an audit row is measured as **`0` references to `audit` or a logger
  across all `67` sources** — an enumerated absence over the MCP surface, not over the whole
  platform, which carries `36` legacy `TrackE*` tracking entities doing something else.

## Run

```sh
python3 test_surface.py                 # 16/16, offline
python3 -I surface.py <dir-of-php>      # > result.tsv
```

## Files

- `surface.py` — definitions, verb classification, enforced-vs-prose guard split
- `test_surface.py` — 16 controls, offline
- `result.2026-10-14.tsv` — **authoritative**, `68` tools with file and class
