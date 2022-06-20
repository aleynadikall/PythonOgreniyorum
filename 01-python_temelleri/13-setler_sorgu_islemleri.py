#Setlerde sorgu islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

# =============================================================================
# İki kümenin bos olup olmadiginin sorgulanmasi 
# =============================================================================

set1.isdisjoint(set2)       
#iki kumenin kesisimi boz mu sorusuna cevap verecek-False döndü.s


# =============================================================================
# Bir kumenin butun elemanlarinin baska bir kume icerisinde
# yer alip almadigi
# =============================================================================

set1.issubset(set2)     #Set1 set2 nin alt kümesi midir?-true döndü


#Bir kumenin bir kumeyi kapsayip kapsamadigini sorgulayalim.

set2.issuperset(set1)       #true döner
