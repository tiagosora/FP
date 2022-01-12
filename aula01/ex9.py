
t1=24720
print("Saiu de casa às 06:52:00")

vpasso=float(input("Ritmo a passo (min/km)?"))
vtreino=float(input("Ritmo a correr (min/km)?"))

t2=vpasso*60
t3=3*vtreino*60
t4=4*vpasso*60

tf=int(t1+t2+t3+t4)
tf2=tf//60
s=tf%60
h=tf2//60
m=tf2%60

print("Chegará a casa às ""{:02d}:{:02d}:{:02d}".format(h, m, s))
