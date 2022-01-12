lst = []

def med(lst):
	s = 0
	for n in range(len(lst)):
		s+=lst[n]
	y = len(lst)
	med = s/y
	return (med)

def countLower(lst, v):
	z=0
	for n in range(len(lst)):
		if v > lst[n]:
			z+=1
	return (z)

def inputFloatList():
	x = 0
	while x != "":
		x = input("Number? ")
		if x != "":
			x = float(x)
			lst.append(x)
	return (lst)

def main():
	inputFloatList()
	v=med(lst)
	z=countLower(lst, v)
	print ("média: ",v," numeros inferiores: ", z)
	main ()

main ()
