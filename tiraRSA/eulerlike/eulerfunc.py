
def intdiv(x: int, y: int) -> int:
    """
    Integer division; euclidian division which returns only quotient without remainder
    :param x: Divisor
    :param y: Dividend
    :return: Quotient
    """
    return int(x/y)


def gcd():
    """
    Todo
    :return:
    """
    pass


def lcm():
    """
    Todo
    :return:
    """
    pass


def d_from_extended_gcd(e: int, m: int):
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
