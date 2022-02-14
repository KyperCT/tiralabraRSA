# User guide

### Setting up

This project is implemented as a Python package, and is easiest to run by installing the package into a virtual enviroment.

You can refresh on how to create and access virtual enviroments here:

[Python venv](https://docs.python.org/3/library/venv.html)

If you only want to use the package, and not run tests, you can install the package with the command:
```
pip install git+https://github.com/KyperCT/tiralabraRSA.git#egg=tirarsa
```

If you also want to run the tests, clone the git repository:
```
git clone https://github.com/KyperCT/tiralabraRSA.git
```
And install the package:
```
pip install tiralabraRSA
```
or
```
cd tiralabraRSA
pip install ./
```

### Example setup code (Linux):
In working directory
```
python -m venv .venv/
source .venv/bin/activate
git clone https://github.com/KyperCT/tiralabraRSA.git
cd tiralabraRSA
pip install ./
```

## Usage

### Key generation
Key generation is done with the command:
```
python -m tiraRSA.main --generate
```
This command creates 2 files: publicrsa and privatersa. they are the public key and private key respectively. The same names are always used, so if you want to generate multiples, rename the old keyfiles before running generate again.

### Encryption
Encryption is done with the command:
```
python -m tiraRSA.main --encrypt [text_file] [public_key]
```
This command outputs into the cmdline the ciphertext for the given text using the given key. Maximum length encryptable is at current time ~300 ASCII characters. 

(printing result is temporary)

### Decryption

Decryption is done with the command:
```
python -m tiraRSA.main --decrypt [cipher_as_text_file] [private_key]
```
This command outputs into the cmdline the original message for the given cipher in a text file using the given key.

(printing result is temporary)

## Running tests
```
pip install -r requirements-dev.txt
pytest
pylint tiraRSA/
```
