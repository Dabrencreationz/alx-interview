#!/usr/bin/python3
"""Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determine the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing 'n' for each round.

    Returns:
        str: Name of the player who won the most rounds ('Ben', 'Maria'), or None if it's a tie.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    is_prime = [1 for _ in range(max(nums) + 1)]
    is_prime[0], is_prime[1] = 0, 0

    for i in range(2, len(is_prime)):
        if is_prime[i]:
            rm_multiples(is_prime, i)

    for i in nums:
        if sum(is_prime[0:i + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None


def rm_multiples(ls, x):
    """Remove multiples of primes."""
    for i in range(2 * x, len(ls), x):
        ls[i] = 0
print("The winner is:", winner)
