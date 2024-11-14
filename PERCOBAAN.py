print("SELAMAT DATANG DI TEST CODINGAN SAYA TENTANG SOALAN")
print("APAKAH KAMU TIDAK KEBEERATAN MENJADI SEORANG TESTIMONI?")

print("HARAP NYALAKAN CAPSLOCKNYA")
jawabanmu = input("YA/TIDAK: ")
if jawabanmu == "YA":
       print("THANK YOU")
else:
    print("MAAF TELAH MENGGANGGU WAKTUNYA")
    exit("PILIHANNYA HANYA ADA YA DAN TIDAK")

print("SILAHKAN LENGKAPI DATA DIRI ANDA")

nama = input("masukan NAMA anda: ")
nim = int(input("masukan NIM anda: "))
prodi = input("masukan PRODI anda: ")
fakultas = input("masukan FAKULTAS anda: ")
tahun_ajaran = input("masukan TAHUN AJARAN anda: ")
asal_kampus = input("masukan NAMA KAMPUS anda: ")

print("TERIMA KASIH TELAH MENGISI DATA DIRI ANDA")

print("INILAH RUMUS TENTANG LUAS DAN KELILING PERSEGI DAN PERSEGI PANJANG")
print("BAHAN UNTUK MENCARI LUAS DAN KELILING PERSEGI ADALAH (sisi). CARA MENCARI LUAS PERSEGI ADALAH (sisiXsisi). DAN UNTUK MENCARI KELILING PERSEGI ADALAH (4Xsisi)")
print("SEDANGKAN BAHAN UNTUK MENCARI LUAS DAN KELILING PERSEGI PANJANG ADALAH (panjang dan lebar). CARA MECARI LUAS PERSEGI PANJANG ADALAH (panjangXlebar) DAN UNTUK MENCARI KELILING PERSEGI PANJANG ADALAH (2X(panjang+lebar))")
print("CONTOH SOAL")



panjang = int(input("Masukan panjang: "))
lebar =  int(input("Masukan lebar: "))
sisi = int(input("Masukan sisi: "))

Luas_Persegi_Panjang = panjang*lebar
Keliling_Persegi_Panjang = 2*(panjang+lebar)
Luas_Persegi = sisi*sisi
Keliling_Persegi = 4*sisi

print("Luas Persegi Panjang = ",panjang, "X", lebar, "=",Luas_Persegi_Panjang)
print("Keliling Persegi Panjang = ","2 X (",panjang,"+",lebar,") =",Keliling_Persegi_Panjang)
print("Luas Persegi = ",sisi, "X", sisi, "=",Luas_Persegi)
print("Keliling Persegi = ","4 x",sisi,"=",Keliling_Persegi)
