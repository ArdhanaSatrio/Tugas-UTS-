# Contoh 10: Segitiga Floyd

X = int(input("Masukan nilai X: "))
number = 1

for i in range(1, X+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()