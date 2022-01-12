# NMEC: 
# NOME: 

def printStocks(stocks):
	for i in range(len(stocks)):
		v = stocks[i][3]/stocks[i][2]*100-100
		print("{:8s} {:12s} {:>10.2f} {:>10.2f} {:>10d} {:>6.1f}%".format(stocks[i][0], stocks[i][1], stocks[i][2], stocks[i][3], stocks[i][4], v))

def load(filename):
	lst = []
	with open(filename) as fin:
		for line in fin:
			line = fin.readline().split()
			line = list(line)
			line[2] = float(line[2])
			line[3] = float(line[3])
			line[4] = int(line[4])
			line = tuple(line)
			lst.append(line)
	return lst

def main():
	# Cada tuplo = (empresa, cidade, abertura, fecho, volume)
	stocks = [
        ('INTC', 'London', 34.249, 34.451, 1792860),
        ('TSLA', 'London', 221.33, 229.63, 398520),
        ('EA', 'Paris', 72.63, 68.98, 1189510),
        ('INTC', 'Tokyo', 33.22001, 34.28999, 4509110),
        ('TSLA', 'Paris', 217.35, 217.75, 252500),
        ('ATML', 'Frankfurt', 8.23, 8.36, 810440),
        ]
	
	print("\na)")
	printStocks(stocks)
	
	print("\nb)")
	stocks2 = sorted(stocks, key=lambda s: (s[0], -s[4]))
	printStocks(stocks2)
	
	print("\nc)")
	stocks3 = [x for x in stocks if x[1] == 'Paris']
	printStocks(stocks3)
	
	print("\nd)")
	stocks4 = load("stocks.txt")
	printStocks(stocks4)
	# As condições seguintes devem ser verdadeiras
	assert type(stocks4)==list
	assert type(stocks4[0])==tuple
	assert len(stocks4[0])==5
	assert type(stocks4[0][2])==float
	assert type(stocks4[0][4])==int
	print("FIM")

if __name__ == "__main__":
    main()

