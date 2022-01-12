# NMEC: 
# NOME: 

import random

"""
Um vagão é uma lista [mercadoria, quant] com 0<quant<=60 toneladas.
Um comboio é uma lista de vagões.
"""

# Capacidade máxima dos vagões:
Qmax = 60

# Constantes para indexar os vagões.
# Se w==['coal', 45], então w[M]=='coal' e w[Q]==45.
M,Q = 0,1

# Esta função cria um comboio aleatório (NÃO PRECISA PERCEBER).
def randomTrain(a, b=0):
    types = ["coal", "iron", "sand", "salt", "sugar", "rice"]
    n = a if a>b else random.randint(a, b)
    train = []
    for i in range(n):
        wagon = [random.choice(types), random.randint(1, Qmax)]
        train.append(wagon)
    return train


#a)
def quantityOf(t, m):
	return sum(x[1] for x in t if x[0] == m)

#b)
def unload(w, m, q):
	for v in w:
		if v[0] == m:
			qa = q - v[1]
			v[1] = v[1] - q
			q = qa
			if q < 0:
				q = 0
			if v[1] < 0:
				v[1] = 0
	for k in range(-len(w), -1):
		if w[k][1] == 0:
			w.remove(w[k]) 
	return sum(x[1] for x in w if x[0] == m)

#c)
def merchandise(t):
	return {x[0]: sum(k[1] for x[0] in t) for x in t}
	

#d)
def trainsPerMerchandise(trains):
    ...


def main():
	random.seed("abc") # Pode alterar o argumento para obter comboios distintos
	
	t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
	#t = randomTrain(5)  # descomente se quiser gerar outro comboio
	print("t:", t)
	
	print("\na)")
	print(quantityOf(t, 'rice'),    # 92
		quantityOf(t, 'iron'),    # 5
		quantityOf(t, 'coal'),    # 75
		quantityOf(t, 'salt'))    # 0
	
	print("\nb)")
	q = unload(t, 'rice', 40)
	print("unload(t, 'rice', 40) ->", q)
	print("t:", t)
	q =unload(t, 'coal', 50)
	print("unload(t, 'coal', 50) ->", q)
	print("t:", t)
	q =unload(t, 'iron', 20)
	print("unload(t, 'iron', 20) ->", q)
	print("t:", t)
	
	t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
	print("\nc)")
	print(merchandise(t))
	print("t:", t)
	
	print("\nd)")
	trains = { tid: randomTrain(1,5) for tid in ['T1', 'T2', 'T3', 'T4'] }
	print("trains:", trains)
	trainsPerM = trainsPerMerchandise(trains)
	print(trainsPerM)

####
if __name__ == "__main__":
    main()



