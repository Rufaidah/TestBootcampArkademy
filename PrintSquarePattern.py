side = int(input("Masukkan panjang sisi persegi : "))
i = 0
j = 0

if side % 2 == 0:
    print("Panjang isi harus ganjil")

else:
    # row
    for i in range (side):
        # column
        for j in range (side):
            if (i == (side - 1) / 2) or (j == (side - 1) / 2) \
                    or (i | j == 0) or (i == 0 and j == side - 1)\
                    or (i == side - 1 and j == 0) or (i == side - 1 and j == side - 1):
                print("*", end='')
            else:
                print("=", end='')
        print()



