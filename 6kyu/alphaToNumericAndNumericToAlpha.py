import re

def AlphaNum_NumAlpha(s):
    alhpanums = dict()

    for index, letter in enumerate([chr(i) for i in range(97, 123)]):
        alhpanums[letter] = index + 1

    numsalpha = dict()

    for index, number in enumerate(range(1, 27)):
        numsalpha[number] = chr(96 + (index + 1))
        
    s_split = list(filter(None, re.split(r'(\d+)', s)))
    
    r = []    
    for i in s_split:
        if i.isdigit():
            r.append(numsalpha.get(int(i)))
        else:
            for j in i:
                r.append(alhpanums.get(j))
    
    return ''.join(str(char) for char in r)