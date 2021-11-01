import datetime

daf_menu = [
  {"nom": '1', "namaMenu": "Jus de mangue du Roi Allain", "hargaPer1": 25000, "jenisMenu": "minuman"},
  {"nom": '2', "namaMenu": "Thé à la camomille d'Afata", "hargaPer1": 17000, "jenisMenu": "minuman"},
  {"nom": '3', "namaMenu": "Café au lait de Lokheim", "hargaPer1": 30000, "jenisMenu": "minuman"},
  {"nom": '4', "namaMenu": "Le toast de Liliana", "hargaPer1": 22000, "jenisMenu": "makanan"},
  {"nom": '5', "namaMenu": "Banane frite védique", "hargaPer1": 20000, "jenisMenu": "makanan"},
  {"nom": '6', "namaMenu": "Poulet au beurre de soja", "hargaPer1": 35000, "jenisMenu": "makanan"},
]
def mataUang(nil):
  return f"Rp. {round(nil)}"

def pilMnu():
  print("""

 ◙◙◙◙◙◙ Bienvenue au café Anatasya, Silahkan pilih menu yang sesuai dengan selera anda ◙◙◙◙◙◙
  """)
  for menu in daf_menu:
    hargaPer1 = mataUang(menu['hargaPer1'])
    print(f"{menu['nom']}. {menu['namaMenu']}  ◖ {hargaPer1}◗")

def dafDiskon():
  print(""" 
          ☆☆ Dan kami punya penawaran yang menarik untuk anda ☆☆

◯  Bila anda membeli 3 Minuman, anda akan mendapat diskon 10% 
◯  Dan jika anda membeli 2 Makanan, anda akan mendapatkan diskon 5% 
◯  Bahkan jika anda melakukan melalui E-money, anda akan mendapat diskon 5%
◯  Pada weekend, anda akan mendapatkan diskon 5%
◯  Sedangkan pada weekdays, anda akan mendapatkan diskon 10%
  """)

pilMnu()
dafDiskon()

yaBeli = True
dafPilmnu = []
while yaBeli:
  noMenu = input("Sudah anda tentukan? Silahkan masukkan nomor menu: ")

  jenisMenu = next((pil for pil in daf_menu if pil['nom'] == noMenu), None)

  if jenisMenu == None:
    print('Mohon maaf, pilihan anda tidak ada dalam menu')
  else:
    jum = input(f"Anda memesan, {jenisMenu['namaMenu']}. Choix parfait! Berapa banyak anda ingin memesannya? ")
    jenisMenu['jum'] = int(jum)
    jenisMenu['pembayaran'] = jenisMenu['jum'] * jenisMenu['hargaPer1']
    dafPilmnu.append(jenisMenu)
    print(f"{jenisMenu['jum']} {jenisMenu['namaMenu']}, Pesanan anda akan kami siapkan")
    print( )
  yaBeli = input('Apakah anda ingin memesan minuman atau makanan lainnya di menu? (y/t) : ') == 'y'

if len(dafPilmnu) == 0:
  print("Je m'excuse, anda belum memesan minuman ataupun makanan dari menu")
else:
  jumMinuman = 0
  jumMakanan = 0
  for mnudipil in dafPilmnu:
    if mnudipil['jenisMenu'] == 'minuman':
      jumMinuman += mnudipil['jum']
    else:
      jumMakanan += mnudipil['jum']
  
  print("""
    ⬇⬇ Daftar pesanan yang anda pilih sebelumnya ⬇⬇
  """)
  for mnudipil in dafPilmnu:
    price = mataUang(mnudipil['hargaPer1'])
    print(f"{mnudipil['jum']} {mnudipil['namaMenu']}  = {mataUang(mnudipil['pembayaran'])}")

  print(" ")
  
  caraBayar = input("Dengan membayar menggunakan E-money anda bisa mendapatkan diskon, ingin menggunakan E-money? (y/t) : ")
  disCBayar = 5 if caraBayar == "y" else 0

  hariDis = 10 if datetime.datetime.today().weekday() < 5 else 5

  disMinum = 5 if jumMinuman >= 2 else 0
  disMakan = 10 if jumMakanan >= 3 else 0

  jumDis = disCBayar + hariDis  + disMinum + disMakan
  jumBayar = sum(mnudipil['pembayaran'] for mnudipil in dafPilmnu)
  potDis = jumBayar * jumDis / 100
  jumAkhirBayar = jumBayar - potDis

  print(f"Harga semua pesanan anda adalah : {mataUang(jumBayar)}")
  print(f"Dengan potongan dari diskon sebesar : {mataUang(potDis)} ({jumDis}%)")
  print (" ")
  print(f"Total keseluruhan pembayaran pesanan anda : {mataUang(jumAkhirBayar)}  ⬅")
  print (" ")
print ("Terima kasih sudah mengunjungi café Anatasya, bonne journée! ")

