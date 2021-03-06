# Testing document

## Unit test coverage

Report generated with coverage.py

| Module | statements | missing | excluded | branches | partial | coverage |
|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
| tests/\_\_init__.py | 0 | 0 | 0 | 0 | 0 | 100% |
| tests/test_mathfuncs.py | 25 | 0 | 0 | 4 | 0 | 100% |
| tests/test_prandom.py | 25 | 0 | 0 | 8 | 0 | 100% |
| tests/test_rsa.py | 68 | 0 | 0 | 6 | 0 | 100% |
| tiraRSA/\_\_init__.py | 0 | 0 | 0 | 0 | 0 | 100% |
| tiraRSA/mathfuncs/\_\_init__.py | 0 | 0 | 0 | 0 | 0 | 100% |
| tiraRSA/mathfuncs/eulerfunc.py | 16 | 0 | 0 | 4 | 0 | 100% |
| tiraRSA/mathfuncs/factor.py | 7 | 0 | 0 | 2 | 0 | 100% |
| tiraRSA/primes/\_\_init__.py | 0 | 0 | 0 | 0 | 0 | 100% |
| tiraRSA/primes/prandom.py | 27 | 0 | 0 | 14 | 0 | 100% |
| tiraRSA/rsa/\_\_init__.py | 0 | 0 | 0 | 0 | 0 | 100% |
| tiraRSA/rsa/rsa_interface.py | 36 | 0 | 0 | 16 | 0 | 100% |
| tiraRSA/rsa/rsamath.py | 14 | 0 | 0 | 0 | 0 | 100% |
| Total | 218 | 0 | 0 | 54 | 0 | 100% |

## Correctness

Testing for this project is focused on correctness testing, as performance testing or comparative testing would not be very interesting. A range of tests has been done for testing that the algorithms in the program produce expected output. The sources for expected outputs are listed with the test. Primary sources for mathematical data are Wolfram Alpha and Mathematica.

### RSA interface

The interface has 2 sets of functions which are important to test: The functions which connect the project together to encrypt and decrypt files, namely `encrypt_string` and `decrypt_to_string`, and the functions which are used for converting text into numbers and back.

The encryption functions are tested through testing reversibility: First some input is encrypted, then decrypted, then we check that the output is the same as the input. This test is done with various inputs. This is a very simple test, but an effective one; Any fault in the algorithms will with near certanty cause these tests to fail, as the mathematical properties required for the process to be reversible are not fufilled. While these tests do not gurantee that the encryption is successful, the chances of finding through error a equally valid process are extremely slim, so these tests alone make it probable that the program is functioning correctly. Conversely, if these tests fail the program is with assurance broken.

The encryption functions are tested using keys generated by the program.

The conversion functions are tested through being given a variety of inputs, and checking the outputs are correct. As these are just helper functions and not mathematically interesting, we can consider these to be simple unit tests, where we just check that the outputs 'look' correct.

### RSA math

The math component of the RSA subpackage has the mathematical implementations of encryption, decryption and key generation. Encryption and decryption are implemented rather directly as large number operations from the standard library, so they are tested with a few tests making sure the math operations are producing the outputs expected, with correct numbers from other trusted math programs. 

### Mathfuncs

The functions in mathfuncs are reimplementations of a variety of well known algorithms. These algorithms correctness is tested with a variety of inputs, and correct answers are from trusted math programs. Testing is effective and rather simple in these cases.

The test most of note is for the defactorization algorithm. As removing powers of 2 from a input is rather strange, there isn't a pre-existing solution, so for testing it the correct answers for small numbers were calculated by hand, and for a big value we test reversibility, that recomposing the number returns the input.

### Prime generation (primes)

This subpackage contains testing for primes and random prime generation.

Testing if a number is prime is tested by testing that a long list of prime numbers all return that they are prime, and that a long list of composites all return that they are composite.

Prime number generation is difficult to test, as the output is intentionally random. It is tested by using the prime checking function and checking if the outputs are prime. This means these tests are only valid if the tests for the prime checking function pass. 


## Repeatability

Instructions for repeating the tests can be found in the [User Guide](https://github.com/KyperCT/tiralabraRSA/blob/main/documentation/User%20guide.md)

## Hey, where are the visualizations of tests?

I couldn't come up with a way to visualize these tests, sorry.
