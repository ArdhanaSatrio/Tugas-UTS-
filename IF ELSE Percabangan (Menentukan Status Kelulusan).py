nilai_ujian = float (input("masukan nilai ujian: "))
absen = int(input("masukan jumlah kehadiran: "))
if nilai_ujian >= 75 and absen >= 80:
    print("Selamat! Anda Lulus.")
else:
    print("Maaf, Anda Dinyatakan Tidak Lulus.")