# `p144-librus-contract-count` — `ACTION DR`

> Re-measure `librus-mcp`'s shipped surface by a second, independent method, because
> `P143-C` means one method already got it wrong twice.
> 🔴 *Refuted if the independent count is not 35.*

## Verdict: 🟢 **DISCHARGED, falsifier SILENT — 35 confirmed, and two further figures with it**

🟢 **The independent count is 35.** 🟢 **And the repository's own `MCP_CONTRACT.md` states the
same number in prose, together with two others this KB did not hold:**

> *"All **31** default tools (including notifications and attachments) have typed outputs.
> Enabling sending gives **35** tools; disabling notifications and attachments leaves **27**."*

| surface | tools | composition | contract says |
|---|---|---|---|
| all features | 🟢 **35** | every module registered | 🟢 **35** |
| **default** | 🟢 **31** | ungated 27 + default-on gated 4 | 🟢 **31** |
| minimal | 🟢 **27** | ungated only | 🟢 **27** |

🔵 **Reproducing all three figures is much stronger than reproducing the one under test.** The
method shares no code with the AST instrument: it counts `server.tool(` sites per shipped
module, reads which modules sit behind a `config.features.*` test, and reads those flags'
declared defaults out of `config.py`.

| module | sites | gated by | default |
|---|---|---|---|
| `read_tools` | 12 | — | — |
| `message_tools` | 8 | — | — |
| `server` | 5 | — | — |
| `send_tools` | 4 | `send_message` | 🔴 **False** |
| `notification_tools` | 3 | `notifications` | 🟢 True |
| `school_history_tools` | 2 | — | — |
| `attachment_tools` | 1 | `attachments` | 🟢 True |

## 🔴 The number this shelf should publish is 31, not 35

🔴 **`send_message` defaults to `False`.** 35 is the *maximum* surface, reachable only when an
operator turns sending on; the shipped default is **31**, and 4 of the 35 are write tools that
do not exist until someone enables them. 🔵 **For a delivery conversation the default is the
relevant figure, and the gap between them is the write surface** — which is exactly the thing
a school's procurement will ask about.

## 🆕 `T38` — a lexical gate detector cannot see a cross-module gate

🔴 **`surface_gate2.py` reports `gated=0` for this repository, which has three real feature
gates.** The gates are in `server.py`:

```python
if config.features.send_message:
    register_send_tools(server)
```

…while the 4 registration sites they control are in `send_tools.py`. 🔴 **The gate and the
sites it gates are in different files**, so an instrument that looks for an enclosing `if`
around a registration site finds nothing. 🔵 **`T28`'s `GATED` category is therefore a floor,
not a measurement**, and every `gated=0` on this shelf means *"no gate in the same file"*.

## Run

```bash
python3 -I module_surface.py <librus-mcp-checkout>
```
