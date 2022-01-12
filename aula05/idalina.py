
def inputFloatList():
	x = 0
	while x != "":
		x = input("Number? ")
		if x != "":
			x = float(x)
			lst.append(x)
	return (lst, x)

def countLower(lst, v):
	z=0
	for n in range(len(lst)):
		if v > lst[n]:
			z+=1
	return (z)

lst = []
def main():
	inputFloatList()
	v = int(input("v? "))
	z = countLower(lst, v)
	print (lst,z, v)

main()
