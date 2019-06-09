def find_missing_letter(chars):
    if chars[0].islower():
        alphabet = [chr(i) for i in range(97, 123)]
        for letter in alphabet[alphabet.index(chars[0]):]:
            if letter not in chars:
                return letter[0]
    else:
        alphabet = [chr(i).upper() for i in range(97, 123)]
        for letter in alphabet[alphabet.index(chars[0]):]:
            if letter not in chars:
                return letter[0]