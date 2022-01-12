
def primesUpTo(n):
	lst0 = [2,3,5,7,11]
	lst=[]
	for i in lst0:
		if i <= n:
			lst.append(i)
	for i in range(13, n+1):
		if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 and i%11 != 0:
			lst.append(i)
	return lst

def main():
	n=int(input("n? "))
	lst=primesUpTo(n)
	
	print(lst)

main()
