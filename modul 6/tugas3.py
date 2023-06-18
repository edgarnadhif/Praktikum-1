# kalkulator
def penjumlahan ():
    bil1 = float(input("Bilangan pertama :"))
    bil2 = float(input("Bilangan kedua :"))
    hasil = bil1+bil2
    print("Hasil penjumlahan :", hasil)

def perkalian ():
    bil1 = float(input("Bilangan pertama :"))
    bil2 = float(input("Bilangan kedua :"))
    hasil = bil1*bil2
    print("Hasil penjumlahan :", hasil)

def pembagian ():
    bil1 = float(input("Bilangan pertama :"))
    bil2 = float(input("Bilangan kedua :"))
    hasil = bil1/bil2
    print("Hasil penjumlahan :", hasil)

def pengurangan ():
    bil1 = float(input("Bilangan pertama :"))
    bil2 = float(input("Bilangan kedua :"))
    hasil = bil1-bil2
    print("Hasil penjumlahan :", hasil)

def pangkat ():
    bil1 = float(input("Bilangan pertama :"))
    bil2 = float(input("Bilangan kedua :"))
    hasil = bil1**bil2
    print("Hasil penjumlahan :", hasil)

print("KALKULATOR")
print("1. Penjumlahan")
print("2. Perkalian")
print("3. Pembagian")
print("4. Pengurangan")
print("5. Pangkat")

pilihan = input("Masukan pilihan: ")

if pilihan == '1':
    penjumlahan()
elif pilihan == '2':
    perkalian()
elif pilihan == '3':
    pembagian()
elif pilihan == '4':
    pengurangan()
elif pilihan == '5':
    pangkat()
else:
    print("Pilihan tidak valid.")