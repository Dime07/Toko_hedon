def laptop_low(laptop):
    if (laptop == 1):
        return print ("1.Acer swift air 3 (Rp.3.500.000)")
    elif (laptop == 2):
        return print ("2.Asus VivoBook Max (Rp.3.549.000)")
    elif (laptop == 3):
        return print ("3.HP 14-af118AU (Rp.3.985.000)")
     
def laptop_medium(laptop):
    if (laptop == 1):
        return print ("1.Asus X509FJ (Rp.8.699.000)")
    elif (laptop == 2):
        return print ("2.HP ProBook 430 G5 (Rp.8.250.000)")
    elif (laptop == 3):
        return print ("3.Acer Nitro 5 AN515-52 (Rp.9.338.000)")

def laptop_high(laptop):
    if (laptop == 1):
        return print ("1.Asus ROG Zephyrus G GA502DU (Rp.19.495.000)")
    elif (laptop == 2):
        return print ("2.Acer Predator Triton 300 (Rp.19.499.000)")
    elif (laptop == 3):
        return print ("3.Lenovo Legion Y7000 SE (Rp.16.999.000)")

def aksesoris(acc):
    if (acc == 1):
        return print ("1.Logitech G243 Prodigy Gaming Keyboard (Rp.698.500)")
    elif (acc == 2):
        return print ("Asus ROG Strix Impact II Gaming Mouse (Rp.620.000)")
    elif (acc == 3):
        return print ("Cooler Master-MasterPulse MH750 Gaming Headset (Rp.988.000)")


    #daftar laptop ini nyesuain sama di list depan
def harga_laptop_low(b):
    switcher={
                1:3500000,
                2:3549000,
                3:3985000,
             }
    return switcher.get(b,"Anda salah input")

def harga_laptop_medium(b):
    switcher={
                1:8699000,
                2:8250000,
                3:9338000,
             }
    return switcher.get(b,"Anda salah input")
    
def harga_laptop_high(b):
    switcher={
                1:19495000,
                2:19499000,
                3:16999000,
             }
    return switcher.get(b,"Anda salah input")

def harga_aksesoris(b):
    switcher={ 
                1:698500,
                2:620000,
                3:988000,
             }
    return switcher.get(b,"Anda salah input")