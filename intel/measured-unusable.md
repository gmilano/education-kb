---
industry: education
region: Global
updated: 2026-10-30
---

# Measured / Unusable — the ungranted-domestic-supply register

**Opened at `p544` · 2026-10-30, closing [`Gap 543-D`](../agents/trending.md#-gap-543-a--gap-543-f-registered).**

🔵 **Why this file exists.** An artefact can be **real, live, education-specific
and still unusable**, because it carries **no grant at all**. Such an artefact is
neither a shelf row (nothing licenses us to build on it) nor a reject (it is not
mis-described, mis-licensed or off-sector — it is *correctly* described and
*genuinely* absent a licence). `Gap 543-D` was registered because the class had
no published home: three Vietnamese agents had been found, filed only in a
trending entry, and were on course to be **re-discovered a fourth time**.

🔴 **The rule this register encodes:** *supply is not the same as usable supply.*
A region can have domestic AI-in-education engineering and offer Globant nothing
to build on. Counting artefacts without reading grants overstates every regional
supply claim on this base.

## The register

| Address | Origin (region) | What it is | Grant, probed at the resolved default ref | Head read at `p544` |
|---|---|---|---|---|
| [`MaiQuangPhuoc/edu_agents`](https://github.com/MaiQuangPhuoc/edu_agents) | 🟢 **APAC (Vietnam)** — *stated*: grade-10 **GDPT 2018** national curriculum | Grade-10 curriculum agent. 🟢 **Architecturally the most interesting artefact four language legs returned:** it chooses a **deterministic pipeline over ReAct** for the education domain and **bounds the LLM to the textbook** to suppress invention. | 🔴 **`UNRESOLVED`** — 10 filenames at `main`, plus sidebar and README at `p543` | `main` · `03e43219c66a` |
| [`dungptt-dng/smart-ict-classroom`](https://github.com/dungptt-dng/smart-ict-classroom) | 🟢 **APAC (Vietnam)** — *stated*: **Vietnam AI in Education Pioneer Award 2026** entry | A computer lab with **fewer machines than groups**: fair turn scheduling and four rotating in-group roles. A constraint a LATAM or APAC public-school engagement meets constantly and no shelf row addresses. | 🔴 **`UNRESOLVED`** — as above | `main` · `a9c56b3b7496` |
| [`minhdevtry/AI-Teacher-Assistant-Agent`](https://github.com/minhdevtry/AI-Teacher-Assistant-Agent) | 🟢 **APAC (Vietnam)** — *stated*: Vietnamese, **Zalo** Bot | *ZaloAgent* — class management over Zalo, the domestic messenger, with fee capture by text **and image OCR**. | 🔴 **`UNRESOLVED`** — as above | `main` · `f3bcc636da1d` |
| 🆕 [`fairyofmiracle/edu_course_agent`](https://github.com/fairyofmiracle/edu_course_agent) | 🟡 **EMEA (Russia)** — *inferred, and the inference is named*: README and UI are **Russian**, the LLM gateways are **Cloud.ru** and **GigaSchool** (both Russian services), and the output is Russian **ДПО** professional-development paperwork. The page itself states no country. | A methodologist's workstation: builds a professional-development programme from an **ACR template**, and exports **DOCX / PPTX / JSON**. 🟢 **It refuses to invent the order number (`наказ`/приказ) and the labour-function code** — the artefact's whole value is that two legally-load-bearing identifiers are *not* generated. 196 commits, **0★, 0 forks**. | 🔴 **`UNRESOLVED`** — 10 filenames at `main`; sidebar shows no licence and does not say "no licence" | `main` · `c425a51c2512` |

🔴 **Four artefacts, two languages of origin, zero grants.** The Vietnamese trio
came off `p543`'s `vi` leg; the Russian row came off `p544`'s **`uk`** leg. The
class is now **stable across two unrelated origins**, which is what makes it a
class rather than a Vietnamese peculiarity.

## 🟢 What a studio may still do with a row here

🔵 Nothing in this register may be **vendored, forked or shipped** — there is no
licence to do so. What it is legitimately good for:

1. **Read the architecture, write your own.** `MaiQuangPhuoc/edu_agents`'s
   deterministic-pipeline-over-ReAct choice and textbook-bounded generation are
   *design* findings. A design is not a derivative work.
2. **Name the requirement.** `smart-ict-classroom`'s fewer-machines-than-groups
   scheduling is a **real constraint of public-school delivery** that no granted
   shelf row covers.
3. **Ask.** 🟢 The cheapest action available: open an issue requesting an
   explicit licence. `ACTION p417-A` already prescribes this for a LATAM address;
   the same move applies to all four here, and a single `LICENSE` commit would
   move a row onto the shelf.

🔴 **What must not happen:** a row here being quoted as regional "supply" in a
market slide. It is supply that cannot be used, and the register exists so the
distinction survives the next pass.
