#!/usr/bin/env python3
"""`p244-absence-states` — the four states a probe collapses into "there is nothing there".

Pass 244 of 2026-10-16.  Registered by `ACTION WC`, which asked for a sweep of the shelves
for `0`-byte grant payloads "carried as `FOUND` with an unclassifiable body".

🔴 **The sweep was run and `ACTION WC`'s premise is FALSE.**  No carried row is a `0`-byte
payload recorded as `FOUND`, because the shared probe never records one as `FOUND` at all.
`lib/probe_payload.sh::_row_from_fetch` gates on `[ -s "$tmp" ]`, which is false for a
zero-byte file, so the ladder WALKS PAST a `200` and the row lands in the README-dangling-link
branch as `DECLARED-NOT-GRANTED`.  Measured, first-hand, this pass:

    rine77/meineschule-digital  main  DANGLING-README-LINK:LICENSE  0  DECLARED-NOT-GRANTED  -

🔴 That verdict asserts **the file is not there**.  The file is there; it answers `200`; it is
empty.  And it is the SAME cell the probe writes for `HAZA-AIOS/HAZA-SMS`, whose README names
`LICENSE` and whose `LICENSE` genuinely `404`s.  Two different facts, one cell, opposite
remedies: an absent file needs an upstream ASK, an empty file needs the maintainer to commit
the text they already believe they shipped.

─── Why this is a CLASS and not one bug ──────────────────────────────────────────────────────

p241 named the dual of this class on the licence side:

  > every one of these matchers enumerates ways of saying "restricted" and treats the absence
  > of its own vocabulary as permission.

🔵 **`p244`'s class is that sentence with the terms swapped:** every one of these PROBES
enumerates ways of finding a thing and treats the absence of its own vocabulary as the absence
of the THING.  Three channels, three independent instances, all measured in this one pass:

| channel | the probe's answer | what was actually true |
|---|---|---|
| PAYLOAD  | `DECLARED-NOT-GRANTED` *(= no file)*  | `200`, `0` bytes — the file exists |
| ADDRESS  | `UNRESOLVED` *(= no such repo)*       | `rc=0`, `0` refs — the repo exists and is EMPTY |
| QUERY    | `total_count: 0` *(= axis exhausted)* | the query shape is VOID; the axis has `124` rows |

🟢 And the dual of the dual, which belongs here because it is the same epistemics: a payload
read COMPLETELY is reported `MIT` when `258` bytes of it are missing.  `belentani7/aprende-brasil`
is `814` B of canonical MIT with the **liability paragraph absent** — the shelves would carry it
as a clean `MIT`.  That is `p243`'s `webuntis-ha` defect (`797` B, cut off) for the second time,
on another continent.

⚠️ SCOPE.  This instrument answers "what did the probe actually learn?".  It does NOT re-ask the
family question — that is `lib/license_family.sh` and it is not reimplemented here (`P237`,
`P171`).  `family_of` is never called by this module and must not be.

Usage:
    from absence_states import payload_state, address_state, query_shape, grant_completeness
"""

# ─── channel 1: the PAYLOAD ───────────────────────────────────────────────────────────────────

# raw.githubusercontent.com serves its refusal as a BODY, so a caller that reads bytes without
# reading the status code measures a 14-byte "grant".  lib/probe_payload.sh guards this with a
# first-line grep; it is restated as a control here because the guard is what the 0-byte test
# shadows: both guards reduce to "falsy", and then the two cases are indistinguishable.
_NOT_FOUND_BODY = "404: not found"


def payload_state(http_code, byte_count, body=None, declared_in_readme=False):
    """What does a licence-path fetch actually establish?

    Five states, because the remedy differs in each.  `http_code` is authoritative and the byte
    count is read BESIDE it, never instead of it — every grant ladder on these shelves documents
    `byte-floor=1B` for exactly that reason, and that rule is correct.  What it lacks is a name
    for the case where the code says yes and the bytes say nothing.
    """
    if body is not None and str(body).strip().lower() == _NOT_FOUND_BODY:
        # Guarded BEFORE the code test: a mis-plumbed probe can hand us a 200 with this body.
        return "NOT-FOUND-BODY"
    if http_code == 200:
        if byte_count == 0:
            return "EMPTY-DECLARED"
        return "GRANTED"
    if http_code == 404:
        return "ABSENT-DECLARED" if declared_in_readme else "ABSENT-UNDECLARED"
    return "UNREADABLE"


def payload_is_usable(http_code, byte_count, body=None, declared_in_readme=False):
    """Only one of the five states is a grant you can read."""
    return payload_state(http_code, byte_count, body, declared_in_readme) == "GRANTED"


def payload_remedy(state):
    """The reason the distinction is worth its code: the next action differs."""
    return {
        "GRANTED": "read the payload and classify it",
        "EMPTY-DECLARED": "upstream COMMIT: the maintainer believes the text is shipped; it is 0 bytes",
        "ABSENT-DECLARED": "upstream ASK: the README names a path that is not there",
        "ABSENT-UNDECLARED": "no claim and no text; withhold without an ask",
        "NOT-FOUND-BODY": "probe defect: a refusal was measured as a payload",
        "UNREADABLE": "re-probe; a non-200/404 is a transport answer, not a licence answer",
    }[state]


# ─── channel 2: the ADDRESS ───────────────────────────────────────────────────────────────────

_AUTH_DEMAND = "could not read username"


def address_state(returncode, ref_count, stderr=""):
    """Does this repository exist?  `git ls-remote --symref URL HEAD` cannot tell you.

    Measured this pass on three slugs the shared probe writes down identically as `UNRESOLVED`:

      cdweaver1992/edfi-mcp-server                 rc=0    refs=0   -> EMPTY-REPO     (exists!)
      openfresno/edgenuity-aeries-grade-passback   rc=0    refs=0   -> EMPTY-REPO     (exists!)
      jakerains/scormplayer                        rc=128  auth     -> UNREACHABLE-AUTH

    🔴 Two of the three are LIVE repositories.  They have no commits, so `--symref … HEAD`
    prints nothing, so `probe_default_branch` returns empty, so `probe_repo` emits `UNRESOLVED`
    — a verdict an existence sweep reads as "dead address".  `p230` declared `26` dead addresses
    on these shelves; any of them reached by this path is unconfirmed.

    🔵 On github.com an auth demand IS the 404: the server will not distinguish private from
    deleted to an unauthenticated caller, so this function does not pretend to either.
    """
    if returncode != 0:
        if _AUTH_DEMAND in (stderr or "").lower():
            return "UNREACHABLE-AUTH"
        return "TRANSPORT-ERROR"
    if ref_count == 0:
        return "EMPTY-REPO"
    return "LIVE"


def address_exists(returncode, ref_count, stderr=""):
    """An EMPTY-REPO exists.  A sweep that counts it as dead is wrong by one repository."""
    return address_state(returncode, ref_count, stderr) in ("LIVE", "EMPTY-REPO")


# ─── channel 3: the QUERY ─────────────────────────────────────────────────────────────────────

_QUALIFIERS = (
    "topic:", "org:", "user:", "repo:", "language:", "stars:", "license:",
    "created:", "pushed:", "size:", "forks:", "in:", "is:", "archived:",
)


def query_shape(query):
    """Is a `0`-result harvest an exhausted axis, or a query the API could not run?

    Measured this pass, same session, minutes apart:

      topic:deped OR topic:nigeria school management -> total_count 0
      topic:deped                                    -> total_count 10
      topic:cbse OR topic:ncert school AI            -> total_count 0
      topic:cbse                                     -> total_count 124

    🔴 GitHub's REPOSITORY search does not take `OR` between qualifiers; the query returns zero
    rather than an error, and zero is exactly what an exhausted axis returns.  `134` rows across
    the two axes were invisible, and two "the axis is empty" findings were one keystroke from
    being published as fact.

    🟢 So: a harvest that returns `0` may NOT be recorded as an absence until the shape is
    checked.  This is the gate for that, and it is the query-channel instance of this
    instrument's whole class.
    """
    q = " ".join(str(query).split())
    low = q.lower()
    if not q:
        return "EMPTY-QUERY"
    # `OR` is only void BETWEEN QUALIFIERS; `a OR b` over bare terms is accepted by the API.
    if " or " in f" {low} ":
        before_after_qualifier = False
        tokens = low.split()
        for i, tok in enumerate(tokens):
            if tok != "or":
                continue
            neighbours = tokens[max(0, i - 1):i] + tokens[i + 1:i + 2]
            if any(n.startswith(_QUALIFIERS) for n in neighbours):
                before_after_qualifier = True
        if before_after_qualifier:
            return "VOID-OR-BETWEEN-QUALIFIERS"
    return "VALID"


def zero_result_is_absence(query, total_count):
    """THE GATE.  Returns True only when a `0` may be published as "there is no X on this axis"."""
    if total_count != 0:
        return False
    return query_shape(query) == "VALID"


# ─── the dual: a payload read in FULL that is not full ────────────────────────────────────────

# The last paragraph of the MIT text, which is the one that goes missing when a payload is
# truncated, because truncation takes the tail.  Matched on two anchors so a reflowed payload
# still passes: the clause is prose and its line breaks are not load-bearing.
_MIT_LIABILITY_ANCHORS = ("in no event shall", "liable for any claim")
_MIT_GRANT_ANCHOR = "permission is hereby granted"
_MIT_WARRANTY_ANCHOR = 'provided "as is"'


def grant_completeness(text):
    """Is this MIT payload the whole MIT text?

    `belentani7/aprende-brasil` (`814` B, read first-hand at `7d9e6170085b`) carries the grant
    and the warranty disclaimer and STOPS at `NONINFRINGEMENT.` — the liability limitation is
    absent.  The family question answers `MIT` correctly and says nothing about this.

    🔵 Why it matters rather than being pedantry: the grant is intact, so the row is USABLE;
    what is missing is the clause that protects the AUTHOR.  A shelf that carries it as a plain
    `MIT` has published a row whose upstream has, by accident, kept liability it meant to
    disclaim — and the fix is the maintainer's to make, not the consumer's.
    """
    low = " ".join(str(text).split()).lower()
    if not low:
        return "EMPTY"
    if _MIT_GRANT_ANCHOR not in low:
        return "NOT-MIT-SHAPED"
    if all(a not in low for a in _MIT_LIABILITY_ANCHORS):
        if _MIT_WARRANTY_ANCHOR in low:
            return "TRUNCATED-AFTER-WARRANTY"
        return "TRUNCATED-AFTER-GRANT"
    return "COMPLETE"


# ─── the carve-out that grants to nobody ──────────────────────────────────────────────────────

_DISCLAIM_MARKERS = (
    "gelten daher nicht unter dem urheberrecht",   # DE: "therefore do not fall under the copyright of"
    "nicht unter dem urheberrecht",
    "not covered by the copyright of",
    "all rights reserved",
    "todos los derechos reservados",
    "todos os direitos reservados",
)
# Entities that cannot hold a copyright in the carve-out they are named in: a model is not a
# legal person.  This list is deliberately short and literal — it is evidence, not a taxonomy.
_NON_HOLDERS = ("chat-gpt", "chatgpt", "gpt-4", "dall-e", "midjourney", "stable diffusion",
                "gemini", "claude", "copilot")


def carveout_holder(text):
    """A split-scope note EXCLUDES a path.  Does it leave that path with an owner who could license it?

    `Lukas1120987/Schul-System` (`1 324` B, `LICENSE.md`, read first-hand at `9c208c271ef2`) is a
    complete, canonical MIT followed by an `# Anmerkung:`

      > "Alle Bilder in dem Ordner /icons sind KI generiert und gelten daher nicht unter dem
      >  Urheberrecht von Lukas1120987.  Das Urheberrecht der Bilder liegt bei Chat-GPT von OpenAI."

    🔴 The author disclaims the asset path AND assigns it to an entity that cannot hold a
    copyright and does not claim one.  So `/icons` has **no identifiable rights holder** — the
    carve-out subtracts a scope without granting it to anyone.

    🔵 This is NOT what `p1054` (added restrictions), `p242-grant-delta` (additions to a canonical
    text) or `p1058.grant_qualifier` (a restriction before the grant verb) ask.  All three read
    the SOFTWARE grant, which here is clean and complete.  The question none of them asks is
    whether a carve-out's named owner is an owner.  🟢 Contrast `T243-E`'s `oga-veve`, which
    names three scopes and gives each one a real grant and a real holder.
    """
    raw = " ".join(str(text).split())
    low = raw.lower()
    if not any(m in low for m in _DISCLAIM_MARKERS):
        return "NO-CARVEOUT"
    named = [n for n in _NON_HOLDERS if n in low]
    if named:
        return "CARVEOUT-NON-HOLDER:" + named[0]
    return "CARVEOUT-HOLDER-STATED"


# ─── one report ───────────────────────────────────────────────────────────────────────────────

def report(http_code=None, byte_count=0, body=None, declared_in_readme=False,
           returncode=None, ref_count=0, stderr="", query=None, total_count=None, text=None):
    """Every channel this instrument gates, in one dict.  Keys absent when not asked."""
    out = {}
    if http_code is not None:
        st = payload_state(http_code, byte_count, body, declared_in_readme)
        out["payload_state"] = st
        out["payload_remedy"] = payload_remedy(st)
    if returncode is not None:
        out["address_state"] = address_state(returncode, ref_count, stderr)
        out["address_exists"] = address_exists(returncode, ref_count, stderr)
    if query is not None:
        out["query_shape"] = query_shape(query)
        if total_count is not None:
            out["zero_is_absence"] = zero_result_is_absence(query, total_count)
    if text is not None:
        out["grant_completeness"] = grant_completeness(text)
        out["carveout_holder"] = carveout_holder(text)
    return out
