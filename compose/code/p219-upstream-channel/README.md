# `p219` — `ACTION QV`'s instrument, rebuilt for the unit the thing actually has

`ACTION QV` was registered as a **risk** probe: *does a licence-unknown repo sit on a reciprocal
upstream, making it a dead end even if the author answers?* Its method was *"one `README` grep each,
`47` requests, no clone"* against the token set `OpenMage|Magento|Moodle|Open edX|Odoo`.

The grep was run. It fires limb `1` at `6` of `47`. Then each hit was adjudicated from the body,
and the finding is that **the question has a cheaper half which has to be asked first.**

An upstream is a **channel hint** before it is a risk. The ecosystem that makes a repo reciprocal
is the same ecosystem that prescribes *where its licence goes* — WordPress in `readme.txt` and the
plugin header, Moodle in `version.php` and the file docblocks, Magento in `composer.json`. On `3`
of the `4` derivative rows, reading that channel returned a grant, so the dead end never arose and
no maintainer needed asking.

## The two rows a token grep gets wrong, in opposite directions

| row | what the token says | what the body says | defect |
|---|---|---|---|
| [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp) | slug begins `moodle-` → a Moodle plugin | a Python MCP server calling `webservice/rest/server.php` with a token from `user/managetoken.php` | **OVER-FIRE** |
| [`Hesham0-0Nasser/tutor-lms-mcp`](https://github.com/Hesham0-0Nasser/tutor-lms-mcp) | *"MCP server"*, *"OAuth"*, *"API"* → an integration | line `1`: *"WordPress Plugin"*; installs into `wp-content`; `tutor-lms-mcp.php` l.`8` carries `License:     GPL-2.0+` | **UNDER-FIRE** |

The deciding evidence in both cases is the **packaging mode** — is the code installed *into* the
upstream, or does it call the upstream *across a network boundary* — and that is neither a token nor
a slug. Same defect family as `T218-1` *(token vs axis)*, `T218-3` *(heading level vs pass
boundary)* and `T218-4` *(line vs sentence)*: **the instrument's unit was wrong for the thing it
measured.** `relation()` exists because of those two rows, and installation deliberately beats
calling — a WordPress plugin that also calls a REST API is still a WordPress plugin.

## Use

```python
from upstream_channel import verdict
verdict(readme_text, 'Hesham0-0Nasser/tutor-lms-mcp')
# -> {'upstream': 'WordPress', 'relation': 'DERIVATIVE', 'reciprocity': 'RECIPROCAL',
#     'read_first': ['readme.txt', 'tutor-lms-mcp.php', 'plugin.php', 'composer.json'],
#     'instruction': "READ [...] FIRST - WordPress prescribes where its licence goes. ..."}
```

`read_first` is populated **only** for `DERIVATIVE` rows — that is the point. An `INTEGRATION` row
has nothing to read in the upstream's conventions, because the upstream's licence does not reach it.

## What it does NOT claim

🔴 **It does not decide the derivative question in law.** Whether a plugin is a derivative work of
its host is contested, and the WordPress Foundation's position is not a court's. What the instrument
does is order the *work*: read the ecosystem channel before asking a maintainer for a file they may
already have shipped under a different name.

🔴 **A `PROPRIETARY-API` row is not a licence gap at all.** `3` of the `47` call Blackboard Learn
over its vendor API. The constraint there is API terms of service, and this KB records those nowhere —
see `ACTION RB`.

## Tests

```sh
cd compose/code/p219-upstream-channel && python3 -m unittest test_upstream_channel -v
```

`8` tests, all passing. Fixtures are verbatim excerpts of the bodies read on `2026-10-15`. Three are
controls that must **not** fire: an `ECL-2.0` upstream is permissive *(p200/p216)*, a row naming no
upstream is left untouched, and the `{name}.php` substitution is checked on two real slugs.

**Evidence:** [`qv-upstream-reciprocity`](../../../evidence/qv-upstream-reciprocity.2026-10-15-p219.tsv) ·
[`qv-ecosystem-channel`](../../../evidence/qv-ecosystem-channel.2026-10-15-p219.tsv)
