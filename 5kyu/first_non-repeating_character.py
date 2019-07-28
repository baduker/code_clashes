from collections import Counter


def first_non_repeating_letter(s):
    singles = Counter(s.lower())
    for char in s:
        if singles[char.lower()] == 1:
            return char
    return ""