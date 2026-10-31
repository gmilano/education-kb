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
| Frappe Education | [frappe/education](https://github.com/frappe/education) | Not named on repo page — confirm before use | 687 | APAC | "Open source education / school management system." The sidebar links a License section but the page text does not name the licence. Frappe's other projects are AGPL-3.0; **do not assume** — read the LICENSE file before committing to it. India. |
| openSIS Classic | [OS4ED/openSIS-Classic](https://github.com/OS4ED/openSIS-Classic) | GPL (per README; not in sidebar) | 347 | North America | Web-based PHP/MySQL Student Information System for running one or several institutions. OS4ED (US). |

## Learning platforms used as the vertical system

| Platform | Repo | Licence | ★ | Region | What it runs |
| --- | --- | --- | --: | --- | --- |
| Moodle | [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | 7,600 | APAC | The default institutional LMS worldwide; vast plugin ecosystem is the customisation surface. Perth, Australia. |
| Chamilo | [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | EMEA | LMS built around ease of use and accessibility; notable francophone and LATAM deployments. |
| OpenOlat | [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 (README badge; sidebar unnamed) | 449 | EMEA | "Learning Management System OpenOlat," developed and maintained by **frentix GmbH, Switzerland**. Notable as a **permissively licensed institutional LMS** — rare in this category, and the one here a commercial derivative could be built from. |

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
- **Odoo itself was not re-verified this run**, so it has no row despite being
  the canonical ERP example; it appears only as OpenEduCat's claimed upstream.
- **Adjacent systems named by vendor sources but not verified here:** Koha
  (library), DSpace (institutional repository), Nextcloud (files), Jitsi
  (conferencing). Real systems, commonly paired with the above, but outside what
  this run verified.
- **No LATAM education ERP outside Brazil** surfaced this run. i-educar is the
  single LATAM row, and it is Brazil-specific.
