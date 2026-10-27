# `p487` — title-anchored GNU classifier + SHA-pinned licence reader

Two instruments, one of which exists because the other one broke inside this pass.

## `licread.sh` — closes `Gap 486-B`

`p486` recorded that a `sha256` taken at `main`/`master` is a measurement of whatever that
branch pointed at, at an unrecorded moment, and that uPortal's fingerprint did not survive one
hour. This reader resolves `HEAD` to a **commit SHA** with `git ls-remote --symref` first and
reads the payload **at that SHA**, so every fingerprint it emits is reproducible by a third party.

It also carries this base's two measured oracle facts:

- `curl -sI` is not used. It returns `403` for a real repository and a fabricated one alike
  (`p450`, re-measured this pass on `HKUDS/DeepTutor`).
- a `404` can arrive as a `200`-shaped 14-byte body. `d5558cd419c8` is this base's named
  **REFUSAL** fingerprint (`p256`/`p257`) and is rejected explicitly, because gating on
  `http_code` alone is not enough when the body is the thing being measured.

## `classify.sh` — the defect this pass found in its own first instrument

`licread.sh` v1 classified the GNU family by grepping the whole body, testing `gnu lesser`
before `gnu general public` — the ordering `p450` prescribed after it found that GPLv3's
closing paragraph recommends the LGPL.

**That ordering is itself a defect generator, and v1 published two wrong verdicts before a
control caught them.** A whole-body grep is unsound in three distinct directions:

| shape | mechanism | wrong verdict |
|---|---|---|
| `p450`, known | GPLv3's closing paragraph recommends the LGPL | `GPL-3.0` → `LGPL` |
| **`p487`, new** | GPL-2.0's **preamble** names the Library/Lesser GPL | `GPL-2.0` → `LGPL` |
| **`p487`, new** | GPL-3.0 **§13** is titled *"Use with the GNU Affero GPL"* | `GPL-3.0` → `AGPL` |

The third is the expensive one: it manufactures a **network-copyleft** verdict on a licence
that has no network clause.

`classify.sh` anchors on the **title block** instead — `p455`'s anchor, the one region of a
payload a preamble cannot reach — and falls back to the body only for families whose title
line is uninformative. Run it against `ieducar.gpl2 rosario.gpl2 lumen.gpl3 freelingo.agpl3`
and it prints the old rule's verdict beside the new one; two `DISAGREE`, two `agree`.

The two `agree` rows are the controls that matter: a classifier that called everything
`GPL-2.0` would also have "fixed" `i-educar`, and `freelingo` is the row that proves the new
reader can still find a genuine AGPL.
