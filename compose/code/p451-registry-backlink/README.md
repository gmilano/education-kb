# `p451` — registry back-link resolution

The instrument behind `p451`'s answer to `Gap 420-C` and `Gap 450-A`.

**The claim it supports.** A package registry stores the `repository` URL submitted *at publish
time*, so that record outlives the repository. A back-link therefore **proves prior existence**
of an address that now `404`s. The converse is NOT claimed: absence of a registry trace proves
nothing, because a repository can be deleted having published nothing.

**The rule it enforces.** A registry record is evidence for an address only when its own metadata
back-links to that exact `owner/repo`. Measured on this base's nine unreachable addresses, **2 of
the 3 name-hits belonged to a third party** (`Gap 451-A`).

## Files

| file | what it does |
|---|---|
| `probe.sh` | the two-channel GitHub probe (`raw` `HEAD/README.md`, then `git ls-remote`). Pass live AND fabricated slugs — if they agree, the probe is zero bits and its negatives are unpublishable (`P249`) |
| `npm_backlink.py` | npm: latest version, declared licence, `repository` back-link, window, maintainers |
| `pypi_backlink.py` | PyPI: version, licence, `project_urls` (where the back-link lives) |
| `packagist_backlink.py` | Packagist: **per-version** licences, `abandoned`, repository. ⚠️ uses `packagist.org/packages/{v}.json` — `repo.packagist.org/packages/…` returns `404` for `laravel/framework` (`Gap 451-B`) |
| `npm_search_channel.py` | the discovery channel that answered `Gap 450-A`: registry search instead of GitHub search |
| `check_contracts.py` | the four contracts re-implemented independently because `make hooks` was DENIED: frontmatter + closed region vocabulary, single canonical `## Opportunities by region` block, no data row rendering as a table header, append-only trending shelves |

## Controls (run them first, every time)

```bash
./probe.sh moodle/moodle globant-fabricated-451/does-not-exist   # expect 200/OK and 404/FAIL
python3 -I npm_backlink.py express globant-fabricated-451-nope-pkg
python3 -I pypi_backlink.py requests globant-fabricated-451-nope-pkg
python3 -I packagist_backlink.py laravel/framework globant-fab-451/nope
```

Measured dead on this host — do not use: `curl -sI github.com/{slug}` (403 for live, dead and
fabricated alike, `p450`); authenticated GitHub MCP `get_file_contents` (identical access-denied
for a live repo and a fabricated one, `p451`). `registry.npmjs.org` and `pypi.org` work here
because they are on the proxy's `noProxy` list; `packagist.org` is not, so its reachability is a
courtesy that may be withdrawn.
