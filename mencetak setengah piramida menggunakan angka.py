# Program untuk mencetak setengah piramida a menggunakan angka

X = int(input("Masukan nilai X : "))

for i in range(X):
    for j in range(i+1):
        print(j+1, end=" ")
    print(" ")