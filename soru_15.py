#beş basamaklı asal sayıları yazdıran program
bolen=1
for j in range(2,10000):
    bolen=1
    for i in range(2,j):
        if j%i==0:
            bolen+=1

    if bolen==1:
        print(j)
    
    


    

    

    
        
            

    
