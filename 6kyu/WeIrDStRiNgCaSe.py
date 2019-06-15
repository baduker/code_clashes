def weird_case_word(word):
    return ''.join(char.upper() if index % 2 == 0 else char for index, char in enumerate(word.lower()))
    
def to_weird_case(s):
    return ' '.join(weird_case_word(word) for word in s.split())