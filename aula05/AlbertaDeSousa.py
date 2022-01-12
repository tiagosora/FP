
def countDigits(insert):
	contagem = 0
	for n in range(len(insert)):
		if insert[n].isdigit():
			contagem += 1
	return (contagem)

def main():
	insert = input("Escreve... ")
	contagem = countDigits(insert)
	print ("A sua frase tem ",contagem," digitos.")
	main ()

main()
