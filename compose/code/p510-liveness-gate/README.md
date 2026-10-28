# `p510-liveness-gate` — a liveness instrument that can fail, and a gate that refuses counts

Closes **`Gap 509-B`**: *"a known-good AND a known-bad control before any count is published"* —
previously advice in prose, now structural. `sweep()` calls `run_controls()` first and raises
`ControlFailure` **instead of returning a count** when the instrument cannot be shown to discriminate.

## Why the prescribed check was replaced

Measured on this channel (`evidence/url-check-control.2026-10-28-p510.tsv`):

| instrument | live repo | repo that never existed | verdict |
|---|---|---|---|
| `curl -sI https://github.com/<slug>` | `403` | `403` | 🔴 zero information |
| `curl -sI https://raw.githubusercontent.com/<slug>/<branch>/LICENSE` | `200` | `404` | 🟢 discriminates |
| `git ls-remote --symref <url> HEAD` | refs + symref | credential prompt | 🟡 positive only |

The standing instruction to *"verify every URL before writing it (`curl -sI`)"* therefore verified
nothing against `github.com`: a deleted repository and a healthy one return the same byte.

## What this module does and does not claim

- 🟢 **`LIVE` is assertable** — refs came back, with the **true default branch** from the symref and a
  `HEAD` SHA.
- 🔴 **`ABSENT` is not assertable here.** GitHub answers an absent repository and a **private** one
  with the same credential prompt, so the classifier returns `UNREADABLE_ABSENT_OR_PRIVATE` and
  never "absent". Retiring an address needs a second channel (**`Gap 510-B`**).

## Run

```
python3 test_gate.py     # 8/8 offline controls, recorded fixtures, no network
python3 -c "import liveness_gate as g; g.run_controls()"   # live control check
```

`classify()` is a pure function over `ls-remote` output, which is what lets the controls run offline.

## Result on this base

All **154** distinct `github.com/<owner>/<repo>` addresses on the six live shelves read `LIVE`
(`evidence/liveness-branch-census.2026-10-28-p510.tsv`) — zero dead, zero unreadable. Branch
distribution: **104 `main`, 32 `master`, 6 `develop`, 12 one-offs** across 14 distinct
non-`main`/`master` names, reproducing `p509`'s 18-address finding on a wider population.

## It caught two of its own author's defects

1. The first classifier expected a literal "not found" and so scored the known-bad as `ERROR`. The
   gate **failed closed** and no count was published.
2. A star-cell extractor scored a bolded **HTTP 404 inside a dead-URL table** as a 404-star row — the
   "probe measures a convention" class on its sixth sighting, caught by a spot-check before
   publication.
