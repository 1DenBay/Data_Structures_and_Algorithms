myList = [1,2,3,4]

def solution(): # Time : bigO(n) - Space : bigO(n)
    hashSet = set() #benzersiz küme oluşturduk
    for num in myList: #listedeki elemanları tek tek kontrol etmek için döngü
        if num in hashSet: #elemanları hashsete atmadan önce kontrol yapar eğer saten aynı elemandan eklenmişse true döndürür
            return True    #yani elemandan bir tane daha olduğu anlaşılır
        hashSet.add(num) #listedeki elemanları tek tek hashsete atar
    return False #tüm elemanlar sorunsuz hashsete eklenmişse tekrar eden yok demektir false döndürür


def solution2(): # Time : bigO(1) - Space : bigO(1)
    return len(myList) != len(set(myList)) #direkt listeyi hashe atıp iki listenin eleman sayısını kontrol eder eşitse saten otomatik true değilse false döndürür