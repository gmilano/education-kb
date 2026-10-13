---
industry: education
region: Global
updated: 2026-10-13
---

# `p172-manifest-attribution` — what a licence MANIFEST can and cannot be asked

**Pass 172, 2026-10-13. `ACTION JO`, `gap 117` settled — and the action asked the wrong question.**

`gap 117` suspected `sakaiproject/sakai`'s `licenses/` manifest of MISLABELLING components: three
files whose body is not the licence the named component ships. p172 read all **86** paths
(**69** distinct blobs, 2 binary PDFs not read) at `HEAD 88f8e09c0a38`.

## The strict question: 3 mismatches, and they are p171's 3

No fourth licence-family mismatch exists. `ACTION JO`'s first falsifier limb — *refuted if the
mismatch rate is `0` outside the `3` p171 already found* — **FIRES**. On the family question the
manifest is three stale files, not a defective map.

Two of the three, verified against authoritative upstream metadata rather than memory:

| file | body | upstream | source |
|---|---|---|---|
| `aopalliance.license.txt` | `LGPL-2.1` | **Public Domain** | mojohaus third-party report; Apache CXF licence listing |
| `dnsjava-1.2.3.license.txt` | `LGPL-2.1` | **BSD** | Maven Central POM |
| `junit-3.8.1.license.txt` | `IPL-1.0` | **`CPL-1.0`** | `repo1.maven.org` POM declares *"Common Public License Version 1.0"* |

The JUnit row is a mismatch **by identifier and barely by effect**: `CPL-1.0` is the IBM Public
License re-stewarded, so the two texts are near-identical. Say "identifier" and not "licence" when
reporting it.

## The mechanism: generic-blob reuse (`T230`)

Both LGPL mismatches have the same cause, and it is structural rather than clerical. Their blob is
**byte-identical** to the manifest's own generic `LGPL2.1.license.txt`. A component file that is a
copy of a family file carries **no component-specific copyright line**, so it is evidence of a
FAMILY and never of that component's grant.

`8` of `86` paths are in this class. `2` of the `8` mismatch; the other `6` happen to be right.

## The finding the action did not ask for: `8` paths are not open source at all (`T231`)

p171's `ACTION JK` swept this same population and reported **`0` hostile**. It tested hostility
with `commercial_use_ok()`, a NONCOMMERCIAL-**phrase** test. A proprietary agreement that withholds
redistribution without ever using the word *"noncommercial"* passes it silently.

Read on the TITLE BLOCK, `8` paths / `7` distinct blobs are proprietary click-through agreements:

| class | paths |
|---|---|
| Sun Microsystems **Binary Code License Agreement** | `activation`, `jta`, `jdbc2_0-stdext` |
| Sun **Software License Agreement and Entitlement** | `servlet` |
| Sun **Specification** click-through | `jsf-api`, `jsf-impl`, `standard` |
| proprietary **single-seat** | `java2html` |

`jta.license.txt` grants *"internal use only … for which the corresponding fee has been paid"* and
forbids modification and decompilation. That is the opposite of a grant Globant can build on.

**And the manifest contradicts itself about one component:** `servlet.license.txt` carries Sun's
proprietary Entitlement while `jsp-api.license.txt` — the sibling API from the same upstream, in the
same directory — carries `Apache-2.0`. The servlet API as shipped by Tomcat is `Apache-2.0`.

## `1` path is not a grant at all

`concurrent.license.txt` is **130 B**: *"Doug Lea's concurrent utilities. See the Notes at
`gee.cs.oswego.edu/...`"*. A grant REFERENCE, not a grant body. Doug Lea's utilities are public
domain; the manifest records nothing.

## `T232` — the shared classifier cannot see Apache-1.1

`25` of the `86` paths carry the **Apache Software License 1.1** text, and
`compose/code/lib/license_family.sh` answers `BSD` for **every one of them**, including the file
literally named `apache1.1.license.txt`. Apache-1.1 is BSD-SHAPED — four clauses, same skeleton —
but it is its own instrument with its own attribution clause. A client scanner that reports
*"34 BSD"* over this tree is reporting ~`25` Apache-1.1 files as BSD.

Detected here on the title block plus the clause-3 signature
(*"This product includes software developed by the Apache Software Foundation"*), which BSD lacks.

## `T224` re-fired, on p172's own instrument

p172's **first** hostility test searched bodies for withholding language and returned `34` raw hits.
`26` were `Apache-2.0` and `LGPL` bodies, caught by phrases like *"shall not modify"* inside
ordinary permissive text. The finding was recovered only by moving to the title block — which is
`P237`'s rule, written in this KB since pass 77, and p172 broke it anyway on its first attempt.
**A rule that has to be remembered is not a control.**

## Files and how to run

```sh
sh classify_bodies.sh /path/to/sakai/licenses   # body family per path, sha256 + bytes
sh detect_nonopen.sh  /path/to/sakai/licenses   # proprietary class per path, TITLE BLOCK only
```

Checkout used: sparse `licenses/*` at `--depth 1`, so the measurement costs no full Sakai clone.

Results: [`../../evidence/sakai-manifest-component-vs-upstream.2026-10-13-p172.tsv`](../../evidence/sakai-manifest-component-vs-upstream.2026-10-13-p172.tsv)
· [`../../evidence/sakai-manifest-nonopen.2026-10-13-p172.tsv`](../../evidence/sakai-manifest-nonopen.2026-10-13-p172.tsv)
· [`../../evidence/sakai-manifest-generic-blob-reuse.2026-10-13-p172.tsv`](../../evidence/sakai-manifest-generic-blob-reuse.2026-10-13-p172.tsv)
