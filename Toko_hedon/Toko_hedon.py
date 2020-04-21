print ("="*20)
print("TOKO HEDONISME")
print("="*20)
import daftar_laptop


def uang_masuk(uang):
    if (uang >= 1000000) and (uang <= 5000000):
        print ("Selamat anda bisa membeli barang dengan spec low,mari saya tunjukkan")
        print ("1.Acer Aspire V5-132 (Rp.3.500.000)")
        print ("2.Asus VivoBook Max (Rp.3.549.000)")
        print ("3.HP 14-af118AU (Rp.3.985.000)")
        print ("4.Lenovo ThinkPad 11e (Rp.2.198.000)")
        print ("5.Acer Aspire One 722 (Rp.2.500.000)")
        print ("6.HP 14-bw016au (Rp.4.025.000)")
        print ("7.Lenovo Ideapad B470 (Rp 4.599.000)")
        print ("8.Lenovo Yoga A12 (Rp 4.999.000)")
        #nanti ini diisi list laptop low
    elif (uang >= 5000100) and (uang <= 10000000):
        print ("Selamat anda bisa membeli barang dengan spec medium,mari saya tunjukkan")
        print ('1.Asus X509FJ (Rp.8.699.000)')
        print ('2.HP ProBook 430 G5 (Rp.8.250.000)')
        print ('3.Acer Nitro 5 AN515-52 (Rp.9.338.000)')
        print ("4.ASUS X401U-WX099D (Rp 5.249.000)")
        print ("5.Lenovo Ideapad 330S 15 (Rp 6.415.000)")
        print ("6.Lenovo Yoga 520 14 (Rp 7.500.000)")
        print ("7.Acer Aspire 5 A514-52G (Rp 5.549.000)")
        print ("8.TOSHIBA Satellite L740-1219U (Rp.6.310.400")
    elif (uang >= 10000100) and (uang <= 50000000):
        print ("Selamat anda bisa membeli barang dengan spec high,mari saya tunjukkan")
        print ('1.Asus ROG Zephyrus G GA502DU (Rp.19.495.000)')
        print ('2.Acer Predator Triton 300 (Rp.19.499.000)')
        print ('3.Lenovo Legion Y7000 SE (Rp.16.999.000)')
        print ("4.Lenovo Legion Y530 (Rp 10.799.000	)")
        print ("5.Acer Spin 5 SP513-52N-36P7 (Rp 11.420.000)")
        print ("6.Lenovo ThinkPad Yoga 12 (Rp 13.099.000)")
        print ("7.ASUS ROG Strix GL503 (Rp 14.299.000)")
        print ("8.Apple MacBook Air 11.6 (Rp 15.266.000)")
        print ("9.Razer Blade Stealth QHD (Rp 18.325.000)")
        print ("10.ASUS ZenBook Flip S UX370UA (Rp 17.350.000)")
    elif (uang >= 100000) and (uang <= 999999):
        print ("Mohon maaf anda tidak bisa membeli laptop dengan harga segitu,Tapi anda bisa membeli aksesorisnya")
        print ('1.Logitech G243 Prodigy Gaming Keyboard (Rp.698.500)')
        print ('2.Asus ROG Strix Impact II Gaming Mouse (Rp.620.000)')
        print ('3.Cooler Master-MasterPulse MH750 Gaming Headset (Rp.988.000)')   
        print ("4.HP DeskJet Ink Advantage 2135 All-in-One Printer (Rp.825.000)")
        print ("5.JBL T450 Foldable Wired On-Ear Headphones (Rp.235.000)")
        print ("6.Portable 1080 P Home Theater Mini LED Proyektor (Rp.527.000)")
        print ("7.Mouse Wireless Logitech M238  (Rp.146.000)")
        print ("8.Fantech mk871 keyboard (Rp.440.000)")




kembalian = 0
a=int(input("Masukkan uang yang ingin anda keluarkan=Rp."))
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
    elif (a >= 10000100) and (a <= 50000000):
        r=daftar_laptop.laptop_high(b)
        harga=daftar_laptop.harga_laptop_high(b)
        kembalian=a-harga
        print ("sisa uang=Rp.",kembalian)

    elif (a >= 100000) and (a <= 999999):
        r=daftar_laptop.aksesoris(b)
        harga=daftar_laptop.harga_aksesoris(b)
        kembalian=a-harga
        print ("sisa uang=Rp.",kembalian)

    kata=input("mau belanja lagi gak?")
    print (" ")
    if (kata == "tidak"):
        break
print ("terima kasih telah menghabiskan uang ditoko kami")







