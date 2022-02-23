# FONKSIYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI

print()
print
?print     
#fonksiyon dökümentasyonunu bize verir.

print("a","b",sep="_")

# Fonksiyon Nasıl Yazılır?

#Matematiksel Islemler:
4*4
4/4
5-1
6+3
3**2
3**5

# Phytonda ben bir fonksiyon tanımlıyorum demenin yolu def dir.
def kare_al(x):
    print(x**2)
kare_al(3)

# Bilgi notuyla çıktı üretmek
def kare_al(x):
    print("Girilen sayinin karesi:" + x**2)
    #TypeError: can only concatenate str (not "int") to str

kare_al(3)      

def kare_al(x):
    print("Girilen sayinin karesi:" + str(x**2))

kare_al(3)

# Hem karesi alınan sayiyi hem de karesi alinmis halini gormmek istiyorsak:
def kare_al(x):
    print("Girilen sayi: " + str(x) + " Girilen sayinin karesi: " + str(x**2))
kare_al(5)
