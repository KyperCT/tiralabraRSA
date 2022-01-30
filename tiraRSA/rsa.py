from .eulerlike import eulerfunc as ef



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
