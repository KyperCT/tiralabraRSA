from . import rsamath as rm


def text_to_integer(text):
    """
    Converts ASCII strings into large integers.
    :param text: String of ASCII letters
    :return: Integer representation of input string
    """
    if text == "":
        return text_to_integer(" ")
    return int('1' + "".join(
        list(map((lambda x: str(ord(x)).zfill(3)), text))
    ))


def integer_to_text(int_text):
    """
    Converts an integer into a string. Inverse function to text_to_integer.
    :param int_text: Integer representation of string (text_to_integer)
    :return: String
    """
    i = str(int_text)[1:]
    numlist = [i[3*n:3*(n+1)] for n in range(0, int(len(i)/3))]
    return "".join(list(map((lambda x: chr(int(x))), numlist)))


def divide_string_to_blocks(text: str) -> list:
    inp = text
    output = []
    while True:
        if len(inp) < 30:
            output.append(inp)
            break
        output.append(inp[:30])
        inp = inp[30:]
        if len(inp) == 0:
            break
    return output


def encrypt_string(text: str, n: int, e: int) -> list:
    """
    Encrypts files with RSA.
    :param text: Text to be encrypted
    :param n: Modulus
    :param e: Public exponent
    :return: list of 300 character ciphers
    """
    string_list = divide_string_to_blocks(text)
    output = []
    for item in string_list:
        textblock = text_to_integer(item)
        enc = rm.encrypt(textblock, n, e)
        output.append(enc)
    return output


def decrypt_to_string(cipher: list, n: int, d: int) -> str:
    """
    Decrypts lists of encrypted integers with RSA; Inverse function to rsa.encrypt
    :param cipher: ciphertext to be decrypted
    :param n: Modulus
    :param d: Private exponent
    :return: Text string
    """
    output = []
    for item in cipher:
        decrypted_int = rm.decrypt(int(item), n, d)
        textblock = integer_to_text(decrypted_int)
        output.append(textblock)
    return ''.join(output)
