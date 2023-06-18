# i = 0
# while i < 7:
#     print("halo ges")
#     i += 1

# Perulangan increment:
# a = 1
# b = 10
# while a<b:
#     print("step ke-",a)
#     a += 1

# Perulangan decrement
# a = 10
# b = 0
# while a > b :
#     print("waktu bermain anda tersisa", a, "menit")
#     a-=1

# Contoh break pada perulangan while:
# a=0 
# while True:
#     print("step ke-",a,"!")
#     a += 1
#     if a == 7:
#         print("step ke-", a,"dihentikan")
#         break

# Contoh continue pada perulangan while:
angka = ['1','2','3','4','5','6','7','8','9','10']
# skip jika i adalah bilangan genap 
# dan i lebih dari 0 
i = -1 
while i < len(angka):
    i += 1
    if i % 2 == 0 and i > 0:
        print('skip')
        continue

    # tidak dieksekusi ketika continue dipanggil 
    print(angka[i])

