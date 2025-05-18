# konditional statement
# if else dalam datu line
# x if kondisi else y

angka = 9
umur  = 19

# positif/negatif
print("positif" if angka > 0 else "negatif")

# ganjil/genap
print ("genap" if angka % 2 == 0 else "ganjil")

# Kelasifikasi umur
kelasifikasi_umur = "dewasa" if umur >= 18 else "anak anak"
print(kelasifikasi_umur)

# hak akses
hak_akses = input("Masukkan hak akses Anda: ").lower()
if hak_akses == "admin":
    print("Full akses")
else:
    print("Akses denied")
