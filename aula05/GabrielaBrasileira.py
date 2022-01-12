
def shoten(nome):
	nome = list(nome)
	resultado = []
	for n in range(len(nome)):
		if nome[n].isupper():
			resultado.append(nome[n])
	resultado = "".join(resultado)
	return resultado


def main():
	nome = input("Escreva o nome... ")
	fim = str(shoten(nome))
	print (fim)
	main ()

main()
