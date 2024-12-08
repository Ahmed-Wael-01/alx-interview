#!/usr/bin/python3
"""calculating the minimum operations needed to result specific digit"""


def minOperations(n):
    """returns the minimum operations"""
    if n < 2:
        return 0

    primes = []
    i = 2
    while i <= (n / 2):
        if n % i == 0:
            primes.append(i)
            n = int(n / i)
            i = 2
        i = i + 1
    if n != 1:
        primes.append(n)

    return sum(primes)
