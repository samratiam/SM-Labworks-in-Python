key=int(input("Enter number:\n"))
def countDigit(key):
    Count = 0
    while (key > 0):
        key = key // 10
        Count = Count + 1
    return Count
for i in range(10):
    l=countDigit(key)
    if(l>=4):
        key = key * key
        key = key//100
        m = key//10000
        key=key%(m*10000)
        print(key)
