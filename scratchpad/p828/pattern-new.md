## P68 — The heterogeneous-LMS student-record connector: one domain model, four vendor adapters (Global build, EMEA control anchor)

🟢 **The premise, and it is a measured one.** `T99` established that the open agent supply for
Brightspace, D2L and Blackboard exists at `147` repositories and was almost entirely unmapped
here, while `T100` established that the usable artefacts are **institution-bound** and carry the
authentication and pagination knowledge that is the expensive part of any LMS integration.
🔴 **No national or multi-campus education client runs one LMS.** A ministry, a university group
or a private HE operator typically runs two to four — and the usual response is four
point-integrations that drift.

🟢 **This recipe builds ONE domain model and mounts vendor adapters under it**, taking the
protocol knowledge from permissively-licensed, byte-read servers rather than rediscovering it.

### Components — all byte-read permissive on `2026-11-15`

| Layer | Component | Licence | Why this one |
|---|---|---|---|
| Orchestration | [`labsai/EDDI`](https://github.com/labsai/EDDI) | Apache-2.0, `394★` | Config-driven: a JSON definition becomes a running multi-agent service, 19+ providers, MCP/A2A and persistent state. Avoids writing an orchestration layer at all |
| Blackboard adapter | [`nitsuah/bb-mcp`](https://github.com/nitsuah/bb-mcp) | MIT | Wraps the **official Blackboard Learn REST API** and already carries **RBAC middleware** — the authorisation shape an institutional deployment needs |
| Blackboard fallback | [`UKplus8HRS/bb-mcp`](https://github.com/UKplus8HRS/bb-mcp) | MIT | **Playwright-driven**, configurable institutions + SSO. Use where the institution issues no REST credentials — which is the common case |
| D2L adapter | [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) | MIT, `67★` | The largest independent D2L server; explicitly *"works with any school"*, so it is the one written against the product rather than one campus |
| D2L (compiled) | [`micho911/brightspace-mcp`](https://github.com/micho911/brightspace-mcp) | MIT | Go — ship as a single binary where a campus will not host a Python runtime |
| Moodle adapter | [`G36maid/moodle-mcp`](https://github.com/G36maid/moodle-mcp) | MIT, `29★` | Operates Moodle broadly (courses, assignments, forums, grades, files-as-markdown) |
| SGA↔Moodle bridge (🇧🇷) | [`suap-ava-suite/djangoapp-integrador_ava`](https://github.com/suap-ava-suite/djangoapp-integrador_ava) | MIT | Where the client is Brazilian: joins SUAP/SIGAA/Q-Acadêmico to Moodle. 🔴 Declared development-use-only — read it as a specification, do not deploy it |
| Write control | [`simonseifert/merlin-mcp`](https://github.com/simonseifert/merlin-mcp) | MIT | Copy its **phone-approved send**: out-of-band human confirmation on every write |
| Auth control | [`heitorsDev/sigaa-ifsc-mcp`](https://github.com/heitorsDev/sigaa-ifsc-mcp) | MIT | Copy its **credential non-possession**: the human logs in, the service inherits the session; the service never holds the password |

### How to wire it

1. **Define the domain model first, from the intersection, not the union.** Course, enrolment,
   assessment item, due date, submission, grade, announcement. Every one of the four vendors has
   these; almost nothing else is common. 🔴 **Model the union and the adapters become the
   product.**
2. **Each adapter implements read-only first** and is accepted against the vendor's own
   documentation, not against the reference server — the reference server is where you learn the
   protocol, not what you certify against.
3. **The write path is a separate, later interface** and is gated by the two controls above:
   out-of-band human confirmation (`merlin-mcp`) and server-side role enforcement (`bb-mcp`'s
   RBAC). 🟢 **Per `T101` this is the default, not a hardening phase.**
4. **Mount the adapters in EDDI** as tool surfaces behind one conversational service; EDDI's
   persistent state carries the student context across vendors, which is the thing none of the
   single-LMS servers can do.
5. **Vendor the adapter code into the client's repository.** 🔴 `T100`: these are
   single-maintainer, `0–2★` repositories against portals that change without notice. The licence
   lets you fork; the risk profile requires you to.

### Compliance anchor — EMEA

🔴 **The write path is the regulated path.** Where the connector is used for **grading, steering
learning, admissions or exam monitoring**, it is an Annex III use under the EU AI Act. 🟢 **This
base already records the Digital Omnibus — `Regulation (EU) 2026/1744` — moving stand-alone
Annex III duties to `2027-12-02`, while the Article 50 transparency duties and the AI-literacy
duty are live now.** 🔵 **Practical reading for a 2026 engagement: the read-only connector ships
under transparency and literacy obligations today, and the write path is the deliverable to
scope against the `2027-12-02` date — which is a procurement argument, not a delay.**

### Shape of the engagement

🟢 **`8`–`10` weeks** for the domain model plus two adapters read-only; **`+4`–`6` weeks** per
further adapter; **`+4` weeks** for the gated write path. 🔵 **The reusable asset is the domain
model and the acceptance suite, not the adapters** — the adapters are the part that will be
rewritten when a vendor changes a portal.
