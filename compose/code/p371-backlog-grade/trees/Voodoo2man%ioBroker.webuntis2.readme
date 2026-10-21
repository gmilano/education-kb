![WebUntis2](docs/webuntis2-readme-banner.png)

# ioBroker.webuntis2

[![NPM version](https://img.shields.io/npm/v/iobroker.webuntis2.svg)](https://www.npmjs.com/package/iobroker.webuntis2)

WebUntis2 connects ioBroker with WebUntis. It retrieves timetables for a
student or family account and makes them available in ioBroker for
visualizations, notifications, and automations.

## What the adapter provides

- School search by school name, city, or address
- Simple school selection during setup
- Secure username and password configuration
- A connection test before saving
- Timetables for today, tomorrow, and the current week
- Lesson details such as subject, teacher, room, class, time, and status, with available long names in additional states
- Information about changes, substitutions, and cancelled lessons
- Daily summaries with lesson counts, school times, subjects, and changes
- Current and next lesson information, including the remaining time
- Current and upcoming school holidays
- Automatic updates every five minutes by default

## Installation and setup

1. Install **WebUntis2** from the ioBroker adapter list.
2. Create a new `webuntis2` instance.
3. Search for your school by entering part of its name or a city.
4. Select the matching school from the results.
5. Enter the WebUntis username and password.
6. Use **Test connection** and save the settings.

The adapter stores the selected school together with the information required
for the connection. No server address needs to be entered manually when it is
provided by the school search.

## Admin configuration interface

The adapter uses a React-based Admin interface because setup includes two
interactive operations: searching WebUntis schools from a user-entered query
and displaying the returned schools for selection, and testing the entered
credentials against the selected school before saving. Both operations call
the adapter asynchronously and need to show loading, empty-result, and error
states in the same form. The standard `jsonConfig` controls do not provide
this complete query-and-result workflow on their own; reproducing it there
would require a custom component or equivalent custom UI code. React keeps
these setup interactions together while the adapter remains responsible for
WebUntis requests and validation.

## Data in ioBroker

The timetable is available below `timetable.today`, `timetable.tomorrow`, and
`timetable.week`. Each lesson contains readable values for the subject,
teacher, room, class, start and end time, and lesson status.

Daily summaries show whether there is school, the number and duration of
lessons, the first and last lesson, the subjects in timetable order, and
changes or cancellations. Each day channel also contains a `lessonComparison`
JSON array with the lesson number, original and actual subject, teacher, room,
and status. The lesson number reflects the position in the daily list. Original
and actual start/end times are currently identical. The `info` section contains the connection
status and update information. Holiday information is available below
`holidays`.

Unread messages are available below `inbox`. `unreadCount` gives their number;
`unread` contains a JSON array with message date/time, sender, subject, content,
and an attachment indicator. The adapter retrieves full content when the
WebUntis endpoint permits it and otherwise uses the available preview; the
`contentIsPreview` property distinguishes the two.

## Requirements and notes

- A WebUntis account with access to the selected school is required.
- Username-and-password login is supported.
- QR-code, Microsoft 365, SAML, and OAuth login are not supported.
- Exams and homework are not provided.
- [WebUntis](https://webuntis.com/) is an external service. This project is
  independent and is not affiliated with Untis GmbH.

## Privacy and security

The password is stored using ioBroker's protected configuration mechanism.
Credentials, cookies, and session information are not shown in logs or
published as states. Do not share login details in issues or support requests.

## Support

If the connection does not work, check the selected school and WebUntis login
in a browser first. Then run the connection test in the adapter configuration
and include only relevant, non-sensitive log messages when asking for help.

## Changelog
### WORK IN PROGRESS

- (Voodoo2man) Added the Ukrainian Admin translation.

### 0.1.10 (2026-10-18)

- (Voodoo2man) Improved configuration feedback, holiday names, and connection status; reduced routine login log messages; verified Node.js 26 compatibility; and migrated Dependabot auto-merging to the `pull_request` event.

### 0.1.9 (2026-10-15)

- (Voodoo2man) Improved timetable data and reliability with comparisons, long names, and automatic re-authentication for expired sessions
- (Voodoo2man) Added an inbox for unread messages.

### 0.1.8 (2026-10-14)

- (Voodoo2man) Updated dynamic lesson names, migrated metadata for existing objects, and repaired legacy i18n names.

### 0.1.7 (2026-10-14)

- (Voodoo2man) Improved ioBroker compliance, multilingual object names, shutdown handling, and state updates.
- (Voodoo2man) Added regression tests and removed the historical object dump containing adapter data.

### 0.1.6 (2026-10-08)

- (Voodoo2man) Improved school search feedback, mobile layout, and button behavior in the Admin interface.
- (Voodoo2man) Added Ukrainian Admin translations and documented why the adapter uses a custom React configuration interface.

For earlier releases, see [CHANGELOG_OLD.md](CHANGELOG_OLD.md).

## License

Copyright (c) 2026 Voodoo2man <Voodoo2man@outlook.de>

MIT License. See [LICENSE](LICENSE).
