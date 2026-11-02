# p603 — the README channel needs a spelling ladder, for the same reason the licence channel did

`lib/probe_payload.sh` line 155 reads the README at **exactly one spelling**:

    _raw "$1" "$2" README.md

That single line is the fallback rung the library's own header calls its most valuable
trap — *"No filename ladder in this base would have found it — the README's own licence
LINK did, in one request"* (measured on `OS4ED/openSIS-Classic`, GPL-2.0 at
`docs/License.txt`). 🔴 **On any repository whose README is not spelled `README.md`, that
rung cannot fire at all**, and a repo with a subdirectory payload falls through to
`NO-PAYLOAD`.

🟢 Measured on this base's own promotion backlog, `2026-11-02`
([`../../../evidence/readme-spelling-ladder.2026-11-02-p603.tsv`](../../../evidence/readme-spelling-ladder.2026-11-02-p603.tsv)):

| README path | repos |
| --- | --: |
| `README.md` | `100` |
| `readme.md` | `3` |
| `README.rst` | `2` |
| `Readme.md` | `1` |
| no README at any probed spelling | `1` |
| **invisible to a `README.md`-only probe** | 🔴 **`6` of `106` = `5.7 %`** |

🔵 **This is the same error class the licence ladder already paid to fix, one channel
over.** `LICENCE` (British spelling) was measured at 1 payout in 44 and is in the ladder;
`readme.md` pays 3 in 106 and was not. The repos it hides are not marginal —
`SafeExamBrowser/seb-server` is one, and this base maintains two dedicated instruments for
it (`seb-proctoring-validator`, `sebserver-mcp-gate`).

🔴 **Why `p603` did not simply patch line 155:** the harness denied executing shell code
from the cloned repository this pass, so the library could not be sourced or exercised, and
a patch this pass could not run is a patch this pass cannot verify. `p603probe.sh` here is
an **independent** implementation written against the four defects the library documents
(D1 branch resolution, D2 README licence link, D3 British spelling, D4 title-anchored
family). The ladder order in `readme_ladder.sh` is the measurement above, not a guess.

🟢 **The one-line fix for the next pass that can run it**, with the order priced here:

    for _rn in README.md readme.md README.rst Readme.md README README.txt docs/README.md; do ...

## Files

* `p603probe.sh` — branch (`ls-remote --symref`) + grant ladder + title-anchored family.
* `readme_ladder.sh` — the README spelling probe that produced the table above.
* `enrich.sh` — recency via treeless bare clone (committer date **and** tz offset, the
  channel `gate-offset-region` places regions with) + per-repo fabricated-path `404` control.

🔴 **No star counts anywhere in `p603`.** `api.github.com` and `github.com` HTML/atom both
return `403` through this session's proxy; the only channels open were `raw.githubusercontent.com`
and the git protocol. A star figure this pass could not read is a star figure it did not write.
