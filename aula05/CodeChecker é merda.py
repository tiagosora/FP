def evenThenOdd(s):
	pares = []
	impares = []
	if len(s) == 1:
		pares.append(s[0])
	else:
		for n in range(0, int(len(s)//2)):
			pares.append(s[int(2*n)])
			impares.append(s[int(2*n+1)])
	return("".join(pares + impares))
