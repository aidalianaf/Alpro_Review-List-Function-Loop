listkelas = []
def cek():
    for x in range(10):
        nama = input("Masukkan Nama: ")
        if nama[0].upper() == "A" or nama[0].upper() == "I" or nama[0].upper() == "U" or nama[0].upper() == "E" or nama[0].upper() == "O":
            listkelas.append(nama)
        else :
            nama = "nah loh ditandain"
            listkelas.append(nama)

cek()
print(listkelas)