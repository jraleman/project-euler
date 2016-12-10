#!/usr/bin/python

"""multiples_sum.py

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

__author__ = "jraleman"
__email__ = "jraleman@bendiburg.com"
__date__ = "2016-12-04"

def multiples_sum(number1, number2, max_value):
	total_sum = 0
	for i in range(0, max_value):
		if (i % number1 is 0) or (i % number2 is 0):
			total_sum += i
	return total_sum

number1 = int(raw_input("Enter a number: "))
number2 = int(raw_input("Enter another number: "))
max_value = int(raw_input("Enter the max value to evaluate to: "))

print "The sum of all multiples of", number1, "and", number2, "below", \
		max_value, "is", multiples_sum(number1, number2, max_value)
