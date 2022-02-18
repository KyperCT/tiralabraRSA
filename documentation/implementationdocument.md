### Implementation document

## Structure
The program is implemented as a package, which is composed of modules and subpackages. Each module provides functions. The program does not have custom classes, but it does use standard data-structures (integers, lists, strings, ect.). Each algorithm has a dedicated function, and each function is built with the principle that the output of the function is always a new object and no function changes state outside of it's own scope. 
 
There are 2 top level modules, 'main' and 'rsa', and 2 subpackages, 'mathfuncs' and 'primes'.

### Main
Main has 1 function, the main function. This function uses commandline arguments to determine what the user wants, and then executes the appropritate functions with given inputs.

### RSA
This module has top-level functions for encrypting, decrypting, converting text into integers and generating keys.

### mathfuncs
This subpackage contains 2 modules, eulerfunc and factor. factor contains 1 function for de-factorizing powers of 2 from a given value. eulerfunc contains implementations of gcd, lcm and extended gcd.

### primes
This subpackage contains 1 module, prandom. This module provides functions for testing if a number is prime, and for generating random primes of spesified size.

## Time and Space complexity

## Sources
