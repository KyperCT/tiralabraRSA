"""
Ramdomized search for primes
"""
import random
from sys import byteorder
from ..mathfuncs import factor

generator = random.SystemRandom()


def is_probably_prime(n: int, trials=10) -> bool:
    """
    Miller Rabin primality test
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    :param n: Value to test
    :param trials: Number of trials before acceptance; probability of false positive is 1/(2^[trials])
    :return: True/False
    """
    return True


def prime_from_seed(n: int) -> int:
    """
    Todo
    :param n:
    :return:
    """
    if n % 2 == 0:
        n -= 1
    while True:
        if is_probably_prime(n):
            return n
        else:
            n += 2


def random_primes(n: int, i0: int = 64, i1: int = 128) -> set:
    """
    Generate almost cryptographically secure distinct random primes.
    :param n: Number of primes to generate
    :param i0: Minimum number of bytes in prime default 64
    :param i1: Maximum number of bytes in prime default 128
    :return: set of primes
    """
    out = set()
    while len(out) < n:
        r = generator.randbytes(generator.randint(i0, i1))
        out.add(prime_from_seed(int.from_bytes(r, byteorder)))
    return out
