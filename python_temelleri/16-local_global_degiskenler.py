# LOCAL VE GLOBAL DEGISKENLER

# global
x = 10
y = 20

#local: örneğin fonksiyonların içinde fonksiyonların etki alanında tanımlamış olduğumuz x y gibi değişkenlerdir.
def carpma_yap(x,y):
    return x*y
    #variable explorerda bu değişkenleri göremeyiz.

carpma_yap(2, 3)

#Local etki alanından global etki alanını degistirme

a = []
def eleman_ekle(y):
    a.append(y)
    print(str(y) + " Ifadesi eklendi.")


# =============================================================================
# a.append(1)
# a
# 
# =============================================================================
eleman_ekle(10)
eleman_ekle("ali")
eleman_ekle("veli")
a

print(a)
