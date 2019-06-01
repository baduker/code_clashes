def name_value(my_list):
    #a list of lowercase alphabet letters
    alpha = [chr(i) for i in range(97, 123)]
    #a dictionary to map values to letters
    values = dict()
    #mapping the values
    for index, letter in enumerate(alpha):
        values[letter] = index + 1
    #list to store the sum of the letter values from a passed string
    name_values = []
    #going through the passed string and counting the letter values
    for i, j in enumerate(my_list):
        name_values.append(
          sum([values.get(k) for k in ''.join(j.split())]) * (i + 1))
        
    return name_values