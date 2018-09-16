# Uses python3

def calc_fibonaccilast(n):
    result = []
    a,b = 1,1

    if n <= 1:
        return n
    
    for i in range (n-1):
        a, b = b, (a+b)%10
    
    return a

n = int(input())
print(calc_fibonaccilast(n))