import tiraRSA.mathfuncs.eulerfunc as ef
import tiraRSA.mathfuncs.factor as mf
import unittest


class TestEulerfunc(unittest.TestCase):
    """
    Correct outputs are sourced from Wolfram Alpha
    """

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


class TestFactor(unittest.TestCase):
    """
    First 2 tests correct answer calculated by hand
    Last test tests mathematical property (reversing the decomposition leads to input).
    """
    def test_fo2_on_power_of_2(self):
        self.assertEqual(mf.factor_out_2(512), (9, 1))

    def test_fo2_on_some_odd_number(self):
        self.assertEqual(mf.factor_out_2(56), (3, 7))

    def test_fo2_on_large_number(self):
        large_number = 18806789087513417307097914989620030248719228414742150346476112113419340441583597412846759474095436243621936173649476569006671220348265338081724505017379
        r, d = mf.factor_out_2(large_number-1)
        self.assertEqual((2**r)*d+1, large_number)
