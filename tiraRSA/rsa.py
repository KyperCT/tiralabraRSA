"""
Implementation of RSA
"""
from .mathfuncs import eulerfunc as ef


def text_to_integer(text):
    """
    Converts ASCII strings into large integers.
    :param text: String of ASCII letters
    :return: Integer representation of input string
    """
    return int('1' + "".join(
        list(map((lambda x: str(ord(x)).zfill(3)), text))
    ))


def integer_to_text(int_text):
    """
    Converts an integer into a string. Inverse function to text_to_integer.
    :param int_text: Integer representation of string (text_to_integer)
    :return: String
    """
    i = str(int_text)[1:]
    numlist = [i[3*n:3*(n+1)] for n in range(0, int(len(i)/3))]
    return "".join(list(map((lambda x: chr(int(x))), numlist)))


def encrypt(text: str, n: int, e: int) -> int:
    """
    Encrypts files with RSA.
    :param text: Text to be encrypted
    :param n: Modulus
    :param e: Public exponent
    :return: Cipher integer
    """
    return pow(text_to_integer(text), e, n)


def decrypt(cipher: int, n: int, d: int) -> str:
    """
    Decrypts files with RSA; Inverse function to rsa.encrypt
    :param cipher: ciphertext to be decrypted
    :param n: Modulus
    :param d: Private exponent
    :return: Text string
    """
    m = pow(cipher, d, n)
    return integer_to_text(m)


def generate_keys(pqset: set) -> tuple:
    """
    Generate public and private key for RSA with given set of primes
    :return: n, e, d
    """
    p = pqset.pop()
    q = pqset.pop()
    n = p * q
    lambdan = ef.lcm(p-1, q-1)
    e = 65537
    d = ef.d_from_extended_gcd(e, lambdan)
    del p, q, lambdan
    return n, e, d
