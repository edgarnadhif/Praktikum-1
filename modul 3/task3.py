# identifikasi biaya operasi 
print("Menu Hitung Biaya Operasi")
print("1. Hitung Biaya Operasi Mata")
print("2. Hitung Biaya Operasi Jantung")
pilihan = int(input("Masukan Pilihan : "))
#1 Biaya Operasi Mata, #2 Biaya Operasi Jantung

if pilihan == 1: 
    # input jenis operasi mata 
    print("Jenis penyakit mata : ")
    print("1. Katarak ")
    print("2. Plus atau minus ")
    print("3. Silinder ")
    jenis_operasi = int(input("Masukan Jenis penyakit mata"))

    # untuk mengidentifikasi biaya operasi mata
    if jenis_operasi == 1:
        biaya = 7500000
        print(f"Biaya Operasi Mata Katarak {biaya}")    
    elif jenis_operasi == 2: 
        biaya = 5000000 
        print(f"Biaya Operasi Mata Plus/Minus {biaya} ")
    elif jenis_operasi == 3:
        biaya = 4000000
        print(f"Biaya operasi Mata Silinder {biaya}")
    else: 
        print("Pilihan tidak ada")

    # untuk operasi jantung
elif pilihan == 2: 
    print("Jenis penyakit jantung :")
    print("1. Jantung Koroner ")
    print("2. Katup Jantung ")
    print("3. Otot Jantung ")
    jenis_operasi = int(input("Masukan Jenis penyakit jantung"))

    # untuk mengidentifikasi biaya operasi jantung
    if jenis_operasi == 1:
        biaya = 500000000
        print(f"Biaya Operasi Jantung Koroner: {biaya}")    
    elif jenis_operasi == 2: 
        biaya = 350000000
        print(f"Biaya Operasi Katup jantung: {biaya} ")
    elif jenis_operasi == 3:
        biaya = 450000000
        print(f"Biaya operasi Otot jantung: {biaya}")
    else: 
        print("pilihan tidak ada")

else: 
    print("pilihan tidak tersedia")

