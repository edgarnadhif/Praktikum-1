print("==Program sederhana menghitung jumlah total bilangan==")
bil = int(input("Masukkan bilangan: "))
total = 0

while bil >= 1:
    print(bil, end = ' ')
    if 1 == bil:
        print('=', end = ' ')
    else:
        print('+', end = ' ')
    total = total + bil
    bil = bil - 1
print(total)