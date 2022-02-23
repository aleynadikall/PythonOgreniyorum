# Ornek Metodlari : Sinif yapisi icerisine fonksiyon eklemek istedigimizde kullaniriz.

#Ornekler uzerinde calisan fonksiyonlar yazmak istiyoruz.

class VeriBilimci():
    bolum = ''
    sql = "Evet"
    deneyim_yili = 0
    bildigi_diller = []

VeriBilimci.bolum

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self,yeni_dil):
        self.bildigi_diller.append(yeni_dil)

ali =  VeriBilimci()
ali.bildigi_diller
ali.bolum

veli = VeriBilimci()
veli.bildigi_diller
veli.bolum

dir(VeriBilimci())      # Kullanabilecegimiz metodlari gösterir ve tanimlamis oldugumuz metodlar da artik buraya dahildir.

VeriBilimci.dil_ekle("R")
# TypeError: dil_ekle() missing 1 required positional argument: 'yeni_dil'
# Sinif ozellikleri ve ornekleme ozelliklerini ayni isimle isimlendirdigimiz icin bu hatayi aliyoruz.

ali.dil_ekle("R")
ali.bildigi_diller

veli.bildigi_diller("Python") 
# TypeError: 'list' object is not callable

veli.dil_ekle("Python")
veli.bildigi_diller



































