import unittest

from home.jcampeau.programming.github.com.jdcampeau.PCSetCalc.src.functions import *

from ...src.calculator import get_no_and_bno

class TestFunctions(unittest.TestCase):

    def test_unittest(self):
        self.assertEqual(2+2, 4)

    def test_find_pcs_notes(self):
        self.assertEqual(
                find_pcs_notes(["Eb", 5, "E#", 2, "C#", "bx", "db", "d#", "fx"]),
                [2, 3, 5, 7])

    def test_find_pcs_booleans(self):
        self.assertEqual(
            find_pcs_booleans([False, False, True, True, False, True, False, True, True, False, False, True]),
            [2, 3, 5, 7, 8, 11])

#test dyad and decachord functions

#test get_intervals

#test get_normal_order_outer

#test get_bno and get_prime_form

#test calculator function
