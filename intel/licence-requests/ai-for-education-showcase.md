---
industry: education
region: APAC
updated: 2026-11-12
---

# Licence request — `mingxuanyan07-lgtm/ai-for-education-showcase`

- **Repository:** https://github.com/mingxuanyan07-lgtm/ai-for-education-showcase
- **Measured 2026-11-12:** `189` files in tree; `2` licence paths, **both vendored** (`Rethlas/LICENSE` Apache-2.0 `11,558 B`; `scripts/vendor/katex/LICENSE.txt` MIT `1,107 B`); 🔴 **no root grant**; `★0`; last push `2026-11-05`
- **Region:** APAC
- **Status:** 🔴 drafted, not sent

## Suggested issue title

Could you add a top-level licence file?

## Suggested issue body

Hello, and thank you for publishing this showcase.

I maintain a curated index of open education-AI projects. I wanted to flag something specific rather
than just ask in general, because it is easy to miss.

The repository **does** contain two licence files — `Rethlas/LICENSE` (Apache-2.0) and
`scripts/vendor/katex/LICENSE.txt` (MIT) — but both belong to **vendored** third-party code. There
is no licence at the repository root, so **your own** code's terms are still unstated. Automated
tooling reports this repository as unlicensed, and anyone reading it carefully reaches the same
conclusion: the vendored grants cover those subtrees only.

If you are willing, adding a root `LICENSE` — **MIT** or **Apache-2.0** for widest reuse — would
make your own work usable, and would sit alongside the vendored licences without conflicting with
them. GitHub can add one: *Add file → Create new file → type `LICENSE` → 'Choose a license
template'*.

No obligation, and thanks for making the work public.

---

🔵 *Drafted by the Globant AI Studios education knowledge base. The measurement above was taken on
the git tree channel (`git clone --filter=blob:none --no-checkout --depth 1` + `git ls-tree -r`),
which enumerates every path case-exactly.*
