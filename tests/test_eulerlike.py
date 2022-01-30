import tiraRSA.eulerlike.eulerfunc as ef
import unittest


class TestEulerlike(unittest.TestCase):

    def test_intdiv_on_no_remainder(self):
        self.assertEqual(ef.intdiv(8, 4), 2)

    def test_intdiv_on_small_remainder(self):
        self.assertEqual(ef.intdiv(24217, 7352), 3)

    def test_intdiv_on_large_remainder(self):
        self.assertEqual(ef.intdiv(7854334, 46532), 168)

    def test_extended_gcd_correct_output_1(self):
        self.assertEqual(ef.d_from_extended_gcd(240, 46), -9)

    def test_extended_gcd_correct_output_2(self):
        self.assertEqual(ef.d_from_extended_gcd(65537, 5726413358266606177580),  -1875979901460000223273)
