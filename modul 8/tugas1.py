# linearsearch
def linear_search(target, data):
    for i in range(len(data)):
        if str(data[i]).lower() == target.lower():
            print(f"Kendaraan {target} Berada di parkiran")
            return i
    print(f"Kendaraan {target} tidak berada di parkiran")
    return -1

data = ["R 2477 SR", "R 1234 DJ", "R 7015 LP", "R 0201 RR", "R 3304 DA", "R 2401 SK", "R 2103 RT", "R 1708 RI", "R 1111 SR", "R 4987 LH"]
target = input("Mencari kendaraan : ")
linear_search(target, data)


