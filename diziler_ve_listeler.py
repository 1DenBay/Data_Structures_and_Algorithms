import sys #sistem ile iletişim kurmayı sağlar
n = 10
myList = []

for i in range(n):
    myLenght = len(myList)
    myByte = sys.getsizeof(myList)
    print(f"uzunluk : {myLenght} , boyut : {myByte}")
    myList.append(n)
