---
industry: education
region: Global
updated: 2026-10-02
---

# SEB Server proctoring settings validator — gap 90, closed with code

Gap 90 was recorded as *"scope you have to warn the client about"*. This turns it into
*"a piece that already exists"*, which is the difference between a caveat and a
deliverable.

Upstream: [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server),
**Apache-2.0**, `master` @ `7f45689`.

## The defect, in one line of upstream code

`webservice/servicelayer/validation/ProctoringSettingsValidator.java` checks credential
fields **only** for `JITSI_MEET` and `ZOOM`, and then ends:

```java
    return true;   // <-- gap 90
}
```

`ProctoringServerType` has exactly two values today, so the branch looks unreachable.
The moment a third provider is added — which is the whole point of integrating one —
**every one of its credential fields passes validation empty**. The failure then
surfaces at first use, as a proctoring session that cannot authenticate, not at save
time as a form error.

The test reproduces this by execution rather than asserting it: a
`BIGBLUEBUTTON` settings object with **every field `null`** is accepted by a
logic-faithful copy of the current validator, with **zero** violations raised.

## The fix

`src/.../ExtendedProctoringSettingsValidator.java` is a drop-in replacement. Two changes:

1. **The new provider is validated like the built-in two**, using the same
   `proctoringSettings:<field>:notNull` violation templates, so existing UI and i18n
   keys keep working untouched. BigBlueButton authenticates with a single shared secret
   (carried in `appSecret`), so `appKey`, `accountId` and the `sdk*` pair are **not**
   required — demanding them would be a false constraint, which is its own kind of
   wrong data.
2. **The fall-through fails closed.** An unrecognised `serverType` is rejected with
   `proctoringSettings:serverType:typeNotSupported`. This is the part that actually
   closes the gap: without it, the next enum value re-opens the identical hole.

Deploying it needs the one-line enum addition in
`gbl/model/exam/ProctoringServiceSettings.java` and swapping the class named by the
`@ValidProctoringSettings` annotation.

## Run the proof

```sh
./run_test.sh
```

Pure JDK — **no third-party dependency is downloaded or installed**. `testsupport/`
holds minimal stand-ins for the Bean Validation container
(`ConstraintValidator`, a *recording* `ConstraintValidatorContext`),
`commons-lang3`'s `StringUtils.isBlank`, the `@ValidProctoringSettings` marker, and a
`ProctoringServiceSettings` carrying only the fields the validator reads. They are test
scaffolding, standing in for the container exactly as a unit test would; the class under
`src/` is the one that ships.

Result on JDK 21:

```
21/21 checks passed
```

covering: gap 90 reproduced; incomplete settings rejected on the right fields;
whitespace treated as missing, not as a value; one violation only when one field is
missing; complete settings accepted with no violations and the default violation never
disabled; **no regression** on `JITSI_MEET` or `ZOOM` in either direction; and `null`
settings and `null` serverType both rejected.

## What this does not cover

Field **presence**, not field **correctness** — the validator does not check that
`serverURL` is reachable or that the shared secret is accepted by the server. In
upstream that live check is `testExamProctoring`, the one interface method that talks
to the remote service (see the P91 cost table in `../../intel/trends.md`).
