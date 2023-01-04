# PROGRAM membayar bakso otomatis

# PyAdeOOP
import sys  # mengimport sys untuk memberhentikan baris ke 16

jumlahpesan = int(input("Masukan jumlah porsi yang ingin di pesan :"))
total = jumlahpesan*10000

uang = int(input("Masukan uang pembayaran : "))
if uang > total:
    print("kembalian Rp.", uang - total)
    print("Jumlah point kamu", jumlahpesan *10000)
elif uang == total:
    print("Hore uang kamu ternyata pas Rp",uang)
    print("Jumlah point kamu", jumlahpesan *10000)
else:
    print("uang kamu kurang Rp.", total - uang)
    sys.exit()  # fungsinya untuk keluar dari program ketika uang yang dimasukan kurang
total_kupon = jumlahpesan / 10 
data_int = int(total_kupon)
tukarkan = input("Apakan anda yakin untuk menukarkan point (iya/tidak): ")
if tukarkan == 'iya':
    point = (jumlahpesan *10000)
    if point >= 100000:
        print("SELAMAT ANDA MENDAPATKAN",data_int, " KUPON BAKSO GRATIS!!!")
    else:
        print("MAAF POINT KAMU KURANG",100000 - jumlahpesan*10000)




# ***

#PSEUDOCODE
# input: masukan nomer menu
# input: masukan jumlah porsi yang ingin dipesan
# input: masukan uang pembayaran
# input: tukar  point
# outpout: uang pembayaran, jumlah point,kupon bakso gratis

# total = jumlahpesan*10000
# uang = int(input("Masukan uang pembayaran : "))
#if uang > total:
    #print("kembalian Rp.", uang - total)
#elif uang == total:
    #print("Hore uang kamu ternyata pas Rp",uang)
    #print("Jumlah point kamu", jumlahpesan * 10000)
#else:
    #print("uang kamu kurang Rp.", total - uang)
#tukarkan = input("Apakan anda yakin untuk menukarkan point (iya/tidak): ")
#if tukarkan == 'iya':
    #point = (jumlahpesan * 10000)
    #if point > 90000:
        #print("SELAMAT ANDA MENDAPATKAN KUPON BAKSO GRATIS!!!")
    #else:
        #print("MAAF POINT KAMU KURANG",100000 - jumlahpesan*10000)
