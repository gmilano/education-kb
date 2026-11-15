## `2026-11-15` (thirty-third pass, `p828`) — **the LMS tier this base named `1,100` times and had shelved five rows of**

🟢 **`54` build-safe agent rows added (`270` → `324`), all licences BYTE-READ; `6` foundations,
`1` vertical platform, `3` trends (`T99`–`T101`), `1` recipe (`P68`), `2` `T27` rescues, and a
defect found in this repository's own README.**

### What moved

🟢 **`T99`: the open education-agent supply for the LMS vendors this base had NOT enumerated is
`147` repositories** — `blackboard mcp` `78`, `brightspace mcp` `41`, `d2l mcp` `28` — against
`moodle mcp` `248` and `canvas lms mcp` `140`. 🔴 **These shelves held roughly `5` rows across
Brightspace, D2L and Blackboard combined while naming those three brands `1,100` times in prose.**
🟢 **`20` filed this pass after byte-read.**

🟢 **`T100`: `30` of the `61` rows filed are bound to ONE named institution**, and in nearly every
case the institution or its system IS the repository name — UFC, UNEMAT, IFSC, UFAL, CEFET-MG,
UnB, UFPE, Cruzeiro do Sul, DTU, EDHEC, TUM, Glasgow, Merlin/SRCE, Burch, UAEU, SLIIT, Tokyo
University of Technology, USTC, Monash, MUN, Waterloo, Purdue, RIT, UH Mānoa. 🔵 **A search for
"tutor", "grading" or "adaptive learning" reaches none of them.**

🔴 **`T101`: the write path is already common and its controls are not.** Five rows submit
coursework or author into courses; three independent implementations ship a real control —
`merlin-mcp`'s **out-of-band phone approval**, `bb-mcp`'s **server-side RBAC**, and
`sigaa-ifsc-mcp`'s **credential non-possession** (the human logs in; the server never holds the
password).

### Four national system brands recorded here for the first time

| System | Country | Via |
|---|---|---|
| **USOS** | 🇵🇱 Poland | `Carlosito606/ai-personal-assistant` — shared across most Polish HEIs |
| **Aurion** | 🇫🇷 France | `Sillvs/edhec-mcp` |
| **Merlin (SRCE)** | 🇭🇷 Croatia | `simonseifert/merlin-mcp` — the national academic computing centre's Moodle |
| **HWP (Hancom) forms** | 🇰🇷 Korea | `Feynman520/d01-p01-hwp-form-automation-mcp` — mandatory format for Korean public-sector paperwork |

### Rejections and limits

🔴 `gangula-karthik/ntulearn-mcp` **NOT filed** — `p828`'s header-and-hash classifier passed it as
MIT; `p827` had already diffed it and found the **grant clause rewritten** (`T93`). 🔵 **This
pass's own harness has the defect `T93` named, and that is recorded rather than hidden.**
🔴 `pengusto/google-classroom-mcp` — bytes are a **"Pengusto Commercial License 1.0"**, all rights
reserved; already held here, re-confirmed by byte-read. 🔴 Nine real, relevant repositories carry
**no licence file** and were not filed, six of them Spanish-speaking LATAM.

### Channel

🟢 **Both channels live — the best conditions in several passes.** `gh api search/repositories`
bidirectionally controlled (live → `total_count=1`; invented → HTTP `422`); `raw.githubusercontent.com`
byte-read **restored** after `p827`'s `403`s. 🔴 `gh api repos/OWNER/NAME` is **blocked** by session
scope — the `search/repositories` `repo:` form is the narrowest working existence oracle here.
🔴 `curl -sI` re-confirmed **useless**: `200 Connection Established` for live and invented alike.
