import random
from . import search
from sys import byteorder

generator = random.SystemRandom()


def random_primes(n: int, i0: int = 64, i1: int = 68) -> set:
    """
    Generate almost cryptographically secure distinct random primes.
    :param n: Number of primes to generate
    :param i0: Minimum number of bytes in prime default 64
    :param i1: Maximum number of bytes in prime default 68
    :return: set of primes
    """
    out = set()
    while len(out) < n:
        r = generator.randbytes(generator.randint(i0, i1))
        out.add(search.prime_from_seed(int.from_bytes(r, byteorder)))
    return out
