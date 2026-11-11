#### 🆕 p763 — two national databases with hard annual deadlines, and their entire public client estate is one AGPL repository with `2` stars

**Register: the education data warehouse and the statutory return.**

🟢 **India's UDISE+ is the largest statutory return on this register by learner count.** The Ministry of Education's Department of School Education and Literacy released the **UDISE+ Report 2025-26 on `2026-07-07`**. A letter dated `2026-07-14` sets **`2026-09-30`** as the last date to complete 2026-27 data entry (**secondary-sourced; not confirmed against `udiseplus.gov.in`**). A national UDISE+ conference was held **`2026-02-27` to `2026-02-28`** in Bhubaneswar and was specifically about **data integrity** for infrastructure, enrolment and teacher records — i.e. the register's core problem, named by the buyer. The collection feeds Samagra Shiksha planning and NEP 2020 benchmarking.

🟢 **Indonesia's PDDikti is the higher-education national database**, and it is the only APAC system on this register with any public client code at all.

| APAC supply, byte-read `2026-11-11` | Grant | Payload |
|---|---|---|
| [`andikadevs/pddikti`](https://github.com/andikadevs/pddikti) (`2★`, `main`, pushed `2026-11-07`) | **AGPL-3.0** | `34,523 B` / `0d96a4ff68ad` |
| [`teszerrakt/pddikti-scraper`](https://github.com/teszerrakt/pddikti-scraper) (`1★`, `main`) | 🔴 **no payload at `17` paths and no manifest declaration** — published as an absence, not as a licence state | — |
| [`hkopenai/hk-education-mcp-server`](https://github.com/hkopenai/hk-education-mcp-server) (`1★`, `main`, pushed `2026-10-02`) | MIT | `1,070 B` / `473af2606a25` |

🔴 **So APAC's two national-database clients are an AGPL-3.0 repository with `2` stars and an unlicensed scraper with `1`.** For a studio that must ship a proprietary deliverable, the AGPL-3.0 client is unusable as a component and the scraper cannot be used at all. **APAC has the register's largest demand and effectively no usable supply.**

🔴 **A region-vocabulary defect in the sources, recorded because this base's `region` field is a closed vocabulary.** The APAC search leg returned the **UAE's `25` generative-AI school prohibitions (February 2026)** and the **UK's January 2026 school AI safety standards** inside an APAC result set. Both are EMEA. Neither is filed here. 🔵 Secondary sources do not respect the five-value vocabulary and a pipeline that trusts their regional framing will mis-bucket findings (`T612`).

🔵 **Adoption context:** Times Higher Education reports patchy uptake across the region with limited connectivity as a barrier and virtual-tutor adoption at `30%` among those surveyed; `34,000` lead teachers are being trained through 2026. The World Bank's Global EdTech Policy Academy on AI ran in Seoul `2026-08-31` to `2026-09-04`. The Ipsos Education Monitor 2026 finds lower support for school AI bans across the Asian markets examined.
