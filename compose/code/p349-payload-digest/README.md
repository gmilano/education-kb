---
industry: education
region: Global
updated: 2026-10-20
---

# `p349-payload-digest` — `ACTION ZZ-ad`: the third identity question

```sh
./payload_digest.sh probes.2026-10-20.tsv      # slug <TAB> path, pinned and hashed
python3 -I group_digests.py result.2026-10-20.tsv
python3 -I test_payload_digest.py              # 7 controls
```

Committed run: [`payload-digest`](../../../evidence/payload-digest.2026-10-20-p349.tsv).

| identity question | instrument | the k12 pair | the wallet pair |
|---|---|---|---|
| same ADDRESS, case-folded? | `gate-fold-identity` (p348) | 🔴 blind | 🔴 blind |
| same HEAD? | `gate-alias-canonical` (p349) · `gate-identity-online` (p283) | 🔴 blind — different HEADs | 🟢 catches |
| same PAYLOAD? | 🟢 **this** | 🟢 catches | 🟢 catches |

🔵 **Namespace note, because this is the first pass where the two collide.** This directory is named for **pass 349**. `compose/code/p349-star-resolution-band/` is named for **finding `P349`** (pass 111's star-resolution band). The `p<N>-` prefix has carried both meanings on this base for a long time; it is written down here so a successor reading `make gate-alias-canonical` does not go looking for a star channel.

## What the committed run says

* `anthropics/k12-teacher-skills` @ `31fd6dbb0c07` and `learning-commons-org/agent-skills`
  @ `8b0599c24469` ship the **same 8 666-byte `SKILL.md`, `152e3272fbd108fe…`**.
* 🟡 **Their READMEs are NOT the same payload** (2 280 B vs 6 441 B). So p348's reading —
  *one pack, two distributions* — is now measured on both halves, and the thing to pick
  on is the MCP server one of them adds, not the skills.
* `learner-credential-wallet`'s README is one digest `d22f8b56af465250` at one HEAD read
  through either address: the alias class, re-derived for free.

## 🔴 A 404 is a path assumption, not an absent payload

This pass's own probe list asked both presidio addresses for `README.md` and got **404 at
the pin**. The file is `README.MD`. 🟢 The instrument refused to call it anything but
`NO-PAYLOAD(404)`, which is the only reason the 404 was read as the case axis (`p347`,
on `LICENSE`) reaching a second surface rather than as an absence. `C4` keeps absent
payloads out of the digest groups: two files that are both missing are not one payload.
