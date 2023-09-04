#!/usr/bin/python3


def isWinner(x, nums):
    # Define a helper function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    # Initialize the players' names and scores
    maria_score = 0
    ben_score = 0

    # Loop through each round
    for n in nums:
        maria_turn = True  # Maria always goes first in each round
        while n > 1:
            prime_found = False
            # Check for prime numbers and remove multiples
            for i in range(2, n + 1):
                if is_prime(i) and n % i == 0:
                    n -= i
                    prime_found = True
                    break
            if not prime_found:
                break  # If no prime number is found, the player loses

            # Switch turns
            maria_turn = not maria_turn

        # Update the scores based on the round winner
        if maria_turn:
            ben_score += 1
        else:
            maria_score += 1

    # Determine the overall winner
    if maria_score > ben_score:
        return "Maria"
    elif maria_score < ben_score:
        return "Ben"
    else:
        return None  # If there's a tie, return None

# Example usage:
x = 3
nums = [5, 7, 11]
winner = isWinner(x, nums)
print(f"The winner is:",{winner} winner)
