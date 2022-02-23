def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3)/3
    
    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 75 and ortalama <= 84:
        harf = "BB"
    elif ortalama >= 65 and ortalama <= 74:
        harf = "CB"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "CC"
    elif ortalama >= 55 and ortalama <= 59:
        harf = "DC"
    elif ortalama >= 50 and ortalama <= 54:
        harf = "DD"
    elif ortalama >= 45 and ortalama <= 49:
        harf = "FD"
    else:
        harf = "FF"
    
    return ogrenciAdi + ": " +harf + "\n"


def ortalamalari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input('Ogrenci Adi: ')
    soyad = input('Ogrenci Soyad: ')
    not1 = input('not1: ')
    not2 = input('not2: ')
    not3 = input('not3: ')

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad+' '+soyad + ':'+not1+','+not2+','+not3+'\n')


def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []
        
        for i in file:
            liste.append(not_hesapla(i))
        
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input('1- Notlari Oku\n2- Not Gir\n3- Notlari Kaydet\n4- Cikis\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kaydet()
    else:
        break
