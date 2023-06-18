# if dengan satu kondisi 
# nilai = int(input("masukan bilangan bulat : "))
# if (nilai > 0 ):
#     print("bilangan", nilai, "merupakan bilangan bulat")

# if dua kondisi
# nilai = int(input("masukan bilangan : "))
# if (nilai > 0 ):
#     print("bilangan", nilai, "merupakan bilangan positif")
# else:
#     print("bilangan",nilai,"merupakan bilangan negatif")

# if tiga kondisi
# nilai = int(input("masukan bilangan : "))
# if (nilai > 0 ):
#     print("bilangan", nilai, "merupakan bilangan positif")
# elif(nilai < 0):
#     print("bilangan", nilai, " merupakan bilangan negatif")
# else:
#     print("anda memasukan bilangan 0")

# suhu 
# suhu = int(input("masukan suhu : "))
# if(suhu <= 0):
#     print("pada suhu",suhu,"derajat celcius,air akan berwujud es")
# elif(suhu > 0 & suhu < 100):
#     print("pada suhu",suhu,"derajat celcius,air akan berwujud air")
# else:
#     print("pada suhu",suhu,"derajat celcius,air akan berwujud gas")

# print("===========INPUT==========")
# nama = input("Nama: ")
# jk = input("Jenis Kelamin (L/P): ")
# agama = int(input("Agama: "))
# # 1=Islam, 2=Protestan, 3=Katolik, 4=Hindu, 5=Budha
# if(agama==1):
#     agama = "Islam"
# elif(agama==2):
#     agama = "Protestan"
# elif(agama==3):
#     agama = "Katolik"
# elif(agama==4):
#     agama = "Hindu"
# elif(agama==5):
#     agama = "Budha"
# else:
#     agama = "Agama tidak ditemukan"
# print("==========OUTPUT========")
# print("Nama: ",nama)
# print("Jenis Kelamin: ",jk)
# print("Agama: ",agama)

# panggilan berdasarkan status

gender = input("Perempuan atau laki-laki ? (L/P): ")
if(gender == 'L'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Bapak!")
    elif(status == 'N'):
        print("Hallo Mas!")
    else:
        print("Tidak ada dalam pilihan")
elif(gender == 'P'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Ibu!")
    elif(status == 'N'):
        print("Hallo Mba!")
    else:
        print("Tidak ada dalam pilihan")
else:
    print("Tidak ada dalam pilihan")



















