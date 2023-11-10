total_belanja = float(input("masukan total belanja anda: "))
if  total_belanja >= 500000:
    diskon = 0.3 * total_belanja
else:
    diskon = 0
total_pembayaran = total_belanja - diskon
print("total pembayaran setelah diskon: ", total_pembayaran)