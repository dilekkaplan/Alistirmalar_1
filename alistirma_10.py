toplam=0

for n in range(10000,100000):
    n=str(n)

    if n[0]==n[1] and n[-2]== n[-1]:
        toplam=toplam+1
       
print(toplam)
