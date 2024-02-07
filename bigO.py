# bigO NOTASYON ÖRNEKLERİ
    
# O(n^2)  
def bigon2(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i , j)


# O(log 2 tabanında n = logn)
import math
def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)


# O(n logn) -> dizme algoritmalarında sık kullanılır
def nlogn(n):
    lim = n
    while n > 1:
        n = math.floor(n/2) #hem log kullandık ikili arama
        for i in range(1,lim): #hem de for döngüsü kullandık brute force
            print(i)


# O(n!) -> en kötü notasyondur , faktöriyel hesaplaması yapıyoz diye o(n!) değildir n! kadar çağırıldığından öyle
def nfact(n):
    if n == 0 :
        print("1")
        return
    else :
        for i in range(0,n):
            print(i)
            nfact(n-1) #recursive