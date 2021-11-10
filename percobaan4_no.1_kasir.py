import datetime

daf_menu = [
  ['1', "Jus de mangue du Roi Allain", 25000, "minuman", "jum = 1,2,3,4,5,6,7,8,9,10"],
  ['2', "Thé à la camomille d'Afata", 17000, "minuman","jum = 1,2,3,4,5,6,7,8,9,10"],
  ['3', "Café au lait de Lokheim", 30000, "minuman", "jum = 1,2,3,4,5,6,7,8,9,10"],
  ['4', "Le toast de Liliana", 22000, "makanan","jum = 1,2,3,4,5,6,7,8,9,10"],
  ['5', "Banane frite védique", 20000, "makanan","jum = 1,2,3,4,5,6,7,8,9,10"],
  ['6', "Poulet au beurre de soja", 35000, "makanan","jum = 1,2,3,4,5,6,7,8,9,10"]
]

# jumpes = {1,2,3,4,5,6,7,8,9,10}

# cbayar = {"pembayaran = E-money" or "tunai"}

def mataUang(nil):
  return f"Rp. {round(nil)}"

def pilMnu():
  print("""

 ◙◙◙◙◙◙ Bienvenue au café Anatasya, Silahkan pilih menu yang sesuai dengan selera anda ◙◙◙◙◙◙
  """)
  for menu in daf_menu:
    hargaPer1 = mataUang(menu[2])
    print(f"{menu[0]}. {menu[1]}   ◖{hargaPer1}◗")

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
jumPes = 0
while yaBeli:
  noMenu = input("Sudah anda tentukan? Silahkan masukkan nomor menu: ")

  jenisMenu = next((pil for pil in daf_menu if pil[0] == noMenu), None)

  if jenisMenu == None:
    print('Mohon maaf, pilihan anda tidak ada dalam menu')
  else:
    jum = input(f"Anda memesan, {jenisMenu[1]}. Choix parfait! Berapa banyak anda ingin memesannya? ")
    jenisMenu['jum'] = int(jum)
    jenisMenu['pembayaran'] = jenisMenu['jum'] * jenisMenu[2]
    dafPilmnu.append(jenisMenu)
    print(f"{jenisMenu['jum']} {jenisMenu[2]}, Pesanan anda akan kami siapkan")
    print( )
  yaBeli = input('Apakah anda ingin memesan minuman atau makanan lainnya di menu? (y/t) : ') == 'y'

if len(dafPilmnu) == 0:
  print("Je m'excuse, anda belum memesan minuman ataupun makanan dari menu")
else:
  jumMinuman = 0
  jumMakanan = 0
  for mnudipil in dafPilmnu:
    if mnudipil[3] == 'minuman':
      jumMinuman += mnudipil['jum']
    else:
      jumMakanan += mnudipil['jum']
  
  print("""
    ⬇⬇ Daftar pesanan yang anda pilih sebelumnya ⬇⬇
  """)
  for mnudipil in dafPilmnu:
    price = mataUang(mnudipil[2])
    print(f"{mnudipil['jum']} {mnudipil[1]}  = {mataUang(mnudipil['pembayaran'])}")

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

