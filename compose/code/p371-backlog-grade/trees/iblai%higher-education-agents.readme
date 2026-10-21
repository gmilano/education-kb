<div align="center">

<a href="https://ibl.ai"><img src="https://ibl.ai/images/iblai-logo.png" alt="ibl.ai" width="300"></a>

# Higher Education Agents

Drop-in [OpenClaw](https://github.com/iblai/iblai-claw-setup) / [NemoClaw](https://github.com/NVIDIA/NemoClaw) agent configuration for the [ibl.ai](https://ibl.ai) **Higher Education** solution segment — one Campus Assistant orchestrator plus 16 specialist subagents, packaged so a NemoClaw host can import the whole roster with zero conversion.

[![OpenClaw](https://img.shields.io/badge/OpenClaw-292929?logoColor=white)](https://github.com/iblai/iblai-claw-setup)
[![NemoClaw](https://img.shields.io/badge/NemoClaw-76B900?logo=nvidia&logoColor=white)](https://github.com/NVIDIA/NemoClaw)
[![ibl.ai Platform](https://img.shields.io/badge/ibl.ai_Platform-4A90D9?logoColor=white)](https://ibl.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

This directory is a complete, drop-in NemoClaw/OpenClaw configuration for the Higher Education solution segment. Copy its contents directly into `/sandbox/.openclaw/` on a NemoClaw sandbox to get a fully operational multi-agent campus AI system with zero additional conversion.

## What's Included

One parent agent that routes all incoming requests, plus 16 specialist subagents covering every major function in a higher education institution.

### Agent Roster

| Agent ID | Name | Role |
|---|---|---|
| `higher-education-assistant` | Campus Assistant | **Parent** — segment entry point; greets users, interprets intent, delegates to subagents via `sessions_spawn`, synthesizes results |
| `enrollment-agent` | Enrollment Advisor | Recruitment campaigns and admissions inquiries |
| `application-reader-agent` | Application Reader | Application scoring and transcript evaluation |
| `financial-aid-agent` | Financial Aid Advisor | FAFSA, aid eligibility, scholarship matching |
| `academic-advisor-agent` | Academic Advisor | Degree planning and course registration |
| `tutoring-agent` | Study Buddy | 24/7 learning support and exam prep grounded in course materials |
| `retention-agent` | Student Success Coach | Identifies at-risk students and runs timely interventions |
| `student-services-agent` | Student Life Guide | Housing, campus life, wellness support |
| `career-services-agent` | Career Coach | Resume building, interview prep, job and internship matching |
| `faculty-agent` | Faculty Assistant | Syllabus creation, lecture prep, assignments, grading |
| `research-agent` | Research Navigator | Literature searches, grant applications, IRB guidance |
| `alumni-agent` | Alumni Engagement Advisor | Alumni engagement, fundraising, events |
| `it-help-desk-agent` | IT Help Desk | Staff and student tech support |
| `prospective-student-agent` | Admissions Guide | 24/7 inquiries, program matching, campus visit scheduling |
| `yield-agent` | Yield Advisor | Personalized outreach to admitted candidates to boost commitment rates |
| `continuing-education-agent` | Continuing Education Advisor | Certificate programs and professional development for working professionals |
| `administrative-agent` | Administrative Services Guide | Policy questions, HR onboarding, compliance guidance |

## Directory Layout

```
higher-education/
├── README.md                          ← this file
├── openclaw.json                      ← gateway configuration (all 17 agents)
├── .config-hash                       ← sha256 of openclaw.json
├── .env.example                       ← OpenClaw daemon env file template (copy to ~/.openclaw/.env)
├── workspace/
│   └── .gitkeep                       ← shared writable workspace (empty at install)
├── skills/
│   ├── banner/SKILL.md                ← Ellucian Banner SIS
│   ├── blackbaud-raisers-edge/SKILL.md ← Blackbaud Raiser's Edge NXT
│   ├── canvas/SKILL.md                ← Instructure Canvas LMS
│   ├── civitas-learning/SKILL.md      ← Civitas Learning analytics
│   ├── eab-navigate/SKILL.md          ← EAB Navigate student success
│   ├── handshake/SKILL.md             ← Handshake career platform
│   ├── salesforce-education-cloud/SKILL.md ← Salesforce Education Cloud / NPSP
│   ├── servicenow/SKILL.md            ← ServiceNow ITSM
│   ├── slate/SKILL.md                 ← Technolutions Slate CRM
│   └── workday/SKILL.md               ← Workday HCM and Workday Student
└── agents/
    ├── higher-education-assistant/
    │   └── agent/
    │       ├── auth-profiles.json
    │       ├── IDENTITY.md
    │       ├── SOUL.md
    │       ├── TOOLS.md
    │       ├── AGENTS.md              ← routing table (parent only)
    │       ├── USER.md                ← optional: user/environment-specific context
    │       ├── BOOTSTRAP.md           ← optional: one-time first-run setup actions
    │       ├── HEARTBEAT.md           ← optional: periodic monitoring task checklist
    │       └── MEMORY.md              ← optional: seed long-term curated facts
    ├── enrollment-agent/agent/        ← same file set minus AGENTS.md; optional files as warranted
    ├── application-reader-agent/agent/
    ├── financial-aid-agent/agent/
    ├── academic-advisor-agent/agent/
    ├── tutoring-agent/agent/
    ├── retention-agent/agent/
    ├── student-services-agent/agent/
    ├── career-services-agent/agent/
    ├── faculty-agent/agent/
    ├── research-agent/agent/
    ├── alumni-agent/agent/
    ├── it-help-desk-agent/agent/
    ├── prospective-student-agent/agent/
    ├── yield-agent/agent/
    ├── continuing-education-agent/agent/
    └── administrative-agent/agent/
```

## Tool Skills

The `skills/` directory contains one subdirectory per third-party platform, each with a `SKILL.md` file. Each skill describes the platform, its data model, the specific API operations available to agents, and declares the required env vars in its frontmatter `metadata` field. Agents reference skills through their `TOOLS.md` file.

All skills draw credentials from `~/.openclaw/.env` on the daemon host. `.env.example` is the committed sample template — it contains non-functional placeholder values and documents every variable name and format expected by the skills.

| Skill | Description |
|---|---|
| `banner` | Ellucian Banner SIS — lets an agent query student academic records, registration, financial aid awards, and employee HR data via Banner REST APIs. |
| `blackbaud-raisers-edge` | Blackbaud Raiser's Edge NXT — lets an agent query alumni constituent records, giving history, pledge tracking, and wealth screening scores for advancement workflows. |
| `canvas` | Instructure Canvas LMS — lets an agent read and write course content, assignments, grades, and engagement analytics. |
| `civitas-learning` | Civitas Learning analytics platform — lets an agent retrieve student risk scores, graduation probability, course success predictions, and intervention outcome tracking. |
| `eab-navigate` | EAB Navigate student success platform — lets an agent manage early alerts, advising appointments, four-year plans, and at-risk cohort outreach. |
| `handshake` | Handshake career platform — lets an agent search jobs and internships, retrieve employer profiles, and surface career fair registrations for students. |
| `salesforce-education-cloud` | Salesforce Education Cloud and NPSP — lets an agent query and update enrollment CRM records, alumni giving history, campaign membership, and engagement scores. |
| `servicenow` | ServiceNow ITSM — lets an agent create, update, and resolve IT incidents, search the knowledge base, and check campus service status. |
| `slate` | Technolutions Slate CRM — lets an agent read and write prospect, applicant, and admitted-student records and trigger enrollment communication workflows. |
| `workday` | Workday HCM and Workday Student — lets an agent retrieve employee records, student financial aid awards, and initiate HR self-service workflows. |

## NemoClaw Import Instructions

1. **Copy this directory's contents** into `/sandbox/.openclaw/` on the NemoClaw sandbox:

   ```bash
   git clone https://github.com/iblai/higher-education-agents.git
cp -r higher-education-agents/. /sandbox/.openclaw/
   ```

2. **Set ownership** so the sandbox user can read all agent workspace files:

   ```bash
   chown -R sandbox:sandbox /sandbox/.openclaw/agents/
   ```

3. **Replace sample credentials** in every `auth-profiles.json`. Each file contains a clearly marked placeholder key. Replace with your actual Anthropic API key (and any other provider keys you add):

   ```bash
   find /sandbox/.openclaw/agents -name auth-profiles.json
   # Edit each file and replace the placeholder apiKey value
   ```

4. **Set up third-party platform credentials** by copying the sample template to `~/.openclaw/.env` and filling in real API keys for each integration your deployment uses:

   ```bash
   cp /sandbox/.openclaw/.env.example ~/.openclaw/.env
   # Edit ~/.openclaw/.env and replace every SAMPLE-replace-me-* value
   ```

   Leave any variables for platforms you are not using set to their placeholder values — skills only attempt connections when an agent explicitly invokes them.

5. **Recompute the config hash** after any edits to `openclaw.json`:

   ```bash
   cd /sandbox/.openclaw
   shasum -a 256 openclaw.json > .config-hash
   ```

6. **Reload the OpenClaw gateway** to pick up the new configuration:

   ```bash
   openclaw reload
   # or restart the gateway service per your deployment method
   ```

## Entry Point

The default agent — `higher-education-assistant` (Campus Assistant) — is the segment entry point. All incoming conversations route through it. It uses `sessions_spawn` to delegate to specialist subagents and synthesizes their responses before returning to the user. The routing logic is defined in `agents/higher-education-assistant/agent/AGENTS.md`.

## Notes

- Model selection and instance configuration for all agents live in `openclaw.json`. To change the model or session settings for a specific agent, update its object in `openclaw.json` and recompute `.config-hash`.
- The `workspace/` directory at `/sandbox/.openclaw/workspace/` is shared across all agents in a conversation thread. The parent agent uses it for multi-step, multi-agent coordination context.
- `auth-profiles.json` credentials are host-only and never exposed to model inference.

---

## License

Released under the [MIT License](LICENSE).
