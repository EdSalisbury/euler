#!/usr/bin/env python

"""
Project Euler
Ed Salisbury <ed.salisbury+git@gmail.com>
GitHub: https://github.com/EdSalisbury
Written: 2014/01/22
Last Modified: 2024/01/25

Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def main(max_num):
    sum = 0
    for i in range(0, max_num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return(sum)

if __name__ == "__main__":
    sum = main(1000)
    print (f"The sum of all the multiples of 3 or 5 below 1000 is: {sum}")
    