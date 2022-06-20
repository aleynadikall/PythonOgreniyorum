# Veri Yapilari - SETLER (Kumeler)
"""
1-Sirasizdir.
2-Degerleri essizdir.
3-Degistirilebilirler.
4-Farkli tipleri barindirabilir.
* Performans odaklı bir veri tipidir. Daha cok programlama anlaminda daha hizli isler
yapmak istedigimizde kullaniriz. Essiz nesneler kullanmak istedigimizde yararlanabiliriz.
* Matematiksel anlamda kümelere benzer

"""
# Setlerin Olusturulmasi

s = set()
s

l = [1,"a","ali",123]
s = set(l)
s     # Bir liste uzerinden basarili sekilde set olusturduk.

t = ("a","ali")
s = set(t)
s     # Bir tuple uzerinden basarili sekilde set olusturduk.

ali = "lutfen_ata_bakma_uzaya_git"
type(ali)

s = set(ali)
s
"""
{'_', 'a', 'b', 'e', 'f', 'g', 'i', 'k',
'l', 'm', 'n', 't', 'u', 'y', 'z'}

Tekillestirerek her harfi ayri sekilde aldi.

"""
k = ["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]
s = set(k)
s
"""
{'ali', 'ata', 'bakma', 'git', 'lutfen', 'uzaya'}
Tekrar edenleri bir kez aldi. Essiz olma ozelliginden kaynaklidir.

"""

len(s)      # 6 elemanlidir.
k[0]
s[0]        #TypeError: 'set' object is not subscriptable

# Set eleman ekleme & cikarma

m=["gelecegi","yazanlar"]
s = set(m)
s

dir(s)  """ Dedigimizde add gibi bir sey geliyor. """
s.add("ile")
s

s.add("gelecege_git")
s

# Sirasiz, rastgele sekilde eklendi.

s.add("ile")
s
# tekrar ile degerini gözlemleyemiyoruz.

s.remove("ile")
s

s.remove("ile")   #KeyError: 'ile'
s

s.discard("ile")
s



























