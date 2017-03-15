#!/usr/bin/python
# -*- coding: utf-8 -*-

"""project-euler.py

Calls an Euler problem (from the srcs folder) depending on the user input.
"""
__author__ = "jraleman"
__email__ = "jraleman@bendiburg.com"
__date__ = "2017-03-15"

# Import system module
import sys

# Prints usage message.
if len(sys.argv) != 2:
    print ("usage: python " + sys.argv[0] + " problem_number")
    print ("valid problem_number: 1, 2, 3")
    sys.exit(0)

# Assign the problem_number, depending on user input.
# On error, shows a message to the user.
try:
    problem_number = int(sys.argv[1])
except:
    print ("Enter a number, please! (╯°□°）╯")
    sys.exit(1)

# Select the problem number and import the specific module from srcs folder.
if problem_number == 1:
    import srcs.multiples_sum
elif problem_number == 2:
    import srcs.even_fibonacci
elif problem_number == 3:
    import srcs.largest_prime_factor
else:
    print ("Not a valid option! ¯\_(ツ)_/¯")
