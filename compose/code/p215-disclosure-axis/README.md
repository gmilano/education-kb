# P215 — The DISCLOSURE axis, measured

## Why this exists

Pass 72 (trend **566**) found that terms-of-use disclosure has started travelling as a **file in
the repo**, and called it *«an axis of selection that neither the licence nor the write gate
shows»*. It named the axis and did **not** sweep it. This is the sweep.

The axis answers one question: **what does the connector DECLARE about the contractual plane of
the system it talks to?** Not what it does with the credential — that is a different and much
weaker claim — but whether the client can decide *informed*.

## The classes

| | Class | Requires |
|---|---|---|
| **D1** | `DISCLOSURE-WITH-STATUTE-AND-TOU` | ToU cited + the admission that the provider **may treat the channel as a violation** + a **named statute** |
| **D2+** | `DISCLOSURE-OF-SCOPE` | D2, plus an explicit statement of **what it does not touch** |
| **D2** | `DISCLOSURE-OF-NON-AFFILIATION` | unofficial / no connection to the **named** provider |
| **D3** | `DISCLOSURE-OF-HANDLING-ONLY` | says what it does with credential/data, **silent on the contractual plane** |
| **D4** | `NO-DISCLOSURE` | none of the above |

`D1` is **conjunctive on purpose**: naming FERPA in a feature list is not an expedient.
`D3` is the trap the instrument exists to catch — *«your password never leaves your machine»*
reads reassuring, answers a question nobody asked, and stays silent on the one the client's
legal review will ask. It classifies **low**, by design.

## Run

```
curl -s https://raw.githubusercontent.com/<owner>/<repo>/HEAD/README.md \
  | python3 classify_disclosure.py <owner>/<repo>
python3 -m unittest test_classify -v     # 16 tests, 3 of them negative controls
```

`classify()` is pure: no IO, no network, deterministic.

## 🔴 The instrument's own defect, published with the result

The **v1** classifier was written in English, and it silently **under-read every non-English
repo in the inventory**. Three verdicts flipped once that was fixed:

| slug | v1 | v2 | what v1 missed |
|---|---|---|---|
| `kohlsalem/schulmanager-mcp` | 🔴 D4 | 🟢 **D2** | German says **`inoffiziell`**, not *«nicht offiziell»*; and *«keine Verbindung zu»* |
| `zaikaman/SGU-Academic-MCP` | 🔴 D4 | 🟢 **D3** | Vietnamese *«Xử lý cục bộ»* / *«Không lưu trữ tập trung»* |
| `sharziki/purdue-mcp` | ⚠️ D2 | 🟢 **D2+** | the scope phrasing *«It **never touches** a student account…»* |

**This is the same SHAPE of defect as P206** (the payload channel being case-sensitive): an
instrument's blind spot manufacturing **false absences** — and manufacturing them precisely in
the regions this KB exists to serve. **Two of the three flips were EMEA and APAC pieces, and
both flipped upward.** `result-v1-englishonly.NEGATIVE-CONTROL-2026-10-03.tsv` is kept as the
control; `test_classify.py::TestNonEnglishRecall` locks the fix so the regression cannot return
quietly.

⚠️ **The bound, stated:** recall is now fixed for **English, German, Portuguese and Vietnamese**.
It is **unmeasured** for Spanish, French, Indonesian, Hindi, Chinese, Japanese and Korean — so a
`D4` on a repo written in those languages is **conditioned**, exactly as P206 conditioned every
`NO-CESSION` verdict of this base. Not wrong: **not closed.**

## The result (2026-10-03, 15 pieces)

`result.2026-10-03.tsv` — D1: **1** · D2+: **2** · D2: **2** · D3: **4** · D4: **6**.

🔴 **The finding the sweep produces:** the best-disclosed piece of the inventory
(`infinitecampus-mcp`, the only **D1**) **has no write gate to close**, and the best-gated piece
(`attendai`, rung **1** of P207) discloses **handling and scope only — nothing contractual**, and
never touches a real institution's portal. 🟢 **Disclosure does not track the other two axes**
— the third anti-correlation this base has measured between two quality axes of a connector.

⚠️ **A caveat on the denominator:** `motiolabs-space/open-academic` scores `D4` and the score is
**not meaningful** — it is a platform the institution runs on its own data, not a connector
against a third party's system, so there is no contractual plane to disclose. **The axis applies
to connectors.** It is listed for completeness and must not be read as a defect.
