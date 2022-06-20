# TUPLE (DEMET) OLUSTURMA : Bir veri yapisidir.

"""
1-Kapsayicidir.
2-Siralidir.
3-Degistirilemezler.

"""
t=("ali","veli",1,2,3.2,[1,2,3,4])

t2="ali","veli",1,2,3.2,[1,2,3,4]

t3=("eleman")
type(t3)

""" 
Yukarıdaki tuple tek elemanli olduğundan tipi string dönüyor.
Bunu engellemek için tek elemanlı tuplelarda , kullanırız.

"""
t4=("eleman",)
type(t4)

#Tuple eleman işlemleri

t5=("ali","veli",1,2,3,[1,2,3,4])
t5
#elemanlara erismek listelerdeki gibi
t5[0]
t5[1]
t5[0:3]

t5[2]=99
""" 
TypeError: 'tuple' object does not support item assignment
Tuple'lar neden değiştirilemez?
Bazen bazı durumlarda oluşturmuş olduğumuz veri yapısında 
değişiklikler meydana gelmesini isteyebiliriz. Bunu listeler 
ile yapıyoruz. Ama bazı durumlarda da ki onlar önemli durumlardır
veri yapilari sabit dursun ve değişiklik olup olmamasından endişe 
etmeyelim şeklinde yaklaşmamız gerekebilir. Bu tip ihtiyaçlar için
de tuple kullanırız.

"""

