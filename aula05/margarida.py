
lst = []

def minmax(lst):
	mi = lst[0]
	ma = lst[0]
	for n in range(len(lst)):
		if lst[n] < mi:
			mi = lst[n]
		elif lst[n] > ma:
			ma = lst[n]
	return(ma, mi)

def inputFloatList():
	x = 0
	while x != "":
		x = input("Number? ")
		if x != "":
			x = float(x)
			lst.append(x)
	return (lst)

def main():
	lst=inputFloatList()
	x = minmax(lst)
	
	print(x)

main()
