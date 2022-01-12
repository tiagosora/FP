
def max2 (x, y):
	if x > y:
		m = x
	else:
		m = y
	return m

def max3 (x, y, z):
	return max2 (max2 (x, y), z)

def main():
	x=float(input("x? "))
	y=float(input("y? "))
	z=float(input("z? "))
		
	m = max3 (x, y, z)
	print ("Maximum value = ",m)

main ()

