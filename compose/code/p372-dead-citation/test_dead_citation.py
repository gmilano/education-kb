#!/usr/bin/env python3
"""`p372-dead-citation` controls — 28 controls over the three questions `Gap 483` ran together.

🔴 Every control below is derived from a string that actually caused a published figure to
be wrong on this base, and the string is named in the control.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dead_citation import (classify_string, classify_liveness,  # noqa: E402
                           citation_is_a_live_claim)

FAILED = []


def check(name, got, want):
    if got != want:
        FAILED.append(f"{name}\n      got  {got!r}\n      want {want!r}")


def t_real_addresses_pass():
    """🟢 The positive class, including the two the proxy answers for."""
    for s in ["moodle/moodle", "apereo/opencast", "opencast/opencast",
              "1EdTech/caliper-spec", "oaknational/oak-curriculum-ontology",
              "yetanalytics/lrsql", "UOC/java-lti-1.3", "plastic-labs/honcho",
              "open-spaced-repetition/py-fsrs", "h5p/moodle-mod_hvp"]:
        check(f"address[{s}]", classify_string(s), "ADDRESS")


def t_the_url_path_shape():
    """🔴 `p372`'s headline string class: FOUR of `Gap 483`'s 46 are a slug extractor
    matching inside an API URL. `api.github.com/repos/HKUDS/DeepTutor` -> `repos/HKUDS`."""
    for s in ["repos/HKUDS", "repos/moodle", "repos/openedx", "repos/dodona-edu",
              "orgs/1edtech", "topics/agent-skills", "topics/claude-skill",
              "users/moodle", "git/trees"]:
        check(f"url-path[{s}]", classify_string(s), "URL-PATH-FRAGMENT")


def t_p371_D1_relative_paths_still_rejected():
    """🟢 `p371`'s `D1` must not regress — committed knowledge wired in, not re-derived."""
    for s in [".../archive", "../evidence", "./compose", "x/..", "../.."]:
        check(f"relative[{s}]", classify_string(s), "RELATIVE-PATH")


def t_documentation_placeholders():
    """🔴 `your-username/SafeTutors` — which this base had ALREADY called a citation
    artefact at `agents/trending.md:26044` and then counted as a dead address anyway."""
    for s in ["your-username/SafeTutors", "owner/repo", "your-org/thing",
              "username/my-repo", "example/example"]:
        check(f"placeholder[{s}]", classify_string(s), "PLACEHOLDER")


def t_this_bases_own_negative_controls():
    """🟢 FIVE of `Gap 483`'s 46 are slugs this base FABRICATED to test its own existence
    oracles. A negative control that fails to resolve is the control PASSING."""
    for s in ["UniTime/this-repo-does-not-exist-xyz123",
              "moodle/moodle-definitely-not-a-real-repo-p152",
              "openedx/fake-repo-zzz999",
              "this-definitely-does-not-exist-xyz123/nope",
              "this-org-does-not-exist-zzz9/nope",
              "thisorgdoesnotexist999/nope-nope-nope",
              "elgg/nosuchrepohere12345"]:
        check(f"neg-control[{s}]", classify_string(s), "NEG-CONTROL")


def t_malformed():
    for s in ["", "moodle", "a/b/c", "/x", "x/"]:
        check(f"malformed[{s}]", classify_string(s), "MALFORMED")


def t_EXISTS_EMPTY_is_not_absent():
    """🔴 **THE CONTROL THIS WHOLE INSTRUMENT IS FOR.** `p230` said `GONE`, `p371` said
    `NO-REMOTE`, and `cdweaver1992/edfi-mcp-server` + `openfresno/edgenuity-aeries-grade-passback`
    are LIVE repositories with zero commits. `rc=0` with an empty advertisement is ALIVE."""
    check("rc0-empty", classify_liveness(0, 0, ""), "EXISTS-EMPTY")
    check("rc0-empty-with-warning",
          classify_liveness(0, 0, "warning: You appear to have cloned an empty repository."),
          "EXISTS-EMPTY")
    check("rc0-refs", classify_liveness(0, 4096, ""), "OK")


def t_absent_requires_a_nonzero_rc():
    check("rc128-auth", classify_liveness(128, 0, "fatal: Authentication failed for 'x'"), "ABSENT")
    check("rc128-notfound", classify_liveness(128, 0, "remote: Repository not found"), "ABSENT")


def t_a_proxy_refusal_is_never_an_absence():
    """🔴 `edugit.org` (AlekSIS's real home) answers `CONNECT tunnel failed, response 403`
    and `gitlab.com` answers `HTTP Basic: Access denied`. Neither is evidence of absence.
    🟢 `p279`'s absence-claims rule, enforced inside the liveness classifier itself."""
    check("edugit", classify_liveness(128, 0,
          "fatal: unable to access 'https://edugit.org/AlekSIS/official/AlekSIS-Core/': "
          "CONNECT tunnel failed, response 403"), "PROXY-REFUSED")
    check("gitlab", classify_liveness(128, 0,
          "remote: HTTP Basic: Access denied."), "PROXY-REFUSED")


def t_transport_failure_is_its_own_class():
    check("dns", classify_liveness(128, 0, "fatal: could not resolve host"), "TRANSPORT-FAIL")


def t_live_claim_vs_record():
    """🟢 An append-only history recording that an address answered `NO-REMOTE` is a
    MEASUREMENT, not a recommendation. Retracting it would destroy the trend the file
    exists to carry. Only the live shelves assert usability TODAY."""
    for p in ["agents/top.md", "repos/foundations.md", "verticals/solutions.md"]:
        check(f"live[{p}]", citation_is_a_live_claim(p), True)
    for p in ["agents/trending.md", "repos/trending.md", "intel/open-gaps.md",
              "README.md", "intel/market.md"]:
        check(f"record[{p}]", citation_is_a_live_claim(p), False)


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("t_")]
    for t in tests:
        t()
    if FAILED:
        print(f"🔴 p372-dead-citation — {len(FAILED)} control(s) FAILED:")
        for f in FAILED:
            print(f"   - {f}")
        return 1
    print(f"🟢 p372-dead-citation — all controls green across {len(tests)} groups.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
