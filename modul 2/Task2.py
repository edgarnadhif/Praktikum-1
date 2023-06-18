#volume kubus
sisi = int (input("masukan sisinya: "))
volume = sisi * sisi * sisi 
print("volume : ", volume)

#volume balok 
panjang = int( input("masukan panjang: "))
lebar = int( input("masukan lebar: "))
tinggi = int( input("masukan tinggi: "))
volume = panjang*lebar*tinggi
print("volume :", volume)

#volume tabung 
phi = 3.14
jari = float (input("masukan jari-jarinya :"))
tinggi = float (input("masukan tinggi : "))
volume = phi * jari**2 * tinggi 
print("volume :", volume)

#volume bola
p = (4/3)
phi = 3.14
jari = float (input("masukan jari-jari : "))
volume = p * phi * jari**3
print("volume :" , volume)