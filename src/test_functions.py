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
        expected = "Tritone (augmented 4th/diminished 5th) - (06)"
        self.assertEqual(get_dyad_name(intervals), expected)

    def test_dyad_m3(self):
        pcs = [11, 2]
        intervals = get_intervals(pcs)
        expected = "Minor 3rd - (03)"
        self.assertEqual(get_dyad_name(intervals), expected)

    def test_get_pf_decachord(self):
        intervals = [[1, 2, 1, 1, 1, 1, 2, 1, 1, 1], [1, 2, 1, 1, 1, 2, 1, 1, 1, 1], [1, 2, 1, 1, 2, 1, 1, 1, 1, 1]]
        expected = ["(012346789T)", "(012345789T)", "(012345689T)"]
        self.assertEqual([get_pf_decachord(intervals[0]), get_pf_decachord(intervals[1]), get_pf_decachord(intervals[2])], expected)


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

    def test_get_icv(self):
        pcsets = [[0, 1, 2, 5, 6, 9], [3, 4, 7, 9], [2, 5, 6, 7, 10, 11]]
        expected = ["<313431>", "<111111>", "<313431>"]
        self.assertEqual([get_icv(pcsets[0]), get_icv(pcsets[1]), get_icv(pcsets[2])], expected)

    #def test_get_name(self):

    def test_calculator_main_triad(self):
        #input_bool = True
        input_list = [False, False, True, False, False, False, False, True, False, False, False, True]
        expected = [[0, 4, 7], [0, 3, 7], "(037)", "<001110>"]
        self.assertEqual(main(True, input_list), expected)

    #def test_calculator_main_hexachord(self):
    #input_bool = True
    #input_list =  [True, True, True, False, False, True, True, False, False, True, False, False]
    #expected = [[0, 1, 4, 5, 6, 9], [0, 1, 2, 5, 6, 9], "(012569)", "<313431>"]
