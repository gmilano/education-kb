---
industry: education
region: Global
updated: 2026-11-17
---

# Licence request draft — `blamb/lti-tutor`

**Drafted by `p874`, 2026-11-17.** **Status: 🔴 never sent** — see the ledger in
`intel/licence-requests/README.md`. This session's GitHub authorisation covers `gmilano/*` only, so
opening an issue on a third-party repository is outside its scope. Recorded as a scope limit, not
logged as a failure (the `T879-bis` rule).

## Why this is the highest-value missing grant in this KB

| Fact | Value |
|---|---|
| Address | https://github.com/blamb/lti-tutor |
| Resolved default branch | `main` (via `git ls-remote --symref`) |
| Licence | 🔴 **No licence file found** — `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE` all absent on `main` |
| What it is | An **LTI 1.3 / LTI Advantage** tool for Moodle and other Advantage platforms, with AI tutoring and optional completion passback via **AGS** (Assignment and Grade Services) |

🔴 **It is the only address this KB has ever resolved that combines LTI 1.3 with AI tutoring.**
That matters because this KB's central strategic finding is that the education platform layer is
overwhelmingly copyleft (Moodle GPL-3.0, Open edX and Canvas AGPL-3.0), so the workable pattern is
**not** forking a platform but attaching permissive AI services over the **LTI 1.3** seam. This
repository is the exact shape of that seam — and it carries no grant, so it cannot be used,
forked, or shipped.

For contrast, the nearest usable alternatives and why they do not substitute:

- `Cvmcosta/ltijs` (Apache-2.0) — excellent LTI 1.3 **transport**, but no tutoring.
- `moocupv/lti-ai-grader` (Apache-2.0) — real AI grading tested against Open edX and Moodle, but
  **LTI 1.1** (OAuth 1.0a, deprecated generation), and grading rather than tutoring.
- `CAHLR/OATutor` (MIT) — tutoring with LTI middleware, but not a 1.3/Advantage tool.

## The ask, kept narrow

A permissive licence (**MIT** or **Apache-2.0**) on the repository as it stands. No change of
maintainership, no contribution commitment, no relicensing of anything else.

## Draft message

> **Subject: Would you consider adding a licence to `lti-tutor`?**
>
> Hello — thank you for publishing `lti-tutor`. While surveying open-source education AI tooling we
> found it is, as far as we can establish, the only public repository that combines an **LTI 1.3 /
> Advantage** tool with AI tutoring and AGS completion passback. That combination is unusually
> useful: most open-source LMS platforms are GPL or AGPL, so attaching a service over LTI 1.3 is
> the main way to add AI to an institutional deployment without forking the platform.
>
> At the moment the repository has no `LICENSE` file, which under default copyright means others
> cannot legally use, modify or redistribute it — so the work is unlikely to be built on even by
> people who would like to.
>
> Would you consider adding a permissive licence such as **MIT** or **Apache-2.0**? GitHub can add
> one in a couple of clicks via *Add file → Create new file → `LICENSE`*, which offers a template
> picker. If you would prefer copyleft, **AGPL-3.0** would still be a large improvement over no
> licence for self-hosted institutional use.
>
> Either way, thank you for making the work public. Happy to help with the mechanics if useful.

## Acceptance test for a later pass

Re-read `https://raw.githubusercontent.com/blamb/lti-tutor/main/LICENSE` (and the `.md`/`.txt`
variants). A `200` with identifiable licence bytes discharges this request; a `404` means it still
stands. **Do not re-draft** — update the ledger row instead.
