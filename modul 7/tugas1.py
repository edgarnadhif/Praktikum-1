
# Descending bubble sort
print("Indeks Prestasi Semester (IPS)")
def bubble_sort(array):
    n = len (array)
    for i in range(n):
        for j in range (n - i - 1):
            if array [j] < array[j+1]:
                array[j] , array[j+1] = array[j+1],array[j]
    return array

list_1 = [3.8, 2.9, 3.3, 4.0, 2.7]
print(f"List sebelum diurutkan : {list_1}")
bubble_sort(list_1)
print(f"List setelah diurutkan : {list_1}")