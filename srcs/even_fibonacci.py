#!/usr/bin/python

"""even_fibonacci.py

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""
__author__ = "jraleman"
__email__ = "jraleman@bendiburg.com"
__date__ = "2016-12-04"

def even_fibonacci(max_value):
    fibbonacci_sum = 0;
    last_term = 1;
    current_term = 2;

    while (current_term <= max_value):
        if current_term % 2 is not 0:
            fibbonacci_sum += current_term
        next_term = last_term + current_term
        last_term = current_term
        current_term = next_term
    return fibbonacci_sum

print even_fibonacci(float(raw_input("Insert max value of fibonacci sum: ")))
