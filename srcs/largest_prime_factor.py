#!/usr/bin/python
# -*- coding: utf-8 -*-

"""largest_prime_factor.py

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
__author__ = "jraleman"
__email__ = "jraleman@bendiburg.com"
__date__ = "2017-12-01"

# Function to find the largest prime factor of a number.
def largest_prime_factor(number):
    """
    Calculate the largest prime factor of a number.
    """
    prime_factor = 2
    while number >= prime_factor**2:
        if number % prime_factor == 0:
            number //= prime_factor
        else:
            prime_factor += 1
    return number

# Prints problem title.
print ("\nProblem 3: Largest prime factor")

# Asks for user input (an integer).
# On error, shows a message to the user.
try:
    print largest_prime_factor(int(raw_input("Insert a number to calculate the largest prime factor: ")))
except ValueError:
    print ("Enter an integer, please! (╯°□°）╯")
except:
    pass
