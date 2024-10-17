#!/usr/bin/python3
"""Module contains isWinner function"""

def isWinner(x, nums):
    """
    Determines the winner of the prime game for x rounds.
    
    Args:
        x (int): Number of rounds
        nums (list): Array of n for each round
        
    Returns:
        str: Name of winner (Maria/Ben) or None if it cannot be determined
    """
    if not nums or x < 1:
        return None
        
    def get_primes_up_to(n):
        """Generate prime numbers up to n using Sieve of Eratosthenes"""
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
                    
        return [i for i in range(2, n + 1) if sieve[i]]
        
    def play_round(n):
        """
        Simulates a single round of the game.
        Returns True if Maria wins, False if Ben wins.
        """
        if n < 2:
            return False  
            
        primes = get_primes_up_to(n)
        return len(primes) % 2 == 1
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_round(n):
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
