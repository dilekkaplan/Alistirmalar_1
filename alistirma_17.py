x=input("lütfen 3 veya 4 basamaklı bir sayı giriniz: ")

if len(x)==3 and x[0]==x[2] or len(x)==4 and x[0]+x[1]==x[-1]+x[-2]:
    print(x, "palindromik bir sayıdır.")

else:
    print(x, "palindromik bir sayı değildir.")
    
