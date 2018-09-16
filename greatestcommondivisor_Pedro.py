# Uses python3
def gcd(a,b):
    if b == 0:
        return a
    c = a%b
    return gcd(b,c)


a, b = map(int, input().split())
print (gcd(a,b))

