# SEB Server MCP gate — the second instance of the P85 allowlist pattern

Closes the open half of **gap 86**: of the two institutional exam layers in this KB,
UniTime (timetabling) already had an MCP gate (`../unitime-mcp-gate`, pattern **P85**)
and **SEB Server** (supervision) did not. Now both do, so the exam layer —
*scheduling plus proctoring* — can be proposed end to end with a usable licence.

Upstream: [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server),
**Apache-2.0**, default branch `master`, measured at commit `7f45689`.

## What it does

Exposes SEB Server's REST surface as MCP tools and partitions them so that

* `tools/list` is built **from the allowlist**, so a withheld tool is never advertised, and
* a withheld `tools/call` is refused with JSON-RPC **`-32601`** *before* the upstream is
  reached — the stub upstream counts its own calls, so "withheld" means "never
  dispatched", not "dispatched and rejected".

## Why the allowlist cannot be derived from route discovery

This is the finding that justifies the pattern rather than just using it.

`ReadonlyEntityController` **keeps** the inherited `PUT` / `POST` / `DELETE`
`@RequestMapping` annotations and throws `AccessDeniedException` in the method body:

```java
@Override
@RequestMapping(method = RequestMethod.PUT, ...)
public T savePut(@Valid @RequestBody final T modifyData) {
    throw new AccessDeniedException(ONLY_READ_ACCESS);
}
```

So the write route **still exists and still advertises itself**. A generator that
trusts the annotations emits write tools that look legitimate; the refusal only
happens at runtime, deep inside the controller. The gate therefore denies **by
name**, never by discovery.

A second reason: `ExamAdministrationController` declares a **`PATCH`** mapping, a verb
absent from the base CRUD surface. A manifest built only from `EntityController`'s ten
operations would silently miss it.

## The data, read from the tree and not from documentation

| file | what it holds | measured |
|---|---|---|
| `endpoints.tsv` | the `*_ENDPOINT` constants of `gbl/api/API.java` | **42** on `master` (47 on `development`) |
| `operations.tsv` | per-controller operations, `own` + `inherited` | **79** for the four target endpoints |

The base CRUD surface in `operations.tsv` comes from the two abstract controllers:
`EntityController` declares **10** operations, `ActivatableEntityController` adds **3**
distinct ones (its fourth, `POST (root)`, is an override of the base).

Two constants share the path `/exam` — `EXAM_ADMINISTRATION_ENDPOINT` and
`LMS_FULL_INTEGRATION_EXAM_ENDPOINT`. A manifest keyed by **path** collapses them; this
one is keyed by constant and controller, so it does not.

## Policy

* **Read-only** — every `POST` / `PUT` / `DELETE` / `PATCH` tool is withheld.
* **Named deny** — `/batch-action` is refused outright, *reads included*. It is a
  bulk-action executor: one call fans out across many entities, which is the same
  reason P85 denies UniTime's `script` connector.

Override either with `SEB_ALLOW` (comma-separated tool names) or by editing
`default_allowlist`.

## Run the proof

```sh
python3 test_gate.py     # stdlib only; SEB Server is never started
```

Measured on `master` @ `7f45689`:

```
operations read from the tree: 79
tools in the manifest:        79
tools exposed by tools/list:  36
...
11/11 checks passed
```

* **37** write tools across `/exam`, `/lms-setup`, `/useraccount`, `/batch-action` → all `-32601`
* **11** `/batch-action` tools → all outside the allowlist, reads included
* **0** withheld calls reached the upstream (asserted on the stub's own counter)
* **36** read tools still dispatch, so the gate is not vacuously refusing everything

## Scope, stated rather than implied

`operations.tsv` carries the four endpoints the pase-42 handoff named for
verification — `/exam`, `/lms-setup`, `/useraccount`, `/batch-action` — measured
controller by controller. The remaining **26** concrete controllers (30 in total, plus
the 3 abstract bases) are **not** yet in the table: their base classes are unmeasured,
and `ReadonlyEntityController` is precisely why that cannot be guessed from the
endpoint name. Extending the table is mechanical — one fetch per controller, same two
columns — and is **not** done here.
