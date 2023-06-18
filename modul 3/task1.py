# task 1 Huruf Vokal dan Konsonan
huruf = str(input("Masukkan Huruf : "))
# vokal = a,i,u,e,o
# konsonan = b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z
# vokal = ['a','i','u','e','o']
if (huruf=='a' or huruf=='i' or huruf=='u' or huruf=='e' or huruf=='o'):
    print("Huruf", huruf, "Merupakan Vokal")
elif(huruf=='b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
    print("Huruf", huruf, "Merupakan konsonan")
else:
    print("Huruf", huruf, "Tidak Terdeteksi")