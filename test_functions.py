import unittest

from functions import find_pcs_notes, find_pcs_booleans, get_intervals, get_normal_order_outer, get_normal_order_inner, get_bno, get_prime_form, pform_from_booleans, pform_from_notes

class TestFunctions(unittest.TestCase):
    def test_get_pcs_booleans(self):
        bools = [False, False, True, True, False, True, False, True, True, False, True, False]
        self.assertEqual(find_pcs_booleans(bools), [2, 3, 5, 7, 8, 10])

    def test_get_intervals(self):
        PCSet = [2, 3, 5, 7, 8, 10]
        self.assertEqual(get_intervals(PCSet), [1, 2, 2, 1, 2, 4])

    #add test to find prime form from boolean input

    #add test to find prime form from text input

    #write each test to compare outputs for a list of chords
