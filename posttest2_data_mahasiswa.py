isi_ulang = "y"
while isi_ulang == "y":

    print("                                     DATA MAHASISWA                                 ")
    print(" ")
    nama = str(input("SILAHKAN MASUKKAN NAMA ANDA : "))
    nim = int(input("SILAHKAN MASUKKAN NIM ANDA : "))
    umur = int(input("SILAHKAN MASUKKAN UMUR ANDA (*Harap untuk hanya memasukkan angka): "))
    asalsekolah = str(input("SILAHKAN MASUKKAN ASAL SEKOLAH ANDA : "))
    nilairaport = float(input("SILAHKAN MASUKKAN RATA-RATA NILAI RAPORT ANDA (*Harap gunakan '.' untuk mengganti ',') : "))

    Data_maha=[]
    Data_maha.append(nama) 
    Data_maha.append(nim)
    Data_maha.append(umur)
    Data_maha.append(asalsekolah)
    Data_maha.append(nilairaport)
    print(" ")
    print("                DATA MAHASISWA          ")
    print (" ")
    print(f"Nama                   : {Data_maha[0]}")
    print(f"NIM                    : {Data_maha[1]}")
    print(f"Umur                   : {Data_maha[2]} Tahun")
    print(f"Asal Sekolah           : {Data_maha[3]}")
    print(f"Rata-rata nilai raport : {Data_maha[4]}")
    print(" ")
    isi_ulang = str(input("INGIN MENGISI DATA? (y/t) : "))
print("TERIMA KASIH MENGISI DATA, SEMOGA HARIMU MENYENANGKAN")
