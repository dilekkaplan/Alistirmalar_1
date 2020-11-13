#Girilen bir sayının asal olup olmadığını kontrol eden program.

sayi=int(input("Lutfen bir sayı giriniz:"))
asal_mi=True
bolen=2

while sayi> bolen:

    if sayi%bolen==0:
        asal_mi=False
        break
        
    if sayi%bolen!=0:
        asal_mi=True
        bolen+=1

if asal_mi==True:
    print(sayi,"bir asal sayidir.")

else:
    print(sayi,"bir asal sayi değildir.")
        


        


        


    
            
