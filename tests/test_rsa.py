import unittest
from tiraRSA import rsa as tr


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

    def test_encryption_and_decryption_short_string(self):
        self.assertEqual("Päivää",
                         tr.decrypt(tr.encrypt("Päivää", self.keys[0], self.keys[1]), self.keys[0], self.keys[2]))

    def test_encryption_and_decryption_medium_string(self):
        self.assertEqual("Hello World!",
                         tr.decrypt(tr.encrypt("Hello World!", self.keys[0], self.keys[1]), self.keys[0], self.keys[2]))

