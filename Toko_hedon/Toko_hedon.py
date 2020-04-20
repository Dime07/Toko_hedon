print ("="*20)
print("TOKO HEDONISME")
print("="*20)
import daftar_laptop


def uang_masuk(uang):
    if (uang >= 1000000) and (uang <= 5000000):
        print ("Selamat anda bisa membeli barang dengan spec low,mari saya tunjukkan")
        print ("1.acer swift air 3")
        print ("2. ASUS APALAH ITU ")
        #nanti ini diisi list laptop low
    elif (uang >= 5000100) and (uang <= 10000000):
        return print ("Selamat anda bisa membeli barang dengan spec medium,mari saya tunjukkan")
    elif (uang >= 10000100) and (uang <= 20000000):
        return print ("Selamat anda bisa membeli barang dengan spec high,mari saya tunjukkan")
    elif (uang >= 100000) and (uang <= 999999):
        return print ("Mohon maaf anda tidak bisa membeli laptop dengan harga segitu,Tapi anda bisa membeli aksesorisnya")



kembalian = 0
a=float(input("Masukkan uang yang ingin anda keluarkan="))
while True:
    if (kembalian != 0):
        uang_masuk(kembalian)
        a=kembalian
    else:
        uang_masuk(a)
    b=int(input("barang urutan berapa yang ingin anda beli?")) #sepertinya harus pakai if
    
    if (a >= 1000000) and (a <= 5000000):
        p=daftar_laptop.laptop_low(b)
        harga=daftar_laptop.harga_laptop_low(b)
        kembalian=a-harga
        print ("sisa uang=Rp.",kembalian)
    elif (a >= 5000100) and (a <= 10000000):
        q=daftar_laptop.laptop_medium(b)
        harga=daftar_laptop.harga_laptop_medium(b)
        kembalian=a-harga
        print ("sisa uang=Rp.",kembalian)
    elif (a >= 10000100) and (a <= 20000000):
        r=daftar_laptop.laptop_high(b)
        harga=daftar_laptop.harga_laptop_medium(b)
        kembalian=a-harga
        print ("sisa uang=Rp.",kembalian)

    elif (a >= 100000) and (a <= 999999):
        r=daftar_laptop.aksesoris(b)
        harga=daftar_laptop.harga_aksesoris(b)
        kembalian=a-harga
        print ("sisa uang=Rp.",kembalian)

    kata=input("apakah anda ingin belanja lagi?")
    if (kata == "tidak"):
        break








