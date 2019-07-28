def cube_odd(arr):
    for i in arr:
        if isinstance(i, str):
            return None
    
    return sum(pow(i, 3) for i in arr if i % 2 != 0)