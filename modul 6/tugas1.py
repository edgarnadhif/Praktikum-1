# menggunakan procedure
bilangan = int(input("Masukan Bilangan :"))
def hitung(bilangan):
    if bilangan == 0:
        print("adalah bilangan 0")
    else:
        if bilangan %2 == 0:
            print("adalah bilangan genap") 
        else:
            print("adalah bilangan ganjil")
    
hitung(bilangan)    

# menggunakan function
def hitung(bil):
    if bil == 0:
        return "Adalah bilangan 0"
    else : 
        if bil %2 == 0:
            return "Adalah bilangan genap"
        else :
            return "Adalah bilangan ganjil"
bil = int(input("masukan bilangan :"))
hasil = hitung (bil)
print(hasil)        


