# menghitung luas  dan keliling lingkaran(procedure)

def menghitung(jari):
    jari = float(jari)
    luas = 3.14 * jari * jari
    keliling = 2 * 3.14 * jari
    print("luas lingkaran: %f" % luas)
    print("keliling lingkaran: %f" % keliling)

p = input("masukan jari-jari: ")
menghitung(p)

# menghitung luas dan keliling lingkaran (function)
def menghitung_luas(jari):
    jari = float(jari)
    luas = 3.14 * jari* jari
    return luas

def menghitung_keliling(jari):
    jari=float(jari)
    keliling = 2 * 3.14 * jari
    return keliling

jari = input("Masukkan jari-jari: ")
print("Luas lingkaran: ", menghitung_luas(jari))
print("Keliling lingkaran: ", menghitung_keliling(jari))
