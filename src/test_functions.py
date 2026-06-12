import unittest

from functions import *

class TestFunctions(unittest.TestCase):

    def test_unittest(self):
        self.assertEqual(2+2, 4)

    def test_find_pcs_notes(self):
        input_notes = ["Eb", 5, "E#", "Cx", 2, "d", "d#", "fx"]
        expected = [2, 3, 5, 7]
        self.assertEqual(find_pcs_notes(input_notes), expected)
