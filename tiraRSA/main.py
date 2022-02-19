"""
Main IO file; used for cmd input
"""
import json
import base64
import argparse
from .rsa import rsa_interface as ri
from .rsa import rsamath as rm
from .primes import prandom


def main():
    """
    Main IO function; Takes arguments from cmdline, runs other functions based on arguments.
    :return: None
    """
    parser = argparse.ArgumentParser(description='Tool for RSA keygen and encrypt/decrypt')
    options = parser.add_mutually_exclusive_group()
    options.add_argument('--encrypt', nargs=2, help='[txt file] [public key]')
    options.add_argument('--decrypt', nargs=2, help='[ciphertext] [private key]')
    options.add_argument('--generate', action='store_true', help='No arguments, creates keys')

    args = parser.parse_args()

    if args.encrypt is not None:
        with open(args.encrypt[0], "r", encoding="latin-1") as f:
            txt = f.read()
        with open(args.encrypt[1], "r", encoding="ascii") as f:
            key = json.load(f)
        n = int.from_bytes(base64.b64decode(key["Modulus"].encode('ascii')), byteorder="little")
        e = int.from_bytes(base64.b64decode(key["Public exponent"].encode('ascii')), byteorder="little")
        out = ri.encrypt_string(txt, n, e)
        with open("ciphertext", "w", encoding="ascii") as outf:
            json.dump({"ciphers": out}, outf)

    if args.decrypt is not None:
        with open(args.decrypt[0], "r", encoding="ascii") as f:
            cipher = json.load(f)["ciphers"]
        with open(args.decrypt[1], "r", encoding="ascii") as f:
            key = json.load(f)
        n = int.from_bytes(base64.b64decode(key["Modulus"].encode('ascii')), byteorder="little")
        d = int.from_bytes(base64.b64decode(key["Private exponent"].encode('ascii')), byteorder="little")
        dec = ri.decrypt_to_string(cipher, n, d)
        with open("original.txt", "w", encoding="latin-1") as outf:
            outf.write(dec)

    if args.generate:
        primes = prandom.random_primes(2)
        keys = rm.generate_keys(primes)
        with open("publicrsa", "w+", encoding="ascii") as f:
            json.dump({"Name": "Publickey1",
                       "Public exponent": base64.b64encode(keys[1].to_bytes(4, byteorder="little")).decode('ascii'),
                       "Modulus": base64.b64encode(keys[0].to_bytes(128, byteorder="little")).decode('ascii')}, f)
        with open("privatersa", "w+", encoding="ascii") as f:
            json.dump({"Name": "Privatekey1",
                       "Private exponent": base64.b64encode(keys[2].to_bytes(128, byteorder="little")).decode('ascii'),
                       "Modulus": base64.b64encode(keys[0].to_bytes(128, byteorder="little")).decode('ascii')}, f)


if __name__ == "__main__":
    main()
