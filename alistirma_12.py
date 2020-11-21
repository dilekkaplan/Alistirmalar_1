
for i in range(1,2005):
    birlerbas= i%10
    onlarbas=(i//10)%10
    yüzlerbas=(i//100)%10
    binlerbas=(i//1000)

    if (birlerbas+onlarbas+yüzlerbas+binlerbas)==2005-i:
        print(i)

