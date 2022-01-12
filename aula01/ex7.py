
x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

import math

dx=abs(x1-x2)
dy=abs(y1-y2)
d=math.sqrt((dx**2)+(dy**2))

print("A distancia entre esses dois pontos é",d)
