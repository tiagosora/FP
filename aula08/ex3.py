
with open("names.txt") as fin:
	dic = {}
	for line in fin:
		line = fin.readline().split()
		if len(line) > 2:
			if line[-1] not in dic.keys():
				dic[line[-1]] = [line[0]]
			else:
				dic[line[-1]].append(line[0])
	print(dic)

