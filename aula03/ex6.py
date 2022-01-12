
def main():
	 a1=float(input("a1? "))
	 a2=float(input("a2? "))
	 b1=float(input("b1? "))
	 b2=float(input("b2? "))
	 
	 x = intersects(a1,b1,a2,b2)
	 print (x)

def intersects(a1,b1,a2,b2):
	return  b1<a2 or b2<a1)
		
main()
