"""Given two strings, secret and guess, which are guaranteed to be of the same length (5 letters), determine how many characters are correct and in the exact same position."""
"""Example 1

Input: secret = "CODEX", guess = "COINS"
Output: 2
This is because the characters C and O are in the same position in both strings.

Example 2

Input: secret= "HELLO", guess = "WORLD"
Output: 1
The second L is in the same position in both strings."""

def wordle(secret, guess):
    
    correct_placements = sum(s == g for s, g in zip(secret, guess))
    
    return correct_placements
# Example usage:
# Example 1
print(f"Match Count: {wordle('CODEX', 'COINS')}") # Output: 2

# Example 2
print(f"Match Count: {wordle('HAPPY', 'WORLD')}") # Output: 0