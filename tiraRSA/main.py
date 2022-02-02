import argparse
from . import rsa
from .primes import prandom
from sys import byteorder
import json
import base64


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

    out = None
    keys = None

    if args.encrypt is not None:
        with open(args.encrypt[0], "r") as f:
            txt = f.read()
        with open(args.encrypt[1], "r") as f:
            key = json.loads(f.read())
        out = rsa.encrypt(txt, key)
    if args.decrypt is not None:
        with open(args.decrypt[0], "r") as f:
            cipher = f.read()
        with open(args.decrypt[1], "r") as f:
            key = json.loads(f.read())
        out = rsa.decrypt(cipher, key)
    if args.generate:
        keys = rsa.generate_keys({107017885421, 107017875299})

    if out is not None:
        print(out)
    if keys is not None:
        with open("publicrsa", "w+") as f:
            json.dump({"Name": "Publickey1",
                       "Public exponent": base64.b64encode(keys[1].to_bytes(4, byteorder=byteorder)).decode('ascii'),
                       "Modulus": base64.b64encode(keys[0].to_bytes(128, byteorder=byteorder)).decode('ascii')}, f)
        with open("privatersa", "w+") as f:
            json.dump({"Name": "Privatekey1",
                       "Private exponent": base64.b64encode(keys[2].to_bytes(128, byteorder=byteorder)).decode('ascii'),
                       "Modulus": base64.b64encode(keys[0].to_bytes(128, byteorder=byteorder)).decode('ascii')}, f)


if __name__ == "__main__":
    main()
