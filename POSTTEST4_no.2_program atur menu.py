dafMenu = [
  ["Jus de mangue du Roi Allain",25000, "minuman", "001MN"],
  ["Thé à la camomille d'Afata",17000, "minuman", "002MN"],
  ["Café au lait de Lokheim",30000, "minuman", "003MN"],
  ["Le toast de Liliana",22000, "makanan", "004MK" ],
  ["Banane frite védique",20000, "makanan", "005MK"],
  ["Poulet au beurre de soja",35000, "makanan", "006MK"]
]

def pilAwal():
  print("""
 ◙◙◙◙◙◙ Selamat datang di program menu kafe Anatasya  ◙◙◙◙◙◙ 

 Silahkan piih tindakan :

1. Melihat seluruh menu yang tersedia.
2. Menambahkan menu baru yang akan segera tersedia di daftar menu.
3. Mengubah menu yang tersedia dan menggantinya.
4. menghapus menu yang tersedia dari daftar menu.
5. Keluar dari program.

note: Harap tekan "Enter" untuk melanjutkan program
  """)


def menuMenu():
  dafmak = []
  dafmin = []
  for menu in dafMenu:
    if menu[2] == "minuman":
      dafmin.append(menu)
    else:
      dafmak.append(menu)
  print(""" 
  ↂↂↂↂ  Menu yang tersedia di kafe ↂↂↂↂ
""")
  print(""" Daftar minuman yang tersedia di kafe :
            ⬇       ⬇       ⬇""")
  for nil, minuman in enumerate(dafmin):
    print(f"{nil + 1}. {minuman[0]} ~~ ◖Rp. {minuman[1]}◗ ({minuman[3]})" )
  print(""" 
  Daftar makanan yang tersedia di kafe :
           ⬇       ⬇       ⬇""")
  for nil, makanan in enumerate(dafmak):
    print(f"{nil + 1}. {makanan[0]} ~~ ◖Rp. {makanan[1]}◗ ({makanan[3]})")
  input()

def mnuditm(mnupil, kode):
  return next((mnu for mnu in mnupil if mnu[3] == kode), None)

def simMnu(mnupil, dataMnu, tngah=True):
  if tngah:
    tngah = len(mnupil)//2  
    mnupil.insert(tngah, dataMnu) 
  else:
    mnupil.append(dataMnu)
  return mnupil

def hapMenu(mnupil, kode):
  menu = mnuditm(mnupil, kode)
  if menu != None:
    if menu[2] == "minuman":
      del menu
    else:
      mnupil.remove(menu)


def dpMn(pengingat):
  print(f"""
{pengingat}
1. Menu minuman.
2. Menu makanan.
  """)
  pil = input("Silahkan pilih diantara dua pilihan tersebut = ")
  return pil == "1"

pil = "0"
while pil != "5":
  pilAwal()
  pil = input("Dari pilihan diatas, ingin melakukan apa? = ")
  if pil == "1":
    menuMenu()
  elif pil == "2":
    itMn = dpMn("Ingin menambah Menu baru? silahkan masukkan jenis menu? ")
    jmnu = "minuman" if itMn else "makanan"
    komnu = input("Silahkan masukkan kode menu baru = ")
    namabru = input("Masukkan nama menu yang ingin di tambahkan = ")
    harmnu = input("Masukkan harga dari menu baru = ")
    print(" ")
    menu = [namabru, int(harmnu), jmnu, komnu]
    awmnu =  input("""Apa anda ingin menambah di bagian akhir urutan menu?
note: menu akan di tempatkan di urutan tengah daftar menu 
      keseluruhan jika anda memilih tidak('t')  (y/t) = """) == "t"
    simMnu(dafMenu, menu, awmnu)
    print("Selamat, menu baru sudah di tambahkan!")
    input()

  elif pil == "3":
    kode = input("Silahkan Masukkan kode menu yang ingin di ubah : ")
    menu = mnuditm(dafMenu, kode)
    if menu != None:
      print(f"""
Kode menu: {menu[3]}
Nama menu: {menu[0]}
Harga Per-porsi: Rp. {menu[1]}""")
      menu[0] = input("Silahkan masukkan nama menu pengganti = ")
      menu[1] = input("Silahkan masukkan harga menu pengganti = ")
      print("Menu berhasil diganti")
    else:
      print("Menu tersebut tidak ada di daftar, harap perhatikan inputan!")
    input()

  elif pil == "4":
    kode = input("Silahkan masukkan kode menu yang ingin di hapus = ")
    menu = mnuditm(dafMenu, kode)
    if menu != None:
      print(f"""
Kode menu: {menu[3]}
Nama Menu: {menu[0]}
Harga Per-porsi: Rp. {menu[1]}""")
      hpusok = input("Apakah anda yakin ingin menghapus menu (y/t) = ") == "y"
      if hpusok:
        hapMenu(dafMenu, kode)
        print("Anda berhasil menghapus menu yang di pilih sebelumnya")
    else:
      print("Tidak ada menu yang dipilih sebelumnya")
    input()
  else:
    print("""

    Terima kasih sudah menggunakan program menu kafe Anatasya, semoga hari anda lancar dan menyenangkan.
    
    """)
    exit()
