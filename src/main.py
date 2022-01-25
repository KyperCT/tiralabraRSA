import argparse
import rsa


def main():
    parser = argparse.ArgumentParser(description='Tool for RSA keygen and encrypt/decrypt')
    options = parser.add_mutually_exclusive_group()
    options.add_argument('--encrypt', nargs=2, help='[txt file] [public key]')
    options.add_argument('--decrypt', nargs=2, help='[ciphertext] [private key]')
    options.add_argument('--generate', action='store_true', help='No arguments, creates keys')

    args = parser.parse_args()

    out = None

    if args.encrypt is not None:
        with open(args.encrypt[0], "r") as f:
            txt = f.read()
        with open(args.encrypt[1], "r") as f:
            key = f.read()
        out = rsa.encrypt(txt, key)
    if args.decrypt is not None:
        with open(args.decrypt[0], "r") as f:
            cipher = f.read()
        with open(args.decrypt[1], "r") as f:
            key = f.read()
        out = rsa.decrypt(cipher, key)
    if args.generate:
        keys = rsa.generate_keys()

    if out is not None:
        print(out)


if __name__ == "__main__":
    main()
