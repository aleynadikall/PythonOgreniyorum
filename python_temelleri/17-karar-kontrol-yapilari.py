# KARAR & KONTROL YAPILARI

# Yagmur yagarsa semsiye alı proglamlama diline ögretmemizi saglayan yapilardir.

# True-False Sorgulama

sinir = 5000
sinir == 4000   # false döner
sinir == 5000   # true döner

5 == 4  #false döner

# if yapisi

gider = 50000
gelir = 40000
kar = 20000

if gelir < gider:
    print("Gelir giderden kucuktur.")

if gelir > kar:
    print("Gelir kardan buyuktur.") 

#else yapisi

if kar > gider:
    print("Kar Giderden Buyuktur.")
else:
    print("Kar Giderden Kucuktur.")


# elif yapisi
gider2 = 35000
gelir2 = 35000
kar2 = 50000

if gelir2 > gider2:
    print("Gelir Giderden Buyuktur.")
elif gelir2 == gider2:
    print("Gelir ve Gider Esittir.")
else:
    print("Gelir Giderden Kucuktur.")

if gelir2 > gider2:
    print("Gelir Giderden Buyuktur.")
elif kar2 == gider2:
    print("Kar ve Gider Esittir.")
elif kar2 == gelir2:
    print("Kar ve Gelir Esittir.")
else:
    print("Gelir ve gider esittir.")

