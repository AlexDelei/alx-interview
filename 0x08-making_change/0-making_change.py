#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of this coin as possible
        count = total // coin
        num_coins += count
        total -= count * coin

    # If total is still not zero, change cannot be made
    if total != 0:
        return -1

    return num_coins
