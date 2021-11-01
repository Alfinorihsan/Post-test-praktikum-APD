akunT = {} 
akunT["AiDahlia"] = "felisya123"

def buatBaru():
    nPengguna = input("Silahkan masukkaan nama pengguna anda : ")
    pw = input("Silahkan masukkan password anda : ")
    akunT[nPengguna] = pw

def masuk():
  coba = 0
  while coba < 3 :    
      nPengguna = input("Silahkan masukkaan nama pengguna anda : ")
      pw = input("Silahkan masukkan password anda : ")
      if akunT[nPengguna] == pw:
          print("Anda berhasil masuk, selamat Datang ")
          break
      else:
          coba += 1
          print("Mohon maaf nama pengguna atau password anda salah")
  if coba >= 3:
    print("Anda gagal mengisi 3 kali username dan password")
  print()

ulang = True
while ulang :
    print("""Selamat datang di program login 018, silahkan perhatikan pilihan di bawah : 
      1. login 
      2. Buat Akun Baru
      3. Exit
      """)
    pilPengguna = int(input("Masukkan no. pilihan yang anda inginkan = "))
    if pilPengguna == 1:
        masuk()
        print()
    elif pilPengguna == 2:
        buatBaru()
        print()
        print ("Selamat akun anda sudah terdaftar")
        print(" ")
    elif pilPengguna == 3:
        print("Terima kasih sudah menggunakan program ini, semoga harimu menyenangkan! ")
        ulang = False
    else:
        print("Anda salah memasukkan no. pilihan,harap masukkan ulang!")