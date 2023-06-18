# menghitung luas dan keliling persegi dengan prosedur
def hitungluasdankeliling(sisi):
    keliling = 4*sisi
    luas = sisi*sisi
    print("keliling persegi : %d" %keliling)
    print("luas persegi : %d" %luas)

panjang = int(input("masukan panjang sisi :"))
hitungluasdankeliling(panjang)
