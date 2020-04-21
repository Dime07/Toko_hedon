def laptop_low(laptop):
    if (laptop == 1):
        return print ("Terima kasih telah membeli Acer Aspire V5-132")
    elif (laptop == 2):
        return print ("Terima kasih telah membeli Asus VivoBook Max")
    elif (laptop == 3):
        return print ("Terima kasih telah membeli HP 14-af118AU")
    elif (laptop == 4):
        return print ("Terima kasih telah membeli Lenovo ThinkPad 11e")
    elif (laptop == 5):
        return print ("Terima kasih telah membeli Acer Aspire One 722")
    elif (laptop == 6):
        return print ("Terima kasih telah membeli HP 14-bw016au")
    elif (laptop == 7):
        return print ("Terima kasih telah membeli Lenovo Ideapad B470")
    elif (laptop == 8):
        return print ("Terima kasih telah membeli Lenovo Yoga A12")


     
def laptop_medium(laptop):
    if (laptop == 1):
        return print ("Terima kasih telah membeli Asus X509FJ")
    elif (laptop == 2):
        return print ("Terima kasih telah membeli HP ProBook 430 G5")
    elif (laptop == 3):
        return print ("Terima kasih telah membeli Acer Nitro 5 AN515-52")
    elif (laptop == 4):
        return print ("Terima kasih telah membeli ASUS X401U-WX099D")
    elif (laptop == 5):
        return print ("Terima kasih telah membeli Lenovo Ideapad 330S 15")
    elif (laptop == 6):
        return print ("Terima kasih telah membeli Lenovo Yoga 520 14")
    elif (laptop == 7):
        return print ("Terima kasih telah membeli Acer Aspire 5 A514-52G")
    elif (laptop == 8):
        return print ("Terima kasih telah membeli TOSHIBA Satellite L740-1219U")

def laptop_high(laptop):
    if (laptop == 1):
        return print ("Terima kasih telah membeli Asus ROG Zephyrus G GA502DU")
    elif (laptop == 2):
        return print ("Terima kasih telah membeli Acer Predator Triton 300")
    elif (laptop == 3):
        return print ("Terima kasih telah membeli Lenovo Legion Y7000 SE")
    elif (laptop == 4):
        return print ("Terima kasih telah membeli Lenovo Legion Y530")
    elif (laptop == 5):
        return print ("Terima kasih telah membeli Acer Spin 5 SP513-52N-36P7")
    elif (laptop == 6):
        return print ("Terima kasih telah membeli Lenovo ThinkPad Yoga 12")
    elif (laptop == 7):
        return print ("Terima kasih telah membeli ASUS ROG Strix GL503")
    elif (laptop == 8):
        return print ("Terima kasih telah membeli Apple MacBook Air 11.6")
    elif (laptop == 9):
        return print ("Terima kasih telah membeli Razer Blade Stealth QHD")
    elif (laptop == 10):
        return print ("Terima kasih telah membeli ASUS ZenBook Flip S UX370UA")

def aksesoris(acc):
    if (acc == 1):
        return print ("Terima kasih telah membeli Logitech G243 Prodigy Gaming Keyboard")
    elif (acc == 2):
        return print ("Terima kasih telah membeli Asus ROG Strix Impact II Gaming Mouse")
    elif (acc == 3):
        return print ("Terima kasih telah membeli Cooler Master-MasterPulse MH750 Gaming Headset")
    elif (acc == 4):
        return print ("Terima kasih telah membeli HP DeskJet Ink Advantage 2135 All-in-One Printer")
    elif (acc == 5):
        return print ("Terima kasih telah membeli JBL T450 Foldable Wired On-Ear Headphones")
    elif (acc == 6):
        return print ("Terima kasih telah membeli Portable 1080 P Home Theater Mini LED Proyektor")
    elif (acc == 7):
        return print ("Terima kasih telah membeli Mouse Wireless Logitech M238")
    elif (acc == 8):
        return print ("Terima kasih telah membeli Fantech mk871 keyboard")


    #daftar laptop ini nyesuain sama di list depan
def harga_laptop_low(b):
    switcher={
                1:3500000,
                2:3549000,
                3:3985000,
                4:2198000,
                5:2500000,
                6:4025000,
                7:4599000,
                8:4999000,

             }
    return switcher.get(b,"Anda salah input")

def harga_laptop_medium(b):
    switcher={
                1:8699000,
                2:8250000,
                3:9338000,
                4:5249000,
                5:6415000,
                6:7500000,
                7:5549000,
                8:6310400,

             }
    return switcher.get(b,"Anda salah input")
    
def harga_laptop_high(b):
    switcher={
                1:19495000,
                2:19499000,
                3:16999000,
                4:10799000,
                5:11420000,
                6:13099000,
                7:14299000,
                8:15266000,
                9:18325000,
                10:17350000,
             }
    return switcher.get(b,"Anda salah input")

def harga_aksesoris(b):
    switcher={ 
                1:698500,
                2:620000,
                3:988000,
                4:825000,
                5:235000,
                6:527000,
                7:146000,
                8:440000,
             }
    return switcher.get(b,"Anda salah input")