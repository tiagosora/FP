# (q * 1.4)*0.9 = q * 1.26

q=float(input("litros de combustível a abastecer? "))

paga=q*1.4

if q>=40:
	paga=q*1.26

print(paga)
