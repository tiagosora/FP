
# NMEC: 
# NOME: 

# Complete...

def arranjos(n,k):
	if k < 1:
		return(1)
	else:
		return(n*arranjos(n-1,k-1))

def main():
	n = int(input("n? "))
	k = int(input("k? "))
	print(arranjos(n,k))

if __name__ == "__main__":
    main()
