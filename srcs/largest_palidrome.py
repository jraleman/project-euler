#!/usr/bin/python
# -*- coding: utf-8 -*-

"""largest_palidrome_product.py

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
993 * 913 = 906609
"""
__author__ = "jraleman"
__email__ = "jraleman@bendiburg.com"
__date__ = "2017-27-03"

# Find the largest palidrome product.
def largest_palidrome_product(digits):
    palidrome = 0
    return palidrome


def isPalindrome(num):
    return str(num) == str(num)[::-1]
def largest(bot, top):
    z = 0
    for x in range(top, bot, -1):
        for y in range(top,bot, -1):
            if isPalindrome(x*y):
                if x*y > z:
                    z = x*y
    return z
print largest(100,999)


# Prints problem title.
print ("\nProblem 4: Largest palidrome product")

# Asks for user input (an integer).
# On error, shows a message to the user.
try:
    nbr1 = int(raw_input("Enter first number: "))
    nbr2 = int(raw_input("Enter second number: "))
    print "The largest palidrome made from", nbr1, "and" nbr2, "is", \
           largest_palidrome_product(number1, number2, max_value)
except ValueError:
    print ("Enter an integer, please! (╯°□°）╯")
except:
    pass
