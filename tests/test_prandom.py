import unittest
import json
from pathlib import Path
from tiraRSA.primes import prandom as tp


class TestPrandom(unittest.TestCase):
    def setUp(self) -> None:
        """
        List of primes generated with Wolfram Mathematica
        List of composites generated with Wolfram Mathematica
        """
        with (Path(__file__).parent / "data/prime.json").open() as primejson:
            self.list_primes = json.load(primejson)
        with (Path(__file__).parent / "data/composite.json").open() as compositejson:
            self.list_composites = json.load(compositejson)

    def test_prime_test_correct_on_small_prime(self):
        self.assertEqual(tp.is_probably_prime(65537, 5), True)

    def test_detect_composite(self):
        self.assertEqual(tp.is_probably_prime(643564534563425632457), False)

    def test_prime_test_correct_on_large_prime(self):
        large_prime = 18806789087513417307097914989620030248719228414742150346476112113419340441583597412846759474095436243621936173649476569006671220348265338081724505017379
        self.assertEqual(tp.is_probably_prime(large_prime), True)

    def test_long_list_of_primes_all_true(self):
        self.assertEqual(all(map(tp.is_probably_prime, self.list_primes)), True)

    def test_long_list_of_composites_all_false(self):
        self.assertEqual(all(map(lambda x: not tp.is_probably_prime(x), self.list_composites)), True)

    def test_prime_generation_passes_prime_test(self):
        set_primes = tp.random_primes(100)
        primes = list(set_primes)
        self.assertEqual(all(map(tp.is_probably_prime, primes)), True)


