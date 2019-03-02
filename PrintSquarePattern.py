side = int(input("Masukkan panjang sisi persegi : "))
i = 0

if side % 2 == 0:
    print("Panjang isi harus ganjil")

else:
    # isi baris
    for i in range (side):
        # jumlah baris
        for i in range (side):
            print('*', end=' ')
        print()



