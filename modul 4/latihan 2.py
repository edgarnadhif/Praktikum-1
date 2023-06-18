# mencari bilangan genap 
print("=== Mencari Bilangan Genap ===")
max_range= int(input("masukan bilangan maximal:"))

for num in range (1, max_range + 1):

    if num % 2 == 0 :
        print(num, end=" ")