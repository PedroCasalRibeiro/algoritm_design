def Huge_Fib(n,m):

    a, b, c = 1, 1, 0  
    for i in bin(n)[3:]:
        calc = (b*b) % m
        a, b, c = (a*a+calc) % m, ((a+c)*b) % m, (calc+c*c) % m
        if i == '1': a, b, c = (a+b) % m, a, b
    print (b)  

n,m = map(int, input().split())
Huge_Fib(n,m)


# Uses python3
from functools import lru_cache

@lru_cache(maxsize=None)
def calc_fibonacci(n,m):
    
    if n < 2:
        return n
    
    elif n % 2:
        a = calc_fibonacci(n // 2, m)
        b = calc_fibonacci(n // 2 + 1, m)
        return (a * a + b * b) % m
    else:
        a = calc_fibonacci(n // 2 - 1, m)
        b = calc_fibonacci(n // 2, m)
        return (2 * a + b) * b % m

n, m = map(int, input().split())
print (calc_fibonacci(n,m))

