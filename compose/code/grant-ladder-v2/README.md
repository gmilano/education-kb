# grant-ladder-v2 — licence verification instrument (pass 90, 2026-10-09)

Resolves a GitHub slug to **(existence, default branch, HEAD SHA, licence read from the payload, bytes)**.

```sh
./ladder.sh moodle/moodle ls1intum/Artemis
```

Output is TSV: `slug \t EXISTS|ABSENT \t ref \t short-SHA \t licence \t file:bytes`.

## Why it is built this way

Under the agent egress proxy used by these sessions:

| probe | real slug | invented slug | discriminates? |
|---|---|---|---|
| `curl -sI https://github.com/<slug>` | prints only the proxy's `200 Connection Established` | same | **no** |
| `curl -o /dev/null -w '%{http_code}' https://github.com/<slug>` | **403** | **403** | **no** |
| `curl .../api.github.com/repos/<slug>` | **403** | **403** | **no** |
| `git ls-remote --symref https://github.com/<slug> HEAD` | ref + SHA | auth failure → empty | **yes** |
| `raw.githubusercontent.com/<slug>/<SHA>/<file>` | `200` + bytes | `404` (14 B) | **yes** |

Earlier passes recorded `curl -sI` as "403 for everything" and treated that as an unresolvable gap. It is not
a gap — `-sI` was reading the proxy's CONNECT response, and the two probes in the bottom rows work. The ladder
uses only those two.

## Rules it enforces

1. **Pin the SHA.** The payload is fetched at the resolved commit, never at a branch name — a branch moves.
2. **Classify from the text, not a badge.** The licence is decided by reading the payload.
3. **Two-sided control every run.** An invented slug must return `ABSENT` and `moodle/moodle` must return
   `COPYING.txt` at **35 147 B**. Both held on 2026-10-09 across seven passes.
4. **17 candidate filenames.** `NO-LICENCE-PAYLOAD` means all 17 missed — a finding, not an error.

## Known limitation, stated

The classifier keys on the familiar licence families and returns `OTHER/unclassified` for
**ECL-2.0 (Educational Community License 2.0)** — OSI-approved, Apache-2.0-derived, **permissive**, and used by
`sakaiproject/sakai` and `opencast/opencast`. Two permissive platforms were nearly dropped as "unclassified"
risk on this basis. **Any future version must recognise ECL by name.** This is recorded in
`intel/trends.md` `T2` as a transferable lesson: a vertical with its own licence family gets undercounted as
copyleft by generic tooling.

`pass90-results.tsv` holds all 92 slugs resolved on 2026-10-09.
