# If ve Input ile Mini Uygulama

sinir = 50000
magaza_adi = input("Magaza Adi Nedir?")
gelir = int(input("Gelirinizi Giriniz:"))

if gelir > sinir:
    print("Tebrikler " + magaza_adi + " subesinden promosyon kazandiniz.")
elif gelir < sinir:
    print("Uyari! Cok dusuk gelir:" + str(gelir))
else:
    print("Takibe Devam...")