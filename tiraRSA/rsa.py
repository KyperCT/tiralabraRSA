from .eulerlike import eulerfunc as ef


def text_to_integer(t):
    return int('1' + "".join(
        list(map((lambda x: str(ord(x)).zfill(3)), t))
    ))


def integer_to_text(i):
    it = str(i)[1:]
    numlist = [it[3*n:3*(n+1)] for n in range(0, int(len(it)/3))]
    return "".join(list(map((lambda x: chr(int(x))), numlist)))


def encrypt(text: str, n: int, e: int) -> int:
    """
    Todo
    :param text: Text to be encrypted
    :param n: Modulus
    :param e: Public exponent
    :return: Cipher integer
    """
    print(text_to_integer(text))
    return pow(text_to_integer(text), e, n)


def decrypt(cipher: int, n: int, d: int) -> str:
    """
    Todo
    :param cipher: ciphertext to be decrypted
    :param n: Modulus
    :param d: Private exponent
    :return: Text string
    """
    m = pow(cipher, d, n)
    print(m)
    return integer_to_text(m)


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
