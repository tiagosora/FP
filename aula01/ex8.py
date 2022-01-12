
PF=float(input("Quanto custa o fabrico do livro (€)?"))
PC=float(input("Qual o preço de capa do livro (€)?"))
IMP=float(input("Qual é o valor do IVA (%)?"))
SPA=float(input("Qual o valor da taxa para compensar os autores (€)?"))

Lucro=((PC-SPA)/((100+IMP)/100))-PF
Estado=(PC-SPA)*(IMP/100)*500

print("Para uma tiragem de 500 exemplares, a livraria lucra ",int(Lucro*500),"€ ; o valor dos impostos coletados é ",Estado,"€ ;e a quantia de taxas reunida é ",SPA*500,"€")
