#!/usr/bin/env python3
"""Controls for `p349-payload-digest` — `ACTION ZZ-ad`'s instrument.

The committed run is the fixture: [`evidence/payload-digest.2026-10-20-p349.tsv`]. Its
two SHARED groups are the two classes this base has met —

  * `152e3272fbd108fe` — the k12 skill body at TWO DIFFERENT HEADs (p348's finding), and
  * `d22f8b56af465250` — `learner-credential-wallet`'s README at ONE head, i.e. an alias.

🔵 So the digest channel answers a question the HEAD channel cannot (different HEADs, one
payload) AND re-derives what it can (same HEAD, so necessarily one payload). The second
is a positive control for free, which is why both are asserted here.
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from group_digests import group, read  # noqa: E402

HEAD = "slug\tpath\thead\tbytes\tsha256_16\tstate\n"


def rows(text):
    head = HEAD.rstrip("\n").split("\t")
    return [dict(zip(head, l.split("\t"))) for l in text.strip().splitlines()]


class Grouping(unittest.TestCase):
    def test_C1_same_digest_two_slugs_is_SHARED(self):
        shared, uniq = group(rows(
            "a/one\tS.md\th1\t10\tdeadbeef\tOK\n"
            "b/two\tS.md\th2\t10\tdeadbeef\tOK"))
        self.assertEqual(list(shared), ["deadbeef"])
        self.assertEqual(uniq, 0)

    def test_C2_same_digest_TWICE_IN_ONE_SLUG_is_not_shared(self):
        # A repository that ships one file twice is not two repositories. Without this
        # control the instrument reports every vendored duplicate as an identity.
        shared, uniq = group(rows(
            "a/one\tx/S.md\th1\t10\tdeadbeef\tOK\n"
            "a/one\ty/S.md\th1\t10\tdeadbeef\tOK"))
        self.assertEqual(shared, {})
        self.assertEqual(uniq, 1)

    def test_C3_different_digests_are_unique(self):
        shared, uniq = group(rows(
            "a/one\tS.md\th1\t10\taaaa\tOK\n"
            "b/two\tS.md\th2\t11\tbbbb\tOK"))
        self.assertEqual(shared, {})
        self.assertEqual(uniq, 2)

    def test_C4_a_404_row_is_not_evidence_of_anything(self):
        # `NO-PAYLOAD` rows carry `-` in the digest column. Counting them would make two
        # ABSENT files look like one shared payload — absence is not identity (`p244`).
        shared, uniq = group(rows(
            "a/one\tREADME.md\th1\t-\t-\tNO-PAYLOAD(404)\n"
            "b/two\tREADME.md\th2\t-\t-\tNO-PAYLOAD(404)"))
        self.assertEqual(shared, {})
        self.assertEqual(uniq, 0)

    def test_C5_committed_run_reproduces_both_classes(self):
        p = os.path.join(HERE, "result.2026-10-20.tsv")
        shared, _ = group(read(p))
        self.assertIn("152e3272fbd108fe", shared)   # two HEADs, one payload
        self.assertIn("d22f8b56af465250", shared)   # one HEAD, so one payload
        k12 = shared["152e3272fbd108fe"]
        self.assertEqual(len({r["head"] for r in k12}), 2)
        self.assertEqual({r["bytes"] for r in k12}, {"8666"})

    def test_C6_the_k12_READMEs_are_NOT_shared(self):
        # p348's reading stands and is sharpened: one pack, two DISTRIBUTIONS. The skills
        # are the same bytes; the documentation around them is not.
        shared, _ = group(read(os.path.join(HERE, "result.2026-10-20.tsv")))
        k12 = {"anthropics/k12-teacher-skills", "learning-commons-org/agent-skills"}
        groups_with_k12 = [rs for rs in shared.values()
                           if {r["slug"] for r in rs} & k12]
        self.assertEqual(len(groups_with_k12), 1,
                         "the k12 pair shares exactly ONE payload, the skill body")
        self.assertEqual({r["path"].rsplit("/", 1)[-1] for r in groups_with_k12[0]},
                         {"SKILL.md"})

    def test_C7_refuses_empty_argument_list(self):
        r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "group_digests.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        self.assertIn("refusing", r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
