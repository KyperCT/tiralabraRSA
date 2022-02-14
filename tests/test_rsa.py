import unittest
from tiraRSA import rsa as tr


class TestRsa(unittest.TestCase):
    def setUp(self) -> None:
        primes = {7943145101710562767712512886836874625466408815303442724266795375607174087802774885055943208810348273071090648052930763205438901854415084861090395327969639,
                  9859683912861508896364108357973411205849725192465586046244521470804052302811503119260174928221790706599031626977590103111024736783439335250311108612188489}
        self.keys = tr.generate_keys(primes)

    def test_keygen_generates_expected_e(self):
        self.assertEqual(self.keys[1], 65537)

    def test_encryption_and_decryption_short_string(self):
        self.assertEqual("Päivää",
                         tr.decrypt(tr.encrypt("Päivää", self.keys[0], self.keys[1]), self.keys[0], self.keys[2]))

    def test_encryption_and_decryption_medium_string(self):
        self.assertEqual("Hello World!",
                         tr.decrypt(tr.encrypt("Hello World!", self.keys[0], self.keys[1]), self.keys[0], self.keys[2]))

    def test_encryption_and_decryption_1024_string(self):
        long_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc turpis nunc, gravida et feugiat ac, var."
        self.assertEqual(long_string,
                         tr.decrypt(tr.encrypt(long_string, self.keys[0], self.keys[1]), self.keys[0], self.keys[2]))

