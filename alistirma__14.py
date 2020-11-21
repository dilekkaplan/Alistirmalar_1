liste=[]
for i in range(2,60606):
    for j in range(i,60606):
        if i*j==1212:
            fark=abs(j-i)
            liste.append(fark)
            print(max(liste))



            
            
            
            

            


