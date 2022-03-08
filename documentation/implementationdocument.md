# Implementation document

## Structure
The program is implemented as a package, which is composed of modules and subpackages. Each module provides functions. The program does not have custom classes, but it does use standard data-structures (integers, lists, strings, ect.). Each algorithm has a dedicated function, and each function is built with the principle that the output of the function is always a new object and no function changes state outside of it's own scope. 
 
There are 2 top level modules, 'main' and 'rsa', and 2 subpackages, 'mathfuncs' and 'primes'.

### Main
Main has 1 function, the main function. This function uses commandline arguments to determine what the user wants, and then executes the appropritate functions with given inputs.

### RSA
This subpackage has 2 modules, interface and math. The interface module has functions for converting strings into numbers and back, converting strings into appropriate blocks for encryption, and functions for encrypting and decrypting strings with the other functions.

The math module contains key generation, and the mathematical implementations of encrypting and decrypting integers.

### mathfuncs
This subpackage contains 2 modules, eulerfunc and factor. factor contains 1 function for de-factorizing powers of 2 from a given value. eulerfunc contains implementations of gcd, lcm and extended gcd.

### primes
This subpackage contains 1 module, prandom. This module provides functions for testing if a number is prime, and for generating random primes of spesified size.

## Time and Space complexity
We will look into the complexity of the functions for encrypting and decrypting strings, and key generation, as these are the primary functions of the program.

### Time: encryption

First, the input is divided into blocks. The block creation is a loop, which is iterated for every 30 characters in the input `O(n/30)=O(n)` . In the loop a 30 character block is collected from the input `O(30)`, appended to an output list `O(1)` and 30 characters are removed from the input `O(n)`, making the blocking `O(n)*(O(30)+O(1)+O(n))=O(n^2)`. We iterate over each block `O(n)` Each block is converted into an integer, with a function which converts each character into a number `O(1)`, normalizes each number into a 3 character string `O(3)`, and then concatanates all numbers into 1 string `O(3n)` and adds a '1' to the start `O(1)` and converts into an integer `O(n)`, making it `O(1)+O(3)+O(3n)+O(1)+O(n)=O(n)`. Each integerified block is then encrypted with modular exponentiation. Assuming python uses an efficient implementation of modular exponentiation, the compexity is `O(log(e))`, where e is from the encryption key. As the key is always ~32 bits, this is effectively `O(1)`, making the total complexity of the loop `O(n)*(O(n)+O(1))=O(n^2)`.

Encryption is thus `O(n^2)+O(n^2)=O(n^2)`

### Space: encryption

Dividing the input into blocks creates a list with the same elements divided into parts, so it's spacial complexity is `O(cn)`, where c is some constant for the extra space required by the new list containing the same data as the starting string. The conversion of each block into integers is `O(3n)`, as the process triples the character count, before converting into an integer. The encryption is a mathematical operation, which creates an output with linear spacial growth, so `O(n)`. This means the spacial complexity in it's entirety is `O(n)`.

### Time: decryption

First, each encrypted block is decrypted, which takes `O(log(e))` time (see: encryption). This e is the private exponent from the private key, ~1024 bits. As the private key could be larger for additional security, we will keep it as a variable. Each decrypted block is converted into a string by converting the integer into it's string representation `O(n)`, removing the leading 1 `O(1)`, cutting that string representation into 3 character parts `O(n)`, and converting those parts into characters `O(1)`, making the process `O(n)+O(1)+O(n)+O(1)=O(n)`. As this is done for every block, the total for these steps is `O(n)*(O(log(e))+O(n))=O(log(e)*n^2)`. The blocks are finally concatanated into 1 string `O(n)`.

The total time complexity is `O(n)+O(log(e)*n^2)=O(n+log(e)*n^2)`

### Space: decryption

TODO

### Time: Key generation

The first step in key generation is generating 2 large random primes. Generating these primes takes `O(k*b^4)` per prime, where b is the size of the prime in bits and k is the number of trials used in testing primality. We generate 2 primes, so `O(2* k*b^4)`. Most operations in the algorithm are `O(1)`, except for gcd and extended gcd, which are `O(h)` in the best case and `O(h^2)` in the worst case, where h is the number of digits in the smaller input number.

The worst case complexity would be `O(h^2*k*b^4)`. Of note however, is that the program has pre-set values for each of the variables in this complexity, making the practical complexity of the key generation constant, aka `O(1)`

### Space: Key generation

TODO

## Sources

[Python time complexity](https://wiki.python.org/moin/TimeComplexity)

[Modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation)

[Eulcidian algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)

[Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)

[Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)


