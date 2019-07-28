from functools import reduce


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def oddity(n):
    return "even" if len(factors(n)) % 2 == 0 else "odd"