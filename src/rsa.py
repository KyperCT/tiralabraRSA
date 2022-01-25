import primes.prandom as pr

# temporary imports
from math import lcm


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


def generate_keys():
    """
    Todo
    :return:
    """
    pqset = pr.random_primes(2)
    p = pqset.pop()
    q = pqset.pop()
    n = p * q
    lambdan = lcm(p-1, q-1)

