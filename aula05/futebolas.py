
equipas = []

def makematches(equipas):
	matches = []
	for n and k in range(len(equipas)):
		if n != k:
			novamatch=[equipas[n],equipas[k]]
			matches.append(novamatch)
	return matches

def main():
	nova = "Start"
	while nova != "":
		nova = input("Adicione uma equipa. ")
		if nova != "":
			equipas.append(nova)
	matches = makematches(equipas)
	print(matches)

main()
