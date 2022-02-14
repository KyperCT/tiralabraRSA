"""
Functions for factorizing
"""


def factor_out_2(n: int):
    """
    Factors out powers of 2 from input number, AKA solve r,d from n=2^r * d, where d % 2 != 0
    :param n: number to process
    :return: Number of powers of 2 and de-factorized number
    """
    runs = 0
    while True:
        if n % 2 == 0:
            n = n // 2
            runs += 1
        else:
            return runs, n
