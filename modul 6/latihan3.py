# program untuk melihat perbandingan lebih besar dan lebih kecil menggunakan prosedur.
def banding(n1,n2):
    if (n1 > n2):
        print(n1)
    elif (n1 == n2):
        print("tidak ada")
    else:
        print(n2)

bil1 = int(input("masukan bilangan 1 :"))
bil2 = int(input("masukan bilangan 2 :"))
print("bilangan yang besar adalah")
banding(bil1,bil2)