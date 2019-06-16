from functools import reduce
def correct(s):
	rep = ("5", "S"), ("0", "O"), ("1", "I")
	return reduce(lambda x kv: x.replace(*kv), rep, s)