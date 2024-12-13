#!/usr/bin/python3
"""prime"""


def isWinner(x, nums):
    """i know your underwear color"""
    ben = 0
    maria = 0
    prm_num = 0
    for i in nums:
        if i == 1:
            ben = ben + 1
            continue
        for j in range(2, i + 1):
            for y in range(2, (j // 2) + 1):
                if j % y == 0:
                    break
            else:
                prm_num = prm_num + 1
        if prm_num % 2 == 0:
            ben = ben + 1
        else:
            maria = maria + 1
        prm_num = 0
    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    else:
        return None
