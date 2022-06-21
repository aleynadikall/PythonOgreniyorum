# VERI YAPILARI

# LISTELER
# Liste Olusturma Yollari:
    # 1-[]
    # 2-list()

notlar=[90,80,70,50]    # tipi list olan bir nesnedir.Bir veri yapisidir.
type(notlar)

# =============================================================================
# Notlarin içindeki değerler integer olmasına rağmen notların tipi listtir.
# Liste bir üst tiptir. Bir veri yapısıdır.
# İçinde int float ve string tipinde değerler olabilir.
# 1-Siralidir.
# 2-Degistirilebilir.
# 3-Kapsayicidir.
# 
# =============================================================================

liste=["a",19.3,90]     #İçinde birbirinden farklı tipte değerler var.
liste_icinde_liste=["a",19.3,90,notlar]     #İçinde başka bir liste de bulunabilir.
len(liste_icinde_liste)     #elemansayisi=4

#Liste Ici Tip Sorgulama:

type(liste_icinde_liste[0]) #str
type(liste_icinde_liste[1]) #float
type(liste_icinde_liste[2]) #int
type(liste_icinde_liste[3]) #list

#Elimizdeki iki listeyi birleştirmek istediğimizi düşünelim

toplam_liste=[liste_icinde_liste,liste]

#Peki olusan bu listeyi nasıl sileriz?
del(toplam_liste)   
#Daha sonrasında del'in başına diez atıp çalışmaya öyle devam etmen önerilir.

#LISTELER-ELEMAN ISLEMLERI
#Liste Elemenalarina Erismek:
    
liste3=[10,20,30,40,50]

liste3[0]
liste3[1]

liste3[6]       #IndexError: list index out of range

liste3[0:2]     #10,20

liste3[ :2]     #10,20
liste3[2: ]     #30,40,50
liste3[:]       #Hepsini yazar

liste4=["a",10,[20,30,40,50]]
liste4

liste4[3]       #IndexError: list index out of range
liste4[2]

#liste4 ün icindeki listenin elemanlarina nasil erisiriz?
liste4[2][1]    #30
liste4[2][3]    #50

# Liste Elemanlarini Degistirmek:

liste5=["ali","veli","berkcan","ayse"]
liste5
liste5[1]="velinin_babasi"
liste5
liste5[1]="veli"
liste5[0:3]="alinin_babasi","velinin_babasi","berkcanin_babasi"
print(liste5)

liste5=["ali","veli","berkcan","ayse"]
liste5=liste5 + ["kemal"]   #atama yaparak kemali de listeye ekledik.
liste5

del liste5[1]   #bir nesneyi silmek icin kullandik. Sonrasinda diezle yoruma al.
liste5

