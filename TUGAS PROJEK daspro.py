from termcolor import colored, cprint

print ("""
======================================
            KARCIS WAHANA PERMAINAN
         Daftar harga KARCIS
======================================
BC.    Bombom car    : Rp 15000
KP.    Komedi putar  : Rp 20000
MB.    Mandi bola    : Rp 10000
BL.    Biang lala    : Rp 35000
OB.    Ombak banyu   : Rp 25000
KK.    Kora kora     : Rp 30000
======================================
""")

kode =str(input("Masukan Kode karcis = "))
jumlahkarcis= int(input("Masukan Jumlah karcis = "))
if kode == "BC":
    listnama = "Bombom car"
    harga=(15000*jumlahkarcis)
    
elif kode == "KP":
    listnama = "Komedi putar "
    harga=(20000*jumlahkarcis)
    int(harga)
elif kode == "MB":
    listnama = "Mandi bola"
    harga=(10000*jumlahkarcis)
    
elif kode == "BL":
    listnama = "Biang lala"
    harga=(35000*jumlahkarcis)
    
elif kode == "Ob":
    listnama = "Ombak banyu"
    harga=(25000*jumlahkarcis)
    
elif kode == "KK":
    listnama = "Kora kora"
    harga=(30000*jumlahkarcis)
    
else:
    listnama = "-"
    harga = "-"
    totalharga = "-"
totalharga=(str(jumlahkarcis * harga))    
cprint("======================================", "cyan")
cprint("KARCIS WAHANA PERMAINAN", "blue")
cprint("======================================", "blue")
print("Kode karcis = " ,kode,)
print("Jumlah karcis = " ,jumlahkarcis)
print("Harga = " ,harga)
print("======================================")
print("Jumlah Bayar = " ,totalharga)
print("======================================")