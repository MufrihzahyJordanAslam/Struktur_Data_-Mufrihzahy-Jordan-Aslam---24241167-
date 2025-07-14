# ============================
# Final Project UAS 
# Nama Kelompok :
# Mufrihzahy Jordan Aslam (24241167)
# Lalu Nabel Alawy (24241160)
# ============================

def meet1():
    print("\n== Meet 1: Perbandingan Boolean ==")
    a = 24  # 2 digit NIM pertama
    b = 67  # 2 digit NIM terakhir

    print("a =", a)
    print("b =", b)

    print("a < b:", a < b)
    print("a > b:", a > b)
    print("a >= b:", a >= b)
    print("a <= b:", a <= b)
    print("a != b:", a != b)
    print("not a:", not a)
    print("not b:", not b)

def meet2():
    print("\n== Meet 2: Operasi Logika ==")

    x = True
    y = False

    print("x AND y =", x and y)
    print("x OR y  =", x or y)
    print("x XOR y =", x != y)
    print("NOT x   =", not x)

def meet3_4():
    print("\n== Meet 3-4: Hitung Luas Persegi / Segitiga ==")
    pilihan = input("Mau hitung apa? (persegi/segitiga): ").lower()

    if pilihan == "persegi":
        p = int(input("Masukkan panjang: "))
        l = int(input("Masukkan lebar: "))
        luas = p * l
        print("Luas persegi =", luas)
    elif pilihan == "segitiga":
        a = int(input("Masukkan alas: "))
        t = int(input("Masukkan tinggi: "))
        luas = 0.5 * a * t
        print("Luas segitiga =", luas)
    else:
        print("Pilihan nggak ada!")

def meet5():
    print("\n== Meet 5: Kalkulator Sederhana ==")
    opr = input("Operasi? (+, -, x, :): ")
    try:
        x = float(input("Masukkan angka pertama: "))
        y = float(input("Masukkan angka kedua: "))

        if opr == "+":
            print("Hasil =", x + y)
        elif opr == "-":
            print("Hasil =", x - y)
        elif opr == "x":
            print("Hasil =", x * y)
        elif opr == ":":
            print("Hasil =", x / y if y != 0 else "Tidak bisa dibagi 0")
        else:
            print("Operasi nggak dikenal.")
    except:
        print("Input harus angka ya!")

def meet6():
    print("\n== Meet 6: If Else Satu Baris ==")
    angka = 9
    umur = 19

    print("Angka positif" if angka > 0 else "Angka negatif")
    print("Angka genap" if angka % 2 == 0 else "Angka ganjil")
    print("Umur:", "Dewasa" if umur >= 18 else "Anak-anak")

    akses = input("Masukkan hak akses: ").lower()
    print("Full akses" if akses == "admin" else "Akses ditolak")

def meet7():
    print("\n== Meet 7: Cek Password ==")
    pw = input("Masukkan password: ")
    if len(pw) < 8:
        print("Karakter kurang (minimal 8)")
    else:
        print("Password aman")

def meet8():
    print("\n== Meet 8: Index String ==")
    number = "1234567890"
    print("Data terakhir :", number[-1])
    print("Data pertama  :", number[0])
    print("Data ke-3 s/d ke-6:", number[2:6])

def meet9_10():
    print("\n== Meet 9-10: Split Nama Domain ==")
    domain = input("Masukkan domain (contoh: jordan.com): ")

    if "." in domain:
        bagian = domain.split(".")
        print("Nama domain   =", bagian[0])
        print("Ekstensi      =", bagian[1])
    else:
        print("Format domain salah!")

def menu():
    print("\n========= Final Project =========")
    print("Nama Kelompok :")
    print("Mufrihzahy Jordan Aslam  (24241167)")
    print("Lalu Nabel Alawy (24241160)")
    print("=================================")
    print("1. Meet 1 - Boolean")
    print("2. Meet 2 - Logika")
    print("3. Meet 3-4 - Luas Bangun")
    print("4. Meet 5 - Kalkulator")
    print("5. Meet 6 - If Else 1 Baris")
    print("6. Meet 7 - Cek Password")
    print("7. Meet 8 - Index String")
    print("8. Meet 9-10 - Split Domain")
    print("0. Keluar")

while True:
    menu()
    try:
        pilih = int(input("Pilih nomor program: "))
        if pilih == 1:
            meet1()
        elif pilih == 2:
            meet2()
        elif pilih == 3:
            meet3_4()
        elif pilih == 4:
            meet5()
        elif pilih == 5:
            meet6()
        elif pilih == 6:
            meet7()
        elif pilih == 7:
            meet8()
        elif pilih == 8:
            meet9_10()
        elif pilih == 0:
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Nomor nggak ada di menu.")
    except:
        print("Masukkan angka saja ya.")