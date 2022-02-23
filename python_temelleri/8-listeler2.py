# Metodlar ile eleman ekleme & silme : append & remove
liste=["ali","veli","isik"]
dir(liste)

liste

#append:Listeler değiştirilebilir olduğu için üzerinde değişilik yapabiliyoruz.
#Kalici değişiklik yapar.
liste.append("berkcan")
liste

#remove
liste.remove("berkcan")
liste


#indekse göre eleman ekleme & silme : insert & pop
liste.insert(0, "ayse")
liste

liste.pop(0)
liste

liste[0]="ayse"
liste   #insertle aynı şey değildir.

liste.insert(2, "mehmet")
liste

liste.insert(6,"berk")
liste

liste_yeni = ["ali","ayse","mehmet"]
liste_yeni
liste_yeni.insert(6,"melisa")
liste_yeni
len(liste_yeni)

liste.insert(len(liste), "beren")
liste

# diğer liste metodlari:
    
#count(): kaç taneyse eleman onu bize verir.
liste.count("ali")
liste

liste2=["ayse","ayse","ayse","mehmet","sefa","sefa","aleyna"]
liste2

liste2.count("ayse")
liste2.count("sefa")
liste2.count("aleyna")
liste2.count("mehmet")

#copy() : elimizdeki mevcut listeyi kopyalamak,yedeklemek,ilk halini saklamak için kullanilabilir.
liste_yedek=liste2.copy()

#extend() : daha önce iki listeyi birleştirmek için el yordamıyla kullandığımız liste birleştirme için kullanılır.

liste.extend(["a","b",10])
liste

#index()

liste2.index("aleyna")


#reverse() : liste elemanlarini ters çevirir.

liste2.reverse()
liste2


#sort() : sıralama için kullanilir.

liste3=[10,40,5,90]
liste3.sort()
liste3


#clear(): liste içindeki tüm elemanlari uçurur.

liste3.clear()
liste3
