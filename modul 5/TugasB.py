# Tugas 2
a = int(input("Masukan jumlah mata kuliah : "))
b = []
u = 1
while len(b) + 1 <= a:
    b.append(float(input(f"Masukkan nilai mata kuliah ke- {u} : ")))
    u += 1

nilaitotal = sum(b)
ratarata = nilaitotal/a
urutannilai = 1

if ratarata >= 90 and ratarata < 100: 
    print("hasil predikat A dengan nilai : ")
    for i in b :
        print(f"mata kuliah ke-{urutannilai} : {i}")
        urutannilai += 1
elif ratarata >= 70 and ratarata < 90:
    print("Hasil Predikat B dengan nilai : ")
    for i in b:
        print(f"Mata kuliah ke-{urutannilai} : {i}")
        urutannilai += 1
elif ratarata >= 50 and ratarata < 70:
    print("Hasil Predikat C dengan nilai : ")
    for i in b:
        print(f"Mata kuliah ke-{urutannilai} : {i}")
        urutannilai += 1
elif ratarata >= 30 and ratarata < 50:
    print("Hasil Predikat D dengan nilai : ")
    for i in b:
        print(f"Mata kuliah ke-{urutannilai} : {i}")
        urutannilai += 1
elif ratarata >= 0 and ratarata < 30:
    print("Hasil Predikat E dengan nilai : ")
    for i in b:
        print(f"Mata kuliah ke-{urutannilai} : {i}")
        urutannilai += 1
else:
    print("Nilai tidak valid")