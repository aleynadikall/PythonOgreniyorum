# HATALAR / ISTISNALAR (exceptions)

# Hata yonetimi programcilik anlaminda ele alinan onemli bir konudur.

# =============================================================================
# Hatalar kaba hatlariyla 3'e ayrilir:
#     1-Programcinin Hatalari : Basit hatalardir.
#     2-Program Hatalari : BUG'lar. Zor cozulurler.
#     3-İstisna Dedigimiz Hatalar
#
# =============================================================================

a = 10
b = 0
a/b  #ZeroDivisionError: division by zero

# ZeroDivisionError
# Bunu istisna olarak gormek icin assagidaki kodu yazmaliyiz.

try:
    print(a/b)      # Yapmaya calis olmazsa...
except ZeroDivisionError:
    print("Paydada sifir olmaz!")   # Bir istisna olarak gor.

# tip hatasi

c = 10
d = "2"
c / d      # TypeError: unsupported operand type(s) for /: 'int' and 'str'

# Bunu gormezden gelmesi icin assagidaki kodu yazariz.

try:
    print(c/d)
except TypeError:
    print("Sayi ve string problemi")

e = 10
f = 2

try:
    print(e/f)
except TypeError:
    print("Sayi ve string problemi")

# Kod akisinin bozulmamasi icin gormezden gelmek onemlidir.

def yap(x,y,z):
    try:
        print(x/y*z)
    except ZeroDivisionError:
        print("gecersiz islem")
 
yap(1,2,0)
