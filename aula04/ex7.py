soma=0
tent=0
a=0
while a!="":
	a=input("Número Real? ")
	if a!="":
		a=float(a)
		soma+=a
		tent+=1
	else:
		med=soma/tent
		print ("A média de resultados foi ",med)
