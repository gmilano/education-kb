# `p220` — `ACTION RG`'s instrument: the unit of a licence is the **FILE**

`ACTION RG` asked whether `P219-A`'s reorder — *read the ecosystem channel before asking the
maintainer* — generalises from the `4` derivative rows `QV` found to the `11`
`CLAIMED-IN-PROSE` rows, a population `3`× larger.

It fires on the count: **`4` of `11`** answer from an ecosystem channel. Its **conclusion is
refuted**. `CLAIMED-IN-PROSE` was never one state, and the `7` that do not answer are not a
reading failure — they are npm, PyPI, Go and HuggingFace rows whose channel was read, is
readable, and is **empty**.

## The prescription test

| ecosystem | file | licence field | verdict | rows p220 read |
|---|---|---|---|---|
| Moodle | `version.php` | 🟢 **mandatory** *(`@license` docblock tag)* | `PRESCRIBED-CHANNEL` | `3` of `3` answered |
| WordPress | `readme.txt` + plugin header | 🟢 **mandatory** | `PRESCRIBED-CHANNEL` | *(p219: `2` of `2`)* |
| ADL / SCORM | source-file header | 🟢 **mandatory** by convention | `PRESCRIBED-CHANNEL` | `1` of `1` answered — **and it contradicted the `README`** |
| npm | `package.json` | 🔴 **optional** | `PERMISSIVE-MANIFEST` | `0` of `3` |
| PyPI | `pyproject.toml` | 🔴 **optional** | `PERMISSIVE-MANIFEST` | `0` of `1` |
| HuggingFace | card front-matter | 🔴 optional, and `huggingface.co` is unreachable here | `PERMISSIVE-MANIFEST` | `0` of `1` |
| Go | `go.mod` | 🔴 **no such field exists** | `NO-CHANNEL` | `0` of `1` |
| *(none — a curated link list)* | — | — | `NO-CHANNEL` | `0` of `1` |

🔴 **So `ACTION PH`'s queue is NOT "mostly a reading job".** `4` of the `11` were a reading
job and are now read. The other `7` sit in ecosystems that never promised an answer, and a
human is the only route. That is the opposite of `RG`'s registered conclusion, on the same
count that fires its limb `1`.

🟢 **The rule worth keeping:** a channel is a **licence** channel only when the ecosystem
mandates the field *in a file that must exist*. Everything else is a place a licence is
*allowed* to be, which is not the same thing and must not be counted as coverage.

## The second half: a repository grant and a file grant can disagree

| row | repository says | the files that SHIP say | verdict |
|---|---|---|---|
| [`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) | `README` `## License`: **Apache-2.0**, quoted in full | `SCORM2004/APIWrapper.js` + `SCORM1.2/APIWrapper.js`: *"© 2000, 2011 Advanced Distributed Learning"*, a custom **non-disparagement** grant, **and CC BY-SA 3.0**. `SCORMToXAPIFunctions.js`: **nothing** | 🔴 `FILE-NARROWER` |
| [`microsoft/moodle-ai-assistant`](https://github.com/microsoft/moodle-ai-assistant) | root `LICENSE` + `README` badge: **MIT** | `local/aichat/version.php`: the Moodle GPL header and `@license … GNU GPL v3 or later` | 🔴 `FILE-NARROWER` |

🔴 **In both rows the thing a studio redistributes is the file, not the repository** — a
wrapper dropped into every SCO, a PHP file edited in place inside a Moodle tree. The
repository-level grant is the one that does not travel.

## The registry identity gate

`registry.npmjs.org` is a new working channel *(`200`, `ACTION PD`'s `16`th test)* and it
answers with `license: MIT` for the package name `canvas-lms-mcp`. 🔴 **That record's
`repository` is [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) —
not the shelf row [`CreveXTech/canvas-lms-mcp`](https://github.com/CreveXTech/canvas-lms-mcp)
that declares the same npm `name` and carries no `license` key.** Reading the channel
without `identity_ok()` would have written a stranger's MIT onto an ungranted row — the
inverse of the propagation failure this KB keeps measuring, and a worse one, because it
manufactures a grant instead of losing one. Same family as
[`p190-holder-package-layer`](../p190-holder-package-layer/README.md) and
[`p791-registry-id-provenance`](../p791-registry-id-provenance/README.md).

## Use

```python
from file_grant import prescription, identity_ok, file_vs_repo, verdict

prescription('npm')['verdict']           # -> 'PERMISSIVE-MANIFEST'
file_vs_repo('MIT', {'local/aichat/version.php': 'GPL-3.0-or-later'})
                                         # -> 'FILE-NARROWER'
verdict('npm', None, {}, npm_record, 'CreveXTech/canvas-lms-mcp')['registry']
                                         # -> 'IDENTITY-FAIL'
```

## What it does NOT claim

🔴 **It does not decide which grant governs in law.** When a repository says MIT and its
files say GPLv3, which one binds a downstream user is a question for counsel and the
copyright holder, not for a script. What the instrument does is refuse to report either as
settled, so the ambiguity reaches an SOW instead of a client's build.

🔴 **`PERMISSIVE-MANIFEST` is not an accusation.** An npm package with no `license` key is
npm working as designed. The instrument says the channel cannot answer, not that the author
did something wrong.

## Tests

```sh
cd compose/code/p220-file-level-grant && python3 -m unittest test_file_grant -v
```

`15` tests, all passing. Fixtures are verbatim readings taken on `2026-10-15`. **Three are
controls that must not fire:** a Moodle row whose `LICENSE` and `version.php` agree must come
back `AGREE`; the npm record *must* pass the identity gate for the owner it actually names;
and a missing `license` key in `package.json` must not be reported as a defect.
