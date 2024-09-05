def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        return primes

    def play_game(n):
        primes = sieve_of_eratosthenes(n)
        remaining = set(range(1, n + 1))
        maria_turn = True
        
        while True:
            prime_choices = [num for num in remaining if primes[num]]
            if not prime_choices:
                return "Ben" if maria_turn else "Maria"
            
            choice = min(prime_choices)
            remaining -= set(range(choice, n + 1, choice))
            maria_turn = not maria_turn

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