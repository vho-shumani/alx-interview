#!/usr/bin/python3
"""0-prime_game.py"""


def isWinner(x, nums):
    """Return: name of the player that won the most rounds"""

    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    def play_game(n):
        remaining = set(range(1, n + 1))
        moves = 0

        for p in range(2, n + 1):
            if primes[p] and p in remaining:
                moves += 1
                remaining -= set(range(p, n + 1, p))

        return "Maria" if moves % 2 == 1 else "Ben"

    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
