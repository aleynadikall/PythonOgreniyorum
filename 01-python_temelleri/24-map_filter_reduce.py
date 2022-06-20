# map & filter & reduce Fonksiyonlari : isimsiz fonksiyon yapisi ile kullanilabilen fonksiyonlardir.

liste = [1,2,3,4,5]

#Fonskiyonlara arguman olarak fonksiyon ekleme olayi yalnizca python ve r'a
#ozel degildir. Son zamanlarda baziprogramlama dilledirinin de genel cabalarindan
#birisidir. Onceki bolumde ele aldigimiz davranislara izin veren fonksiyonlara
#firstclass fonksiyonlar denir. Bu fonksiyonlar kendilerine iteratif nesneleri ve
#fonksiyonlari arguman olarak alarak islemlerimizi oldukca kolay hale getirebilir.

#Bunlardan birisi map fonksiyonudur.

for i in liste:
    print(i+10)

list(map(lambda x: x+10, liste))
liste

A = [[1,2],[3,4],[5,6]]
list(map(lambda x: x[0]*3, A))
list(map(lambda x: x[1]*3, A))

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A,B]
AB
 
for i in AB:
    if type(i[0]) == int:
        print(list(map(lambda x: x-3, i)))


# ikincisi filter : iteratif nesne alir ve iteratif nesne olusturur. Bie kosula bagli calisir.

liste2 = [1,2,3,4,5,6,7,8,9,10]

# ikiye bolundugunde sifir kalan degerleri bulmak istiyoruz.

list(filter(lambda x: x%2 == 0, liste2))
liste2


# ucuncusu reduce : indirgeme islemi yapar.

from functools import reduce    # functools modulu uzerinden kutuphane cagirma islemi

liste3 = [1,2,3,4]
reduce(lambda a,b: a + b, liste3)

#ONEMLI
from functools import reduce
a = [1,2,3,4]
reduce(lambda a,b: a*b, a)

from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))

# fonksiyonel programlamada aklinda kalmasi gereken cumle islerimizi daha kolay 
# hale getiren, daha az yan etkileri olan ve daha az problemler olusturan yapilardir.
# daha cok matematiksel islemler, vektorel operasyonlar, matris islemleri, lineer 
# cebir islemleri ile birlikte kullanilir. Ve bunlara paralel olarak istatistik, 
# makine ogrenmesi ve veri bilimi islemlerine dogru ilerledigimizde artik biraz daha 
# pythonın bu klasik anlamdaki nesne yonelimli ozelliklerinden fonksiyonel programlama 
# ozelliklerine dogru ilerliyor olacagiz. 