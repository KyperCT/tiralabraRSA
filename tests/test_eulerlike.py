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

    def test_gcd_correct_output_1(self):
        self.assertEqual(ef.gcd(17,29), 1)

    def test_gcd_correct_output_2(self):
        self.assertEqual(ef.gcd(641781484987498489536435,4869684546868478676846684), 3)

    def test_lcm_correct_output_1(self):
        self.assertEqual(ef.lcm(13, 7), 91)

    def test_lcm_correct_output_2(self):
        self.assertEqual(ef.lcm(107017885420, 107017875298), 5726413358266606177580)
