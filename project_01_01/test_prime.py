#!/usr/bin/env python3
"""
Prime checker using gmpy2 for big integers.
Takes hex string input in the format: (h_0*16^0 + h_1*16^1 + ... + h_k*16^k)
where h_0 is the first character in the hex string.
"""

import sys
import gmpy2


def hex_to_int_unusual_format(hex_string):
    """
    Convert hex string to integer using the unusual format from the task description.
    Format: (h_0*16^0 + h_1*16^1 + ... + h_k*16^k)
    where h_0 is the FIRST character (leftmost).
    
    Example: "B5" = B*16^0 + 5*16^1 = 11*1 + 5*16 = 11 + 80 = 91
    """
    hex_string = hex_string.strip().upper()
    
    if not hex_string:
        return 0
    
    result = 0
    for i, char in enumerate(hex_string):
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            continue  # Skip invalid characters
        
        result += digit * (16 ** i)
    
    return result


def is_probably_prime(n, iterations=25):
    """
    Check if n is probably prime using gmpy2.
    
    Args:
        n: Integer to test
        iterations: Number of Miller-Rabin iterations (default 25)
    
    Returns:
        True if n is probably prime, False if composite
    """
    if n < 2:
        return False
    
    # Convert to gmpy2 mpz type for efficient arithmetic
    n_mpz = gmpy2.mpz(n)
    
    # gmpy2.is_prime() performs Miller-Rabin primality test
    # Returns 2 if definitely prime (for small primes)
    # Returns 1 if probably prime
    # Returns 0 if composite
    result = gmpy2.is_prime(n_mpz, iterations)
    
    return result > 0


def main():
    if len(sys.argv) == 3:
        # File mode: ./test_prime.py input.txt output.txt
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        
        with open(input_file, 'r') as f:
            hex_string = f.read().strip()
        
        n = hex_to_int_unusual_format(hex_string)
        is_prime = is_probably_prime(n)
        
        with open(output_file, 'w') as f:
            f.write('1\n' if is_prime else '0\n')
    
    else:
        # stdin mode: cat input.txt | ./test_prime.py
        hex_string = sys.stdin.read().strip()
        n = hex_to_int_unusual_format(hex_string)
        is_prime = is_probably_prime(n)
        
        print('1' if is_prime else '0')


if __name__ == '__main__':
    main()
