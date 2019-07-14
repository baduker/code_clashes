def power_of_two(x):
    base = 2
    if x == base:
        return True

    if x == 1:
        return True

    temp = base

    while (temp <= x):
        if temp == x:
            return True
        temp *= base

    return False