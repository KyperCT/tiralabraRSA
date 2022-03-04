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

First, the input is divided into blocks. The block creation is a loop, which is iterated for every 30 characters in the input `O(n/30)=O(n)` . In the loop a 30 character block is collected from the input `O(30)`, appended to an output list `O(1)` and 30 characters are removed from the input `O(n)`, making the blocking `O(n)*(O(30)+O(1)+O(n))=O(n^2)`. We iterate over each block `O(n)` Each block is converted into an integer, with a function which converts each character into a number `O(1)`, normalizes each number into a 3 character string `O(3)`, and then concatanates all numbers into 1 string `O(3n)` and adds a '1' to the start `O(1)` and converts into an integer `O(n)`, making it `O(1)+O(3)+O(3n)+O(1)+O(n)=O(n)`. Each integerified block is then encrypted with modular exponentiation


## Sources

[Python time complexity](https://wiki.python.org/moin/TimeComplexity)
