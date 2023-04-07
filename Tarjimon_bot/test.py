def capital_letter(word):
	word = word.capitalize()
	if len(word) > 3:
		if word[1] == 'h':
			return word[0] + 'H' + word[2:]
	return word

if __name__ == '__main__':
	ism = input("Ismi:\n>>>")
	print(capital_letter(ism))