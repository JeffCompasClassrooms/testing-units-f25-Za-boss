"""
text_utils.py

A small, testable Python utility library for text and list processing.

Created by ChatGPT (OpenAI), 2025
"""

def normalize_whitespace(text):
    """Removes leading/trailing whitespace and replaces multiple spaces with a single space."""
    return ' '.join(text.strip().split())

def is_palindrome(text):
    """Checks if a string is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def word_count(text):
    """Returns the number of words in a string."""
    return len(text.strip().split())

def most_frequent_word(text):
    """Returns the most frequent word in the text. Returns None if empty."""
    words = text.strip().split()
    if not words:
        return None
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return max(counts, key=counts.get)

def truncate(text, length):
    """Truncates the string to a specified length, adding '...' if truncation occurs."""
    if len(text) <= length:
        return text
    if length <= 3:
        return '.' * length
    return text[:length - 3] + '...'

def unique_words(text):
    """Returns a sorted list of unique words (case-sensitive)."""
    return sorted(set(text.strip().split()))

def reverse_words(text):
    """Returns a string with the words in reversed order."""
    return ' '.join(text.strip().split()[::-1])

def contains_digit(text):
    """Returns True if the text contains any digits."""
    return any(char.isdigit() for char in text)

def remove_punctuation(text):
    """Removes all punctuation from a string."""
    import string
    return ''.join(char for char in text if char not in string.punctuation)