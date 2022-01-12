
a=float(input("Cateto A?"))
b=float(input("Cateto B?"))

import math

c=math.sqrt((a**2)+(b**2))
alfarad=math.acos(a/c)
alfagr=math.degrees(alfarad)

print("Hipotenusa é ",c,"e o valor do ângulo é ",alfagr,"º")
	
