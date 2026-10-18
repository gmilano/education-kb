---
industry: education
region: Global
updated: 2026-10-08
---

# `P798` — the refusing layer testifies, so a refusal stops being an inference

Artefacts and suite of the **sixty-fifth pass (2026-10-08)**. 🟢 **9/9 green under `python3 -I`.**

## What changed against `P797`

🟢 Pass 64 closed `Gap 293` by a **control**: Wikipedia — not a policy host, not a regulator, not
down — refused identically to four policy hosts, so the variable had to be the channel's allowlist.
🔵 That was sound and it was an **inference from a pattern**.

🆕 **This pass read the refusing layer's own ledger.** `$HTTPS_PROXY/__agentproxy/status` returns
`recentRelayFailures`, and for each of the four hosts probed it carries a **host, a timestamp and a
mechanism**:

```
connect_rejected · gateway answered 403 to CONNECT (policy denial or upstream failure)
en.wikipedia.org:443 · digital-strategy.ec.europa.eu:443
www.iesalc.unesco.org:443 · www.multistate.us:443        all at 2026-10-08T19:52:0?Z
```

🟢 **So `EGRESS_DENIED (allowlist)` is now a reading of a first-party record, not a deduction.**

## The trap the suite guards

🔴 `curl` writes **`000`** for a proxy CONNECT denial **and** for a genuinely unreachable host.
🔵 Those are not the same fact and they license **opposite** next actions — one says *"the source is
fine, this environment may not read it"*, the other says *"retry, or doubt the source."*
🟢 `verdict()` therefore refuses to promote an **unlogged** `000` to a policy denial: it returns
`UNDETERMINED (transport)`. That negative control is `test_an_unlogged_000_is_NOT_promoted_to_a_policy_denial`.

## 🔴 The correction this pass owes its own oracle map

🟢 `pypi` and `npm` answer **200/404** cleanly, and this KB has leaned on that as calibration.
🔴 **They are in the proxy's `noProxy` list** — `pypi.org`, `files.pythonhosted.org`,
`registry.npmjs.org`, `jsr.io`, `index.crates.io`, `proxy.golang.org` — **so they never traverse the
gateway that refused the four policy hosts.**

🔵 **Two instruments, two network paths.** A healthy registry pair says nothing about how broad the
allowlist is, and a map that treats registry health as general reachability over-reads every datum
it takes from a registry. `TheOracleMapIsTwoDifferentNetworks` asserts both halves at once, because
it is their **co-occurrence** that proves neither predicts the other.

## 🔴 Still not measured

🔴 **The allowlist is not enumerated.** `P744` holds: four of four denied is **not a rate**, and
`noProxy` is a **bypass** list, not the allowlist. Nothing here says which hosts would be allowed.

---

## 🔴 `P294` (pass 294, 2026-10-18) — THE NEGATIVE CONTROL THIS FILE NEVER RAN

🟢 **22/22 green under `python3 -I`** (was 9/9; `p294` adds 13).

`P798`'s negative control is `example.invalid`, a host it **asserted** was absent from the ledger
rather than one it probed. `p294` probed one: **`this-host-does-not-exist-p294.example`**, an
invented name with no DNS record anywhere.

🔴 **It is IN the ledger**, with the byte-identical mechanism the seven real hosts got —
`connect_rejected` · `gateway answered 403 to CONNECT`. The gateway refuses the CONNECT
**before any name resolution**, so a ledger entry is written for a host that cannot exist.

| what `P798` said | what `p294` measured |
|---|---|
| an unlogged `000` must not be promoted to a policy denial | 🟢 **still true, and now known to be unreachable** — every HTTPS host probed through the gateway is logged, so `verdict()`'s `UNDETERMINED` arm never runs |
| a ledger hit says *"the source is fine, this environment may not read it"* | 🔴 **REFUTED.** The invented host earns the same hit. It says nothing about the source |
| `EGRESS_DENIED (allowlist)` as a verdict | 🟢 **kept, unchanged** — as a statement about the **channel** it is right, for the invented host too |

🟢 **The repair is a SECOND verdict, not a new folder.** `existence_verdict()` is a separate
function with a closed two-token vocabulary, so a channel reading can never be spent as an
existence reading: `EXISTENCE-CONFIRMED (payload read)` is available **only** from a payload
actually read on a channel that was not refused, and `EXISTENCE-UNMEASURED (channel refused)` is
everything else.

🔵 **The case that shows why it matters.** `github.com` answers **`403`** to curl here. `p294`
nonetheless read **five** `LICENSE` blobs at pins through `raw.githubusercontent.com`. The refusal
was never evidence about those repositories — and the mandated instruction to *"verify every URL
with `curl -sI`"* cannot be satisfied on this channel at all, because a real URL and an invented
one return the same `000`.

🔴 **And one trap this pass set for itself and caught.** The first draft of `existence_verdict()`
branched on `host`/`transport_code` with **identical tokens in both arms** — `p293`'s `C36` trap
(`... or True`) arriving one pass later, a condition written from the author's intent rather than
from the value. Nothing could make it fail. The branch is gone;
`test_the_verdict_is_INVARIANT_under_host_and_code` now asserts its absence across 4 hosts × 4
codes × 3 ledgers.

🔴 **What `p294` did NOT measure:** a name resolution **off** the proxy path, which is the one
experiment that would separate *absent* from *blocked*. `test_a_DNS_only_probe_was_not_run` says
so rather than implying the question is closed.
