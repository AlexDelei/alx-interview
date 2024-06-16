#!/usr/bin/python3
"""
Finding the minimum number of operations to perform
"""


def minOperations(n: int) -> int:
    """
    Calculating the minimum number of operations
    """
    if n == 0:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n]
