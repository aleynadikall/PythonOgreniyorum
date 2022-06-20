# iki argümanlı fonksiyon tanımlamak

def kare_al(x):
    print(x**2)


def carpma_yap(x,y):
    print(x*y)
carpma_yap(6,7)

# On tanımlı Argumanlar:
carpma_yap(3)
# TypeError: carpma_yap() missing 1 required positional argument: 'y'

def carpma_yap2(x,y=1):
    print(x*y)

carpma_yap2(3)      #sonuc basarili sekilde donmus olur.

carpma_yap2(3,4)    #3 ü 1 ile degil 4 ile çarpar. Basta  verilen degeri degistirebiliyoruz yani.
carpma_yap2(8)      #Yine 1 ile carpti.

carpma_yap2(y=2,x=3)    #Siralamadan bagimsiz olarak argumanlarin isimlerini yazarak da yapabiliriz.

# Ne zaman fonksiyon yazilir?
# =============================================================================
# Fonksiyonlar tekrar eden görevleri yerine getirmek ve var olan 
# işleri daha programatik şekilde yapmak istendiğinde kullanılır.
# =============================================================================

#îsi, nem, sarj
 40    25   90
(40+25)/90

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)
direk_hesap(25,40,70)

#	cıktıyı girdi olarak kullanmak

def direk_hesap2(isi,nem,sarj):
    print((isi+nem)/sarj)
cikti=direk_hesap2(25,40,70)
cikti

print(cikti)

# Nasıl bir fonksiyonun cıktısını girdi olarak kullanabiliriz?
#return ifadesi:
def direk_hesap3(isi,nem,sarj):
    return (nem+isi)/sarj
direk_hesap3(25,40,70)
direk_hesap3(25, 40, 70)*9
cikti=direk_hesap3(25,40,70)
cikti
print(cikti)

def direk_hesap4(isi,nem,sarj):
    return
    (nem+isi)/sarj

direk_hesap4(20,40,70)
#Çalışmadı çünkü fonksiyonda return görüldüğü an kendi bulunduğu satır dışındakilerle ilgilenmez. Kendi satırını çalıştırır ve fonksiyon son bulur.

