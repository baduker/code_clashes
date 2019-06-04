def encrypt_this(text):
	encrypted = []

	for word in text.split():
		# turn string into a list
		word = list(word)

		# encode the first letter with its ascii value
		word[0] = str(ord(word[0]))

		# swap the second letter with the last one
		if len(word) > 2:
			word[1], word[-1] = word[-1], word[1]

		#append the encrypted list
		encrypted.append(''.join(word))

	return ' '.join(encrypted)