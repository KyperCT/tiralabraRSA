import unittest
import tiraRSA.rsa as tr


class TestRsa(unittest.TestCase):
    def setUp(self) -> None:
        primes = {107017885421, 107017875299}
        self.keys = tr.generate_keys(primes)

    def test_keygen_generates_expected_n(self):
        self.assertEqual(self.keys[0], 11452826716747248115879)

    def test_keygen_generates_expected_e(self):
        self.assertEqual(self.keys[1], 65537)

    def test_keygen_generates_expected_d(self):
        self.assertEqual(self.keys[2], 1875979901460000223273)

