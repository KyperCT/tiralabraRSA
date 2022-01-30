import primes.prandom as pr
import eulerlike.eulerfunc as ef

# temporary imports
import math


def encrypt(text, key):
    """
    Todo
    :param text:
    :param key:
    :return:
    """
    return text,key


def decrypt(cipher, key):
    """
    Todo
    :param cipher:
    :param key:
    :return:
    """
    return cipher, key


def generate_keys() -> tuple[tuple[int, int], int]:
    """
    INCOMPLETE. Generate public and private key for RSA.
    :return: Public key, private key
    """
    pqset = {107017885421, 107017875299}
    p = pqset.pop()
    q = pqset.pop()
    n = p * q
    lambdan = math.lcm(p-1, q-1)
    e = 65537
    d = ef.d_from_extended_gcd(e, lambdan)
    del p, q, lambdan
    return (n, e), d
