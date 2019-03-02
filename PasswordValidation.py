import re

pas = input("Masukkan pasword : ")
val = True
char = "[`~!@#$%^&*()_+-={}|:<>?\;',.]"

while val:
    if (len(pas) < 8):
        break
    elif not re.search("[a-z]",pas):
        break
    elif not re.search("[A-Z]", pas):
        break
    elif not re.search("[0-9]", pas):
        break
    elif not re.search(char, pas):
        break

    else:
        print("Valid Password")
        val = False
        break

if val:
    print("Not a Valid Password")


