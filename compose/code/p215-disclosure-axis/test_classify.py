#!/usr/bin/env python3
"""Tests for the P215 classifier, with the negative controls this base requires.

The controls are the point.  A classifier that returns D1 for everything careful-sounding
would "confirm" the axis and tell us nothing, so three of these tests exist to make the
instrument FAIL to see disclosure where there is none.
"""
import unittest

from classify_disclosure import classify


class TestD1(unittest.TestCase):
    def test_infinitecampus_shape_is_d1(self):
        # Shape of chrischall/infinitecampus-mcp: ToU + provider risk + statute + date.
        t = ("## Acknowledgement of Terms\n"
             "The Infinite Campus Terms of Use state that automated access is not supported. "
             "Infinite Campus may treat use of this channel as a violation of those terms. "
             "This project handles student data subject to FERPA and COPPA. "
             "Terms read on 2026-05-23.")
        cls, label, fired = classify(t)
        self.assertEqual(cls, "D1")
        self.assertEqual(label, "DISCLOSURE-WITH-STATUTE-AND-TOU")
        self.assertIn("dated", fired)

    def test_statute_alone_is_not_d1(self):
        # NEGATIVE CONTROL: naming FERPA in a feature list is not an expedient.
        t = "Features: FERPA-friendly export, gradebook sync, attendance reports."
        cls, _, _ = classify(t)
        self.assertNotEqual(cls, "D1")

    def test_tou_without_the_admission_is_not_d1(self):
        # NEGATIVE CONTROL: quoting the ToU but never admitting the provider may object.
        t = ("See the vendor Terms of Service for details. We comply with FERPA.")
        cls, _, _ = classify(t)
        self.assertNotEqual(cls, "D1")


class TestD2(unittest.TestCase):
    def test_schulmanager_shape_is_d2(self):
        t = ("This is an unofficial community project. There is no connection to "
             "Schulmanager Online GmbH. Use at your own risk.")
        cls, label, _ = classify(t)
        self.assertEqual(cls, "D2")
        self.assertEqual(label, "DISCLOSURE-OF-NON-AFFILIATION")

    def test_myschoolapp_shape_is_d2(self):
        t = ("**Unofficial.** Not affiliated with Blackbaud. Endpoints were "
             "reverse-engineered from network traffic on one school's deployment.")
        self.assertEqual(classify(t)[0], "D2")

    def test_portuguese_non_affiliation_is_d2(self):
        # CaioCastro1/usp-mcp: the declaration is in the project's own language.
        t = ("Projeto nao-oficial, sem vinculo com a Universidade de Sao Paulo.")
        self.assertEqual(classify(t)[0], "D2")

    def test_purdue_shape_is_d2_plus(self):
        t = ("Unofficial and community-run. Not affiliated with, endorsed by, or operated "
             "by Purdue University. Accesses only public, unauthenticated data; no student "
             "accounts, grades or login-protected content.")
        cls, label, _ = classify(t)
        self.assertEqual(cls, "D2+")
        self.assertEqual(label, "DISCLOSURE-OF-SCOPE")


class TestD3(unittest.TestCase):
    def test_handling_promise_alone_is_d3_not_higher(self):
        # The trap this instrument exists to catch: reassuring, and still silent on the
        # contractual plane.
        t = ("Security: your token never leaves your computer. All data is processed "
             "locally. Read-only.")
        cls, label, _ = classify(t)
        self.assertEqual(cls, "D3")
        self.assertEqual(label, "DISCLOSURE-OF-HANDLING-ONLY")

    def test_portuguese_handling_is_d3(self):
        t = "A sua chave fica so no seu computador. Nao vai para nenhum servidor."
        self.assertEqual(classify(t)[0], "D3")


class TestD4(unittest.TestCase):
    def test_bare_readme_is_d4(self):
        t = ("# TechMCP\nSetup: put your roll number and password in config.json and run "
             "the server. Tools: grades, attendance, timetable.")
        cls, label, fired = classify(t)
        self.assertEqual(cls, "D4")
        self.assertEqual(label, "NO-DISCLOSURE")
        self.assertEqual(fired, [])

    def test_praise_is_not_disclosure(self):
        # NEGATIVE CONTROL: a project calling itself safe and production-grade discloses
        # nothing.
        t = ("Production-grade, secure, enterprise-ready, privacy-first, battle-tested, "
             "trusted by students everywhere.")
        self.assertEqual(classify(t)[0], "D4")


class TestPurity(unittest.TestCase):
    def test_classify_is_deterministic(self):
        t = "Unofficial. Not affiliated with Blackbaud."
        self.assertEqual(classify(t), classify(t))



class TestNonEnglishRecall(unittest.TestCase):
    """The v1 classifier was written in English and SILENTLY under-read every non-English
    repo in the inventory -- German "inoffiziell" (not "nicht offiziell"), Vietnamese
    "Xu ly cuc bo", and the English scope phrasing "never touches a student account".

    That is the same SHAPE of defect as P206 (the payload channel being case-sensitive):
    an instrument's blind spot manufacturing FALSE ABSENCES, and manufacturing them
    exactly in the regions this KB is supposed to serve.  These tests exist so the
    regression cannot come back quietly.
    """

    def test_german_inoffiziell_is_d2(self):
        t = ("> **Hinweis:** Dies ist ein inoffizielles Community-Projekt. Es besteht "
             "keine Verbindung zu Schulmanager Online GmbH. Nutzung auf eigene "
             "Verantwortung.")
        cls, label, fired = classify(t)
        self.assertEqual(cls, "D2", f"v1 scored this D4; fired={fired}")
        self.assertIn("non-affiliation", fired)

    def test_vietnamese_local_processing_is_d3(self):
        t = ("## Bao mat & Quyen rieng tu\n"
             "* **Xu ly cuc bo (Local Execution):** Moi thong tin dang nhap va du lieu "
             "hoc tap ca nhan duoc xu ly hoan toan tren may cuc bo cua nguoi dung.")
        cls, _, fired = classify(t)
        self.assertEqual(cls, "D3", f"v1 scored this D4; fired={fired}")
        self.assertIn("handling", fired)

    def test_never_touches_phrasing_is_scope(self):
        t = ("Everything it reads is public and unauthenticated. It never touches a "
             "student account, grades, schedules, bursar records, or anything behind a "
             "Purdue login.\n"
             "> Unofficial and community-run. Not affiliated with, endorsed by, or "
             "operated by Purdue University.")
        cls, label, fired = classify(t)
        self.assertEqual(cls, "D2+", f"v1 scored this D2; fired={fired}")
        self.assertIn("scope", fired)

    def test_the_fixes_did_not_turn_the_negative_controls_positive(self):
        # The whole point of widening recall is that PRECISION must hold.
        for t in ("Production-grade, secure, enterprise-ready, privacy-first.",
                  "Features: FERPA-friendly export, gradebook sync.",
                  "# TechMCP\nPut your roll number and password in config.json."):
            self.assertIn(classify(t)[0], ("D3", "D4"), t)
        self.assertEqual(classify("Production-grade, secure, privacy-first.")[0], "D4")


if __name__ == "__main__":
    unittest.main(verbosity=2)
