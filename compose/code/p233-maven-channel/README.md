# `p233-maven-channel` — the response classifier, and why a status code is never a verdict

`ACTION TS` asked for one readable Maven channel. It found one — and found something more
durable on the way: **`repo1.maven.org` served `200` with a full directory listing, `404` with a
one-byte body, and `429`, for the SAME url, inside one minute.**

That makes the throttle **byte-identical to a real miss**. The negative control
(`org/zzz-not-a-group-9f8e7d/`) exhausted exactly as the positive control (`com/google/`,
a `200` minutes earlier) did.

## The two findings, which are mirror images

| pass | lesson | how the channel lied |
|---|---|---|
| p232 | **a `200` is not a READ** | PyPI's search answers `200` with a *"Client Challenge"* body and no results markup |
| p233 | **a `404` is not an ABSENCE** | `repo1.maven.org` answers `404` with a one-byte body while throttling |

So on a rate-limited channel **PRESENCE is provable and ABSENCE is not** — unless a known
positive passed in the *same window*. `classify()` enforces exactly that: an empty `404`
returns `THROTTLED` without a passing control and `ABSENT` with one. Those are different
claims, and these shelves have conflated them before.

## What was discarded, and why that is recorded here

A paced reader was built for a 17-path groupId sweep and **killed unpublished** when its own
positive control failed. Seventeen paths would have been tabled as seventeen absences. A second
defect was caught before that: the first probe reused **one** output file, so a failed transfer
left the previous url's body in place and three rows inherited Maven's `429` text while
reporting `000`. Every probe now writes its own file.

Both are p230's lint lesson in a new medium: **believe an instrument's silence only after a
known positive.**

## The economical instrument

Do **not** probe coordinates one at a time. One request for a namespace listing enumerates the
whole namespace and is then parsed offline:

```
/maven2/org/   →  603 014 B  →  4 798 groupIds, zero further requests
```

That single read produced this pass's entire JVM education census, including the headline that
`org/imsglobal/` holds exactly one artefact — `basiclti-util/`, LTI 1.1-era.

## Running it

```
cd compose/code/p233-maven-channel && python3 test_classify_response.py
```

Offline and pure: no network, no egress, safe in a hook. It `sys.path`-inserts its own
directory so it passes from any working directory — `p355-cwd-portability`, the lesson p229
paid for.
