"""
Ramdomized search for primes
"""
import random
from ..mathfuncs import factor

generator = random.SystemRandom()


def is_probably_prime(n: int, trials=50) -> bool:
    """
    Miller Rabin primality test
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    :param n: Value to test
    :param trials: Number of trials before acceptance; probability of false positive is 1/(2^[trials])
    :return: True/False
    """
    r, d = factor.factor_out_2(n-1)
    for _ in range(0, trials):
        witness = generator.randint(2, n-2)
        x = pow(witness, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(0, r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True


def random_primes(n: int, b=512) -> set:
    """
    Generate almost cryptographically secure distinct random primes.
    :param n: Number of primes to generate
    :param b: number of bits in prime
    :return: set of primes
    """
    out = set()
    minimum = pow(2, b - 1)
    maximum = pow(2, b) - 1
    while len(out) < n:
        num = generator.randint(minimum, maximum)
        if num % 2 == 0:
            num += 1
        if is_probably_prime(num):
            out.add(num)
    return out
