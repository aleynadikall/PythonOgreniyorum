# FONKSIYONEL PROGRAMLAMAYA GIRIS

# =============================================================================
# Python'da Fonksiyonel Programlama
# 
# Fonksiyonlar dilin bastacidir.
# (Birinci sinif nesnelerdir.)
# Yan etkisiz fonksiyonlar. (stateless, girdi-cikti)
# “Ancak bir girdi verildiğinde çıktı üreten fonksiyonlar” ifadesi aşağıdaki 
# fonksiyonel programlama özelliklerinden hangisini işaret etmektedir.= Yan Etkisiz.

# Yuksek seviye fonksiyonlardir.    "Daha az caba
# Vektorel operasyonlardir.         Daha fazla is"
# =============================================================================


# Yan Etkisiz Fonksiyonlar (Pure Functions)

#Ornek-1:Yan Etki : Bagimsizlik

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6)
#A degerini degistirdigimizde sonuc da degisiyor. Bir takim bagimliliklari(A) oldugu icin impure
# yani saf olmayan fonskiyondur. Yan etki durumunun 1.ornegi budur.

pure_sum(3,4)  # Bunun cevabi parametreler degismedigi sürece her zaman 7 olur. Girdi-Cikti durumu vardir. Disariya
# bir bagimliligi yoktur. 


#Ornek-2:Olumcul Yan Etkiler

#Asagidaki kodlara takilma
class LineCounter:
    def __init__(self,filename):
        self.file = open(filename,'r')
        self.lines = []
    
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)

lc = LineCounter('deneme.txt')

print(lc.lines)     #[]
print(lc.count())   #0

lc.read()

print(lc.lines)
print(lc.count())   #10

# =============================================================================
# lc.count() ve lc.lines degerlerinin degismesine ic nesnenin durum degismesi denir.
# Bircok konuda bu sekilde kucuk bir islemle degismesi bir nimettir bazen de hic 
# istenmeyen bir durumdur.
# =============================================================================

#Fonksiyonel Programlama (FP) : Daha rahat, daha bagimsiz, ancak girdi verildiginde cikti ureten bir yapi

def read(filename):
    with open(filename,'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count

# Naparsak yapalim yukaridaki example_lines ve lines_count ifadeleri degismeyecektir.
# Ancak bir girdi verdigimizde cikti uretecek sekilde degisecektir ve baska hicbir 
# yapiyi etkilemeyecektir. Verdigimiz girdi disinda bir cikti uretemez.


# Isimsiz Fonksiyonlar (Anonymous Functions)

def old_sum(a,b):   #isimli fonksiyon
    return a + b

old_sum(4,5)


new_sum = lambda a,b : a+b
new_sum(4,5)


sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x : x[1])

# Bir fonksiyona isimlendirme yapmadan o fonksiyonu kullanabiliyor oldugumuzu bilsen yeter su anlik.


# Vektorel Operasyonlar (Vectoral Operations)

# Nesneye Dayali Programlama (OOP)
a = [1,2,3,4]   #bir tek boyutlu vektor
b = [2,3,4,5]   #bir tek boyutlu vektor

ab = []

range(0,len(a))  #range(0, 4)

for i in range(0,len(a)):
    ab.append(a[i]*b[i])
    
ab
# Vektorel islemlerde yukaridaki gibi kullanmak dogru degildir.

#FP

import numpy as np  #bir modulü import ettik.
a = np.array([1,2,3,4]) #elimizde bir liste olmus oldu.
b = np.array([2,3,4,5])

#Aynı a ve b vektorlerini yeniden tanımladık.

a*b     #direkt sonuc bize geldi. Daha basit ve buyuk bir kolaylık.Bu vektor duzeyinde bir operasyondur.

# Python az caba ile yuksek performanslı isler yapmamiza olanak saglar cunku yuksek seviyeli bir dildir.
# Bazı kutuphanelerle daha yuksek seviyeli bir dil olarak kullanabilriz. Mesela numpy


import numpy as np
a = np.array([1,1,1])
b = np.array([2])
 
a+b

















