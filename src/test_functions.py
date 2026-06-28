import unittest

from functions import *

from calculator import *

class TestFunctions(unittest.TestCase):

    def test_find_pcs_notes(self):
        input_notes = ["Eb", 5, "E#", "Cx", 2, "d", "d#", "fx"]
        expected = [2, 3, 5, 7]
        self.assertEqual(find_pcs_notes(input_notes), expected)

    def test_find_pcs_booleans(self):
        input_bools = [False, False, True, True, False, True, False, True, True, False, False, True]
        expected = [2, 3, 5, 7, 8, 11]
        self.assertEqual(find_pcs_booleans(input_bools), expected)

    def test_get_intervals(self):
        pcs = [2, 3, 5, 7, 8, 11]
        expected = [1, 2, 2, 1, 3, 3]
        self.assertEqual(get_intervals(pcs), expected)

    def test_dyad_tritone(self):
        pcs = [8, 2]
        intervals = get_intervals(pcs)
        expected = "Tritone (augmented 4th/diminished 5th) - 06"
        self.assertEqual(get_dyad_interval(intervals), expected)

    def test_dyad_m3(self):
        pcs = [11, 2]
        intervals = get_intervals(pcs)
        expected = "Minor 3rd - 03"
        self.assertEqual(get_dyad_interval(intervals), expected)

    #def test_decachord(self):

    def test_get_normal_order_outer(self):
        intvls = [2, 1, 2, 1, 3, 3]
        expected = [0, 2, 3, 5, 6, 9]
        self.assertEqual(get_normal_order_outer(intvls), expected)

    def test_get_bno(self):
        intvls = [2, 1, 2, 1, 3, 3]
        expected = [0, 1, 3, 4, 6, 9]
        self.assertEqual(get_bno(intvls), expected)

    def test_get_prime_form(self):
        bno = [0, 2, 4, 6, 8, 10]
        expected = "(02468T)"
        self.assertEqual(get_prime_form(bno), expected)

    #def test_get_icv(self):

    #def test_get_name(self):

    #def test_full_calculation(self):
