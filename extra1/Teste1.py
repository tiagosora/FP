import random

def segredo ():
	return ("{:04d}".format(random.randint(0,9999)))

def valida(k):
	t ="Tentativa " + str(k) + "? "
	t = input(t)
	if len(t) != 4 or not t.isdigit():
		print ("Use 4 algarismos!")
		valida(k)
	return t

def pontuacao(segredo, tentativa):
	c = 0
	e = 0
	#Algarismos na posição certa
	for n in range(len(segredo)):
		if segredo[n] == tentativa[n]:
			c += 1
	#Algarismos na posição errada
	for n in range(len(tentativa)):
		if segredo[n] == tentativa[n]:
			tentativa[n] = "N"
			segredo[n] = "N"
	for n in range(len(tentativa)):
		if tentativa[n] != segredo[n] and tentativa[n] in segredo:
			segredo[segredo.index(tentativa[n])] = "N"
			tentativa[n] = "N"
			e += 1
	#Pontuação
	l = c*10+e
	print (c, " certas, ", e, " no lugar errado,", l, " pontos.")
	return (l)

def jogo():
	#Número de tentativa
	k = 0
	p = 0
	#Processamento
	asave = segredo()
	print("Adivinhe o segredo de 4 algarismos.")
	while p != 40:
		print(asave)
		k += 1
		a = list(asave)
		b = list(valida(k))
		p = pontuacao(a, b)
	print ("Conseguiu em ", k, " tentativas.")
	

jogo()
