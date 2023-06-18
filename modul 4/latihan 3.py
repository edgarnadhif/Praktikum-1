# mencari fpb
def menghitung_fpb(x, y):
    # memilih bilangan yang paling kecil
    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range(1, terkecil+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
    return fpb 

nilai1 = int(input("masukan bilangan pertama: "))
nilai2 = int(input("masukan bilangan kedua: "))
print("fpb = ", menghitung_fpb(nilai1, nilai2))
