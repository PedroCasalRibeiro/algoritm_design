# Uses python3
def calc_fibonacci(n):
    
    a,b = 1,1
    
    if n < 2:
        return n
    
    for i in range (n-1):
        a, b = b, a+b
        
    
    return a

n = int(input())
print(calc_fibonacci(n))

