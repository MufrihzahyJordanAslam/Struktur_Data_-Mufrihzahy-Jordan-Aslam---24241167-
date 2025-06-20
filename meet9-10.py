#Program memisahkan string nama domain 
nama_domain = input("masukan nama domain anda:")
index = nama_domain.index(".")
nama = nama_domain[:index]
domain = nama_domain[index:]

print(f"nama anda adalah = {nama}")
print(f"domain anda adalah = {domain}")






#terdapat variabel "number" yang isinya (1234567890) buatlah aplikasi untuk
#menampilkan data terakhir
#menampilkan data pertama
#menampilkan data ke3-ke6

number = "1234567890"

print("data terakhir:", number[-1])
print("data pertama:", number[0])
print("data ke 3 - ke 6:", number[2:6])