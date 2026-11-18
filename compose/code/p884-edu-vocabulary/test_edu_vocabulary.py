"""Controls for `p884-edu-vocabulary`.

Every control is a real string from p884's 5,741-repository owner sweep. The
defect this module exists to stop: a naive education keyword set returned 326
"education finds" from that sweep and essentially all of them were machine-learning
repositories. The collision is structural, not careless -- the two vocabularies
share their most useful words, and a university AI lab is the population where
they overlap hardest.
"""
import unittest

import classify_edu as E


class TestMachineLearningIsNotEducation(unittest.TestCase):
    """Real descriptions from the sweep that a naive filter called education."""

    ML_FALSE_POSITIVES = [
        ("thuml/Transfer-Learning-Library",
         "Transfer Learning Library for Domain Adaptation, Task Adaptation, and Domain Generalization"),
        ("lasgroup/SDPO", "Reinforcement Learning via Self-Distillation (SDPO)"),
        ("OpenDriveLab/UniVLA", "[RSS 2025] Learning to Act Anywhere with Task-centric Latent Actions"),
        ("zjunlp/PromptKG", "PromptKG Family: a Gallery of Prompt Learning & KG-related research works"),
        ("SysCV/qdtrack", "Quasi-Dense Similarity Learning for Multiple Object Tracking, CVPR 2021 (Oral)"),
        ("eth-sri/debin", "Machine Learning to Deobfuscate Binaries"),
        ("thuml/Koopa", "Learning Non-stationary Time Series Dynamics with Koopman Predictors"),
        ("OpenDriveLab/SimScale", "[CVPR 2026 Oral] Learning to Drive via Real-World Simulation at Scale"),
    ]

    def test_ml_learning_is_never_PUBLISHED_as_education(self):
        """The contract is `not A`, not `None`.

        TIER-B means "a human must read this", so a repository landing in B has
        made no education claim. What must never happen is an ML repository
        reaching TIER-A, because TIER-A is the bucket this KB publishes from.
        """
        for name, desc in self.ML_FALSE_POSITIVES:
            self.assertNotEqual(E.tier(name, desc), "A",
                                "%s reached the publishable tier" % name)

    # The collocations this module has actually been taught. Kept explicit, because
    # a derived list hides which words the instrument knows.
    LISTED = [
        ("thuml/Transfer-Learning-Library", "Transfer Learning Library for Domain Adaptation"),
        ("lasgroup/SDPO", "Reinforcement Learning via Self-Distillation (SDPO)"),
        ("eth-sri/debin", "Machine Learning to Deobfuscate Binaries"),
        ("OpenDriveLab/UniVLA", "Learning to Act Anywhere with Task-centric Latent Actions"),
        ("zjunlp/PromptKG", "A Gallery of Prompt Learning & KG-related research works"),
        ("SysCV/qdtrack", "Quasi-Dense Similarity Learning for Multiple Object Tracking"),
    ]

    def test_the_LISTED_ml_collocations_are_dropped_OUTRIGHT(self):
        for name, desc in self.LISTED:
            self.assertIsNone(E.tier(name, desc), "%s was called education" % name)

    def test_the_collocation_list_is_OPEN_ENDED_and_that_is_declared(self):
        """An unlisted ML phrase lands in B, never in A.

        This is the module's honest boundary: new ML vocabulary appears faster than
        any list tracks it, so the design requirement is that an unknown phrase
        degrades to "needs reading" rather than to "education".
        """
        self.assertEqual(E.tier("x/y", "Hyperspherical Energy Learning for graphs"), "B")
        self.assertNotEqual(E.tier("x/y", "Hyperspherical Energy Learning for graphs"), "A")

    def test_prompt_learning_was_found_by_THIS_modules_own_controls(self):
        """`prompt learning` was missing from the collocation list until these
        controls caught it. The list is open-ended by nature, which is exactly why
        TIER-B defers rather than decides."""
        self.assertIsNone(E.tier("zjunlp/PromptKG",
                                 "PromptKG Family: a Gallery of Prompt Learning & KG-related research works"))

    def test_gradient_is_not_grading(self):
        self.assertIsNone(E.tier("x/y", "A gradient-based optimiser"))

    def test_example_is_not_an_exam(self):
        self.assertIsNone(E.tier("x/y", "A minimal example of the API"))

    def test_coarse_is_not_a_course(self):
        self.assertIsNone(E.tier("x/y", "coarse-to-fine registration"))

    def test_curriculum_LEARNING_is_an_ml_technique_not_a_syllabus(self):
        """The nastiest collision: `curriculum` is a real ML term of art."""
        self.assertIsNone(E.tier("x/y", "Curriculum learning for robust training"))


class TestRealEducationSurvives(unittest.TestCase):
    """Byte-verified education repositories from the same sweep."""

    TRUE_POSITIVES = [
        # The REAL description from the sweep. An earlier draft of this control
        # truncated it before the word "students" and the control then failed --
        # correctly. A keyword instrument is only as good as the text it is given.
        ("cilt-uct/qna",
         "QNA (Questions and Answers) is a new tool being developed by UNISA and UCT. "
         "QNA enables students to ask questions anonymously, which can be answered by "
         "other students or lecturers or tutors (instructors/TAs)."),
        ("kyoto-u/comfortable-sakai", "A Web browser Extension for improving UX of Sakai LMS"),
        ("KTH/canvas-api", "Node.js API client for Canvas LMS"),
        ("UniversityOfHelsinkiCS/suoritustarkistin",
         "SUOTAR helps graders (i.e. teachers) report course completions"),
        ("RWTH-OS/eduOS-rs", "A teaching operating system written in Rust"),
        ("wasedatime/syllabus-scraper",
         "A high-performance web scraper for obtaining the syllabus of Waseda University."),
    ]
    # `ECNU/EduWork` is deliberately NOT in this list. It is p883's headline find and
    # it is unreachable by ANY keyword instrument: empty description, and a
    # portmanteau name (`EduWork`) that contains no education token. It is asserted
    # absent in `test_an_EMPTY_description_is_judged_on_the_NAME_alone` below. That
    # is the measured justification for the owner channel, stated as a control.

    def test_education_repos_are_kept(self):
        for name, desc in self.TRUE_POSITIVES:
            self.assertIsNotNone(E.tier(name, desc), "%s was dropped" % name)

    def test_tier_a_is_unambiguous(self):
        for name, desc in self.TRUE_POSITIVES[:5]:
            self.assertEqual(E.tier(name, desc), "A", name)

    def test_an_EMPTY_description_is_judged_on_the_NAME_alone(self):
        """p883's find had no description at all; a filter that needs one is blind.

        `EduWork` is a portmanteau rather than a keyword, so even the name does not
        carry an education token -- which is the honest limit of any keyword
        instrument and the reason the OWNER channel exists.
        """
        self.assertEqual(E.tier("AaltoGIS/classroom-grader", ""), "A")
        self.assertIsNone(E.tier("ECNU/EduWork", None))


class TestTierBIsDeferredNotDecided(unittest.TestCase):
    def test_ambiguous_terms_without_ml_noise_land_in_B(self):
        self.assertEqual(E.tier("x/thesis-template", "LaTeX thesis template for students"), "B")

    def test_B_is_never_silently_promoted_to_A(self):
        self.assertNotEqual(E.tier("x/y", "a study of protein folding"), "A")


if __name__ == "__main__":
    unittest.main(verbosity=2)
