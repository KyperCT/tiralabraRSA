"""
Implementation of euclidian algorithms
"""


def intdiv(x: int, y: int) -> int:
    """
    Integer division; euclidian division which returns only quotient without remainder
    :param x: Divisor
    :param y: Dividend
    :return: Quotient
    """
    return int(x/y)


def gcd(a: int, b: int) -> int:
    """
    Greatest common divisor implemented via the Euclidian algorithm
    :param a: Integer
    :param b: Integer
    :return: gcd for a and b
    """
    old_r, r = a, b

    while r != 0:
        q = intdiv(old_r, r)
        old_r, r = r, (old_r - (q * r))

    return abs(old_r)


def lcm(a: int, b: int) -> int:
    """
    Lowest common multiple calculated with GCD
    :param a: integer
    :param b: integer
    :return: lcm for a and b
    """
    return (int((abs(a)) / (gcd(a, b)))) * abs(b)


def d_from_extended_gcd(e: int, m: int) -> int:
    """
    Partial implementation of the extended euclidian algorithm for discovering d from ed = 1 (mod l(n))
    (Based on wikipedia pseudocode: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm )
    :param e: e-value from RSA keygen
    :param m: lambda(n) value from RSA keygen
    :return: d -value for RSA private key
    """
    old_r, r = e, m
    old_s, s = 1, 0

    while r != 0:
        q = intdiv(old_r, r)
        old_r, r = r, (old_r - (q * r))
        old_s, s = s, (old_s - (q * s))

    return abs(old_s)
