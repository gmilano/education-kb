#!/usr/bin/env python3
"""Controls for `p349-keyed-authors` — the key rule, and the multibyte defect this
instrument's own first build shipped.

🔴 Build 1 of `keyed_authors.sh` read the top timezone offset with `cut -d'×'`. `cut`
refuses a MULTIBYTE delimiter — *"the delimiter must be a single character"* — twice per
row on stderr, while the row printed a plausible `-` in both columns. `×` was this base's
own choice of separator in the histogram it had just written. `C9` is that defect, as a
control: the parse has to come back `+0200 / 894` from the real histogram string.
"""
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from author_key_gate import KEY, census, gate  # noqa: E402

TZ_ALL = ("894×+0200 474×+0300 45×+0100 41×+0000 37×+0530 31×-0500 30×-0700 "
          "29×-0400 19×+0900 13×+0800")


def run_sh(script, body):
    return subprocess.run(["bash", "-c", body], capture_output=True, text=True)


class MultibyteParse(unittest.TestCase):
    def test_C9_parameter_expansion_splits_on_the_multibyte_separator(self):
        r = run_sh(None, 'tz_all="%s"; f=${tz_all%%%% *}; echo "${f#*×}|${f%%%%×*}"' % TZ_ALL)
        self.assertEqual(r.stdout.strip(), "+0200|894")

    def test_C10_cut_still_refuses_it_so_the_fix_is_load_bearing(self):
        r = run_sh(None, "echo '894×+0200' | cut -d'×' -f2")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("single character", r.stderr)

    def test_C11_the_committed_run_carries_all_three_keys_and_they_differ(self):
        p = os.path.join(HERE, "result.2026-10-20.tsv")
        with open(p, encoding="utf-8") as fh:
            head = fh.readline().rstrip("\n").split("\t")
            rows = [dict(zip(head, l.rstrip("\n").split("\t"))) for l in fh if l.strip()]
        for k in ("an", "ae", "an_ae"):
            self.assertIn(k, head)
        terracotta = [r for r in rows if r["slug"].endswith("/terracotta")][0]
        # p348 published "2 815 commits, 18 authors"; the key is `%ae`.
        self.assertEqual((terracotta["commits"], terracotta["an"],
                          terracotta["ae"], terracotta["an_ae"]),
                         ("2815", "14", "18", "20"))
        # and at least one row carries MORE names than addresses — the signature p348
        # found once and this run reproduces, so the spread is not one repository's quirk.
        self.assertTrue(any(int(r["an"]) > int(r["ae"]) for r in rows))


class KeyRule(unittest.TestCase):
    def tmpfile(self, text):
        import tempfile
        d = tempfile.mkdtemp()
        p = os.path.join(d, "s.md")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(text)
        return p

    def test_C1_unkeyed_figure_in_the_live_section_is_a_finding(self):
        f = gate([self.tmpfile("## Pass 9\n\n2 815 commits, 18 authors\n")])
        self.assertEqual([x[1] for x in f], ["P349-UNKEYED-AUTHORS"])

    def test_C2_the_same_figure_keyed_is_clean(self):
        self.assertEqual(gate([self.tmpfile(
            "## Pass 9\n\n2 815 commits, 18 authors (`%ae`)\n")]), [])

    def test_C3_identities_counts_as_a_key(self):
        self.assertEqual(gate([self.tmpfile(
            "## Pass 9\n\n20 authors by identities\n")]), [])

    def test_C4_spanish_vocabulary_is_read(self):
        f = gate([self.tmpfile("## Pass 9\n\n18 autores\n")])
        self.assertEqual(len(f), 1)
        self.assertEqual(gate([self.tmpfile("## Pass 9\n\n18 autores (`%ae`)\n")]), [])

    def test_C5_a_word_without_a_figure_is_not_a_cell(self):
        self.assertEqual(gate([self.tmpfile("## Pass 9\n\nthe authors of this repo\n")]), [])

    def test_C6_history_is_a_census_and_never_a_failure(self):
        p = self.tmpfile("## Pass 9\n\nclean: 3 authors (`%ae`)\n\n"
                         "## Pass 8\n\ninherited: 18 authors\n")
        self.assertEqual(gate([p]), [])
        self.assertEqual(census([p]), (1, 1))

    def test_C7_NO_KEY_is_itself_a_declaration(self):
        # A pass that cannot derive the key says so rather than dropping the figure.
        self.assertEqual(gate([self.tmpfile("## Pass 9\n\n18 authors — NO-KEY\n")]), [])

    def test_C8_refuses_empty_argument_list(self):
        r = subprocess.run([sys.executable, "-I",
                            os.path.join(HERE, "author_key_gate.py"), "gate"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        self.assertIn("refusing", r.stderr)

    def test_C12_key_regex_does_not_fire_on_an_unrelated_percent_token(self):
        self.assertIsNone(KEY.search("92 % of students"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
