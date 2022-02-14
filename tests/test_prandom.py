import unittest
from tiraRSA.primes import prandom as tp


class TestPrandom(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_prime_test_correct_on_small_prime(self):
        self.assertEqual(tp.is_probably_prime(65537, 5), True)

    def test_detect_composite(self):
        self.assertEqual(tp.is_probably_prime(643564534563425632457), False)

    def test_prime_test_correct_on_large_prime(self):
        large_prime = 18806789087513417307097914989620030248719228414742150346476112113419340441583597412846759474095436243621936173649476569006671220348265338081724505017379
        self.assertEqual(tp.is_probably_prime(large_prime), True)


