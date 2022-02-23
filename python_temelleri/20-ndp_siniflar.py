# NESNE YONELIMLI PROGRAMLAMA

# 1)Siniflara Giris ve Sinif (Class) Tanimlamak

# Sinif Nedir?
# =============================================================================
# Siniflar benzer ozellikler, ortak amaclar tasiyan, icerisinde metod
# ve degiskenler olan yapilardir.
# =============================================================================

# =============================================================================
# class VeriBilimci():
#     print("Bu bir siniftir.")
#
# =============================================================================

# 2)Sinif Ozellikleri (Class Attributes

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []

# Siniflarin Ozelliklerine Erismek:
VeriBilimci.bolum
VeriBilimci.sql

# Siniflarin Ozelliklerine Erismek: Mumkundur.
VeriBilimci.sql="Hayir"
VeriBilimci.sql

# 3)Sinif Orneklemesi:Instantiation
# =============================================================================
#  Birbirinden farkli veri bilimcilerin bu ozellikleri degisekcektir. Dolayisiyla bizim bir
#  de veri bilimci olusturmamiz gerekiyor. Bu alt kümelendirme islemine sinif orneklemesi denir.
# =============================================================================

ali = VeriBilimci()
ali.sql
# =============================================================================
# Ali ile ilgili hicbir tanimlama yapmadik ancak bu sinifin bir ornegi oldugundan dolayi sql ozelligini
# cagirdigimizda hayir cevabini bize vermis oldu.
# =============================================================================

ali.deneyim_yili
ali.bolum

# Peki Ali'nin ozelliklerini nasil degistirecegiz.
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli =  VeriBilimci()
veli.sql

veli.bildigi_diller    # Python geldi ancak biz Veli'nin bildigi dilleri girmemistikki.

# =============================================================================
# Yukarida Ali icin yapilan degisiklik tum sinifa mal oldu.
# Dolayisiyle ornekledigimiz bir deger uzerinde yaptigimiz bir degisiklik
# genel anlamda sinifin ozelliklerini etkiledi ve yine bu sinifin ozelliklerini
# tasiyan bir instance bende de bu ozellik var dedi. Peki bunu nasil duzeltiriz?
# Ornek ozellikleri kisminda bunu anlatacagiz.
# =============================================================================



# 4)Ornek Ozellikleri

# =============================================================================
# Orneklerin her birinin kendi icinde degistirilebilir ozelliklerden olustugunu 
# pythona vermemiz gerekiyor.
# 
# 
# =============================================================================


class VeriBilimci():
    bildigi_diller = ["R","PYTHON"]     # VeriBilimci.bildigi_diller yazdigimizda attributeError almamak icin buraya ekledik.
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):     # self orneklemleri temsil eden temsilcidir.
        self.bildigi_diller = []
        self.bolum = ''

ali = VeriBilimci()
ali.bildigi_diller


veli = VeriBilimci()
veli.bildigi_diller

# İkisi de bos degerler verir.

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller
veli.bildigi_diller.append("R")
veli.bildigi_diller
ali.bildigi_diller

VeriBilimci.bildigi_diller
# AttributeError: type object 'VeriBilimci' has no attribute 'bildigi_diller'

ali.bolum

VeriBilimci.bolum
ali.bolum = "istatistik"
VeriBilimci.bolum
veli.bolum
veli.bolum = "end_muh"
veli.bolum
ali.bolum
VeriBilimci.bolum



















