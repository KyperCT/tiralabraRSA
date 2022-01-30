import tiraRSA.eulerlike.eulerfunc as ef
import unittest


class TestEulerlike(unittest.TestCase):

    def test_intdiv_on_no_remainder(self):
        self.assertEqual(ef.intdiv(8, 4), 2)

    def test_intdiv_on_small_remainder(self):
        self.assertEqual(ef.intdiv(24217, 7352), 3)

    def test_intdiv_on_large_remainder(self):
        self.assertEqual(ef.intdiv(7854334, 46532), 168)

    def test_extended_gcd_correct_output(self):
        e = 65537
        lambdan = 5726413358266606177580
        self.assertEqual((e * ef.d_from_extended_gcd(e, lambdan)) % lambdan,  1)