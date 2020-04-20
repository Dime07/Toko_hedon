def laptop_low(laptop):
    if (laptop == 1):
        return print ("Anda memilih acer swift air 3 (Rp.3.500.000)")
    elif (laptop == 2):
        return print ("Anda memilih ASUS Saja")
     
def laptop_medium(laptop):
    if (laptop == 1):
        return print ("Anda memilih acer swift air 3 (Rp.6.000.000)")
    elif (laptop == 2):
        return print ("Anda memilih ASUS Saja")

def laptop_high(laptop):
    if (laptop == 1):
        return print ("Anda memilih acer swift air 3 (Rp.6.000.000)")
    elif (laptop == 2):
        return print ("Anda memilih ASUS Saja")

def aksesoris(acc):
    if (laptop == 1):
        return print ("Anda memilih acer swift air 3 (Rp.6.000.000)")
    elif (laptop == 2):
        return print ("Anda memilih ASUS Saja")


    #daftar laptop ini nyesuain sama di list depan
def harga_laptop_low(b):
    switcher={
                1:3500000,
                2:10,
                3:22,
             }
    return switcher.get(b,"Anda salah input")

def harga_laptop_medium(b):
    switcher={
                1:6000000,
                2:10,
                3:22,
             }
    return switcher.get(b,"Anda salah input")
    
def harga_aksesoris(b):
    switcher={
                1:6000000,
                2:10,
                3:22,
             }
    return switcher.get(b,"Anda salah input")