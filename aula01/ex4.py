
time=int(input("Segundos?"))

time2=time//60
s=time%60
h=time2//60
m=time2%60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))
