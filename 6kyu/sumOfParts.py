from itertools import accumulate
def parts_sums(l):
    return list(accumulate(reversed(l)))[::-1] + [0]