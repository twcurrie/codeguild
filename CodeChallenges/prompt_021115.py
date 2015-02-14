#!/usr/bin/env python
import math

def find_primes(integer):
    # Start with an empty list:
    primes_list = []

    # Go through a range of numbers between
    # 2 and integer (skip 1 because all numbers
    # have it as a factor!)
    for number in range(2,integer):
        # Assume it is a prime
        is_prime = True
        # Compare each number to all the primes 
        # already found:
        for prime in primes_list:
            # All numbers need to be floats:
            number = float(number)
            prime = float(prime)
            if math.floor(number/prime) == number/prime:
                # A number goes into it perfectly, 
                # so..... its not a prime :-(
                is_prime = False
        if is_prime:
            primes_list.append(int(number))

    # Now add 1 back to the list!
    primes_list.insert(0,1)
    
    return primes_list

