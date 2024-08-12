#!/usr/bin/python3
"""
Prime Numbers Game
"""


def isWinner(x, nums):
    """
    Defining a winner based on the most won rounds.
    A player wins by making the most successful moves.

    Args:
        x - the number of rounds
        nums - an array of n
    Returns:
        - Name of the winner if there is; else None.
    """
    def seive(n):
        """
        Makes an array of prime numbers.

        Args:
            n - the limit of choosing the prime number
        Returns:
            An array of prime numbers
        """
        sieve = [True] * (n + 1)
        p = 2

        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False

            p += 1
        primes = [p for p in range(n + 1) if sieve[p]]
        return primes

    maria_wins, ben_wins = 0, 0

    for n in nums:
        primes = seive(n)
        round_prime_count = 0

        while primes:
            round_prime_count += 1
            prime = primes.pop(0)

            primes = [p for p in primes if p % prime != 0]

            if round_prime_count % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
