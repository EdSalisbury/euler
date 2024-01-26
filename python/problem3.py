#!/usr/bin/env python

"""
Project Euler
Ed Salisbury <ed.salisbury+git@gmail.com>
GitHub: https://github.com/EdSalisbury
Written: 2024/01/25


Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

"""


def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

def pollard_rho(n):
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n
        d = gcd(abs(x - y), n)
    if d == n:
        return None
    return d

def largest_prime_factor(n):
    d = pollard_rho(n)
    while d is not None:
        n = n // d
        d = pollard_rho(n)
    return n

def __main__():
    n = 600851475143
    d = largest_prime_factor(n)
    print(f"The largest prime factor of {n} is {d}")

if __name__ == "__main__":
    __main__()