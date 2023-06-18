# program sederhana menghitung pangkat 
print("Program sederhana mencari pangkat")
bilangan = int(input("Masukan bilangan :"))
pencacah = int(input("masukan pencacah :"))
hasil = 1

for i in range(pencacah):
    hasil *= bilangan
    print(hasil)
