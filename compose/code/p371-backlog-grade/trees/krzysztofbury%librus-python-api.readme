# librus-python-api

[![Weekly live check](https://github.com/krzysztofbury/librus-python-api/actions/workflows/live-check.yml/badge.svg?branch=main)](https://github.com/krzysztofbury/librus-python-api/actions/workflows/live-check.yml)

Read grades, attendance, homework, timetables and messages from **Librus Synergia**
in Python. This independent, asynchronous client handles login, session recovery,
pagination and request limits, returning typed Python objects rather than HTML.

Use it in personal scripts, notification services or application backends. One
service can manage multiple logins while keeping their sessions and data separate.
It is not an official Librus product.

**Requirements:** Python 3.13 or newer. Disk workflows require a trusted local
POSIX filesystem on Linux/macOS, or a fixed local NTFS volume on Windows with
private ACLs. Windows installations include `pywin32` and `tzdata` automatically.
Network paths, reparse-point paths and unsafe storage permissions fail closed.
See [platform requirements](contracts/persistence.md#windows-disk-boundary-25).

**Status:** `1.6.2` accepts more completed-lesson and grade layouts, including
behaviour points, which are validated and not reported as grades.
Class free days, typed capability outcomes and the live-check freshness watchdog
remain available. See [verification](VERIFICATION.md).
The stable 1.x API does not guarantee every school layout. School features depend
on what each account can access. See the [compatibility policy](API.md#compatibility-policy).
See [limitations](#supported-features-and-limitations) below.

## Install

Install the exact release from PyPI after its gated publication completes:

```sh
python -m pip install librus-python-api==1.6.2
```

Pin the exact version qualified by your application. Before publication, use a
checkout or locally built wheel instead.
From a checkout, install into a virtual environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install .
```

To install a locally built wheel instead:

```sh
python -m pip install ./dist/librus_python_api-1.6.2-py3-none-any.whl
```

No CLI or background process is installed: import the library in your own program.

## First request

Provide your login and password through your application's secret management.
The example reads environment variables; the library itself does not discover
environment variables or credential files.

You also need an application context key. Generate it **once**, store it alongside
your other application secrets, and reuse it across runs:

```sh
python -c 'import secrets; print(secrets.token_hex(32))'
```

Set `LIBRUS_LOGIN`, `LIBRUS_PASSWORD` and `LIBRUS_CONTEXT_KEY` in your environment.
The last variable is the 64-character hex output from that command. Do not use
your password as this key. Then run:

```python
import asyncio
import os
from datetime import date

from librus_python_api import AccountCredentials, HomeworkRangeRequest, LibrusService


async def main() -> None:
    accounts = {
        "school": AccountCredentials(
            login=os.environ["LIBRUS_LOGIN"],
            password=os.environ["LIBRUS_PASSWORD"],
        )
    }
    context_key = bytes.fromhex(os.environ["LIBRUS_CONTEXT_KEY"])
    async with LibrusService(accounts, context_key=context_key) as service:
        client = service.account("school")
        profile = await client.student_information()
        print(profile)

        today = date.today()
        homework = await client.homework_range(
            HomeworkRangeRequest(today.replace(day=1), today)
        )
        for item in homework.items:
            print(item.subject, item.topic, item.due_on)


asyncio.run(main())
```

`"school"` is your local account alias, not a student ID. Login occurs on the first
request. The async context manager closes sessions and outstanding work when it
exits. Results are immutable dataclasses; personal fields are omitted from their
`repr`, so access named attributes when displaying data intentionally.

## Common tasks

Inside the service context above:

```python
from datetime import timedelta

# School-provided final grades, grouped into typed subject records.
grades = await client.final_grades()
for subject in grades.items:
    print(subject.subject, subject.annual.raw)

# A week always starts on Monday.
today = date.today()
monday = today - timedelta(days=today.weekday())
timetable = await client.timetable(monday)

# Inclusive date window. Neither attendance nor grades computes a GPA.
attendance = await client.attendance_window(today.replace(day=1), today)

# Permit reuse of this account's cached result for up to 60 seconds.
announcements = await client.announcements(max_age_seconds=60)

# Earlier school years, separate from the message archive (1.3.0).
archive = await client.school_year_archive()
for year in archive.years:
    print(year.school_year, year.subjects)
```

Collections expose named record tuples, for example `homework.items`, rather than
name-keyed dictionaries. Dates are Python `date` values where established by the
upstream contract. Displayed detail values remain strings; missing or unknown
values are not replaced with guessed zeros. Full signatures, result fields and
examples are in the [API reference][api].

### Multiple accounts

Add more aliases to `accounts`, then use `service.account(alias)` for each login.
Reuse **one service** so concurrent calls share its request budget and connection
limits. A parent login and a student login are separate contexts even when they
refer to the same student. Separate processes need application-level coordination
if they share an upstream traffic allowance.

### Bounded pagination and errors

```python
from librus_python_api import RequestBudget
from librus_python_api.exceptions import LibrusError, ViewDisabledError

budget = RequestBudget(max_requests=20, timeout_seconds=60)
try:
    batch = await client.messages(limit=25, max_pages=2, budget=budget)
    for message in batch.items:
        print(message.subject)
    # Request another batch with cursor=batch.next_cursor when it is not None.
except ViewDisabledError:
    print("This school has disabled the requested view.")
except LibrusError as error:
    print(f"Request failed: {error.kind.value}")
```

A budget covers login, queueing and all pages of an operation. Defaults allow
10 requests/second, a burst of 20 and four simultaneous requests across the
service, with one at a time per login.
Fresh reads are the default. Unsupported layouts raise typed errors rather than
silently returning incomplete data. Cursors detect changes; they are not snapshots.

## Messages, files and notifications

- **Message content:** opening received content can mark it read. Pass
  `allow_mark_read=True` only when your application permits that effect.
- **Sending:** prepare a single-use send attempt and obtain approval in your
  application. An `UNKNOWN` result must not trigger an automatic resend.
- **Attachments:** stream bytes with explicit limits, or use the optional
  `files.publish_attachment()` helper to save atomically into an existing directory.
- **Notifications:** optional `NotificationStore` and `NotificationWorkflow`
  provide durable checkpoints, pending delivery and explicit acknowledgement.
- **Persistent sends:** optional `PersistenceStore` records confirmations, claims
  and uncertain outcomes across restarts. Stores create or validate private
  caller-selected directories; core reads do not create files. Use explicit
  `files.prepare_attachment_directory(path)` to provision a private download
  directory without writing platform-specific ACL code.

The legacy and modern messaging backends have distinct references and permissions;
select one explicitly. See the [API reference][api] for complete workflows.

## Context keys and upgrading from 0.6

`LibrusService` now requires `context_key`, exactly 32 secret random bytes.
`client.context.identifier` is an HMAC-SHA256 pseudonym bound to that key, the
alias, login and configured origins. Password changes preserve it. Different
application keys produce different identifiers; the identifier is not a login
credential or permission token. The separate `context.alias` is still plain text.

**Back up and reuse the key with persistent state.** Losing or rotating it changes
all context identifiers. Do not treat an empty history under a different key as
permission to resend a message. Version 0.7 uses storage and notification archive
format 3 and refuses older formats without modifying them. Keep 0.6 stores and
their pending/UNKNOWN records for reconciliation; there is no automatic migration.
See the [upgrade guide][upgrade] before reusing a persistent application.

Loguru is no longer a dependency. For optional diagnostics, pass
`diagnostic_sink=librus_python_api.diagnostics.logging_sink` after importing that
function. Configure handlers with Python's standard `logging` module. You can
also pass your own callable; events contain allowlisted timing/outcome fields,
not credentials, account aliases or response bodies. The old `loguru_sink` was
removed in 0.7.

## Supported features and limitations

| Area | Available |
| --- | --- |
| School data | Profile, grades, school-year archive, attendance, timetable, announcements, agenda, homework and completed lessons |
| Communication | Legacy/modern message lists and content, recipient discovery, bounded attachment streams and explicit sending |
| Application workflows | Shared multi-account limits, caching, notification checkpoints, optional durable send/notification stores |

Completed lessons may be disabled by the school. Behaviour notes are not
implemented. Some recipient, archive and receipt layouts remain
unqualified; backend acceptance is not proof of delivery. Tests cover supported
contracts, not every school or role. Detailed coverage is in the
[verification log][verification]; open work is tracked in [issues][issues].

## Development and support

Use a repository checkout for tests and development tools; they are deliberately
excluded from published source archives. See [CONTRIBUTING.md][contributing] for
setup and offline checks. Report bugs through [GitHub Issues][issues] and security
concerns according to [SECURITY.md][security]. Do not attach credentials or raw
school data to public reports.

MIT licensed. See [LICENSE][license].

[api]: https://github.com/krzysztofbury/librus-python-api/blob/main/API.md
[upgrade]: https://github.com/krzysztofbury/librus-python-api/blob/main/contracts/account-context.md
[verification]: https://github.com/krzysztofbury/librus-python-api/blob/main/VERIFICATION.md
[contributing]: https://github.com/krzysztofbury/librus-python-api/blob/main/CONTRIBUTING.md
[issues]: https://github.com/krzysztofbury/librus-python-api/issues
[security]: https://github.com/krzysztofbury/librus-python-api/blob/main/SECURITY.md
[license]: https://github.com/krzysztofbury/librus-python-api/blob/main/LICENSE
