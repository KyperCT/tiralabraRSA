import unittest
from tiraRSA.rsa import rsa_interface as tri
from tiraRSA.rsa import rsamath as trm


class TestRsaInterface(unittest.TestCase):
    def setUp(self) -> None:
        primes = {7943145101710562767712512886836874625466408815303442724266795375607174087802774885055943208810348273071090648052930763205438901854415084861090395327969639,
                  9859683912861508896364108357973411205849725192465586046244521470804052302811503119260174928221790706599031626977590103111024736783439335250311108612188489}
        self.keys = trm.generate_keys(primes)
        self.n = self.keys[0]
        self.e = self.keys[1]
        self.d = self.keys[2]

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

    def test_one_empty_blocks_with_empty_string(self):
        blocks = tri.divide_string_to_blocks("")
        self.assertEqual(blocks, [''])

    def test_one_block_with_30_chr_string(self):
        blocks = tri.divide_string_to_blocks("a string with exactly 30 chars")
        self.assertEqual(len(blocks), 1)

    def test_3_blocks_with_61_chr_string(self):
        blocks = tri.divide_string_to_blocks("This string has exactly 61 characters, which creates 3 blocks")
        self.assertEqual(len(blocks), 3)

    def test_tti_to_itt_returns_input(self):
        inp = "This text must return unchanged"
        looped = tri.integer_to_text(tri.text_to_integer(inp))
        self.assertEqual(looped, inp)

    def test_tti_empty_string_is_whitespace(self):
        self.assertEqual(tri.text_to_integer(""), 1032)

    def test_tti_30_chr_string(self):
        integer = tri.text_to_integer("a string with exactly 30 chars")
        correct_integer = 1097032115116114105110103032119105116104032101120097099116108121032051048032099104097114115
        self.assertEqual(integer, correct_integer)

    def test_itt_returns_correctly(self):
        text = tri.integer_to_text(1116104105115032115116114105110103032119097115032097110032105110116101103101114033)
        correct_text = "this string was an integer!"
        self.assertEqual(text, correct_text)


class TestRsaMath(unittest.TestCase):
    def test_dummy(self):
        pass
