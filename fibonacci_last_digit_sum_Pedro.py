PISANO = 60

def fibonacci_last_digit_sum(n):
    if n < 2:
        return n

    n %= PISANO

    results = [1, 1]
    for _ in range(n):  # 2
        results.append((results[-1] + results[-2]) % 10)  # 3

    return (results[-1] - 1) % 10

n = int(input())
print(fibonacci_last_digit_sum(n))

