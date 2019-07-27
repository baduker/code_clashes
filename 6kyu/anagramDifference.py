from collections import Counter

def anagram_difference(*words):
    count_one,count_two = map(Counter, words)
    count_one.subtract(count_two)
    return sum(map(abs, count_one.values()))