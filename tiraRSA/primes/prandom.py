import random
from . import search
from sys import byteorder

generator = random.SystemRandom()


def random_primes(n: int) -> set:
    """
    Generate almost cryptographically secure distinct random primes.
    :param n: Number of primes to generate
    :return: list of primes
    """
    out = set()
    while len(out) < n:
        r = generator.randbytes(generator.randint(64, 68))
        out.add(search.prime_from_seed(int.from_bytes(r, byteorder)))
    return out
