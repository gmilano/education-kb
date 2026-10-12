---
industry: education
region: Global
updated: 2026-10-12
---

# p147-tooldef-sum — `ACTION ED` discharged at exactly 227

`@imazhar101/mcp-canvas-server` reads **227 `BOUNDED_STATIC` descriptors** on
`surface_bound` and **18 dynamic registration sites** on `surface_gate*`. `T42` says both
instruments are right about different properties. `ACTION ED` tested that, *refuted if the
sum of the 18 is not 227.*

    python3 tooldef_sum.py <package-root>       # per-module TSV + sum
    python3 test_tooldef_sum.py                 # 11 tests, authored fixtures, offline

## Result — 🟢 the sum is **227**, and `T42` is confirmed by a third method

**18 modules, 18 spread sites in the `tools/list` handler, 1:1.** `dist/servers/canvas/src/index.js:263-280`.

| module | n | module | n | module | n |
|---|---|---|---|---|---|
| `user-tools` | **39** | `module-tools` | 18 | `quiz-tools` | 12 |
| `page-tools` | **21** | `enrollment-tools` | 15 | `course-tools` | 11 |
| `file-tools` | 20 | `assignment-tools` | 12 | `rubric-tools` | 9 |
| `submission-tools` | 20 | `discussion-tools` | 12 | `authentication-provider-tools` | 8 |
| | | `external-tool-tools` | 12 | `login-tools` | 5 |
| | | | | `grade-change-log-tools` | 5 |
| | | | | `admin-tools` | 4 |
| | | | | `grading-standard-tools` | 3 |
| | | | | `lti-launch-definition-tools` | 1 |
| | | | | **TOTAL** | 🟢 **227** |

🟢 **So the largest tool surface this KB quotes is correct**, and the 18 and the 227 are
the same surface counted at two levels. 🔵 **`surface_bound` counts descriptors,
`surface_gate*` counts registration sites, and resolving the sites one level turns one into
the other exactly.**

## 🔴 Why this is not a `grep -c 'name:'`

Canvas tools take a parameter called `name`, so the token occurs inside
`inputSchema.properties` as often as it occurs as a descriptor key. 🔴 **`course-tools.js`
reads 13 occurrences and publishes 11 descriptors.** This probe tracks bracket depth from
the `[` that opens the returned array and counts only the `{` at depth 1, consuming strings
and comments. 🔴 **No module is imported or executed.**
