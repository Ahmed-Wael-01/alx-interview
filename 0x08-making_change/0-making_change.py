#!/usr/bin/python3
"""calc the change"""


def makeChange(coins, total):
    """function to determine the number of coins in a change"""
    if total <= 0:
        return 0

    remain = total
    i = 0
    num = 0
    coins.sort(reverse=True)
    while remain and i < len(coins):
        if remain >= coins[i]:
            remain = remain - coins[i]
            num = num + 1
        else:
            i = i + 1
    if remain == 0:
        return num
    else:
        return -1
