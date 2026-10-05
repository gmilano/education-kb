#!/usr/bin/env python3
"""
Suite del pase 109 — P342 (una afirmacion de licencia no es una cesion) y P343
(una captura de ancho acotado trunca un numero con separador de miles).

Las aserciones corren contra los ARTEFACTOS del pase, no contra la prosa:
  p340-sweep.2026-10-05.tsv        300 sondas (15 repos x 10 nombres x 2 ramas)
  actionC-fingerprints.2026-10-05.tsv  medicion de 3 valores en un mismo acto
"""
import csv, os, re, subprocess, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SWEEP = os.path.join(HERE, "p340-sweep.2026-10-05.tsv")
FING = os.path.join(HERE, "actionC-fingerprints.2026-10-05.tsv")

NAMES = ["LICENSE", "LICENCE", "COPYING", "README.md", "LICENSE.md",
         "LICENCE.md", "LICENSE.txt", "LICENSE.TXT", "COPYING.txt", "LICENCE.txt"]
BRANCHES = ["main", "master"]
CONTROL = "gmilano/repo-inventado-p109-control"
PERMISSIVE = {"MIT", "Apache-2.0", "BSD"}


def load_sweep():
    rows = []
    with open(SWEEP, encoding="utf-8") as fh:
        for r in csv.reader(fh, delimiter="\t"):
            if len(r) != 7:
                continue
            rows.append({"repo": r[0], "branch": r[1], "name": r[2],
                         "code": r[3], "bytes": r[4], "sha": r[5], "fam": r[6]})
    return rows


def load_fing():
    rows = []
    with open(FING, encoding="utf-8") as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        for r in rd:
            rows.append(r)
    return rows


class TestSweepShape(unittest.TestCase):
    """El artefacto tiene la forma que la accion B pre-registro."""

    def setUp(self):
        self.rows = load_sweep()

    def test_row_count_is_the_product(self):
        self.assertEqual(len(self.rows), 15 * len(NAMES) * len(BRANCHES))
        self.assertEqual(len(self.rows), 300)

    def test_every_name_probed_on_every_branch(self):
        for repo in {r["repo"] for r in self.rows}:
            for br in BRANCHES:
                got = {r["name"] for r in self.rows
                       if r["repo"] == repo and r["branch"] == br}
                self.assertEqual(got, set(NAMES), f"{repo}/{br}")

    def test_codes_are_http_or_zero(self):
        for r in self.rows:
            self.assertRegex(r["code"], r"^(200|404|403|000)$")


class TestNegativeControl(unittest.TestCase):
    """Sin control negativo, un 404 no se distingue de un canal caido."""

    def setUp(self):
        self.rows = load_sweep()

    def test_control_repo_is_present_in_the_same_batch(self):
        ctl = [r for r in self.rows if r["repo"] == CONTROL]
        self.assertEqual(len(ctl), 20)

    def test_control_repo_is_404_everywhere(self):
        ctl = [r for r in self.rows if r["repo"] == CONTROL]
        self.assertTrue(all(r["code"] == "404" for r in ctl))

    def test_channel_discriminates(self):
        """Un repo real da 200 en algo; el inventado en nada."""
        real = [r for r in self.rows
                if r["repo"] == "oaknational/oak-open-curriculum-ecosystem"]
        self.assertTrue(any(r["code"] == "200" for r in real))
        ctl = [r for r in self.rows if r["repo"] == CONTROL]
        self.assertFalse(any(r["code"] == "200" for r in ctl))


class TestP340Replication(unittest.TestCase):
    """oak cede en LICENCE, no en LICENSE. openedx/XBlock en LICENSE.TXT."""

    def setUp(self):
        self.rows = load_sweep()

    def _one(self, repo, branch, name):
        hits = [r for r in self.rows if r["repo"] == repo
                and r["branch"] == branch and r["name"] == name]
        self.assertEqual(len(hits), 1)
        return hits[0]

    def test_oak_cedes_in_LICENCE_spelling(self):
        r = self._one("oaknational/oak-open-curriculum-ecosystem", "main", "LICENCE")
        self.assertEqual(r["code"], "200")
        self.assertEqual(r["fam"], "MIT")
        self.assertEqual(r["bytes"], "1086")

    def test_oak_does_NOT_cede_in_LICENSE_spelling(self):
        r = self._one("oaknational/oak-open-curriculum-ecosystem", "main", "LICENSE")
        self.assertEqual(r["code"], "404")

    def test_oak_identical_on_both_branches(self):
        a = self._one("oaknational/oak-open-curriculum-ecosystem", "main", "LICENCE")
        b = self._one("oaknational/oak-open-curriculum-ecosystem", "master", "LICENCE")
        self.assertEqual(a["sha"], b["sha"])
        self.assertEqual(a["bytes"], b["bytes"])

    def test_xblock_cedes_in_uppercase_extension(self):
        r = self._one("openedx/XBlock", "master", "LICENSE.TXT")
        self.assertEqual(r["code"], "200")
        self.assertEqual(r["fam"], "Apache-2.0")

    def test_xblock_does_NOT_cede_in_plain_LICENSE(self):
        for br in BRANCHES:
            self.assertEqual(self._one("openedx/XBlock", br, "LICENSE")["code"], "404")


class TestP342ClaimWithoutFile(unittest.TestCase):
    """OlivIA-RAG: afirma MIT en el README, y el archivo no existe."""

    NO_LICENSE_SET = [
        "alfredang/ai4kids", "alfredang/ai-mms", "dddanielliu/NCCU-Moodle-MCP",
        "ASEpochs/ai-digital-teacher", "speechace/speechace-api-samples",
        "moarshy/mcp-tutor", "IMSGlobal/openbadges-specification",
        "ANTONIOALGMAR/StudyAgent", "Javi111003/OlivIA-RAG",
    ]

    def setUp(self):
        self.rows = load_sweep()

    def test_olivia_has_no_license_file_anywhere(self):
        lic = [r for r in self.rows if r["repo"] == "Javi111003/OlivIA-RAG"
               and r["name"] != "README.md"]
        self.assertEqual(len(lic), 18)
        self.assertTrue(all(r["code"] == "404" for r in lic))

    def test_olivia_readme_IS_reachable(self):
        """El testigo de alcance: la ausencia es del archivo, no del canal."""
        rm = [r for r in self.rows if r["repo"] == "Javi111003/OlivIA-RAG"
              and r["name"] == "README.md"]
        self.assertEqual(len(rm), 2)
        self.assertTrue(all(r["code"] == "200" for r in rm))

    def test_olivia_readme_payload_is_the_one_published(self):
        rm = [r for r in self.rows if r["repo"] == "Javi111003/OlivIA-RAG"
              and r["name"] == "README.md" and r["branch"] == "main"][0]
        self.assertEqual(rm["bytes"], "5785")
        self.assertEqual(rm["sha"], "f4be1a6367c6")

    def test_action_B_strong_clause_zero_of_nine(self):
        """Ninguno de los 9 declarados «sin licencia» tiene archivo de cesion."""
        offenders = []
        for repo in self.NO_LICENSE_SET:
            lic = [r for r in self.rows if r["repo"] == repo
                   and r["name"] != "README.md" and r["code"] == "200"]
            if lic:
                offenders.append(repo)
        self.assertEqual(offenders, [], f"cesion escondida en: {offenders}")

    def test_no_permissive_family_hides_in_the_no_license_set(self):
        for repo in self.NO_LICENSE_SET:
            fams = {r["fam"] for r in self.rows
                    if r["repo"] == repo and r["code"] == "200"}
            self.assertFalse(fams & PERMISSIVE, f"{repo} -> {fams}")


class TestP339Tiebreak(unittest.TestCase):
    """Accion C: la huella publicada es del archivo COMPLETO, no del truncado."""

    def setUp(self):
        self.rows = load_fing()

    def test_all_five_reachable(self):
        self.assertEqual(len(self.rows), 5)
        self.assertTrue(all(r["code"] == "200" for r in self.rows))

    def test_full_and_minus1_fingerprints_always_differ(self):
        """Si coincidieran, la medicion no podria desempatar nada."""
        for r in self.rows:
            self.assertNotEqual(r["sha_full"], r["sha_minus1"], r["repo"])

    def test_every_file_ends_in_newline(self):
        """P327 (archivo sin salto final) esta AUSENTE en esta muestra."""
        for r in self.rows:
            self.assertEqual(r["last_byte"], "0a", r["repo"])

    def test_published_fingerprints_match_the_FULL_file(self):
        published = {
            "gibbonedu/core": "93178a43d6d3",
            "openeducat/openeducat_erp": "528f84036800",
            "oaknational/oak-open-curriculum-ecosystem": "02c5a8e84229",
        }
        for r in self.rows:
            if r["repo"] in published:
                self.assertEqual(r["sha_full"], published[r["repo"]], r["repo"])

    def test_no_published_fingerprint_matches_the_TRUNCATED_file(self):
        """La firma de P333 esta AUSENTE: 0 de 5."""
        published = {"93178a43d6d3", "528f84036800", "02c5a8e84229"}
        for r in self.rows:
            self.assertNotIn(r["sha_minus1"], published, r["repo"])

    def test_gibbon_byte_count_is_35121_not_5121(self):
        """P343: la cifra publicada por esta base es la correcta."""
        g = [r for r in self.rows if r["repo"] == "gibbonedu/core"][0]
        self.assertEqual(g["bytes"], "35121")
        self.assertNotEqual(g["bytes"], "5121")


class TestP343GreedyPrefix(unittest.TestCase):
    """
    El defecto de instrumento de este pase, como guardia ejecutable.

    OJO: el primer enunciado de P343 culpaba al cuantificador acotado {1,3}.
    Esta suite lo REFUTO. La causa real es el prefijo goloso ^.* sin frontera
    izquierda en el grupo de captura, y POSIX ERE no ofrece con que frenarlo.
    """

    SUBJECT = "bytes 35.121 B tail"
    SED = ["sed", "-E", r"s/^.*([0-9]{1,3}[.,][0-9]{3}) B.*$/[\1]/"]

    # --- lo que NO es la causa -------------------------------------------
    def test_bounded_quantifier_alone_captures_the_WHOLE_number(self):
        """Refutacion del primer diagnostico: la expresion sola esta bien."""
        self.assertEqual(
            re.search(r"[0-9]{1,3}[.,][0-9]{3}", "35.121 B").group(0), "35.121")

    def test_bounded_quantifier_alone_is_not_fooled_by_longer_numbers(self):
        self.assertEqual(
            re.search(r"[0-9]{1,3}[.,][0-9]{3}", "7.890 B").group(0), "7.890")

    # --- lo que SI es la causa ------------------------------------------
    def test_greedy_prefix_steals_the_leading_digit(self):
        """^.* es goloso y retrocede solo lo minimo: cede '5', se queda el '3'."""
        out = subprocess.run(self.SED, input=self.SUBJECT, capture_output=True,
                             text=True, check=True).stdout.strip()
        self.assertEqual(out, "[5.121]")
        self.assertNotEqual(out, "[35.121]")

    def test_the_truncated_residue_is_plausible(self):
        """Por eso no se detecta mirando el numero: sigue pareciendo bytes."""
        self.assertTrue(re.fullmatch(r"[0-9]{1,3}[.,][0-9]{3}", "5.121"))

    def test_left_boundary_in_PCRE_fixes_it(self):
        """Con lookbehind (PCRE/Python) el numero sale entero."""
        m = re.search(r"(?<![0-9])[0-9]{1,3}(?:[.,][0-9]{3})+", self.SUBJECT)
        self.assertEqual(m.group(0), "35.121")

    # --- las dos propiedades de POSIX ERE que lo vuelven trampa ---------
    def test_posix_ere_has_NO_lazy_quantifiers(self):
        """'.*?X' sobre aXbXc consume aXbX: el '?' no lo vuelve perezoso."""
        out = subprocess.run(["sed", "-E", "s/^.*?X/[LAZY]/"], input="aXbXc",
                             capture_output=True, text=True, check=True).stdout.strip()
        self.assertEqual(out, "[LAZY]c")
        self.assertNotEqual(out, "[LAZY]bXc")

    def test_posix_ere_has_NO_lookbehind(self):
        """La correccion por asercion de frontera no es disponible en sed -E."""
        r = subprocess.run(["sed", "-E", r"s/^.*((?<![0-9])[0-9]{1,3}) B.*$/[\1]/"],
                           input=self.SUBJECT, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("Invalid preceding regular expression", r.stderr)

    # --- la segunda instancia de la misma clase, sin numeros ------------
    def test_same_class_lands_a_PATH_in_a_repo_slug_field(self):
        """El patron de slug tambien encaja en un camino de archivo."""
        slug = r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"
        self.assertTrue(re.fullmatch(slug, "master/LICENSE.TXT"))
        self.assertTrue(re.fullmatch(slug, "gibbonedu/core"))

    # --- el detector ----------------------------------------------------
    def test_fingerprint_is_what_detects_it(self):
        """35.121 y 5.121 no pueden compartir huella: la huella desempata."""
        self.assertEqual(35121 - 5121, 30000)

    def test_published_gibbon_bytes_agree_with_its_fingerprint(self):
        g = [r for r in load_fing() if r["repo"] == "gibbonedu/core"][0]
        self.assertEqual(g["bytes"], "35121")
        self.assertEqual(g["sha_full"], "93178a43d6d3")


if __name__ == "__main__":
    unittest.main(verbosity=2)
