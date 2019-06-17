def tail(digits):
    #get the tail fo the number
    return [digits[0]] + digits[1:][::-1]
    
    
def swap(digits):
    # 2017 -> 7210
    for index in range(len(digits) - 1, 0, -1):
        if digits[0] < digits[index]:
            digits[0], digits[index] = digits[index], digits[0]
            break
    return digits
    
    
def next_bigger(n):
    digits = list(str(n))
    for index in range(len(digits) - 1, 0, -1):
        if digits[index - 1] < digits[index]:
            left = digits[:index - 1]
            right = tail(swap(digits[index - 1:]))
            return int(''.join(left + right))
    return - 1