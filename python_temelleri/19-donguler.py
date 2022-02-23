# DONGULER

# for yapisi

ogrenci = ["ali","veli","isik","berk"]

for i in ogrenci:
    print(i)

for a in ogrenci:
    print(a)

# for dongusu ornek

maaslar = [1000,2000,3000,4000,5000]

for maas in maaslar:
    print(maas*0)

# Dongu ve Fonksiyonlarin Birlikte Kullanimi

def kare_al(x):
    print(x**2)
kare_al(2)


# maaslara yuzde 20 zam yapilacak gerekli kodlari yaziniz.
def yeni_maas(x):
    print(x*20/100+x)
    
for i in maaslar:
    yeni_maas(i)

# Uygulama 2: if,for ve fonksiyonlarin birlikte kulllanimi
maaslar2 = [1000,2000,3000,4000,5000]
def maas_ust(x):
    print(x*10/100+x)

def maas_alt(x):
    print(x*40/100+x)

for i in maaslar2:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)

# break & continue ifadeleri

maaslar3 = [8000,5000,2000,1000,3000,7000,1000]
dir(maaslar)
maaslar.sort()
maaslar

for i in maaslar3:
    if i == 3000:
        print("kesildi.")
        break
    print(i)

for i in maaslar3:
    if i == 1000:
        print("kesildi.")
        continue
    print(i)

# While yapisi

sayi = 1

while sayi < 10:
    sayi += 1
    print(sayi)




































