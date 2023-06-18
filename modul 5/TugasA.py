# Tugas 1
x = int(input("Masukan Jumlah kata :"))
y = []
while len(y) + 1 <= x:
    y.append(input("Masukan Kata :"))

z = input("Masukan kata yang ingin di cari : ")
for index, i in enumerate(y):
    if i == z:
        print(z, "ditemukan pada indeks ke :",index )
        break
    else:
        print("indeks tidak ditemukan")