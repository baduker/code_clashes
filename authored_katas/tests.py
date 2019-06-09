import random

# My first predefined solution
def chop_it_up_author(array, delimiter):
    return ", ".join(["[{}]".format(delimiter.join(map(str,chunk))) for chunk in [array[i:i+2] for i in range(0, len(array), 2)]])

# A function generating a random, even-lenght array of positive integers
def get_random_array():
    return [random.randint(1,501) for _ in range(random.randint(0, 10)*2)]

# A function generating a random string delimiter from a preloaded list of delimiters
def get_random_delimiter():
    return random.choice([":", "-", " | ", "..", " && ", ","])

# A set of basic tests
test.describe("Basic tests")
test.assert_equals(chop_it_up([11, 22, 33, 44], ":"), '[11:22], [33:44]')
test.assert_equals(chop_it_up([182, 38, 752, 901], ":"), '[182:38], [752:901]')
test.assert_equals(chop_it_up([239, 5, 1, 13], "-"), '[239-5], [1-13]')
test.assert_equals(chop_it_up([76, 2, 33, 47, 84, 331, 84, 135], "-"), '[76-2], [33-47], [84-331], [84-135]')

# A set of 100 random tests
test.describe("Random tests")
for i in range(100):
    ra = get_random_array()
    rd = get_random_delimiter()
    test.assert_equals(chop_it_up(ra, rd), chop_it_up_author(ra, rd))