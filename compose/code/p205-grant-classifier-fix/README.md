# p205 — title-anchored licence classification

Drop-in replacement for [`../p203-grant-blob-reader/classify.sh`](../p203-grant-blob-reader/classify.sh).

## Why

p203's `classify_grant()` tests the **whole licence body**, with the AGPL branch first. Three
licences name **other** licences inside their own text:

| licence | names another licence at | p203 says | truth |
|---|---|---|---|
| `GPL-3.0` | §13, "…the GNU Affero General Public License…" | `AGPL-3.0` | `GPL-3.0` |
| `MPL-2.0` | §1.12, "`Secondary License` means … the GNU Affero General Public License, Version 3.0" | `AGPL-3.0` | `MPL-2.0` |
| `ECL-2.0` | ¶1, "the Apache 2.0 license, modified…" | `UNRECOGNISED` | `ECL-2.0` |

Reproduced on `OptiKey/OptiKey`, `moodle/moodle` and `coqui-ai/TTS`. A true-AGPL control
(`frappe/lms`) still classifies correctly, so the defect is a **false positive for the AGPL**.

Published exposure when found: **0 rows** — the only classifier-era AGPL row
(`Lumieducation/Lumi`) is manifest-only. But 4 of pass 205's own OER rows were wrong before
re-adjudication, so the bug was live.

## The fix

**Anchor on the title LINE.** A licence names itself on a line of its own; §13 of the GPL is
prose. Classify on the first line that *is* a licence title (plus the two lines after it, which
carry the version), and fall back to a body-wide search only when that decides nothing.

A fixed 300-character *window* is not enough: `kaldi-asr/kaldi` prefixes its Apache text with
~1.5 kB of copyright-header prose. It is a fixture.

Also added: `ECL-2.0`, `NON-OSI-BSL` (Business Source License — source-available, converts to
Apache-2.0 at a change date), `CC-BY-NC`, `*-DEED` (the repo ships the human-readable *summary*,
not the instrument) and `TWO-SCOPE` (a file granting content and code under different
instruments cannot honestly return one token).

## Use

```bash
source classify.sh
classify_grant "$(curl -sS https://raw.githubusercontent.com/OWNER/REPO/HEAD/LICENSE)"
scope_headings "$body"   # >= 2 means two-scope (Carpentries shape)
```

`HEAD` is a valid `raw.githubusercontent.com` ref and resolves the default branch whatever it is
called — controlled on `opencast/opencast`, whose default branch is `develop`. No `ls-remote`
step is needed.

Note the **two-file** two-scope shape (`microsoft/autogen`: `LICENSE` is `CC-BY-4.0`,
`LICENSE-CODE` is `MIT`), which `scope_headings()` returns `0` on. Test for a second licence
*file* as well as for two headings.

## Test

```bash
./test_classify.sh    # 15/15, offline, against ./fixtures
```

Fixtures are real licence bodies captured 2026-10-14. The GPL/MPL fixtures are **full** bodies on
purpose — truncated to 3 kB they do not reach the Affero mention and the regression disappears.
