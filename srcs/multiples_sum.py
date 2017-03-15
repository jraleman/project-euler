#!/usr/bin/python
# -*- coding: utf-8 -*-

"""multiples_sum.py

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

__author__ = "jraleman"
__email__ = "jraleman@bendiburg.com"
__date__ = "2016-12-04"

# Function to find the sum of two multiples below a certain value.
def multiples_sum(number1, number2, max_value):
    total_sum = 0
    for i in range(0, max_value):
        if (i % number1 is 0) or (i % number2 is 0):
            total_sum += i
    return total_sum

# Prints problem title.
print ("\nProblem 1: Multiples of 3 and 5")

# Asks for user input (an integer).
# On error, shows a message to the user.
try:
    number1 = int(raw_input("Enter first multiple: "))
    number2 = int(raw_input("Enter second multiple: "))
    max_value = int(raw_input("Enter the max value to evaluate to: "))
    print "The sum of all multiples of", number1, "and", number2, "below", \
        max_value, "is", multiples_sum(number1, number2, max_value)
except ValueError:
    print ("Enter an integer, please! (╯°□°）╯")
except:
    pass
