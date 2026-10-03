#!/usr/bin/env python3
"""Controls for extract_license.py — one per defect found in the pass-65 build, plus negatives."""
import unittest
from extract_license import find

class T(unittest.TestCase):
    def test_direct_prefixed(self):            # the FWU / dini-ag-kim form
        self.assertEqual(find('terms:license <https://creativecommons.org/licenses/by-sa/4.0/> ;'),
                         'https://creativecommons.org/licenses/by-sa/4.0/')
    def test_D1_predicate_as_uri(self):        # reasoned.ttl — must NOT return the predicate
        self.assertEqual(find('<http://purl.org/dc/terms/license> <https://creativecommons.org/licenses/by-sa/4.0/> ;'),
                         'https://creativecommons.org/licenses/by-sa/4.0/')
    def test_D2_blank_node(self):              # jp-cos dataset-20250927.ttl
        self.assertEqual(find('dct:license [\n rdf:value <https://creativecommons.org/licenses/by/4.0/>;\n'
                              ' rdfs:label "Creative Commons license Attribution 4.0"@en;\n'
                              ' foaf:thumbnail <https://licensebuttons.net/l/by/4.0/88x31.png>\n ];'),
                         'https://creativecommons.org/licenses/by/4.0/')
    def test_D3_depth(self):                   # declaration far past any header window
        self.assertEqual(find('@prefix x: <http://e.org/> .\n' + ('# pad\n' * 4000) +
                              'dct:license <https://creativecommons.org/licenses/by/4.0/> .'),
                         'https://creativecommons.org/licenses/by/4.0/')
    def test_rdfxml(self):                     # lp-full.owl form
        self.assertEqual(find('<terms:license rdf:resource="https://creativecommons.org/licenses/by-sa/4.0/"/>'),
                         'https://creativecommons.org/licenses/by-sa/4.0/')
    def test_negative_annotation_property(self):   # declares the TERM, cedes nothing
        self.assertIsNone(find('terms:license rdf:type owl:AnnotationProperty .'))
    def test_negative_thumbnail_only(self):        # a button image is not a cession
        self.assertIsNone(find('foaf:thumbnail <https://licensebuttons.net/l/by/4.0/88x31.png>'))
    def test_negative_no_license(self):
        self.assertIsNone(find('dct:title "x" ; dct:source <https://example.org/a> .'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
