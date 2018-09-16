def gcd(a,b):
    if b == 0:
        return a
    c = a%b
    return gcd(b,c)


def lcm(a,b):
    return (a*b)//gcd(a,b)

a, b = map(int, input().split())
print (lcm(a,b))

