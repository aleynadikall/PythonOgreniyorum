# STRING METODLARI
# 1-UZUNLUK (ELEMAN SAYISI) BILGISINE ERISMEK: len() metodu

gel_yaz = "gelecegi_yazanlar"
# atama islemi
# del(mvk)
a = 9
b = 10
a*b
gel_yaz*b
len(gel_yaz)
c = len(gel_yaz)
print(c)
len("gelecegi_yazanlar")

# 2-upper() lower() fonksiyonlari
gel_yaz.upper()
gel_yaz.lower()
gel_yaz.islower()  # true ifadesi gelir.
B = gel_yaz.upper()
B.isupper()  # true ifadesi gelir.
gel_yaz.isupper()  # false ifadesi gelir.
B.islower()  # false ifadesi gelir.


# 3-replace() metodu
gel_yaz.replace("e", "a")
gel_yaz
# Nesnede kalici degisiklik meydana getirmez ama bazi metodlar atama dahi yapilmasa kalici degisiklige sebep olabilir.

gel_yaz.replace("a", "i")


# 4-KARAKTER KIRPMA METODU: strip()
gelecek = " gelecegi_yazanlar "
gelecek.strip()  # bosluklari silerek yazdirdi.
gelecek2 = "*gelecegi_yazanlar*"
gelecek2.strip()  # bastaki ve sondaki yildizlar silinmez.
gelecek3 = "*gelecegi_yazanlar*"
gelecek3.strip("*")
gelecek2.strip("*")

# veri tipinin üzerinde kullanabilecegimiz metodları ögrenmek icin dir() metodunu kullaniriz.
# Veri yapılarına ilişkin metodlara ulaşmak için dir() kullanılır.
dir(gelecek3)
gel_yaz.capitalize()  # sadece ilk kelimenin baş harfi büyük
gel_yaz.title()  # kelimelerin ilk harfleri büyük


# SUBSTRINGS
gelecek4 = "gelecegi_yazanlar"
gelecek4[0]  # 'g'
gelecek4[2]  # 'l'
gelecek4[20]  # IndexError:string index out of range

gelecek4[0:3]    #3'e kadar
gelecek4[3:7]    #'eceg'
