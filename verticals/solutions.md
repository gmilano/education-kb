---
industry: education
region: Global
updated: 2026-10-31
---

# Vertical education platforms (customisable with AI on top)

Real, deployed systems that run an institution's operations — the education
equivalent of Odoo for ERP. These are the systems a client already has, and the
systems an AI layer gets attached to. All rows verified first-hand on the
repository page, 2026-10-31.

## Education ERP / Student Information Systems

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| Frappe LMS | [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | 3,400 | APAC | "Easy to use, 100% open source LMS." Built on the Frappe framework, so it inherits Frappe's ERP primitives. India. |
| OpenEduCat | [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 902 | APAC | "Comprehensive Open Source ERP for Educational Institutes" — admissions, students, faculty, courses, exams, library, fees. **LGPL-3.0, not MIT/Apache**: the library may be linked from closed applications, but modifications to it stay open. OpenEduCat's own website describes Odoo as its underlying ERP framework; the GitHub page never mentions Odoo. India. |
| i-educar | [portabilis/i-educar](https://github.com/portabilis/i-educar) | GPL-2.0 | 722 | LATAM | *"Lançando o maior software livre de educação do Brasil!"* School management for Brazilian municipal education secretariats (*Secretarias de Educação*) and public schools, nationwide. **The reference LATAM public-sector education platform** and the most important row on this page for a Brazilian government engagement. |
| Frappe Education | [frappe/education](https://github.com/frappe/education) | **GPL-3.0** (resolved) | 687 | APAC | "Open source education / school management system." **Licence resolved on the second pass of 2026-10-31:** the repo's own `license.txt` on `master` reads `License: GNU GPL V3`. The first pass left this unknown because the sidebar does not name it and advised reading the file — that has now been done. Note it is **GPL-3.0, not AGPL-3.0** like Frappe's other projects, and not LGPL like its OpenEduCat neighbour. Copyleft either way: attach, do not fork. India. |
| openSIS Classic | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | **GPL-2.0** (pinned) | 347 | North America | Web-based PHP/MySQL Student Information System for running one or several institutions. OS4ED (US). **Version pinned on the second pass of 2026-10-31:** the README points to `docs/License.txt`, which is **GPL version 2, June 1991** — *not* GPL-3.0. The distinction is load-bearing: GPL-2.0 has no patent grant and is incompatible with GPL-3.0-only code, so a component mixing this with a GPL-3.0-only library cannot be redistributed. Default branch is `master`; there is no `main`. |
| Odoo | [odoo/odoo](https://github.com/odoo/odoo) | **LGPL-3.0** (file, not sidebar) | 55,400 | EMEA | "Odoo. Open Source Apps To Grow Your Business." The canonical open-source ERP, and the comparison point this KB is measured against. **Verified on the second pass of 2026-10-31**, closing a gap the first pass declared: the sidebar names **no licence**, but `LICENSE` on the default branch (`20.0`) states *"Odoo is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3)"*. **LGPL-3.0, not Apache/MIT** — so a closed application may *link* it, but modifications to Odoo itself stay open. This is what [OpenEduCat](https://github.com/openeducat/openeducat_erp) claims as its upstream, and it explains OpenEduCat's own LGPL-3.0: it inherits it. Odoo SA is Belgian; the repository page does not state a location. |

## Learning platforms used as the vertical system

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | APAC | The default institutional LMS worldwide; vast plugin ecosystem is the customisation surface. Perth, Australia. |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | EMEA | LMS built around ease of use and accessibility; notable francophone and LATAM deployments. |
| OpenOlat | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 (README badge; sidebar unnamed) | 449 | EMEA | "Learning Management System OpenOlat," developed and maintained by **frentix GmbH, Switzerland**. Notable as a **permissively licensed institutional LMS** — rare in this category, and the one here a commercial derivative could be built from. |

## Adjacent institutional systems (added second pass, 2026-10-31)

Systems that are not learning platforms but are always in the estate, and are
usually where an AI search or discovery agent is actually pointed. Licences read
from the licence file, not the sidebar.

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| DSpace | [DSpace/DSpace](https://github.com/DSpace/DSpace) | **BSD-3-Clause** | 1,100 | North America | The institutional repository — theses, datasets, faculty output, grey literature. **The only permissively licensed platform of record in this entire KB.** Java; LYRASIS (US non-profit). See [`../repos/foundations.md`](../repos/foundations.md) for why this is the licence exception that matters. |
| Koha | [Koha-Community/Koha](https://github.com/Koha-Community/Koha) | GPL-3.0 (or later) | 597 | Global | Integrated library system (ILS) — catalogue, circulation, acquisitions. Commonly paired with the LMS and the repository. Contributions go through the project's **own bug tracker, not GitHub issues**. |

## How to read this page

**The operations layer is copyleft almost without exception.** Of the eight
platforms above, exactly one (OpenOlat, Apache-2.0) is permissive, and one more
(OpenEduCat, LGPL-3.0) permits linking from closed code. The AI-on-top strategy
is therefore not a matter of taste — it is forced by licensing:

1. **Do not fork the platform of record.** Under GPL/AGPL the derivative must be
   released; under AGPL that triggers on network use, which is how these systems
   are always deployed.
2. **Attach across a standard boundary instead** — LTI 1.3 via `ltijs`, LMS data
   via MCP, telemetry via xAPI into an LRS. All permissive. See
   [`../repos/foundations.md`](../repos/foundations.md).
3. **Where a permissive substrate is genuinely required**, OpenOlat (Apache-2.0)
   is the only institutional LMS on this page that supports it.

## Declared gaps

- **No MIT- or Apache-licensed education ERP/CRM comparison exists.** The
  prescribed search `open source platform education ERP CRM MIT Apache` returned
  almost entirely OpenEduCat's own marketing glossary — vendor-supplied, and it
  confirms OpenEduCat is LGPL rather than MIT or Apache. No independent
  comparison of permissively licensed education ERPs was found.
- ~~**Odoo itself was not re-verified this run**~~ — **closed on the second
  pass of 2026-10-31.** Odoo is now a verified row above: **LGPL-3.0**, 55.4k★,
  licence read from the file because the sidebar names none. It also explains
  OpenEduCat's LGPL-3.0 by inheritance.
- **Adjacent systems named by vendor sources:** **Koha** (library) and **DSpace**
  (institutional repository) were **verified on the second pass** and now have
  rows above — DSpace is BSD-3-Clause, Koha is GPL-3.0. **Still unverified:**
  Nextcloud (files) and Jitsi (conferencing). Real systems, commonly paired with
  the above, but outside what has been checked.
- **Two licence defects found by reading files instead of sidebars**, and both
  were invisible to the first pass: `frappe/education` is GPL-3.0 (was recorded
  unknown) and `OS4ED/openSIS-Classic` is GPL-**2.0** specifically (was recorded
  as unversioned "GPL"). The method matters more than either finding: a sidebar
  that names no licence is not the same as a repo that has no licence, and only
  fetching the file distinguishes them.
- **No LATAM education ERP outside Brazil** surfaced this run. i-educar is the
  single LATAM row, and it is Brazil-specific.
