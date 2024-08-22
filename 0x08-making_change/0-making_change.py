#!/usr/bin/python3
"""0-making_change.py"""


def makeChange(coins, total):
    """ determine the fewest number of coins
    needed to meet a given amount total"""
    if total <= 0:
        return 0
    array = [total + 1] * (total + 1)
    array[0] = 0
    for i in range(total + 1):
        for coin in coins:
            if coin <= i:
                array[i] = min(array[i - coin] + 1, array[i])
    if array[total] > total:
        return -1
    return array[total]
