def is_divisible(n, *args):
    return sum([n % k for k in args]) == 0