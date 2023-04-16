def countBits(n):
    l=[]
    for i in range(n+1):
        val=str(bin(i))[2:]
        l.append(val.count(str('1')))
    return l
n=5
print(countBits(n))