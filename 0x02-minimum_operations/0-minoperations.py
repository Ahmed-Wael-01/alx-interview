#!/usr/bin/env python3
"""calculating the minimum operations needed to result specific digit"""


def minOperations(n):
    """returns the minimum operations"""
    if n == 1:
        return 0

    primes = []
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            primes.append(i)
            n = int(n / i)
            i = 2
            continue
    primes.append(n)
    n = 0
    return sum(primes)
