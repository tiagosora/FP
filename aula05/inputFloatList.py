s = []

def inputFloatList(x):
	x = float(x)
	s.append(x)
	return (s, x)

def main():
	x = 0
	while x != "":
		x = input("Number? ")
		if x != "":
			inputFloatList(x)
	print(s)

main()
