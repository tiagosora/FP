
def maximo (x, y):
	if x > y:
		m = x
	else:
		m = y
	return m

def main():
	x=float(input("x? = "))
	y=float(input("y? = "))
	
	m = maximo (x, y)
	print ("Maximum value = ",m)

main ()
