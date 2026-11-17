---
industry: education
region: Global
updated: 2026-11-16
---

# Fixture A — a shelf whose licence column carries the byte-read DATE

🔵 This fixture and `shelf-B-dated-2026-11-17.md` differ in **exactly one byte run**: the
date embedded in the licence column header, `2026-11-16` here and `2026-11-17` there.
Nothing else — not a row, not a column, not a word of prose — differs. `881-G3`'s acceptance
test is that the two grade **identically**.

## The shelf — 2 rows

| Repo | Licence (byte-read `2026-11-16`) | ★ | Pushed | Why it is here |
|---|---|---:|---|---|
| https://github.com/ls1intum/Artemis | MIT | 832 | 2026-11-17 | MIT auto-grading at scale |
| https://github.com/apereo/cas | Apache-2.0 | 11402 | 2026-11-17 | The SSO layer under higher education |
