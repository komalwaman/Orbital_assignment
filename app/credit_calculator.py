import re
from .utils import is_palindrome, get_words

def calculate_credits(text: str) -> float:
    """
    Calculates the number of credits for a given text message according to business rules.

    Rules include:
    - base cost(1.0)
    - character-based cost
    - word length multipliers
    - vowel bonuses
    - unique word bonus
    - length penalty
    - final palindrome multiplier
    """
    base_cost = 1.0
    char_cost = 0.05 * len(text)

    words = get_words(text)
    word_cost = 0.0

    for word in words:
        if len(word) <= 3:
            # For words of 1-3 characters: Add 0.1 credits per word.
            word_cost += 0.1
        elif 4 <= len(word) <= 7:
            # For words of 4-7 characters: Add 0.2 credits per word.
            word_cost += 0.2
        else:
            # For words of 8+ characters: Add 0.3 credits per word.
            word_cost += 0.3

    third_vowel_cost = calculate_third_vowel_credits(text)

    # If the message length exceeds 100 characters, add a penalty of 5 credits.
    length_penalty = 5.0 if len(text) > 100 else 0.0
    # If all words in the message are unique (case-sensitive), subtract 2 credits from the total cost (remember the minimum cost should still be 1 credit).
    unique_word_bonus = -2.0 if len(words) == len(set(words)) else 0.0

    breakpoint()
    total = base_cost + char_cost + word_cost + third_vowel_cost + length_penalty + unique_word_bonus
    total = max(total, 1.0)
    breakpoint()

    if is_palindrome(text):
        total *= 2
    breakpoint()

    return total

def calculate_third_vowel_credits(text: str) -> float:
    # Calculate additional credits for vowels found at every third character position in the input text.
    # Positions checked are 3rd, 6th, 9th, and so on (1-based indexing).
    # Both uppercase and lowercase vowels (a, e, i, o, u) count.
    # Each such vowel adds 0.3 credits to the total.
    vowels = 'aeiou'
    third_vowel_credits = 0.0
    for position, char in enumerate(text, start=1):
        if position % 3 == 0 and char.lower() in vowels:
            third_vowel_credits += 0.3
    return third_vowel_credits