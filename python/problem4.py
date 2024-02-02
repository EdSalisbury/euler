#!/usr/bin/env python

"""
Project Euler
Ed Salisbury <ed.salisbury+git@gmail.com>
GitHub: https://github.com/EdSalisbury
Written: 2024/02/02

Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 
9009=91*99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(val):
    return val == val[::-1]

def __main__():
    max_product = 0
    for i in range(100,1000):
        for j in range(i,1000):
            product = i * j
            if product > max_product and is_palindrome(str(product)):
                max_product = product
    print(f"The largest palindrome made from the product of two 3-digit numbers is: {max_product}")

if __name__ == "__main__":
    __main__()


