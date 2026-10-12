---
industry: education
region: Global
updated: 2026-10-12
---

# p147-licence-language — `ACTION EE` refuted, and the census turns out to be monolingual

`ACTION EE` asked whether the 8 unlicensed connector rows are **forks of a licensed
parent**, *refuted if fewer than 2 are.*

## 🔴 `ACTION EE` REFUTED — 0 of 8 are forks of anything

Measured on the WebFetch channel `T60` opened, one page per row. 🔴 **Not one carries a
"forked from" notice.** Three show forks *of* themselves, which is the opposite relation.

| row | ★ | fork of | licence in sidebar |
|---|---|---|---|
| `MatheusMach/QuantoFalta` | 9 | 🔴 none | 🔴 none |
| `P1ckle3/blackboard-mcp` | 0 | 🔴 none | 🔴 none |
| `Piyushtanwani/DAU-buddy` | 7 | 🔴 none | 🔴 none |
| `SIU-Toba/docker-guarani` | 4 | 🔴 none | 🔴 none |
| `eugeborzone/Auto_Grade_Guarani` | 0 | 🔴 none | 🔴 none |
| `frjunioalves/suap-mcp` | 0 | 🔴 none | 🔴 none |
| `karkarkins/BlackboardAssistantMCP` | 0 | 🔴 none | 🔴 none |
| `ruud0/aula-virtual-mcp` | 0 | 🔴 none | 🔴 none |

🔵 **The action's consequence clause therefore stands: "ask the author" is the only route**
for the rows that really are unlicensed. 🔴 **Two of the eight are not.**

## 🆕 `T63` — `licen[cs]e` cannot reach `licença` or `licencia`

`p145-licence-census.readme_mention` matches `(?i)##?\s*licen[cs]e|licen[cs]ed under`.
🔴 `Licença` is `l-i-c-e-n-ç-a`; `Licencia` is `l-i-c-e-n-c-i-a`. Neither can match a
pattern requiring `e` in position 7. 🔵 **Not a tuning problem — the two commonest Romance
spellings of the word are outside the character class**, on a shelf whose own pages call a
third of these rows LATAM systems of record.

| row | heading | what it says | p145 | here |
|---|---|---|---|---|
| `frjunioalves/suap-mcp` | `## Licença` | *"licenciado sob a licença MIT. Veja o arquivo `LICENSE`"* | 🔴 `NONE` | 🟢 `README_ONLY / MIT` |
| `eugeborzone/Auto_Grade_Guarani` | `# Licencia` | *"Usted es libre de copiar y modificar lo que quiera de esta repo"* | 🔴 `NONE` | 🟡 `README_ONLY / UNIDENTIFIED` |

🔴 **`suap-mcp` cites a `LICENSE` file that was never committed** — `git ls-files` matches
nothing. The declaration is real, the file it points at does not exist, and a studio has
only prose.

🟡 **`Auto_Grade_Guarani` is a grant, not a licence.** It permits copying and modification
and says nothing about warranty, patents, attribution or redistribution. 🟢 **`UNIDENTIFIED`
is the honest value**, and it is materially different from silence.

## Result over 44 clones, with the baseline as the control

    python3 licence_language.py /path/to/clones base44.tsv
    python3 test_licence_language.py       # 13 tests, authored fixtures, offline

| | FILE | PKG_ONLY | README_ONLY | NONE |
|---|---|---|---|---|
| baseline (p145's pattern) | 34 | 1 | 1 | 🔴 **8** |
| extended | 34 | 1 | 🟢 **3** | 🟢 **6** |

🟢 **The baseline reproduces p145's published value for all 44 rows**, so the only variable
is the pattern. 🟢 **Exactly 2 rows change and 34 `FILE` rows do not** — no false positives.

### Corrected shelf figures

🔴 **Strict-unlicensed over the full 52: 9 → 7.** 🟢 **"No shipped grant" is UNCHANGED at
18** — both rows move from `NONE` into `README_ONLY`, and `README_ONLY` was already inside
that total. 🔵 **One figure moves and the other cannot, which is a property of how the two
were defined and worth knowing before either is quoted.**
