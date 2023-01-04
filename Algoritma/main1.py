
total = []
point = []



jumlahpesan = int(input("Masukan jumlah porsi yang ingin di pesan :"))
total = jumlahpesan * 10000

uang = int(input("Masukan uang pembayaran : "))
if uang > total:
    print("kembalian Rp.", uang - total)
elif uang == total:
    print("Hore uang kamu ternyata pas Rp",uang)
    print("Jumlah point kamu", jumlahpesan * 10000)
else:
    print("uang kamu kurang Rp.", total - uang)
    
#PSEUDOCODE
# input: masukan nama menu
# input: masukan jumlah porsi yang ingin dipesan
# input: masukan uang pembayaran
# outpout: uang pembayaran
#if menu == 1:
    #listnama = "Bakso biasa"
    #harga = (10000)
#else:
    #total=(10000*jumlahpesan)
# uang = int(input("Masukan uang pembayaran : "))
#if uang > total:
    #print("kembalian Rp.", uang - total)
#elif uang == total:
    #print("Hore uang kamu ternyata pas Rp",uang)
    #print("Jumlah point kamu", jumlahpesan * 10000)
#else:
    #print("uang kamu kurang Rp.", total - uang)