
def leibnizPi4(n):
	f=0
	for n in range(0, n, 1):
		f+=(((-1)**n)/(2*n+1))
	return f

def main():
	n=int(input("n? "))
	print (leibnizPi4(n))

main()
