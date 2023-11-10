# Setengah piramida terbalik menggunakan angka

X = int(input(" Masukan nilai X: "))

for i in range(X, 0,-1):
    for j in range(1, i+1):
        print("j", end=" ")
    
    print(" ")