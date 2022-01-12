

def makeMatches(equipas):
	matches = []
	for k in range(len(equipas)):
		for n in range(len(equipas)):
			if n != k:
				novamatch=[equipas[n],equipas[k]]
				if [equipas[k],equipas[n]] not in matches:
					matches.append(novamatch)
	print(matches)
	return matches

def resultado(matches):
	d = {}
	for match in matches:
		t = "Resultado de " + str(match) + " ?"
		r = input(t)
		r = (r[0],r[1])
		d[tuple(match)] = r
	return d

def dataTeams(data):
	print ("ola")

def main():
	nova = "mainStart"
	equipas = []
	#carregar novas equipas
	while nova != "":
		nova = input("Adicione uma equipa. ")
		if nova != "":
			equipas.append(nova)
	#fazer matches
	matches = makeMatches(equipas)
	#fazer os resultados
	resultados = resultado(matches)
	#fazer os dados das equipas
	


if __name__ == "__main__":
    main()
