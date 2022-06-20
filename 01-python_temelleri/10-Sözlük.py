# DICTIONARY- Veri Ypisidir.
"""
1-Kapsayicidir.
2-Sirasizdir.
3-Degistirilebilir.
* Listelerde olduğu gibi index işlemleri yapılmaz.
* key-value şeklinde bir yapısı vardır.

"""

# Sözlük (Dictionary) Olusturma

sozluk={"REG" : "Regresyon Modeli" ,
        "LOJ" : "Lojistik Regresyon" ,
        "CART" : "Classification and Reg"}
sozluk

len(sozluk)     #3 elemanlidir.

    
sozluk2={"REG" : 10 ,
        "LOJ" : 20 ,
        "CART" : 30}      

sozluk2

sozluk3={"REG" : ["RMSE",10] ,
        "LOJ" : ["MSE",20] ,
        "CART" : ["SSE",30] }    
sozluk3
len(sozluk3)    #3 elemanlidir.

# Sozluk (dictionary) Eleman Islemleri 
sozluk4={ "REG" : "Regresyon Modeli" ,
         "LOJ" : "Lojistik Regresyonu" ,
         "CART" : "Classification and Reg" }

sozluk4

sozluk4[0]      #KeyError: 0

sozluk4["REG"]
sozluk4["LOJ"]

sozluk3["REG"]

sozluk5={"REG" : {"RMSE" : 10 ,
                  "MSE" : 20 ,
                  "SSE" : 30} ,
         
        "LOJ" : {"RMSE" : 10 ,
                 "MSE" : 20 ,
                 "SSE" : 30} ,
        
        "CART" : {"RMSE" : 10 ,
                  "MSE" : 20 ,
                  "SSE" : 30} }

sozluk5["REG"]
sozluk5["REG"]["SSE"]

# Sozluk (Dictionary) Eleman Ekleme & Degistirme

#Ekleme :Var olmayan bir nesne yazarsak ekleme yapar.
sozluk6={"REG" : "Regresyon Modeli" ,
        "LOJ" : "Lojistik Regresyon" ,
        "CART" : "Classification and Reg"}

sozluk6["GBM"] = "Gradient Boosting Mac"
sozluk6

#Degistirme : Var olan nesneyi yazarsak içeriğini degistirir.
sozluk6["REG"]= "Coklu Dogrusal Regresyon"
sozluk6

sozluk6[1] = "Yapay Sinir Aglari"
sozluk6

l = [1]
l

sozluk6[l]="yeni bir sey"     #TypeError: unhashable type: 'list'
""" Sozluklerde key degerleri yalnız sabit 
veri yapilari ile olusturulabilir."""

t = ("tuple",)
sozluk6[t]="yeni bir sey"
sozluk6
