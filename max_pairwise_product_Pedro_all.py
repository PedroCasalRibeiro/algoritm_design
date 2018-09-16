def maxproductnaive(a):
    result = 0
    for i in range (0,len(a)):
        for j in range (i+1, len(a)):
            if i!=j and a[i]*a[j] > result:
                result = a[i]*a[j]
    return result


def maxproductfast(a):
    index1 = 0
    for i in range(0,len(a)):
        if a[i] > a[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for f in range(0,len(a)):
        if f != index1 and a[f] > a[index2]:
            index2 = f
    return a[index1]*a[index2]


def maxproductsort(a):
    a.sort(reverse=True)
    return a[0]*a[1]

#Stress test
import random
def stresstestmax(N,M):
    while True:
        a = []
        n = random.randint(2,N)
        for i in range(n):
            a.append(random.randint(1,M))
        print (a)
        result1 = maxproductnaive(a)
        result2 = maxproductfast(a)
        result3 = maxproductsort(a)
        if result1 == result2 == result3:
            print("OK", result1)
        else:
            print("Wrong answer", result1, result2, result3)
    return

