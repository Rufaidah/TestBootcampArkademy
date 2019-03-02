side = int(input("Masukkan panjang sisi persegi : "))
i = 0
j = 0

if side % 2 == 0:
    print("Panjang isi harus ganjil")

else:
    # index vertical
    for i in range (side):
        # index horizontal
        for j in range (side):
            if i == ((side - 1) / 2) or j == ((side - 1) / 2):
                print("*", end='')
            else:
                print("=", end='')
        print()



