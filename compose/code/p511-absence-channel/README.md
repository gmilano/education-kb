# `p511-absence-channel` — the half of `p510`'s prescribed instrument that is false, made unusable

`p510` replaced `curl -sI github.com` (which answers **403** to a live repository and a deleted one
alike) with two instruments, and stated the second one too strongly:

> `git ls-remote --symref` for liveness and the true default branch, `raw.githubusercontent.com`
> for payloads (**200** live / **404** absent).

🟢 The first half holds. 🔴 **The `404 absent` half is false, and the population it fails on was
already enumerated by `p509`.**

## The refutation, measured this pass

`p509`'s `T34` proved by enumeration that **18 shelf addresses carry no grant at all**. On those,
the discriminating probe `raw/<ref>/LICENSE` returns the same byte as a repository that never
existed:

| slug | `git ls-remote --symref` | `raw HEAD/LICENSE` | truth |
|---|---|---|---|
| [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench) | `ref: refs/heads/main` | **404** | 🟢 **LIVE** |
| [`h9-tect/AI-Roadmaps`](https://github.com/h9-tect/AI-Roadmaps) | `ref: refs/heads/main` | **404** | 🟢 **LIVE** |
| `zzzz-nonexistent-org-9931/nope-repo-9931` | credential prompt | **404** | 🔴 never existed |

And the failure is not confined to the grant-nil set. [`oppia/oppia`](https://github.com/oppia/oppia)
— live, public, **6,950★**, Apache-2.0, a shelf row — answers **404** on `README.md` at **both**
`HEAD` and `develop` while serving `LICENSE` **200** and `develop/package.json` **200**. There is no
path whose absence is informative, because no path is guaranteed present.

🔵 `p510`'s gate **code** is not at fault: it probed `LICENSE` and its 8/8 controls were green. The
defect is the generalisation in the shelf prose, and the fact that the chosen path is itself missing
on a population this base has already listed.

## What this module does

- 🟢 `classify()` returns `LIVE`, `UNREADABLE_ABSENT_OR_PRIVATE` or `UNKNOWN_NO_USABLE_OBSERVATION`.
  **There is no code path that returns `ABSENT`** — a control asserts this over the whole
  observation cross-product.
- 🔴 `liveness_from_raw(404)` **raises `UnsoundProbe` instead of answering**. `200` grades `LIVE`.
- 🟡 A **private** repository inside this session's scope answers `REF_OK`, because the proxy injects
  credentials — verified on `gmilano/education-kb`. So `UNREADABLE` cannot be narrowed from here
  either, in **either** direction, and `Gap 510-B` stays open as a channel limit rather than a
  query problem.
- 🟢 A repository that the MCP catalogue **silently excludes** still grades `LIVE` from the git
  channel. [`openedx/edx-platform`](https://github.com/openedx/edx-platform) was silently absent
  from a **5-slug** batch reporting `incomplete_results: false` this pass — a **fifth consecutive**
  reproduction of `Gap 504-A`, and the smallest batch it has been seen at.

## Controls

`python3 -I test_gate.py` → **12/12 green**, offline, fixtures only. `sweep()` calls `run_controls()`
first and raises `ControlFailure` rather than returning a dictionary, per `Gap 509-B`'s precondition.

Reads: [`absence-truth-table.2026-10-28-p511.tsv`](../../../evidence/absence-truth-table.2026-10-28-p511.tsv).
