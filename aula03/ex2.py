
def calc(x):
	y = (x**2)+(2*x)+3
	return y

def main():
	
	x = int(input("x? "))
	y = calc(x)
	
	print("p(x) = ",y)
	
main()
