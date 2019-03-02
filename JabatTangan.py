orang = int(input("Masukkan jumlah orang : "))

counter = 1

if orang == 1:
    jabat_tangan = 0
else:
    jabat_tangan = 1
    while counter<orang-1:
        counter = counter + 1
        jabat_tangan = jabat_tangan + counter
print("Terdapat " + str(jabat_tangan) + " jabat tangan")
