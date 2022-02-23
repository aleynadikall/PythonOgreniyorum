# SETLERLE KLASIK KUME ISLEMLERI

# =============================================================================
# difference() ile iki kumenin farkini ya da "-" ifadesi
#intersection() iki kume kesisimi ya da "&" ifadesi
#union() iki kumenin birlesimi
#symmetric_difference() ikisinde de olmayanlar
# =============================================================================

# Setlerde Fark Islemleri - difference & symmetric_difference
set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)

set1-set2
set2-set1

# Setlerde Kesisim ve Birlesim Islemleri - intersection & union

set1.intersection(set2)
set2.intersection(set1)

kesisim = set1 & set2
kesisim

set1.union(set2)

birlesim = set2.union(set1)
birlesim

set1.intersection_update(set2)
set1

