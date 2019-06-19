def paren(s):
    nesting = 0
    for char in s:
        if char == "(": nesting += 1
        elif char == ")": nesting -= 1
        if nesting < 0: return False
    return True if nesting == 0 else False