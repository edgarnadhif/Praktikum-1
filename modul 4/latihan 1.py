print("====SISTEM LOGIN SEDERHANA=====")

login = 0
while login < 3:
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")

    if username == "edgar" and password == "edgar123":
        print("Selamat datang", username)
        break
    else:
        print("Login gagal!")
        login += 1

if login == 3:
    print("Login gagal! kesempatan mencoba sudah habis. silahkan hubungi admin.")
