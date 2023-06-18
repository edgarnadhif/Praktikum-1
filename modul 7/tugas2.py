def selection_sort(nama):
    n = len(nama)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nama[j] < nama[min_index]:
                min_index = j
        nama [i], nama [min_index] = nama[min_index], nama[i]

nama = ["Zhafira", "Nirmala", "Aksara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]
print(f"Nama sebelum diurutkan:{nama}")
selection_sort(nama)
print(f"Nama setelah diurutkan:{nama}")
