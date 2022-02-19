import unittest
from tiraRSA.rsa import rsa_interface as tri
from tiraRSA.rsa import rsamath as trm


class TestRsa(unittest.TestCase):
    def setUp(self) -> None:
        primes = {7943145101710562767712512886836874625466408815303442724266795375607174087802774885055943208810348273071090648052930763205438901854415084861090395327969639,
                  9859683912861508896364108357973411205849725192465586046244521470804052302811503119260174928221790706599031626977590103111024736783439335250311108612188489}
        self.keys = trm.generate_keys(primes)
        self.n = self.keys[0]
        self.e = self.keys[1]
        self.d = self.keys[2]

    def test_keygen_generates_expected_e(self):
        self.assertEqual(self.keys[1], 65537)

    def test_encryption_and_decryption_short_string(self):
        self.assertEqual("Päivää",
                         tri.decrypt_to_string(tri.encrypt_string("Päivää", self.n, self.e), self.n, self.d))

    def test_encryption_and_decryption_medium_string(self):
        self.assertEqual("Hello World!",
                         tri.decrypt_to_string(tri.encrypt_string("Hello World!", self.n, self.e), self.n, self.d))

    def test_encryption_and_decryption_1024_string(self):
        long_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc turpis nunc, gravida et feugiat ac, vari."
        self.assertEqual(long_string,
                         tri.decrypt_to_string(tri.encrypt_string(long_string, self.keys[0], self.keys[1]), self.keys[0], self.keys[2]))

