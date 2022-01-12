def primesUpTo(n):
	lista = []
	for c in range(n + 1):
		lista.append(c)
	lista.remove(0)
	lista.remove(1)
	print(lista)
	for o in range(len(lista)-1):
		m = 2
		while m <= lista[o]/2:
			if lista[o] % m == 0:
				print(lista[o])
				lista.remove(lista[o])
				break
			else:
				m += 1
	return(lista)

def main():
	n=int(input("n? "))
	lst=primesUpTo(n)
	
	print(lst)

main()
