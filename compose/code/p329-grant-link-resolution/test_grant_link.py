#!/usr/bin/env python3
"""
Controls for `p329-grant-link-resolution` (pass 329).

Rule of this KB (P126): an instrument ships with a control that FAILS if the instrument does not
discriminate. There are five things to discriminate here and the last two are what justify the file:

  1. that a licence CLAIM inside the repository is held apart from the GRANT the repository ships;
  2. that an empty tree RAISES rather than reporting an absence (P275/P278 -- an absence must be
     enumerated; a zero over a path that does not exist measures the PATH);
  3. that a missing README is UNKNOWN and NOT "unlicensed" (P126/P151 -- a missing input is never
     a convenient default);
  4. that a REMOTE licence link (opensource.org, choosealicense.com) is NOT a grant by this repo;
  5. that NOTICE is attribution and NOT a grant -- the shape the Learning Commons repos ship.

Run: `python3 test_grant_link.py` (no pytest on this base; plain asserts, like pass 63's controls).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grant_link import (classify, grant_paths, attribution_paths, declared_licences,
                        claim_links, has_static_badge)

N = 0
def ok(label, got, want):
    global N
    assert got == want, "FAIL %s: got %r want %r" % (label, got, want)
    N += 1
    print("  ok   %-62s %s" % (label, got))

def raises(label, fn, needle):
    global N
    try:
        fn()
    except Exception as e:
        assert needle in str(e), "FAIL %s: %r lacks %r" % (label, str(e), needle)
        N += 1
        print("  ok   %-62s raised" % label)
        return
    raise AssertionError("FAIL %s: nothing raised" % label)

# --- the two real p329 cases, from their actual bytes ------------------------------------------

EDUCATE_AI_README = """# Educate AI
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## License
This project is licensed under the [MIT License](LICENSE).
"""
# Real enumeration was 42 files, zero licence-shaped. Abridged; shape preserved.
EDUCATE_AI_TREE = ['README.md', 'package.json', 'src/App.jsx', 'index.html', 'vite.config.js']

TUTOR_AGENT_README = """# Education Tutor Agent
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
Socratic Tutor Agent with RAG over curriculum content.
## License
This project is licensed under the MIT License.
"""
TUTOR_AGENT_TREE = ['README.md', 'requirements.txt', 'Dockerfile',
                    'src/agents/socratic_tutor.py', 'src/api/app.py']

print("== The p329 case: the README points at its own grant and the grant is not there ==")
r = classify(EDUCATE_AI_README, EDUCATE_AI_TREE)
ok("techpivot25/Educate-AI verdict", r['verdict'], 'DEAD_LINK_GRANT')
ok("  ... and it is NOT usable", r['usable'], False)
ok("  ... MIT was genuinely declared", r['declared'], ['MIT'])
ok("  ... the dead pointer is recorded", r['claim_links'], ['LICENSE'])

r = classify(TUTOR_AGENT_README, TUTOR_AGENT_TREE)
ok("Naresh1401/education-tutor-agent verdict", r['verdict'], 'DEAD_LINK_GRANT')
ok("  ... pointer came from the BADGE href alone", r['claim_links'], ['LICENSE'])

print("== The badge is a claim and never evidence (it is a static image URL) ==")
ok("a green 'License: MIT' badge is present", has_static_badge(EDUCATE_AI_README), True)
ok("  ... and the repo is still unusable", classify(EDUCATE_AI_README, EDUCATE_AI_TREE)['usable'], False)

print("== P275/P278: an absence must be ENUMERATED, never inferred from a probe list ==")
raises("empty tree raises and names P275", lambda: classify(EDUCATE_AI_README, []), 'P275')

print("== P126/P151: a missing input is UNKNOWN, not a default ==")
r = classify(None, ['main.py', 'LICENSE'])
ok("no README -> UNKNOWN", r['verdict'], 'UNKNOWN_NO_README')
ok("  ... declared is None, NOT []", r['declared'], None)
ok("  ... but the shipped grant still counts", r['usable'], True)
ok("no README and no grant -> still UNKNOWN", classify(None, ['main.py'])['verdict'], 'UNKNOWN_NO_README')
ok("  ... and unusable", classify(None, ['main.py'])['usable'], False)

print("== The healthy case, and the p322 boundary this instrument does NOT cross ==")
r = classify(EDUCATE_AI_README, EDUCATE_AI_TREE + ['LICENSE'])
ok("grant present", r['verdict'], 'GRANT_PRESENT')
ok("  ... usable", r['usable'], True)
# A README saying MIT over an AGPL grant file is GRANT_PRESENT here: this instrument resolves the
# POINTER. Comparing the grant TEXT to the claim is p322's job and a different instrument.
r = classify('## License\nMIT\n[MIT License](LICENSE)', ['LICENSE', 'README.md'])
ok("pointer resolves; text comparison is p322's job", r['verdict'], 'GRANT_PRESENT')

print("== Grant-shaped paths: nested, COPYING, and the British spelling ==")
ok("nested LICENSE.md", grant_paths(['sub/LICENSE.md', 'a.py']), ['sub/LICENSE.md'])
ok("COPYING", grant_paths(['COPYING']), ['COPYING'])
ok("licence.txt", grant_paths(['licence.txt']), ['licence.txt'])
ok("a file merely NAMED licensing.py is not a grant", grant_paths(['src/licensing.py']), [])

print("== NOTICE is attribution, not a grant (the Learning Commons shape) ==")
r = classify('## License\nApache-2.0', ['NOTICE', 'src/a.py'])
ok("NOTICE alone -> claim without grant", r['verdict'], 'CLAIM_WITHOUT_GRANT')
ok("  ... unusable", r['usable'], False)
ok("  ... and NOTICE is reported separately", r['attribution_only'], ['NOTICE'])
r = classify('## License\nApache-2.0', ['LICENSE', 'NOTICE'])
ok("NOTICE beside a grant -> grant present", r['verdict'], 'GRANT_PRESENT')
ok("  ... NOTICE still held apart", r['attribution_only'], ['NOTICE'])

print("== A remote licence link is not a grant BY THIS REPOSITORY ==")
remote = """[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## License
Released under the MIT License.
"""
r = classify(remote, ['main.py'])
ok("remote-only pointer -> claim, not dead link", r['verdict'], 'CLAIM_WITHOUT_GRANT')
ok("  ... no repo-relative pointer recorded", r['claim_links'], [])

print("== Silence in both channels ==")
r = classify('# A tool\nDoes a thing.\n', ['main.py'])
ok("no claim, no grant", r['verdict'], 'NO_CLAIM_NO_GRANT')
ok("  ... declared is [] (asked and found none)", r['declared'], [])

print("== Normalisation ==")
ok("Apache 2.0 -> APACHE-2.0", declared_licences('licensed under Apache 2.0'), ['APACHE-2.0'])
ok("two licences, order preserved", declared_licences('Apache-2.0 and MIT'), ['APACHE-2.0', 'MIT'])
ok("anchors and ./ stripped", claim_links('[the license](./LICENSE#summary)'), ['LICENSE'])

print("\nALL ASSERTIONS PASS (%d)" % N)
