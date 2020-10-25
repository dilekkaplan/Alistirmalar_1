toplam= 0
toplam=float(toplam)

for  n in range(1,1000000):
    toplam=(toplam)+ 1/(n**2)    

pi=(toplam*6)**(1/2)

print(pi)
