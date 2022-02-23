# Miras Yapilari (Inheritance)
# Var olan sınıfların özelliklerini başka sınıflar için kullanmamiz inharitance ile mumkundur.

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""

class Marketing(Employees):
    def __init__(self):
        self.StorryTelling = ""

veriBilimci1 = DataScience()
veriBilimci1.LastName

mar1 = Marketing()
mar1.Address

# =============================================================================
# Sinif tanimlamalari yaparken olusturdugumuz bu yapilari fonskiyonel bir yapida degil de
# sabit degerleriyle olusturduk. Ne demek bu yani ben ornegin employees classını birisi 
# calistirmak istediginde eger bu classin icerisinde degisken degerler olmasini istersem 
# ve bu sekilde kullanilmasini istersem bunu yerine getirmenin yolu tanimlamayi asagidaki
# gibi yapmaktir.
# 
# =============================================================================

class Employees_yeni():
    def __init__(self,FirstName, LastName, Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address

ali = Employees_yeni()
# TypeError: __init__() missing 3 required positional arguments: 'FirstName', 'LastName', and 'Address'

ali = Employees_yeni(a,b,c)     #NameError: name 'a' is not defined
# String olarak tanimlamamiz gerekiyor.

ali = Employees_yeni("a","b","c")
ali.Address

ali.FirstName

#Nesneye dayali programlama bolumunun sonuna geldik. 