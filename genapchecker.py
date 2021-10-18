while True: 
    angka = input("Isi list angka (Integer) : ")
    angka = list(angka.split(" "))
    anyGenap = False
    isInteger = True
    for a in angka:
        try:
            if int(a)%2==0:
                anyGenap=True
        except:
            print("Input error, bukan integer")
            isInteger = False
            break
    if not isInteger:
        continue
    if anyGenap :
        print("List angka memiliki angka genap")
    else :
        print("List angka tidak memiliki angka genap")