"""
Implementation of RSA
"""
from tiraRSA.mathfuncs import eulerfunc as ef


def encrypt(data: int, n: int, e: int) -> int:
    """
    Encrypts integers with RSA.
    :param data: Integer to be encrypted
    :param n: Modulus
    :param e: Public exponent
    :return: Cipher integer
    """
    return pow(data, e, n)


def decrypt(cipher: int, n: int, d: int) -> str:
    """
    Decrypts rsa encrypted integers; Inverse function to rsa.encrypt
    :param cipher: ciphertext to be decrypted
    :param n: Modulus
    :param d: Private exponent
    :return: Decrypted integer
    """
    return pow(cipher, d, n)


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
