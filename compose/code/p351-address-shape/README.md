# `p351-address-shape` — `ACTION ZZ-an`

**Question.** Every identity instrument on these shelves quotes its coverage against the
count of addresses harvested from them. `p350` sampled the 17 addresses its identity run
had recorded `UNANSWERED` and found **8 were never addresses** — GitHub navigation paths
read as `owner/repo`, two planted controls, and a README placeholder. So the denominator
is inflated, and `ACTION ZZ-an` was registered to republish it.

**Answer, re-derived 2026-10-21 by `p355` over the nine shelves, AFTER its writes.**

| cifra | valor |
|---|---:|
| harvested folded shapes | **2 483** |
| rejected — not addresses | **33** |
| **addresses, corrected** | **2 450** |
| inflation | **1.33 %** |

`p349`/`p350` published **2 462** and `p351`–`p354` published *2 476 → 2 443*. 🔴 `p355`
rewrote six of the nine shelves, so this triple had to be re-derived rather than carried:
`make address-shape-census` was run as the **last act before the commit**, which is the
procedure `gate-census-currency` exists to enforce and which `p355`'s own first run
violated.

🟢 **The rejected count is unchanged at 33, and that is the load-bearing part.** The
harvested total moved 2 476 → 2 483 purely because `p355` restored 72 addresses its own
rewrite had dropped (the `openeduhub/*` estate among them) — caught by
`p348-fold-identity`, re-probed first-hand, all 72 alive, and now pinned by equality in
`test_no_address_is_dropped`. The non-address shapes this instrument rejects — the
`topics/*` and `trending/*` navigation namespaces, `your-username/SafeTutors` and the
rest — are unaffected by a shelf rewrite, which is the evidence that the inflation this
gate measures is a property of the harvest and not of the prose.

## 🔴 ZZ-an's own prescription is insufficient, and that is the finding

ZZ-an asked for a filter rejecting `topics/`, `orgs/`, `repos/`, `trending/` and
placeholder owners. Run shelf-wide that rejects **28 of 33** and misses **five**:

| missed shape | class | why no namespace list reaches it |
|---|---|---|
| `search/repositories` | `NAV-NAMESPACE` | a **fifth** namespace ZZ-an did not name — a blacklist is complete only against the examples that prompted it |
| `.../archive` `.../blob` `.../releases` | `OWNER-ELLIDED` | prose writing a URL as `github.com/.../blob/main/LICENSE` leaves an owner that is literally `...` |
| `GIT_USER_ID/GIT_REPO_ID` | `OWNER-TEMPLATE-VAR` | the swagger/openapi-generator placeholder. It is not a placeholder *word*, so no list of `your-`/`example-` prefixes reaches it |

## 🟡 Both arms are load-bearing, and neither is sufficient alone

- **The shape rule** is GitHub's own naming rule (owner: 1–39 chars, alphanumerics and
  interior single hyphens; name: 1–100 chars of alphanumerics `.` `-` `_`). It needs no
  foresight: `...` fails on the dot, `git_user_id` on the underscore, an empty component
  on length. It reaches **6** of the 33.
- **The namespace and placeholder lists** reach the other **27**. They are needed because
  `topics/education` passes GitHub's rules outright — **legality is not repository-hood.**

Reporting only the first would have looked more elegant and missed 27 shapes.

## 🔵 What this does NOT claim

No network call. A legal shape is not a live repository. This separates *cannot be an
address* from *may be an address* and nothing else — whether an address answers is
`p293-slug-existence-oracle`'s question, and whether two addresses are one repository is
`p349-name-collision`'s. **A pass that reads 2 443 as a coverage figure has overclaimed
in exactly the way ZZ-an was registered to stop.**

## Run

```
cd compose/code/p351-address-shape && python3 -I test_address_shape.py   # 22 controls
make gate-address-shape                                                  # standing gate
make address-shape-census                                                # the 33, by class
```

Standing in `make hooks` since p351.
