# `pass260-ecosystem-manifest-tier` — the tier `ACTION ZA` asked for, built, run, and refuted

`ACTION ZA` (`p259`, highest priority) asked to **add the ecosystem-native manifest tier
and probe every grantless and `NOASSERTION` row on it**, keyed by the row's
language/platform: `appinfo/info.xml` *(Nextcloud)*, `*.info.yml` *(Drupal)*, the plugin
header comment *(WordPress)*, `*.cabal`, `*.gemspec`, `*.csproj`.

Its falsifier: *"fewer than `3` rows across all ecosystems resolve — in which case
Nextcloud is a special case and the ladder stays as it is."*

## What was run

| | |
|---|---|
| population | `155` rows — the `13` `ABSENCE-CONFIRMED` grantless rows of `p259`, plus every cell-level `NOASSERTION` / `NONE` / `NO_LICENCE_FILE` / `unlicensed` row harvested from the eight shelves |
| ecosystem detection | from each repository's **own tree** — one `git ls-remote --symref` plus one `--filter=blob:none --depth 1` clone each. `153` trees read, `2` slugs have no ref |
| manifests probed | `104`, each fetched from `raw.githubusercontent.com` on the `ls-remote`-resolved ref and read by **that ecosystem's own reader**, never a grep for the word *license* |

## The result: `ACTION ZA` is REFUTED

Over `153` repositories, the six ecosystems `ZA` named returned:

| ecosystem `ZA` named | repositories | declarations read | |
|---|---|---|---|
| `NEXTCLOUD` *(`appinfo/info.xml`)* | `2` | `2` | 🟡 **both already resolved at `p259` by this very channel** |
| `DRUPAL` *(`*.info.yml`)* | `0` | `0` | 🔴 not one Drupal module or theme in the corpus |
| `WORDPRESS` *(plugin header)* | `0` | `0` | 🔴 none |
| `HASKELL` *(`*.cabal`)* | `0` | `0` | 🔴 none |
| `RUBYGEM` *(`*.gemspec`)* | `1` | 🔴 **`0` valid** | `3` files, **every one vendored** |
| `DOTNET` *(`*.csproj`)* | `2` | 🔴 **`0`** | `5` files, no licence element in any |

🔴 **Zero rows that `p259` had not already resolved. The falsifier is met: Nextcloud is
a special case and the ladder stays as it is.**

## And the sweep that refuted it resolved `36` slugs anyway

| ecosystem | declarations | on this base's ladder? |
|---|---|---|
| `package.json` | `19` | ✅ yes |
| `pyproject.toml` | `9` | ✅ yes |
| `REUSE.toml` + `LICENSES/` | `6` *(the `2` Nextcloud rows)* | 🔴 **no — the one genuinely new channel** |
| `composer.json` | `3` | ✅ yes |
| `pom.xml` | `2` | ✅ yes |
| `version.php` | `2` | ✅ yes — `p259`'s own new tier, paying again |
| `DESCRIPTION` | `2` | ✅ yes |
| `appinfo/info.xml` | `2` | added by `p259` |

🔴 **`34` of the `36` resolved slugs came from an ecosystem that was ALREADY on the
ladder and had simply never been fetched for that row.**

## The finding: a ladder's REACH and a ladder's RUN are different quantities

`p259` classified its `11` resolutions by cause and measured `TIER-NOT-RUN` in `1` of
them — `9 %`, the second-rarest cause. On a population `14×` larger:

| cause | `p259` | 🔴 `p260` |
|---|---|---|
| `TIER-NOT-RUN` | `1` of `11` | 🔴 **`34` of `36` — `94.4 %`** |
| `CHANNEL-ALREADY-RESOLVED` | — | `2` |
| 🔴 `CHANNEL-ABSENT` *(the only cause a longer path list fixes)* | `3` of `11` | 🔴 **`0`** |

🔵 Four consecutive passes have asked for a **wider** ladder. `p257` and `p258` widened
the list of path NAMES across `590` probes and moved `0` rows. `p259` found the tier it
wanted was already present and mis-contracted. `p260` finds the tier present, correctly
contracted, and **never executed on the population that needed it**.

`tier_coverage()` is the predicate that keeps the two apart. `NOT-RUN` and `ABSENT` are
different verdicts, and only one of them is fixed by adding paths.

## Four payload traps, each a guard rather than a note

| guard | the row that forced it |
|---|---|
| `is_foreign(path)` — run **before** the read | `sonic-pi`'s only `.gemspec` files are `app/server/ruby/vendor/concurrent-ruby-1.3.5/*.gemspec`. They say `MIT`; sonic-pi **is** `MIT`. 🔴 `ZA`'s named channel would have been **accidentally right**, which is worse than wrong |
| `is_generated(body)` | `mn-mde-edfi`'s `.csproj` carries `<RepositoryUrl>https://github.com/GIT_USER_ID/GIT_REPO_ID.git</RepositoryUrl>` unsubstituted and `<Copyright>No Copyright</Copyright>`. Those are a **generator's defaults**, not the publisher's assertion |
| `manifest_verdict(name, url)` | `OpenOLAT`'s `pom.xml` line `24`: `<name>Apache 2.0 Open Source L6icense</name>`, against a canonical Apache `<url>`. 🔵 A declaration is a `(name, url)` **pair** — `p259`'s `(path, payload)` key, one layer further in |
| `token_verdict()` → `NOT-SPDX-PROSE` | `pipwerks`'s `package.json`: `"license": "MIT-style license: http://pipwerks.mit-license.org/"`. **"MIT-style" is not MIT**, and a field whose schema says SPDX can still hold a sentence |

And one guard that exists to prevent a **false retraction** rather than a false grant:

- `reservation_verdict()` — `Open-TutorAi/open-tutor-ai-CE`'s `LICENSE` opens *"Copyright
  (c) 2023-2025 … All rights reserved."* and **is** `BSD-3-Clause`. A reader that stops
  at line `2` retracts a correct cell. The verdict is `BOILERPLATE` whenever the
  permissive grant follows, and `RESERVED` only when it does not.


## Two declarations, one repository

[`Zenglian990/AI_Tutor_Release`](https://github.com/Zenglian990/AI_Tutor_Release) carries
a canonical `MIT` text at `LICENSE` *(`1 068` B)* **and** `"license": "ISC"` in
`package.json` — which is what `npm init` writes when nobody chooses. `reconcile()`
answers from `STRENGTH` rather than from judgement: a filed payload carries family,
bound **and** terms, a manifest carries a declaration, so **the filed text is operative
and the manifest is evidence about it**.

And the state that matters more, because it is the common one:

🔴 **`5` of the `7` LMS connectors resolved this pass have NO filed licence text at
all.** Their grant exists only as a manifest field. `MIT`, `ISC`, `BSD` and `Apache-2.0`
each require a distributor to **reproduce the licence text** — so a `MANIFEST-ONLY`
grant in one of those families leaves a studio owing a document the upstream never
published. `manifest_only_duty_gap()` is that predicate.

## The retroactive absence audit

`p259` fixed the single-observation rule **going forward**. It never asked how many
absences already on the shelves were produced by the old one. Every tree in this pass's
census answers it for free:

| | |
|---|---|
| rows whose shelf cell asserts an **absence** | `72` |
| 🔴 carrying a root licence path **after all** | 🔴 **`10` — `13.9 %`** |
| 🟢 absences that hold | 🟢 **`62`** |

🟢 **The ladder is sound** — `86 %` of its absences reproduce against a full tree, which
is the strongest check this base has run on it. 🔴 **And `3` of the `10` are still live
cells, not corrected history:** [`fauzcategui/moodle-sence`](https://github.com/fauzcategui/moodle-sence)
*(a `35 126` B canonical `GPL-3.0` at `license.txt`)*,
[`open-spaced-repetition/fsrs4anki-helper`](https://github.com/open-spaced-repetition/fsrs4anki-helper)
*(`MIT`, at a file named `License` — a case variant)*, and
[`Zenglian990/AI_Tutor_Release`](https://github.com/Zenglian990/AI_Tutor_Release).

🔵 Evidence: [`p260-absence-audit`](../../../evidence/p260-absence-audit.2026-10-17-p260.tsv).

## Controls

`118` controls, every fixture a payload read first-hand at `p260` over
`raw.githubusercontent.com` on an `ls-remote`-resolved ref. `12` mutants run; **all `12`
caught, with the control count holding at `118` for every one** — no silent skip.

🔴 One of them was not caught on the first attempt. Deleting a single member of
`GENERATOR_TOKENS` left every control green, because the live `.csproj` carries **two**
of them. That is `p258`'s *redundant positive list masking its own members*, met inside
the instrument written to record it. The set is now pinned member by member and each
member is asserted to fire alone.

## Running it

```sh
cd compose/code/pass260-ecosystem-manifest-tier && python3 test_manifest_tier.py
```

🔴 **From this directory.** `python3 -I` strips the script's own directory from
`sys.path` (`p229`/`p355`), which is why every `Makefile` recipe `cd`s into the
instrument.
