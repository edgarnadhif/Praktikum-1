def insertion_sort(names):
    for i in range(1, len(names)):
        key = names[i]
        j = i - 1
        while j >= 0 and names[j] > key:
            names[j + 1] = names[j]
            j -= 1
        names[j + 1] = key

def display_books(names):
    print("Daftar Buku:")
    for i, name in enumerate(names):
        print(f"Judul buku ke-{i+1}: {name}")

names = []

n = int(input("Masukkan Total buku: "))

for i in range(n):
    book_name = input(f"Masukkan judul buku ke-{i+1}: ")
    names.append(book_name)

print("<======= Urutkan ? =======>")
print("1. Ascending")
print("2. Descending")
option = int(input("Pilih: "))

if option == 1:
    insertion_sort(names)
    print("Sorting Buku Secara Ascending:")
    display_books(names)
elif option == 2:
    insertion_sort(names)
    names.reverse()
    print("Sorting Buku Secara Descending:")
    display_books(names)
else:
    print("Pilihan salah. Silakan pilih 1 atau 2.")
