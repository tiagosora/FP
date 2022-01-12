
def phrasechecker (phrase):
	phraselist = list(phrase)
	for x in range(0, len(phraselist)):
		y = len(phraselist) - (x + 1)
		if phraselist[x] != phraselist[y]:
			return False
			break
	return True



def main ():
	phrase = input("Verifique se é palíndromo... (Cuidado com as maiusculas) ")
	print(phrasechecker(phrase))


main()
